# Esquema de Transliteración de la Peshitta (Español)

## Overview / Visión general

This folder contains a **3-tier Latin transliteration of the Peshitta**, aimed at
**Spanish-speaking readers**, generated **deterministically** from the project's
IPA pronunciation guides (`IPA/Peshitta/**/<name>_ipa.txt`).

Every output character is produced by a single, rule-based converter
(`transliterate_es.py`). There is no hand-editing and no machine-learning step:
the same IPA input always yields exactly the same Latin output. The IPA guides are
the single source of truth; the three Latin tiers are mechanical re-encodings of
that phonetic data for three different audiences.

The converter operates on the **phonetic** representation only. It splits text on
ASCII spaces (preserving them verbatim), segments each token using a longest-match
rule, and renders each segment through one of three tier tables. Any character not
covered by the tables is passed through unchanged and reported, so the corpus can
never silently lose information.

## The Three Tiers / Los tres niveles

| Tier | Audience | Philosophy |
|------|----------|------------|
| **Scholarly** | Semiticists, students of Syriac/Aramaic, anyone comparing against academic editions | **Language-neutral.** Maximum fidelity. Uses the standard scholarly diacritics (macrons for long vowels; underlined/dotted letters for spirantized and emphatic consonants; `ʾ` for *alaph* and `ʿ` for *ayin*). Nothing is collapsed or dropped — every phonemic distinction in the IPA is preserved. **Byte-for-byte identical to the English Peshitta's Scholarly tier.** |
| **Pretty** | General readers who want accuracy and the look of the original | **Language-neutral.** A readable middle ground. Long vowels keep their macrons, but spirantized consonants use familiar digraphs (`sh`, `th`, `dh`, `kh`, `gh`, `v`) instead of underlined letters. The pharyngeal `ʿ` (*ayin*) is kept; *alaph* is dropped word-initially and written `'` elsewhere. **Byte-for-byte identical to the English Peshitta's Pretty tier.** |
| **Hispanicized** | First-time readers reading aloud in Spanish | **Spanish orthographic respelling.** Maximum approachability *for a Spanish speaker*. The Aramaic phonetics are re-spelled so a reader applying ordinary Spanish letter-to-sound rules lands roughly on the right pronunciation: `j` for the back fricatives (Spanish `j` = /x/), the hard-`g`/`gu` rule before front vowels, `z` for /θ/, and the clean Spanish 5-vowel system with no vowel-length marks. Both glottal/pharyngeal markers are mostly dropped, and emphatics collapse to their plain consonants. The goal is "say it roughly right on the first try, reading it as Spanish." |

Because **Scholarly** and **Pretty** are language-neutral, they are produced by the
exact same logic as the English Peshitta and their output matches it character for
character. If you need those two tiers, the canonical reference is
`English/Peshita_English/TRANSLITERATION_SCHEME.md`; only the **Hispanicized** tier
is unique to this folder, so the mapping table below documents it in full.

## Hispanicized Mapping Table / Tabla de correspondencias

The full Hispanicized rendering of every IPA symbol. The **Scholarly** and
**Pretty** columns are shown for reference but are identical to
`English/Peshita_English`; see that document for their rationale.

Tier order in every row: **Scholarly | Pretty | Hispanicized**.

### Plain Consonants / Consonantes simples

| IPA | Scholarly | Pretty | Hispanicized | Note |
|-----|-----------|--------|--------------|------|
| `b` | b | b | b | |
| `ɡ` | g | g | **g / gu** | hard-g rule (see below) |
| `d` | d | d | d | |
| `h` | h | h | h | Spanish `h` is silent (see Limitations) |
| `w` | w | w | w | |
| `z` | z | z | **s** | Spanish has no phonemic /z/; nearest /s/ |
| `k` | k | k | k | |
| `l` | l | l | l | |
| `m` | m | m | m | |
| `n` | n | n | n | |
| `s` | s | s | s | |
| `p` | p | p | p | |
| `q` | q | q | **k** | no /q/ in Spanish; nearest /k/ |
| `r` | r | r | r | |
| `t` | t | t | t | |
| `f` | f | f | f | |
| `j` | y | y | y | (IPA palatal glide) |

### Spirantized (begadkepat) Consonants / Consonantes espirantizadas

| IPA | Scholarly | Pretty | Hispanicized | Note |
|-----|-----------|--------|--------------|------|
| `v` | ḇ | v | **v** | Spanish reads `v` as [b]~[β] |
| `ʃ` | š | sh | **sh** | |
| `θ` | ṯ | th | **z** | Castilian `z` = /θ/ (Latin-American /s/) |
| `ð` | ḏ | dh | **d** | Spanish intervocalic `d` already is [ð] |
| `x` | ḵ | kh | **j** | Spanish `j` = /x/, an exact match |
| `ɣ` | ḡ | gh | **g / gu** | hard-g rule (see below) |
| `ħ` | ḥ | ḥ | **j** | approximates the pharyngeal with /x/ |

### Glottal / Pharyngeal / Glotales y faríngeas

| IPA | Name | Scholarly | Pretty | Hispanicized |
|-----|------|-----------|--------|--------------|
| `ʔ` | *alaph* | `ʾ` (always) | dropped word-initial, else `'` | **dropped word-initial, else `'`** |
| `ʕ` | *ayin* | `ʿ` | `ʿ` | **dropped everywhere** |

For the Hispanicized tier, a token boundary is whitespace **or a hyphen**, so a
*alaph* immediately after a hyphen (e.g. `bar-ʔaba`) counts as word-initial and is
dropped → `bar-aba`. (Scholarly and Pretty keep the English transducer's
space-only boundary so they stay identical to the English Peshitta.)

### Emphatics (consonant + `ˤ`) / Enfáticas

| IPA | Scholarly | Pretty | Hispanicized |
|-----|-----------|--------|--------------|
| `tˤ` | ṭ | ṭ | **t** |
| `sˤ` | ṣ | ṣ | **s** |
| *any other* `Cˤ` | tier(C) + combining dot below ( ̣ ) | tier(C) + combining dot below ( ̣ ) | **tier(C)** (emphasis dropped) |

### Short Vowels (no length mark) / Vocales breves

Identical across all three tiers — the clean Spanish 5-vowel system.

| IPA | Scholarly | Pretty | Hispanicized |
|-----|-----------|--------|--------------|
| `a` | a | a | a |
| `ɑ` | a | a | a |
| `e` | e | e | e |
| `i` | i | i | i |
| `o` | o | o | o |
| `u` | u | u | u |

### Long Vowels (vowel + `ː`) / Vocales largas

Spanish has no phonemic vowel length, so the Hispanicized tier **collapses** length
(no macron, same letter as the short vowel).

| IPA | Scholarly | Pretty | Hispanicized |
|-----|-----------|--------|--------------|
| `aː` | ā | ā | a |
| `ɑː` | ā | ā | a |
| `eː` | ē | ē | e |
| `iː` | ī | ī | i |
| `oː` | ō | ō | o |
| `uː` | ū | ū | u |

### The Hard-g Rule / La regla de la g dura

In the Hispanicized tier, `ɡ` and `ɣ` are spelled to keep the **hard /g/** sound
under ordinary Spanish reading rules. Spanish `g` is read as /x/ (the `j` sound)
before the front vowels `e` and `i`, so:

- before a front vowel (`e`, `eː`, `i`, `iː`) → **`gu`** (the silent-`u` digraph that
  preserves hard /g/, e.g. *guerra*, *guitarra*);
- everywhere else → **`g`**.

Example: the segment `ɡe`/`ɡi` becomes `gue`/`gui`. In Romans 1:1 the cluster
`…ɡelijjɑːwn…` is rendered `…guelijjawn…` for exactly this reason.

### Back-fricative / θ / z choices / Elecciones de fricativas posteriores

- **Back fricatives `x` and `ħ` → `j`.** Spanish `j` is /x/, a near-exact match for
  the velar `x`; the pharyngeal `ħ` is approximated by the same /x/.
- **`θ` → `z`.** Spanish `z` is /θ/ in Castilian (the original *th* sound), which is
  the closest single-letter Spanish spelling; Latin-American readers will say /s/.
- **`ð` → `d`** and **soft `ɣ` → `g`** lean on Spanish's own spirantization: an
  intervocalic `d` is already pronounced [ð] and an intervocalic `g` [ɣ], so the
  plain letters land on the right sound automatically.

### Other Literals / Otros literales

| Symbol | All tiers |
|--------|-----------|
| `-` (hyphen) | `-` |
| space | preserved verbatim |
| anything else | passed through unchanged and reported |

## Documented Limitations / Limitaciones documentadas

The Hispanicized tier is a **reader-aid**, not a reversible scholarly transcription.
Spanish lacks several Aramaic phonemes, so the following information is intentionally
approximated or lost. Use the **Scholarly** tier when precision matters.

- **Silent Spanish `h`.** The Aramaic `h` (*he*) is kept as the letter `h`, but a
  Spanish reader will normally not pronounce it at all (Spanish `h` is mute). The
  sound is effectively dropped on reading even though the letter is preserved.
- **/z/ → `s` (voicing lost).** Spanish has no phonemic /z/, so `z` is respelled `s`;
  the voiced/voiceless distinction disappears.
- **`θ` → `z` is dialect-split.** It yields Castilian /θ/ (correct) but Latin-American
  /s/ (merged with `s`), so the θ/s contrast is not recoverable for *seseo* readers.
- **Collapsed back fricatives.** The velar `x` and the pharyngeal `ħ` both map to `j`
  (/x/), so they are no longer distinguished; the pharyngeal place of articulation is
  not represented.
- **Dropped *ayin* and initial *alaph*.** *Ayin* (`ʕ`) is dropped everywhere and a
  word-initial *alaph* (`ʔ`) is dropped, so those consonantal slots vanish in the
  Hispanicized text.
- **No vowel length.** Long vowels collapse onto their short counterparts; vowel
  length is not represented.
- **Emphasis lost.** Emphatic `tˤ`/`sˤ` collapse to plain `t`/`s`.

All of these distinctions are fully preserved in the **Scholarly** tier (and most in
**Pretty**), which is why those tiers remain language-neutral.

## Worked Example / Ejemplo trabajado

Three verses, shown in source IPA followed by all three tiers. These values come
straight from the converter (they are the embedded gold cases used by
`--selftest`), so they are guaranteed to match the shipped tool exactly.

### John 1:1

```
IPA          breːʃiːθ ʔiːθawj wɑː melθɑː whuː melθɑː ʔiːθawj wɑː lwɑːθ ʔɑːlɑːhɑː waʔlɑːhɑː ʔiːθawj wɑː huː melθɑː
Scholarly    brēšīṯ ʾīṯawy wā melṯā whū melṯā ʾīṯawy wā lwāṯ ʾālāhā waʾlāhā ʾīṯawy wā hū melṯā
Pretty       brēshīth īthawy wā melthā whū melthā īthawy wā lwāth ālāhā wa'lāhā īthawy wā hū melthā
Hispanicized breshiz izawy wa melza whu melza izawy wa lwaz alaha wa'laha izawy wa hu melza
```

### John 1:3

```
IPA          kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː
Scholarly    kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā
Pretty       kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā
Hispanicized kul b'iydeh hwa wveladawy afla jda hwaz medem dahwa
```

### Romans 1:1

```
IPA          pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː
Scholarly    pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā
Pretty       pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā
Hispanicized pawlaws avda dyeshu mshija karya washlija d'ezpresh le'wangueliyyawn d'alaha
```

Note in Romans 1:1 how `ɡe` surfaces as `gue` (hard-g rule), `θ` as `z`
(`dʔeθpreʃ` → `d'ezpresh`), `ʃ` as `sh`, `ħ` as `j` (`mʃiːħɑː` → `mshija`),
and both *ayin* and the word-initial *alaph* drop out (`ʕavdɑː` → `avda`,
`dʔ…` → `d'…`).

## Folder Layout / Estructura de carpetas

Everything lives under the repository path `Spanish/Peshita_Spanish/`
(relative to the repo root):

```
Spanish/Peshita_Spanish/
├── TRANSLITERATION_SCHEME.md          # this document
├── transliterate_es.py                # the deterministic converter (authoritative)
├── transliteration_mapping_es.json    # machine-readable mirror of the mapping tables
├── Scholarly/                         # tier 1 output (language-neutral)
│   ├── Matthew-Matityahu/
│   │   ├── matthewmatityahu1_scholarly.txt
│   │   ├── matthewmatityahu2_scholarly.txt
│   │   └── ...
│   ├── 1stCorinthians/
│   └── ...                            # 27 book folders
├── Pretty/                            # tier 2 output (same tree, *_pretty.txt)
│   └── ...
└── Hispanicized/                      # tier 3 output (same tree, *_hispanicized.txt)
    └── ...
```

Each tier directory (`Scholarly/`, `Pretty/`, `Hispanicized/`) mirrors the
book/chapter structure of `IPA/Peshitta/`. For every source file
`IPA/Peshitta/<Book>/<name>_ipa.txt` the build produces one file per tier at
`Spanish/Peshita_Spanish/<Tier>/<Book>/<name>_<tier>.txt`. Each output line keeps
its `<verse#>\t` prefix verbatim; only the verse text after the first tab is
transliterated.

The current corpus is **260 IPA source files** across **27 books**, yielding
**780 transliterated files** (260 × 3 tiers).

## Reproducing / Reproducción

The whole corpus can be regenerated from scratch with one command, run from this
folder:

```sh
python3 transliterate_es.py --build
```

This walks every `*_ipa.txt` under `IPA/Peshitta/`, transliterates each into all
three tiers, and writes the `Scholarly/`, `Pretty/`, and `Hispanicized/` trees
described above. It reports the number of files written and any unmapped characters
(there should be none). The converter resolves the repository root from its own
location, so it runs correctly from this shipped folder.

Other useful entry points:

```sh
python3 transliterate_es.py --selftest        # run the embedded gold cases (John 1:1, John 1:3, Romans 1:1, etc.)
python3 transliterate_es.py --coverage        # scan the corpus for characters not in the mapping
python3 transliterate_es.py --write-mapping   # (re)write transliteration_mapping_es.json from the authoritative tables
```

`transliterate_es.py` is authoritative: `transliteration_mapping_es.json` is a
machine-readable mirror of its hard-coded tables, regenerated by `--write-mapping`.
The **Scholarly** and **Pretty** tiers reuse the English transducer's logic verbatim,
so their output matches `English/Peshita_English` character for character.

---

*Prepared and signed by **Shin**.*
