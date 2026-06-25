#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deterministic IPA -> Chinese (Mandarin) transducer for the Peshitta corpus.

SIX tiers:
    SCHOLARLY | PRETTY | PINYIN(toneless) | ZHUYIN | HANZI-SIMPLIFIED | HANZI-TRADITIONAL

Architecture (see AI_Helping/chinese_design/CHINESE_DESIGN.md):
  KEY INVERSION. Hanzi is logographic and CANNOT phonetically spell foreign input, so
  PINYIN is the phonetic engine, ZHUYIN is a deterministic transcode of the pinyin, and
  HANZI is a DOWNSTREAM one-character-per-syllable lookup off the pinyin syllable stream
  (NON-faithful: it imposes a citation tone and a meaning).

  * SCHOLARLY / PRETTY are reproduced VERBATIM from the English transducer
    (English/Peshita_English/transliterate.py) and are byte-for-byte identical to it.
  * PINYIN: each IPA segment maps to a (Mandarin initial, nucleus, optional -n coda),
    then SNAPs to a LEGAL toneless Mandarin syllable. Mandarin has no consonant clusters
    and codas only -n/-ng (~400 toneless syllables), so stranded consonants get forced
    epenthesis (default 'e'; apical 'i' after z/c/s/zh/ch/sh/r) and g/k/h + i palatalize
    to j/q/x + i. Glottals (ʔ ʕ) drop. EVERY emitted pinyin syllable MUST be in the legal
    whitelist (a hard invariant, checked by --coverage).
  * ZHUYIN: standard deterministic pinyin<->bopomofo transcode (apical -i after the seven
    apical initials = the bare initial symbol; y/w zero-initial spellings restore the
    i-/u- medials).
  * HANZI: a frozen {simplified, traditional} character per produced syllable, drawn from
    the standard Xinhua 音译表 / 《世界人名翻译大辞典》 NEUTRAL transcription characters
    (semantically bleached: 巴 拉 西 斯 德 萨 阿 ...). The table shipped here is PARTIAL;
    the Sinology curation phase completes it. Syllables with no character render as '□' so
    that --coverage reports the exact remaining gap.

TONES are OMITTED in Pinyin/Zhuyin: the source IPA is atonal, so emitting a tone would
fabricate data. Hanzi unavoidably carries each glyph's citation tone -- that tone is an
ARTIFACT, documented below, and verifiable via strip_tones(hanzi -> pinyin) == toneless
syllable.

LIMITATIONS (loud, per the design study): Mandarin forces the heaviest collapse of any
target language in this project -- no clusters, codas only -n/-ng; voicing, emphatics,
gutturals, /v θ ð ʃ z/, vowel length, and the l/r distinction are all lost. Tones are
fabricated-then-omitted in Pinyin/Zhuyin and imposed-as-artifact in Hanzi. Hanzi imposes
MEANING and is NOT readback-grade: it cannot distinguish e.g. Barabba from Barava. The
output is NOT reversible.

Public API:
    transliterate(text, tier) -> str

CLI:
    transliterate_zh.py --selftest       run embedded gold cases, print per-(ref,tier)
    transliterate_zh.py --coverage       scan IPA corpus; report unmapped IPA, ANY illegal
                                         pinyin syllable, zhuyin gaps, and produced
                                         syllables missing a Hanzi character
    transliterate_zh.py --build          transliterate the whole corpus into the 6 tier trees
    transliterate_zh.py --write-mapping  (re)write transcription_mapping_zh.json
    transliterate_zh.py --verify-hanzi   strict tone-strip invariant: each glyph's DEFAULT
                                         (preferred) Mandarin reading, tones stripped, == its
                                         syllable key, for BOTH columns (optional pypinyin QA;
                                         SKIPPED-pass if pypinyin is not installed)

Author: Shin
"""

import os
import sys
import json
import argparse

# ===========================================================================
# Paths -- resolved from THIS file only (no absolute paths baked in)
#   <repo>/Chinese/Peshita_Chinese/transliterate_zh.py  ->  repo = ../..
# ===========================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
IPA_ROOT = os.path.join(REPO_ROOT, "IPA", "Peshitta")
CHINESE_ROOT = SCRIPT_DIR
MAPPING_JSON = os.path.join(SCRIPT_DIR, "transcription_mapping_zh.json")

# ===========================================================================
# Unicode codepoints used in the SPEC (named for clarity)
# ===========================================================================
SUPER_RHOTIC = "ˤ"            # ˤ  emphatic marker (modifier letter small reversed glottal stop)
LENGTH_MARK = "ː"             # ː  long-vowel marker (modifier letter triangular colon)
COMBINING_DOT_BELOW = "̣"      # ̣  combining dot below (generic emphatic fallback)
HYPHEN = "-"
SPACE = " "

# IPA source symbols
G_VOICED = "ɡ"   # ɡ  latin small letter script g
V_LABIO = "v"
F_LABIO = "f"
SH = "ʃ"
THETA = "θ"
ETH = "ð"
X_VELAR = "x"
GAMMA = "ɣ"
HBAR = "ħ"
J_PALATAL = "j"
ALAPH = "ʔ"      # ʔ  glottal stop
AYIN = "ʕ"       # ʕ  voiced pharyngeal
A_FRONT = "a"
ALPHA = "ɑ"      # ɑ  open back unrounded

VOWELS = {"a", "ɑ", "e", "i", "o", "u"}

# ===========================================================================
# Tier names
# ===========================================================================
SCHOLARLY = "scholarly"
PRETTY = "pretty"
PINYIN = "pinyin"
ZHUYIN = "zhuyin"
HANZI_S = "hanzi_simplified"
HANZI_T = "hanzi_traditional"
TIERS = (SCHOLARLY, PRETTY, PINYIN, ZHUYIN, HANZI_S, HANZI_T)

# Per-tier output directory name and filename suffix.
TIER_DIRNAME = {
    SCHOLARLY: "Scholarly",
    PRETTY: "Pretty",
    PINYIN: "Pinyin",
    ZHUYIN: "Zhuyin",
    HANZI_S: "Hanzi-Simplified",
    HANZI_T: "Hanzi-Traditional",
}
TIER_SUFFIX = {
    SCHOLARLY: "scholarly",
    PRETTY: "pretty",
    PINYIN: "pinyin",
    ZHUYIN: "zhuyin",
    HANZI_S: "hanzi_simplified",
    HANZI_T: "hanzi_traditional",
}

# ===========================================================================
# SCHOLARLY / PRETTY  --  reproduced VERBATIM from English/Peshita_English/transliterate.py
# (only the scholarly+pretty columns of its tables; logic is identical, so output is
#  byte-for-byte identical to the English Scholarly/Pretty tiers).
# ===========================================================================
# (scholarly, pretty)
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
    V_LABIO:   ("ḇ", "v"),
    SH:        ("š", "sh"),
    THETA:     ("ṯ", "th"),
    ETH:       ("ḏ", "dh"),
    X_VELAR:   ("ḵ", "kh"),
    GAMMA:     ("ḡ", "gh"),
    HBAR:      ("ḥ", "ḥ"),
    J_PALATAL: ("y", "y"),
}
SHORT_VOWELS = {
    A_FRONT: ("a", "a"),
    ALPHA:   ("a", "a"),
    "e":     ("e", "e"),
    "i":     ("i", "i"),
    "o":     ("o", "o"),
    "u":     ("u", "u"),
}
LONG_VOWELS = {
    A_FRONT: ("ā", "ā"),
    ALPHA:   ("ā", "ā"),
    "e":     ("ē", "ē"),
    "i":     ("ī", "ī"),
    "o":     ("ō", "ō"),
    "u":     ("ū", "ū"),
}
LONG_VOWEL_BASES = set(LONG_VOWELS.keys())
EMPHATICS_EXPLICIT = {
    "t": ("ṭ", "ṭ"),
    "s": ("ṣ", "ṣ"),
}
_SP_IDX = {SCHOLARLY: 0, PRETTY: 1}


def _tier_consonant(ch, tier):
    entry = CONSONANTS.get(ch)
    if entry is None:
        return None
    return entry[_SP_IDX[tier]]


def _sp_segment_token(token):
    """Segment a token for the Scholarly/Pretty renderer (longest-match left-to-right)."""
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


def _sp_render_segment(seg, tier, is_word_initial, unmapped):
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
    if ch == AYIN:  # ʕ
        return "ʿ"

    if ch == HYPHEN:
        return "-"
    if ch == SPACE:
        return " "

    unmapped.add(ch)
    return ch


def _scholarly_pretty(text, tier, unmapped):
    """Render Scholarly/Pretty exactly as the English transducer does."""
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
# PINYIN ENGINE
# ===========================================================================
# LEGAL toneless Mandarin syllable whitelist (Putonghua; conservative standard set).
# EVERY emitted pinyin syllable must be a member of this set (hard invariant).
# ===========================================================================
_LEGAL = set("""
a o e ai ei ao ou an en ang eng er
ba bo bai bei bao ban ben bang beng bi bie biao bian bin bing bu
pa po pai pei pao pou pan pen pang peng pi pie piao pian pin ping pu
ma mo me mai mei mao mou man men mang meng mi mie miao miu mian min ming mu
fa fo fei fou fan fen fang feng fu
da de dai dei dao dou dan den dang deng dong di die diao diu dian ding du duo dui duan dun
ta te tai tao tou tan tang teng tong ti tie tiao tian ting tu tuo tui tuan tun
na ne nai nei nao nou nan nen nang neng nong ni nie niao niu nian nin niang ning nu nuo nuan nü nüe
la le lai lei lao lou lan lang leng long li lia lie liao liu lian lin liang ling lu luo luan lun lü lüe
ga ge gai gei gao gou gan gen gang geng gong gu gua guo guai gui guan gun guang
ka ke kai kao kou kan ken kang keng kong ku kua kuo kuai kui kuan kun kuang
ha he hai hei hao hou han hen hang heng hong hu hua huo huai hui huan hun huang
ji jie jiao jiu jian jin jiang jing jiong ju jue juan jun
qi qie qiao qiu qian qin qiang qing qiong qu que quan qun
xi xie xiao xiu xian xin xiang xing xiong xu xue xuan xun
zha zhe zhi zhai zhei zhao zhou zhan zhen zhang zheng zhong zhu zhua zhuo zhuai zhui zhuan zhun zhuang
cha che chi chai chao chou chan chen chang cheng chong chu chua chuo chuai chui chuan chun chuang
sha she shi shai shei shao shou shan shen shang sheng shu shua shuo shuai shui shuan shun shuang
re ri rao rou ran ren rang reng rong ru rua ruo rui ruan run
za ze zi zai zei zao zou zan zen zang zeng zong zu zuo zui zuan zun
ca ce ci cai cao cou can cen cang ceng cong cu cuo cui cuan cun
sa se si sai sao sou san sen sang seng song su suo sui suan sun
ya ye yao you yan yin yang ying yong yi yu yue yuan yun
wa wo wai wei wan wen wang weng wu
""".split())

# IPA segment -> Mandarin onset approximation.  None = the onset is dropped (glottals).
VOWEL_NUC = {"a": "a", "ɑ": "a", "e": "e", "i": "i", "o": "o", "u": "u"}
ONSET = {
    "b": "b", "p": "p", "f": "f", "v": "f", "m": "m", "w": "w",
    "d": "d", "t": "t", "tˤ": "t", "θ": "s", "ð": "z",
    "n": "n", "l": "l", "r": "r", "z": "z", "s": "s", "sˤ": "s", "ʃ": "sh",
    "j": "y", "ɡ": "g", "k": "k", "x": "h", "ɣ": "h", "q": "k",
    "ħ": "h", "h": "h", "ʔ": None, "ʕ": None,
}

# Palatalization before /i/: g/k/h -> j/q/x.
_PAL = {"g": "j", "k": "q", "h": "x"}


def _seg_base(seg):
    return seg[0] if (len(seg) == 2 and seg[1] in (SUPER_RHOTIC, LENGTH_MARK)) else seg


def _is_vowel(seg):
    return _seg_base(seg) in VOWELS


def _segment_pinyin(token):
    """Segment a token for the pinyin engine (emphatics and long vowels kept as 2-char)."""
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


def _snap(initial, nucleus, coda):
    """Return a LEGAL toneless pinyin syllable for (initial, nucleus, coda)."""
    if nucleus == "i" and initial in _PAL:
        initial = _PAL[initial]
    result = _snap_raw(initial, nucleus, coda)
    # Targeted artifact removal: 'fo' is legal but its ONLY common Hanzi is 佛
    # ('Buddha' -- religiously loaded). The /f/ here is always stranded (epenthesis)
    # or a /f/+/o/ nucleus that Mandarin cannot render faithfully anyway, so the nucleus
    # is arbitrary. Route 'fo' -> 'fu' (legal; neutral -> 福). No other syllable affected.
    if result == "fo":
        return "fu"
    return result


def _snap_raw(initial, nucleus, coda):
    """Nearest legal toneless pinyin syllable for (initial, nucleus, coda) before fix-ups."""
    cands = []
    if coda:
        # A nasal coda was intended: keep it (n -> ng if -n illegal), then relax.
        cands += [initial + nucleus + coda, initial + nucleus + "ng"]
        for v in (nucleus, "a", "e", "o", "u", "i"):
            cands += [initial + v + coda, initial + v + "ng"]
        cands += [initial + nucleus]                       # last resort: drop coda
        for v in (nucleus, "a", "e", "o", "u", "i"):
            cands.append(initial + v)
    else:
        # No coda intended (bare/epenthetic): prefer a clean CV, NEVER add a coda.
        cands.append(initial + nucleus)
        for v in ("o", "u", "a", "e", "i"):
            cands.append(initial + v)
    for cand in cands:
        if cand in _LEGAL:
            return cand
    # Guaranteed-legal CV fallback.
    for v in ("a", "e", "i", "u", "o"):
        if initial + v in _LEGAL:
            return initial + v
    return "a"


def _zero(nuc):
    """Zero-initial (vowel-only) syllable spelling."""
    return {"i": "yi", "u": "wu", "a": "a", "e": "e", "o": "o"}[nuc]


def _glide(g, nuc):
    """Glide-initial (j=/j/, w=/w/) syllable spelling."""
    if g == "j":
        return {"a": "ya", "e": "ye", "o": "yao", "u": "yu", "i": "yi"}[nuc]
    return {"a": "wa", "e": "wo", "o": "wo", "u": "wu", "i": "wei"}[nuc]


def to_pinyin_syllables(text, unmapped):
    """Return a list of words, each a list of LEGAL pinyin syllables; '-' marks a literal hyphen."""
    words = []
    for tok in text.split(" "):
        if not tok:
            words.append([])
            continue
        segs = _segment_pinyin(tok)
        sylls = []
        i = 0
        n = len(segs)
        while i < n:
            s = segs[i]
            if s == HYPHEN:
                sylls.append("-")
                i += 1
                continue
            if s in (ALAPH, AYIN):
                i += 1
                continue
            if _is_vowel(s):
                sylls.append(_zero(VOWEL_NUC[_seg_base(s)]))
                i += 1
                continue
            base = _seg_base(s) if (len(s) == 2 and s[1] == SUPER_RHOTIC) else s
            onset = ONSET.get(s, ONSET.get(base, "MISS"))
            if onset == "MISS":
                if s not in (SUPER_RHOTIC, LENGTH_MARK):
                    unmapped.add(s)
                i += 1
                continue
            if onset is None:
                i += 1
                continue
            if base in ("j", "w"):
                if i + 1 < n and _is_vowel(segs[i + 1]):
                    sylls.append(_glide(base, VOWEL_NUC[_seg_base(segs[i + 1])]))
                    i += 2
                    continue
                sylls.append("yi" if base == "j" else "wu")
                i += 1
                continue
            if i + 1 < n and _is_vowel(segs[i + 1]):
                nuc = VOWEL_NUC[_seg_base(segs[i + 1])]
                coda = ""
                consumed = 2
                if (i + 2 < n and _seg_base(segs[i + 2]) == "n"
                        and not (i + 3 < n and _is_vowel(segs[i + 3]))):
                    coda = "n"
                    consumed = 3
                sylls.append(_snap(onset, nuc, coda))
                i += consumed
                continue
            # Stranded consonant -> epenthetic legal syllable.
            ev = "i" if onset in ("z", "c", "s", "zh", "ch", "sh", "r") else "e"
            sylls.append(_snap(onset, ev, ""))
            i += 1
        words.append(sylls)
    return words


# ===========================================================================
# PINYIN -> ZHUYIN transcode (standard deterministic pinyin<->bopomofo)
# ===========================================================================
ZH_INIT = {
    "b": "ㄅ", "p": "ㄆ", "m": "ㄇ", "f": "ㄈ", "d": "ㄉ", "t": "ㄊ", "n": "ㄋ", "l": "ㄌ",
    "g": "ㄍ", "k": "ㄎ", "h": "ㄏ", "j": "ㄐ", "q": "ㄑ", "x": "ㄒ",
    "zh": "ㄓ", "ch": "ㄔ", "sh": "ㄕ", "r": "ㄖ", "z": "ㄗ", "c": "ㄘ", "s": "ㄙ",
}
ZH_FINAL = {
    "a": "ㄚ", "o": "ㄛ", "e": "ㄜ", " e": "ㄝ", "ai": "ㄞ", "ei": "ㄟ", "ao": "ㄠ", "ou": "ㄡ",
    "an": "ㄢ", "en": "ㄣ", "ang": "ㄤ", "eng": "ㄥ", "er": "ㄦ",
    "i": "ㄧ", "u": "ㄨ", "ü": "ㄩ",
    "ia": "ㄧㄚ", "ie": "ㄧㄝ", "iao": "ㄧㄠ", "iu": "ㄧㄡ", "ian": "ㄧㄢ", "in": "ㄧㄣ",
    "iang": "ㄧㄤ", "ing": "ㄧㄥ", "iong": "ㄩㄥ",
    "ua": "ㄨㄚ", "uo": "ㄨㄛ", "uai": "ㄨㄞ", "ui": "ㄨㄟ", "uan": "ㄨㄢ", "un": "ㄨㄣ",
    "uang": "ㄨㄤ", "ueng": "ㄨㄥ", "ong": "ㄨㄥ", "ue": "ㄩㄝ", "üe": "ㄩㄝ",
    "üan": "ㄩㄢ", "ün": "ㄩㄣ", "iou": "ㄧㄡ",
}
# Apical -i after zh/ch/sh/r/z/c/s = the "empty rime" (no extra symbol in standard zhuyin).
_APICAL_INITS = {"zh", "ch", "sh", "r", "z", "c", "s"}


def _split_syllable(syl):
    for ini in ("zh", "ch", "sh"):
        if syl.startswith(ini):
            return ini, syl[len(ini):]
    if syl[0] in "bpmfdtnlgkhjqxrzcs":
        return syl[0], syl[1:]
    return "", syl


def pinyin_to_zhuyin(syl):
    # Zero-initial y/w spellings -> restore medial finals.
    special = {
        "yi": "i", "yu": "ü", "wu": "u", "ye": "ie", "ya": "ia", "yao": "iao",
        "wa": "ua", "wo": "uo", "wei": "ui", "yo": "iao",
        "yun": "ün", "yuan": "üan", "yue": "üe",
    }
    if syl in special:
        fin = special[syl]
        return ZH_FINAL.get(fin, ZH_FINAL.get(fin.lstrip("iu"), "?"))
    ini, fin = _split_syllable(syl)
    if ini in _APICAL_INITS and fin == "i":
        return ZH_INIT[ini]   # apical empty rime: just the initial symbol
    # After j/q/x the orthographic 'u' is always /y/ (ü): rewrite u->ü, un->ün, uan->üan
    # so the bopomofo medial is ㄩ, not ㄨ (ue->üe already handled by ZH_FINAL).
    if ini in ("j", "q", "x") and fin and fin[0] == "u":
        fin = "ü" + fin[1:]
    zi = ZH_INIT.get(ini, "")
    zf = ZH_FINAL.get(fin, "")
    return zi + zf if (zi or zf) else "?"


# ===========================================================================
# HANZI table  --  COMPLETE {simplified, traditional} per produced syllable.
# Neutral transcription characters (Xinhua 音译表 / 《世界人名翻译大辞典》); semantically
# bleached, scripture-safe. Most are script-invariant; both columns are authored where they
# differ (热/熱 萨/薩 乌/烏 维/維 书/書 达/達 兰/蘭 图/圖 ...).
#
# Curated by the Sinology phase to cover EVERY syllable the transducer produces (the exact
# set enumerated by --coverage). Each character was chosen by Mandarin SOUND (tone ignored),
# preferring the conventional 音译 character, and avoiding strong / negative / sacred / loaded
# meanings (this is scripture -- neutrality matters). HARD INVARIANT (per design study sec. 4,
# "Self-test invariant"): each glyph's PREFERRED (default, most-common) Mandarin reading, with
# tones stripped, equals its target syllable -- so the Hanzi tier adds nothing but artifactual
# tone. This is the STRICT test, verified for BOTH columns by --verify-hanzi (and re-checked
# offline against pypinyin's default reading): strip_tones(default_reading(字)) == syllable.
# A handful of syllables are pure engine artifacts (epenthesis / coda-snap residue, e.g. den,
# hen, ne, nen, nin, pen, zen) for which the most neutral legal character was taken.
# Simplified->Traditional pairs verified against OpenCC s2t / t2s.
#
# HETERONYM DRIFT FIXED: four earlier glyphs spelled their key only via a MINORITY reading
# (their pypinyin default differed), which violated the strict invariant above. Each was
# replaced with a neutral 音译 character whose DEFAULT reading IS the key:
#     le  : 勒 (default 'lei') -> 叻 (default 'le'; attested transcription char, e.g. 石叻)
#     se  : 塞 (default 'sai') -> 瑟 (default 'se'; single-reading, neutral)
#     shi : 什 (default 'shen') -> 士 (default 'shi'; single-reading, neutral)
#     za  : 扎 (default 'zha')  -> 匝 (default 'za'; single-reading, neutral)
# All four replacements are script-invariant (identical S/T columns; OpenCC-confirmed).
#
# Any produced syllable not present here would render as '□'; --coverage reports ZERO gaps.
#
# DOCUMENTED LIMITATIONS (NOT clean -- inherent to Mandarin phonotactics, no fixable swap):
#   Some snapped syllables land on near-empty Mandarin finals that have NO common,
#   semantically-bleached transcription character. The least-bad legal glyph is used, but it
#   is unavoidably either loaded or obscure. These are artifacts of the pinyin engine snapping
#   stranded /n i n/, etc. to these finals, not curation errors:
#     nin -> 您 : the polite 2nd-person pronoun; no neutral 音译 char reads 'nin' (囜/拰/脌 obscure).
#     zen -> 怎 : the interrogative 'how'; no neutral 音译 char reads 'zen' (谮 'slander' is worse,
#            others obscure).
#     den -> 扽 : a rare dialectal verb; 'den' has no common, readable glyph (扥 equally obscure).
#   These three should be treated as known artifacts to fix UPSTREAM (engine epenthesis), not by
#   shipping a different character here.
#   FIXED UPSTREAM (no longer an artifact): the former heaviest-hit case 'fo' -> 佛 'Buddha'
#   (religiously loaded). The pinyin engine now routes stranded /f/+/o/ to 'fu' (->福, neutral)
#   in _snap, so 'fo' is never produced and 佛 is never shipped. 'fo' is absent from this table.
# ===========================================================================
HANZI = {
    # --- original seed (script-invariant + a few S/T splits) ---
    "a":   ("阿", "阿"), "ba":  ("巴", "巴"), "la":  ("拉", "拉"), "sha": ("沙", "沙"),
    "si":  ("斯", "斯"), "yi":  ("伊", "伊"), "sa":  ("萨", "薩"), "wu":  ("乌", "烏"),
    "wa":  ("瓦", "瓦"), "me":  ("么", "麼"), "le":  ("叻", "叻"), "hu":  ("胡", "胡"),
    "ha":  ("哈", "哈"), "na":  ("纳", "納"), "bo":  ("波", "波"), "re":  ("热", "熱"),
    "shi": ("士", "士"), "de":  ("德", "德"), "ye":  ("耶", "耶"), "shu": ("书", "書"),
    "mo":  ("摩", "摩"), "fa":  ("法", "法"), "wei": ("维", "維"), "zu":  ("祖", "祖"),
    "he":  ("赫", "赫"), "ke":  ("克", "克"), "ri":  ("日", "日"), "li":  ("利", "利"),
    "di":  ("迪", "迪"),
    # --- b- ---
    "ban": ("班", "班"), "ben": ("本", "本"), "bi":  ("比", "比"), "bin": ("宾", "賓"),
    "bu":  ("布", "布"),
    # --- d- ---
    "da":  ("达", "達"), "dan": ("丹", "丹"), "den": ("扽", "扽"), "ding": ("丁", "丁"),
    "dong": ("东", "東"), "du":  ("杜", "杜"), "dun": ("敦", "敦"),
    # --- e / o (zero-onset) ---
    "e":   ("厄", "厄"), "o":   ("哦", "哦"),
    # --- f- ---  ('fo' is intentionally ABSENT: the engine routes stranded /f/+/o/ to
    #              'fu' (->福), so 佛 'Buddha' is never produced. See _snap.)
    "fan": ("凡", "凡"), "fen": ("芬", "芬"), "fu":  ("福", "福"),
    # --- g- ---
    "ga":  ("嘎", "嘎"), "gan": ("甘", "甘"), "ge":  ("格", "格"), "gen": ("根", "根"),
    "gong": ("贡", "貢"), "gu":  ("古", "古"), "gun": ("衮", "袞"),
    # --- h- ---
    "han": ("汉", "漢"), "hen": ("痕", "痕"), "hong": ("洪", "洪"), "hun": ("浑", "渾"),
    # --- j- ---
    "ji":  ("吉", "吉"), "jin": ("金", "金"),
    # --- k- ---
    "ka":  ("卡", "卡"), "kan": ("坎", "坎"), "ken": ("肯", "肯"), "kong": ("孔", "孔"),
    "ku":  ("库", "庫"), "kun": ("昆", "昆"),
    # --- l- ---
    "lan": ("兰", "蘭"), "leng": ("楞", "楞"), "lin": ("林", "林"), "long": ("隆", "隆"),
    "lu":  ("卢", "盧"), "lun": ("伦", "倫"),
    # --- m- ---
    "ma":  ("玛", "瑪"), "man": ("曼", "曼"), "men": ("门", "門"), "mi":  ("米", "米"),
    "min": ("民", "民"), "mu":  ("穆", "穆"),
    # --- n- ---
    "nan": ("南", "南"), "ne":  ("讷", "訥"), "nen": ("嫩", "嫩"), "ni":  ("尼", "尼"),
    "nin": ("您", "您"), "nong": ("农", "農"), "nu":  ("努", "努"),
    # --- p- ---
    "pa":  ("帕", "帕"), "pan": ("潘", "潘"), "pen": ("盆", "盆"), "pi":  ("皮", "皮"),
    "pin": ("品", "品"), "po":  ("珀", "珀"), "pu":  ("普", "普"),
    # --- q- ---
    "qi":  ("奇", "奇"), "qin": ("钦", "欽"),
    # --- r- ---
    "ran": ("然", "然"), "ren": ("任", "任"), "rong": ("荣", "榮"), "ru":  ("茹", "茹"),
    "run": ("润", "潤"),
    # --- s- ---
    "san": ("散", "散"), "se":  ("瑟", "瑟"), "sen": ("森", "森"), "song": ("松", "松"),
    "su":  ("苏", "蘇"), "sun": ("孙", "孫"),
    # --- sh- ---
    "shan": ("山", "山"), "she": ("舍", "舍"), "shen": ("申", "申"),
    # --- t- ---
    "ta":  ("塔", "塔"), "tan": ("坦", "坦"), "te":  ("特", "特"), "teng": ("腾", "騰"),
    "ti":  ("提", "提"), "ting": ("廷", "廷"), "tong": ("通", "通"), "tu":  ("图", "圖"),
    "tun": ("吞", "吞"),
    # --- w- ---
    "wo":  ("沃", "沃"),
    # --- x- ---
    "xi":  ("锡", "錫"), "xin": ("辛", "辛"),
    # --- y- ---
    "ya":  ("亚", "亞"), "yao": ("姚", "姚"), "yu":  ("宇", "宇"),
    # --- z- ---
    "za":  ("匝", "匝"), "zan": ("赞", "贊"), "ze":  ("泽", "澤"), "zen": ("怎", "怎"),
    "zi":  ("孜", "孜"), "zong": ("宗", "宗"), "zun": ("尊", "尊"),
}
_HANZI_IDX = {HANZI_S: 0, HANZI_T: 1}
MISSING_HANZI = "□"


# ===========================================================================
# Render helpers
# ===========================================================================
def _join_word(sylls, mapper):
    """Join a word's syllables with a mid-dot, keeping literal '-' contiguous."""
    out = ""
    for s in sylls:
        if s == "-":
            out += "-"
            continue
        piece = mapper(s)
        if out and not out.endswith("-"):
            out += "·"
        out += piece
    return out


def transliterate(text, tier, unmapped=None):
    """
    Transliterate IPA `text` for the given `tier` (one of TIERS).

    SCHOLARLY/PRETTY: byte-for-byte identical to the English transducer.
    PINYIN: space-separated words, mid-dot between syllables (e.g. 'a·la·ha').
    ZHUYIN: same layout, bopomofo per syllable.
    HANZI_SIMPLIFIED / HANZI_TRADITIONAL: one character per syllable, no inner separators;
        a syllable with no table entry renders as '□'.

    If `unmapped` (a set) is supplied, unmapped IPA segments are collected into it.
    """
    if tier not in TIERS:
        raise ValueError("Unknown tier: %r (expected one of %r)" % (tier, TIERS))
    if unmapped is None:
        unmapped = set()

    if tier in (SCHOLARLY, PRETTY):
        return _scholarly_pretty(text, tier, unmapped)

    words = to_pinyin_syllables(text, unmapped)
    if tier == PINYIN:
        return " ".join(_join_word(w, lambda s: s) for w in words)
    if tier == ZHUYIN:
        return " ".join(_join_word(w, pinyin_to_zhuyin) for w in words)
    # Hanzi tiers
    idx = _HANZI_IDX[tier]
    return " ".join(
        "".join("-" if s == "-" else HANZI.get(s, (MISSING_HANZI, MISSING_HANZI))[idx] for s in w)
        for w in words
    )


def transliterate_line(line, tier, unmapped=None):
    """
    Transliterate a single corpus line '<verse#>\\t<text>'.
    Keep the '<verse#>\\t' prefix verbatim; convert only text after the FIRST tab.
    Lines without a tab are returned unchanged. Trailing newline is preserved.
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
    "Mandarin forces the heaviest phonetic collapse of any target language in this project.",
    "No consonant clusters; codas only -n/-ng. Stranded consonants get an epenthetic vowel "
    "(default 'e'; apical 'i' after z/c/s/zh/ch/sh/r), so cluster structure is lost.",
    "Voicing, emphatics (ˤ), gutturals (ħ ʕ ʔ x ɣ), and /v θ ð ʃ z/ all collapse onto the "
    "nearest Mandarin onset; the l/r distinction and vowel length are lost.",
    "Glottals ʔ and ʕ are dropped entirely.",
    "g/k/h before /i/ palatalize to j/q/x (Mandarin phonotactics).",
    "Tones are OMITTED in Pinyin and Zhuyin because the source IPA is atonal; emitting a tone "
    "would fabricate data.",
    "Hanzi unavoidably carries each glyph's citation tone -- this tone is an ARTIFACT, not a "
    "claim about the source; verify via strip_tones(hanzi -> pinyin) == the toneless syllable.",
    "Hanzi imposes MEANING and is NOT readback-grade: it cannot distinguish near-homophones "
    "such as Barabba from Barava.",
    "The transduction is NOT reversible.",
    "Scholarly and Pretty are byte-for-byte identical to the English Peshitta transducer.",
]


def build_mapping_dict():
    """Build the JSON-serializable mapping table (IPA rules + Hanzi table + limitations)."""
    onset = {k: (v if v is not None else None) for k, v in ONSET.items()}
    hanzi = {syl: {"simplified": v[0], "traditional": v[1]} for syl, v in sorted(HANZI.items())}

    return {
        "meta": {
            "description": "Deterministic IPA->Chinese (Mandarin) mapping for the Peshitta corpus.",
            "tiers": list(TIERS),
            "note": "transliterate_zh.py is authoritative; this file mirrors its hard-coded "
                    "tables. Scholarly/Pretty are byte-identical to the English transducer.",
            "author": "Shin",
        },
        "unicode": {
            "emphatic_marker": SUPER_RHOTIC,
            "length_mark": LENGTH_MARK,
            "combining_dot_below": COMBINING_DOT_BELOW,
            "alaph": ALAPH,
            "ayin": AYIN,
            "hyphen": HYPHEN,
        },
        "pinyin_engine": {
            "vowel_nucleus": dict(VOWEL_NUC),
            "onset_ipa_to_mandarin": onset,
            "palatalization_before_i": dict(_PAL),
            "epenthesis": {
                "default": "e",
                "apical_i_after": sorted(["z", "c", "s", "zh", "ch", "sh", "r"]),
            },
            "dropped_onsets": ["ʔ", "ʕ"],
            "snap": "Every emitted pinyin syllable is snapped to a member of the legal "
                    "toneless Mandarin whitelist; codas only -n/-ng.",
            "legal_syllable_count": len(_LEGAL),
            "legal_syllables": sorted(_LEGAL),
        },
        "zhuyin_transcode": {
            "initials": dict(ZH_INIT),
            "finals": {k: v for k, v in ZH_FINAL.items()},
            "apical_empty_rime_initials": sorted(_APICAL_INITS),
            "note": "Standard deterministic pinyin<->bopomofo. Apical -i after the apical "
                    "initials = bare initial symbol; y/w zero-initial spellings restore "
                    "i-/u- medials.",
        },
        "scholarly_pretty_tables": {
            "consonants": {ch: {SCHOLARLY: v[0], PRETTY: v[1]} for ch, v in CONSONANTS.items()},
            "short_vowels": {ch: {SCHOLARLY: v[0], PRETTY: v[1]} for ch, v in SHORT_VOWELS.items()},
            "long_vowels": {ch: {SCHOLARLY: v[0], PRETTY: v[1]} for ch, v in LONG_VOWELS.items()},
            "emphatics_explicit": {ch: {SCHOLARLY: v[0], PRETTY: v[1]}
                                   for ch, v in EMPHATICS_EXPLICIT.items()},
            "note": "Verbatim from English/Peshita_English/transliterate.py "
                    "(scholarly+pretty columns only).",
        },
        "hanzi_table": {
            "characters": hanzi,
            "missing_glyph": MISSING_HANZI,
            "status": "PARTIAL -- the Sinology curation phase completes this table; produced "
                      "syllables absent here render as the missing glyph.",
            "source": "Standard Xinhua 音译表 / 《世界人名翻译大辞典》 neutral transcription "
                      "characters (semantically bleached, scripture-safe).",
        },
        "documented_limitations": list(DOCUMENTED_LIMITATIONS),
    }


def write_mapping_json(path=MAPPING_JSON):
    data = build_mapping_dict()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return path


# ===========================================================================
# Gold cases
#   Scholarly/Pretty == the English gold (byte-identical).
#   Pinyin/Zhuyin/Hanzi are the deterministic Chinese outputs (□ where the Hanzi
#   table is still partial).
# ===========================================================================
GOLD_CASES = [
    {
        "ref": "John 1:1",
        "ipa": "breːʃiːθ ʔiːθawj wɑː melθɑː whuː melθɑː ʔiːθawj wɑː lwɑːθ ʔɑːlɑːhɑː waʔlɑːhɑː ʔiːθawj wɑː huː melθɑː",
        "scholarly": "brēšīṯ ʾīṯawy wā melṯā whū melṯā ʾīṯawy wā lwāṯ ʾālāhā waʾlāhā ʾīṯawy wā hū melṯā",
        "pretty": "brēshīth īthawy wā melthā whū melthā īthawy wā lwāth ālāhā wa'lāhā īthawy wā hū melthā",
        "pinyin": "bo·re·shi·si yi·sa·wu·yi wa me·le·sa wu·hu me·le·sa yi·sa·wu·yi wa le·wa·si a·la·ha wa·la·ha yi·sa·wu·yi wa hu me·le·sa",
        "zhuyin": "ㄅㄛ·ㄖㄜ·ㄕ·ㄙ ㄧ·ㄙㄚ·ㄨ·ㄧ ㄨㄚ ㄇㄜ·ㄌㄜ·ㄙㄚ ㄨ·ㄏㄨ ㄇㄜ·ㄌㄜ·ㄙㄚ ㄧ·ㄙㄚ·ㄨ·ㄧ ㄨㄚ ㄌㄜ·ㄨㄚ·ㄙ ㄚ·ㄌㄚ·ㄏㄚ ㄨㄚ·ㄌㄚ·ㄏㄚ ㄧ·ㄙㄚ·ㄨ·ㄧ ㄨㄚ ㄏㄨ ㄇㄜ·ㄌㄜ·ㄙㄚ",
        "hanzi_simplified": "波热士斯 伊萨乌伊 瓦 么叻萨 乌胡 么叻萨 伊萨乌伊 瓦 叻瓦斯 阿拉哈 瓦拉哈 伊萨乌伊 瓦 胡 么叻萨",
        "hanzi_traditional": "波熱士斯 伊薩烏伊 瓦 麼叻薩 烏胡 麼叻薩 伊薩烏伊 瓦 叻瓦斯 阿拉哈 瓦拉哈 伊薩烏伊 瓦 胡 麼叻薩",
    },
    {
        "ref": "John 1:2",
        "ipa": "hɑːnɑː ʔiːθawj wɑː breːʃiːθ lwɑːθ ʔɑːlɑːhɑː",
        "scholarly": "hānā ʾīṯawy wā brēšīṯ lwāṯ ʾālāhā",
        "pretty": "hānā īthawy wā brēshīth lwāth ālāhā",
        "pinyin": "ha·na yi·sa·wu·yi wa bo·re·shi·si le·wa·si a·la·ha",
        "zhuyin": "ㄏㄚ·ㄋㄚ ㄧ·ㄙㄚ·ㄨ·ㄧ ㄨㄚ ㄅㄛ·ㄖㄜ·ㄕ·ㄙ ㄌㄜ·ㄨㄚ·ㄙ ㄚ·ㄌㄚ·ㄏㄚ",
        "hanzi_simplified": "哈纳 伊萨乌伊 瓦 波热士斯 叻瓦斯 阿拉哈",
        "hanzi_traditional": "哈納 伊薩烏伊 瓦 波熱士斯 叻瓦斯 阿拉哈",
    },
    {
        "ref": "John 1:3",
        "ipa": "kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː",
        "scholarly": "kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā",
        "pretty": "kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā",
        "pinyin": "ku·le bo·yi·yi·ze·he he·wa wu·fu·le·a·za·wu·yi a·fu·la he·za he·wa·si me·de·me da·he·wa",
        "zhuyin": "ㄎㄨ·ㄌㄜ ㄅㄛ·ㄧ·ㄧ·ㄗㄜ·ㄏㄜ ㄏㄜ·ㄨㄚ ㄨ·ㄈㄨ·ㄌㄜ·ㄚ·ㄗㄚ·ㄨ·ㄧ ㄚ·ㄈㄨ·ㄌㄚ ㄏㄜ·ㄗㄚ ㄏㄜ·ㄨㄚ·ㄙ ㄇㄜ·ㄉㄜ·ㄇㄜ ㄉㄚ·ㄏㄜ·ㄨㄚ",
        "hanzi_simplified": "库叻 波伊伊泽赫 赫瓦 乌福叻阿匝乌伊 阿福拉 赫匝 赫瓦斯 么德么 达赫瓦",
        "hanzi_traditional": "庫叻 波伊伊澤赫 赫瓦 烏福叻阿匝烏伊 阿福拉 赫匝 赫瓦斯 麼德麼 達赫瓦",
    },
    {
        "ref": "Matthew 1:1",
        "ipa": "kθɑːvɑː diːliːðuːθeh djeʃuːʕ mʃiːħɑː breh dðawiːð breh dʔavrɑːhɑːm",
        "scholarly": "kṯāḇā dīlīḏūṯeh dyešūʿ mšīḥā breh dḏawīḏ breh dʾaḇrāhām",
        "pretty": "kthāvā dīlīdhūtheh dyeshūʿ mshīḥā breh ddhawīdh breh d'avrāhām",
        "pinyin": "ke·sa·fa di·li·zu·se·he de·ye·shu me·shi·ha bo·re·he de·za·wei·zi bo·re·he de·a·fu·ru·ha·me",
        "zhuyin": "ㄎㄜ·ㄙㄚ·ㄈㄚ ㄉㄧ·ㄌㄧ·ㄗㄨ·ㄙㄜ·ㄏㄜ ㄉㄜ·ㄧㄝ·ㄕㄨ ㄇㄜ·ㄕ·ㄏㄚ ㄅㄛ·ㄖㄜ·ㄏㄜ ㄉㄜ·ㄗㄚ·ㄨㄟ·ㄗ ㄅㄛ·ㄖㄜ·ㄏㄜ ㄉㄜ·ㄚ·ㄈㄨ·ㄖㄨ·ㄏㄚ·ㄇㄜ",
        "hanzi_simplified": "克萨法 迪利祖瑟赫 德耶书 么士哈 波热赫 德匝维孜 波热赫 德阿福茹哈么",
        "hanzi_traditional": "克薩法 迪利祖瑟赫 德耶書 麼士哈 波熱赫 德匝維孜 波熱赫 德阿福茹哈麼",
    },
    {
        "ref": "Romans 1:1",
        "ipa": "pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː",
        "scholarly": "pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā",
        "pretty": "pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā",
        "pinyin": "pa·wu·la·wu·si a·fu·da de·ye·shu me·shi·ha ka·ri·ya wa·shi·li·ha de·e·si·po·re·shi le·wa·ne·ge·li·yi·ya·wu·ne de·a·la·ha",
        "zhuyin": "ㄆㄚ·ㄨ·ㄌㄚ·ㄨ·ㄙ ㄚ·ㄈㄨ·ㄉㄚ ㄉㄜ·ㄧㄝ·ㄕㄨ ㄇㄜ·ㄕ·ㄏㄚ ㄎㄚ·ㄖ·ㄧㄚ ㄨㄚ·ㄕ·ㄌㄧ·ㄏㄚ ㄉㄜ·ㄜ·ㄙ·ㄆㄛ·ㄖㄜ·ㄕ ㄌㄜ·ㄨㄚ·ㄋㄜ·ㄍㄜ·ㄌㄧ·ㄧ·ㄧㄚ·ㄨ·ㄋㄜ ㄉㄜ·ㄚ·ㄌㄚ·ㄏㄚ",
        "hanzi_simplified": "帕乌拉乌斯 阿福达 德耶书 么士哈 卡日亚 瓦士利哈 德厄斯珀热士 叻瓦讷格利伊亚乌讷 德阿拉哈",
        "hanzi_traditional": "帕烏拉烏斯 阿福達 德耶書 麼士哈 卡日亞 瓦士利哈 德厄斯珀熱士 叻瓦訥格利伊亞烏訥 德阿拉哈",
    },
    {
        "ref": "Matthew 27:16",
        "ipa": "dmeθqre bar-ʔaba lvar-ʔaba lvar-ʔava",
        "scholarly": "dmeṯqre bar-ʾaba lḇar-ʾaba lḇar-ʾaḇa",
        "pretty": "dmethqre bar-'aba lvar-'aba lvar-'ava",
        "pinyin": "de·me·si·ke·re ba·ri-a·ba le·fa·ri-a·ba le·fa·ri-a·fa",
        "zhuyin": "ㄉㄜ·ㄇㄜ·ㄙ·ㄎㄜ·ㄖㄜ ㄅㄚ·ㄖ-ㄚ·ㄅㄚ ㄌㄜ·ㄈㄚ·ㄖ-ㄚ·ㄅㄚ ㄌㄜ·ㄈㄚ·ㄖ-ㄚ·ㄈㄚ",
        "hanzi_simplified": "德么斯克热 巴日-阿巴 叻法日-阿巴 叻法日-阿法",
        "hanzi_traditional": "德麼斯克熱 巴日-阿巴 叻法日-阿巴 叻法日-阿法",
    },
]


def run_selftest():
    """
    Run gold cases. ALL SIX tiers are locked and checked against GOLD_CASES.
    Scholarly/Pretty additionally serve as the English-gold byte-identical anchors
    (their gold strings ARE the English transducer's output).
    """
    all_pass = True
    for case in GOLD_CASES:
        ref = case["ref"]
        print("== %s" % ref)
        print("   IPA         %s" % case["ipa"])
        for tier in TIERS:
            got = transliterate(case["ipa"], tier)
            print("   %-18s %s" % (tier, got))
            expected = case.get(tier)
            if expected is None:
                all_pass = False
                print("     !! no locked gold for tier %s" % tier)
                continue
            if got != expected:
                all_pass = False
                anchor = " (English gold)" if tier in (SCHOLARLY, PRETTY) else ""
                print("     !! %s != locked gold%s" % (tier, anchor))
                print("        expected: %r" % expected)
                print("        got:      %r" % got)
        print("")
    print("All six tiers vs locked gold:", "OK" if all_pass else "FAIL")
    return all_pass


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
    Scan every *_ipa.txt; report:
      - unmapped IPA segments,
      - ANY illegal pinyin syllable (must be NONE),
      - zhuyin transcode gaps,
      - produced syllables MISSING a Hanzi character (the set the curation phase must cover).
    """
    unmapped = set()
    illegal = set()
    zh_gaps = set()
    hz_missing = set()
    n_files = 0
    for path in iter_ipa_files(root):
        n_files += 1
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if "\t" not in line:
                    continue
                text = line.rstrip("\r\n").split("\t", 1)[1]
                for word in to_pinyin_syllables(text, unmapped):
                    for s in word:
                        if s == "-":
                            continue
                        if s not in _LEGAL:
                            illegal.add(s)
                        z = pinyin_to_zhuyin(s)
                        if "?" in z:
                            zh_gaps.add(s)
                        if s not in HANZI:
                            hz_missing.add(s)
    print("Scanned %d IPA file(s)." % n_files)
    print("  unmapped IPA segments     :", sorted(unmapped) if unmapped else "none")
    print("  ILLEGAL pinyin syllables  :", sorted(illegal) if illegal else "NONE (all legal)")
    print("  zhuyin transcode gaps     :", sorted(zh_gaps) if zh_gaps else "none")
    print("  hanzi table gaps          : %d syllable(s) need a character" % len(hz_missing))
    if hz_missing:
        print("    " + " ".join(sorted(hz_missing)))
    return unmapped, illegal, zh_gaps, hz_missing


# ===========================================================================
# Hanzi tone-strip invariant (authoring-time QA; design study sec. 4)
# ===========================================================================
def run_verify_hanzi():
    """
    STRICT invariant: for every {simplified, traditional} entry, the glyph's
    PREFERRED (default) Mandarin reading with tones stripped must equal the
    syllable key, for BOTH columns. This proves the Hanzi tier adds nothing but
    artifactual citation tone (no fabricated SOUND, only tone).

    pypinyin is an OPTIONAL authoring-QA dependency; the shipped transducer does
    NOT import it at runtime. If it is not installed, this check reports SKIPPED
    (exit 0) rather than failing the build.
    """
    try:
        import pypinyin
        from pypinyin import pinyin, Style
    except Exception as e:
        print("verify-hanzi: pypinyin not installed -> SKIPPED (%s)" % e)
        print("  (install with `pip install pypinyin` to run the strict tone-strip check)")
        return True

    def default_reading(ch):
        r = pinyin(ch, style=Style.NORMAL, errors="default")
        return r[0][0] if r and r[0] else ""

    strict_fail = []
    for syl, (simp, trad) in sorted(HANZI.items()):
        for col, ch in (("simplified", simp), ("traditional", trad)):
            d = default_reading(ch)
            if d != syl:
                strict_fail.append((syl, col, ch, d))

    print("verify-hanzi (pypinyin %s): %d entries x 2 columns" % (pypinyin.__version__, len(HANZI)))
    print("  STRICT tone-strip failures (default_reading(glyph) != key):", len(strict_fail))
    for syl, col, ch, d in strict_fail:
        print("    FAIL key=%r %s glyph=%r default=%r" % (syl, col, ch, d))
    ok = not strict_fail
    print("  INVARIANT:", "PASS" if ok else "FAIL")
    return ok


# ===========================================================================
# Build
# ===========================================================================
def _out_path_for(ipa_path, tier):
    """
    IPA/Peshitta/<Book>/<name>_ipa.txt
      -> Chinese/Peshita_Chinese/<TierDir>/<Book>/<name>_<suffix>.txt
    """
    rel = os.path.relpath(ipa_path, IPA_ROOT)        # <Book>/<name>_ipa.txt
    book_dir = os.path.dirname(rel)
    base = os.path.basename(rel)
    assert base.endswith("_ipa.txt"), base
    name = base[:-len("_ipa.txt")]
    out_name = "%s_%s.txt" % (name, TIER_SUFFIX[tier])
    return os.path.join(CHINESE_ROOT, TIER_DIRNAME[tier], book_dir, out_name)


def run_build(root=IPA_ROOT):
    """Transliterate the whole corpus into the 6 tier trees."""
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
        print("WARNING: unmapped IPA segments encountered during build:", sorted(unmapped))
    else:
        print("No unmapped IPA segments encountered.")
    return n_files, n_out, sorted(unmapped)


# ===========================================================================
# CLI
# ===========================================================================
def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Deterministic IPA->Chinese (Mandarin) transducer for the Peshitta corpus."
    )
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--selftest", action="store_true", help="run embedded gold cases")
    g.add_argument("--coverage", action="store_true",
                   help="report unmapped IPA, illegal pinyin, zhuyin gaps, missing hanzi")
    g.add_argument("--build", action="store_true", help="transliterate whole corpus into 6 trees")
    g.add_argument("--write-mapping", action="store_true",
                   help="(re)write transcription_mapping_zh.json")
    g.add_argument("--verify-hanzi", action="store_true",
                   help="strict tone-strip invariant: default_reading(glyph)==key (needs pypinyin)")
    args = parser.parse_args(argv)

    if args.selftest:
        return 0 if run_selftest() else 1
    if args.coverage:
        un, il, zq, _hz = run_coverage()
        return 0 if not (un or il or zq) else 2
    if args.verify_hanzi:
        return 0 if run_verify_hanzi() else 1
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
