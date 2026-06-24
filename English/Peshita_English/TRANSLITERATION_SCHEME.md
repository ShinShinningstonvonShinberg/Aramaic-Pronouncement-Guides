# Peshitta Latin Transliteration Scheme

## Overview

This folder contains a **3-tier Latin transliteration of the Peshitta**, generated
**deterministically** from the project's IPA pronunciation guides
(`IPA/Peshitta/**/<name>_ipa.txt`).

Every output character is produced by a single, rule-based converter
(`transliterate.py`). There is no hand-editing and no machine-learning step: the
same IPA input always yields exactly the same Latin output. The IPA guides are the
single source of truth; the three Latin tiers are mechanical re-encodings of that
phonetic data for three different audiences.

The converter operates on the **phonetic** representation only. It splits text on
ASCII spaces (preserving them verbatim), segments each token using a longest-match
rule, and renders each segment through one of three tier tables. Any character not
covered by the tables is passed through unchanged and reported, so the corpus can
never silently lose information.

## The Three Tiers

| Tier | Audience | Philosophy |
|------|----------|------------|
| **Scholarly** | Semiticists, students of Syriac/Aramaic, anyone comparing against academic editions | Maximum fidelity. Uses the standard scholarly diacritics (macrons for long vowels; underlined/dotted letters for spirantized and emphatic consonants; `ʾ` for *alaph* and `ʿ` for *ayin*). Nothing is collapsed or dropped — every phonemic distinction in the IPA is preserved. |
| **Pretty** | General readers who still want accuracy and the look of the original | A readable middle ground. Long vowels keep their macrons, but spirantized consonants use familiar digraphs (`sh`, `th`, `dh`, `kh`, `gh`, `v`) instead of underlined letters. The pharyngeal `ʿ` (*ayin*) is kept; *alaph* is dropped word-initially and written `'` elsewhere. |
| **Anglicized** | First-time readers and English speakers reading aloud | Maximum approachability. No diacritics at all. Long vowels are spelled out the way an English speaker would sound them (`ay`, `ee`, `oh`, `oo`, and plain `a`). Both glottal/pharyngeal markers (*alaph*, *ayin*) are dropped, and emphatics collapse to their plain consonants. The goal is "say it roughly right on the first try." |

## Mapping Table

Tier order in every row below: **Scholarly | Pretty | Anglicized**.

### Plain Consonants

| IPA | Scholarly | Pretty | Anglicized |
|-----|-----------|--------|------------|
| `b` | b | b | b |
| `ɡ` | g | g | g |
| `d` | d | d | d |
| `h` | h | h | h |
| `w` | w | w | w |
| `z` | z | z | z |
| `k` | k | k | k |
| `l` | l | l | l |
| `m` | m | m | m |
| `n` | n | n | n |
| `s` | s | s | s |
| `p` | p | p | p |
| `q` | q | q | q |
| `r` | r | r | r |
| `t` | t | t | t |
| `f` | f | f | f |
| `j` | y | y | y |

### Spirantized (begadkepat) Consonants

| IPA | Scholarly | Pretty | Anglicized |
|-----|-----------|--------|------------|
| `v` | ḇ | v | v |
| `ʃ` | š | sh | sh |
| `θ` | ṯ | th | th |
| `ð` | ḏ | dh | dh |
| `x` | ḵ | kh | kh |
| `ɣ` | ḡ | gh | gh |
| `ħ` | ḥ | ḥ | kh |

### Glottal / Pharyngeal

| IPA | Name | Scholarly | Pretty | Anglicized |
|-----|------|-----------|--------|------------|
| `ʔ` | *alaph* | `ʾ` (always) | dropped word-initial, else `'` | dropped (always) |
| `ʕ` | *ayin* | `ʿ` | `ʿ` | dropped |

### Emphatics (consonant + `ˤ`)

| IPA | Scholarly | Pretty | Anglicized |
|-----|-----------|--------|------------|
| `tˤ` | ṭ | ṭ | t |
| `sˤ` | ṣ | ṣ | s |
| *any other* `Cˤ` | tier(C) + combining dot below ( ̣ ) | tier(C) + combining dot below ( ̣ ) | tier(C) |

### Short Vowels (no length mark)

Identical across all three tiers.

| IPA | Scholarly | Pretty | Anglicized |
|-----|-----------|--------|------------|
| `a` | a | a | a |
| `ɑ` | a | a | a |
| `e` | e | e | e |
| `i` | i | i | i |
| `o` | o | o | o |
| `u` | u | u | u |

### Long Vowels (vowel + `ː`)

| IPA | Scholarly | Pretty | Anglicized |
|-----|-----------|--------|------------|
| `aː` | ā | ā | a |
| `ɑː` | ā | ā | a |
| `eː` | ē | ē | ay |
| `iː` | ī | ī | ee |
| `oː` | ō | ō | oh |
| `uː` | ū | ū | oo |

### Other Literals

| Symbol | All tiers |
|--------|-----------|
| `-` (hyphen) | `-` |
| space | preserved verbatim |
| anything else | passed through unchanged and reported |

## Worked Example

Three verses, shown in source IPA followed by all three tiers. These are the
embedded gold cases used by `--selftest`, so they are guaranteed to match the
shipped converter exactly.

### John 1:1

```
IPA        breːʃiːθ ʔiːθawj wɑː melθɑː whuː melθɑː ʔiːθawj wɑː lwɑːθ ʔɑːlɑːhɑː waʔlɑːhɑː ʔiːθawj wɑː huː melθɑː
Scholarly  brēšīṯ ʾīṯawy wā melṯā whū melṯā ʾīṯawy wā lwāṯ ʾālāhā waʾlāhā ʾīṯawy wā hū melṯā
Pretty     brēshīth īthawy wā melthā whū melthā īthawy wā lwāth ālāhā wa'lāhā īthawy wā hū melthā
Anglicized braysheeth eethawy wa meltha whoo meltha eethawy wa lwath alaha walaha eethawy wa hoo meltha
```

### John 1:3

```
IPA        kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː
Scholarly  kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā
Pretty     kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā
Anglicized kul biydheh hwa wveladhawy afla khdha hwath medem dahwa
```

### Romans 1:1

```
IPA        pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː
Scholarly  pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā
Pretty     pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā
Anglicized pawlaws avda dyeshoo msheekha qarya washleekha dethpresh lewangeliyyawn dalaha
```

## Folder Layout

Everything lives under the repository path
`English/Peshita_English/` (relative to the repo root):

```
English/Peshita_English/
├── TRANSLITERATION_SCHEME.md       # this document
├── transliterate.py                # the deterministic converter (authoritative)
├── transliteration_mapping.json    # machine-readable mirror of the mapping tables
├── Scholarly/                      # tier 1 output
│   ├── Matthew-Matityahu/
│   │   ├── matthewmatityahu1_scholarly.txt
│   │   ├── matthewmatityahu2_scholarly.txt
│   │   └── ...
│   ├── 1stCorinthians/
│   └── ...                         # 27 book folders
├── Pretty/                         # tier 2 output (same tree, *_pretty.txt)
│   └── ...
└── Anglicized/                     # tier 3 output (same tree, *_anglicized.txt)
    └── ...
```

Each tier directory (`Scholarly/`, `Pretty/`, `Anglicized/`) mirrors the book/chapter
structure of `IPA/Peshitta/`. For every source file
`IPA/Peshitta/<Book>/<name>_ipa.txt` the build produces one file per tier at
`English/Peshita_English/<Tier>/<Book>/<name>_<tier>.txt`. Each output line keeps its
`<verse#>\t` prefix verbatim; only the verse text after the first tab is transliterated.

The current corpus is **260 IPA source files** across **27 books**, yielding
**780 transliterated files** (260 × 3 tiers).

## Reproducing

The whole corpus can be regenerated from scratch with one command, run from this
folder:

```sh
python3 transliterate.py --build
```

This walks every `*_ipa.txt` under `IPA/Peshitta/`, transliterates each into all
three tiers, and writes the `Scholarly/`, `Pretty/`, and `Anglicized/` trees
described above. It reports the number of files written and any unmapped characters
(there should be none).

Other useful entry points:

```sh
python3 transliterate.py --selftest        # run the embedded gold cases (John 1:1, John 1:3, Romans 1:1, etc.)
python3 transliterate.py --coverage        # scan the corpus for characters not in the mapping
python3 transliterate.py --write-mapping   # (re)write transliteration_mapping.json from the authoritative tables
```

`transliterate.py` is authoritative: `transliteration_mapping.json` is a
machine-readable mirror of its hard-coded tables, regenerated by `--write-mapping`.

---

*Prepared and signed by **Shin**.*
