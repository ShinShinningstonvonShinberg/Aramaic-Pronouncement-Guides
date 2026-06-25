# Peshitta Korean Transliteration Scheme (한국어)

## Overview / 개요

This folder contains a **4-tier transliteration of the Peshitta**, aimed at
**Korean-speaking readers**, generated **deterministically** from the project's
IPA pronunciation guides (`IPA/Peshitta/**/<name>_ipa.txt`).

Every output character is produced by a single, rule-based converter
(`transliterate_ko.py`). There is no hand-editing and no machine-learning step:
the same IPA input always yields exactly the same output. The IPA guides are the
single source of truth; the four tiers are mechanical re-encodings of that
phonetic data for different audiences.

The two scholarly tiers operate on the **phonetic** representation only. They
split text on ASCII spaces (preserving them verbatim), segment each token using a
longest-match rule, and render each segment through a tier table. The two Korean
**reader** tiers (Hangul and Romanized) go a step further: they re-syllabify the
phonetic stream into legal Korean syllable blocks before composing precomposed
Hangul, and the Romanized tier is then a Revised-Romanization (RR) readback of
that Hangul — so the two reader tiers are guaranteed mutually consistent.

Any character not covered by the tables is passed through unchanged and reported,
so the corpus can never silently lose information.

## The Four Tiers / 네 개의 단계

| Tier | Audience | Philosophy |
|------|----------|------------|
| **Scholarly** | Semiticists, students of Syriac/Aramaic, anyone comparing against academic editions | **Language-neutral.** Maximum fidelity. Uses the standard scholarly diacritics (macrons for long vowels; underlined/dotted letters for spirantized and emphatic consonants; `ʾ` for *alaph* and `ʿ` for *ayin*). Nothing is collapsed or dropped — every phonemic distinction in the IPA is preserved. **Byte-for-byte identical to the English Peshitta's Scholarly tier.** |
| **Pretty** | General readers who want accuracy and the look of the original | **Language-neutral.** A readable middle ground. Long vowels keep their macrons, but spirantized consonants use familiar digraphs (`sh`, `th`, `dh`, `kh`, `gh`, `v`) instead of underlined letters. The pharyngeal `ʿ` (*ayin*) is kept; *alaph* is dropped word-initially and written `'` elsewhere. **Byte-for-byte identical to the English Peshitta's Pretty tier.** |
| **Hangul** | First-time Korean readers reading aloud in 한글 | **Native composed Hangul blocks.** The Aramaic phonetics are mapped to Korean jamo and re-syllabified into legal `(C)(G)V(C)` blocks, then composed into precomposed Hangul (가–힣). A reader applying ordinary Korean letter-to-sound rules lands roughly on the right pronunciation. Korean phonotactics are obeyed: no onset clusters, restricted codas, an epenthetic ㅡ where needed. |
| **Romanized** | Readers who want the Hangul reading in the Latin alphabet | **Revised-Romanization (RR) readback** of the generated Hangul, syllable by syllable. Derived directly from the Hangul tier (decompose each block to cho/jung/jong, map to RR letters), so it is exactly "how the Hangul reads," with **no cross-syllable sandhi** (a documented limitation). |

Because **Scholarly** and **Pretty** are language-neutral, they are produced by
the exact same logic as the English Peshitta and their output matches it character
for character. If you need those two tiers, the canonical reference is
`English/Peshita_English/TRANSLITERATION_SCHEME.md`; the **Hangul** and
**Romanized** reader tiers are unique to this folder, so the mapping tables below
document them in full.

## Segmentation / 분절

Both reader tiers start from the same longest-match segmentation as the scholarly
tiers:

- Split on the ASCII space `" "` only; spaces are preserved verbatim.
- Within each token, left-to-right longest match:
  1. consonant + `ˤ` (U+02E4) → emphatic segment (2 chars)
  2. vowel (`a ɑ e i o u`) + `ː` (U+02D0) → long-vowel segment (2 chars)
  3. otherwise a single character
- For the reader tiers, an internal hyphen `-` also splits a token into Hangul
  word-pieces (the hyphen is preserved in the output), so `bar-ʔaba` renders as
  two blocks joined by `-`.

---

# Hangul Reader Tier

The Hangul tier converts the IPA phonetic stream into composed Hangul syllable
blocks in three steps: **(1)** map each IPA segment to jamo, **(2)** syllabify
into legal `(C)(G)V(C)` blocks (inserting an epenthetic ㅡ where Korean
phonotactics forbid a cluster or coda), and **(3)** compose precomposed Hangul via
the 0xAC00 formula.

## 1. Jamo Mapping Tables / 자모 대응표

These reflect the **finalized** mappings hard-coded in `transliterate_ko.py`.

### Consonants → choseong / jongseong (자음)

A consonant becomes a *choseong* (initial) when it begins a syllable and a
*jongseong* (final/batchim) when it codas one (after neutralization).

| IPA | Jamo | Note |
|-----|------|------|
| `b` | ㅂ | |
| `v` | ㅂ | merges with `b` (no /v/ in Korean) |
| `p` | ㅍ | |
| `f` | ㅍ | merges with `p` (no /f/ in Korean) |
| `t` | ㅌ | |
| `d` | ㄷ | |
| `ð` | ㄷ | merges with `d` |
| `k` | ㅋ | |
| `q` | ㅋ | merges with `k` (no /q/ in Korean) |
| `ɡ` | ㄱ | |
| `ɣ` | ㄱ | merges with `ɡ` |
| `s` | ㅅ | |
| `z` | ㅈ | nearest available; voiced distinction lost |
| `θ` | ㅅ | plain (not tense); merges with `s` |
| `ʃ` | ㅅ | + y-glide medial before a back/low vowel (see below) |
| `x` | ㅎ | guttural → /h/ |
| `ħ` | ㅎ | pharyngeal → /h/ |
| `h` | ㅎ | |
| `m` | ㅁ | |
| `n` | ㄴ | |
| `l` | ㄹ | |
| `r` | ㄹ | merges with `l` |

### Emphatics (consonant + `ˤ`) → tense jamo (긴장음)

| IPA | Jamo | Note |
|-----|------|------|
| `tˤ` | ㄸ | tense; no jongseong slot → neutralizes to ㄷ as a coda |
| `sˤ` | ㅆ | tense |
| *any other* `Cˤ` | jamo(C) | emphasis dropped; rendered as the plain consonant's jamo |

The tense series approximates emphasis only; the Korean three-way laryngeal
contrast (plain / tense / aspirated) cannot encode Syriac voicing.

### Vowels (length collapsed) → jungseong (모음)

Vowel length is **collapsed**: a long vowel (`V` + `ː`) maps to the same medial as
its short counterpart.

| IPA | Jamo |
|-----|------|
| `a`, `ɑ` (and `aː`, `ɑː`) | ㅏ |
| `e` (and `eː`) | ㅔ |
| `i` (and `iː`) | ㅣ |
| `o` (and `oː`) | ㅗ |
| `u` (and `uː`) | ㅜ |
| *epenthetic* | ㅡ (inserted by the syllabifier; see below) |

### Glides + vowel → compound medial (이중모음)

A glide (`w`, `j`) plus its following vowel collapses into a single compound
*jungseong*.

| IPA glide+vowel | Compound medial |
|-----------------|------|
| `j` + `a` / `ɑ` | ㅑ |
| `j` + `e` | ㅖ |
| `j` + `o` | ㅛ |
| `j` + `u` | ㅠ |
| `j` + `i` | ㅣ (homorganic — collapses to bare ㅣ) |
| `w` + `a` / `ɑ` | ㅘ |
| `w` + `e` | ㅞ |
| `w` + `i` | ㅟ |
| `w` + `o` | ㅝ |
| `w` + `u` | ㅜ (homorganic — collapses to bare ㅜ) |

A bare glide that is **not** followed by a mappable vowel falls back to its vowel
form so nothing is lost: `w` → ㅜ, `j` → ㅣ.

### `ʃ` y-glide rule (구개음 [ɕ] 살리기)

`ʃ` always maps to ㅅ. When it is an onset **directly before a back/low vowel**
(`a ɑ o u`), it additionally takes a y-glide *jungseong* so a Korean reader sounds
out the palatal `[ɕ]` ("sh") allophone rather than plain `[s]`:

| `ʃ` + vowel | Block | (vs. plain ㅅ) |
|-------------|-------|----------------|
| `ʃa` / `ʃɑ` | 샤 (ㅅ+ㅑ) | not 사 |
| `ʃo` | 쇼 (ㅅ+ㅛ) | not 소 |
| `ʃu` | 슈 (ㅅ+ㅠ) | not 수 |

`ʃi` (시) and `ʃe` (세) are already in the `[ɕ]` class and are left untouched.

### Dropped / silent (탈락)

| IPA | Name | Treatment |
|-----|------|-----------|
| `ʔ` | *alaph* | dropped (treated as a boundary) |
| `ʕ` | *ayin* | dropped (silent) |

## 2. Syllabification + Epenthesis / 음절화와 삽입모음

Korean syllable structure is `(C)(G)V(C)`: **no onset clusters** and a
**restricted coda set**. The mapped item stream (a sequence of consonant jamo and
nucleus medials) is packed into legal blocks as follows:

- **Silent onset.** A syllable that starts with a vowel uses the silent onset
  ㅇ (`ieung`) as its choseong.
- **No onset clusters.** When more consonants pile up before a nucleus than a
  single onset can hold, the surplus leading consonants each become their own
  `C + ㅡ` (epenthetic) syllable; the last one becomes the real onset.
- **One coda max.** Between two nuclei, the first surplus consonant codas the
  current syllable, any middle consonants get their own `C + ㅡ` syllables, and
  the last consonant becomes the next onset. At the end of a token, one consonant
  may coda; any extra get `C + ㅡ` syllables.
- **Coda neutralization.** The tense stops ㄸ / ㅃ / ㅉ have **no jongseong slot**,
  so as a coda they neutralize: ㄸ → ㄷ, ㅃ → ㅂ, ㅉ → ㅈ.
- **`/h/`-class coda diversion.** ㅎ (only ever produced by `x` / `ħ` / `h`) is
  never a real, audible Korean batchim — a final ㅎ block reads back in RR as a
  spurious `[t]`, deleting the `/h/`. So a ㅎ that would land in a coda slot is
  instead emitted as its own ㅎ+ㅡ (흐, *heu*) syllable, the standard Korean device
  for an audible foreign final `/h/` (cf. 바흐 "Bach"). This is why
  `hwɑːθ` → 홧 keeps a real coda but a stranded `/h/` surfaces as 흐.
- **No nuclei at all.** A token with no vowel becomes a run of `C + ㅡ` syllables.

The epenthetic vowel is always **ㅡ** (*eu*).

## 3. Composition Formula / 조합 공식

Each block is composed into a single precomposed Hangul code point:

```
syllable = 0xAC00 + (cho_index * 588) + (jung_index * 28) + jong_index
```

with the following authoritative index orders (jong index 0 = no batchim):

```
cho  (19): ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ
jung (21): ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ
jong (28): (none) ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄹ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅄ ㅅ ㅆ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ
```

---

# Romanized Reader Tier (RR Readback)

The Romanized tier is the **Revised-Romanization** readback of the generated
Hangul, computed by decomposing each precomposed block back to cho/jung/jong and
mapping each jamo to its RR letters. Because it is derived from the Hangul tier,
the two reader tiers are always mutually consistent. There is **no cross-syllable
sandhi**: each block is read in isolation.

### RR choseong (초성)

| Jamo | ㄱ | ㄲ | ㄴ | ㄷ | ㄸ | ㄹ | ㅁ | ㅂ | ㅃ | ㅅ | ㅆ | ㅇ | ㅈ | ㅉ | ㅊ | ㅋ | ㅌ | ㅍ | ㅎ |
|------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| RR | g | kk | n | d | tt | r | m | b | pp | s | ss | *(none)* | j | jj | ch | k | t | p | h |

### RR jungseong (중성)

| Jamo | ㅏ | ㅐ | ㅑ | ㅒ | ㅓ | ㅔ | ㅕ | ㅖ | ㅗ | ㅘ | ㅙ | ㅚ | ㅛ | ㅜ | ㅝ | ㅞ | ㅟ | ㅠ | ㅡ | ㅢ | ㅣ |
|------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| RR | a | ae | ya | yae | eo | e | yeo | ye | o | wa | wae | oe | yo | u | wo | we | wi | yu | eu | ui | i |

### RR jongseong (종성, neutralized)

Every coda is **neutralized** to its single released consonant (this is correct
RR, not a defect):

| Coda jamo | RR |
|-----------|----|
| ㄱ / ㄲ / ㅋ | k |
| ㄴ | n |
| ㄷ / ㅅ / ㅆ / ㅈ / ㅊ / ㅌ / ㅎ | t |
| ㄹ | l |
| ㅁ | m |
| ㅂ / ㅍ | p |
| ㅇ | ng |

(The syllabifier only ever composes a single neutralized coda, so cluster-coda
slots such as ㄳ/ㄵ/ㄺ are unreachable; they are kept consistent with the same
neutralization rule for any external block fed through the readback.)

**No-sandhi note:** real spoken Korean applies cross-syllable assimilation (e.g. a
final ㅎ before a vowel, or ㄴ+ㄹ → ㄹㄹ). The Romanized tier deliberately does
**not** model this — it is a faithful per-block readback of the Hangul, so a final
ㅎ reads back as `t` and a final ㄹ as `l` regardless of what follows.

---

# Documented Limitations / 문서화된 한계

The Hangul and Romanized tiers are **reader aids**, not reversible scholarly
transcriptions. Korean lacks several Aramaic phonemes and forbids several Aramaic
syllable shapes, so the following information is intentionally approximated or
lost. **Use the Scholarly tier when precision matters.**

- **Forced epenthesis.** Korean syllables are `(C)(G)V(C)` with no onset clusters
  and a restricted coda set, so an epenthetic **ㅡ** is inserted to break up Syriac
  clusters and codas. This **adds vowels that are not in the Syriac**.
- **Lost `/f v θ ð z/` distinctions.** `f` → ㅍ (like `p`), `v` → ㅂ (like `b`),
  `θ` → ㅅ (like `s`), `ð` → ㄷ (like `d`), `z` → ㅈ. These contrasts disappear.
- **l / r merger.** Both `l` and `r` map to a single **ㄹ**; they are not
  distinguished.
- **No voicing encoding.** The Korean three-way laryngeal contrast (plain / tense /
  aspirated) cannot encode Syriac voicing; emphatics are approximated with tense
  jamo and the voiced/voiceless contrast is not recoverable.
- **Approximated gutturals and emphatics.** `x` / `ħ` / `h` all collapse to ㅎ;
  `q` → ㅋ (like `k`); soft `ɣ` → ㄱ (like `ɡ`); `ʔ` (*alaph*) and `ʕ` (*ayin*) are
  dropped entirely. The pharyngeal place of articulation is not represented.
- **Glide + homorganic vowel collapse.** `ji` → ㅣ and `wu` → ㅜ, because Korean
  has no distinct *yi* / *wu* medial.
- **RR coda neutralization.** Revised-Romanization neutralizes every coda — e.g. a
  final ㅎ reads back as `t`, and ㅅ/ㅆ/ㅈ/ㅊ/ㅌ codas also read `t`. (This is
  correct RR, but means the underlying jamo is not recoverable from the RR.)
- **No cross-syllable sandhi.** The Romanized tier is a per-syllable readback only;
  spoken-Korean assimilation is not applied.
- **Not reversible.** The Hangul and Romanized tiers cannot be inverted back to the
  original IPA.

All of these distinctions are fully preserved in the **Scholarly** tier (and most
in **Pretty**), which is why those two tiers remain language-neutral.

---

# Worked Example / 예시

Six verses, shown in source IPA followed by all four tiers. These values come
straight from the converter (they are the embedded gold cases used by
`--selftest`), so they are guaranteed to match the shipped tool exactly.

### John 1:1

```
IPA        breːʃiːθ ʔiːθawj wɑː melθɑː whuː melθɑː ʔiːθawj wɑː lwɑːθ ʔɑːlɑːhɑː waʔlɑːhɑː ʔiːθawj wɑː huː melθɑː
Scholarly  brēšīṯ ʾīṯawy wā melṯā whū melṯā ʾīṯawy wā lwāṯ ʾālāhā waʾlāhā ʾīṯawy wā hū melṯā
Pretty     brēshīth īthawy wā melthā whū melthā īthawy wā lwāth ālāhā wa'lāhā īthawy wā hū melthā
Hangul     브레싯 이사우이 와 멜사 우후 멜사 이사우이 와 뢋 아라하 와라하 이사우이 와 후 멜사
Romanized  beuresit isaui wa melsa uhu melsa isaui wa rwat araha waraha isaui wa hu melsa
```

### John 1:2

```
IPA        hɑːnɑː ʔiːθawj wɑː breːʃiːθ lwɑːθ ʔɑːlɑːhɑː
Scholarly  hānā ʾīṯawy wā brēšīṯ lwāṯ ʾālāhā
Pretty     hānā īthawy wā brēshīth lwāth ālāhā
Hangul     하나 이사우이 와 브레싯 뢋 아라하
Romanized  hana isaui wa beuresit rwat araha
```

### John 1:3

```
IPA        kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː
Scholarly  kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā
Pretty     kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā
Hangul     쿨 비이데흐 화 우베라다우이 앞라 흐다 홧 메뎀 다화
Romanized  kul biideheu hwa uberadaui apra heuda hwat medem dahwa
```

### Matthew 1:1

```
IPA        kθɑːvɑː diːliːðuːθeh djeʃuːʕ mʃiːħɑː breh dðawiːð breh dʔavrɑːhɑːm
Scholarly  kṯāḇā dīlīḏūṯeh dyešūʿ mšīḥā breh dḏawīḏ breh dʾaḇrāhām
Pretty     kthāvā dīlīdhūtheh dyeshūʿ mshīḥā breh ddhawīdh breh d'avrāhām
Hangul     크사바 디리두세흐 뎨슈 므시하 브레흐 드다윋 브레흐 답라함
Romanized  keusaba diriduseheu dyesyu meusiha beureheu deudawit beureheu dapraham
```

### Romans 1:1

```
IPA        pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː
Scholarly  pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā
Pretty     pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā
Hangul     파우라웃 압다 뎨슈 므시하 카랴 왓리하 뎃프렛 레완게리이야운 다라하
Romanized  pauraut apda dyesyu meusiha karya watriha detpeuret rewangeriiyaun daraha
```

### Matthew 27:16 (Barabbas)

```
IPA        dmeθqre bar-ʔaba lvar-ʔaba lvar-ʔava
Scholarly  dmeṯqre bar-ʾaba lḇar-ʾaba lḇar-ʾaḇa
Pretty     dmethqre bar-'aba lvar-'aba lvar-'ava
Hangul     드멧크레 발-아바 르발-아바 르발-아바
Romanized  deumetkeure bal-aba reubal-aba reubal-aba
```

Notes you can trace through these examples:

- **Epenthesis.** `breːʃiːθ` → 브레싯 / `beuresit`: the onset cluster `br-` is
  broken with ㅡ (브) and the final `θ`/ㅅ codas the last syllable.
- **`ʃ` y-glide.** `djeʃuːʕ` → 뎨슈 / `dyesyu`: `ʃu` surfaces as 슈 (the `[ɕ]`
  allophone), and *ayin* drops.
- **`/h/` coda diversion.** `breh` → 브레흐 / `beureheu`: the stranded `/h/`
  becomes its own 흐 syllable rather than a silent batchim.
- **l/r merger and dropped gutturals.** `ʕavdɑː` → 압다 / `apda`: *ayin* drops,
  `v` reads as ㅂ, and the coda neutralizes.

---

# Folder Layout / 폴더 구조

Everything lives under the repository path `Korean/Peshita_Korean/`
(relative to the repo root):

```
Korean/Peshita_Korean/
├── TRANSLITERATION_SCHEME.md          # this document
├── transliterate_ko.py                # the deterministic converter (authoritative)
├── transliteration_mapping_ko.json    # machine-readable mirror of the mapping tables
├── Scholarly/                         # tier 1 output (language-neutral)
│   ├── Matthew-Matityahu/
│   │   ├── matthewmatityahu1_scholarly.txt
│   │   ├── matthewmatityahu2_scholarly.txt
│   │   └── ...
│   ├── 1stCorinthians/
│   └── ...                            # 27 book folders
├── Pretty/                            # tier 2 output (same tree, *_pretty.txt)
│   └── ...
├── Hangul/                            # tier 3 output (same tree, *_hangul.txt)
│   └── ...
└── Romanized/                         # tier 4 output (same tree, *_romanized.txt)
    └── ...
```

Each tier directory (`Scholarly/`, `Pretty/`, `Hangul/`, `Romanized/`) mirrors the
book/chapter structure of `IPA/Peshitta/`. For every source file
`IPA/Peshitta/<Book>/<name>_ipa.txt` the build produces one file per tier at
`Korean/Peshita_Korean/<Tier>/<Book>/<name>_<tier>.txt`. Each output line keeps
its `<verse#>\t` prefix verbatim; only the verse text after the first tab is
transliterated.

The current corpus is **260 IPA source files** across **27 books**, yielding
**1040 transliterated files** (260 × 4 tiers).

---

# Reproducing / 재현

The whole corpus can be regenerated from scratch with one command, run from this
folder:

```sh
python3 transliterate_ko.py --build
```

This walks every `*_ipa.txt` under `IPA/Peshitta/`, transliterates each into all
four tiers, and writes the `Scholarly/`, `Pretty/`, `Hangul/`, and `Romanized/`
trees described above. It reports the number of files written and any unmapped
characters (there should be none). The converter resolves the repository root from
its own location, so it runs correctly from this shipped folder.

Other useful entry points:

```sh
python3 transliterate_ko.py --selftest        # run the embedded gold cases (all 4 tiers)
python3 transliterate_ko.py --coverage        # scan the corpus for characters not in the mapping
python3 transliterate_ko.py --write-mapping   # (re)write transliteration_mapping_ko.json from the authoritative tables
```

`transliterate_ko.py` is authoritative: `transliteration_mapping_ko.json` is a
machine-readable mirror of its hard-coded tables, regenerated by `--write-mapping`.
The **Scholarly** and **Pretty** tiers reuse the English transducer's logic
verbatim, so their output matches `English/Peshita_English` character for
character.

---

*Prepared and signed by **Shin**.*
