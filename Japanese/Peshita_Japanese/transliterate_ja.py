#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deterministic IPA -> (Latin + Japanese kana) transliterator for the Peshitta corpus.

FIVE tiers:
    SCHOLARLY | PRETTY | KATAKANA | HIRAGANA | ROMAJI(Hepburn)

  * SCHOLARLY + PRETTY are LANGUAGE-NEUTRAL Latin renderings, reproduced
    BYTE-FOR-BYTE from the English Peshitta transducer
    (English/Peshita_English/transliterate.py).  They share the exact same
    hard-coded tables and rendering rules, so for any IPA input the scholarly
    and pretty output of this module is identical to the English module's.

  * KATAKANA | HIRAGANA | ROMAJI are the Japanese "reader tiers".  They render
    the Syriac IPA into Japanese sound-units (mora) using the algorithm
    documented below.  KATAKANA (the foreign-word script) is the primary tier;
    HIRAGANA gives the same mora in native glyphs; ROMAJI is a Hepburn-style
    readback of the same mora.

This file is AUTHORITATIVE for the Japanese corpus.  A machine-readable copy of
all tables, rules and limitations is exported to transliteration_mapping_ja.json
(see build_mapping_dict() / write_mapping_json()).

------------------------------------------------------------------------------
KANA READER-TIER ALGORITHM
------------------------------------------------------------------------------
Japanese is strictly MORAIC.  A mora is one of:
    (C)(j)V          a (optionally consonant-, optionally glide-) onset + vowel
    N                the moraic nasal  ン / ん
    Q                the sokuon (geminating pause) -- not produced here
    a long-vowel part (chōonpu ー  /  doubled vowel  /  macron)

There are NO consonant clusters and NO codas other than the moraic nasal.  To
render Syriac (which has clusters, codas, gutturals and emphatics) we must:

  1. MAP each IPA segment to a Japanese mora:
        consonant + vowel        -> the CV kana       (e.g. /ka/ -> カ)
        vowel alone              -> a vowel kana       (e.g. /a/  -> ア)
        on-glide /j/,/w/ + vowel -> y-row / w-row kana (or yōon)
        /ʔ/ (alaph) and /ʕ/ (ayin) are DROPPED.

  2. EPENTHESIZE: a consonant with no following vowel is given an epenthetic
     vowel, forming a CV mora.  Default epenthetic vowel is /u/ (ク, ス, ...),
     but /o/ after t and d (ト, ド), and /ʃ/ becomes シュ.  A *coda* /n/ -- one
     that closes a syllable, i.e. immediately preceded by a vowel -- becomes the
     moraic nasal ン (NOT ヌ).  An *onset* /n/ with no preceding vowel (e.g. the
     imperfect prefix n- in /nquːm/, /njɑːħɑː/) is NOT ン -- a Japanese mora may
     never BEGIN with ン -- so it epenthesizes to ヌ/nu like any other onset
     consonant.

  3. LONG VOWELS (Vː):
        katakana  -> append the chōonpu  ー
        hiragana  -> double the vowel    (あ い う え お)
        romaji    -> macron              (ā ī ū ē ō)

  4. THREE reader tiers are produced from the SAME mora parse:
        KATAKANA  カタカナ  -- idiomatic foreign-word script (primary)
        HIRAGANA  ひらがな  -- same mora, native glyphs
        ROMAJI              -- Hepburn readback (shi/chi/tsu/fu/ji, macrons)
     The ROMAJI tier is constrained to a strict charset (ASCII letters, the
     macron long vowels ā ī ū ē ō, space, hyphen, digit, tab).  Standard
     Hepburn would insert an apostrophe after the moraic nasal 'n' before a
     vowel- or y-initial syllable (メンイ -> "men'i"); because U+0027 is not in
     the allowed charset, this build does NOT emit it -- the moraic nasal is a
     bare 'n' (メンイ -> "meni").  The ン/ん boundary is still shown in the
     Katakana/Hiragana tiers, so the disambiguation survives in the build.

IPA -> kana category (draft, finalized in the reference seed):
    b->b  v->v(ヴ)  p->p  f->f(ファ row)  t->t(タ ティ トゥ テ ト)  tˤ->t
    d->d(ダ ディ ドゥ デ ド)  ð->z  k->k  ɡ,ɣ->g  q->k
    s,sˤ,θ->s(サ シ ス セ ソ)  z->z  ʃ->sh(シャ シ シュ シェ ショ)
    x,ħ,h->h(ハ ヒ フ ヘ ホ)  m->m  n->n(coda -> ン)  l,r->r(ラ行)
    w->w-row  j->y-row(or yōon).
    Vowels  a,ɑ->ア  e->エ  i->イ  o->オ  u->ウ.

------------------------------------------------------------------------------
LIMITATIONS  (read me!)
------------------------------------------------------------------------------
The kana tiers are an APPROXIMATION and are NOT reversible:
  * Heavy forced vowel epenthesis inflates length (every coda/cluster grows a
    vowel), so the kana is markedly longer than the source.
  * No /θ ð f v z ʃ/ vs plain-stop distinctions survive cleanly: θ, s and sˤ all
    collapse to the サ row and ð and z both collapse to the ザ row.  Note this is
    a full MERGER, not an approximation: θ and s become true homographs in kana
    (melθɑː and a hypothetical melsɑː both -> メルサー), and likewise ð and z.
  * l and r MERGE to the ラ行 (Japanese has a single liquid).
  * Gutturals / emphatics / glottals are approximated or DROPPED: x, ħ, h all
    map to the ハ row; emphasis (ˤ) is lost; ʔ (alaph) and ʕ (ayin) are dropped.
  * Pitch accent and fine vowel quality are NOT represented (a and ɑ merge).
  * Hiragana for foreign text is UNIDIOMATIC (katakana is the natural script for
    loanwords); the hiragana tier is provided because it was explicitly
    requested, as a same-mora native-glyph readback.

SCHOLARLY and PRETTY have no such caveats -- they are the language-neutral Latin
renderings shared verbatim with the English corpus.

------------------------------------------------------------------------------
CLI
------------------------------------------------------------------------------
    transliterate_ja.py --selftest        run the embedded gold cases (5 tiers)
    transliterate_ja.py --coverage        scan every *_ipa.txt for unmapped chars
    transliterate_ja.py --build           transliterate the whole corpus -> 5 trees
    transliterate_ja.py --write-mapping   (re)write transliteration_mapping_ja.json

Public API:
    transliterate(text, tier) -> str
    transliterate_line(line, tier) -> str

Author: Shin
"""

import os
import sys
import json
import argparse

# ---------------------------------------------------------------------------
# Paths -- resolved from THIS file (no absolute paths baked in), exactly like
# the English/Korean transducers, so the shipped copy works from
# Japanese/Peshita_Japanese/.
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
IPA_ROOT = os.path.join(REPO_ROOT, "IPA", "Peshitta")
JAPANESE_ROOT = os.path.join(REPO_ROOT, "Japanese", "Peshita_Japanese")
MAPPING_JSON = os.path.join(SCRIPT_DIR, "transliteration_mapping_ja.json")

# ---------------------------------------------------------------------------
# Unicode codepoints used in the SPEC (named for clarity)
# ---------------------------------------------------------------------------
SUPER_RHOTIC = "ˤ"          # U+02E4 modifier letter small reversed glottal stop (emphatic marker)
LENGTH_MARK = "ː"           # U+02D0 modifier letter triangular colon (long vowel)
COMBINING_DOT_BELOW = "̣"    # U+0323 combining dot below (generic emphatic fallback)
CHOONPU = "ー"              # U+30FC katakana-hiragana prolonged sound mark

# IPA source symbols
G_VOICED = "ɡ"   # U+0261 latin small letter script g
V_LABIO = "v"
F_LABIO = "f"
SH = "ʃ"
THETA = "θ"
ETH = "ð"
X_VELAR = "x"
GAMMA = "ɣ"
HBAR = "ħ"
J_PALATAL = "j"
ALAPH = "ʔ"      # glottal stop
AYIN = "ʕ"       # voiced pharyngeal
A_FRONT = "a"
ALPHA = "ɑ"      # open back unrounded

HYPHEN = "-"
SPACE = " "

# ---------------------------------------------------------------------------
# Tier names
# ---------------------------------------------------------------------------
SCHOLARLY = "scholarly"
PRETTY = "pretty"
KATAKANA = "katakana"
HIRAGANA = "hiragana"
ROMAJI = "romaji"
TIERS = (SCHOLARLY, PRETTY, KATAKANA, HIRAGANA, ROMAJI)

# Output directory name per tier (capitalized).
TIER_DIR_NAME = {
    SCHOLARLY: "Scholarly",
    PRETTY: "Pretty",
    KATAKANA: "Katakana",
    HIRAGANA: "Hiragana",
    ROMAJI: "Romaji",
}

# ===========================================================================
# SCHOLARLY / PRETTY  --  reproduced VERBATIM from the English transducer.
# Tuple order = (scholarly, pretty).  These tables and the _sp_* renderers
# below produce byte-for-byte identical output to English/Peshita_English/
# transliterate.py for the scholarly and pretty tiers.
# ===========================================================================
CONSONANTS_SP = {
    "b":        ("b", "b"),
    G_VOICED:   ("g", "g"),
    "d":        ("d", "d"),
    "h":        ("h", "h"),
    "w":        ("w", "w"),
    "z":        ("z", "z"),
    "k":        ("k", "k"),
    "l":        ("l", "l"),
    "m":        ("m", "m"),
    "n":        ("n", "n"),
    "s":        ("s", "s"),
    "p":        ("p", "p"),
    "q":        ("q", "q"),
    "r":        ("r", "r"),
    "t":        ("t", "t"),
    F_LABIO:    ("f", "f"),
    V_LABIO:    ("ḇ", "v"),    # ḇ | v
    SH:         ("š", "sh"),   # š | sh
    THETA:      ("ṯ", "th"),   # ṯ | th
    ETH:        ("ḏ", "dh"),   # ḏ | dh
    X_VELAR:    ("ḵ", "kh"),   # ḵ | kh
    GAMMA:      ("ḡ", "gh"),   # ḡ | gh
    HBAR:       ("ḥ", "ḥ"),    # ḥ | ḥ
    J_PALATAL:  ("y", "y"),
}

SHORT_VOWELS_SP = {
    A_FRONT: ("a", "a"),
    ALPHA:   ("a", "a"),
    "e":     ("e", "e"),
    "i":     ("i", "i"),
    "o":     ("o", "o"),
    "u":     ("u", "u"),
}

LONG_VOWELS_SP = {
    A_FRONT: ("ā", "ā"),
    ALPHA:   ("ā", "ā"),
    "e":     ("ē", "ē"),
    "i":     ("ī", "ī"),
    "o":     ("ō", "ō"),
    "u":     ("ū", "ū"),
}
LONG_VOWEL_BASES = set(LONG_VOWELS_SP.keys())

EMPHATICS_EXPLICIT_SP = {
    "t": ("ṭ", "ṭ"),
    "s": ("ṣ", "ṣ"),
}

_SP_IDX = {SCHOLARLY: 0, PRETTY: 1}


def _sp_segment_token(token):
    """Segment a token for the scholarly/pretty tiers (longest match)."""
    segs = []
    i = 0
    n = len(token)
    while i < n:
        ch = token[i]
        nxt = token[i + 1] if i + 1 < n else None
        if nxt == SUPER_RHOTIC and ch in CONSONANTS_SP:
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


def _sp_render_segment(seg, tier, is_word_initial, unmapped):
    """Render one segment for the scholarly/pretty tiers (English logic)."""
    idx = _SP_IDX[tier]

    # Emphatic segment (consonant + ˤ)
    if len(seg) == 2 and seg[1] == SUPER_RHOTIC:
        base = seg[0]
        explicit = EMPHATICS_EXPLICIT_SP.get(base)
        if explicit is not None:
            return explicit[idx]
        entry = CONSONANTS_SP.get(base)
        if entry is None:
            unmapped.add(base)
            return base
        return entry[idx] + COMBINING_DOT_BELOW

    # Long-vowel segment (V + ː)
    if len(seg) == 2 and seg[1] == LENGTH_MARK:
        entry = LONG_VOWELS_SP.get(seg[0])
        if entry is not None:
            return entry[idx]
        unmapped.add(seg[0])
        return seg

    ch = seg
    sv = SHORT_VOWELS_SP.get(ch)
    if sv is not None:
        return sv[idx]
    cons = CONSONANTS_SP.get(ch)
    if cons is not None:
        return cons[idx]
    if ch == ALAPH:
        if tier == SCHOLARLY:
            return "ʾ"
        return "" if is_word_initial else "'"
    if ch == AYIN:
        return "ʿ"
    if ch == HYPHEN:
        return "-"
    if ch == SPACE:
        return " "
    unmapped.add(ch)
    return ch


def _sp_transliterate(text, tier, unmapped):
    """Scholarly/Pretty rendering -- byte-identical to the English transducer."""
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
# KANA tables and rules (KATAKANA | HIRAGANA | ROMAJI)
# ===========================================================================
# Per-category mora table: category -> {vowel: (katakana, hiragana, hepburn)}.
# The empty-string category "" is the bare-vowel / glide-fallback row.
VOWELS = ["a", "i", "u", "e", "o"]
KANA = {
    "":   {"a": ("ア", "あ", "a"),   "i": ("イ", "い", "i"),     "u": ("ウ", "う", "u"),    "e": ("エ", "え", "e"),     "o": ("オ", "お", "o")},
    "k":  {"a": ("カ", "か", "ka"),  "i": ("キ", "き", "ki"),    "u": ("ク", "く", "ku"),   "e": ("ケ", "け", "ke"),    "o": ("コ", "こ", "ko")},
    "g":  {"a": ("ガ", "が", "ga"),  "i": ("ギ", "ぎ", "gi"),    "u": ("グ", "ぐ", "gu"),   "e": ("ゲ", "げ", "ge"),    "o": ("ゴ", "ご", "go")},
    "s":  {"a": ("サ", "さ", "sa"),  "i": ("シ", "し", "shi"),   "u": ("ス", "す", "su"),   "e": ("セ", "せ", "se"),    "o": ("ソ", "そ", "so")},
    "z":  {"a": ("ザ", "ざ", "za"),  "i": ("ジ", "じ", "ji"),    "u": ("ズ", "ず", "zu"),   "e": ("ゼ", "ぜ", "ze"),    "o": ("ゾ", "ぞ", "zo")},
    "sh": {"a": ("シャ", "しゃ", "sha"), "i": ("シ", "し", "shi"), "u": ("シュ", "しゅ", "shu"), "e": ("シェ", "しぇ", "she"), "o": ("ショ", "しょ", "sho")},
    "t":  {"a": ("タ", "た", "ta"),  "i": ("ティ", "てぃ", "ti"), "u": ("トゥ", "とぅ", "tu"), "e": ("テ", "て", "te"),    "o": ("ト", "と", "to")},
    "d":  {"a": ("ダ", "だ", "da"),  "i": ("ディ", "でぃ", "di"), "u": ("ドゥ", "どぅ", "du"), "e": ("デ", "で", "de"),    "o": ("ド", "ど", "do")},
    "n":  {"a": ("ナ", "な", "na"),  "i": ("ニ", "に", "ni"),    "u": ("ヌ", "ぬ", "nu"),   "e": ("ネ", "ね", "ne"),    "o": ("ノ", "の", "no")},
    "h":  {"a": ("ハ", "は", "ha"),  "i": ("ヒ", "ひ", "hi"),    "u": ("フ", "ふ", "fu"),   "e": ("ヘ", "へ", "he"),    "o": ("ホ", "ほ", "ho")},
    "f":  {"a": ("ファ", "ふぁ", "fa"), "i": ("フィ", "ふぃ", "fi"), "u": ("フ", "ふ", "fu"), "e": ("フェ", "ふぇ", "fe"), "o": ("フォ", "ふぉ", "fo")},
    "b":  {"a": ("バ", "ば", "ba"),  "i": ("ビ", "び", "bi"),    "u": ("ブ", "ぶ", "bu"),   "e": ("ベ", "べ", "be"),    "o": ("ボ", "ぼ", "bo")},
    "p":  {"a": ("パ", "ぱ", "pa"),  "i": ("ピ", "ぴ", "pi"),    "u": ("プ", "ぷ", "pu"),   "e": ("ペ", "ぺ", "pe"),    "o": ("ポ", "ぽ", "po")},
    "m":  {"a": ("マ", "ま", "ma"),  "i": ("ミ", "み", "mi"),    "u": ("ム", "む", "mu"),   "e": ("メ", "め", "me"),    "o": ("モ", "も", "mo")},
    "v":  {"a": ("ヴァ", "ゔぁ", "va"), "i": ("ヴィ", "ゔぃ", "vi"), "u": ("ヴ", "ゔ", "vu"), "e": ("ヴェ", "ゔぇ", "ve"), "o": ("ヴォ", "ゔぉ", "vo")},
    "r":  {"a": ("ラ", "ら", "ra"),  "i": ("リ", "り", "ri"),    "u": ("ル", "る", "ru"),   "e": ("レ", "れ", "re"),    "o": ("ロ", "ろ", "ro")},
    "y":  {"a": ("ヤ", "や", "ya"),  "i": ("イ", "い", "i"),     "u": ("ユ", "ゆ", "yu"),   "e": ("イェ", "いぇ", "ye"), "o": ("ヨ", "よ", "yo")},
    "w":  {"a": ("ワ", "わ", "wa"),  "i": ("ウィ", "うぃ", "wi"), "u": ("ウ", "う", "u"),    "e": ("ウェ", "うぇ", "we"), "o": ("ウォ", "うぉ", "wo")},
}

# IPA consonant -> kana category.
CAT = {
    "b": "b", "v": "v", "p": "p", "f": "f",
    "t": "t", "d": "d", "ð": "z",
    "k": "k", "ɡ": "g", "ɣ": "g", "q": "k",
    "s": "s", "z": "z", "ʃ": "sh",
    "x": "h", "ħ": "h", "h": "h",
    "m": "m", "n": "n", "l": "r", "r": "r",
}
EMPH_CAT = {"t": "t", "s": "s"}   # tˤ, sˤ -> t, s (emphasis lost)
THETA_CAT = "s"                   # θ -> サ row
VOWBASE = {"a": "a", "ɑ": "a", "e": "e", "i": "i", "o": "o", "u": "u"}
EPV = {"t": "o", "d": "o"}        # epenthetic vowel by category (default 'u')
MACRON = {"a": "ā", "i": "ī", "u": "ū", "e": "ē", "o": "ō"}
HIRA_LONG = {"a": "あ", "i": "い", "u": "う", "e": "え", "o": "お"}

_KANA_WHICH = {KATAKANA: 0, HIRAGANA: 1, ROMAJI: 2}


def _kana_segment_token(token):
    """Segment a token into IPA segments for the kana tiers (longest match)."""
    segs = []
    i = 0
    n = len(token)
    while i < n:
        ch = token[i]
        nxt = token[i + 1] if i + 1 < n else None
        if nxt == SUPER_RHOTIC and (ch in CAT or ch in EMPH_CAT):
            segs.append(ch + SUPER_RHOTIC)
            i += 2
            continue
        if nxt == LENGTH_MARK and ch in VOWBASE:
            segs.append(ch + LENGTH_MARK)
            i += 2
            continue
        segs.append(ch)
        i += 1
    return segs


def _is_vowel_seg(seg):
    base = seg[0] if (len(seg) == 2 and seg[1] == LENGTH_MARK) else seg
    return base in VOWBASE


def _vowel_info(seg):
    """Return (vowel_base, is_long) for a vowel segment."""
    if len(seg) == 2 and seg[1] == LENGTH_MARK:
        return VOWBASE[seg[0]], True
    return VOWBASE[seg], False


def _consonant_category(seg, unmapped):
    """Return the kana category for a consonant segment, or None."""
    if len(seg) == 2 and seg[1] == SUPER_RHOTIC:
        base = seg[0]
        if base in EMPH_CAT:
            return EMPH_CAT[base]
        if base in CAT:
            return CAT[base]
        unmapped.add(base)
        return None
    if seg == THETA:
        return THETA_CAT
    if seg in CAT:
        return CAT[seg]
    return None


def _moras(token, unmapped):
    """
    Parse one token into render-ready mora units.  Mora unit forms:
      ("cv", category, vowel, is_long)          a CV (or V) mora
      ("cv", "", None, False, fixed_vowel)      a standalone glide -> bare vowel
      ("N",)                                     the moraic nasal
      ("sep",)                                   a hyphen separator
    """
    segs = _kana_segment_token(token)
    out = []
    i = 0
    n = len(segs)
    while i < n:
        s = segs[i]
        # Drop glottals (alaph / ayin).
        if s in (ALAPH, AYIN):
            i += 1
            continue
        if s == HYPHEN:
            out.append(("sep",))
            i += 1
            continue
        if _is_vowel_seg(s):
            base, lo = _vowel_info(s)
            out.append(("cv", "", base, lo))
            i += 1
            continue
        if s == J_PALATAL:
            if i + 1 < n and _is_vowel_seg(segs[i + 1]):
                base, lo = _vowel_info(segs[i + 1])
                out.append(("cv", "y", base, lo))
                i += 2
                continue
            out.append(("cv", "", None, False, "i"))   # standalone /j/ -> i
            i += 1
            continue
        if s == "w":
            if i + 1 < n and _is_vowel_seg(segs[i + 1]):
                base, lo = _vowel_info(segs[i + 1])
                out.append(("cv", "w", base, lo))
                i += 2
                continue
            out.append(("cv", "", None, False, "u"))   # standalone /w/ -> u
            i += 1
            continue
        cat = _consonant_category(s, unmapped)
        if cat is None:
            if s not in (SUPER_RHOTIC, LENGTH_MARK):
                unmapped.add(s)
            i += 1
            continue
        # Consonant + following vowel -> a single CV mora.
        if i + 1 < n and _is_vowel_seg(segs[i + 1]):
            base, lo = _vowel_info(segs[i + 1])
            out.append(("cv", cat, base, lo))
            i += 2
            continue
        # Coda / cluster -> epenthesis.
        # A GENUINE coda /n/ (one that closes a syllable, i.e. immediately
        # preceded by a vowel-bearing CV mora) becomes the moraic nasal ン.
        # But an ONSET /n/ with no preceding vowel -- word-initial or
        # cluster-initial, e.g. the imperfect prefix n- in /nquːm/, /nettaɡron/ --
        # CANNOT be ン (a Japanese mora may not BEGIN with ン).  Such an onset
        # /n/ epenthesizes to ヌ/nu like any other onset consonant.
        if cat == "n":
            if out and out[-1][0] == "cv":
                out.append(("N",))
                i += 1
                continue
            # onset /n/ with no preceding vowel -> ヌ (default epenthesis)
        out.append(("cv", cat, EPV.get(cat, "u"), False))
        i += 1
    return out


def _render_moras(moras, which):
    """Render a mora list to a tier (which: 0=katakana, 1=hiragana, 2=romaji)."""
    out = []
    for m in moras:
        if m[0] == "sep":
            out.append("-")
            continue
        if m[0] == "N":
            out.append(("ン", "ん", "n")[which])
            continue
        # m[0] == "cv"
        if len(m) == 5:
            # standalone glide stored as ("cv","",None,False,fixed_vowel)
            v = m[4]
            out.append(KANA[""][v][which])
            continue
        _, cat, v, lo = m
        base = KANA[cat][v][which]
        if lo:
            if which == 0:
                base += CHOONPU
            elif which == 1:
                base += HIRA_LONG[v]
            else:
                base = base[:-1] + MACRON[v]
        out.append(base)

    # NOTE on the moraic nasal before a vowel/y in ROMAJI:
    # Standard Hepburn disambiguates a moraic nasal 'n' from a following
    # vowel- or y-initial syllable with an apostrophe (メンイ -> "men'i", not
    # "meni" = メニ).  This corpus, however, constrains the Romaji tier to a
    # strict charset -- ASCII letters, the macron long vowels (ā ī ū ē ō),
    # space, hyphen, digit and tab -- which does NOT include the apostrophe
    # U+0027.  We therefore do NOT emit the Hepburn apostrophe: the moraic
    # nasal is rendered as a bare 'n' in every position.  The visual ン/ん
    # boundary is still preserved in the Katakana and Hiragana tiers (the
    # primary reader tiers), so no information is lost from the build as a
    # whole; only the Latin readback omits the disambiguating mark, which is
    # consistent with the Romaji tier being a documented, non-reversible
    # approximation.  (The hyphen, the only charset-allowed Hepburn
    # alternative, is reserved as the word-internal separator -- e.g.
    # baru-aba for bar-ʔaba -- so it cannot double as the nasal break.)
    return "".join(out)


def _kana_transliterate(text, which, unmapped):
    """Render a whole text in a kana tier, preserving spaces verbatim."""
    return " ".join(
        _render_moras(_moras(t, unmapped), which) if t else ""
        for t in text.split(" ")
    )


# ===========================================================================
# Public API
# ===========================================================================
def transliterate(text, tier, unmapped=None):
    """
    Transliterate IPA `text` for the given `tier`, one of:
        "scholarly", "pretty", "katakana", "hiragana", "romaji".

    Splits on the ASCII space ' ' only; spaces are preserved verbatim.  The
    scholarly/pretty tiers reproduce the English transducer byte-for-byte; the
    katakana/hiragana/romaji tiers apply the moraic kana algorithm.

    If `unmapped` (a set) is supplied, any unmapped characters encountered are
    added to it (and passed through unchanged in the Latin tiers).
    """
    if tier not in TIERS:
        raise ValueError("Unknown tier: %r (expected one of %r)" % (tier, TIERS))
    if unmapped is None:
        unmapped = set()
    if tier in (SCHOLARLY, PRETTY):
        return _sp_transliterate(text, tier, unmapped)
    return _kana_transliterate(text, _KANA_WHICH[tier], unmapped)


def transliterate_line(line, tier, unmapped=None):
    """
    Transliterate a single corpus line of the form '<verse#>\\t<text>'.
    Keeps the '<verse#>\\t' prefix verbatim; only the text after the FIRST tab
    is transliterated.  Lines without a tab are returned unchanged.  A trailing
    newline (if any) is preserved.
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
    "Kana tiers are an approximation and are NOT reversible.",
    "Forced vowel epenthesis (default /u/, /o/ after t,d, /ʃ/ -> シュ) inflates length: "
    "every coda/cluster grows an extra vowel mora.",
    "No /θ ð f v z ʃ/ vs plain-stop distinctions survive cleanly: θ, s, sˤ collapse to "
    "the サ row and ð, z collapse to the ザ row. This is a full merger, so θ and s become "
    "true homographs in kana (melθɑː and melsɑː both -> メルサー), and likewise ð and z.",
    "l and r merge to the ラ行 (Japanese has a single liquid).",
    "Gutturals/emphatics/glottals are approximated or dropped: x, ħ, h -> ハ row; "
    "emphasis (ˤ) is lost; ʔ (alaph) and ʕ (ayin) are dropped.",
    "Pitch accent and fine vowel quality are not represented (a and ɑ merge).",
    "A coda /n/ (preceded by a vowel) becomes the moraic nasal ン (not ヌ); an onset "
    "/n/ with no preceding vowel (word/cluster-initial, e.g. the imperfect prefix n-) "
    "epenthesizes to ヌ/nu, because a Japanese mora may never begin with ン.",
    "Long vowels: katakana appends ー (chōonpu); hiragana doubles the vowel; "
    "romaji uses a macron (ā ī ū ē ō).",
    "Romaji is constrained to a strict charset (ASCII letters, macron long vowels ā ī ū ē ō, "
    "space, hyphen, digit, tab) and therefore does NOT emit the standard Hepburn apostrophe "
    "(U+0027) after the moraic nasal 'n' before a vowel- or y-initial syllable: メンイ -> 'meni', "
    "not 'men'i'. The ン/ん boundary is still visible in the katakana/hiragana tiers.",
    "Hiragana for foreign text is unidiomatic (katakana is the natural loanword script); "
    "it is provided as a same-mora native-glyph readback because it was requested.",
    "Scholarly and Pretty are the language-neutral Latin renderings shared byte-for-byte "
    "with the English Peshitta and carry none of these caveats.",
]


def build_mapping_dict():
    """Build the JSON-serializable mapping (all tables + rules + limitations)."""
    consonants_sp = {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                     for ch, v in CONSONANTS_SP.items()}
    short_vowels_sp = {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                       for ch, v in SHORT_VOWELS_SP.items()}
    long_vowels_sp = {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                      for ch, v in LONG_VOWELS_SP.items()}
    emphatics_sp = {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                    for ch, v in EMPHATICS_EXPLICIT_SP.items()}

    kana_table = {
        cat: {v: {KATAKANA: cell[0], HIRAGANA: cell[1], ROMAJI: cell[2]}
              for v, cell in rows.items()}
        for cat, rows in KANA.items()
    }

    return {
        "meta": {
            "description": "Deterministic IPA -> (Latin + Japanese kana) mapping for the Peshitta corpus.",
            "tiers": list(TIERS),
            "note": "transliterate_ja.py is authoritative; this file mirrors its hard-coded tables.",
            "scholarly_pretty_source": "Byte-for-byte identical to English/Peshita_English/transliterate.py.",
            "author": "Shin",
        },
        "unicode": {
            "emphatic_marker": SUPER_RHOTIC,        # ˤ
            "length_mark": LENGTH_MARK,             # ː
            "combining_dot_below": COMBINING_DOT_BELOW,
            "choonpu": CHOONPU,                     # ー
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
            "word-initial = the FIRST segment of a token (used by the Alaph rule in scholarly/pretty).",
        ],
        "scholarly_pretty": {
            "consonants": consonants_sp,
            "short_vowels": short_vowels_sp,
            "long_vowels": long_vowels_sp,
            "emphatics_explicit": emphatics_sp,
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
                "unmapped": "Any char not covered above (besides space) is recorded and passed through unchanged.",
            },
        },
        "kana": {
            "table": kana_table,
            "ipa_consonant_to_category": CAT,
            "emphatic_to_category": EMPH_CAT,
            "theta_to_category": THETA_CAT,
            "vowel_base": VOWBASE,
            "epenthetic_vowel": {"default": "u", "by_category": EPV, "note": "sh -> シュ via the sh-row 'u' cell"},
            "macron": MACRON,
            "hiragana_long_vowel": HIRA_LONG,
            "choonpu": CHOONPU,
            "rules": [
                "Map each IPA segment to a mora: C+V -> CV kana; V alone -> vowel kana; "
                "j/w + V -> y-row/w-row (or yōon).",
                "Drop ʔ (alaph) and ʕ (ayin).",
                "Standalone glide /j/ -> i, standalone /w/ -> u.",
                "A consonant with no following vowel gets an epenthetic vowel: default /u/, "
                "/o/ after t and d, /ʃ/ -> シュ.",
                "A coda /n/ (immediately preceded by a vowel) -> the moraic nasal ン (not ヌ); "
                "an onset /n/ with no preceding vowel (word/cluster-initial) -> ヌ/nu, since a "
                "Japanese mora may never begin with ン.",
                "Long vowels: katakana += ー; hiragana doubles the vowel; romaji uses a macron.",
                "Romaji charset is restricted (ASCII letters, macron long vowels ā ī ū ē ō, space, "
                "hyphen, digit, tab); the standard Hepburn apostrophe (U+0027) after a moraic nasal "
                "'n' before a vowel/y is NOT emitted (メンイ -> meni, not men'i). The ン/ん boundary "
                "is preserved in the katakana/hiragana tiers.",
                "Hyphen '-' is preserved as a separator.",
            ],
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
# ===========================================================================
# Scholarly/Pretty expected values are the ENGLISH gold (byte-identical).
# Katakana/Hiragana/Romaji expected values are COMPUTED by this transducer and
# pasted in, so --selftest is a real regression lock for all five tiers.
GOLD_CASES = [
    {
        "ref": "John 1:1",
        "ipa": "breːʃiːθ ʔiːθawj wɑː melθɑː whuː melθɑː ʔiːθawj wɑː lwɑːθ ʔɑːlɑːhɑː waʔlɑːhɑː ʔiːθawj wɑː huː melθɑː",
        "scholarly": "brēšīṯ ʾīṯawy wā melṯā whū melṯā ʾīṯawy wā lwāṯ ʾālāhā waʾlāhā ʾīṯawy wā hū melṯā",
        "pretty": "brēshīth īthawy wā melthā whū melthā īthawy wā lwāth ālāhā wa'lāhā īthawy wā hū melthā",
        "katakana": "ブレーシース イーサウイ ワー メルサー ウフー メルサー イーサウイ ワー ルワース アーラーハー ワラーハー イーサウイ ワー フー メルサー",
        "hiragana": "ぶれえしいす いいさうい わあ めるさあ うふう めるさあ いいさうい わあ るわあす ああらあはあ わらあはあ いいさうい わあ ふう めるさあ",
        "romaji": "burēshīsu īsaui wā merusā ufū merusā īsaui wā ruwāsu ārāhā warāhā īsaui wā fū merusā",
    },
    {
        "ref": "John 1:2",
        "ipa": "hɑːnɑː ʔiːθawj wɑː breːʃiːθ lwɑːθ ʔɑːlɑːhɑː",
        "scholarly": "hānā ʾīṯawy wā brēšīṯ lwāṯ ʾālāhā",
        "pretty": "hānā īthawy wā brēshīth lwāth ālāhā",
        "katakana": "ハーナー イーサウイ ワー ブレーシース ルワース アーラーハー",
        "hiragana": "はあなあ いいさうい わあ ぶれえしいす るわあす ああらあはあ",
        "romaji": "hānā īsaui wā burēshīsu ruwāsu ārāhā",
    },
    {
        "ref": "John 1:3",
        "ipa": "kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː",
        "scholarly": "kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā",
        "pretty": "kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā",
        "katakana": "クル ブイイゼフ フワー ウヴェルアーザウイ アーフラー フザー フワース メデム ダフワー",
        "hiragana": "くる ぶいいぜふ ふわあ うゔぇるああざうい ああふらあ ふざあ ふわあす めでむ だふわあ",
        "romaji": "kuru buiizefu fuwā uveruāzaui āfurā fuzā fuwāsu medemu dafuwā",
    },
    {
        "ref": "Matthew 1:1",
        "ipa": "kθɑːvɑː diːliːðuːθeh djeʃuːʕ mʃiːħɑː breh dðawiːð breh dʔavrɑːhɑːm",
        "scholarly": "kṯāḇā dīlīḏūṯeh dyešūʿ mšīḥā breh dḏawīḏ breh dʾaḇrāhām",
        "pretty": "kthāvā dīlīdhūtheh dyeshūʿ mshīḥā breh ddhawīdh breh d'avrāhām",
        "katakana": "クサーヴァー ディーリーズーセフ ドイェシュー ムシーハー ブレフ ドザウィーズ ブレフ ドアヴラーハーム",
        "hiragana": "くさあゔぁあ でぃいりいずうせふ どいぇしゅう むしいはあ ぶれふ どざうぃいず ぶれふ どあゔらあはあむ",
        "romaji": "kusāvā dīrīzūsefu doyeshū mushīhā burefu dozawīzu burefu doavurāhāmu",
    },
    {
        "ref": "Romans 1:1",
        "ipa": "pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː",
        "scholarly": "pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā",
        "pretty": "pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā",
        "katakana": "パウラーウス アヴダー ドイェシュー ムシーハー カルヤー ワシュリーハー ドエスプレシュ レワンゲリイヤーウン ドアーラーハー",
        "hiragana": "ぱうらあうす あゔだあ どいぇしゅう むしいはあ かるやあ わしゅりいはあ どえすぷれしゅ れわんげりいやあうん どああらあはあ",
        "romaji": "paurāusu avudā doyeshū mushīhā karuyā washurīhā doesupureshu rewangeriiyāun doārāhā",
    },
    {
        # Moraic-nasal-before-vowel/y regression lock: standard Hepburn would
        # write an apostrophe (an'yā, ...n'yā, ...an'i); this build emits a bare
        # 'n' in romaji because U+0027 is outside the romaji charset.  The ン/ん
        # boundary is still present in katakana/hiragana.  Real corpus tokens:
        # ʕanjɑː, daθmɑːnjɑː, ʔawdʕanj.
        "ref": "Moraic nasal (no Hepburn apostrophe)",
        "ipa": "ʕanjɑː daθmɑːnjɑː ʔawdʕanj",
        "scholarly": "ʿanyā daṯmānyā ʾawdʿany",
        "pretty": "ʿanyā dathmānyā awdʿany",
        "katakana": "アンヤー ダスマーンヤー アウドアンイ",
        "hiragana": "あんやあ だすまあんやあ あうどあんい",
        "romaji": "anyā dasumānyā audoani",
    },
    {
        "ref": "Matthew 27:16 (Barabbas)",
        "ipa": "dmeθqre bar-ʔaba lvar-ʔaba lvar-ʔava",
        "scholarly": "dmeṯqre bar-ʾaba lḇar-ʾaba lḇar-ʾaḇa",
        "pretty": "dmethqre bar-'aba lvar-'aba lvar-'ava",
        "katakana": "ドメスクレ バル-アバ ルヴァル-アバ ルヴァル-アヴァ",
        "hiragana": "どめすくれ ばる-あば るゔぁる-あば るゔぁる-あゔぁ",
        "romaji": "domesukure baru-aba ruvaru-aba ruvaru-ava",
    },
]


def run_selftest():
    """
    Run gold cases for all five tiers; print PASS/FAIL per (ref, tier) with
    diffs.  Returns (all_pass, mismatches).
    """
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


def run_coverage(root=IPA_ROOT):
    """
    Scan every *_ipa.txt under root; transliterate verse text in all five tiers,
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
      -> Japanese/Peshita_Japanese/<Tier>/<Book>/<name>_<tier>.txt
    """
    rel = os.path.relpath(ipa_path, IPA_ROOT)        # <Book>/<name>_ipa.txt
    book_dir = os.path.dirname(rel)
    base = os.path.basename(rel)
    assert base.endswith("_ipa.txt"), base
    name = base[:-len("_ipa.txt")]                   # <name>
    out_name = "%s_%s.txt" % (name, tier)
    return os.path.join(JAPANESE_ROOT, TIER_DIR_NAME[tier], book_dir, out_name)


def run_build(root=IPA_ROOT):
    """Transliterate the whole corpus into the five tier trees."""
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
        description="Deterministic IPA -> (Latin + Japanese kana) transliterator for the Peshitta corpus."
    )
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--selftest", action="store_true", help="run embedded gold cases (5 tiers)")
    g.add_argument("--coverage", action="store_true", help="report chars not in mapping")
    g.add_argument("--build", action="store_true", help="transliterate whole corpus -> 5 trees")
    g.add_argument("--write-mapping", action="store_true", help="(re)write transliteration_mapping_ja.json")
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
