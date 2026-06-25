#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deterministic IPA -> Latin transliterator for the FRENCH Peshitta corpus.

Three tiers: SCHOLARLY | PRETTY | FRENCHIFIED.

SCHOLARLY and PRETTY are LANGUAGE-NEUTRAL and byte-for-byte identical to the
English Peshitta (their mapping logic is copied verbatim from
English/Peshita_English/transliterate.py).

FRENCHIFIED renders the Peshitta IPA using French orthographic conventions so a
French reader can approximate the pronunciation. It is a reader-aid; the
Scholarly tier remains the precise/reversible one.

The mapping table below is AUTHORITATIVE and hard-coded from the project SPEC.
A machine-readable copy is also written to mapping_fr.json (see
build_mapping_dict()).

CLI:
    transliterate_fr.py --selftest    run the embedded gold cases, print PASS/FAIL per (ref,tier)
    transliterate_fr.py --coverage    scan every *_ipa.txt for chars (besides space) not in the mapping
    transliterate_fr.py --build        transliterate the whole corpus into the 3 tier trees
    transliterate_fr.py --write-mapping  (re)write mapping_fr.json

Public API:
    transliterate(text, tier) -> str

DOCUMENTED LIMITATIONS (Frenchified tier):
    - French has no /h/; the French h is usually silent to French readers, so
      both /h/ and the pharyngeal /ħ/ (rendered "h") may be dropped by a reader.
    - A vowel followed by n/m may be read as a French nasal vowel.
    - θ ("th"), ð ("dh"), x ("kh"), ɣ ("gh"), ħ ("h") and the emphatics are
      approximations; French has no native equivalents.
    - ʕ (ayin) is not producible by French speakers and is dropped everywhere.
"""

import os
import sys
import json
import argparse

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
IPA_ROOT = os.path.join(REPO_ROOT, "IPA", "Peshitta")
FRENCH_ROOT = os.path.join(REPO_ROOT, "French", "Peshita_French")
MAPPING_JSON = os.path.join(SCRIPT_DIR, "mapping_fr.json")

# ---------------------------------------------------------------------------
# Unicode codepoints used in the SPEC (named for clarity)
# ---------------------------------------------------------------------------
SUPER_RHOTIC = "ˤ"      # ˤ  modifier letter small reversed glottal stop (emphatic marker)
LENGTH_MARK = "ː"       # ː  modifier letter triangular colon (long vowel)
COMBINING_DOT_BELOW = "̣"  # ̣  combining dot below (generic emphatic fallback)

# IPA source symbols
G_VOICED = "ɡ"   # ɡ  latin small letter script g
V_LABIO = "v"    # v
F_LABIO = "f"    # f
SH = "ʃ"         # ʃ
THETA = "θ"      # θ
ETH = "ð"        # ð
X_VELAR = "x"    # x
GAMMA = "ɣ"      # ɣ
HBAR = "ħ"       # ħ
J_PALATAL = "j"  # j
ALAPH = "ʔ"      # ʔ  glottal stop
AYIN = "ʕ"       # ʕ  voiced pharyngeal
A_FRONT = "a"    # a
ALPHA = "ɑ"      # ɑ  open back unrounded

# ---------------------------------------------------------------------------
# Tier names
# ---------------------------------------------------------------------------
SCHOLARLY = "scholarly"
PRETTY = "pretty"
FRENCHIFIED = "frenchified"
TIERS = (SCHOLARLY, PRETTY, FRENCHIFIED)

# Tier index lookup (scholarly=0, pretty=1) for the language-neutral tables.
# Frenchified is handled by dedicated logic, not by these tuples.
_TIER_IDX = {SCHOLARLY: 0, PRETTY: 1}

# ---------------------------------------------------------------------------
# CONSONANTS (single).  Order of tuple = (scholarly, pretty)
#   Copied verbatim from the English transducer for scholarly+pretty.
# ---------------------------------------------------------------------------
CONSONANTS = {
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
    V_LABIO:   ("ḇ", "v"),    # ḇ | v
    SH:        ("š", "sh"),   # š | sh
    THETA:     ("ṯ", "th"),   # ṯ | th
    ETH:       ("ḏ", "dh"),   # ḏ | dh
    X_VELAR:   ("ḵ", "kh"),   # ḵ | kh
    GAMMA:     ("ḡ", "gh"),   # ḡ | gh
    HBAR:      ("ḥ", "ḥ"),    # ḥ | ḥ
    J_PALATAL: ("y", "y"),
}

# ---------------------------------------------------------------------------
# SHORT VOWELS (no following length mark) -- (scholarly, pretty)
# ---------------------------------------------------------------------------
SHORT_VOWELS = {
    A_FRONT: ("a", "a"),
    ALPHA:   ("a", "a"),
    "e":     ("e", "e"),
    "i":     ("i", "i"),
    "o":     ("o", "o"),
    "u":     ("u", "u"),
}

# ---------------------------------------------------------------------------
# LONG VOWELS (V + ː).  (scholarly, pretty) -- macron form for both.
# ---------------------------------------------------------------------------
LONG_VOWELS = {
    A_FRONT: ("ā", "ā"),
    ALPHA:   ("ā", "ā"),
    "e":     ("ē", "ē"),
    "i":     ("ī", "ī"),
    "o":     ("ō", "ō"),
    "u":     ("ū", "ū"),
}

LONG_VOWEL_BASES = set(LONG_VOWELS.keys())  # a ɑ e i o u

# ---------------------------------------------------------------------------
# EMPHATICS (consonant + ˤ).  (scholarly, pretty)
# ---------------------------------------------------------------------------
EMPHATICS_EXPLICIT = {
    "t": ("ṭ", "ṭ"),   # ṭ | ṭ
    "s": ("ṣ", "ṣ"),   # ṣ | ṣ
}

# ---------------------------------------------------------------------------
# OTHER literals
# ---------------------------------------------------------------------------
HYPHEN = "-"  # -
SPACE = " "

# ===========================================================================
# FRENCHIFIED tier tables (per SPEC)
# ===========================================================================

# Simple (context-free) consonant mappings for the Frenchified tier.
# ɡ, s, and the emphatics sˤ/tˤ are context-sensitive and handled separately.
FR_CONSONANTS = {
    "b": "b",
    "d": "d",
    F_LABIO: "f",
    "k": "k",
    "l": "l",
    "m": "m",
    "n": "n",
    "p": "p",
    "q": "q",
    "r": "r",
    "t": "t",
    V_LABIO: "v",
    "z": "z",
    GAMMA: "gh",   # ɣ -> gh
    ETH: "dh",     # ð -> dh
    THETA: "th",   # θ -> th
    SH: "ch",      # ʃ -> ch
    X_VELAR: "kh", # x -> kh
    HBAR: "h",     # ħ -> h (approximation; French h usually silent)
    "h": "h",
    "w": "w",
    J_PALATAL: "y",  # j -> y
}

# Frenchified vowels (length collapsed; map by quality, with eː special).
FR_SHORT_VOWELS = {
    A_FRONT: "a",
    ALPHA: "a",
    "e": "è",
    "i": "i",
    "o": "o",
    "u": "ou",
}
FR_LONG_VOWELS = {
    A_FRONT: "a",
    ALPHA: "a",
    "e": "é",    # eː -> é  (the only length-sensitive distinction)
    "i": "i",
    "o": "o",
    "u": "ou",
}

# Front vowels that trigger the French hard-g "gu" spelling before ɡ.
# These are checked against the BASE vowel of the NEXT segment, restricted to
# /e/, /eː/, /i/, /iː/.
_FR_FRONT_VOWEL_BASES = {"e", "i"}

# IPA characters that count as a "vowel" for the intervocalic-s rule.
_VOWEL_CHARS = {A_FRONT, ALPHA, "e", "i", "o", "u"}


# ---------------------------------------------------------------------------
# Segmentation (shared by all tiers)
# ---------------------------------------------------------------------------
def _segment_token(token):
    """
    Segment a single whitespace/hyphen-delimited token's characters
    (left-to-right, longest match):
      1. consonant + ˤ            -> 2-char emphatic segment
      2. vowel (a ɑ e i o u) + ː  -> 2-char long-vowel segment
      3. otherwise single char
    Returns a list of segment strings.
    """
    segs = []
    i = 0
    n = len(token)
    while i < n:
        ch = token[i]
        nxt = token[i + 1] if i + 1 < n else None
        # Rule 1: consonant + ˤ
        if nxt == SUPER_RHOTIC and ch in CONSONANTS:
            segs.append(ch + SUPER_RHOTIC)
            i += 2
            continue
        # Rule 2: long vowel base + ː
        if nxt == LENGTH_MARK and ch in LONG_VOWEL_BASES:
            segs.append(ch + LENGTH_MARK)
            i += 2
            continue
        # Rule 3: single char
        segs.append(ch)
        i += 1
    return segs


def _seg_is_vowel(seg):
    """True if a segment is a vowel (short vowel char, or long-vowel V+ː)."""
    if seg is None:
        return False
    if len(seg) == 1:
        return seg in _VOWEL_CHARS
    if len(seg) == 2 and seg[1] == LENGTH_MARK:
        return seg[0] in _VOWEL_CHARS
    return False


def _seg_front_vowel(seg):
    """True if a segment is a FRONT vowel (/e/, /eː/, /i/, /iː/)."""
    if seg is None:
        return False
    if len(seg) == 1:
        return seg in _FR_FRONT_VOWEL_BASES
    if len(seg) == 2 and seg[1] == LENGTH_MARK:
        return seg[0] in _FR_FRONT_VOWEL_BASES
    return False


# ===========================================================================
# scholarly / pretty rendering (verbatim from English transducer)
# ===========================================================================
def _tier_consonant(ch, tier):
    """Return the scholarly/pretty rendering of a base consonant, or None."""
    entry = CONSONANTS.get(ch)
    if entry is None:
        return None
    return entry[_TIER_IDX[tier]]


def _render_segment_neutral(seg, tier, is_word_initial, unmapped):
    """
    Render a single segment for the language-neutral tiers (scholarly/pretty).
    Logic copied verbatim from English/Peshita_English/transliterate.py.
    """
    idx = _TIER_IDX[tier]

    # Emphatic segment (consonant + ˤ)
    if len(seg) == 2 and seg[1] == SUPER_RHOTIC:
        base = seg[0]
        explicit = EMPHATICS_EXPLICIT.get(base)
        if explicit is not None:
            return explicit[idx]
        # generic fallback for any other C + ˤ
        base_render = _tier_consonant(base, tier)
        if base_render is None:
            unmapped.add(base)
            base_render = base
        # scholarly / pretty: tier(C) + combining dot below
        return base_render + COMBINING_DOT_BELOW

    # Long-vowel segment (V + ː)
    if len(seg) == 2 and seg[1] == LENGTH_MARK:
        base = seg[0]
        entry = LONG_VOWELS.get(base)
        if entry is not None:
            return entry[idx]
        unmapped.add(base)
        return seg

    # Single character below this point
    ch = seg

    # Short vowel
    sv = SHORT_VOWELS.get(ch)
    if sv is not None:
        return sv[idx]

    # Consonant
    cons = _tier_consonant(ch, tier)
    if cons is not None:
        return cons

    # Glottals (special)
    if ch == ALAPH:  # ʔ
        if tier == SCHOLARLY:
            return "ʾ"  # ʾ
        # pretty
        return "" if is_word_initial else "'"
    if ch == AYIN:  # ʕ
        # scholarly and pretty both render ʿ
        return "ʿ"  # ʿ

    # Hyphen
    if ch == HYPHEN:
        return "-"

    # Space (handled by caller, but be safe)
    if ch == SPACE:
        return " "

    # Unmapped: record and pass through unchanged
    unmapped.add(ch)
    return ch


# ===========================================================================
# Frenchified rendering
# ===========================================================================
def _render_segment_frenchified(seg, is_word_initial, prev_seg, next_seg, unmapped):
    """
    Render a single segment for the FRENCHIFIED tier.

    Context:
      is_word_initial : True only for the first segment of a token (Alaph rule).
      prev_seg/next_seg : the adjacent segments within the SAME token (or None),
                          used by the hard-g rule (next) and intervocalic-s rule.
    """
    # Emphatic segment (consonant + ˤ)
    if len(seg) == 2 and seg[1] == SUPER_RHOTIC:
        base = seg[0]
        if base == "t":          # tˤ -> "t"
            return "t"
        if base == "s":          # sˤ -> same rule as s
            return _fr_s(prev_seg, next_seg)
        # generic fallback for any other C + ˤ: render the base consonant only.
        out = FR_CONSONANTS.get(base)
        if out is not None:
            return out
        if base == G_VOICED:
            return _fr_g(next_seg)
        unmapped.add(base)
        return base

    # Long-vowel segment (V + ː)
    if len(seg) == 2 and seg[1] == LENGTH_MARK:
        base = seg[0]
        out = FR_LONG_VOWELS.get(base)
        if out is not None:
            return out
        unmapped.add(base)
        return seg

    # Single character below this point
    ch = seg

    # Short vowel
    sv = FR_SHORT_VOWELS.get(ch)
    if sv is not None:
        return sv

    # ɡ  (context-sensitive hard-g rule)
    if ch == G_VOICED:
        return _fr_g(next_seg)

    # s  (context-sensitive intervocalic rule)
    if ch == "s":
        return _fr_s(prev_seg, next_seg)

    # Other (context-free) consonants
    out = FR_CONSONANTS.get(ch)
    if out is not None:
        return out

    # Glottals
    if ch == ALAPH:  # ʔ -> "" word-initial, "'" medial
        return "" if is_word_initial else "'"
    if ch == AYIN:   # ʕ -> dropped everywhere
        return ""

    # Hyphen
    if ch == HYPHEN:
        return "-"

    # Space (handled by caller, but be safe)
    if ch == SPACE:
        return " "

    # Unmapped: record and pass through unchanged
    unmapped.add(ch)
    return ch


def _fr_g(next_seg):
    """French hard-g rule: 'gu' before a front vowel (/e/,/eː/,/i/,/iː/), else 'g'."""
    return "gu" if _seg_front_vowel(next_seg) else "g"


def _fr_s(prev_seg, next_seg):
    """
    Intervocalic-s rule: 'ss' when BOTH neighbour SEGMENTS are vowels; else 's'.

    The test is on the literal IPA segment neighbours within the token (same
    rule for the emphatic sˤ). A dropped glottal -- ayin (ʕ) anywhere or a
    word-initial alaph (ʔ) -- is a CONSONANT segment, NOT a vowel, so it is
    OPAQUE: it is never skipped over. E.g. in 'treʕsar' the s's left neighbour
    is the ʕ segment (a consonant), so s stays single -> 'trèsar'; in 'mesˤʕaθ'
    the sˤ's right neighbour is the ʕ segment, so it stays single -> 'mèsath'.
    """
    return "ss" if (_seg_is_vowel(prev_seg) and _seg_is_vowel(next_seg)) else "s"


# ===========================================================================
# Public transliteration
# ===========================================================================
def transliterate(text, tier, unmapped=None):
    """
    Transliterate IPA `text` to Latin for the given `tier`
    (one of "scholarly", "pretty", "frenchified").

    Splits on the ASCII space ' ' only, preserving each space verbatim. Each
    token is segmented and rendered.

    "word-initial" (used by the Alaph drop rule) differs by tier:
      - FRENCHIFIED follows the SPEC: a segment is word-initial if it is the
        first segment of a whitespace/HYPHEN token, i.e. the token's first
        segment OR the segment immediately after a hyphen. So a post-hyphen
        alaph drops, e.g. 'bar-ʔaba' -> 'bar-aba'.
      - scholarly/pretty stay byte-for-byte identical to the language-neutral
        English transducer, which treats ONLY the token's first segment as
        word-initial (a hyphen is NOT a word boundary there).

    If `unmapped` (a set) is supplied, any unmapped characters encountered are
    added to it. Unmapped characters are passed through unchanged.
    """
    if tier not in TIERS:
        raise ValueError("Unknown tier: %r (expected one of %r)" % (tier, TIERS))
    if unmapped is None:
        unmapped = set()

    out_parts = []
    tokens = text.split(" ")
    for ti, token in enumerate(tokens):
        if ti > 0:
            out_parts.append(" ")  # the space that split() consumed
        if token == "":
            continue
        segs = _segment_token(token)
        n = len(segs)
        for si, seg in enumerate(segs):
            if tier == FRENCHIFIED:
                # SPEC (Frenchified): "word-initial" = first segment of a
                # whitespace/HYPHEN token. The token is already space-delimited,
                # so a segment is word-initial if it is the token's first
                # segment OR it immediately follows a hyphen segment (a hyphen
                # starts a new sub-token). This drops a post-hyphen alaph, e.g.
                # 'bar-ʔaba' -> 'bar-aba'.
                is_word_initial = (si == 0) or (segs[si - 1] == HYPHEN)
            else:
                # scholarly/pretty are byte-for-byte identical to the English
                # transducer, which treats ONLY the token's first segment as
                # word-initial (hyphen is NOT a word boundary there).
                is_word_initial = (si == 0)
            if tier == FRENCHIFIED:
                # Context neighbours for the hard-g and intervocalic-s rules are
                # the LITERAL adjacent segments within the token. Dropped
                # glottals (ayin ʕ, word-initial alaph ʔ) are CONSONANT
                # segments, so they are OPAQUE: a single 's' next to a dropped
                # glottal is NOT intervocalic and stays single (spec-literal).
                prev_seg = segs[si - 1] if si > 0 else None
                next_seg = segs[si + 1] if si + 1 < n else None
                out_parts.append(
                    _render_segment_frenchified(
                        seg, is_word_initial, prev_seg, next_seg, unmapped
                    )
                )
            else:
                out_parts.append(
                    _render_segment_neutral(seg, tier, is_word_initial, unmapped)
                )
    return "".join(out_parts)


def transliterate_line(line, tier, unmapped=None):
    """
    Transliterate a single corpus line of the form '<verse#>\\t<text>'.
    Keeps the '<verse#>\\t' prefix verbatim; only the text after the FIRST tab
    is transliterated. Lines without a tab are returned unchanged.
    Trailing newline (if any) is preserved.
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
    return prefix + "\t" + transliterate(text, tier, unmapped) + newline


# ---------------------------------------------------------------------------
# Machine-readable mapping export
# ---------------------------------------------------------------------------
def build_mapping_dict():
    """Build the JSON-serializable mapping table (per-tier dicts + rules)."""
    consonants = {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                  for ch, v in CONSONANTS.items()}
    short_vowels = {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                    for ch, v in SHORT_VOWELS.items()}
    long_vowels = {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                   for ch, v in LONG_VOWELS.items()}
    emphatics_explicit = {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                          for ch, v in EMPHATICS_EXPLICIT.items()}

    return {
        "meta": {
            "description": "Deterministic IPA->Latin mapping for the FRENCH Peshitta corpus.",
            "tiers": list(TIERS),
            "note": "transliterate_fr.py is authoritative; this file mirrors its hard-coded tables.",
            "scholarly_pretty_note": ("scholarly and pretty are language-neutral and "
                                      "byte-for-byte identical to the English Peshitta."),
        },
        "unicode": {
            "emphatic_marker": SUPER_RHOTIC,        # ˤ
            "length_mark": LENGTH_MARK,             # ː
            "combining_dot_below": COMBINING_DOT_BELOW,
            "alaph": ALAPH,                         # ʔ
            "ayin": AYIN,                           # ʕ
            "hyphen": HYPHEN,
        },
        "segmentation": [
            "Split on ASCII space ' ' only; spaces are preserved verbatim.",
            "Within each token, left-to-right longest match:",
            "  1. consonant + \\u02E4 (ˤ) -> emphatic segment (2 chars)",
            "  2. vowel (a ɑ e i o u) + \\u02D0 (ː) -> long-vowel segment (2 chars)",
            "  3. otherwise single char",
            ("word-initial = the FIRST segment of a whitespace/hyphen token (used by the Alaph rule). "
             "Frenchified treats a post-hyphen segment as word-initial (drops a post-hyphen alaph); "
             "scholarly/pretty stay identical to the English transducer, where only the token's first "
             "segment is word-initial."),
        ],
        "tier_dicts": {
            "scholarly_pretty": {
                "consonants": consonants,
                "short_vowels": short_vowels,
                "long_vowels": long_vowels,
                "emphatics_explicit": emphatics_explicit,
            },
            "frenchified": {
                "consonants_context_free": dict(FR_CONSONANTS),
                "short_vowels": dict(FR_SHORT_VOWELS),
                "long_vowels": dict(FR_LONG_VOWELS),
            },
        },
        "rules": {
            "scholarly_pretty": {
                "alaph": {
                    "symbol": ALAPH,
                    SCHOLARLY: "always \\u02BE (ʾ)",
                    PRETTY: "word-initial -> '' (drop); else -> \"'\"",
                },
                "ayin": {
                    "symbol": AYIN,
                    SCHOLARLY: "\\u02BF (ʿ)",
                    PRETTY: "\\u02BF (ʿ)",
                },
                "emphatic_fallback": {
                    "applies_to": "any consonant + \\u02E4 not in emphatics_explicit",
                    SCHOLARLY: "tier(C) + \\u0323 (combining dot below)",
                    PRETTY: "tier(C) + \\u0323 (combining dot below)",
                },
            },
            "frenchified": {
                "alaph": {
                    "symbol": ALAPH,
                    "rule": ("word-initial -> '' (drop); medial -> \"'\". "
                             "'word-initial' = first segment of a whitespace/HYPHEN "
                             "token, so a post-hyphen alaph also drops "
                             "(e.g. bar-ʔaba -> 'bar-aba')."),
                },
                "ayin": {
                    "symbol": AYIN,
                    "rule": "'' (dropped everywhere; not producible by French speakers)",
                },
                "hard_g": {
                    "symbol": G_VOICED,
                    "rule": "'gu' if NEXT segment is a front vowel (/e/, /eː/, /i/, /iː/); else 'g'",
                },
                "intervocalic_s": {
                    "symbol": "s",
                    "rule": ("'ss' when BOTH neighbour SEGMENTS are vowels "
                             "(intervocalic); else 's'. Same rule applies to the "
                             "emphatic sˤ. The test uses the LITERAL adjacent IPA "
                             "segments within the token. A dropped glottal -- ayin "
                             "(ʕ) anywhere, or a word-initial alaph (ʔ) -- is a "
                             "CONSONANT segment, NOT a vowel, so it is OPAQUE and is "
                             "never skipped over. E.g. daʕsiːq -> 'dasiq', treʕsar -> "
                             "'trèsar', mesˤʕaθ -> 'mèsath' (single s, because a ʕ "
                             "segment neighbours the s). A truly intervocalic s still "
                             "doubles, e.g. pesˤe -> 'pèssè'. This matches the literal "
                             "spec and the parallel English 'Anglicized' convention. "
                             "Cross-token word-initial s before a vowel stays single "
                             "'s' (neighbour is None across the space)."),
                },
                "emphatic_t": {"symbol": "tˤ", "rule": "'t'"},
                "vowel_length": "Length is collapsed (map by quality), except eː -> 'é' (e -> 'è').",
                "limitations": [
                    "French has no /h/ (often silent to French readers).",
                    "A vowel followed by n/m may be read as a French nasal vowel.",
                    "θ, ð, x, ɣ, ħ and the emphatics are approximations.",
                ],
            },
            "hyphen": {"symbol": HYPHEN, "all_tiers": "-"},
            "space": {"all_tiers": "space (preserved verbatim)"},
            "unmapped": "Any char not covered above (besides space) is recorded and passed through unchanged.",
        },
    }


def write_mapping_json(path=MAPPING_JSON):
    data = build_mapping_dict()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path


# ---------------------------------------------------------------------------
# Gold cases
# ---------------------------------------------------------------------------
GOLD_CASES = [
    {
        "ref": "John 1:1",
        "ipa": "breːʃiːθ ʔiːθawj wɑː melθɑː whuː melθɑː ʔiːθawj wɑː lwɑːθ ʔɑːlɑːhɑː waʔlɑːhɑː ʔiːθawj wɑː huː melθɑː",
        "scholarly": "brēšīṯ ʾīṯawy wā melṯā whū melṯā ʾīṯawy wā lwāṯ ʾālāhā waʾlāhā ʾīṯawy wā hū melṯā",
        "pretty": "brēshīth īthawy wā melthā whū melthā īthawy wā lwāth ālāhā wa'lāhā īthawy wā hū melthā",
        "frenchified": "bréchith ithawy wa mèltha whou mèltha ithawy wa lwath alaha wa'laha ithawy wa hou mèltha",
    },
    {
        "ref": "John 1:2",
        "ipa": "hɑːnɑː ʔiːθawj wɑː breːʃiːθ lwɑːθ ʔɑːlɑːhɑː",
        "scholarly": "hānā ʾīṯawy wā brēšīṯ lwāṯ ʾālāhā",
        "pretty": "hānā īthawy wā brēshīth lwāth ālāhā",
        "frenchified": "hana ithawy wa bréchith lwath alaha",
    },
    {
        "ref": "John 1:3",
        "ipa": "kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː",
        "scholarly": "kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā",
        "pretty": "kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā",
        "frenchified": "koul b'iydhèh hwa wvèladhawy afla hdha hwath mèdèm dahwa",
    },
    {
        "ref": "Matthew 1:1",
        "ipa": "kθɑːvɑː diːliːðuːθeh djeʃuːʕ mʃiːħɑː breh dðawiːð breh dʔavrɑːhɑːm",
        "scholarly": "kṯāḇā dīlīḏūṯeh dyešūʿ mšīḥā breh dḏawīḏ breh dʾaḇrāhām",
        "pretty": "kthāvā dīlīdhūtheh dyeshūʿ mshīḥā breh ddhawīdh breh d'avrāhām",
        "frenchified": "kthava dilidhouthèh dyèchou mchiha brèh ddhawidh brèh d'avraham",
    },
    {
        "ref": "Romans 1:1",
        "ipa": "pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː",
        "scholarly": "pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā",
        "pretty": "pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā",
        "frenchified": "pawlaws avda dyèchou mchiha qarya wachliha d'èthprèch lè'wanguèliyyawn d'alaha",
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
                print("PASS  %-14s %-12s" % (ref, tier))
            else:
                all_pass = False
                print("FAIL  %-14s %-12s" % (ref, tier))
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
                mismatches.append({
                    "ref": ref,
                    "tier": tier,
                    "expected": expected,
                    "got": got,
                })
    print("")
    print("ALL PASS" if all_pass else "SOME FAILED")
    return all_pass, mismatches


# ---------------------------------------------------------------------------
# Coverage
# ---------------------------------------------------------------------------
def iter_ipa_files(root=IPA_ROOT):
    for dirpath, _dirs, files in os.walk(root):
        for fn in sorted(files):
            if fn.endswith("_ipa.txt"):
                yield os.path.join(dirpath, fn)


def run_coverage(root=IPA_ROOT):
    """
    Scan every *_ipa.txt under root; transliterate verse text in all three tiers,
    collecting any character (besides space) not covered by the mapping.
    Returns a sorted list of unmapped characters.
    """
    unmapped = set()
    n_files = 0
    for path in iter_ipa_files(root):
        n_files += 1
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if "\t" not in line:
                    continue
                body = line.rstrip("\r\n")
                _prefix, text = body.split("\t", 1)
                for tier in TIERS:
                    transliterate(text, tier, unmapped)
    chars = sorted(unmapped)
    print("Scanned %d IPA file(s) under %s" % (n_files, root))
    if chars:
        print("UNMAPPED characters (besides space):")
        for ch in chars:
            print("  U+%04X  %r" % (ord(ch), ch))
    else:
        print("UNMAPPED characters (besides space): none")
    return chars


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def _out_path_for(ipa_path, tier):
    """
    Map an IPA source path to the output path for a tier.
      IPA/Peshitta/<Book>/<name>_ipa.txt
      -> French/Peshita_French/<Tier>/<Book>/<name>_<tier>.txt
    """
    rel = os.path.relpath(ipa_path, IPA_ROOT)        # <Book>/<name>_ipa.txt
    book_dir = os.path.dirname(rel)
    base = os.path.basename(rel)
    assert base.endswith("_ipa.txt"), base
    name = base[:-len("_ipa.txt")]                   # <name>
    tier_dir_name = {
        SCHOLARLY: "Scholarly",
        PRETTY: "Pretty",
        FRENCHIFIED: "Frenchified",
    }[tier]
    out_name = "%s_%s.txt" % (name, tier)
    return os.path.join(FRENCH_ROOT, tier_dir_name, book_dir, out_name)


def run_build(root=IPA_ROOT):
    """Transliterate the whole corpus into the 3 tier trees."""
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
        print("WARNING: unmapped characters encountered during build:")
        for ch in sorted(unmapped):
            print("  U+%04X  %r" % (ord(ch), ch))
    else:
        print("No unmapped characters encountered.")
    return n_files, n_out, sorted(unmapped)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Deterministic IPA->Latin transliterator for the FRENCH Peshitta corpus."
    )
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--selftest", action="store_true", help="run embedded gold cases")
    g.add_argument("--coverage", action="store_true", help="report chars not in mapping")
    g.add_argument("--build", action="store_true", help="transliterate whole corpus")
    g.add_argument("--write-mapping", action="store_true", help="(re)write mapping_fr.json")
    args = parser.parse_args(argv)

    if args.selftest:
        all_pass, _ = run_selftest()
        return 0 if all_pass else 1
    if args.coverage:
        chars = run_coverage()
        return 0 if not chars else 2
    if args.build:
        run_build()
        return 0
    if args.write_mapping:
        path = write_mapping_json()
        print("Wrote %s" % path)
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
