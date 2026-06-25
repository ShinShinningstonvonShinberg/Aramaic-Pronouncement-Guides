# Schéma de translittération de la Peshitta (édition française)

## Overview / Vue d'ensemble

This folder contains a **3-tier Latin transliteration of the Peshitta for French
readers**, generated **deterministically** from the project's IPA pronunciation
guides (`IPA/Peshitta/**/<name>_ipa.txt`).

Every output character is produced by a single, rule-based converter
(`transliterate_fr.py`). There is no hand-editing and no machine-learning step: the
same IPA input always yields exactly the same Latin output. The IPA guides are the
single source of truth; the three Latin tiers are mechanical re-encodings of that
phonetic data.

The converter operates on the **phonetic** representation only. It splits text on
ASCII spaces (preserving them verbatim), segments each token using a longest-match
rule (consonant + `ˤ` → emphatic; vowel + `ː` → long vowel; otherwise a single
character), and renders each segment through one of three tier tables. Any character
not covered by the tables is passed through unchanged and reported, so the corpus
can never silently lose information.

## The Three Tiers / Les trois niveaux

| Tier | Audience | Philosophy |
|------|----------|------------|
| **Scholarly** | Semiticists, students of Syriac/Aramaic, anyone comparing against academic editions | **Language-neutral.** Maximum fidelity: standard scholarly diacritics (macrons for long vowels; underlined/dotted letters for spirantized and emphatic consonants; `ʾ` for *alaph* and `ʿ` for *ayin*). Nothing is collapsed or dropped — every phonemic distinction in the IPA is preserved. Byte-for-byte identical to the English Peshitta Scholarly tier. |
| **Pretty** | General readers who want accuracy and the look of the original | **Language-neutral.** A readable middle ground: long vowels keep their macrons, spirantized consonants use familiar digraphs (`sh`, `th`, `dh`, `kh`, `gh`, `v`). The pharyngeal `ʿ` (*ayin*) is kept; *alaph* is dropped word-initially and written `'` elsewhere. Byte-for-byte identical to the English Peshitta Pretty tier. |
| **FRENCHIFIED** | French speakers reading the Peshitta aloud | **French orthographic respelling.** Maximum approachability *for a French reader*: every sound is respelled the way French spelling would represent it, so a French speaker can sound the verse out on the first try. Uses French conventions such as `ch` for `ʃ`, `ou` for `u`, `è`/`é` for `e`/`eː`, and the French hard-g rule (`gu` before a front vowel). This is a reader aid, not a reversible scheme — the Scholarly tier remains the precise one. |

The **Scholarly** and **Pretty** tiers are *language-neutral*: their mapping logic is
copied verbatim from the English Peshitta converter, so the same verse renders
identically in `English/Peshita_English/Scholarly` and
`French/Peshita_French/Scholarly` (likewise for Pretty). Only the **FRENCHIFIED**
tier is specific to French.

## Frenchified Mapping Table / Table de correspondance (niveau FRENCHIFIED)

The full FRENCHIFIED table is given below. For the **Scholarly** and **Pretty**
columns, see the table in `English/Peshita_English/TRANSLITERATION_SCHEME.md` —
they match that document exactly.

### Plain Consonants

| IPA | Frenchified | Note |
|-----|-------------|------|
| `b` | b | |
| `d` | d | |
| `f` | f | |
| `k` | k | |
| `l` | l | |
| `m` | m | |
| `n` | n | |
| `p` | p | |
| `q` | q | |
| `r` | r | |
| `t` | t | |
| `v` | v | |
| `z` | z | |
| `w` | w | |
| `j` | y | the IPA glide `j` (yod), not the French *j* |

### Hard-g (context-sensitive)

| IPA | Context | Frenchified | Note |
|-----|---------|-------------|------|
| `ɡ` | before a front vowel `/e/`, `/eː/`, `/i/`, `/iː/` (next segment) | gu | French hard-g spelling (so `ge`/`gi` are not read as soft *g*) |
| `ɡ` | otherwise | g | |

### s (intervocalic, context-sensitive)

| IPA | Context | Frenchified | Note |
|-----|---------|-------------|------|
| `s` | **both** neighbouring segments are vowels (truly intervocalic) | ss | prevents a French reader pronouncing a single intervocalic *s* as `/z/` |
| `s` | otherwise | s | |

The same intervocalic rule applies to the emphatic `sˤ` (see Emphatics). The test
uses the **literal** adjacent IPA segments within the token. A *dropped* glottal —
*ayin* (`ʕ`) anywhere, or a word-initial *alaph* (`ʔ`) — is still a **consonant**
segment, not a vowel, so it is opaque and is never skipped over. For example
`treʕsar` → `trèsar` (single *s*, because its left neighbour is the `ʕ` segment),
while a genuinely intervocalic *s* doubles, e.g. `pesˤe` → `pèssè`. A
word-initial *s* before a vowel across a space stays single (its neighbour is `None`
across the token boundary).

### Spirantized / Foreign-approximated Consonants

| IPA | Frenchified | Note |
|-----|-------------|------|
| `ʃ` | ch | French digraph for `/ʃ/` |
| `θ` | th | approximation (no native French `/θ/`) |
| `ð` | dh | approximation (no native French `/ð/`) |
| `x` | kh | approximation (no native French `/x/`) |
| `ɣ` | gh | approximation (no native French `/ɣ/`) |
| `ħ` | h | approximation; the French *h* is usually silent (see Limitations) |
| `h` | h | the French *h* is usually silent (see Limitations) |

### Glottal / Pharyngeal

| IPA | Name | Frenchified | Note |
|-----|------|-------------|------|
| `ʔ` | *alaph* | dropped word-initial, else `'` | "word-initial" = first segment of a whitespace/**hyphen** token, so a post-hyphen *alaph* also drops (e.g. `bar-ʔaba` → `bar-aba`) |
| `ʕ` | *ayin* | dropped everywhere | not producible by French speakers |

### Emphatics (consonant + `ˤ`)

| IPA | Frenchified | Note |
|-----|-------------|------|
| `tˤ` | t | emphasis dropped |
| `sˤ` | s / ss | same intervocalic rule as plain `s` |
| *any other* `Cˤ` | the plain consonant `C` | emphasis dropped; generic fallback |

### Short Vowels (no length mark)

| IPA | Frenchified | Note |
|-----|-------------|------|
| `a` | a | |
| `ɑ` | a | |
| `e` | è | French open-e spelling |
| `i` | i | |
| `o` | o | |
| `u` | ou | French `/u/` spelling |

### Long Vowels (vowel + `ː`)

Length is collapsed (rendered by quality), **except** `eː`, which is the one
length-sensitive distinction.

| IPA | Frenchified | Note |
|-----|-------------|------|
| `aː` | a | |
| `ɑː` | a | |
| `eː` | é | the only length distinction kept (`e` → `è`, `eː` → `é`) |
| `iː` | i | |
| `oː` | o | |
| `uː` | ou | |

### Other Literals

| Symbol | All tiers |
|--------|-----------|
| `-` (hyphen) | `-` |
| space | preserved verbatim |
| anything else | passed through unchanged and reported |

A machine-readable mirror of all of these tables (every tier) lives in
`transliteration_mapping_fr.json` in this folder.

## Documented Limitations (FRENCHIFIED tier)

The FRENCHIFIED tier is a *reader aid*, deliberately lossy. Known approximations:

1. **Silent French *h*.** French has no `/h/` phoneme, and the written *h* is
   usually silent to a French reader. Both `h` (from IPA `/h/`) and `h` (the
   approximation chosen for the pharyngeal `ħ`) may simply be dropped when read
   aloud. The two also collapse to the same letter, so the `/h/` vs `/ħ/`
   distinction is not recoverable from the Frenchified text.
2. **Possible nasalization of vowel + n/m.** A vowel immediately followed by `n` or
   `m` may be read by a French speaker as a French *nasal* vowel (e.g. *an*, *on*,
   *in*) rather than as vowel-plus-consonant. The transliteration does not try to
   prevent this.
3. **Approximated foreign consonants.** `θ` (`th`), `ð` (`dh`), `x` (`kh`),
   `ɣ` (`gh`), `ħ` (`h`) and the emphatics have no native French equivalents and are
   only approximations. The pharyngeal `ʕ` (*ayin*) is not producible by French
   speakers and is dropped everywhere, and a word-initial `ʔ` (*alaph*) is also
   dropped.

For full fidelity (no dropped sounds, every distinction preserved), use the
**Scholarly** tier.

## Worked Example / Exemple détaillé

Three verses, shown in source IPA followed by all three tiers. These are the
embedded gold cases used by `--selftest`, so they are guaranteed to match the
shipped converter exactly.

### John 1:1

```
IPA         breːʃiːθ ʔiːθawj wɑː melθɑː whuː melθɑː ʔiːθawj wɑː lwɑːθ ʔɑːlɑːhɑː waʔlɑːhɑː ʔiːθawj wɑː huː melθɑː
Scholarly   brēšīṯ ʾīṯawy wā melṯā whū melṯā ʾīṯawy wā lwāṯ ʾālāhā waʾlāhā ʾīṯawy wā hū melṯā
Pretty      brēshīth īthawy wā melthā whū melthā īthawy wā lwāth ālāhā wa'lāhā īthawy wā hū melthā
Frenchified bréchith ithawy wa mèltha whou mèltha ithawy wa lwath alaha wa'laha ithawy wa hou mèltha
```

### John 1:3

```
IPA         kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː
Scholarly   kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā
Pretty      kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā
Frenchified koul b'iydhèh hwa wvèladhawy afla hdha hwath mèdèm dahwa
```

### Romans 1:1

```
IPA         pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː
Scholarly   pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā
Pretty      pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā
Frenchified pawlaws avda dyèchou mchiha qarya wachliha d'èthprèch lè'wanguèliyyawn d'alaha
```

## Folder Layout / Arborescence

Everything lives under the repository path `French/Peshita_French/`
(relative to the repo root):

```
French/Peshita_French/
├── TRANSLITERATION_SCHEME.md          # this document
├── transliterate_fr.py                # the deterministic converter (authoritative)
├── transliteration_mapping_fr.json    # machine-readable mirror of the mapping tables
├── Scholarly/                         # tier 1 output (language-neutral)
│   ├── Matthew-Matityahu/
│   │   ├── matthewmatityahu1_scholarly.txt
│   │   └── ...
│   ├── 1stCorinthians/
│   └── ...                            # 27 book folders
├── Pretty/                            # tier 2 output (language-neutral, *_pretty.txt)
│   └── ...
└── Frenchified/                       # tier 3 output (French respelling, *_frenchified.txt)
    └── ...
```

Each tier directory (`Scholarly/`, `Pretty/`, `Frenchified/`) mirrors the
book/chapter structure of `IPA/Peshitta/`. For every source file
`IPA/Peshitta/<Book>/<name>_ipa.txt` the build produces one file per tier at
`French/Peshita_French/<Tier>/<Book>/<name>_<tier>.txt`. Each output line keeps its
`<verse#>\t` prefix verbatim; only the verse text after the first tab is
transliterated.

The current corpus is **260 IPA source files** across **27 books**, yielding
**780 transliterated files** (260 × 3 tiers).

## Reproducing / Reproduire

The whole corpus can be regenerated from scratch with one command, run from this
folder:

```sh
python3 transliterate_fr.py --build
```

This walks every `*_ipa.txt` under `IPA/Peshitta/`, transliterates each into all
three tiers, and writes the `Scholarly/`, `Pretty/`, and `Frenchified/` trees
described above. It reports the number of files written and any unmapped characters
(there should be none).

The converter locates the repository automatically: it derives the repo root from
its own file location (two directories up from `French/Peshita_French/`), so
`--build` works from this shipped folder without any extra configuration.

Other useful entry points:

```sh
python3 transliterate_fr.py --selftest        # run the embedded gold cases (John 1:1, John 1:3, Romans 1:1, etc.)
python3 transliterate_fr.py --coverage        # scan the corpus for characters not in the mapping
python3 transliterate_fr.py --write-mapping   # (re)write the machine-readable mapping mirror
```

`transliterate_fr.py` is authoritative: the JSON mapping is a machine-readable
mirror of its hard-coded tables. The `--build`, `--selftest`, and `--coverage`
entry points read only those hard-coded tables, never the JSON, so they are
unaffected by the mapping file's name.

---

*Prepared and signed by **Shin**.*
