# Peshitta Chinese Transliteration Scheme (中文)

## Overview / 概要

This folder contains a **6-tier transliteration of the Peshitta**, aimed at
**Chinese-speaking readers**, generated **deterministically** from the project's
IPA pronunciation guides (`IPA/Peshitta/**/<name>_ipa.txt`).

Every output character is produced by a single, rule-based converter
(`transliterate_zh.py`). There is no hand-editing and no machine-learning step:
the same IPA input always yields exactly the same output. The IPA guides are the
single source of truth; the six tiers are mechanical re-encodings of that
phonetic data for different audiences.

The two scholarly tiers operate on the **phonetic** representation only. They
split text on ASCII spaces (preserving them verbatim), segment each token using a
longest-match rule, and render each segment through a tier table. The four
Chinese **reader** tiers (Pinyin, Zhuyin, Hanzi-Simplified, Hanzi-Traditional)
go a step further: they re-parse the phonetic stream into legal **toneless
Mandarin syllables**, forcing epenthetic vowels wherever Mandarin phonotactics
forbid a consonant cluster or a non-nasal coda, and then render that single
syllable parse four ways.

Any character not covered by the tables is passed through and reported, so the
corpus can never silently lose information.

## The KEY INVERSION — Pinyin is the engine, Hanzi is a downstream artifact

Every other language in this project (Japanese kana, Korean Hangul) has a
**phonographic native script**: you can spell a foreign sound directly in the
native letters. **Chinese characters cannot do this.** Hanzi is *logographic* —
each glyph is a morpheme with a fixed sound *and a fixed meaning*. There is no
way to "spell" an arbitrary foreign syllable in Hanzi; you can only pick an
existing character whose citation reading is *near* the syllable you want.

So the architecture is **inverted** relative to kana/Hangul:

1. **Pinyin is the phonetic engine.** The IPA stream is approximated to a string
   of **legal toneless Mandarin syllables** by a phonotactic-repair transducer.
   Pinyin is the faithful, atonal spine of all four reader tiers.
2. **Zhuyin (Bopomofo) is a deterministic transcode of the Pinyin.** It spells
   exactly the same syllable inventory in the indigenous phonetic alphabet, one
   syllable to one Bopomofo cluster.
3. **Hanzi is a *downstream*, frozen, one-character-per-syllable lookup off the
   Pinyin syllable stream.** It consumes the syllables the Pinyin engine already
   produced and replaces each with a single neutral transcription character.
   Hanzi is **NON-faithful**: it imposes a citation tone the source never had and
   a meaning the source never had, and it cannot be read back to the original.

The practical consequence: **do not treat Hanzi as "the Hangul of Chinese."** It
is the *least* faithful tier in the whole project. The authoritative atonal
statement is the **Pinyin** tier; Hanzi exists only for the "native look" of
real Chinese text, clearly labeled sound-only.

## The Six Tiers / 六个段階

| Tier | Audience | Philosophy |
|------|----------|------------|
| **Scholarly** | Semiticists, students of Syriac/Aramaic, anyone comparing against academic editions | **Language-neutral.** Maximum fidelity. Standard scholarly diacritics (macrons for long vowels; underlined/dotted letters for spirantized and emphatic consonants; `ʾ` for *alaph* and `ʿ` for *ayin*). Nothing is collapsed or dropped. **Byte-for-byte identical to the English Peshitta's Scholarly tier.** |
| **Pretty** | General readers who want accuracy and the look of the original | **Language-neutral.** Long vowels keep their macrons; spirantized consonants use familiar digraphs (`sh`, `th`, `dh`, `kh`, `gh`, `v`). The pharyngeal `ʿ` (*ayin*) is kept; *alaph* is dropped word-initially and written `'` elsewhere. **Byte-for-byte identical to the English Peshitta's Pretty tier.** |
| **Pinyin** *(toneless)* | Mainland + Singapore readers, learners, anyone who wants the faithful sound | **The phonetic spine.** Each IPA segment maps to a (Mandarin initial, nucleus, optional `-n` coda) and is **snapped to a legal toneless Mandarin syllable**. Words are space-separated; syllables within a word are joined by a middot `·`; literal hyphens are preserved. **Tones are omitted** (the source is atonal). Every emitted syllable is in the legal Mandarin whitelist (hard invariant). |
| **Zhuyin** *(Bopomofo, toneless)* | Taiwan readers; the indigenous phonetic-script analog | **Same syllable parse, native phonetic glyphs.** A standard deterministic Pinyin↔Bopomofo transcode of the identical toneless syllable stream. Apical `-i` after the seven apical initials is the bare initial symbol; `y/w` zero-initial spellings restore the `i-/u-` medials. Tones omitted (so bare Zhuyin, conventionally tone-1, is read level here). |
| **Hanzi-Simplified** *(简体)* | Broad outreach: PRC mainland + Singapore (普通话 standard) | **Native look; NON-faithful.** A frozen one-character-per-syllable lookup off the Pinyin stream, drawn from the standard Xinhua 音译表 / 《世界人名翻译大辞典》 neutral transcription characters. One glyph per syllable, no inner separators. Each glyph imposes a citation tone and a meaning — an artifact, documented below. |
| **Hanzi-Traditional** *(繁體)* | Taiwan / HK recognizability (國語 standard) | **Same syllables, Traditional column.** The same frozen table authored as a dual `{simplified, traditional}` column; most characters are script-invariant, and the pairs that differ (热/熱 萨/薩 乌/烏 维/維 书/書 …) are authored directly. Same NON-faithful caveats as Simplified. |

Because **Scholarly** and **Pretty** are language-neutral, they are produced by
the exact same logic as the English Peshitta and their output matches it
character for character. If you need those two tiers, the canonical reference is
`English/Peshita_English/TRANSLITERATION_SCHEME.md`; the **Pinyin**, **Zhuyin**,
and two **Hanzi** reader tiers are unique to this folder, so the mapping tables
below document them in full.

This is one tier *fewer* than a naive parallel to Japanese's five-reader count
would suggest in one direction and *more* in another, by design: there is **no
tone-marked Pinyin tier**, because the source is atonal and any tone would be
fabricated; and there are **two** Hanzi tiers because Simplified and Traditional
are a genuine script split over the same spoken Mandarin.

## Segmentation / 分節

All six tiers start from the same longest-match segmentation:

- Split on the ASCII space `" "` only; spaces are preserved verbatim.
- Within each token, left-to-right longest match:
  1. consonant + `ˤ` (U+02E4) → emphatic segment (2 chars)
  2. vowel (`a ɑ e i o u`) + `ː` (U+02D0) → long-vowel segment (2 chars)
  3. otherwise a single character
- For the reader tiers, an internal hyphen `-` is preserved verbatim as a literal
  word seam, so `bar-ʔaba` renders as two syllable-runs joined by `-`.
- **Word-initial** = the first segment of a token (used only by the *alaph* rule
  in the Scholarly/Pretty tiers).

---

# The Pinyin Engine (the spine)

Mandarin is phonotactically tiny relative to Syriac. A legal Mandarin syllable is
`(initial)(medial)nucleus(coda)` where:

- there are **no consonant clusters**;
- the **only codas are `-n` and `-ng`**;
- the whole inventory is roughly **400 toneless syllables**.

Syriac, by contrast, has clusters, voiced/voiceless pairs, emphatics, a full
guttural/pharyngeal series, and codas of every kind. Rendering it into Mandarin
therefore requires **forced vowel epenthesis** and a chain of **mergers**. The
engine builds one toneless-syllable parse and then renders it four ways.

## 1. Algorithm

1. **MAP each IPA segment to a Mandarin onset and/or nucleus.**
   - A vowel becomes a zero-initial syllable nucleus (`a → a`, `i → yi`, `u → wu`,
     `e → e`, `o → o`). `a` and `ɑ` merge to `a`.
   - A consonant + following vowel becomes a CV syllable on the mapped onset.
   - On-glides `j` and `w` before a vowel take the `y-`/`w-` zero-initial
     spellings (`ja → ya`, `wa → wa`, …); a glide with no mappable following
     vowel falls back to its vowel (`j → yi`, `w → wu`).
   - `ʔ` (*alaph*) and `ʕ` (*ayin*) are **dropped**.

2. **SNAP to a legal toneless syllable.** The candidate `(initial, nucleus,
   coda)` is matched against the **legal whitelist** (403 syllables). If the exact
   syllable is illegal, the snapper relaxes — trying `-ng` for a stranded `-n`,
   then other nuclei, then dropping the coda — until it lands on a legal CV(N)
   syllable. **Every emitted Pinyin syllable is guaranteed to be a member of the
   whitelist** (a hard invariant, checked by `--coverage`, which reports zero
   illegal syllables across the corpus).

3. **EPENTHESIZE stranded consonants.** A consonant with no following vowel (a
   cluster member or a non-nasal coda) is given an epenthetic vowel to form a
   legal CV syllable:
   - default epenthetic vowel **`e`** (the neutral nucleus that collocates with
     the widest initial set), e.g. `br-` → `bo·re`, final `θ` → `si`/`se`;
   - apical **`i`** after the seven apical/retroflex initials `z c s zh ch sh r`
     (e.g. `s` stranded → `si`, `sh` stranded → `shi`).
   - The single survivable Syriac coda is a **non-pre-vocalic `-n`**, attached as
     a legal `-an/-en/-in/-un`; every other coda epenthesizes.

4. **PALATALIZE before `/i/`.** Mandarin forbids `gi/ki/hi`; before nucleus `i`
   the velars/`h` palatalize: `g → j`, `k → q`, `h → x` (so `g`+`i` → `ji`, etc.).

5. **One targeted artifact removal.** The syllable `fo` is legal but its only
   common character is 佛 ("Buddha" — religiously loaded). Because the `/f/` here
   is always stranded or an unfaithful `/f/+/o/` nucleus anyway, `_snap` routes
   `fo → fu` (legal; neutral → 福). No other syllable is affected, and `fo` is
   never produced.

6. **Render the SAME syllable parse four ways:** Pinyin (the spine), Zhuyin (a
   Bopomofo transcode), Hanzi-Simplified, Hanzi-Traditional.

## 2. IPA → Mandarin onset / 子音の対応

Each IPA consonant maps to a Mandarin **onset** (the `ONSET` table in
`transliterate_zh.py`). `None` means the onset is dropped.

### Plain consonants

| IPA | Onset | Note |
|-----|-------|------|
| `b` | b | |
| `p` | p | |
| `f` | f | |
| `v` | f | **merges with `f`** (Mandarin has no `v`) |
| `m` | m | |
| `w` | w | onset glide |
| `d` | d | |
| `t` | t | |
| `θ` | s | **merges with `s`** |
| `ð` | z | **merges with `z`** |
| `n` | n | coda `-n` survives; onset `n` epenthesizes |
| `l` | l | |
| `r` | r | **merges with `l`-class liquids in effect** (see limitations) |
| `z` | z | |
| `s` | s | |
| `ʃ` | sh | |
| `j` | y | onset glide |
| `ɡ` | g | (palatalizes to `j` before `i`) |
| `k` | k | (palatalizes to `q` before `i`) |
| `q` | k | **merges with `k`** |
| `x` | h | guttural → `h` (palatalizes to `x` before `i`) |
| `ɣ` | h | **merges with `h`** |
| `ħ` | h | pharyngeal → `h` |
| `h` | h | |

### Emphatics (consonant + `ˤ`) → plain onset

| IPA | Onset | Note |
|-----|-------|------|
| `tˤ` | t | emphasis lost |
| `sˤ` | s | emphasis lost |
| *any other* `Cˤ` | onset(C) | emphasis dropped; rendered as the plain consonant |

### Glottal / pharyngeal (dropped)

| IPA | Name | Treatment |
|-----|------|-----------|
| `ʔ` | *alaph* | dropped |
| `ʕ` | *ayin* | dropped |

### Vowel nuclei

| IPA | Nucleus | Note |
|-----|---------|------|
| `a`, `ɑ` | a | **merge** to a single `a` |
| `e` | e | |
| `i` | i | (triggers `g/k/h → j/q/x` palatalization) |
| `o` | o | |
| `u` | u | |

Vowel **length** (`Vː`) carries no extra information in Mandarin and is dropped:
a long vowel snaps to the same nucleus as its short counterpart.

## 3. The legal-syllable whitelist

`transliterate_zh.py` hard-codes a conservative standard Putonghua whitelist of
**403 toneless syllables** (`_LEGAL`). It is the single source of legality:

> **Hard invariant:** every syllable the engine emits MUST be in `_LEGAL`.
> `--coverage` scans the entire corpus and reports `ILLEGAL pinyin syllables:
> NONE (all legal)`.

Across the 260-file corpus the engine produces **128 distinct syllables**, all of
them members of the whitelist and all of them covered by the Hanzi table (so
`--coverage` reports **zero** illegal syllables, **zero** Zhuyin gaps, and
**zero** Hanzi gaps).

---

# Pinyin → Zhuyin transcode

The Zhuyin tier is a **standard deterministic Pinyin↔Bopomofo transcode** of the
same toneless syllable stream — no second phonetic decision is made. The
`ZH_INIT` and `ZH_FINAL` tables in `transliterate_zh.py` implement it.

| Mechanism | Rule |
|-----------|------|
| **Initials** | `b→ㄅ p→ㄆ m→ㄇ f→ㄈ d→ㄉ t→ㄊ n→ㄋ l→ㄌ g→ㄍ k→ㄎ h→ㄏ j→ㄐ q→ㄑ x→ㄒ zh→ㄓ ch→ㄔ sh→ㄕ r→ㄖ z→ㄗ c→ㄘ s→ㄙ` |
| **Finals** | the standard `a→ㄚ o→ㄛ e→ㄜ ai→ㄞ … an→ㄢ en→ㄣ ang→ㄤ eng→ㄥ`, medials `i→ㄧ u→ㄨ ü→ㄩ`, and the compound finals (`ia→ㄧㄚ`, `uo→ㄨㄛ`, `ong→ㄨㄥ`, …) |
| **Apical empty rime** | `-i` after the seven apical initials `zh ch sh r z c s` is the **bare initial symbol** (no extra vowel glyph): `shi → ㄕ`, `si → ㄙ`, `ri → ㄖ`, `zi → ㄗ` |
| **Zero-initial `y/w`** | the `y-`/`w-` spellings are *restored* to their `i-`/`u-` medials before transcoding: `yi→ㄧ`, `wu→ㄨ`, `ya→ㄧㄚ`, `wo→ㄨㄛ`, `wei→ㄨㄟ`, `ye→ㄧㄝ`, … |
| **`j/q/x` + u** | the orthographic `u` after `j/q/x` is always `/y/` (ü), so the medial is ㄩ, not ㄨ |

Because Zhuyin is a pure transcode, it inherits the Pinyin tier's faithfulness
exactly: it is atonal by the same decision, and it loses and merges precisely the
same distinctions (nothing more, nothing less).

---

# The Hanzi tiers (Simplified + Traditional)

## Approach

Hanzi is **Stage B**: a frozen `syllable → 字` lookup that **consumes** the
Pinyin engine's output. It makes **no phonetic decisions** of its own — those
were all made by the Pinyin engine. Each of the produced toneless syllables is
mapped to **one** character, chosen from the standard Xinhua 音译表 /
《世界人名翻译大辞典》 inventory of **neutral, semantically-bleached
transcription characters** (巴 拉 西 斯 德 萨 阿 …).

Curation principles, applied once at authoring time:

- **Choose by Mandarin sound only** (tone ignored), preferring the conventional
  音译 character for the syllable.
- **Avoid strong, negative, sacred, or loaded meanings.** This is scripture;
  sound-chosen characters can spell accidental words, so neutrality is a hard
  requirement (see Limitations).
- **Resolve all one-to-many ambiguity once, by fiat** — the standard offers
  several characters per syllable; exactly one is frozen, making the tier
  deterministic.

## Simplified vs Traditional: one dual-column table

The two Hanzi tiers are driven by **one hand-authored dual-column table**
(`HANZI` in `transliterate_zh.py`), `{simplified, traditional}` per syllable:

- A large majority of transcription characters are **script-invariant** (阿 巴 波
  瓦 哈 米 尼 …) and the two columns are identical.
- Only a minority differ; both columns are **authored directly** for those, e.g.
  热/熱, 萨/薩, 乌/烏, 尔/爾, 亚/亞, 维/維, 书/書, 达/達, 兰/蘭, 图/圖, 么/麼, …
- **OpenCC is NOT a build dependency.** Running OpenCC `s2t`/`t2s` at build time
  would reintroduce the genuine Simplified→Traditional one-to-many ambiguity and
  add version drift. OpenCC is used **only as authoring-time QA**, to verify each
  chosen pair is a recognized variant pair.

A syllable with no table entry would render as the missing glyph `□`, so
`--coverage` reports the exact remaining gap. The shipped table covers **every**
syllable the corpus produces — `hanzi table gaps: 0`.

## Tones: omitted in Pinyin/Zhuyin, an imposed artifact in Hanzi

**Decision: TONELESS.** The Peshitta source is phonetic with **no tone marks**.
Toneless Pinyin is the only option that adds *zero fabricated information*.

- "Neutral tone" (轻声) is **rejected** — it is a *marked* Mandarin phonological
  category (destressed, pitch-conditioned), not "no tone"; tagging every syllable
  neutral would assert a false claim.
- "Default contour tone" (all tone-1, etc.) is **rejected** — maximally
  fabricated, reads as a robotic monotone.

So Pinyin and Zhuyin are emitted **toneless by design** (tones omitted, not lost;
pronounce with even/level pitch).

**The Hanzi artifact.** There is no toneless Hanzi glyph: choosing 西 for `xi`
commits to xī (T1); choosing 萨 for `sa` commits to sà (T4). The Hanzi tier is
therefore *structurally incapable* of the honesty the Pinyin tier achieves — it
**silently imposes one citation tone per syllable** via the character chosen.
This is acceptable **only because it is documented as an artifact**: it is exactly
how all foreign-name transcription works (巴拉巴 Barabbas already carries tones
nobody claims Aramaic had). The authoritative atonal statement is the **Pinyin**
tier.

**The verification invariant.** The Hanzi tier must add *nothing but* artifactual
tone — no extra phonetic distortion, no table drift. This is provable:

> `strip_tones(hanzi_to_pinyin(字)) == toneless_pinyin_syllable`
>
> for every syllable, in **both** the Simplified and Traditional columns. Each
> chosen glyph's standard Mandarin reading, with its tone stripped, must equal the
> target syllable the Pinyin engine produced. This catches any wrong or drifted
> character.

The check is **strict**: the glyph's *preferred (default) reading* — not merely
one of its heteronym readings — must strip to the key, so no character is chosen
that a reader would most naturally voice as a different syllable. It is enforced
by `transliterate_zh.py --verify-hanzi` (an optional `pypinyin` authoring-QA pass;
it reports SKIPPED rather than failing where `pypinyin` is not installed, since the
shipped transducer has no runtime `pypinyin` dependency).

> **Heteronym-drift fix.** Four earlier glyphs spelled their key only via a
> *minority* reading (their default reading was a different syllable), which the
> strict check flagged. Each was re-frozen to a neutral 音译 character whose
> **default** reading is the key: `le` 勒(lèi)→**叻**(lè); `se` 塞(sāi)→**瑟**(sè);
> `shi` 什(shén)→**士**(shì); `za` 扎(zhā)→**匝**(zā). All four are script-invariant
> (identical Simplified/Traditional columns, OpenCC-confirmed).

---

# Documented Limitations / 文書化された限界

The Pinyin, Zhuyin, and two Hanzi tiers are **reader aids**, not reversible
scholarly transcriptions. **Mandarin forces the heaviest phonetic collapse of any
target language in this project.** Use the **Scholarly** tier when precision
matters.

- **Heaviest collapse / forced epenthesis inflates length.** Mandarin admits
  **zero** consonant clusters and codas only `-n`/`-ng`, so an epenthetic vowel
  (default `e`; apical `i` after `z c s zh ch sh r`) is inserted to break **every**
  Syriac cluster and non-nasal coda. This **adds vowels not in the Syriac** and
  the syllable string is markedly longer than the source (e.g. `breːʃiːθ` →
  `bo·re·shi·si`, four syllables for one CCVCC root).
- **Voicing lost.** Mandarin initials are aspiration-, not voicing-, contrastive;
  voiced/voiceless distinctions collapse onto the nearest onset.
- **Massive consonant mergers.** `v → f`; `θ → s`; `ð → z`; `q → k`; `ɣ → h`;
  the whole guttural/pharyngeal series `x ħ h` all collapse to `h`. So `/f v θ ð
  ʃ z/` and the gutturals are not reliably distinguished.
- **`l / r` distinction effectively lost.** Mandarin has one liquid system; the
  Syriac `l`/`r` contrast does not survive cleanly into the reader tiers.
- **Emphatics lost.** The emphatic marker `ˤ` is dropped; `tˤ → t`, `sˤ → s`, any
  other `Cˤ → C`. Pharyngealization is not represented.
- **Glottals dropped.** `ʔ` (*alaph*) and `ʕ` (*ayin*) are dropped entirely.
- **Vowel length and quality lost.** `Vː` snaps to the same nucleus as `V`; `a`
  and `ɑ` merge to a single `a`.
- **Palatalization is imposed.** `g/k/h` before `/i/` become `j/q/x` (a Mandarin
  phonotactic requirement), changing the consonant's surface form.
- **Tones fabricated-then-omitted (Pinyin/Zhuyin) and imposed-as-artifact
  (Hanzi).** Pinyin and Zhuyin carry **no** tone by deliberate design. Hanzi
  **necessarily imposes** one citation tone per glyph — an artifact of the writing
  system, not a feature of the source. Verify with the `strip_tones` invariant
  above.
- **Hanzi imposes MEANING and is NOT readback-grade.** Sound-chosen characters
  can spell accidental words (a scripture-sensitivity risk, mitigated by the
  hand-curated neutral table). A reader recovers morphemes, not the Aramaic or
  even reliably our intended syllables. Concretely, **the Hanzi tier cannot
  distinguish Barabba from Barava**: with `v → f` and voicing collapse, `ʔaba` and
  `ʔava` both fall together (Pinyin `a·ba` vs `a·fa` already merges the `b/v`
  meaning, and the Hanzi spells the same neutral characters) — the contrast is
  gone. See the worked example.
- **Not reversible.** None of the four reader tiers can be inverted back to the
  original IPA.

All of these distinctions are fully preserved in the **Scholarly** tier (and most
in **Pretty**), which is why those two tiers remain language-neutral.

---

# Reference standards / 参照基準

Two reference standards are declared in **one** guide (the GA/RP analog), paired
with the two script tiers:

| Axis | Standard A (Simplified tier) | Standard B (Traditional tier) |
|------|------------------------------|-------------------------------|
| Name | **普通话 Pǔtōnghuà** | **國語 Guóyǔ** |
| Region | PRC mainland, Singapore | Taiwan (HK adjacent) |
| Romanization of record | Hanyu Pinyin | Zhuyin/Bopomofo (pedagogical) |
| Dictionary | 《现代汉语词典》 / GB | 教育部《國語辭典》 |

The transducer is **not** forked: the phonetic core (the toneless syllable
inventory) is shared, and the real Putonghua/Guoyu differences (retroflex
realization, erhua, a few lexical tones) **do not change the deterministic
toneless spelling** — they affect only prose, not the build. Pair
Simplified↔Putonghua/Pinyin and Traditional↔Guoyu/Zhuyin so the script split has
a coherent identity. The Traditional tier targets the **Taiwan** variant
(OpenCC `s2tw` for QA), not HK.

**Cantonese is out of scope** for this phase. Trad vs. Simp is a *script*
difference over the same spoken Mandarin; Cantonese is a *different spoken
language* (different codas `-p -t -k -m`, six tones, Jyutping, a Cantonese-specific
Hanzi set) needing a separate transducer core — a Phase-2 candidate. The IPA→
syllable approximation is kept in a swappable module so that fork stays clean.

---

# Worked Example / 例示

Six verses, shown in source IPA followed by all six tiers. These values come
straight from the converter (they are the embedded gold cases used by
`--selftest`), so they are guaranteed to match the shipped tool exactly.
Scholarly/Pretty are byte-identical to the English Peshitta.

### John 1:1

```
IPA        breːʃiːθ ʔiːθawj wɑː melθɑː whuː melθɑː ʔiːθawj wɑː lwɑːθ ʔɑːlɑːhɑː waʔlɑːhɑː ʔiːθawj wɑː huː melθɑː
Scholarly  brēšīṯ ʾīṯawy wā melṯā whū melṯā ʾīṯawy wā lwāṯ ʾālāhā waʾlāhā ʾīṯawy wā hū melṯā
Pretty     brēshīth īthawy wā melthā whū melthā īthawy wā lwāth ālāhā wa'lāhā īthawy wā hū melthā
Pinyin     bo·re·shi·si yi·sa·wu·yi wa me·le·sa wu·hu me·le·sa yi·sa·wu·yi wa le·wa·si a·la·ha wa·la·ha yi·sa·wu·yi wa hu me·le·sa
Zhuyin     ㄅㄛ·ㄖㄜ·ㄕ·ㄙ ㄧ·ㄙㄚ·ㄨ·ㄧ ㄨㄚ ㄇㄜ·ㄌㄜ·ㄙㄚ ㄨ·ㄏㄨ ㄇㄜ·ㄌㄜ·ㄙㄚ ㄧ·ㄙㄚ·ㄨ·ㄧ ㄨㄚ ㄌㄜ·ㄨㄚ·ㄙ ㄚ·ㄌㄚ·ㄏㄚ ㄨㄚ·ㄌㄚ·ㄏㄚ ㄧ·ㄙㄚ·ㄨ·ㄧ ㄨㄚ ㄏㄨ ㄇㄜ·ㄌㄜ·ㄙㄚ
Hanzi(简)  波热士斯 伊萨乌伊 瓦 么叻萨 乌胡 么叻萨 伊萨乌伊 瓦 叻瓦斯 阿拉哈 瓦拉哈 伊萨乌伊 瓦 胡 么叻萨
Hanzi(繁)  波熱士斯 伊薩烏伊 瓦 麼叻薩 烏胡 麼叻薩 伊薩烏伊 瓦 叻瓦斯 阿拉哈 瓦拉哈 伊薩烏伊 瓦 胡 麼叻薩
```

### John 1:2

```
IPA        hɑːnɑː ʔiːθawj wɑː breːʃiːθ lwɑːθ ʔɑːlɑːhɑː
Scholarly  hānā ʾīṯawy wā brēšīṯ lwāṯ ʾālāhā
Pretty     hānā īthawy wā brēshīth lwāth ālāhā
Pinyin     ha·na yi·sa·wu·yi wa bo·re·shi·si le·wa·si a·la·ha
Zhuyin     ㄏㄚ·ㄋㄚ ㄧ·ㄙㄚ·ㄨ·ㄧ ㄨㄚ ㄅㄛ·ㄖㄜ·ㄕ·ㄙ ㄌㄜ·ㄨㄚ·ㄙ ㄚ·ㄌㄚ·ㄏㄚ
Hanzi(简)  哈纳 伊萨乌伊 瓦 波热士斯 叻瓦斯 阿拉哈
Hanzi(繁)  哈納 伊薩烏伊 瓦 波熱士斯 叻瓦斯 阿拉哈
```

### John 1:3

```
IPA        kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː
Scholarly  kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā
Pretty     kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā
Pinyin     ku·le bo·yi·yi·ze·he he·wa wu·fu·le·a·za·wu·yi a·fu·la he·za he·wa·si me·de·me da·he·wa
Zhuyin     ㄎㄨ·ㄌㄜ ㄅㄛ·ㄧ·ㄧ·ㄗㄜ·ㄏㄜ ㄏㄜ·ㄨㄚ ㄨ·ㄈㄨ·ㄌㄜ·ㄚ·ㄗㄚ·ㄨ·ㄧ ㄚ·ㄈㄨ·ㄌㄚ ㄏㄜ·ㄗㄚ ㄏㄜ·ㄨㄚ·ㄙ ㄇㄜ·ㄉㄜ·ㄇㄜ ㄉㄚ·ㄏㄜ·ㄨㄚ
Hanzi(简)  库叻 波伊伊泽赫 赫瓦 乌福叻阿匝乌伊 阿福拉 赫匝 赫瓦斯 么德么 达赫瓦
Hanzi(繁)  庫叻 波伊伊澤赫 赫瓦 烏福叻阿匝烏伊 阿福拉 赫匝 赫瓦斯 麼德麼 達赫瓦
```

### Matthew 1:1

```
IPA        kθɑːvɑː diːliːðuːθeh djeʃuːʕ mʃiːħɑː breh dðawiːð breh dʔavrɑːhɑːm
Scholarly  kṯāḇā dīlīḏūṯeh dyešūʿ mšīḥā breh dḏawīḏ breh dʾaḇrāhām
Pretty     kthāvā dīlīdhūtheh dyeshūʿ mshīḥā breh ddhawīdh breh d'avrāhām
Pinyin     ke·sa·fa di·li·zu·se·he de·ye·shu me·shi·ha bo·re·he de·za·wei·zi bo·re·he de·a·fu·ru·ha·me
Zhuyin     ㄎㄜ·ㄙㄚ·ㄈㄚ ㄉㄧ·ㄌㄧ·ㄗㄨ·ㄙㄜ·ㄏㄜ ㄉㄜ·ㄧㄝ·ㄕㄨ ㄇㄜ·ㄕ·ㄏㄚ ㄅㄛ·ㄖㄜ·ㄏㄜ ㄉㄜ·ㄗㄚ·ㄨㄟ·ㄗ ㄅㄛ·ㄖㄜ·ㄏㄜ ㄉㄜ·ㄚ·ㄈㄨ·ㄖㄨ·ㄏㄚ·ㄇㄜ
Hanzi(简)  克萨法 迪利祖瑟赫 德耶书 么士哈 波热赫 德匝维孜 波热赫 德阿福茹哈么
Hanzi(繁)  克薩法 迪利祖瑟赫 德耶書 麼士哈 波熱赫 德匝維孜 波熱赫 德阿福茹哈麼
```

### Romans 1:1

```
IPA        pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː
Scholarly  pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā
Pretty     pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā
Pinyin     pa·wu·la·wu·si a·fu·da de·ye·shu me·shi·ha ka·ri·ya wa·shi·li·ha de·e·si·po·re·shi le·wa·ne·ge·li·yi·ya·wu·ne de·a·la·ha
Zhuyin     ㄆㄚ·ㄨ·ㄌㄚ·ㄨ·ㄙ ㄚ·ㄈㄨ·ㄉㄚ ㄉㄜ·ㄧㄝ·ㄕㄨ ㄇㄜ·ㄕ·ㄏㄚ ㄎㄚ·ㄖ·ㄧㄚ ㄨㄚ·ㄕ·ㄌㄧ·ㄏㄚ ㄉㄜ·ㄜ·ㄙ·ㄆㄛ·ㄖㄜ·ㄕ ㄌㄜ·ㄨㄚ·ㄋㄜ·ㄍㄜ·ㄌㄧ·ㄧ·ㄧㄚ·ㄨ·ㄋㄜ ㄉㄜ·ㄚ·ㄌㄚ·ㄏㄚ
Hanzi(简)  帕乌拉乌斯 阿福达 德耶书 么士哈 卡日亚 瓦士利哈 德厄斯珀热士 叻瓦讷格利伊亚乌讷 德阿拉哈
Hanzi(繁)  帕烏拉烏斯 阿福達 德耶書 麼士哈 卡日亞 瓦士利哈 德厄斯珀熱士 叻瓦訥格利伊亞烏訥 德阿拉哈
```

### Matthew 27:16 (Barabbas)

```
IPA        dmeθqre bar-ʔaba lvar-ʔaba lvar-ʔava
Scholarly  dmeṯqre bar-ʾaba lḇar-ʾaba lḇar-ʾaḇa
Pretty     dmethqre bar-'aba lvar-'aba lvar-'ava
Pinyin     de·me·si·ke·re ba·ri-a·ba le·fa·ri-a·ba le·fa·ri-a·fa
Zhuyin     ㄉㄜ·ㄇㄜ·ㄙ·ㄎㄜ·ㄖㄜ ㄅㄚ·ㄖ-ㄚ·ㄅㄚ ㄌㄜ·ㄈㄚ·ㄖ-ㄚ·ㄅㄚ ㄌㄜ·ㄈㄚ·ㄖ-ㄚ·ㄈㄚ
Hanzi(简)  德么斯克热 巴日-阿巴 叻法日-阿巴 叻法日-阿法
Hanzi(繁)  德麼斯克熱 巴日-阿巴 叻法日-阿巴 叻法日-阿法
```

Notes you can trace through these examples:

- **Forced epenthesis.** `breːʃiːθ` → `bo·re·shi·si`: the onset cluster `br-`
  grows `bo·re` (default `e`), the `ʃ` apical-epenthesizes to `shi`, and the final
  `θ` (→ `s`) grows `si`. One root, four syllables.
- **Mergers.** `melθɑː` → `me·le·sa`: `θ` reads as `s`. `wvelʕɑːðawj` →
  `wu·fu·le·a·za·wu·yi`: `v → f`, `ð → z`, *ayin* drops.
- **Palatalization and dropped gutturals.** `mʃiːħɑː` (Messiah) → `me·shi·ha`:
  the pharyngeal `ħ` collapses to `h`.
- **Glide + zero-initial spelling.** `ʔiːθawj` → `yi·sa·wu·yi`: *alaph* drops,
  and the `j` glide surfaces as `yi`.
- **Zhuyin apical empty rime.** `shi → ㄕ`, `si → ㄙ`, `ri → ㄖ`, `zi → ㄗ` — the
  apical `-i` is the bare initial symbol.
- **The Barabbas loss.** `ba` (from `ʔaba`) and `fa` (from `ʔava`) differ in
  Pinyin only because `b`/`v` already collapsed `v → f` upstream; the **Hanzi**
  spells neutral characters that **cannot distinguish Barabba from Barava** — a
  concrete, citable loss of the Hanzi tier.

---

# Folder Layout / フォルダ構成

Everything lives under the repository path `Chinese/Peshita_Chinese/`
(relative to the repo root):

```
Chinese/Peshita_Chinese/
├── TRANSLITERATION_SCHEME.md            # this document
├── transliterate_zh.py                  # the deterministic converter (authoritative)
├── transcription_mapping_zh.json        # machine-readable mirror of the mapping tables
├── Scholarly/                           # tier 1 output (language-neutral)
│   ├── Matthew-Matityahu/
│   │   ├── matthewmatityahu1_scholarly.txt
│   │   ├── matthewmatityahu2_scholarly.txt
│   │   └── ...
│   ├── 1stCorinthians/
│   └── ...                              # 27 book folders
├── Pretty/                              # tier 2 output (same tree, *_pretty.txt)
│   └── ...
├── Pinyin/                              # tier 3 output (same tree, *_pinyin.txt)
│   └── ...
├── Zhuyin/                              # tier 4 output (same tree, *_zhuyin.txt)
│   └── ...
├── Hanzi-Simplified/                    # tier 5 output (same tree, *_hanzi_simplified.txt)
│   └── ...
└── Hanzi-Traditional/                   # tier 6 output (same tree, *_hanzi_traditional.txt)
    └── ...
```

Each tier directory (`Scholarly/`, `Pretty/`, `Pinyin/`, `Zhuyin/`,
`Hanzi-Simplified/`, `Hanzi-Traditional/`) mirrors the book/chapter structure of
`IPA/Peshitta/`. For every source file `IPA/Peshitta/<Book>/<name>_ipa.txt` the
build produces one file per tier at
`Chinese/Peshita_Chinese/<Tier>/<Book>/<name>_<tier>.txt`. Each output line keeps
its `<verse#>\t` prefix verbatim; only the verse text after the first tab is
transliterated.

The current corpus is **260 IPA source files** across **27 books**, yielding
**1560 transliterated files** (260 × 6 tiers).

---

# Reproducing / 再現

The whole corpus can be regenerated from scratch with one command, run from this
folder:

```sh
python3 transliterate_zh.py --build
```

This walks every `*_ipa.txt` under `IPA/Peshitta/`, transliterates each into all
six tiers, and writes the `Scholarly/`, `Pretty/`, `Pinyin/`, `Zhuyin/`,
`Hanzi-Simplified/`, and `Hanzi-Traditional/` trees described above. It reports
the number of files written and any unmapped characters (there should be none).
The converter resolves the repository root from its own location, so it runs
correctly from this shipped folder.

Other useful entry points:

```sh
python3 transliterate_zh.py --selftest        # run the embedded gold cases (all 6 tiers)
python3 transliterate_zh.py --coverage        # scan the corpus: unmapped IPA, ILLEGAL pinyin,
                                              #   zhuyin gaps, and syllables missing a Hanzi char
python3 transliterate_zh.py --write-mapping   # (re)write transcription_mapping_zh.json
```

`--coverage` is the build's safety net. On the shipped corpus it reports:

```
Scanned 260 IPA file(s).
  unmapped IPA segments     : none
  ILLEGAL pinyin syllables  : NONE (all legal)
  zhuyin transcode gaps     : none
  hanzi table gaps          : 0 syllable(s) need a character
```

`transliterate_zh.py` is authoritative: `transcription_mapping_zh.json` is a
machine-readable mirror of its hard-coded tables, regenerated by
`--write-mapping`. The **Scholarly** and **Pretty** tiers reuse the English
transducer's logic verbatim, so their output matches `English/Peshita_English`
character for character.

---

*Prepared and signed by **Shin**.*
