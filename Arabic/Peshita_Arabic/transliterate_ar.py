#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deterministic IPA -> Arabic transliterator for the Peshitta corpus.

Four tiers:

    SCHOLARLY    Latin, byte-for-byte identical to the English Peshitta transducer.
    PRETTY       Latin, byte-for-byte identical to the English Peshitta transducer.
    VOCALIZED    Arabic abjad with full harakat (fatḥa/kasra/ḍamma), sukun on codas,
                 shadda on geminates, matres lectionis (alif/wāw/yāʾ) for long vowels.
    UNVOCALIZED  VOCALIZED with the harakat (U+064B..U+0652) and tatweel stripped.

WHY ARABIC IS THE MOST FAITHFUL READER TIER IN THE PROJECT
----------------------------------------------------------
Arabic is a SEMITIC SIBLING of the source (Syriac / Aramaic), so the reader tier
here is near-reversible -- the inverse of the lossy CJK collapse.  About 25 of 28
consonants map 1:1, including the pharyngeals (ħ->ح, ʕ->ع), the emphatics
(tˤ->ط, sˤ->ص), the interdentals (θ->ث, ð->ذ), and x->خ, ɣ->غ, q->ق, ʃ->ش, ʔ->ء.

DOCUMENTED LIMITATIONS (only FIVE merges -- tiny next to CJK)
------------------------------------------------------------
  1. p / b   -> ب   (native Arabic lacks /p/; p merges to b)
  2. v / f   -> ف   (native Arabic lacks /v/; v merges to f)            [consonant]
  3. ɡ       -> ج   (realization only; reversible in-corpus, the only ج source)
  4. e -> i        (vowel quality; matches attested Western Syriac vocalism)
  5. o -> u        (vowel quality; matches attested Western Syriac vocalism)
Vowel LENGTH is preserved via matres lectionis, so only vowel QUALITY (3 of the
above) and the two consonant merges are lossy.  Everything else round-trips.

RTL / BIDI POLICY
-----------------
The Arabic body is emitted in LOGICAL (reading) order only -- NO reordering, NO
Arabic presentation forms (U+FE70..U+FEFF), NO tatweel padding.  The renderer is
responsible for RTL layout and contextual shaping.  transliterate_line() keeps the
'<verse#>\\t' gutter intact and wraps ONLY the Vocalized / Unvocalized body in bidi
isolates RLI (U+2067) ... PDI (U+2069) so the LTR verse-number gutter and the RTL
body never scramble.  Scholarly / Pretty are Latin and are NOT wrapped -- preserving
byte-identity with the English Peshitta.

PATHS
-----
This module is self-contained and resolves the repository root from its OWN
__file__ -- it contains no absolute paths.

CLI:
    transliterate_ar.py --selftest        run embedded gold cases; PASS/FAIL per (ref,tier)
    transliterate_ar.py --coverage        scan every *_ipa.txt: report unmapped IPA +
                                          any non-Arabic-block char in the Vocalized tier
    transliterate_ar.py --build           transliterate the whole corpus into the 4 tier trees
    transliterate_ar.py --write-mapping   (re)write transliteration_mapping_ar.json

Public API:
    transliterate(text, tier) -> str
    transliterate_line(line, tier) -> str

Author: Shin
"""

import os
import sys
import json
import argparse

# ===========================================================================
# Paths (resolved from THIS file -- no absolute paths embedded)
# ===========================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
IPA_ROOT = os.path.join(REPO_ROOT, "IPA", "Peshitta")
ARABIC_ROOT = os.path.join(REPO_ROOT, "Arabic", "Peshita_Arabic")
MAPPING_JSON = os.path.join(SCRIPT_DIR, "transliteration_mapping_ar.json")

# ===========================================================================
# Unicode codepoints used in the SPEC (named for clarity)
# ===========================================================================
SUPER_RHOTIC = "ˤ"        # ˤ  modifier letter small reversed glottal stop (emphatic marker)
LENGTH_MARK = "ː"         # ː  modifier letter triangular colon (long vowel)
COMBINING_DOT_BELOW = "̣" # ̣  combining dot below (generic emphatic fallback, Latin tiers)

# IPA source symbols
G_VOICED = "ɡ"  # ɡ  latin small letter script g
V_LABIO = "v"
F_LABIO = "f"
SH = "ʃ"        # ʃ
THETA = "θ"     # θ
ETH = "ð"       # ð
X_VELAR = "x"
GAMMA = "ɣ"     # ɣ
HBAR = "ħ"      # ħ
J_PALATAL = "j"
ALAPH = "ʔ"     # ʔ  glottal stop
AYIN = "ʕ"      # ʕ  voiced pharyngeal
A_FRONT = "a"
ALPHA = "ɑ"     # ɑ  open back unrounded

VOWELS = {A_FRONT, ALPHA, "e", "i", "o", "u"}

# Bidi isolates wrapping the Arabic body in transliterate_line()
RLI = "⁧"  # RIGHT-TO-LEFT ISOLATE
PDI = "⁩"  # POP DIRECTIONAL ISOLATE

# Arabic harakat / marks stripped for the UNVOCALIZED tier (U+064B..U+0652 + tatweel)
TATWEEL = "ـ"
HARAKAT = {
    "ً",  # fathatan
    "ٌ",  # dammatan
    "ٍ",  # kasratan
    "َ",  # fatha
    "ُ",  # damma
    "ِ",  # kasra
    "ّ",  # shadda
    "ْ",  # sukun
    TATWEEL,
}

# ===========================================================================
# Tier names
# ===========================================================================
SCHOLARLY = "scholarly"
PRETTY = "pretty"
VOCALIZED = "vocalized"
UNVOCALIZED = "unvocalized"
TIERS = (SCHOLARLY, PRETTY, VOCALIZED, UNVOCALIZED)

TIER_DIR_NAME = {
    SCHOLARLY: "Scholarly",
    PRETTY: "Pretty",
    VOCALIZED: "Vocalized",
    UNVOCALIZED: "Unvocalized",
}

# ===========================================================================
# SCHOLARLY / PRETTY tables  (VERBATIM from the English Peshitta transducer)
# ---------------------------------------------------------------------------
# Tuple order = (scholarly, pretty).  These reproduce English/Peshita_English/
# transliterate.py exactly for the two Latin tiers so the Arabic Scholarly /
# Pretty outputs are byte-for-byte identical to English.
# ===========================================================================
SP_CONSONANTS = {
    "b":       ("b", "b"),
    G_VOICED:  ("g", "g"),
    "d":       ("d", "d"),
    "h":       ("h", "h"),
    "w":       ("w", "w"),
    "z":       ("z", "z"),
    "k":       ("k", "k"),
    "l":       ("l", "l"),
    "m":       ("m", "m"),
    "n":       ("n", "n"),
    "s":       ("s", "s"),
    "p":       ("p", "p"),
    "q":       ("q", "q"),
    "r":       ("r", "r"),
    "t":       ("t", "t"),
    F_LABIO:   ("f", "f"),
    V_LABIO:   ("ḇ", "v"),   # ḇ | v
    SH:        ("š", "sh"),  # š | sh
    THETA:     ("ṯ", "th"),  # ṯ | th
    ETH:       ("ḏ", "dh"),  # ḏ | dh
    X_VELAR:   ("ḵ", "kh"),  # ḵ | kh
    GAMMA:     ("ḡ", "gh"),  # ḡ | gh
    HBAR:      ("ḥ", "ḥ"),  # ḥ | ḥ
    J_PALATAL: ("y", "y"),
}

SP_SHORT_VOWELS = {
    A_FRONT: ("a", "a"),
    ALPHA:   ("a", "a"),
    "e":     ("e", "e"),
    "i":     ("i", "i"),
    "o":     ("o", "o"),
    "u":     ("u", "u"),
}

SP_LONG_VOWELS = {
    A_FRONT: ("ā", "ā"),  # ā | ā
    ALPHA:   ("ā", "ā"),  # ā | ā
    "e":     ("ē", "ē"),  # ē | ē
    "i":     ("ī", "ī"),  # ī | ī
    "o":     ("ō", "ō"),  # ō | ō
    "u":     ("ū", "ū"),  # ū | ū
}
SP_LONG_VOWEL_BASES = set(SP_LONG_VOWELS.keys())

SP_EMPHATICS_EXPLICIT = {
    "t": ("ṭ", "ṭ"),  # ṭ | ṭ
    "s": ("ṣ", "ṣ"),  # ṣ | ṣ
}

HYPHEN = "-"
SPACE = " "

_SP_IDX = {SCHOLARLY: 0, PRETTY: 1}


def _sp_consonant(ch, tier):
    """Return the Latin tier rendering of a base consonant char, or None."""
    entry = SP_CONSONANTS.get(ch)
    if entry is None:
        return None
    return entry[_SP_IDX[tier]]


def _sp_segment_token(token):
    """Segment a token for the Latin tiers (longest-match consonant+ˤ, vowel+ː)."""
    segs = []
    i = 0
    n = len(token)
    while i < n:
        ch = token[i]
        nxt = token[i + 1] if i + 1 < n else None
        if nxt == SUPER_RHOTIC and ch in SP_CONSONANTS:
            segs.append(ch + SUPER_RHOTIC)
            i += 2
            continue
        if nxt == LENGTH_MARK and ch in SP_LONG_VOWEL_BASES:
            segs.append(ch + LENGTH_MARK)
            i += 2
            continue
        segs.append(ch)
        i += 1
    return segs


def _sp_render_segment(seg, tier, is_word_initial, unmapped):
    """Render one segment for a Latin tier (scholarly / pretty)."""
    idx = _SP_IDX[tier]

    # Emphatic segment (consonant + ˤ)
    if len(seg) == 2 and seg[1] == SUPER_RHOTIC:
        base = seg[0]
        explicit = SP_EMPHATICS_EXPLICIT.get(base)
        if explicit is not None:
            return explicit[idx]
        base_render = _sp_consonant(base, tier)
        if base_render is None:
            unmapped.add(base)
            base_render = base
        # scholarly / pretty: tier(C) + combining dot below
        return base_render + COMBINING_DOT_BELOW

    # Long-vowel segment (V + ː)
    if len(seg) == 2 and seg[1] == LENGTH_MARK:
        entry = SP_LONG_VOWELS.get(seg[0])
        if entry is not None:
            return entry[idx]
        unmapped.add(seg[0])
        return seg

    ch = seg

    sv = SP_SHORT_VOWELS.get(ch)
    if sv is not None:
        return sv[idx]

    cons = _sp_consonant(ch, tier)
    if cons is not None:
        return cons

    if ch == ALAPH:  # ʔ
        if tier == SCHOLARLY:
            return "ʾ"  # ʾ
        return "" if is_word_initial else "'"
    if ch == AYIN:  # ʕ
        return "ʿ"  # ʿ  (scholarly and pretty)

    if ch == HYPHEN:
        return "-"
    if ch == SPACE:
        return " "

    unmapped.add(ch)
    return ch


def _sp_transliterate(text, tier, unmapped):
    """Latin transliteration (scholarly / pretty), splitting on ASCII space."""
    out_parts = []
    tokens = text.split(" ")
    for ti, token in enumerate(tokens):
        if ti > 0:
            out_parts.append(" ")
        if token == "":
            continue
        for si, seg in enumerate(_sp_segment_token(token)):
            out_parts.append(_sp_render_segment(seg, tier, si == 0, unmapped))
    return "".join(out_parts)


# ===========================================================================
# ARABIC abjad tables  (native gap policy: v->ف, p->ب, ɡ->ج)
# ===========================================================================
AR_CONSONANTS = {
    ALAPH:    "ء",  # ء  hamza (bare hamza for ʔ everywhere, deterministic)
    "b":      "ب",  # ب
    "t":      "ت",  # ت
    THETA:    "ث",  # ث
    "d":      "د",  # د
    ETH:      "ذ",  # ذ
    "r":      "ر",  # ر
    "z":      "ز",  # ز
    "s":      "س",  # س
    SH:       "ش",  # ش
    AYIN:     "ع",  # ع
    GAMMA:    "غ",  # غ
    "f":      "ف",  # ف
    "q":      "ق",  # ق
    "k":      "ك",  # ك
    "l":      "ل",  # ل
    "m":      "م",  # م
    "n":      "ن",  # ن
    "h":      "ه",  # ه
    "w":      "و",  # و
    J_PALATAL:"ي",  # ي
    HBAR:     "ح",  # ح
    X_VELAR:  "خ",  # خ
    # --- native gap policy (the consonant merges) ---
    V_LABIO:  "ف",  # v -> ف  (merges with f)
    "p":      "ب",  # p -> ب  (merges with b)
    G_VOICED: "ج",  # ɡ -> ج  (sole ج source; reversible in-corpus)
}
AR_EMPHATICS = {
    "t": "ط",  # tˤ -> ط
    "s": "ص",  # sˤ -> ص
}

# Harakat / matres lectionis
FATHA = "َ"
KASRA = "ِ"
DAMMA = "ُ"
SUKUN = "ْ"
SHADDA = "ّ"
ALIF = "ا"
ALIF_MADDA = "آ"  # آ  U+0622 alif with madda above (= carrier alif + fatḥa + alif mater)
WAW = "و"
YA = "ي"

# vowel -> (short haraka, long mater letter).  e/i share kasra; o/u share damma.
AR_VOWELS = {
    A_FRONT: (FATHA, ALIF),
    ALPHA:   (FATHA, ALIF),
    "e":     (KASRA, YA),
    "i":     (KASRA, YA),
    "o":     (DAMMA, WAW),
    "u":     (DAMMA, WAW),
}


def _seg_base(seg):
    """Return the base char of a (possibly 2-char) segment."""
    if len(seg) == 2 and seg[1] in (SUPER_RHOTIC, LENGTH_MARK):
        return seg[0]
    return seg


def _is_vowel_seg(seg):
    return _seg_base(seg) in VOWELS


def _segment_token(token):
    """Segment a token for the Arabic tiers (consonant+ˤ, vowel+ː, else single)."""
    segs = []
    i = 0
    n = len(token)
    while i < n:
        ch = token[i]
        nxt = token[i + 1] if i + 1 < n else None
        if nxt == SUPER_RHOTIC:
            segs.append(ch + SUPER_RHOTIC)
            i += 2
            continue
        if nxt == LENGTH_MARK and ch in VOWELS:
            segs.append(ch + LENGTH_MARK)
            i += 2
            continue
        segs.append(ch)
        i += 1
    return segs


def _ar_consonant_letter(seg, unmapped):
    """Return the Arabic letter for a consonant segment, or None if not a consonant."""
    if len(seg) == 2 and seg[1] == SUPER_RHOTIC:
        base = seg[0]
        if base in AR_EMPHATICS:
            return AR_EMPHATICS[base]
        if base in AR_CONSONANTS:
            return AR_CONSONANTS[base]
        unmapped.add(base)
        return None
    if seg in AR_CONSONANTS:
        return AR_CONSONANTS[seg]
    return None


def _vowel_part(vseg):
    """Return the haraka (+ mater for a long vowel) for a vowel segment."""
    base = _seg_base(vseg)
    haraka, mater = AR_VOWELS[base]
    if len(vseg) == 2 and vseg[1] == LENGTH_MARK:
        return haraka + mater
    return haraka


def _ar_token(token, unmapped):
    """Transliterate one token into vocalized Arabic (logical order)."""
    segs = _segment_token(token)
    out = []
    i = 0
    n = len(segs)
    while i < n:
        s = segs[i]

        if s == HYPHEN:
            out.append("-")
            i += 1
            continue

        # Bare vowel with no consonant carrier: seat it on a carrier alif.
        # A LONG a/ɑ would otherwise be carrier-alif + fatḥa + alif-mater, i.e. two
        # consecutive alifs (malformed). Standard Arabic writes that sequence as a
        # single alif-madda آ (U+0622), so collapse it.
        if _is_vowel_seg(s):
            base = _seg_base(s)
            haraka, mater = AR_VOWELS[base]
            is_long = len(s) == 2 and s[1] == LENGTH_MARK
            if is_long and mater == ALIF:
                out.append(ALIF_MADDA)
                i += 1
                continue
            tail = mater if is_long else ""
            out.append(ALIF + haraka + tail)
            i += 1
            continue

        letter = _ar_consonant_letter(s, unmapped)
        if letter is None:
            if s not in (SUPER_RHOTIC, LENGTH_MARK):
                unmapped.add(s)
            i += 1
            continue

        nxt = segs[i + 1] if i + 1 < n else None

        # Geminate: the next segment is the SAME consonant with no vowel between
        # them -> fuse to one letter + shadda (e.g. ...elijjawn -> ي + shadda).
        is_geminate = (
            nxt is not None
            and not _is_vowel_seg(nxt)
            and nxt != HYPHEN
            and _ar_consonant_letter(nxt, set()) == letter
        )
        if is_geminate:
            after = segs[i + 2] if i + 2 < n else None
            if after is not None and _is_vowel_seg(after):
                out.append(letter + SHADDA + _vowel_part(after))
                i += 3
                continue
            out.append(letter + SHADDA + SUKUN)
            i += 2
            continue

        # Consonant + following vowel
        if nxt is not None and _is_vowel_seg(nxt):
            out.append(letter + _vowel_part(nxt))
            i += 2
            continue

        # Coda consonant (no following vowel) -> sukun
        out.append(letter + SUKUN)
        i += 1

    return "".join(out)


def _vocalized(text, unmapped):
    """Full vocalized Arabic for a whole verse text (space-delimited tokens)."""
    return " ".join(_ar_token(t, unmapped) if t else "" for t in text.split(" "))


def _strip_harakat(s):
    """Remove harakat (U+064B..U+0652) and tatweel for the UNVOCALIZED tier."""
    return "".join(c for c in s if c not in HARAKAT)


# ===========================================================================
# Public API
# ===========================================================================
def transliterate(text, tier, unmapped=None):
    """
    Transliterate IPA `text` for the given `tier`.

    Tiers:
        scholarly    Latin (byte-identical to English Peshitta)
        pretty       Latin (byte-identical to English Peshitta)
        vocalized    Arabic abjad + full harakat
        unvocalized  vocalized with harakat stripped

    If `unmapped` (a set) is supplied, any unmapped IPA char encountered is added
    to it.  Latin tiers pass unmapped chars through unchanged; Arabic tiers drop
    them (after recording).
    """
    if tier not in TIERS:
        raise ValueError("Unknown tier: %r (expected one of %r)" % (tier, TIERS))
    if unmapped is None:
        unmapped = set()

    if tier in (SCHOLARLY, PRETTY):
        return _sp_transliterate(text, tier, unmapped)
    if tier == VOCALIZED:
        return _vocalized(text, unmapped)
    # UNVOCALIZED
    return _strip_harakat(_vocalized(text, unmapped))


def transliterate_line(line, tier, unmapped=None):
    """
    Transliterate a single corpus line of the form '<verse#>\\t<text>'.

    Keeps the '<verse#>\\t' prefix verbatim; only the text after the FIRST tab is
    transliterated.  Lines without a tab are returned unchanged.  The trailing
    newline (if any) is preserved.

    For the Arabic tiers (vocalized / unvocalized) the transliterated BODY is
    wrapped in bidi isolates RLI (U+2067) ... PDI (U+2069) so the LTR verse-number
    gutter and the RTL body never scramble.  Scholarly / Pretty are Latin and are
    NOT wrapped (preserving byte-identity with English).
    """
    newline = ""
    body = line
    if body.endswith("\r\n"):
        newline = "\r\n"
        body = body[:-2]
    elif body.endswith("\n"):
        newline = "\n"
        body = body[:-1]

    if "\t" not in body:
        return line  # unchanged (no verse text to transliterate)

    prefix, text = body.split("\t", 1)
    rendered = transliterate(text, tier, unmapped)
    if tier in (VOCALIZED, UNVOCALIZED):
        rendered = RLI + rendered + PDI
    return prefix + "\t" + rendered + newline


# ===========================================================================
# Machine-readable mapping export
# ===========================================================================
def build_mapping_dict():
    """Build the JSON-serializable mapping table (IPA->Arabic + rules + limits)."""
    consonants = {
        ipa: letter for ipa, letter in AR_CONSONANTS.items()
    }
    emphatics = {ipa + SUPER_RHOTIC: letter for ipa, letter in AR_EMPHATICS.items()}
    short_vowels = {ipa: AR_VOWELS[ipa][0] for ipa in AR_VOWELS}
    long_vowels = {
        ipa + LENGTH_MARK: AR_VOWELS[ipa][0] + AR_VOWELS[ipa][1] for ipa in AR_VOWELS
    }
    sp_consonants = {
        ipa: {SCHOLARLY: v[0], PRETTY: v[1]} for ipa, v in SP_CONSONANTS.items()
    }
    sp_short_vowels = {
        ipa: {SCHOLARLY: v[0], PRETTY: v[1]} for ipa, v in SP_SHORT_VOWELS.items()
    }
    sp_long_vowels = {
        ipa: {SCHOLARLY: v[0], PRETTY: v[1]} for ipa, v in SP_LONG_VOWELS.items()
    }
    sp_emphatics = {
        ipa: {SCHOLARLY: v[0], PRETTY: v[1]} for ipa, v in SP_EMPHATICS_EXPLICIT.items()
    }

    return {
        "meta": {
            "description": "Deterministic IPA->Arabic mapping for the Peshitta corpus.",
            "tiers": list(TIERS),
            "note": (
                "transliterate_ar.py is authoritative; this file mirrors its "
                "hard-coded tables. Scholarly/Pretty are byte-identical to the "
                "English Peshitta transducer."
            ),
            "author": "Shin",
        },
        "unicode": {
            "emphatic_marker": SUPER_RHOTIC,
            "length_mark": LENGTH_MARK,
            "alaph": ALAPH,
            "ayin": AYIN,
            "hyphen": HYPHEN,
            "harakat": {
                "fatha": FATHA, "kasra": KASRA, "damma": DAMMA,
                "sukun": SUKUN, "shadda": SHADDA,
            },
            "matres": {"alif": ALIF, "alif_madda": ALIF_MADDA, "waw": WAW, "ya": YA},
            "bidi_isolates": {"RLI": RLI, "PDI": PDI},
        },
        "segmentation": [
            "Split on ASCII space ' ' only; spaces are preserved verbatim.",
            "Within each token, left-to-right longest match:",
            "  1. consonant + \\u02E4 (ˤ) -> emphatic segment (2 chars)",
            "  2. vowel (a ɑ e i o u) + \\u02D0 (ː) -> long-vowel segment (2 chars)",
            "  3. otherwise single char",
        ],
        "latin_tiers (scholarly/pretty)": {
            "note": "Verbatim from English/Peshita_English/transliterate.py.",
            "consonants": sp_consonants,
            "short_vowels": sp_short_vowels,
            "long_vowels": sp_long_vowels,
            "emphatics_explicit": sp_emphatics,
            "alaph": {
                "symbol": ALAPH,
                SCHOLARLY: "always \\u02BE (ʾ)",
                PRETTY: "word-initial -> '' (drop); else -> \"'\"",
            },
            "ayin": {"symbol": AYIN, SCHOLARLY: "\\u02BF (ʿ)", PRETTY: "\\u02BF (ʿ)"},
            "emphatic_fallback": "tier(C) + \\u0323 (combining dot below)",
        },
        "arabic_tiers (vocalized/unvocalized)": {
            "consonants": consonants,
            "emphatics": emphatics,
            "short_vowels": short_vowels,
            "long_vowels_matres": long_vowels,
            "rules": {
                "hamza": "ʔ -> \\u0621 (bare hamza ء) everywhere (deterministic).",
                "sukun": "A coda consonant (no following vowel) takes sukun \\u0652.",
                "shadda": (
                    "Two adjacent identical consonants with no vowel between fuse "
                    "to one letter + shadda \\u0651 (the geminate carries the vowel "
                    "of the segment after the twin, e.g. jj in ...elijjawn -> ي+shadda)."
                ),
                "bare_initial_vowel": (
                    "A word-initial vowel with no consonant carrier is seated on a "
                    "carrier alif \\u0627. A long a/ɑ (which would otherwise be "
                    "carrier-alif + fatḥa + alif-mater = two consecutive alifs) is "
                    "written as a single alif-madda \\u0622 (آ)."
                ),
                "long_vowel": (
                    "Long vowel = haraka + mater lectionis (a/ɑ->alif, e/i->ya, "
                    "o/u->waw); vowel LENGTH is thereby preserved."
                ),
                "unvocalized": (
                    "VOCALIZED with harakat (\\u064B..\\u0652) and tatweel "
                    "(\\u0640) stripped."
                ),
            },
            "rtl_policy": (
                "Emit LOGICAL (reading) order only: NO reordering, NO presentation "
                "forms (\\uFE70..\\uFEFF), NO tatweel. The renderer handles RTL + "
                "contextual shaping. transliterate_line() wraps ONLY the Arabic body "
                "in bidi isolates RLI (\\u2067) ... PDI (\\u2069); the Latin "
                "scholarly/pretty bodies are NOT wrapped."
            ),
        },
        "documented_limitations": {
            "summary": (
                "Arabic is a Semitic sibling of the source, so the reader tier is "
                "near-reversible -- the inverse of the lossy CJK collapse. Only FIVE "
                "merges, and vowel LENGTH is preserved via matres."
            ),
            "merges": [
                {"type": "consonant", "ipa": "p", "arabic": AR_CONSONANTS["p"],
                 "note": "p merges with b (native Arabic lacks /p/)."},
                {"type": "consonant", "ipa": "v", "arabic": AR_CONSONANTS[V_LABIO],
                 "note": "v merges with f (native Arabic lacks /v/)."},
                {"type": "realization", "ipa": G_VOICED, "arabic": AR_CONSONANTS[G_VOICED],
                 "note": "ɡ -> ج; realization only, reversible in-corpus (sole ج source)."},
                {"type": "vowel_quality", "ipa": "e->i", "arabic": KASRA,
                 "note": "e merges with i; matches attested Western Syriac vocalism."},
                {"type": "vowel_quality", "ipa": "o->u", "arabic": DAMMA,
                 "note": "o merges with u; matches attested Western Syriac vocalism."},
            ],
            "preserved": "Vowel LENGTH (via matres), pharyngeals, emphatics, interdentals.",
        },
    }


def write_mapping_json(path=MAPPING_JSON):
    data = build_mapping_dict()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path


# ===========================================================================
# Gold cases (regression lock)
# ---------------------------------------------------------------------------
# scholarly / pretty = English Peshitta gold (byte-identical).
# vocalized / unvocalized = computed from THIS finalized code, pasted as the lock.
# ===========================================================================
GOLD_CASES = [
    {
        "ref": "John 1:1",
        "ipa": "breːʃiːθ ʔiːθawj wɑː melθɑː whuː melθɑː ʔiːθawj wɑː lwɑːθ ʔɑːlɑːhɑː waʔlɑːhɑː ʔiːθawj wɑː huː melθɑː",
        "scholarly": "brēšīṯ ʾīṯawy wā melṯā whū melṯā ʾīṯawy wā lwāṯ ʾālāhā waʾlāhā ʾīṯawy wā hū melṯā",
        "pretty": "brēshīth īthawy wā melthā whū melthā īthawy wā lwāth ālāhā wa'lāhā īthawy wā hū melthā",
        "vocalized": "بْرِيشِيثْ ءِيثَوْيْ وَا مِلْثَا وْهُو مِلْثَا ءِيثَوْيْ وَا لْوَاثْ ءَالَاهَا وَءْلَاهَا ءِيثَوْيْ وَا هُو مِلْثَا",
        "unvocalized": "بريشيث ءيثوي وا ملثا وهو ملثا ءيثوي وا لواث ءالاها وءلاها ءيثوي وا هو ملثا",
    },
    {
        "ref": "John 1:2",
        "ipa": "hɑːnɑː ʔiːθawj wɑː breːʃiːθ lwɑːθ ʔɑːlɑːhɑː",
        "scholarly": "hānā ʾīṯawy wā brēšīṯ lwāṯ ʾālāhā",
        "pretty": "hānā īthawy wā brēshīth lwāth ālāhā",
        "vocalized": "هَانَا ءِيثَوْيْ وَا بْرِيشِيثْ لْوَاثْ ءَالَاهَا",
        "unvocalized": "هانا ءيثوي وا بريشيث لواث ءالاها",
    },
    {
        "ref": "John 1:3",
        "ipa": "kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː",
        "scholarly": "kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā",
        "pretty": "kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā",
        "vocalized": "كُلْ بْءِيْذِهْ هْوَا وْفِلْعَاذَوْيْ ءَافْلَا حْذَا هْوَاثْ مِدِمْ دَهْوَا",
        "unvocalized": "كل بءيذه هوا وفلعاذوي ءافلا حذا هواث مدم دهوا",
    },
    {
        "ref": "Matthew 1:1",
        "ipa": "kθɑːvɑː diːliːðuːθeh djeʃuːʕ mʃiːħɑː breh dðawiːð breh dʔavrɑːhɑːm",
        "scholarly": "kṯāḇā dīlīḏūṯeh dyešūʿ mšīḥā breh dḏawīḏ breh dʾaḇrāhām",
        "pretty": "kthāvā dīlīdhūtheh dyeshūʿ mshīḥā breh ddhawīdh breh d'avrāhām",
        "vocalized": "كْثَافَا دِيلِيذُوثِهْ دْيِشُوعْ مْشِيحَا بْرِهْ دْذَوِيذْ بْرِهْ دْءَفْرَاهَامْ",
        "unvocalized": "كثافا ديليذوثه ديشوع مشيحا بره دذويذ بره دءفراهام",
    },
    {
        "ref": "Romans 1:1",
        "ipa": "pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː",
        "scholarly": "pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā",
        "pretty": "pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā",
        "vocalized": "بَوْلَاوْسْ عَفْدَا دْيِشُوعْ مْشِيحَا قَرْيَا وَشْلِيحَا دْءِثْبْرِشْ لِءْوَنْجِلِيَّاوْنْ دْءَالَاهَا",
        "unvocalized": "بولاوس عفدا ديشوع مشيحا قريا وشليحا دءثبرش لءونجلياون دءالاها",
    },
    {
        "ref": "Matthew 27:16 (Barabbas)",
        "ipa": "dmeθqre bar-ʔaba lvar-ʔaba lvar-ʔava",
        "scholarly": "dmeṯqre bar-ʾaba lḇar-ʾaba lḇar-ʾaḇa",
        "pretty": "dmethqre bar-'aba lvar-'aba lvar-'ava",
        "vocalized": "دْمِثْقْرِ بَرْ-ءَبَ لْفَرْ-ءَبَ لْفَرْ-ءَفَ",
        "unvocalized": "دمثقر بر-ءب لفر-ءب لفر-ءف",
    },
]


def run_selftest():
    """Run gold cases; print PASS/FAIL per (ref, tier) with diffs. Return (all_pass, mismatches)."""
    all_pass = True
    mismatches = []
    for case in GOLD_CASES:
        ref = case["ref"]
        for tier in TIERS:
            expected = case[tier]
            got = transliterate(case["ipa"], tier)
            if got == expected:
                print("PASS  %-26s %-11s" % (ref, tier))
            else:
                all_pass = False
                print("FAIL  %-26s %-11s" % (ref, tier))
                print("        expected: %r" % expected)
                print("        got:      %r" % got)
                diff_at = None
                for k in range(min(len(expected), len(got))):
                    if expected[k] != got[k]:
                        diff_at = k
                        break
                if diff_at is None and len(expected) != len(got):
                    diff_at = min(len(expected), len(got))
                if diff_at is not None:
                    e = expected[diff_at] if diff_at < len(expected) else "<EOL>"
                    g = got[diff_at] if diff_at < len(got) else "<EOL>"
                    print("        first diff at index %d: expected %r got %r" % (diff_at, e, g))
                mismatches.append({"ref": ref, "tier": tier, "expected": expected, "got": got})
    print("")
    print("ALL PASS" if all_pass else "SOME FAILED")
    return all_pass, mismatches


# ===========================================================================
# Coverage
# ===========================================================================
def iter_ipa_files(root=IPA_ROOT):
    for dirpath, _dirs, files in os.walk(root):
        for fn in sorted(files):
            if fn.endswith("_ipa.txt"):
                yield os.path.join(dirpath, fn)


def _is_arabic_block(ch):
    """True for the Arabic Unicode block (U+0600..U+06FF)."""
    return 0x0600 <= ord(ch) <= 0x06FF


def run_coverage(root=IPA_ROOT):
    """
    Scan every *_ipa.txt under `root`; transliterate verse text in all four tiers,
    collecting (a) any unmapped IPA segment and (b) any non-Arabic-block char that
    leaks into the Vocalized tier (space and hyphen excepted).
    Returns (unmapped_set, non_arabic_set).
    """
    unmapped = set()
    non_arabic = set()
    n_files = 0
    for path in iter_ipa_files(root):
        n_files += 1
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if "\t" not in line:
                    continue
                text = line.rstrip("\r\n").split("\t", 1)[1]
                for tier in TIERS:
                    transliterate(text, tier, unmapped)
                voc = transliterate(text, VOCALIZED, unmapped)
                for ch in voc:
                    if ch in (" ", "-"):
                        continue
                    if not _is_arabic_block(ch):
                        non_arabic.add(ch)
    print("Scanned %d IPA file(s) under %s" % (n_files, os.path.relpath(root, REPO_ROOT)))
    print("  unmapped IPA segments              :",
          sorted(unmapped) if unmapped else "none")
    if non_arabic:
        print("  non-Arabic-block chars in Vocalized:")
        for ch in sorted(non_arabic):
            print("    U+%04X  %r" % (ord(ch), ch))
    else:
        print("  non-Arabic-block chars in Vocalized: none")
    return unmapped, non_arabic


# ===========================================================================
# Build
# ===========================================================================
def _out_path_for(ipa_path, tier):
    """
    Map an IPA source path to its output path for a tier:
      IPA/Peshitta/<Book>/<name>_ipa.txt
      -> Arabic/Peshita_Arabic/<Tier>/<Book>/<name>_<tier>.txt
    """
    rel = os.path.relpath(ipa_path, IPA_ROOT)   # <Book>/<name>_ipa.txt
    book_dir = os.path.dirname(rel)
    base = os.path.basename(rel)
    assert base.endswith("_ipa.txt"), base
    name = base[:-len("_ipa.txt")]
    out_name = "%s_%s.txt" % (name, tier)
    return os.path.join(ARABIC_ROOT, TIER_DIR_NAME[tier], book_dir, out_name)


def run_build(root=IPA_ROOT):
    """Transliterate the whole corpus into the 4 tier trees (via transliterate_line)."""
    unmapped = set()
    n_files = 0
    n_out = 0
    for ipa_path in iter_ipa_files(root):
        n_files += 1
        with open(ipa_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for tier in TIERS:
            out_path = _out_path_for(ipa_path, tier)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            out_lines = [transliterate_line(ln, tier, unmapped) for ln in lines]
            with open(out_path, "w", encoding="utf-8") as f:
                f.writelines(out_lines)
            n_out += 1
    print("Transliterated %d IPA file(s) -> %d output file(s)." % (n_files, n_out))
    if unmapped:
        print("WARNING: unmapped IPA segments encountered during build:",
              sorted(unmapped))
    else:
        print("No unmapped IPA segments encountered.")
    return n_files, n_out, sorted(unmapped)


# ===========================================================================
# CLI
# ===========================================================================
def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Deterministic IPA->Arabic transliterator for the Peshitta corpus."
    )
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--selftest", action="store_true", help="run embedded gold cases")
    g.add_argument("--coverage", action="store_true",
                   help="report unmapped IPA + non-Arabic-block chars in Vocalized")
    g.add_argument("--build", action="store_true", help="transliterate whole corpus")
    g.add_argument("--write-mapping", action="store_true",
                   help="(re)write transliteration_mapping_ar.json")
    args = parser.parse_args(argv)

    if args.selftest:
        all_pass, _ = run_selftest()
        return 0 if all_pass else 1
    if args.coverage:
        unmapped, non_arabic = run_coverage()
        return 0 if not (unmapped or non_arabic) else 2
    if args.build:
        run_build()
        return 0
    if args.write_mapping:
        path = write_mapping_json()
        print("Wrote %s" % os.path.relpath(path, REPO_ROOT))
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
