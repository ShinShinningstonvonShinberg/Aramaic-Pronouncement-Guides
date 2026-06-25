# Peshitta Japanese Transliteration Scheme (日本語)

## Overview / 概要

This folder contains a **5-tier transliteration of the Peshitta**, aimed at
**Japanese-speaking readers**, generated **deterministically** from the project's
IPA pronunciation guides (`IPA/Peshitta/**/<name>_ipa.txt`).

Every output character is produced by a single, rule-based converter
(`transliterate_ja.py`). There is no hand-editing and no machine-learning step:
the same IPA input always yields exactly the same output. The IPA guides are the
single source of truth; the five tiers are mechanical re-encodings of that
phonetic data for different audiences.

The two scholarly tiers operate on the **phonetic** representation only. They
split text on ASCII spaces (preserving them verbatim), segment each token using a
longest-match rule, and render each segment through a tier table. The three
Japanese **reader** tiers (Katakana, Hiragana, Romaji) go a step further: they
re-parse the phonetic stream into legal Japanese **mora** (sound-units),
inserting forced epenthetic vowels where Japanese phonotactics forbid a consonant
cluster or coda, and then render that single mora parse three ways. Katakana —
the idiomatic script for foreign words — is the **primary** reader tier; Hiragana
gives the same mora in native glyphs; Romaji is a Hepburn-style readback of the
same mora.

Any character not covered by the tables is passed through unchanged and reported,
so the corpus can never silently lose information.

## The Five Tiers / 五つの段階

| Tier | Audience | Philosophy |
|------|----------|------------|
| **Scholarly** | Semiticists, students of Syriac/Aramaic, anyone comparing against academic editions | **Language-neutral.** Maximum fidelity. Uses the standard scholarly diacritics (macrons for long vowels; underlined/dotted letters for spirantized and emphatic consonants; `ʾ` for *alaph* and `ʿ` for *ayin*). Nothing is collapsed or dropped — every phonemic distinction in the IPA is preserved. **Byte-for-byte identical to the English Peshitta's Scholarly tier.** |
| **Pretty** | General readers who want accuracy and the look of the original | **Language-neutral.** A readable middle ground. Long vowels keep their macrons, but spirantized consonants use familiar digraphs (`sh`, `th`, `dh`, `kh`, `gh`, `v`) instead of underlined letters. The pharyngeal `ʿ` (*ayin*) is kept; *alaph* is dropped word-initially and written `'` elsewhere. **Byte-for-byte identical to the English Peshitta's Pretty tier.** |
| **Katakana** | First-time Japanese readers reading aloud in カタカナ | **Idiomatic foreign-word script (the primary reader tier).** The Aramaic phonetics are mapped to Japanese mora and rendered in katakana, the script Japanese natively uses for loanwords and foreign names. Long vowels use the chōonpu (ー). A reader applying ordinary katakana letter-to-sound rules lands roughly on the right pronunciation. Japanese phonotactics are obeyed: no consonant clusters, no codas except the moraic nasal ン, with forced epenthetic vowels inserted where needed. |
| **Hiragana** | Readers who want the same reading in ひらがな native glyphs | **Same mora parse, native glyphs.** Identical sound-units to the Katakana tier, written in hiragana. Long vowels are spelled by **doubling the vowel** (あ い う え お). Hiragana for foreign text is *unidiomatic* (katakana is the natural loanword script), but this tier was explicitly requested as a same-mora native-glyph readback. |
| **Romaji** | Readers who want the Japanese reading in the Latin alphabet | **Hepburn readback** of the same mora parse, mora by mora (`shi`/`chi`/`tsu`/`fu`/`ji` style, macron long vowels `ā ī ū ē ō`). Derived from the identical mora parse as Katakana/Hiragana, so all three reader tiers are mutually consistent. The tier is held to a strict charset (ASCII letters, the macron vowels `ā ī ū ē ō`, space, hyphen, digit, tab), so the standard Hepburn apostrophe after a moraic nasal is **not** emitted: メンイ is written `meni`, not `men'i`. The ン / ん boundary is still visible in the Katakana/Hiragana tiers. |

Because **Scholarly** and **Pretty** are language-neutral, they are produced by
the exact same logic as the English Peshitta and their output matches it character
for character. If you need those two tiers, the canonical reference is
`English/Peshita_English/TRANSLITERATION_SCHEME.md`; the **Katakana**,
**Hiragana**, and **Romaji** reader tiers are unique to this folder, so the
mapping tables below document them in full.

## Segmentation / 分節

All five tiers start from the same longest-match segmentation:

- Split on the ASCII space `" "` only; spaces are preserved verbatim.
- Within each token, left-to-right longest match:
  1. consonant + `ˤ` (U+02E4) → emphatic segment (2 chars)
  2. vowel (`a ɑ e i o u`) + `ː` (U+02D0) → long-vowel segment (2 chars)
  3. otherwise a single character
- For the reader tiers, an internal hyphen `-` splits a token into mora
  word-pieces (the hyphen is preserved in the output), so `bar-ʔaba` renders as
  two pieces joined by `-`.
- **Word-initial** = the first segment of a token (used only by the *alaph* rule
  in the scholarly/pretty tiers).

---

# Kana Reader Tiers (Katakana | Hiragana | Romaji)

Japanese is strictly **moraic**. A mora is one of:

- `(C)(j)V` — an optionally consonant-, optionally glide-onset, plus a vowel
- the **moraic nasal** ン / ん
- the **sokuon** ッ (geminating pause — not produced here)
- a **long-vowel part** (chōonpu ー / a doubled vowel / a macron)

There are **no consonant clusters** and **no codas** other than the moraic nasal.
Syriac, by contrast, has clusters, codas, gutturals, and emphatics. Rendering it
into Japanese therefore requires **forced vowel epenthesis**. The reader tiers
build a single mora parse and then render it three ways.

## 1. Algorithm

1. **MAP each IPA segment to a mora.**
   - consonant + vowel → the CV kana (e.g. `/ka/` → カ)
   - vowel alone → a vowel kana (e.g. `/a/` → ア)
   - on-glide `/j/` or `/w/` + vowel → y-row / w-row kana (or a yōon)
   - `/ʔ/` (*alaph*) and `/ʕ/` (*ayin*) are **dropped**.
   - a standalone glide with no mappable following vowel falls back to its vowel:
     `/j/` → イ (`i`), `/w/` → ウ (`u`).

2. **EPENTHESIZE.** A consonant with no following vowel is given an epenthetic
   vowel, forming a CV mora. The default epenthetic vowel is `/u/` (ク, ス, …),
   but it is `/o/` after `t` and `d` (ト, ド), and `ʃ` becomes シュ (the sh-row
   `u` cell). A **coda** `/n/` — one immediately preceded by a vowel-bearing mora
   — becomes the moraic nasal ン (not ヌ). An **onset** `/n/` with no preceding
   vowel (word- or cluster-initial, e.g. the imperfect prefix *n-* in `/nquːm/`)
   is **not** ン — a Japanese mora may never *begin* with ン — so it epenthesizes
   to ヌ / `nu` like any other onset consonant.

3. **LONG VOWELS** (`Vː`):
   - Katakana → append the chōonpu ー
   - Hiragana → double the vowel (あ い う え お)
   - Romaji → a macron (ā ī ū ē ō)

4. **Render the SAME mora parse three ways:** Katakana (primary), Hiragana (same
   mora, native glyphs), Romaji (Hepburn readback). The Romaji tier is held to a
   strict charset (ASCII letters, the macron vowels `ā ī ū ē ō`, space, hyphen,
   digit, tab). Standard Hepburn would insert an apostrophe after the moraic
   nasal `n` before a vowel- or y-initial syllable (メンイ → `men'i`); because
   `U+0027` is outside that charset, this build does **not** emit it — メンイ is
   written `meni`. The ン / ん boundary remains visible in the Katakana/Hiragana
   tiers, so the distinction is not lost from the build as a whole.

## 2. IPA → kana category / 子音の対応

Each IPA consonant maps to a **kana category** (a row of the mora table). These
reflect the **finalized** `CAT` / `EMPH_CAT` / `THETA_CAT` tables hard-coded in
`transliterate_ja.py`.

### Plain consonants

| IPA | Category | Note |
|-----|----------|------|
| `b` | b (バ行) | |
| `v` | v (ヴ row) | |
| `p` | p (パ行) | |
| `f` | f (ファ row) | |
| `t` | t (タ ティ トゥ テ ト) | |
| `d` | d (ダ ディ ドゥ デ ド) | |
| `ð` | z (ザ行) | merges with `z` |
| `k` | k (カ行) | |
| `ɡ` | g (ガ行) | |
| `ɣ` | g (ガ行) | merges with `ɡ` |
| `q` | k (カ行) | merges with `k` |
| `s` | s (サ行) | |
| `z` | z (ザ行) | |
| `θ` | s (サ行) | merges with `s` (via `THETA_CAT`) |
| `ʃ` | sh (シャ シ シュ シェ ショ) | |
| `x` | h (ハ行) | guttural → ハ row |
| `ħ` | h (ハ行) | pharyngeal → ハ row |
| `h` | h (ハ行) | |
| `m` | m (マ行) | |
| `n` | n (ナ行; coda → ン) | see epenthesis rules |
| `l` | r (ラ行) | merges with `r` |
| `r` | r (ラ行) | |
| `w` | w (ワ row, onset glide) | |
| `j` | y (ヤ row, onset glide) | |

### Emphatics (consonant + `ˤ`) → plain category

| IPA | Category | Note |
|-----|----------|------|
| `tˤ` | t | emphasis lost (`EMPH_CAT`) |
| `sˤ` | s | emphasis lost (`EMPH_CAT`) |
| *any other* `Cˤ` | category(C) | emphasis dropped; rendered as the plain consonant |

### Glottal / pharyngeal (dropped)

| IPA | Name | Treatment |
|-----|------|-----------|
| `ʔ` | *alaph* | dropped |
| `ʕ` | *ayin* | dropped |

## 3. The mora table / モーラ表

Each category row gives the five `a i u e o` cells as **(katakana, hiragana,
romaji)**. This is the finalized `KANA` table in `transliterate_ja.py`. The empty
category `""` is the bare-vowel / glide-fallback row.

| Cat | a | i | u | e | o |
|-----|---|---|---|---|---|
| *(vowel)* `""` | ア / あ / a | イ / い / i | ウ / う / u | エ / え / e | オ / お / o |
| `k` | カ / か / ka | キ / き / ki | ク / く / ku | ケ / け / ke | コ / こ / ko |
| `g` | ガ / が / ga | ギ / ぎ / gi | グ / ぐ / gu | ゲ / げ / ge | ゴ / ご / go |
| `s` | サ / さ / sa | シ / し / shi | ス / す / su | セ / せ / se | ソ / そ / so |
| `z` | ザ / ざ / za | ジ / じ / ji | ズ / ず / zu | ゼ / ぜ / ze | ゾ / ぞ / zo |
| `sh` | シャ / しゃ / sha | シ / し / shi | シュ / しゅ / shu | シェ / しぇ / she | ショ / しょ / sho |
| `t` | タ / た / ta | ティ / てぃ / ti | トゥ / とぅ / tu | テ / て / te | ト / と / to |
| `d` | ダ / だ / da | ディ / でぃ / di | ドゥ / どぅ / du | デ / で / de | ド / ど / do |
| `n` | ナ / な / na | ニ / に / ni | ヌ / ぬ / nu | ネ / ね / ne | ノ / の / no |
| `h` | ハ / は / ha | ヒ / ひ / hi | フ / ふ / fu | ヘ / へ / he | ホ / ほ / ho |
| `f` | ファ / ふぁ / fa | フィ / ふぃ / fi | フ / ふ / fu | フェ / ふぇ / fe | フォ / ふぉ / fo |
| `b` | バ / ば / ba | ビ / び / bi | ブ / ぶ / bu | ベ / べ / be | ボ / ぼ / bo |
| `p` | パ / ぱ / pa | ピ / ぴ / pi | プ / ぷ / pu | ペ / ぺ / pe | ポ / ぽ / po |
| `m` | マ / ま / ma | ミ / み / mi | ム / む / mu | メ / め / me | モ / も / mo |
| `v` | ヴァ / ゔぁ / va | ヴィ / ゔぃ / vi | ヴ / ゔ / vu | ヴェ / ゔぇ / ve | ヴォ / ゔぉ / vo |
| `r` | ラ / ら / ra | リ / り / ri | ル / る / ru | レ / れ / re | ロ / ろ / ro |
| `y` (glide) | ヤ / や / ya | イ / い / i | ユ / ゆ / yu | イェ / いぇ / ye | ヨ / よ / yo |
| `w` (glide) | ワ / わ / wa | ウィ / うぃ / wi | ウ / う / u | ウェ / うぇ / we | ウォ / うぉ / wo |

Notes embedded in the table:

- **Glide + homorganic vowel collapse.** `j` + `i` → イ / い / `i` (no distinct
  *yi*); `w` + `u` → ウ / う / `u` (no distinct *wu*).
- **`ʃ` yōon.** `ʃa` → シャ, `ʃu` → シュ, `ʃe` → シェ, `ʃo` → ショ, `ʃi` → シ —
  so the palatal `[ɕ]` ("sh") allophone is heard, not a plain `s`.
- **`f`/`t`/`d`/`v` rows** use small-kana digraphs (ファ, ティ, トゥ, ヴァ …) so the
  foreign sounds survive as far as katakana allows.

## 4. Vowels, glides, and long-vowel handling

- **Vowel base** (`VOWBASE`): `a`, `ɑ` → `a`; `e` → `e`; `i` → `i`; `o` → `o`;
  `u` → `u`. (`a` and `ɑ` merge.)
- **Glide + vowel** uses the y-row / w-row of the mora table above (or a yōon
  cell). A glide that is **not** followed by a mappable vowel falls back to its
  vowel form: `j` → イ / い / `i`, `w` → ウ / う / `u`.
- **Epenthetic vowel** (`EPV`): default `/u/`; `/o/` after `t` and `d`; `ʃ` →
  シュ (the sh-row `u` cell). A coda `/n/` (preceded by a vowel) → ン; an onset
  `/n/` with no preceding vowel → ヌ / `nu`.
- **Long vowels** (`Vː`): Katakana appends ー (`CHOONPU`); Hiragana doubles the
  vowel via `HIRA_LONG` (あ い う え お); Romaji uses a macron via `MACRON`
  (ā ī ū ē ō).

---

# Documented Limitations / 文書化された限界

The Katakana, Hiragana, and Romaji tiers are **reader aids**, not reversible
scholarly transcriptions. Japanese lacks several Aramaic phonemes and forbids
several Aramaic syllable shapes, so the following information is intentionally
approximated or lost. **Use the Scholarly tier when precision matters.**

- **Forced epenthesis inflates length.** Japanese mora are `(C)(j)V` plus the
  moraic nasal — no clusters, no other codas — so an epenthetic vowel (default
  `/u/`, `/o/` after `t`/`d`, `ʃ` → シュ) is inserted to break every Syriac
  cluster and coda. This **adds vowels that are not in the Syriac**, and the kana
  is markedly longer than the source.
- **Lost `/f v θ ð z ʃ/` distinctions (full mergers).** `θ`, `s`, and `sˤ` all
  collapse to the **サ row**, and `ð` and `z` both collapse to the **ザ row**.
  This is a true *merger*, not a near-miss: `melθɑː` and a hypothetical `melsɑː`
  become identical kana (メルサー), and likewise `ð` and `z`. (`f` and `v` survive
  via ファ / ヴ small-kana digraphs, but only as far as katakana allows.)
- **l / r merger.** Both `l` and `r` map to the single **ラ行** (Japanese has one
  liquid); they are not distinguished.
- **Approximated gutturals / emphatics / glottals.** `x`, `ħ`, and `h` all
  collapse to the **ハ row**; `q` → カ行 (like `k`); soft `ɣ` → ガ行 (like `ɡ`);
  emphasis (`ˤ`) is lost; `ʔ` (*alaph*) and `ʕ` (*ayin*) are dropped entirely.
  Pharyngeal place of articulation is not represented.
- **No pitch accent or fine vowel quality.** Japanese pitch accent is not
  encoded, and `a` and `ɑ` merge to a single ア.
- **Moraic-nasal asymmetry.** A coda `/n/` becomes ン, but an onset `/n/` with no
  preceding vowel becomes ヌ / `nu`, because a Japanese mora may never begin with
  ン. (Romaji does **not** emit the standard Hepburn apostrophe after a moraic
  `n` before a vowel- or y-initial syllable — メンイ → `meni`, not `men'i` —
  because `U+0027` is outside the Romaji charset; the ン / ん boundary stays
  visible in the Katakana/Hiragana tiers.)
- **Hiragana for foreign text is unidiomatic.** Katakana is the natural loanword
  script; the Hiragana tier exists only because it was requested, as a same-mora
  native-glyph readback.
- **Not reversible.** The kana tiers cannot be inverted back to the original IPA.

All of these distinctions are fully preserved in the **Scholarly** tier (and most
in **Pretty**), which is why those two tiers remain language-neutral.

---

# Worked Example / 例示

Six verses, shown in source IPA followed by all five tiers. These values come
straight from the converter (they are the embedded gold cases used by
`--selftest`), so they are guaranteed to match the shipped tool exactly.

### John 1:1

```
IPA        breːʃiːθ ʔiːθawj wɑː melθɑː whuː melθɑː ʔiːθawj wɑː lwɑːθ ʔɑːlɑːhɑː waʔlɑːhɑː ʔiːθawj wɑː huː melθɑː
Scholarly  brēšīṯ ʾīṯawy wā melṯā whū melṯā ʾīṯawy wā lwāṯ ʾālāhā waʾlāhā ʾīṯawy wā hū melṯā
Pretty     brēshīth īthawy wā melthā whū melthā īthawy wā lwāth ālāhā wa'lāhā īthawy wā hū melthā
Katakana   ブレーシース イーサウイ ワー メルサー ウフー メルサー イーサウイ ワー ルワース アーラーハー ワラーハー イーサウイ ワー フー メルサー
Hiragana   ぶれえしいす いいさうい わあ めるさあ うふう めるさあ いいさうい わあ るわあす ああらあはあ わらあはあ いいさうい わあ ふう めるさあ
Romaji     burēshīsu īsaui wā merusā ufū merusā īsaui wā ruwāsu ārāhā warāhā īsaui wā fū merusā
```

### John 1:2

```
IPA        hɑːnɑː ʔiːθawj wɑː breːʃiːθ lwɑːθ ʔɑːlɑːhɑː
Scholarly  hānā ʾīṯawy wā brēšīṯ lwāṯ ʾālāhā
Pretty     hānā īthawy wā brēshīth lwāth ālāhā
Katakana   ハーナー イーサウイ ワー ブレーシース ルワース アーラーハー
Hiragana   はあなあ いいさうい わあ ぶれえしいす るわあす ああらあはあ
Romaji     hānā īsaui wā burēshīsu ruwāsu ārāhā
```

### John 1:3

```
IPA        kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː
Scholarly  kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā
Pretty     kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā
Katakana   クル ブイイゼフ フワー ウヴェルアーザウイ アーフラー フザー フワース メデム ダフワー
Hiragana   くる ぶいいぜふ ふわあ うゔぇるああざうい ああふらあ ふざあ ふわあす めでむ だふわあ
Romaji     kuru buiizefu fuwā uveruāzaui āfurā fuzā fuwāsu medemu dafuwā
```

### Matthew 1:1

```
IPA        kθɑːvɑː diːliːðuːθeh djeʃuːʕ mʃiːħɑː breh dðawiːð breh dʔavrɑːhɑːm
Scholarly  kṯāḇā dīlīḏūṯeh dyešūʿ mšīḥā breh dḏawīḏ breh dʾaḇrāhām
Pretty     kthāvā dīlīdhūtheh dyeshūʿ mshīḥā breh ddhawīdh breh d'avrāhām
Katakana   クサーヴァー ディーリーズーセフ ドイェシュー ムシーハー ブレフ ドザウィーズ ブレフ ドアヴラーハーム
Hiragana   くさあゔぁあ でぃいりいずうせふ どいぇしゅう むしいはあ ぶれふ どざうぃいず ぶれふ どあゔらあはあむ
Romaji     kusāvā dīrīzūsefu doyeshū mushīhā burefu dozawīzu burefu doavurāhāmu
```

### Romans 1:1

```
IPA        pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː
Scholarly  pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā
Pretty     pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā
Katakana   パウラーウス アヴダー ドイェシュー ムシーハー カルヤー ワシュリーハー ドエスプレシュ レワンゲリイヤーウン ドアーラーハー
Hiragana   ぱうらあうす あゔだあ どいぇしゅう むしいはあ かるやあ わしゅりいはあ どえすぷれしゅ れわんげりいやあうん どああらあはあ
Romaji     paurāusu avudā doyeshū mushīhā karuyā washurīhā doesupureshu rewangeriiyāun doārāhā
```

### Matthew 27:16 (Barabbas)

```
IPA        dmeθqre bar-ʔaba lvar-ʔaba lvar-ʔava
Scholarly  dmeṯqre bar-ʾaba lḇar-ʾaba lḇar-ʾaḇa
Pretty     dmethqre bar-'aba lvar-'aba lvar-'ava
Katakana   ドメスクレ バル-アバ ルヴァル-アバ ルヴァル-アヴァ
Hiragana   どめすくれ ばる-あば るゔぁる-あば るゔぁる-あゔぁ
Romaji     domesukure baru-aba ruvaru-aba ruvaru-ava
```

Notes you can trace through these examples:

- **Forced epenthesis.** `breːʃiːθ` → ブレーシース / `burēshīsu`: the onset cluster
  `br-` grows ブ (`bu`), and the final `θ` (サ row) grows ス (`su`).
- **`ʃ` yōon.** `djeʃuːʕ` → ドイェシュー / `doyeshū`: `ʃu` surfaces as シュ (the
  `[ɕ]` allophone), the onset `d` epenthesizes to ド (`do`), and *ayin* drops.
- **θ/s and ð/z mergers.** `melθɑː` → メルサー / `merusā`: `θ` reads as サ row;
  `wvelʕɑːðawj` → ウヴェルアーザウイ: `ð` reads as ザ row.
- **l/r merger and dropped gutturals.** `ʕavdɑː` → アヴダー / `avudā`: *ayin*
  drops, `v` survives as ヴ, and the coda `d` grows ド.
- **Long vowels per tier.** `wɑː` → ワー (chōonpu) / わあ (doubled) / `wā`
  (macron).

---

# Folder Layout / フォルダ構成

Everything lives under the repository path `Japanese/Peshita_Japanese/`
(relative to the repo root):

```
Japanese/Peshita_Japanese/
├── TRANSLITERATION_SCHEME.md          # this document
├── transliterate_ja.py                # the deterministic converter (authoritative)
├── transliteration_mapping_ja.json    # machine-readable mirror of the mapping tables
├── Scholarly/                         # tier 1 output (language-neutral)
│   ├── Matthew-Matityahu/
│   │   ├── matthewmatityahu1_scholarly.txt
│   │   ├── matthewmatityahu2_scholarly.txt
│   │   └── ...
│   ├── 1stCorinthians/
│   └── ...                            # 27 book folders
├── Pretty/                            # tier 2 output (same tree, *_pretty.txt)
│   └── ...
├── Katakana/                          # tier 3 output (same tree, *_katakana.txt)
│   └── ...
├── Hiragana/                          # tier 4 output (same tree, *_hiragana.txt)
│   └── ...
└── Romaji/                            # tier 5 output (same tree, *_romaji.txt)
    └── ...
```

Each tier directory (`Scholarly/`, `Pretty/`, `Katakana/`, `Hiragana/`,
`Romaji/`) mirrors the book/chapter structure of `IPA/Peshitta/`. For every source
file `IPA/Peshitta/<Book>/<name>_ipa.txt` the build produces one file per tier at
`Japanese/Peshita_Japanese/<Tier>/<Book>/<name>_<tier>.txt`. Each output line
keeps its `<verse#>\t` prefix verbatim; only the verse text after the first tab is
transliterated.

The current corpus is **260 IPA source files** across **27 books**, yielding
**1300 transliterated files** (260 × 5 tiers).

---

# Reproducing / 再現

The whole corpus can be regenerated from scratch with one command, run from this
folder:

```sh
python3 transliterate_ja.py --build
```

This walks every `*_ipa.txt` under `IPA/Peshitta/`, transliterates each into all
five tiers, and writes the `Scholarly/`, `Pretty/`, `Katakana/`, `Hiragana/`, and
`Romaji/` trees described above. It reports the number of files written and any
unmapped characters (there should be none). The converter resolves the repository
root from its own location, so it runs correctly from this shipped folder.

Other useful entry points:

```sh
python3 transliterate_ja.py --selftest        # run the embedded gold cases (all 5 tiers)
python3 transliterate_ja.py --coverage        # scan the corpus for characters not in the mapping
python3 transliterate_ja.py --write-mapping   # (re)write transliteration_mapping_ja.json from the authoritative tables
```

`transliterate_ja.py` is authoritative: `transliteration_mapping_ja.json` is a
machine-readable mirror of its hard-coded tables, regenerated by
`--write-mapping`. The **Scholarly** and **Pretty** tiers reuse the English
transducer's logic verbatim, so their output matches `English/Peshita_English`
character for character.

---

*Prepared and signed by **Shin**.*
