#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deterministic IPA -> Latin transliterator for the Peshitta corpus.

Three tiers: SCHOLARLY | PRETTY | ANGLICIZED.

The mapping table below is AUTHORITATIVE and hard-coded from the project SPEC.
A machine-readable copy is also written to mapping.json (see build_mapping_dict()).

CLI:
    transliterate.py --selftest    run the embedded gold cases, print PASS/FAIL per (ref,tier)
    transliterate.py --coverage    scan every *_ipa.txt for chars (besides space) not in the mapping
    transliterate.py --build        transliterate the whole corpus into the 3 tier trees

Public API:
    transliterate(text, tier) -> str
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
ENGLISH_ROOT = os.path.join(REPO_ROOT, "English", "Peshita_English")
MAPPING_JSON = os.path.join(SCRIPT_DIR, "mapping.json")

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
ANGLICIZED = "anglicized"
TIERS = (SCHOLARLY, PRETTY, ANGLICIZED)

# ---------------------------------------------------------------------------
# CONSONANTS (single).  Order of tuple = (scholarly, pretty, anglicized)
# ---------------------------------------------------------------------------
CONSONANTS = {
    "b":       ("b", "b", "b"),
    G_VOICED:  ("g", "g", "g"),
    "d":       ("d", "d", "d"),
    "h":       ("h", "h", "h"),
    "w":       ("w", "w", "w"),
    "z":       ("z", "z", "z"),
    "k":       ("k", "k", "k"),
    "l":       ("l", "l", "l"),
    "m":       ("m", "m", "m"),
    "n":       ("n", "n", "n"),
    "s":       ("s", "s", "s"),
    "p":       ("p", "p", "p"),
    "q":       ("q", "q", "q"),
    "r":       ("r", "r", "r"),
    "t":       ("t", "t", "t"),
    F_LABIO:   ("f", "f", "f"),
    V_LABIO:   ("ḇ", "v", "v"),   # ḇ | v | v
    SH:        ("š", "sh", "sh"), # š | sh | sh
    THETA:     ("ṯ", "th", "th"), # ṯ | th | th
    ETH:       ("ḏ", "dh", "dh"), # ḏ | dh | dh
    X_VELAR:   ("ḵ", "kh", "kh"), # ḵ | kh | kh
    GAMMA:     ("ḡ", "gh", "gh"), # ḡ | gh | gh
    HBAR:      ("ḥ", "ḥ", "kh"),  # ḥ | ḥ | kh
    J_PALATAL: ("y", "y", "y"),
}

# ---------------------------------------------------------------------------
# SHORT VOWELS (no following length mark) -- identical across all tiers
# ---------------------------------------------------------------------------
SHORT_VOWELS = {
    A_FRONT: ("a", "a", "a"),
    ALPHA:   ("a", "a", "a"),
    "e":     ("e", "e", "e"),
    "i":     ("i", "i", "i"),
    "o":     ("o", "o", "o"),
    "u":     ("u", "u", "u"),
}

# ---------------------------------------------------------------------------
# LONG VOWELS (V + ː).  (scholarly, pretty, anglicized)
#   scholarly and pretty share the macron form.
# ---------------------------------------------------------------------------
LONG_VOWELS = {
    A_FRONT: ("ā", "ā", "a"),   # ā  | ā  | a
    ALPHA:   ("ā", "ā", "a"),   # ā  | ā  | a
    "e":     ("ē", "ē", "ay"),  # ē  | ē  | ay
    "i":     ("ī", "ī", "ee"),  # ī  | ī  | ee
    "o":     ("ō", "ō", "oh"),  # ō  | ō  | oh
    "u":     ("ū", "ū", "oo"),  # ū  | ū  | oo
}

LONG_VOWEL_BASES = set(LONG_VOWELS.keys())  # a ɑ e i o u

# ---------------------------------------------------------------------------
# EMPHATICS (consonant + ˤ).  (scholarly, pretty, anglicized)
# ---------------------------------------------------------------------------
EMPHATICS_EXPLICIT = {
    "t": ("ṭ", "ṭ", "t"),   # ṭ | ṭ | t
    "s": ("ṣ", "ṣ", "s"),   # ṣ | ṣ | s
}

# ---------------------------------------------------------------------------
# OTHER literals
# ---------------------------------------------------------------------------
HYPHEN = "-"  # -
SPACE = " "

# Tier index lookup
_TIER_IDX = {SCHOLARLY: 0, PRETTY: 1, ANGLICIZED: 2}


def _tier_consonant(ch, tier):
    """Return the tier rendering of a base consonant char, or None if not a consonant."""
    entry = CONSONANTS.get(ch)
    if entry is None:
        return None
    return entry[_TIER_IDX[tier]]


def _segment_token(token):
    """
    Segment a single whitespace-delimited token into segments (left-to-right,
    longest match):
      1. consonant + ˤ            -> 2-char emphatic segment
      2. vowel (a ɑ e i o u) + ː  -> 2-char long-vowel segment
      3. otherwise single char
    Returns a list of (segment_string, is_word_initial) ... but word-initial is
    tracked by the caller via index, so here we just return the list of segments.
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


def _render_segment(seg, tier, is_word_initial, unmapped):
    """
    Render a single segment for the given tier.
    `is_word_initial` is True only for the FIRST segment of a token (used by the
    Alaph rule).  `unmapped` is a set that collects any unmapped characters.
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
            # base consonant itself is unmapped; record it, pass base through,
            # and drop the marker per "pass it through unchanged" intent.
            unmapped.add(base)
            base_render = base
        if tier == ANGLICIZED:
            return base_render
        # scholarly / pretty: tier(C) + combining dot below
        return base_render + COMBINING_DOT_BELOW

    # Long-vowel segment (V + ː)
    if len(seg) == 2 and seg[1] == LENGTH_MARK:
        base = seg[0]
        entry = LONG_VOWELS.get(base)
        if entry is not None:
            return entry[idx]
        # Shouldn't happen (segmenter only makes these for known bases), but be safe.
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
        if tier == PRETTY:
            return "" if is_word_initial else "'"
        # anglicized
        return ""
    if ch == AYIN:  # ʕ
        if tier == SCHOLARLY:
            return "ʿ"  # ʿ
        if tier == PRETTY:
            return "ʿ"  # ʿ
        # anglicized
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


def transliterate(text, tier, unmapped=None):
    """
    Transliterate IPA `text` to Latin for the given `tier`
    (one of "scholarly", "pretty", "anglicized").

    Splits on spaces only (a single ASCII space ' ' separator), preserving each
    space verbatim.  Each token is segmented and rendered.  The first segment of
    a token is "word-initial" (used by the Alaph rule).

    If `unmapped` (a set) is supplied, any unmapped characters encountered are
    added to it.  Unmapped characters are passed through unchanged.
    """
    if tier not in _TIER_IDX:
        raise ValueError("Unknown tier: %r (expected one of %r)" % (tier, TIERS))
    if unmapped is None:
        unmapped = set()

    out_parts = []
    # Split on the ASCII space, keeping the separators so spaces are verbatim.
    # We process token / space / token / space ...
    tokens = text.split(" ")
    for ti, token in enumerate(tokens):
        if ti > 0:
            out_parts.append(" ")  # the space that split() consumed
        if token == "":
            continue
        segs = _segment_token(token)
        for si, seg in enumerate(segs):
            is_word_initial = (si == 0)
            out_parts.append(_render_segment(seg, tier, is_word_initial, unmapped))
    return "".join(out_parts)


def transliterate_line(line, tier, unmapped=None):
    """
    Transliterate a single corpus line of the form '<verse#>\\t<text>'.
    Keeps the '<verse#>\\t' prefix verbatim; only the text after the FIRST tab
    is transliterated.  Lines without a tab are returned unchanged.
    Trailing newline (if any) is preserved.
    """
    # Preserve trailing newline characters exactly.
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
    """Build the JSON-serializable mapping table (three tier dicts + rules)."""
    consonants = {ch: {SCHOLARLY: v[0], PRETTY: v[1], ANGLICIZED: v[2]}
                  for ch, v in CONSONANTS.items()}
    short_vowels = {ch: {SCHOLARLY: v[0], PRETTY: v[1], ANGLICIZED: v[2]}
                    for ch, v in SHORT_VOWELS.items()}
    long_vowels = {ch: {SCHOLARLY: v[0], PRETTY: v[1], ANGLICIZED: v[2]}
                   for ch, v in LONG_VOWELS.items()}
    emphatics_explicit = {ch: {SCHOLARLY: v[0], PRETTY: v[1], ANGLICIZED: v[2]}
                          for ch, v in EMPHATICS_EXPLICIT.items()}

    return {
        "meta": {
            "description": "Deterministic IPA->Latin mapping for the Peshitta corpus.",
            "tiers": list(TIERS),
            "note": "transliterate.py is authoritative; this file mirrors its hard-coded tables.",
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
            "word-initial = the FIRST segment of a token (used only by the Alaph rule).",
        ],
        "tier_dicts": {
            "consonants": consonants,
            "short_vowels": short_vowels,
            "long_vowels": long_vowels,
            "emphatics_explicit": emphatics_explicit,
        },
        "rules": {
            "alaph": {
                "symbol": ALAPH,
                SCHOLARLY: "always \\u02BE (ʾ)",
                PRETTY: "word-initial -> '' (drop); else -> \"'\"",
                ANGLICIZED: "always '' (drop)",
            },
            "ayin": {
                "symbol": AYIN,
                SCHOLARLY: "\\u02BF (ʿ)",
                PRETTY: "\\u02BF (ʿ)",
                ANGLICIZED: "'' (drop)",
            },
            "emphatic_fallback": {
                "applies_to": "any consonant + \\u02E4 not in emphatics_explicit",
                SCHOLARLY: "tier(C) + \\u0323 (combining dot below)",
                PRETTY: "tier(C) + \\u0323 (combining dot below)",
                ANGLICIZED: "tier(C)",
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
        "anglicized": "braysheeth eethawy wa meltha whoo meltha eethawy wa lwath alaha walaha eethawy wa hoo meltha",
    },
    {
        "ref": "John 1:2",
        "ipa": "hɑːnɑː ʔiːθawj wɑː breːʃiːθ lwɑːθ ʔɑːlɑːhɑː",
        "scholarly": "hānā ʾīṯawy wā brēšīṯ lwāṯ ʾālāhā",
        "pretty": "hānā īthawy wā brēshīth lwāth ālāhā",
        "anglicized": "hana eethawy wa braysheeth lwath alaha",
    },
    {
        "ref": "John 1:3",
        "ipa": "kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː",
        "scholarly": "kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā",
        "pretty": "kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā",
        "anglicized": "kul biydheh hwa wveladhawy afla khdha hwath medem dahwa",
    },
    {
        "ref": "Matthew 1:1",
        "ipa": "kθɑːvɑː diːliːðuːθeh djeʃuːʕ mʃiːħɑː breh dðawiːð breh dʔavrɑːhɑːm",
        "scholarly": "kṯāḇā dīlīḏūṯeh dyešūʿ mšīḥā breh dḏawīḏ breh dʾaḇrāhām",
        "pretty": "kthāvā dīlīdhūtheh dyeshūʿ mshīḥā breh ddhawīdh breh d'avrāhām",
        "anglicized": "kthava deeleedhootheh dyeshoo msheekha breh ddhaweedh breh davraham",
    },
    {
        "ref": "Romans 1:1",
        "ipa": "pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː",
        "scholarly": "pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā",
        "pretty": "pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā",
        "anglicized": "pawlaws avda dyeshoo msheekha qarya washleekha dethpresh lewangeliyyawn dalaha",
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
                print("PASS  %-14s %-11s" % (ref, tier))
            else:
                all_pass = False
                print("FAIL  %-14s %-11s" % (ref, tier))
                print("        expected: %r" % expected)
                print("        got:      %r" % got)
                # character-level first divergence
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
      -> English/Peshita_English/<Tier>/<Book>/<name>_<tier>.txt
    """
    rel = os.path.relpath(ipa_path, IPA_ROOT)        # <Book>/<name>_ipa.txt
    book_dir = os.path.dirname(rel)
    base = os.path.basename(rel)
    assert base.endswith("_ipa.txt"), base
    name = base[:-len("_ipa.txt")]                   # <name>
    tier_dir_name = {SCHOLARLY: "Scholarly", PRETTY: "Pretty", ANGLICIZED: "Anglicized"}[tier]
    out_name = "%s_%s.txt" % (name, tier)
    return os.path.join(ENGLISH_ROOT, tier_dir_name, book_dir, out_name)


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
        description="Deterministic IPA->Latin transliterator for the Peshitta corpus."
    )
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--selftest", action="store_true", help="run embedded gold cases")
    g.add_argument("--coverage", action="store_true", help="report chars not in mapping")
    g.add_argument("--build", action="store_true", help="transliterate whole corpus")
    g.add_argument("--write-mapping", action="store_true", help="(re)write mapping.json")
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
