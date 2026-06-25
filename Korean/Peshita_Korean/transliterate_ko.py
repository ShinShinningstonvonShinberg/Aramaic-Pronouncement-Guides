#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deterministic IPA transliterator for the KOREAN Peshitta corpus.

Four tiers:  SCHOLARLY | PRETTY | HANGUL | ROMANIZED(RR)

    SCHOLARLY + PRETTY  are LANGUAGE-NEUTRAL: their mapping logic is reproduced
        VERBATIM from the English transducer
        (English/Peshita_English/transliterate.py) so their output is
        byte-for-byte identical to the English Peshitta.  The Scholarly tier
        remains the precise / reversible one.

    HANGUL  renders the Syriac IPA into composed Hangul syllable blocks as a
        reader aid for Korean readers:  map each IPA segment to jamo, syllabify
        into legal (C)(G)V(C) blocks (inserting an epenthetic ㅡ where Korean
        phonotactics forbid a cluster or coda), then compose precomposed Hangul
        via the 0xAC00 formula.

    ROMANIZED  is the Revised-Romanization (RR) readback of the generated
        Hangul, per syllable, with NO cross-syllable sandhi.  Because it is
        derived from the Hangul tier, the two reader tiers are guaranteed
        mutually consistent.

The mapping tables below are AUTHORITATIVE and hard-coded.  A machine-readable
copy is also written to transliteration_mapping_ko.json (see
build_mapping_dict()).

------------------------------------------------------------------------------
LIMITATIONS of the two READER tiers (Hangul / Romanized) -- READ THIS:
  * Forced epenthesis: Korean syllable structure is (C)(G)V(C) with no onset
    clusters and a restricted coda set, so an epenthetic ㅡ (eu) is inserted to
    break up Syriac clusters/codas.  This adds vowels that are NOT in the
    Syriac.
  * No /f v θ ð z/ distinctions survive (f->ㅍ like p, v->ㅂ like b, θ->ㅅ like s,
    ð->ㄷ like d, z->ㅈ).
  * l and r MERGE to a single ㄹ.
  * A glide + its homorganic vowel collapses to the bare vowel (ji->ㅣ, wu->ㅜ);
    Korean has no distinct *yi / *wu medial.
  * The Korean 3-way laryngeal contrast (plain / tense / aspirated) cannot
    encode Syriac voicing; emphatics are approximated with tense jamo.
  * Gutturals and emphatics are heavily approximated (x/ħ/h->ㅎ, ʔ/ʕ dropped,
    q->ㅋ like k, ɣ->ㄱ like g).  A syllable-final /h/-class consonant is NOT
    placed as a (non-occurring, [t]-reading) ㅎ batchim but emitted as its own
    ㅎ+ㅡ (heu) syllable so the /h/ stays audible.
  * ʃ -> ㅅ; before a back/low vowel it takes a y-glide medial (ʃa->샤, ʃo->쇼,
    ʃu->슈) to surface the palatal [ɕ] 'sh' allophone (ʃi->시, ʃe->세 already
    [ɕ]-class).
  * Revised-Romanization neutralizes every coda: e.g. final ㅎ reads back as 't'
    (this is correct RR, not a defect) and ㅅ/ㅆ/ㅈ/ㅊ/ㅌ codas also read 't'.
  * The Hangul/Romanized tiers are NOT reversible.
------------------------------------------------------------------------------

CLI:
    transliterate_ko.py --selftest        run embedded gold cases (all 4 tiers)
    transliterate_ko.py --coverage        scan every *_ipa.txt for unmapped chars
    transliterate_ko.py --build           transliterate the whole corpus -> Korean tree
    transliterate_ko.py --write-mapping   (re)write transliteration_mapping_ko.json

Public API:
    transliterate(text, tier) -> str
    transliterate_line(line, tier) -> str
"""

import os
import sys
import json
import argparse

# ---------------------------------------------------------------------------
# Paths -- resolved from THIS file's location only (no absolute paths).
#   Korean/Peshita_Korean/transliterate_ko.py
#       SCRIPT_DIR = .../Korean/Peshita_Korean
#       ../..      = repo root (Korean -> repo root)
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
IPA_ROOT = os.path.join(REPO_ROOT, "IPA", "Peshitta")
KOREAN_ROOT = os.path.join(REPO_ROOT, "Korean", "Peshita_Korean")
MAPPING_JSON = os.path.join(SCRIPT_DIR, "transliteration_mapping_ko.json")

# ---------------------------------------------------------------------------
# Unicode codepoints used in the SPEC (named for clarity)
# ---------------------------------------------------------------------------
SUPER_RHOTIC = "ˤ"          # ˤ  modifier letter small reversed glottal stop (emphatic)
LENGTH_MARK = "ː"           # ː  modifier letter triangular colon (long vowel)
COMBINING_DOT_BELOW = "̣"   # ̣  combining dot below (generic emphatic fallback)

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
HYPHEN = "-"
SPACE = " "

# ---------------------------------------------------------------------------
# Tier names
# ---------------------------------------------------------------------------
SCHOLARLY = "scholarly"
PRETTY = "pretty"
HANGUL = "hangul"
ROMANIZED = "romanized"
TIERS = (SCHOLARLY, PRETTY, HANGUL, ROMANIZED)

# Directory + file-suffix naming for the build tree
TIER_DIR_NAME = {
    SCHOLARLY: "Scholarly",
    PRETTY: "Pretty",
    HANGUL: "Hangul",
    ROMANIZED: "Romanized",
}

# ===========================================================================
# SCHOLARLY / PRETTY tables and logic -- reproduced VERBATIM from the English
# transducer.  Each tuple is (scholarly, pretty).  The output of these two
# tiers is byte-for-byte identical to English/Peshita_English/transliterate.py.
# ===========================================================================
CONSONANTS = {  # (scholarly, pretty)
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

SHORT_VOWELS = {  # identical across tiers
    A_FRONT: ("a", "a"),
    ALPHA:   ("a", "a"),
    "e":     ("e", "e"),
    "i":     ("i", "i"),
    "o":     ("o", "o"),
    "u":     ("u", "u"),
}

LONG_VOWELS = {  # V + ː ; scholarly and pretty share the macron form
    A_FRONT: ("ā", "ā"),
    ALPHA:   ("ā", "ā"),
    "e":     ("ē", "ē"),
    "i":     ("ī", "ī"),
    "o":     ("ō", "ō"),
    "u":     ("ū", "ū"),
}
LONG_VOWEL_BASES = set(LONG_VOWELS.keys())  # a ɑ e i o u

EMPHATICS_EXPLICIT = {  # consonant + ˤ
    "t": ("ṭ", "ṭ"),
    "s": ("ṣ", "ṣ"),
}

_SP_IDX = {SCHOLARLY: 0, PRETTY: 1}


def _tier_consonant(ch, tier):
    """Return the tier rendering of a base consonant char, or None if not a consonant."""
    entry = CONSONANTS.get(ch)
    if entry is None:
        return None
    return entry[_SP_IDX[tier]]


def _segment_token(token):
    """
    Segment a single whitespace-delimited token into segments (left-to-right,
    longest match):
      1. consonant + ˤ            -> 2-char emphatic segment
      2. vowel (a ɑ e i o u) + ː  -> 2-char long-vowel segment
      3. otherwise single char
    """
    segs = []
    i = 0
    n = len(token)
    while i < n:
        ch = token[i]
        nxt = token[i + 1] if i + 1 < n else None
        if nxt == SUPER_RHOTIC and ch in CONSONANTS:
            segs.append(ch + SUPER_RHOTIC)
            i += 2
            continue
        if nxt == LENGTH_MARK and ch in LONG_VOWEL_BASES:
            segs.append(ch + LENGTH_MARK)
            i += 2
            continue
        segs.append(ch)
        i += 1
    return segs


def _render_segment(seg, tier, is_word_initial, unmapped):
    """
    Render a single SCHOLARLY/PRETTY segment for the given tier.
    `is_word_initial` is True only for the FIRST segment of a token (Alaph rule).
    `unmapped` collects any unmapped characters.
    """
    idx = _SP_IDX[tier]

    # Emphatic segment (consonant + ˤ)
    if len(seg) == 2 and seg[1] == SUPER_RHOTIC:
        base = seg[0]
        explicit = EMPHATICS_EXPLICIT.get(base)
        if explicit is not None:
            return explicit[idx]
        base_render = _tier_consonant(base, tier)
        if base_render is None:
            unmapped.add(base)
            base_render = base
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

    sv = SHORT_VOWELS.get(ch)
    if sv is not None:
        return sv[idx]

    cons = _tier_consonant(ch, tier)
    if cons is not None:
        return cons

    if ch == ALAPH:  # ʔ
        if tier == SCHOLARLY:
            return "ʾ"
        return "" if is_word_initial else "'"
    if ch == AYIN:   # ʕ
        return "ʿ"

    if ch == HYPHEN:
        return "-"
    if ch == SPACE:
        return " "

    unmapped.add(ch)
    return ch


def _sp_transliterate(text, tier, unmapped):
    """Scholarly/Pretty transliteration (English-identical)."""
    out_parts = []
    tokens = text.split(" ")
    for ti, token in enumerate(tokens):
        if ti > 0:
            out_parts.append(" ")
        if token == "":
            continue
        segs = _segment_token(token)
        for si, seg in enumerate(segs):
            out_parts.append(_render_segment(seg, tier, si == 0, unmapped))
    return "".join(out_parts)


# ===========================================================================
# HANGUL tier
# ===========================================================================
# Jamo index orders (per the authoritative algorithm spec).
CHO = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
JUNG = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
JONG_LIST = [
    "", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ",
    "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ",
    "ㅌ", "ㅍ", "ㅎ",
]
CHO_IDX = {c: i for i, c in enumerate(CHO)}
JUNG_IDX = {c: i for i, c in enumerate(JUNG)}
JONG_IDX = {c: i for i, c in enumerate(JONG_LIST)}

# IPA consonant -> jamo.
#   b,v->ㅂ  p,f->ㅍ  t->ㅌ  d,ð->ㄷ  k,q->ㅋ  ɡ,ɣ->ㄱ  s->ㅅ  z->ㅈ  ʃ->ㅅ
#   x,ħ,h->ㅎ  m->ㅁ  n->ㄴ  l,r->ㄹ
CONS_JAMO = {
    "b": "ㅂ", "v": "ㅂ", "p": "ㅍ", "f": "ㅍ", "t": "ㅌ", "d": "ㄷ", "ð": "ㄷ",
    "k": "ㅋ", "ɡ": "ㄱ", "ɣ": "ㄱ", "q": "ㅋ", "s": "ㅅ", "z": "ㅈ", "ʃ": "ㅅ",
    "x": "ㅎ", "ħ": "ㅎ", "h": "ㅎ", "m": "ㅁ", "n": "ㄴ", "l": "ㄹ", "r": "ㄹ",
}
EMPH_JAMO = {"t": "ㄸ", "s": "ㅆ"}   # tˤ -> ㄸ , sˤ -> ㅆ
THETA_JAMO = "ㅅ"                     # θ -> ㅅ (plain, not tense)

# Length collapsed: a,ɑ->ㅏ  e->ㅔ  i->ㅣ  o->ㅗ  u->ㅜ
VOW_JAMO = {"a": "ㅏ", "ɑ": "ㅏ", "e": "ㅔ", "i": "ㅣ", "o": "ㅗ", "u": "ㅜ"}
GLIDES = {"w", "j"}
# glide + vowel -> compound medial (jungseong)
COMPOUND = {
    ("j", "a"): "ㅑ", ("j", "ɑ"): "ㅑ", ("j", "e"): "ㅖ", ("j", "o"): "ㅛ",
    ("j", "u"): "ㅠ", ("j", "i"): "ㅣ",
    ("w", "a"): "ㅘ", ("w", "ɑ"): "ㅘ", ("w", "e"): "ㅞ", ("w", "i"): "ㅟ",
    ("w", "o"): "ㅝ", ("w", "u"): "ㅜ",
}
# y-glide medials used when ʃ precedes a back/low vowel so a Korean reader
# sounds out the palatal [ɕ] ('sh') allophone (ʃa->샤, ʃo->쇼, ʃu->슈) instead
# of plain [s] (사/소/수).  ʃ+i (시) and ʃ+e (세) are already [ɕ]-class, untouched.
SH_GLIDE_MEDIAL = {"a": "ㅑ", "ɑ": "ㅑ", "o": "ㅛ", "u": "ㅠ"}

# Tense stops that have no jongseong slot must neutralize before use as a coda.
CODA_NEUTRAL = {"ㄸ": "ㄷ", "ㅃ": "ㅂ", "ㅉ": "ㅈ"}

# The /h/-class jamo (only ever produced by x/ħ/h) is never legal/audible as a
# real Korean batchim -- a final ㅎ block (e.g. 렣/붛/닿) looks impossible to a
# reader and RR-reads back as a spurious [t], DELETING the /h/.  So a ㅎ that
# would land in a coda slot is instead emitted as its own ㅎ+ㅡ (heu) syllable,
# the standard Korean device for an audible foreign final /h/ (바흐 'Bach').
CODA_DIVERT = {"ㅎ"}

EPENTHETIC_VOWEL = "ㅡ"     # inserted to break illegal clusters / codas
SILENT_ONSET = "ㅇ"         # placeholder onset for a vowel-initial syllable


def _compose(cho, jung, jong=""):
    """Compose a precomposed Hangul syllable block from three jamo."""
    return chr(0xAC00 + CHO_IDX[cho] * 588 + JUNG_IDX[jung] * 28 + JONG_IDX[jong])


def _h_segment(tok):
    """Segment an IPA token for the Hangul tier (emphatic + long-vowel longest match)."""
    segs = []
    i = 0
    n = len(tok)
    while i < n:
        ch = tok[i]
        nxt = tok[i + 1] if i + 1 < n else None
        if nxt == SUPER_RHOTIC and (ch in CONS_JAMO or ch in EMPH_JAMO):
            segs.append(ch + SUPER_RHOTIC)
            i += 2
            continue
        if nxt == LENGTH_MARK and ch in VOW_JAMO:
            segs.append(ch + LENGTH_MARK)
            i += 2
            continue
        segs.append(ch)
        i += 1
    return segs


def _vbase(seg):
    """Strip a trailing length mark for vowel-base lookups (length collapsed)."""
    return seg[0] if (len(seg) == 2 and seg[1] == LENGTH_MARK) else seg


def _cons_jamo(seg, unmapped):
    """Map a consonant segment to its jamo, or None if it is not a consonant."""
    if len(seg) == 2 and seg[1] == SUPER_RHOTIC:
        b = seg[0]
        if b in EMPH_JAMO:
            return EMPH_JAMO[b]
        if b in CONS_JAMO:
            return CONS_JAMO[b]
        unmapped.add(b)
        return None
    if seg == THETA:
        return THETA_JAMO
    if seg in CONS_JAMO:
        return CONS_JAMO[seg]
    return None


def _token_items(tok, unmapped):
    """
    Convert an IPA token into an ordered list of phonological items:
      ("N", jungseong)  for a nucleus (vowel or glide+vowel compound medial)
      ("C", jamo)       for a consonant
    ʔ (alaph) and ʕ (ayin) are DROPPED (boundary / silent).
    A bare glide that is not followed by a mappable vowel falls back to its
    vowel form (w->ㅜ, j->ㅣ) so nothing is lost.
    ʃ directly before a back/low vowel (a/ɑ/o/u) becomes ㅅ + a y-glide medial
    (ʃa->샤, ʃo->쇼, ʃu->슈) so the [ɕ] 'sh' allophone surfaces.
    """
    segs = _h_segment(tok)
    items = []
    i = 0
    n = len(segs)
    while i < n:
        s = segs[i]
        if s in (ALAPH, AYIN):
            i += 1
            continue
        b = _vbase(s)
        if b in VOW_JAMO:
            items.append(("N", VOW_JAMO[b]))
            i += 1
            continue
        # ʃ as an onset immediately before a back/low vowel -> ㅅ + y-glide medial.
        if s == SH and i + 1 < n:
            nb = _vbase(segs[i + 1])
            if nb in SH_GLIDE_MEDIAL:
                items.append(("C", "ㅅ"))
                items.append(("N", SH_GLIDE_MEDIAL[nb]))
                i += 2
                continue
        if s in GLIDES:
            if i + 1 < n:
                nb = _vbase(segs[i + 1])
                if nb in VOW_JAMO and (s, nb) in COMPOUND:
                    items.append(("N", COMPOUND[(s, nb)]))
                    i += 2
                    continue
            items.append(("N", "ㅜ" if s == "w" else "ㅣ"))
            i += 1
            continue
        jm = _cons_jamo(s, unmapped)
        if jm:
            items.append(("C", jm))
        else:
            if s not in (SUPER_RHOTIC, LENGTH_MARK):
                unmapped.add(s)
        i += 1
    return items


def _syllabify(items):
    """
    Pack the item list into legal (C)(G)V(C) Hangul blocks.
      * No onset clusters and no illegal codas: surplus consonants get an
        epenthetic ㅡ.
      * A vowel-initial syllable uses the silent onset ㅇ.
      * A coda is neutralized (tense stops -> plain) before being placed.
    Returns a list of [cho, jung, jong] triples.
    """
    out = []

    def place_coda(syl, c):
        """Place consonant `c` as the coda of `syl`, OR -- if it is a divert-class
        jamo (ㅎ, which is never a real Korean batchim) -- emit it as its own
        ㅎ+ㅡ syllable so the /h/ stays audible instead of becoming a spurious [t]."""
        if c in CODA_DIVERT:
            out.append([c, EPENTHETIC_VOWEL, ""])
        else:
            syl[2] = CODA_NEUTRAL.get(c, c)

    nuclei = [k for k, it in enumerate(items) if it[0] == "N"]

    # No vowels at all: every consonant becomes its own C + ㅡ syllable.
    if not nuclei:
        for it in items:
            if it[0] == "C":
                out.append([it[1], EPENTHETIC_VOWEL, ""])
        return out

    first = nuclei[0]
    # Consonants before the first nucleus.
    lead = [items[k][1] for k in range(first) if items[k][0] == "C"]
    onset = SILENT_ONSET
    if lead:
        for c in lead[:-1]:
            out.append([c, EPENTHETIC_VOWEL, ""])
        onset = lead[-1]

    for ni, npos in enumerate(nuclei):
        nucleus = items[npos][1]
        syl = [onset, nucleus, ""]
        out.append(syl)
        nxt = nuclei[ni + 1] if ni + 1 < len(nuclei) else len(items)
        cluster = [items[k][1] for k in range(npos + 1, nxt) if items[k][0] == "C"]
        m = len(cluster)
        if ni + 1 < len(nuclei):
            # There is a following nucleus to receive an onset.
            if m == 0:
                onset = SILENT_ONSET
            elif m == 1:
                onset = cluster[0]
            else:
                # First consonant codas this syllable; middle ones get ㅡ; last
                # becomes the onset of the next syllable.
                place_coda(syl, cluster[0])
                for c in cluster[1:-1]:
                    out.append([c, EPENTHETIC_VOWEL, ""])
                onset = cluster[-1]
        else:
            # Final nucleus: one consonant codas; any extra get ㅡ syllables.
            if m >= 1:
                place_coda(syl, cluster[0])
                for c in cluster[1:]:
                    out.append([c, EPENTHETIC_VOWEL, ""])
    return out


def _h_render_token(tok, unmapped):
    """Render one space-delimited token to Hangul, preserving internal hyphens."""
    parts = tok.split("-")
    out = []
    for p in parts:
        if p == "":
            out.append("")
            continue
        syls = _syllabify(_token_items(p, unmapped))
        out.append("".join(_compose(c, v, j) for c, v, j in syls))
    return "-".join(out)


def _hangul_transliterate(text, unmapped):
    return " ".join(_h_render_token(t, unmapped) if t else "" for t in text.split(" "))


# ===========================================================================
# ROMANIZED (RR) tier -- Revised-Romanization readback of the Hangul.
# Per syllable; NO cross-syllable sandhi (documented limitation).
# ===========================================================================
RR_CHO = ["g", "kk", "n", "d", "tt", "r", "m", "b", "pp", "s", "ss", "",
          "j", "jj", "ch", "k", "t", "p", "h"]
RR_JUNG = ["a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae",
           "oe", "yo", "u", "wo", "we", "wi", "yu", "eu", "ui", "i"]
# Coda RR values, all NEUTRALIZED to the single released consonant per the rule
#   ㄱ/ㄲ/ㅋ->k  ㄴ->n  ㄷ/ㅅ/ㅆ/ㅈ/ㅊ/ㅌ/ㅎ->t  ㄹ->l  ㅁ->m  ㅂ/ㅍ->p  ㅇ->ng
# (cluster codas neutralize to their surviving consonant: ㄳ->k, ㄵ->n, ㄺ->k,
#  ㄻ->m, ㄼ->p, ㄽ->l, ㄾ->l, ㄿ->p, ㅀ->l, ㅄ->p, ㄶ->n).  The syllabifier only
# ever composes a single neutralized coda, so the cluster slots are unreachable;
# they are kept consistent with the stated neutralization rule for any external
# block fed through _rr_readback.
RR_JONG = ["", "k", "k", "k", "n", "n", "n", "t", "l", "k", "m", "p",
           "l", "l", "p", "l", "m", "p", "p", "t", "t", "ng", "t", "t",
           "k", "t", "p", "t"]


def _rr_readback(hangul_text):
    """Read each precomposed Hangul block back to RR; pass other chars through."""
    out = []
    for ch in hangul_text:
        o = ord(ch)
        if 0xAC00 <= o <= 0xD7A3:
            s = o - 0xAC00
            cho = s // 588
            jung = (s % 588) // 28
            jong = s % 28
            out.append(RR_CHO[cho] + RR_JUNG[jung] + RR_JONG[jong])
        else:
            out.append(ch)
    return "".join(out)


# ===========================================================================
# Public API
# ===========================================================================
def transliterate(text, tier, unmapped=None):
    """
    Transliterate IPA `text` for the given `tier`
    (one of "scholarly", "pretty", "hangul", "romanized").

    Scholarly/Pretty split on the ASCII space only, preserving each space
    verbatim, and produce English-identical output.  Hangul composes precomposed
    syllable blocks; Romanized is the RR readback of the Hangul.

    If `unmapped` (a set) is supplied, any unmapped characters encountered are
    added to it.
    """
    if tier not in TIERS:
        raise ValueError("Unknown tier: %r (expected one of %r)" % (tier, TIERS))
    if unmapped is None:
        unmapped = set()
    if tier in (SCHOLARLY, PRETTY):
        return _sp_transliterate(text, tier, unmapped)
    if tier == HANGUL:
        return _hangul_transliterate(text, unmapped)
    if tier == ROMANIZED:
        return _rr_readback(_hangul_transliterate(text, unmapped))
    raise ValueError("Unknown tier: %r" % (tier,))  # unreachable


def transliterate_line(line, tier, unmapped=None):
    """
    Transliterate a single corpus line of the form '<verse#>\\t<text>'.
    Keeps the '<verse#>\\t' prefix verbatim; only the text after the FIRST tab
    is transliterated.  Lines without a tab are returned unchanged.
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
        return line

    prefix, text = body.split("\t", 1)
    return prefix + "\t" + transliterate(text, tier, unmapped) + newline


# ===========================================================================
# Machine-readable mapping export
# ===========================================================================
DOCUMENTED_LIMITATIONS = [
    "Forced epenthesis: Korean syllables are (C)(G)V(C) with no onset clusters "
    "and a restricted coda set, so an epenthetic \\u3161 (ㅡ) is inserted to "
    "break up Syriac clusters/codas, adding vowels not present in the Syriac.",
    "No /f v \\u03b8 \\u00f0 z/ distinctions survive (f->\\u314d like p, "
    "v->\\u3142 like b, \\u03b8->\\u3145 like s, \\u00f0->\\u3137 like d, "
    "z->\\u3148).",
    "l and r merge to a single \\u3139 (ㄹ).",
    "A glide + its homorganic vowel collapses to the bare vowel "
    "(ji->\\u3163 ㅣ, wu->\\u315c ㅜ); Korean has no distinct *yi / *wu medial.",
    "The Korean 3-way laryngeal contrast (plain/tense/aspirated) cannot encode "
    "Syriac voicing; emphatics are approximated with tense jamo.",
    "Gutturals and emphatics are heavily approximated "
    "(x/\\u0127/h->\\u314e, \\u0294/\\u0295 dropped, q->\\u314b like k, "
    "\\u0263->\\u3131 like g).  A syllable-final /h/-class consonant is emitted "
    "as its own \\u314e+\\u3161 (heu) syllable, not as a non-occurring "
    "\\u314e batchim.",
    "\\u0283 (ʃ) -> \\u3145; before a back/low vowel it takes a y-glide medial "
    "(ʃa->\\uc0e4 샤, ʃo->\\uc1fc 쇼, ʃu->\\uc288 슈) for the "
    "palatal [\\u0255] 'sh' allophone.",
    "Romanized (RR) uses NO cross-syllable sandhi (per-syllable readback only) "
    "and neutralizes every coda (e.g. final \\u314e reads back as 't').",
    "The Hangul and Romanized reader tiers are NOT reversible.",
]


def build_mapping_dict():
    """Build the JSON-serializable mirror of all tables + rules + limitations."""
    consonants_sp = {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                     for ch, v in CONSONANTS.items()}
    short_vowels_sp = {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                       for ch, v in SHORT_VOWELS.items()}
    long_vowels_sp = {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                      for ch, v in LONG_VOWELS.items()}
    emphatics_explicit_sp = {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                             for ch, v in EMPHATICS_EXPLICIT.items()}

    return {
        "meta": {
            "description": "Deterministic four-tier IPA transliteration for the "
                           "Korean Peshitta corpus.",
            "tiers": list(TIERS),
            "note": "transliterate_ko.py is authoritative; this file mirrors its "
                    "hard-coded tables. Scholarly/Pretty are byte-identical to "
                    "the English Peshitta.",
        },
        "unicode": {
            "emphatic_marker": SUPER_RHOTIC,
            "length_mark": LENGTH_MARK,
            "combining_dot_below": COMBINING_DOT_BELOW,
            "alaph": ALAPH,
            "ayin": AYIN,
            "hyphen": HYPHEN,
        },
        "segmentation": [
            "Split on ASCII space ' ' only; spaces are preserved verbatim.",
            "Within each token, left-to-right longest match:",
            "  1. consonant + \\u02E4 (ˤ) -> emphatic segment (2 chars)",
            "  2. vowel (a ɑ e i o u) + \\u02D0 (ː) -> long-vowel segment",
            "  3. otherwise single char",
            "word-initial = the FIRST segment of a token (Scholarly/Pretty Alaph rule).",
        ],
        "scholarly_pretty": {
            "note": "Reproduced verbatim from English/Peshita_English/"
                    "transliterate.py; output is byte-identical to the English "
                    "Scholarly/Pretty tiers.",
            "tier_dicts": {
                "consonants": consonants_sp,
                "short_vowels": short_vowels_sp,
                "long_vowels": long_vowels_sp,
                "emphatics_explicit": emphatics_explicit_sp,
            },
            "rules": {
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
                "hyphen": {"symbol": HYPHEN, "all_tiers": "-"},
                "space": {"all_tiers": "space (preserved verbatim)"},
                "unmapped": "Any char not covered above (besides space) is "
                            "recorded and passed through unchanged.",
            },
        },
        "hangul": {
            "jamo_orders": {
                "choseong": CHO,
                "jungseong": JUNG,
                "jongseong": JONG_LIST,
            },
            "compose_formula": "syllable = 0xAC00 + cho*588 + jung*28 + jong",
            "consonant_jamo": dict(CONS_JAMO),
            "emphatic_jamo": dict(EMPH_JAMO),
            "theta_jamo": THETA_JAMO,
            "vowel_jamo": dict(VOW_JAMO),
            "glides": sorted(GLIDES),
            "compound_medials": {"%s+%s" % k: v for k, v in COMPOUND.items()},
            "coda_neutralization": dict(CODA_NEUTRAL),
            "epenthetic_vowel": EPENTHETIC_VOWEL,
            "silent_onset": SILENT_ONSET,
            "dropped": {"alaph": ALAPH, "ayin": AYIN,
                        "note": "\\u0294/\\u0295 are dropped (boundary/silent)."},
            "syllabification": [
                "Map each IPA segment to jamo (length collapsed; glide+vowel -> "
                "compound medial).",
                "Pack into legal (C)(G)V(C) blocks: no onset clusters, no illegal "
                "codas -> insert epenthetic \\u3161 (ㅡ).",
                "Vowel-initial syllable uses silent onset \\u3147 (ㅇ).",
                "Codas are neutralized (ㄸㅃㅉ have no jongseong slot).",
            ],
        },
        "romanized": {
            "note": "Revised-Romanization (RR) readback of the generated Hangul, "
                    "per syllable, with NO cross-syllable sandhi.",
            "rr_cho": list(RR_CHO),
            "rr_jung": list(RR_JUNG),
            "rr_jong": list(RR_JONG),
        },
        "documented_limitations": DOCUMENTED_LIMITATIONS,
    }


def write_mapping_json(path=MAPPING_JSON):
    data = build_mapping_dict()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path


# ===========================================================================
# Gold cases
#   Scholarly/Pretty expected values are the English gold (byte-identical).
#   Hangul/Romanized expected values were COMPUTED by this transducer and
#   pasted here so --selftest is a real regression lock for all four tiers.
# ===========================================================================
GOLD_CASES = [
    {
        "ref": "John 1:1",
        "ipa": "breːʃiːθ ʔiːθawj wɑː melθɑː whuː melθɑː ʔiːθawj wɑː lwɑːθ ʔɑːlɑːhɑː waʔlɑːhɑː ʔiːθawj wɑː huː melθɑː",
        "scholarly": "brēšīṯ ʾīṯawy wā melṯā whū melṯā ʾīṯawy wā lwāṯ ʾālāhā waʾlāhā ʾīṯawy wā hū melṯā",
        "pretty": "brēshīth īthawy wā melthā whū melthā īthawy wā lwāth ālāhā wa'lāhā īthawy wā hū melthā",
        "hangul": "브레싯 이사우이 와 멜사 우후 멜사 이사우이 와 뢋 아라하 와라하 이사우이 와 후 멜사",
        "romanized": "beuresit isaui wa melsa uhu melsa isaui wa rwat araha waraha isaui wa hu melsa",
    },
    {
        "ref": "John 1:2",
        "ipa": "hɑːnɑː ʔiːθawj wɑː breːʃiːθ lwɑːθ ʔɑːlɑːhɑː",
        "scholarly": "hānā ʾīṯawy wā brēšīṯ lwāṯ ʾālāhā",
        "pretty": "hānā īthawy wā brēshīth lwāth ālāhā",
        "hangul": "하나 이사우이 와 브레싯 뢋 아라하",
        "romanized": "hana isaui wa beuresit rwat araha",
    },
    {
        "ref": "John 1:3",
        "ipa": "kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː",
        "scholarly": "kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā",
        "pretty": "kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā",
        "hangul": "쿨 비이데흐 화 우베라다우이 앞라 흐다 홧 메뎀 다화",
        "romanized": "kul biideheu hwa uberadaui apra heuda hwat medem dahwa",
    },
    {
        "ref": "Matthew 1:1",
        "ipa": "kθɑːvɑː diːliːðuːθeh djeʃuːʕ mʃiːħɑː breh dðawiːð breh dʔavrɑːhɑːm",
        "scholarly": "kṯāḇā dīlīḏūṯeh dyešūʿ mšīḥā breh dḏawīḏ breh dʾaḇrāhām",
        "pretty": "kthāvā dīlīdhūtheh dyeshūʿ mshīḥā breh ddhawīdh breh d'avrāhām",
        "hangul": "크사바 디리두세흐 뎨슈 므시하 브레흐 드다윋 브레흐 답라함",
        "romanized": "keusaba diriduseheu dyesyu meusiha beureheu deudawit beureheu dapraham",
    },
    {
        "ref": "Romans 1:1",
        "ipa": "pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː",
        "scholarly": "pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā",
        "pretty": "pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā",
        "hangul": "파우라웃 압다 뎨슈 므시하 카랴 왓리하 뎃프렛 레완게리이야운 다라하",
        "romanized": "pauraut apda dyesyu meusiha karya watriha detpeuret rewangeriiyaun daraha",
    },
    {
        "ref": "Matthew 27:16 (Barabbas)",
        "ipa": "dmeθqre bar-ʔaba lvar-ʔaba lvar-ʔava",
        "scholarly": "dmeṯqre bar-ʾaba lḇar-ʾaba lḇar-ʾaḇa",
        "pretty": "dmethqre bar-'aba lvar-'aba lvar-'ava",
        "hangul": "드멧크레 발-아바 르발-아바 르발-아바",
        "romanized": "deumetkeure bal-aba reubal-aba reubal-aba",
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
                print("PASS  %-26s %-10s" % (ref, tier))
            else:
                all_pass = False
                print("FAIL  %-26s %-10s" % (ref, tier))
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
                mismatches.append({"ref": ref, "tier": tier,
                                   "expected": expected, "got": got})
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


def run_coverage(root=IPA_ROOT):
    """
    Scan every *_ipa.txt under root; transliterate verse text in all four tiers,
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


# ===========================================================================
# Build
# ===========================================================================
def _out_path_for(ipa_path, tier):
    """
    Map an IPA source path to the output path for a tier.
      IPA/Peshitta/<Book>/<name>_ipa.txt
      -> Korean/Peshita_Korean/<Tier>/<Book>/<name>_<tier>.txt
    """
    rel = os.path.relpath(ipa_path, IPA_ROOT)        # <Book>/<name>_ipa.txt
    book_dir = os.path.dirname(rel)
    base = os.path.basename(rel)
    assert base.endswith("_ipa.txt"), base
    name = base[:-len("_ipa.txt")]                   # <name>
    out_name = "%s_%s.txt" % (name, tier)
    return os.path.join(KOREAN_ROOT, TIER_DIR_NAME[tier], book_dir, out_name)


def run_build(root=IPA_ROOT):
    """Transliterate the whole corpus into the four Korean tier trees."""
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


# ===========================================================================
# CLI
# ===========================================================================
def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Deterministic four-tier IPA transliterator for the Korean "
                    "Peshitta corpus."
    )
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--selftest", action="store_true",
                   help="run embedded gold cases (all 4 tiers)")
    g.add_argument("--coverage", action="store_true",
                   help="report chars not in mapping")
    g.add_argument("--build", action="store_true",
                   help="transliterate whole corpus -> Korean tree")
    g.add_argument("--write-mapping", action="store_true",
                   help="(re)write transliteration_mapping_ko.json")
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
