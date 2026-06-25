# Chinese (Mandarin) IPA Pronunciation Guide

**Version:** 1.0.0
**Date:** 2026-06-25
**Language:** Chinese (Mandarin) (汉语 / 漢語) (ISO 639-3: `cmn`)  
**Encoding:** UTF-8  
**IPA Standard:** IPA (International Phonetic Alphabet, 2015 revision)  
**Reference Standards:** 普通话 Pǔtōnghuà (PRC, Simplified) and 國語 Guóyǔ (Taiwan, Traditional)  

Machine-readable IPA-based pronunciation guide for Standard Mandarin Chinese (标准汉语 / 標準漢語). All pronunciation data is encoded in the International Phonetic Alphabet (IPA, 2015 revision) as the primary and only phonetic system. Designed for AI-assisted pronunciation, text-to-speech reference, second-language teaching, and language documentation. Two reference standards are documented in parallel: 普通话 Pǔtōnghuà (PRC Standard Mandarin, Beijing-based phonology, written in SIMPLIFIED characters and romanized with Hanyu Pinyin) and 國語 Guóyǔ (Taiwan Standard Mandarin, written in TRADITIONAL characters and taught with Zhuyin/Bopomofo). Mandarin's signature feature — LEXICAL TONE (four contrastive tones plus a neutral tone) — is treated as first-class data throughout, alongside the aspiration-based (not voicing-based) obstruent contrast, the initial/final syllable architecture, and the logographic Hanzi writing system. NOTE on scope: tone is fully documented for the LANGUAGE here; only the downstream Peshitta READER TIERS are toneless, because the Peshitta source IPA carries no tone.

### Varieties Covered

- **Pǔtōnghuà (普通话 / 普通話, 'common speech'; PRC Standard Mandarin, PTH)** — People's Republic of China (the de jure national standard; also the basis of Mandarin teaching in Singapore and Malaysia). **Script:** Simplified characters (简体字). **Romanization:** Hanyu Pinyin (汉语拼音). **Basis:** codified Standard Mandarin whose phonology is based on the BEIJING dialect, its grammar on exemplary modern vernacular (白话 báihuà) writing, and its vocabulary on Northern Mandarin at large; it is the national lingua franca of the PRC, the medium of schooling, broadcasting (CCTV), dictionaries and TTS, and the default standard most learners and speech systems target. **Key features:**
  - fully retains the RETROFLEX initial series zh `/ʈʂ/`, ch `/ʈʂʰ/`, sh `/ʂ/`, r `/ʐ~ɻ/` as distinct from the dental series z `/ts/`, c `/tsʰ/`, s `/s/`;
  - characteristic, often pervasive ERHUA (儿化 érhuà): a rhotacizing -r suffix restructures the rime — 花儿 huār 'flower', 一点儿 yìdiǎnr 'a little', 哪儿 nǎr 'where' (more frequent in Beijing/Northern speech than in the formal codified norm);
  - robust NEUTRAL TONE (轻声 qīngshēng) on particles (的 de, 了 le, 吗 ma, 呢 ne), reduplications and many disyllable suffixes (子 zi, 头 / 頭 tou);
  - standard lexical readings where Taiwan differs (e.g. 垃圾 lājī 'garbage', 和 'and' usually hé, 企 qǐ in 企业 qǐyè);
  - the default basis of mainland dictionaries, schooling, broadcasting and most learner materials and TTS systems.
  
  The prestige reference standard of mainland China, Beijing-based in phonology and written in simplified characters with Hanyu Pinyin. Analogous to the Eastern (Madnhaya) tradition in the Peshitta guide, General American (GA) in the English guide, Peninsular Castilian in the Spanish guide, Standard South Korean (Seoul) in the Korean guide, and Standard/Tokyo Japanese in the Japanese guide — one of two co-equal documented standards.
- **Guóyǔ (國語, 'national language'; Taiwan Standard Mandarin, GUO)** — Taiwan (Republic of China); the term 華語 / 华语 Huáyǔ is the parallel label used for Mandarin abroad. **Script:** Traditional characters (繁體字). **Romanization:** Zhuyin / Bopomofo (注音符號) for pedagogy; Hanyu Pinyin is also official for romanizing names. **Basis:** Taiwan's codified Standard Mandarin, sharing the same phonemic backbone as Pǔtōnghuà but with its own pronunciation-dictionary norms and strong contact influence from Taiwanese Hokkien (Min Nan); written in traditional characters and taught through Zhuyin/Bopomofo. **Key features:**
  - little to NO ERHUA (儿化): the rhotacized -r suffix is largely absent; 一点 yìdiǎn rather than 一点儿 yìdiǎnr;
  - frequent DE-RETROFLEXION: the retroflex series zh `/ʈʂ/`, ch `/ʈʂʰ/`, sh `/ʂ/`, r `/ʐ/` tends to merge toward the dental series z `/ts/`, c `/tsʰ/`, s `/s/`, and r toward `[z]` or a glide — so zh→z, ch→c, sh→s, r→(z/-) in colloquial speech;
  - fewer and weaker NEUTRAL TONES — many syllables that are 轻声 in Pǔtōnghuà keep a full citation tone in Guóyǔ;
  - lexical tone/pronunciation and vocabulary differences: 垃圾 lèsè (vs lājī), 和 'and' often hàn (vs hé), 企 qì in 企業 qìyè (vs qǐyè), 法國 Fàguó (vs Fǎguó), 期 qí (vs qī);
  - the major regional standard and principal alternative reference to mainland Pǔtōnghuà.
  
  The major alternative reference standard, the Standard Mandarin of Taiwan, written in traditional characters and taught with Zhuyin/Bopomofo. It shares the entire Mandarin phonological backbone with Pǔtōnghuà — the same initials, finals and four-tone system — but is defined against it chiefly by its reduced/absent erhua, frequent de-retroflexion of the zh/ch/sh/r series, fewer neutral tones, and a set of lexical tone/pronunciation/vocabulary differences, all of which are surface or lexical and leave the toneless syllable spelling unchanged. Analogous to the Western (Serto) tradition in the Peshitta guide, Received Pronunciation (RP/SSBE) in the English guide, General Latin American in the Spanish guide, North Korean 문화어 (Pyongyang) in the Korean guide, and Kansai/Keihan Japanese in the Japanese guide — one of two co-equal documented standards.

Pǔtōnghuà and Guóyǔ share ONE phonemic system — the same 21 initials + zero initial, the same ~35–38 finals, and the identical four lexical tones plus neutral tone — so the toneless pinyin spelling of a syllable is the same in both. Their differences are SURFACE and LEXICAL: (1) ERHUA (儿化) is characteristic of Pǔtōnghuà (花儿 huār) but largely absent in Guóyǔ (花 huā); (2) Guóyǔ shows frequent DE-RETROFLEXION, merging zh/ch/sh/r toward z/c/s, whereas Pǔtōnghuà keeps the retroflex series fully distinct; (3) Pǔtōnghuà has more, and more obligatory, NEUTRAL TONES than Guóyǔ; (4) a set of LEXICAL splits in tone, reading or word choice (垃圾 lājī vs lèsè, 和 hé vs hàn, 企 qǐ vs qì, 法 Fǎguó vs Fàguó). None of these change the phonemic inventory or the toneless spelling; they are documented as the two standards' realizations of one shared system. Because the two reference standards key the two Hanzi reader tiers of the Chinese Peshitta — Pǔtōnghuà → Simplified, Guóyǔ → Traditional — the simplified vs traditional character distinction in this guide is anchored to these two co-equal norms rather than treated as a mere font choice.

### Companion Files

- `Chinese/chinese_pronunciation_guide.md`
- `Chinese/Peshita_Chinese/Scholarly/`
- `Chinese/Peshita_Chinese/Pretty/`
- `Chinese/Peshita_Chinese/Pinyin/`
- `Chinese/Peshita_Chinese/Zhuyin/`
- `Chinese/Peshita_Chinese/Hanzi-Simplified/`
- `Chinese/Peshita_Chinese/Hanzi-Traditional/`
- `peshitta_pronunciation_guide.json`
- `biblical_aramaic_pronunciation_guide.json`
- `biblical_hebrew_pronunciation_guide.json`
- `English/english_pronunciation_guide.json`
- `Spanish/spanish_pronunciation_guide.json`
- `Korean/korean_pronunciation_guide.json`
- `Japanese/japanese_pronunciation_guide.json`

The Chinese Peshitta ships in SIX reader tiers: Scholarly and Pretty (language-neutral Latin transcription), Pinyin (汉语拼音, the deterministic phonetic spine), Zhuyin (注音符號, a transcode of the pinyin into Bopomofo), and Hanzi in two character sets — Hanzi-Simplified (简体字, keyed to Pǔtōnghuà) and Hanzi-Traditional (繁體字, keyed to Guóyǔ), a downstream transcription-character lookup. ALL FOUR phonetic/native tiers (Pinyin, Zhuyin, and both Hanzi sets) are TONELESS because the Peshitta source IPA carries no tone; the Hanzi tiers are additionally NON-FAITHFUL, since mapping a toneless syllable onto a Chinese character unavoidably borrows that character's citation tone and graphic meaning as an artifact. All paths are repo-relative; `Chinese/chinese_pronunciation_guide.md` is the human-readable companion to this JSON.

### Notes

- Chinese is written in HANZI (汉字 / 漢字), a LOGOGRAPHIC / morphosyllabic script in which each character writes one morpheme and (in Mandarin) almost always exactly one syllable + tone — a near one-to-one character ↔ syllable ↔ morpheme correspondence, unlike the segmental Semitic, English and Spanish scripts and unlike Japanese's three-script mixture. Characters are built from radicals (部首) and components and are mostly 形声 / 形聲 phono-semantic compounds (semantic radical + phonetic component), written with conventional stroke order.
- Two character sets are in use and both appear in this guide: SIMPLIFIED (简体字, PRC / Singapore — 马, 妈, 汉, 语, 国) and TRADITIONAL (繁體字, Taiwan / Hong Kong / Macau — 馬, 媽, 漢, 語, 國). The simplified vs traditional split is purely ORTHOGRAPHIC and does NOT change the spoken phonology, the IPA, or the toneless pinyin spelling.
- Mandarin's defining feature is LEXICAL TONE: every full syllable carries one of four contrastive tones (T1 high-level 55 `˥`, T2 rising 35 `˧˥`, T3 low-dipping 214 `˨˩˦`, T4 high-falling 51 `˥˩`) plus a neutral tone (轻声), and tone DISTINGUISHES MEANING — mā 妈/媽 'mother', má 麻 'hemp', mǎ 马/馬 'horse', mà 骂/罵 'scold' differ in tone alone. Pinyin marks tone with diacritics (ā á ǎ à); Zhuyin with tone marks (ˊ ˇ ˋ ˙, T1 unmarked).
- Mandarin has NO VOICING CONTRAST in its obstruents: where European languages oppose voiced and voiceless (b/p, d/t, g/k), Mandarin opposes UNASPIRATED and ASPIRATED voiceless stops/affricates — b `/p/` vs p `/pʰ/`, d `/t/` vs t `/tʰ/`, g `/k/` vs k `/kʰ/`, z `/ts/` vs c `/tsʰ/`, zh `/ʈʂ/` vs ch `/ʈʂʰ/`, j `/tɕ/` vs q `/tɕʰ/`. Pinyin b/d/g are voiceless and UNaspirated, not voiced `[b d ɡ]`; this is the single most common segmental learner error.
- The initial inventory is 21 consonants + the zero initial, in three parallel coronal series — DENTAL z `/ts/` c `/tsʰ/` s `/s/`, RETROFLEX zh `/ʈʂ/` ch `/ʈʂʰ/` sh `/ʂ/` r `/ʐ~ɻ/`, and ALVEOLO-PALATAL j `/tɕ/` q `/tɕʰ/` x `/ɕ/` — where j/q/x are in COMPLEMENTARY DISTRIBUTION with z/c/s, zh/ch/sh and g/k/h, occurring only before high front i / ü. The retroflex series and the alveolo-palatals are cross-linguistically marked and are frequent learner difficulties.
- The written final -i after the dental and retroflex series is an APICAL ('buzzed') vowel, NOT `[i]`: `[ɹ̩]` after z/c/s (zi, ci, si) and `[ɻ̩]` after zh/ch/sh/r (zhi, chi, shi, ri) — so zi is `/tsɹ̩/`, not `/tsi/`, a point where IPA, not the pinyin letter, is authoritative.
- The Mandarin syllable is strictly (C)(G)V(C) + TONE: there are NO consonant clusters and the only permitted codas are the nasals `/n/` and `/ŋ/` (-ng) plus the rhotic `/ɚ/` (er / 儿化 erhua). This yields ~400 toneless and ~1,300 tone-bearing syllables, far fewer than in the companion languages, with extensive homophony resolved by tone, by disyllabic compounding, and by the characters themselves.
- Tone is dynamic in connected speech: third-tone SANDHI (T3 + T3 → T2 + T3, 你好 nǐ hǎo → ní hǎo; a non-final T3 surfaces as a low 'half-third'), the 一 yī alternation (yì before T1/T2/T3, yí before T4), the 不 bù alternation (bú before T4), the NEUTRAL tone (轻声 on particles 的 了 吗 呢, reduplication, and suffixes 子 头/頭), and ERHUA (儿化, the rhotacizing -r that restructures the rime — 花儿 huār, 一点儿 yìdiǎnr) are all documented in the tone and sandhi sections.
- The two reference standards share ONE phonemic system but differ at the surface and lexically: Pǔtōnghuà (PRC, simplified, Pinyin) keeps the full retroflex series and pervasive erhua and neutral tone; Guóyǔ (Taiwan, traditional, Zhuyin) has little/no erhua, frequent DE-RETROFLEXION (zh/ch/sh/r → z/c/s/-), fewer neutral tones, and lexical splits (垃圾 lājī vs lèsè, 和 hé vs hàn, 企 qǐ vs qì). None of these change the toneless syllable spelling.
- Phonemic transcriptions use `/ /` slashes and phonetic transcriptions use `[ ]` brackets; suprasegmentals here include the IPA TONE LETTERS / Chao pitch values (`˥` 55, `˧˥` 35, `˨˩˦` 214, `˥˩` 51), the aspiration mark `/ʰ/`, the syllabic / apical under-mark for the buzzed -i vowels `[ɹ̩ ɻ̩]`, and the rhotic hook for erhua `[ɚ]`. IPA, not pinyin or zhuyin, is the authoritative pronunciation record.
- SCOPE CAVEAT on tone: the LANGUAGE is fully tonal and tone is documented richly throughout this guide, but the downstream Peshitta READER TIERS are TONELESS BY DESIGN, because the Peshitta source IPA carries no tone. The Pinyin and Zhuyin tiers are therefore stripped of tone marks, and the Simplified and Traditional Hanzi tiers are NON-FAITHFUL transcription lookups: rendering a toneless source syllable as a Chinese character unavoidably imposes that character's citation tone and lexical meaning, which is an artifact of the medium, not a feature of the Aramaic source.

## Table of Contents

- [How to Read This Guide](#how-to-read-this-guide)
  - [Phonemic vs phonetic notation](#phonemic-vs-phonetic-notation)
  - [How to read the IPA](#how-to-read-the-ipa)
  - [The four tones, the neutral tone & tone notation](#the-four-tones-the-neutral-tone--tone-notation)
  - [The three scripts: Hanzi, Pinyin, Zhuyin (and Wade–Giles)](#the-three-scripts-hanzi-pinyin-zhuyin-and-wadegiles)
  - [How the parallel Pǔtōnghuà / Guóyǔ standards & Simplified / Traditional are shown](#how-the-parallel-pǔtōnghuà--guóyǔ-standards--simplified--traditional-are-shown)
  - [Note: the Peshitta reader tiers are TONELESS](#note-the-peshitta-reader-tiers-are-toneless)
- [Phonological Inventory](#phonological-inventory)
  - [Consonant Phonemes](#consonant-phonemes)
  - [Vowel / Final Phonemes](#vowel--final-phonemes)
  - [Tone Inventory](#tone-inventory)
  - [Cross-References](#cross-references)
- [Initials (声母 / Consonants)](#initials-声母--consonants)
  - [Initial Inventory](#initial-inventory)
  - [Zero Initial (零声母)](#zero-initial-零声母)
  - [Natural Classes](#natural-classes)
  - [Summary Notes](#summary-notes)
  - [Companion Files](#companion-files-1)
- [Vowels & Nuclei](#vowels--nuclei)
  - [Vowel System Overview](#vowel-system-overview)
  - [Nuclear Vowel Inventory](#nuclear-vowel-inventory)
  - [Per-Vowel Notes and Example Words](#per-vowel-notes-and-example-words)
  - [Medial Glides (介音 `jièyīn`) — `i`/`u`/`ü` (/j w ɥ/)](#medial-glides-介音-jièyīn--iuü-j-w-ɥ)
  - [Vowel Quality Is Determined WITHIN the Final](#vowel-quality-is-determined-within-the-final)
  - [普通话 `Pǔtōnghuà` vs 国语 `Guóyǔ` — Vowel-Relevant Differences](#普通话-pǔtōnghuà-vs-国语-guóyǔ--vowel-relevant-differences)
  - [IPA Symbol Summary](#ipa-symbol-summary)
- [Finals (韵母)](#finals-韵母)
  - [Final Structure: (medial) + nucleus + (coda)](#final-structure-medial--nucleus--coda)
  - [Spelling Conventions](#spelling-conventions)
  - [Finals by Group](#finals-by-group)
  - [Medial × Rime Combinatorics](#medial--rime-combinatorics)
  - [Erhua Rime Restructuring (儿化)](#erhua-rime-restructuring-儿化)
  - [Reference Standards](#reference-standards)
  - [Note: the Peshitta reader tiers are TONELESS](#note-the-peshitta-reader-tiers-are-toneless-1)
- [The Pinyin Syllable Chart (声母 × 韵母)](#the-pinyin-syllable-chart-声母--韵母)
  - [Syllable Inventory Counts](#syllable-inventory-counts)
  - [Romanization & Script Systems](#romanization--script-systems)
  - [Finals Used as Columns](#finals-used-as-columns)
  - [Finals Inventory (韵母)](#finals-inventory-韵母)
  - [Initials Inventory (声母)](#initials-inventory-声母)
  - [Co-occurrence Restrictions](#co-occurrence-restrictions)
  - [Phonology Notes](#phonology-notes)
  - [Secondary Standard Notes (Putonghua vs Guoyu)](#secondary-standard-notes-putonghua-vs-guoyu)
  - [Matrix Legend](#matrix-legend)
  - [Initial × Final Matrix (声母 × 韵母)](#initial--final-matrix-声母--韵母)
  - [Per-Row Phonetic & Example Notes](#per-row-phonetic--example-notes)
  - [Special Syllables](#special-syllables)
  - [Accent Notes (Putonghua vs Guoyu)](#accent-notes-putonghua-vs-guoyu)
  - [Unicode Reference](#unicode-reference)
  - [Cross-Reference](#cross-reference)
- [Tones & Suprasegmentals](#tones--suprasegmentals)
  - [Typological Summary](#typological-summary)
  - [Tones](#tones)
  - [Tone Sandhi](#tone-sandhi)
  - [Neutral-Tone Distribution](#neutral-tone-distribution)
  - [Erhua — 儿化 / 兒化 (*érhuà*)](#erhua--儿化--兒化-érhuà)
  - [Stress & Prominence](#stress--prominence)
  - [Intonation](#intonation)
  - [Pǔtōnghuà vs Guóyǔ Suprasegmental Differences](#pǔtōnghuà-vs-guóyǔ-suprasegmental-differences)
  - [The Reader Tiers Are Toneless](#the-reader-tiers-are-toneless)
  - [Comparison to Other Systems](#comparison-to-other-systems)
  - [Cross-References](#cross-references-1)
- [Syllable Structure](#syllable-structure)
  - [Reference Standards](#reference-standards-1)
  - [Components](#components)
  - [Phonotactics](#phonotactics)
  - [Syllable Types](#syllable-types)
  - [Syllabification](#syllabification)
  - [Loanword Adaptation](#loanword-adaptation)
  - [Constraints](#constraints)
- [Phonological Rules & Tone Sandhi](#phonological-rules--tone-sandhi)
  - [Rules at a Glance](#rules-at-a-glance)
  - [Rule 1: 三声变调 / 三聲變調 (`sānshēng biàndiào`) — third-tone sandhi (T3 + T3 → T2 + T3)](#rule-1-三声变调--三聲變調-sānshēng-biàndiào--third-tone-sandhi-t3--t3--t2--t3)
  - [Rule 2: 半三声 / 半三聲 (`bàn sānshēng`) — half-third tone (low non-rising allophone)](#rule-2-半三声--半三聲-bàn-sānshēng--half-third-tone-low-non-rising-allophone)
  - [Rule 3: 一字变调 / 一字變調 (`yī-zì biàndiào`) — tone sandhi of 一 `yī` ('one')](#rule-3-一字变调--一字變調-yī-zì-biàndiào--tone-sandhi-of-一-yī-one)
  - [Rule 4: 不字变调 / 不字變調 (`bù-zì biàndiào`) — tone sandhi of 不 `bù` ('not')](#rule-4-不字变调--不字變調-bù-zì-biàndiào--tone-sandhi-of-不-bù-not)
  - [Rule 5: 轻声 / 輕聲 (`qīngshēng`) — neutral-tone reduction](#rule-5-轻声--輕聲-qīngshēng--neutral-tone-reduction)
  - [Rule 6: 儿化 / 兒化 (`érhuà`) — rhotacization / erhua rime restructuring](#rule-6-儿化--兒化-érhuà--rhotacization--erhua-rime-restructuring)
  - [Rule 7: 尖团音的互补分布 / 尖團音的互補分佈 (`jiān-tuán yīn hùbǔ fēnbù`) — complementary distribution of `j/q/x` ~ `z/c/s` ~ `zh/ch/sh`](#rule-7-尖团音的互补分布--尖團音的互補分佈-jiān-tuán-yīn-hùbǔ-fēnbù--complementary-distribution-of-jqx--zcs--zhchsh)
  - [Rule 8: 卷舌音的实现 / 卷舌音的實現 (`juǎnshé yīn de shíxiàn`) — retroflex realization of `zh/ch/sh/r`](#rule-8-卷舌音的实现--卷舌音的實現-juǎnshé-yīn-de-shíxiàn--retroflex-realization-of-zhchshr)
  - [Rule 9: 去卷舌化 (`qù-juǎnshé huà`) — Taiwan de-retroflexion (`zh/ch/sh/r → z/c/s/-`)](#rule-9-去卷舌化-qù-juǎnshé-huà--taiwan-de-retroflexion-zhchshr--zcs-)
  - [Rule 10: `ü→u` 拼写规则 / 拼寫規則 (`ü→u pīnxiě guīzé`) — `ü`-to-`u` spelling after `j/q/x/y`](#rule-10-üu-拼写规则--拼寫規則-üu-pīnxiě-guīzé--ü-to-u-spelling-after-jqxy)
  - [Rule 11: 音节缩合 / 音節縮合 (`yīnjié suōhé`) — syllable contraction in fast speech](#rule-11-音节缩合--音節縮合-yīnjié-suōhé--syllable-contraction-in-fast-speech)
  - [Rule 12: 无连音 / 無連音 (`wú liányīn`) — absence of consonantal liaison](#rule-12-无连音--無連音-wú-liányīn--absence-of-consonantal-liaison)
  - [Rule 13: 鼻音韵尾的同化 / 鼻音韻尾的同化 (`bíyīn yùnwěi de tónghuà`) — coda-nasal place assimilation (gradient)](#rule-13-鼻音韵尾的同化--鼻音韻尾的同化-bíyīn-yùnwěi-de-tónghuà--coda-nasal-place-assimilation-gradient)
  - [Rule 14: 规则排序 / 規則排序 (`guīzé páixù`) — rule ordering of Mandarin sandhi processes](#rule-14-规则排序--規則排序-guīzé-páixù--rule-ordering-of-mandarin-sandhi-processes)
  - [Summary](#summary)
- [Pǔtōnghuà vs. Guóyǔ (Mainland vs. Taiwan Standard)](#pǔtōnghuà-vs-guóyǔ-mainland-vs-taiwan-standard)
  - [Reference standards](#reference-standards-2)
  - [Differences](#differences)
  - [Asides: the other major Sinitic branches (方言)](#asides-the-other-major-sinitic-branches-方言)
  - [Summary](#summary-1)
- [Orthography: Hanzi, Pinyin & Zhuyin](#orthography-hanzi-pinyin--zhuyin)
  - [General Principles](#general-principles)
  - [Hanzi (汉字 / 漢字)](#hanzi-汉字--漢字)
  - [Simplified vs Traditional](#simplified-vs-traditional)
  - [Pinyin (汉语拼音)](#pinyin-汉语拼音)
  - [Zhuyin / Bopomofo (注音符号 / 注音符號)](#zhuyin--bopomofo-注音符号--注音符號)
  - [Wade–Giles & Other Romanizations](#wadegiles--other-romanizations)
  - [Pinyin ↔ Zhuyin ↔ IPA Correspondence](#pinyin--zhuyin--ipa-correspondence)
  - [Sample Radicals](#sample-radicals)
  - [Reader Tiers (toneless by design)](#reader-tiers-toneless-by-design)
  - [Notes](#notes)
- [Connected Speech & Tone Sandhi](#connected-speech--tone-sandhi)
  - [Reference Standards](#reference-standards-3)
  - [Boundary Phenomena](#boundary-phenomena)
  - [Process Classification](#process-classification)
  - [Process Ordering](#process-ordering)
  - [Rate & Register](#rate--register)
  - [Dialect Variation (`普通话` vs `國語`)](#dialect-variation-普通话-vs-國語)
  - [Contrast with English](#contrast-with-english)
  - [Cross-Reference](#cross-reference-1)
- [Sample Words in IPA](#sample-words-in-ipa)
  - [How tone is written across the tiers](#how-tone-is-written-across-the-tiers)
  - [Sample Words Table](#sample-words-table)
  - [Per-word phenomena and notes](#per-word-phenomena-and-notes)
  - [Coverage Matrix](#coverage-matrix)
- [Unicode Reference](#unicode-reference-1)
  - [IPA Consonant Symbols](#ipa-consonant-symbols)
  - [IPA Vowel Symbols](#ipa-vowel-symbols)
  - [Tone Symbols](#tone-symbols)
  - [Bopomofo Characters (注音符號)](#bopomofo-characters-注音符號)
  - [Unicode Blocks Used](#unicode-blocks-used)
- [Cross-Reference to the Companion Guides](#cross-reference-to-the-companion-guides)
  - [Shared Framework](#shared-framework)
  - [Typological Contrasts](#typological-contrasts)
  - [Companion Guides](#companion-guides)
  - [Shared IPA Symbols](#shared-ipa-symbols)
  - [Reader Tiers](#reader-tiers)

## How to Read This Guide

This guide records pronunciation in the International Phonetic Alphabet (IPA, 2015 revision). A few conventions are used throughout.

### Phonemic vs phonetic notation

- **Phonemic transcription** is written between forward slashes: `/ /`. It records the contrastive sound categories (phonemes) of the language, abstracting away from predictable detail — e.g. the pinyin initial b is the unaspirated voiceless stop phoneme `/p/`, and zh is the retroflex affricate `/ʈʂ/`.
- **Phonetic transcription** is written between square brackets: `[ ]`. It records the actual realized sounds, including allophonic detail — e.g. the aspirated onset of p `[pʰ]`, the apical 'buzzed' vowel of zi `[tsɹ̩]` and zhi `[ʈʂɻ̩]`, and the rhotacized rime of erhua 花儿 huār `[xwɑɚ]`.

### How to read the IPA

- Consonants (INITIALS, 声母 / 聲母 shēngmǔ) are described by IPA **place of articulation** (bilabial, labiodental, alveolar/dental, retroflex, alveolo-palatal, velar, glottal), **manner of articulation** (plosive, affricate, fricative, nasal, lateral approximant), and — crucially — by **aspiration, NOT voicing**. Mandarin has NO voicing contrast in its obstruents; each stop/affricate pair contrasts UNASPIRATED vs ASPIRATED: b `/p/` vs p `/pʰ/`, d `/t/` vs t `/tʰ/`, g `/k/` vs k `/kʰ/`, z `/ts/` vs c `/tsʰ/`, zh `/ʈʂ/` vs ch `/ʈʂʰ/`, j `/tɕ/` vs q `/tɕʰ/`. The aspiration mark is `/ʰ/`. Pinyin b/d/g are voiceless and UNaspirated `[p t k]`, NOT voiced `[b d ɡ]`.
- Vowels and FINALS (韵母 / 韻母 yùnmǔ) have the structure (medial glide)(nucleus)(coda) and are described by **height** (close/mid/open), **backness** (front/central/back), **roundedness**, and **medial-glide onset** (open / i- / u- / ü-). The medials are i `/j/`, u `/w/`, ü `/ɥ/`; the only codas are the nasals `/n/`, `/ŋ/` (-ng) and the rhotic `/ɚ/` (er / erhua). The written final -i after the dental and retroflex series is an APICAL vowel marked with the syllabic under-ring, `[ɹ̩]` after z/c/s and `[ɻ̩]` after zh/ch/sh/r — NOT `[i]`.
- The organizing suprasegmental is **LEXICAL TONE, not stress and not pitch accent**, so no stress mark `ˈ` is used. Pitch is shown with IPA TONE LETTERS / Chao pitch values on a 5-point scale (1 = lowest, 5 = highest): T1 `˥` (55), T2 `˧˥` (35), T3 `˨˩˦` (214), T4 `˥˩` (51) — see the next subsection.

### The four tones, the neutral tone & tone notation

**Tone is contrastive and meaning-distinguishing.** Every full syllable carries one of four tones (or, when weak, the neutral tone), and tone alone distinguishes lexemes on an otherwise identical syllable — the classic five-way set mā / má / mǎ / mà / ma (妈/媽, 麻, 马/馬, 骂/罵, 吗/嗎) = 'mother / hemp / horse / scold / [question particle]'.

| Tone | Name | Chao value | IPA tone letter | Pinyin diacritic | Zhuyin mark | Example |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | 阴平 / 陰平 (yīnpíng), 'high level' | 55 | `˥` | macron (ā) | unmarked | mā 妈 / 媽 'mother' |
| T2 | 阳平 / 陽平 (yángpíng), 'rising' | 35 | `˧˥` | acute (á) | ˊ | má 麻 'hemp' |
| T3 | 上声 / 上聲 (shǎngshēng), 'low / dipping' | 214 | `˨˩˦` | caron / háček (ǎ) | ˇ | mǎ 马 / 馬 'horse' |
| T4 | 去声 / 去聲 (qùshēng), 'high falling' | 51 | `˥˩` | grave (à) | ˋ | mà 骂 / 罵 'scold' |
| neutral | 轻声 / 輕聲 (qīngshēng), 'neutral / light tone' | short; pitch set by the preceding tone | (no fixed contour) | unmarked | ˙ (before the syllable) | ma 吗 / 嗎 (question particle); 的 de, 了 le |

Four parallel notation systems are referenced throughout:

- **Pinyin diacritics** — a mark over the main vowel: ā á ǎ à (T1–T4); the neutral tone is unmarked. Encoded with precomposed vowels (ā U+0101, á U+00E1, ǎ U+01CE, à U+00E0, …) or base letter + combining marks (U+0304 macron, U+0301 acute, U+030C caron, U+0300 grave).
- **Tone numbers** — a trailing digit: ma1 ma2 ma3 ma4 and ma0 / ma5 (or nothing) for neutral — common in computational, dictionary and input contexts.
- **Zhuyin tone marks** — placed after (or, for the neutral tone, before) the Bopomofo syllable: T1 unmarked, T2 ˊ, T3 ˇ, T4 ˋ, neutral ˙.
- **Chao tone letters** — pitch on a 5-point scale (1 low … 5 high) as Chao digits or IPA tone letters: T1 = 55 `˥`, T2 = 35 `˧˥`, T3 = 214 `˨˩˦`, T4 = 51 `˥˩`.

**Tone is dynamic in connected speech.** The major sandhi rules — third-tone sandhi (T3 + T3 → T2 + T3, 你好 nǐ hǎo → ní hǎo; a non-final T3 surfaces as a low 'half-third'), the 一 yī alternation (yì before T1/T2/T3, yí before T4), the 不 bù alternation (bú before T4), plus neutral-tone (轻声) and erhua (儿化) effects — are documented in the dedicated tone and sandhi sections.

### The three scripts: Hanzi, Pinyin, Zhuyin (and Wade–Giles)

- **Hanzi** (汉字 / 漢字) is the primary, native, LOGOGRAPHIC / morphosyllabic script: each character writes one morpheme and almost always exactly one syllable + tone, giving a near one-to-one character ↔ syllable ↔ morpheme correspondence (马 / 馬 mǎ 'horse', 妈 / 媽 mā 'mother'). Characters are built from radicals (部首 bùshǒu) and are mostly 形声 / 形聲 phono-semantic compounds (semantic radical + phonetic component, e.g. 妈 / 媽 = 女 'woman' + 马 / 馬 mǎ phonetic), written with conventional stroke order (笔顺 / 筆順). Because the reading is not fully recoverable from the glyph and a character may have more than one reading (多音字, e.g. 行 háng 'row' vs xíng 'to go/OK'), pinyin or zhuyin annotation disambiguates.
- **Hanyu Pinyin** (汉语拼音 / 漢語拼音) is the official Latin-script romanization (1958; ISO 7098) and the deterministic phonetic spine of this guide. It spells each syllable as INITIAL + FINAL and marks the four tones with diacritics over the main vowel. Conventions: i after z/c/s/zh/ch/sh/r is the apical 'buzzed' vowel (not `[i]`); ü is written u after j/q/x/y (ju = jü); -iu, -ui, -un abbreviate -iou, -uei, -uen.
- **Zhuyin Fuhao / Bopomofo** (注音符號) is the native phonetic semi-syllabary (1918) standard in Taiwan for teaching, dictionary annotation and input. Its 37 symbols (nicknamed 'Bopomofo' after ㄅㄆㄇㄈ bo po mo fo) write initials, medials and finals — ㄓ zh `/ʈʂ/`, ㄐ j `/tɕ/`, ㄗ z `/ts/`; ㄚ a, ㄜ e `/ɤ/`, ㄢ an, ㄤ ang, ㄦ er. It is a faithful, one-to-one transcode of the same phonemic system as pinyin: 妈 / 媽 mā = ㄇㄚ, 马 / 馬 mǎ = ㄇㄚˇ; encoded in the Unicode Bopomofo block U+3100–U+312F.
- **Wade–Giles** (威妥瑪拼音 / 韦氏拼音) is the dominant pre-Pinyin Anglophone romanization, still seen in older scholarship and proper names (Taipei, Chiang Kai-shek). It marks ASPIRATION with an apostrophe (pinyin b/p = WG p/p', d/t = t/t', g/k = k/k'), renders pinyin zh/ch/sh = WG ch/ch'/sh and j/q/x = WG ch/ch'/hs (collapsing distinctions pinyin keeps), pinyin r = WG j, and marks tone with superscript numerals when shown at all (e.g. Pinyin Beijing = WG Pei-ching, Pinyin Qing = WG Ch'ing). IPA, not any romanization, is the authoritative pronunciation record here; the romanizations are provided for cross-referencing and read-back only.

### How the parallel Pǔtōnghuà / Guóyǔ standards & Simplified / Traditional are shown

Two co-equal reference standards are documented in parallel:

- **Pǔtōnghuà (普通话, PRC, PTH)** — Simplified characters (简体字), Hanyu Pinyin; keeps the full retroflex series and pervasive erhua and neutral tone.
- **Guóyǔ (國語, Taiwan, GUO)** — Traditional characters (繁體字), Zhuyin / Bopomofo; little/no erhua, frequent de-retroflexion (zh/ch/sh/r → z/c/s/-), fewer neutral tones.

Both standards SHARE one phonemic system — the same 21 initials + zero initial, the same ~35–38 finals, and the identical four lexical tones plus neutral tone — so the **toneless pinyin spelling of a syllable is the same in both**, and the **Simplified vs Traditional split is purely orthographic** (马 / 馬, 妈 / 媽, 国 / 國), changing neither the phonology nor the IPA. Where the two standards differ, both realizations are noted; their differences are SURFACE and LEXICAL — Guóyǔ's reduced erhua, frequent de-retroflexion, fewer neutral tones, and a handful of lexical tone/reading/word splits (垃圾 lājī vs lèsè, 和 hé vs hàn, 企 qǐ vs qì, 法 Fǎguó vs Fàguó). Throughout this guide Hanzi examples are given in both character sets where they differ (Simplified / Traditional, keyed Pǔtōnghuà → Simplified, Guóyǔ → Traditional).

### Note: the Peshitta reader tiers are TONELESS

The LANGUAGE is fully tonal and tone is documented richly above and throughout this guide. The downstream Peshitta READER TIERS, however, are **TONELESS BY DESIGN**, because the Peshitta source IPA carries no tone. The Pinyin and Zhuyin tiers are therefore stripped of all tone marks, and the Simplified and Traditional Hanzi tiers are **NON-FAITHFUL** transcription lookups: rendering a toneless source syllable as a Chinese character unavoidably imposes that character's citation tone and lexical meaning — an artifact of using tonal characters to transcribe toneless source material, NOT a feature of the Aramaic source.

## Phonological Inventory

The complete phonemic inventory of Standard Mandarin Chinese (标准汉语 / 標準漢語 *Biāozhǔn Hànyǔ*; ISO 639-3 `cmn`, macrolanguage `zho`; Sino-Tibetan › Sinitic), organized by IPA categories and presented through the traditional Chinese 声母/韵母/声调 (initial / final / tone) analysis that frames a **TONAL, ANALYTIC, one-morpheme-per-syllable** language. Documented in parallel for two reference standards: **普通话 / 普通話 *Pǔtōnghuà*** — PRC Standard Mandarin, Beijing-based phonology, written in SIMPLIFIED characters and romanized with Hanyu Pinyin (汉语拼音); and **国语 / 國語 *Guóyǔ*** — Taiwan Standard Mandarin, written in TRADITIONAL characters and taught with Zhuyin/Bopomofo (注音符号 / 注音符號).

The two standards share an essentially identical PHONEMIC system — the same initials, finals, and four-tone framework — and diverge chiefly in SURFACE and LEXICAL detail: Guoyu has little or no 儿化 ERHUA, frequent DE-RETROFLEXION (zh/ch/sh/r → z/c/s/-), fewer neutral tones, and scattered lexical tone or vocabulary differences (垃圾 `lèsè` vs `lājī`, 和 `hàn` vs `hé`, 企 `qì` vs `qǐ`); none of these change the toneless spelling.

The defining structural facts of the system are:

1. it is **TONAL**, with four lexical tones plus a neutral tone that are CONTRASTIVE on the syllable (mā/má/mǎ/mà 妈/麻/马/骂 = mother/hemp/horse/scold);
2. the obstruent contrast is **ASPIRATION, not voicing** (b/p = /p/ vs /pʰ/, not /b/ vs /p/);
3. there are **THREE parallel sibilant series** — dental z/c/s, retroflex zh/ch/sh, and alveolo-palatal j/q/x — the palatals standing in complementary distribution with the other two series and with g/k/h;
4. the syllable is rigidly **(C)(G)V(C)** with NO consonant clusters and only /n/, /ŋ/ (and rhotacized /ɚ/) as codas, giving ~400 toneless and ~1300 tone-bearing syllables in near one-to-one correspondence with morphemes and characters.

/slashes/ mark phonemes, [brackets] mark phonetic realizations. This object is a SUMMARY; exhaustive per-segment entries live in the separate **Consonants** (声母), **Vowels / Finals** (韵母), and tone (声调) material.

### Consonant Phonemes

The consonant phonemes of Standard Mandarin — the 21 initials (声母 *shēngmǔ*) plus the zero initial (零声母 *líng shēngmǔ*) — arranged by place and manner of articulation. The single most important fact is that Mandarin obstruents do NOT contrast in voicing the way English or Japanese do: the laryngeal contrast is **ASPIRATION** (unaspirated lenis vs aspirated fortis), so Pinyin `b d g z zh j` are voiceless UNASPIRATED [p t k ts ʈʂ tɕ] and `p t k c ch q` are voiceless ASPIRATED [pʰ tʰ kʰ tsʰ ʈʂʰ tɕʰ]. The inventory is shared between 普通话 Pǔtōnghuà and 国语 Guóyǔ; the surface differences are de-retroflexion of the zh/ch/sh/r series toward z/c/s in much Taiwan speech and the realization of `r-`.

**Total initial consonant phonemes:** 21 (+ zero initial)
The 21 initials: stops `b p d t g k` (6) + affricates `z c zh ch j q` (6) + fricatives `f s sh r x h` (6) + nasals `m n` (2) + lateral `l` (1) = 21. The **zero initial** (零声母) is the absence of an onset consonant before a vowel- or glide-initial syllable (爱 ài, 我 wǒ, 鱼/魚 yú) and is not itself a consonant. The velar nasal [ŋ] is NOT an initial (it occurs only as the coda `-ng`), so it is documented under the coda inventory, not here. Some analyses add a marginal initial [ŋ-] or [ɣ-] in dialectal/zero-initial onsets, but Standard Mandarin recognizes 21.

The three sibilant SERIES are the system's signature: dental `z c s` = /ts tsʰ s/, retroflex `zh ch sh r` = /ʈʂ ʈʂʰ ʂ ʐ~ɻ/, alveolo-palatal `j q x` = /tɕ tɕʰ ɕ/. **THE ASPIRATION CONTRAST:** `b/p`, `d/t`, `g/k`, `z/c`, `zh/ch`, `j/q` are unaspirated↔aspirated pairs, ALL voiceless — this is the chief L2 pitfall (English speakers hear b d g as 'voiced', but they are tenuis [p t k]). **COMPLEMENTARY DISTRIBUTION:** the palatals `j q x` occur ONLY before the high front vocoids `i` /i/ and `ü` /y/ (and their glides), exactly where the dentals `z c s`, retroflexes `zh ch sh`, and velars `g k h` do NOT occur before /i y/; historically j q x descend from both the g/k/h and z/c/s series, so they are often treated as positional allophones, but Pinyin and Zhuyin spell them as a distinct series.

#### IPA Consonant Chart

IPA chart of the 21 Mandarin INITIALS (rows = manner, columns = place of articulation). Where two symbols appear in an obstruent cell, the **UNASPIRATED member precedes the ASPIRATED member** (the Mandarin laryngeal contrast is aspiration, not voicing — both members are voiceless). The three sibilant series occupy the alveolar (dental z/c/s), retroflex (zh/ch/sh/r), and alveolo-palatal (j/q/x) columns. The chart is shared by 普通话 Pǔtōnghuà and 国语 Guóyǔ.

*Cell order: unaspirated → aspirated (both voiceless; aspiration is the contrast).*

| Manner | Bilabial | Labiodental | Alveolar | Retroflex | Alveolo-palatal | Velar |
|---|---|---|---|---|---|---|
| Stop | p pʰ |  | t tʰ |  |  | k kʰ |
| Affricate |  |  | ts tsʰ | ʈʂ ʈʂʰ | tɕ tɕʰ |  |
| Fricative |  | f | s | ʂ ʐ | ɕ | x |
| Nasal | m |  | n |  |  |  |
| Lateral |  |  | l |  |  |  |

**Medial glides (outside the chart — syllable on-glides, not initials):**

- `j` (medial `i` / `y-` — palatal on-glide: 也 yě [jɛ], 家 jiā [tɕja])
- `w` (medial `u` / `w-` — labio-velar on-glide: 我 wǒ [wo], 瓜 guā [kwa])
- `ɥ` (medial `ü` / `yu-` — labio-palatal on-glide: 月 yuè [ɥɛ], 全 quán [tɕʰɥɛn])

**Coda consonants (outside the chart):**

- `n` (coda `-n`: 安 ān [an], 但 dàn [tan])
- `ŋ` (coda `-ng`: 昂 áng [aŋ], 东/東 dōng [tʊŋ]) — the velar nasal occurs ONLY as a coda, never as an initial
- `ɚ` / `ɻ` (er 儿/兒 and 儿化 erhua rhotacization: 儿/兒 ér [ɚ], 花儿/花兒 huār)

*The laryngeal contrast lives WITHIN each stop and affricate cell as UNASPIRATED↔ASPIRATED (both voiceless): bilabial /p pʰ/, alveolar stops /t tʰ/ and affricates /ts tsʰ/, retroflex /ʈʂ ʈʂʰ/, alveolo-palatal /tɕ tɕʰ/, velar /k kʰ/ — there is NO /b d ɡ/ voicing series. The voiced member `r` /ʐ~ɻ/ appears only in the retroflex fricative cell (it is the lone 'voiced obstruent' initial). The medial glides /j w ɥ/ are syllable on-glides, not initials, and the velar nasal [ŋ] is a CODA only — both shown beneath the chart. PHONEME tally of initials: stops p pʰ t tʰ k kʰ (6) + affricates ts tsʰ ʈʂ ʈʂʰ tɕ tɕʰ (6) + fricatives f s ʂ ʐ ɕ x (6) + nasals m n (2) + lateral l (1) = 21, plus the zero initial. 普通话↔国语 share this chart; Taiwan Guoyu tends to merge the retroflex column into the alveolar column (de-retroflexion) at the surface.*

#### Notes by Place of Articulation

- **Bilabial** — `b p m` /p pʰ m/. The bilabial stops contrast in ASPIRATION, not voicing: `b` /p/ is voiceless UNASPIRATED (爸/爸 bà 'dad', 八 bā 'eight') and `p` /pʰ/ is voiceless ASPIRATED (怕 pà 'fear', 拍 pāi 'clap') — minimal pair 爸 bà /pa/ vs 怕 pà /pʰa/. Both are tenuis/fortis, NOT the /b/~/p/ voicing contrast of European languages. The bilabial nasal `m` /m/ (妈/媽 mā 'mother', 们/們 men plural suffix) is the only voiced bilabial. The labiodental fricative `f` /f/ is listed under labiodental, and the medial glide `u` /w/ (with bilabial rounding) under the glides row.
- **Labiodental** — `f` /f/. The single labiodental, a voiceless labiodental fricative (飞/飛 fēi 'fly', 饭/飯 fàn 'rice/meal', 风/風 fēng 'wind'). Mandarin has NO /v/, so there is no labiodental voicing pair; `f` never combines with the `i` /j/ or `ü` /ɥ/ medials. Historically Mandarin `f` derives from earlier labial stops before back/rounded finals, which is why it never co-occurs with the high front medials.
- **Alveolar** — `d t z c s n l` /t tʰ ts tsʰ s n l/. The densest place of articulation, holding both the alveolar stops and the DENTAL sibilant series. Stops: `d` /t/ unaspirated (大 dà 'big', 东/東 dōng 'east'), `t` /tʰ/ aspirated (他/他 tā 'he', 天 tiān 'sky') — pair 大 dà /ta/ vs 他 tā /tʰa/. Dental sibilants (the z/c/s series): affricates `z` /ts/ unaspirated (字 zì 'character', 早 zǎo 'early') and `c` /tsʰ/ aspirated (词/詞 cí 'word', 草 cǎo 'grass'), plus fricative `s` /s/ (四 sì 'four', 三 sān 'three'). Before the apical vowel written `-i` these give `zi ci si` = [tsɹ̩ tsʰɹ̩ sɹ̩] (字 zì [tsɹ̩˥˩]). `n` /n/ (你 nǐ 'you', 南 nán 'south') is both an initial AND the coda `-n`; `l` /l/ (来/來 lái 'come', 六 liù 'six') is the only lateral. The dental series never occurs before /i y/ (that environment belongs to the palatals j q x), so `z c s` + 'i' always means the apical [ɹ̩], never [i].
- **Retroflex** — `zh ch sh r` /ʈʂ ʈʂʰ ʂ ʐ~ɻ/. The retroflex series, made with the tongue tip curled back toward the post-alveolar/retroflex region — a hallmark of northern Mandarin. Affricates: `zh` /ʈʂ/ unaspirated (知 zhī 'know', 中 zhōng 'middle/China') and `ch` /ʈʂʰ/ aspirated (吃 chī 'eat', 茶 chá 'tea'); fricative `sh` /ʂ/ (是 shì 'to be', 山 shān 'mountain'); and the VOICED member `r` /ʐ~ɻ/ (日 rì 'sun/day', 人 rén 'person'), ranging from a voiced retroflex fricative [ʐ] to a retroflex approximant [ɻ]. Before the apical vowel written `-i` these give `zhi chi shi ri` = [ʈʂɻ̩ ʈʂʰɻ̩ ʂɻ̩ ʐɻ̩] (是 shì [ʂɻ̩˥˩], 日 rì [ʐɻ̩˥˩]). **普通话↔国语:** this is the series most affected by Taiwan DE-RETROFLEXION, where `zh ch sh` tend toward `z c s` [ts tsʰ s] and `r` weakens; the contrast 四 sì /sɹ̩/ vs 十/十 shí /ʂɻ̩/ may neutralize in casual Guoyu. Standard 普通话 keeps the retroflex/dental contrast fully phonemic.
- **Alveolo-palatal** — `j q x` /tɕ tɕʰ ɕ/. Articulated with the tongue blade at the alveolo-palatal region: affricates `j` /tɕ/ unaspirated (鸡/雞 jī 'chicken', 家 jiā 'home/family') and `q` /tɕʰ/ aspirated (七 qī 'seven', 去 qù 'go'); fricative `x` /ɕ/ (西 xī 'west', 谢/謝 xiè 'thank'). **CRITICAL DISTRIBUTION:** `j q x` occur ONLY before the high front vocoids `i` /i/ and `ü` /y/ and their glides /j ɥ/ — precisely the slot where g/k/h, z/c/s, and zh/ch/sh do NOT appear before /i y/. Because of this complementary distribution they are often analyzed as positional allophones of the velar and/or dental series (and historically arose from palatalization of both), but Pinyin and Zhuyin treat them as a separate series. **Spelling note:** after `j q x` (and `y`), Pinyin writes the `ü` vowel as plain `u` (居 jū = /tɕy/, 去 qù = /tɕʰy/, 需 xū = /ɕy/), since /u/ never follows these initials — no ambiguity arises. This series is shared identically by 普通话 and 国语.
- **Velar** — `g k h` /k kʰ x/. Velar stops contrast in aspiration: `g` /k/ unaspirated (高 gāo 'tall', 国/國 guó 'country') and `k` /kʰ/ aspirated (开/開 kāi 'open', 看 kàn 'look') — minimal pair 干 gàn /kan/ 'to do' (same form in simplified and traditional) vs 看 kàn /kʰan/ 'look'. The velar fricative `h` /x/ (好 hǎo 'good', 喝 hē 'drink', 黑 hēi 'black') is a voiceless VELAR (sometimes uvular [χ]) fricative — NOT the English glottal [h]; it has audible velar friction (好 [xau˨˩˦]). Like the dental and retroflex series, `g k h` never occur before the high front vocoids /i y/ — that environment is filled by the palatals j q x, with which g k h are historically and distributionally linked. There is NO velar nasal INITIAL: the velar nasal [ŋ] of Mandarin appears only as the coda `-ng` (see coda inventory).
- **Glides / medials** — `i/y-` /j/, `u/w-` /w/, `ü/yu-` /ɥ/. The three medial GLIDES are not initials but on-glides of the final; they are listed for completeness because they pattern with the consonants in syllable onset. `i` /j/ (palatal, 家 jiā [tɕja], 也 yě [jɛ]); `u` /w/ (labio-velar/rounded, 瓜 guā [kwa], 我 wǒ [wo]); `ü` /ɥ/ (labio-palatal rounded, 月 yuè [ɥɛ], 全 quán [tɕʰɥɛn]). In the zero-initial syllable these glides are spelled `y-` and `w-` (也 yě, 我 wǒ, 鱼/魚 yú) — orthographic, not a separate phoneme. The glides are the medial slot of the (C)(G)V(C) syllable and combine with nuclei to build the rising diphthongs and the bulk of the finals; full detail is in the **Finals** section.

### Vowel / Final Phonemes

The vowel/FINAL inventory of Standard Mandarin. Mandarin finals (韵母 *yùnmǔ*) have the structure (medial glide)(nucleus)(coda); this object summarizes the underlying vowel phonemes — the nuclei, the medial glides, the special APICAL vowels written `-i`, the rhotacized er/erhua vowel, and the coda inventory — while the full ~35–38 finals (diphthongs, triphthongs, nasal finals, erhua rimes) are enumerated in the separate **Finals** section. The vowel system is famously hard to phonemicize because surface vowel quality is heavily conditioned by the surrounding medial and coda; a common analysis posits a small set of underlying nuclei whose allophones fill the vowel space. The two reference standards share this vowel/final framework; 国语 Guóyǔ differs mainly in the near-absence of erhua and in some lexical finals, not in the underlying system.

**Nucleus count:** 7 | **Medial count:** 3
Underlying NUCLEI (commonly given as ~5–7): `a` /a/, `o` /o/, `e` /ɤ/, `ê` /ɛ/, plus the high vocoids `i` /i/, `u` /u/, `ü` /y/ which double as nuclei and as medial glides — here counted as 7 nucleus qualities (a o ɤ ɛ i u y). MEDIAL glides: `i` /j/, `u` /w/, `ü` /ɥ/ = 3. SPECIAL apical vowels: the syllabic [ɹ̩] (after z c s) and [ɻ̩] (after zh ch sh r), both written `-i` in Pinyin, plus the rhotic `er` /ɚ/. Reductive analyses collapse the nuclei to as few as two underlying vowels (/a/ and /ə/) whose realizations are derived by rule; the surface tally of ~35–38 finals is what learners actually use. Codas: /n/, /ŋ/, and the rhotic /ɚ/.

**NUCLEI:** `a` /a/ (low central; surfaces as [a]~[ɑ]~[ɛ]~[æ] by context — 八 bā [pa], 安 ān [an], 昂 áng [ɑŋ]); `o` /o/ (mid back rounded, mainly after labials and in -uo/-ong — 波 bō [pwo], 我 wǒ [wo]); `e` /ɤ/ (close-mid back UNROUNDED, the 'schwa-ish' nucleus of 饿/餓 è [ɤ], 哥 gē [kɤ]); `ê` /ɛ/ (open-mid front, surfaces in ie/üe and the rare standalone 欸/誒 ê — 谢/謝 xiè [ɕjɛ], 月 yuè [ɥɛ]); and the high `i` /i/ (西 xī [ɕi]), `u` /u/ (五 wǔ [u]), `ü` /y/ (鱼/魚 yú [y], the high front ROUNDED vowel, a major L2 difficulty).

**THE APICAL ('buzzed') VOWELS:** the letter `-i` after a sibilant initial is NOT [i] but a syllabic continuation of the sibilant — [ɹ̩] (apical/dental, after z c s: 字 zì [tsɹ̩˥˩], 四 sì [sɹ̩˥˩]) and [ɻ̩] (apical/retroflex, after zh ch sh r: 知 zhī [ʈʂɻ̩˥], 日 rì [ʐɻ̩˥˩]); these are the most language-specific vowels in the system and never occur elsewhere.

**THE RHOTIC er** /ɚ/ (儿/兒 ér [ɚ], 二 èr [ɚ˥˩], 耳 ěr [ɚ˨˩˦]): a rhotacized central vowel that forms its own syllable and also drives 儿化 ERHUA, in which a suffixal `-r` fuses with and restructures the preceding final (花 huā → 花儿/花兒 huār, 一点/一點 yìdiǎn → 一点儿/一點兒 yìdiǎnr).

**CODA inventory:** only the nasals /n/ (`-n`: 安 ān, 但 dàn) and /ŋ/ (`-ng`: 昂 áng, 东/東 dōng [tʊŋ]) plus the rhotic /ɚ/ — there are NO obstruent codas (no /p t k/), no /m/ coda, and no consonant clusters anywhere.

**FALLING DIPHTHONGS:** `ai` /aɪ/ (爱/愛 ài), `ei` /eɪ/ (黑 hēi), `ao` /aʊ/ (好 hǎo), `ou` /oʊ/ (走 zǒu); rising and triphthong rimes (ia ie ua uo üe, iao iou/-iu uai uei/-ui) are built with the medials.

**普通话↔国语:** same underlying vowels and finals; Guoyu drops erhua almost entirely (so the er/erhua rimes are marginal there) and has minor lexical final differences.

#### IPA Vowel Chart

IPA vowel space for the Standard Mandarin nuclei and high vocoids (rows = height, columns = backness/rounding). Because Mandarin vowel quality is strongly allophonic — conditioned by the medial and coda — this chart shows the canonical/citation qualities of the underlying nuclei plus the three high vowels that also serve as medial glides. The two APICAL syllabic vowels [ɹ̩ ɻ̩] and the rhotic [ɚ] are listed separately beneath the chart because they do not sit on the ordinary vowel quadrilateral. The same vowel space underlies 普通话 and 国语.

| Height | Front (unrounded) | Front (rounded) | Central | Back (unrounded) | Back (rounded) |
|---|---|---|---|---|---|
| close | i | y |  |  | u |
| close-mid |  |  |  | ɤ | o |
| open-mid | ɛ |  |  |  |  |
| open |  |  | a |  |  |

**Apical & rhotic vowels (outside the quadrilateral):**

- `ɹ̩` — apical/dental syllabic vowel, the `-i` after z c s (字 zì [tsɹ̩], 四 sì [sɹ̩])
- `ɻ̩` — apical/retroflex syllabic vowel, the `-i` after zh ch sh r (知 zhī [ʈʂɻ̩], 日 rì [ʐɻ̩])
- `ɚ` — rhotacized central vowel, er 儿/兒 (儿/兒 ér [ɚ], 二 èr [ɚ]) and the 儿化 erhua coda

*By height: CLOSE — `i` /i/ (front unrounded, 西 xī [ɕi]), `ü` /y/ (front ROUNDED, 鱼/魚 yú [y] — the typological standout, a high front rounded vowel absent from English/Japanese), `u` /u/ (back rounded, 五 wǔ [u]); CLOSE-MID — `e` /ɤ/ (back UNROUNDED, 哥 gē [kɤ], 饿/餓 è [ɤ]) and `o` /o/ (back rounded, 波 bō [pwo]); OPEN-MID — `ê` /ɛ/ (front, in ie/üe: 谢/謝 xiè [ɕjɛ], 月 yuè [ɥɛ]); OPEN — `a` /a/ (low central, ranging [a]~[ɑ]~[æ] by context: 八 bā [pa], 安 ān [an], 昂 áng [ɑŋ]). The three high vowels i u ü double as the MEDIAL glides /j w ɥ/. STRONG ALLOPHONY: the nuclei have wide context-driven ranges (a fronts to [ɛ]/[æ] before -n/-i and backs to [ɑ] before -ng; e is [ɤ] in open syllables but [ə] in en/eng and [e] in ei). OUTSIDE THE QUADRILATERAL: the two APICAL syllabic vowels [ɹ̩] (after z c s) and [ɻ̩] (after zh ch sh r), which are sustained voicings of the preceding sibilant rather than ordinary vowels, and the RHOTIC [ɚ] of er/erhua, a rhotacized central vowel. There are NO reduced/centralized vowels in stressed syllables (unlike English schwa); vowels reduce only under the neutral tone (轻声/輕聲). 普通话↔国语 share this vowel space; the chief difference is that Guoyu rarely uses erhua, so [ɚ]/erhua rimes are marginal in Taiwan speech.*

#### Underlying Vowel / Nucleus Inventory

| Pinyin | Phoneme | Height | Backness | Rounding | Examples (简 / 繁) | Notes |
|---|---|---|---|---|---|---|
| `a` | /a/ | open | central | unrounded | 八 bā, 安 ān, 昂 áng | Low central; surfaces [a]~[ɑ]~[ɛ]~[æ] by context (fronts before `-n`/`-i`, backs to [ɑ] before `-ng`). |
| `o` | /o/ | close-mid | back | rounded | 波 bō, 我 wǒ | Mid back rounded; mainly after labials and in `-uo`/`-ong`. |
| `e` | /ɤ/ | close-mid | back | unrounded | 饿 / 餓 è, 哥 gē | The 'schwa-ish' back UNROUNDED nucleus; [ə] in en/eng, [e] in ei. |
| `ê` | /ɛ/ | open-mid | front | unrounded | 谢 / 謝 xiè, 月 yuè | Open-mid front; surfaces in `ie`/`üe` and the rare standalone 欸 / 誒 ê. |
| `i` | /i/ | close | front | unrounded | 西 xī, 鸡 / 雞 jī | High front unrounded; also the medial glide /j/. |
| `u` | /u/ | close | back | rounded | 五 wǔ, 不 bù | High back rounded; also the medial glide /w/. |
| `ü` | /y/ | close | front | rounded | 鱼 / 魚 yú, 绿 / 綠 lǜ | High front ROUNDED — the typological standout, absent from English/Japanese; also the medial glide /ɥ/. |

#### Special (Apical & Rhotic) Vowels

| Symbol | Type | Environment | Examples (简 / 繁) | Notes |
|---|---|---|---|---|
| `[ɹ̩]` | apical/dental syllabic | written `-i` after z c s | 字 zì [tsɹ̩˥˩], 四 sì [sɹ̩˥˩] | A sustained voicing of the preceding dental sibilant, NOT [i]; occurs nowhere else. |
| `[ɻ̩]` | apical/retroflex syllabic | written `-i` after zh ch sh r | 知 zhī [ʈʂɻ̩˥], 日 rì [ʐɻ̩˥˩] | A sustained voicing of the preceding retroflex sibilant, NOT [i]; occurs nowhere else. |
| `/ɚ/` | rhotacized central vowel | standalone `er` and 儿化 erhua | 儿 / 兒 ér [ɚ], 二 èr [ɚ˥˩], 耳 ěr [ɚ˨˩˦] | Forms its own syllable and drives 儿化 erhua (花 → 花儿 / 花兒 huār). Marginal in 国语 Guóyǔ. |

#### Coda Inventory

| Coda | Phoneme | Pinyin | Examples (简 / 繁) | Notes |
|---|---|---|---|---|
| nasal | /n/ | `-n` | 安 ān [an], 但 dàn [tan] | Alveolar nasal coda. |
| nasal | /ŋ/ | `-ng` | 昂 áng [aŋ], 东 / 東 dōng [tʊŋ] | Velar nasal; CODA only, never an initial. |
| rhotic | /ɚ/ | `-r` (儿化) | 花儿 / 花兒 huār, 一点儿 / 一點兒 yìdiǎnr | The erhua rhotacizing coda. |

*There are NO obstruent codas (no /p t k/), no /m/ coda, and no consonant clusters anywhere — the defining phonotactic restriction that forces epenthesis or substitution when rendering Aramaic.*

### Tone Inventory

The **TONES** (声调/聲調 *shēngdiào*) of Standard Mandarin — the system's defining suprasegmental feature and the property that makes it a TONAL language. Mandarin has **FOUR lexical tones plus a NEUTRAL tone**; tone is LEXICAL and CONTRASTIVE, distinguishing otherwise identical syllables (mā/má/mǎ/mà 妈/麻/马/骂 = mother/hemp/horse/scold; mā/má/mǎ/mà 媽/麻/馬/罵 in traditional). Contour is described with Chao tone-letter pitch numbers (1 = lowest, 5 = highest).

**Lexical tone count:** 4 | **Total with neutral:** 5
**Pitch-number convention:** Chao tone letters, 1 (lowest) to 5 (highest); a contour is written as a sequence (e.g. 35 = mid-rising). IPA tone-letter diacritics shown alongside (˥ ˧˥ ˨˩˦ ˥˩).

> **IMPORTANT:** tones are a property of the **LANGUAGE** and are documented fully here; the Chinese Peshitta **READER TIERS are toneless by design** — the toneless Pinyin / Zhuyin / Hanzi tiers carry NO tone because the Peshitta source IPA is toneless (see **Cross-References**).

| # | Name (拼音) | Name (汉字 简 / 繁) | Gloss | Contour | IPA tone letter | Pinyin diacritic | Zhuyin mark | Example (拼音) | Example (简) | Example (繁) | Meaning |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **T1** | yīnpíng | 阴平 / 陰平 | high level | `55` | `˥` | `ˉ` (macron: ā ē ī ō ū ǖ) | unmarked (no tone mark) | `mā` | 妈 | 媽 | mother |
| **T2** | yángpíng | 阳平 / 陽平 | rising | `35` | `˧˥` | `ˊ` (acute: á é í ó ú ǘ) | `ˊ` | `má` | 麻 | 麻 | hemp |
| **T3** | shǎngshēng | 上声 / 上聲 | low dipping (falling–rising) | `214` | `˨˩˦` | `ˇ` (caron/háček: ǎ ě ǐ ǒ ǔ ǚ) | `ˇ` | `mǎ` | 马 | 馬 | horse |
| **T4** | qùshēng | 去声 / 去聲 | high falling | `51` | `˥˩` | `ˋ` (grave: à è ì ò ù ǜ) | `ˋ` | `mà` | 骂 | 罵 | scold |
| **T0** | qīngshēng | 轻声 / 輕聲 | neutral (light) tone | variable (pitch set by preceding tone; short and unstressed) | (no fixed contour) | unmarked (sometimes a leading dot ·) | `˙` (dot, written before the syllable) | `ma` | 吗 | 嗎 | question particle |

**Per-tone notes:**

- **T1 阴平 / 陰平** — High and level, held near the top of the pitch range: mā [ma˥]. Pinyin marks it with a macron; Zhuyin leaves T1 unmarked (the bare syllable).
- **T2 阳平 / 陽平** — Mid-rising, from mid to high: má [ma˧˥]. The output of 3rd-tone sandhi (T3+T3 → T2+T3) and of 一/不 sandhi is a T2-like rise.
- **T3 上声 / 上聲** — Low dipping: starts mid-low, dips to the bottom, then rises — mǎ [ma˨˩˦]. In connected speech a NON-FINAL T3 is usually a 'half-third' (low [21], no final rise), and T3+T3 undergoes SANDHI to T2+T3 (你好/你好 nǐ hǎo → ní hǎo). The full 214 contour appears mainly in citation/utterance-final position.
- **T4 去声 / 去聲** — High falling, from the top sharply to the bottom: mà [ma˥˩]. 一 yī → yí and 不 bù → bú before a following T4 (一定/一定 yídìng, 不是 búshì).
- **T0 轻声 / 輕聲** — Short, light, unstressed, with no inherent contour — its pitch is determined by the preceding syllable's tone (e.g. mid-low after T1, low after T2/T4, half-high after T3). Borne by grammatical particles (的 de, 了 le, 吗/嗎 ma, 呢 ne), reduplication, and some suffixes (子 zi, 头/頭 tou); it also reduces the vowel. Often listed as a fifth tone but is better described as the ABSENCE of a lexical tone. 国语 Guóyǔ uses neutral tone less often than 普通话, frequently keeping the full lexical tone (e.g. 东西/東西 'thing' 普 dōngxi vs 国 dōngxī).

**Contrastive minimal sets:** the four-way set mā/má/mǎ/mà (妈/麻/马/骂 — 媽/麻/馬/罵) is the canonical demonstration, as is yī 一 'one', yí 姨 'aunt', yǐ 椅 'chair', yì 亿/億 'hundred million'.

**Notation:** PINYIN marks tone with a diacritic over the main vowel (ā á ǎ à, ē é ě è, etc.; neutral = unmarked); ZHUYIN/BOPOMOFO marks T2 `ˊ`, T3 `ˇ`, T4 `ˋ` after the syllable, leaves T1 unmarked, and writes the neutral tone with a leading dot `˙`.

**Key connected-speech rules** (summarized; full detail in the tone / connected-speech material):

1. **3rd-tone sandhi** T3+T3 → T2+T3 (你好/你好 nǐ hǎo → ní hǎo), and non-final T3 → half-third [21];
2. **一 yī** → yì before T1/T2/T3 and → yí before T4; **不 bù** → bú before T4;
3. the **neutral tone** takes its pitch from context and shortens/reduces the syllable;
4. **ERHUA 儿化** rhotacizes the final and can restructure the rime.

**普通话↔国语:** the four-tone framework and pitch contours are essentially shared, but Guoyu has FEWER neutral tones, little/no erhua, and some LEXICAL tone differences (垃圾 'rubbish' 普 `lājī` vs 国 `lèsè`; 企 'enterprise' 普 `qǐ-` vs 国 `qì-`; 和 'and' 普 `hé` vs 国 `hàn`).

> **CRITICAL FRAMING:** tones fully characterize the LANGUAGE and are documented richly here, but the Chinese Peshitta's TONELESS PINYIN / ZHUYIN / HANZI reader tiers carry NO tone, because the Peshitta source IPA is toneless; any citation tone that appears on a Hanzi reader glyph is an artifact of the character, not a feature of the source (see Cross-References).

### Cross-References

This section is a SUMMARY of the inventory. Per-segment articulatory detail, allophony, and example words for each initial and final are given in the **Consonants** and **Finals** sections; the four tones, the neutral tone, and all TONE SANDHI (3rd-tone sandhi, 一/不 sandhi, half-third) are detailed in the tone material, with connected-speech processes (neutral-tone reduction, 儿化 erhua rime restructuring, tone-3 chains) in **Connected Speech and Tone Sandhi**. The legal syllable shape (C)(G)V(C), the ~400 toneless / ~1300 tone-bearing syllable inventory, the medial+nucleus+coda final structure, the complementary distribution of j q x with z c s / zh ch sh / g k h, and the apical-vowel and coda restrictions are covered in **Syllable Structure**. The romanization and script systems — Hanyu Pinyin (汉语拼音/漢語拼音), Zhuyin/Bopomofo (注音符号/注音符號), the Hanzi writing system in SIMPLIFIED (简体字) and TRADITIONAL (繁體字) forms, radicals/部首 and 形声/形聲 phonetic-semantic compounds, plus Wade–Giles and Gwoyeu Romatzyh — are handled in the **Orthography** and **Unicode Reference** sections (CJK Unified Ideographs `U+4E00`–`U+9FFF`, Bopomofo `U+3100`–`U+312F`, Pinyin combining/precomposed tone vowels). The 普通话 Pǔtōnghuà ↔ 国语 Guóyǔ contrasts (de-retroflexion, erhua absence, neutral-tone frequency, lexical differences) recur throughout.

**Companion files** (repo-relative):

- `Chinese/chinese_pronunciation_guide.md`
- `Chinese/Peshita_Chinese/Pinyin/`
- `Chinese/Peshita_Chinese/Zhuyin/`
- `Chinese/Peshita_Chinese/Hanzi_Simplified/`
- `Chinese/Peshita_Chinese/Hanzi_Traditional/`

**Reader tiers:** the Chinese Peshitta ships SIX reader tiers — **Scholarly** and **Pretty** (language-neutral Latin), **TONELESS PINYIN** (the deterministic phonetic spine), **ZHUYIN/BOPOMOFO** (a transcode of the toneless pinyin), and **HANZI** in **SIMPLIFIED** (简体字) and **TRADITIONAL** (繁體字) (a downstream transcription-character lookup) — which present the segments catalogued here at increasing levels of script-specificity. The reader tiers are TONELESS because the Peshitta source IPA carries NO tone; the Hanzi tiers unavoidably impose a citation tone per character (an artifact, not a source feature). Because Mandarin syllables are rigidly (C)(G)V(C) with no clusters and only /n ŋ ɚ/ codas, rendering Aramaic into these tiers requires mapping each foreign consonant onto a legal Mandarin syllable, with epenthesis or substitution where Aramaic sounds (e.g. /b d ɡ v z ʕ ħ q/) have no Mandarin counterpart.

---

*Guide maintained by Shin.*

## Initials (声母 / Consonants)

The INITIALS (声母 *shēngmǔ*) of Standard Mandarin Chinese (标准汉语 / 標準漢語), documented in parallel for the two reference standards of the spoken language: 普通话 *Pǔtōnghuà* (PRC Standard Mandarin, Beijing-based phonology, written here with SIMPLIFIED characters and Hanyu Pinyin) and 國語 *Guóyǔ* (Taiwan Standard Mandarin, written with TRADITIONAL characters and glossed in Zhuyin/Bopomofo). Mandarin has 21 consonantal initials plus the ZERO INITIAL (零声母, a syllable with no onset consonant).

The single most important fact about this system — and the way it differs fundamentally from English, Aramaic and even Japanese — is that the obstruent contrast is **ASPIRATION, NOT VOICING**: Mandarin has NO phonemic voiced stops or affricates (no /b d ɡ dʒ/ as in English). The Pinyin letters `b d g j z zh` stand for VOICELESS UNASPIRATED [p t k tɕ ts ʈʂ], and `p t k q c ch` stand for their VOICELESS ASPIRATED partners [pʰ tʰ kʰ tɕʰ tsʰ ʈʂʰ]; the only phonemically voiced obstruent is `r` [ʐ~ɻ].

A second defining fact is the **THREE PARALLEL SIBILANT SERIES** that share the same affricate+fricative shape at three places of articulation — DENTAL `z c s` [ts tsʰ s], RETROFLEX `zh ch sh r` [ʈʂ ʈʂʰ ʂ ʐ], and ALVEOLO-PALATAL `j q x` [tɕ tɕʰ ɕ] — where the palatal series `j q x` is in strict COMPLEMENTARY DISTRIBUTION with `z c s`, `zh ch sh` and `g k h`, appearing only before the high front vowels `i` [i] and `ü` [y]. Phonemic values are given in /slashes/ and surface realisations in [brackets], following the IPA (2015 revision). The two reference standards share the same phonemic inventory; they differ mainly in surface realisation — most notably Taiwan Guóyǔ's widespread DE-RETROFLEXION (zh ch sh r → z c s / loss), recorded per-initial in the allophony notes.

> **Note on the LANGUAGE vs the READER TIERS.** Mandarin is a TONAL language and tones are rendered fully throughout this guide (see *Suprasegmentals / Tones*). The initials themselves carry no tone, but the example syllables below show tone marks. The toneless Pinyin SPINE used by the Peshitta reader tiers is unchanged by tone or by the Guóyǔ surface variants: the underlying initial inventory of both 普通话 and 國語 is identical, and where the reader tiers are TONELESS the initial chart still applies exactly.

**Consonantal initials:** 21 | **Effective onset phonemes:** 21 (+ zero initial)

The 21 consonantal INITIALS (声母 *shēngmǔ*) are the standard count for Pinyin/Zhuyin pedagogy: stops `b p d t g k` (6), affricates `z c zh ch j q` (6), fricatives `f s sh r x h` (6), nasals `m n` (2), and lateral `l` (1). The ZERO INITIAL (零声母 *líng shēngmǔ*) — a syllable that begins directly with a vowel or glide, e.g. 爱 *ài*, 我 *wǒ*, 鱼 *yú* — is documented separately below as the 22nd onset slot rather than counted among the 21 consonants.

Note that `j q x`, `z c s`, `zh ch sh` and `g k h` do NOT all contrast in the same environment: `j q x` occur ONLY before `i`/`ü`, while `z c s` / `zh ch sh` / `g k h` occur ONLY before non-front vowels, so the surface 21 reduce to fewer underlying contrasts under a complementary-distribution analysis.

**On the effective count.** The 21 initials map essentially one-to-one onto Pinyin onset spellings (`b`→[p], `p`→[pʰ], `zh`→[ʈʂ], etc.), so at the level of the toneless Pinyin SPINE the consonant inventory is exactly these 21 onsets plus the zero initial. Under a tighter PHONEMIC analysis the count drops, because `j q x` are in complementary distribution with both `z c s` and `g k h` (and with `zh ch sh`) — `j`/`q`/`x` never contrast with them in the same slot — so several scholars treat `j q x` as positional variants and reach an underlying count nearer **19**. Conversely, because the syllable canon is so tight (only /n ŋ/ and the rhotic /ɚ/ may close a syllable, and there are no consonant clusters), each of the ~400 toneless syllables is uniquely an (initial)(glide)(nucleus)(coda) string, and the 21-initial chart, the Zhuyin onset letters ㄅㄆㄇㄈ…, and the Hanyu-Pinyin onset spellings are three notations for the same 21 units. This effective inventory is shared by 普通话 Pǔtōnghuà and 國語 Guóyǔ.

### Initial Inventory

The 21 consonantal initials with their Pinyin spelling, Zhuyin (Bopomofo) glyph, phonemic IPA value, name, place / manner / aspiration / voicing, example words (with simplified + traditional 汉字, Pinyin, IPA, gloss), and allophony notes.

| # | Pinyin | Zhuyin | IPA | Name | Place | Manner | Asp. | Voicing | Example Words | Allophony Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `b` | `ㄅ` | `/p/` | b ㄅ — voiceless unaspirated bilabial stop | bilabial | stop | unasp. | voiceless | 爸爸 / 爸爸 `bàba` [pâ.pa] "father, dad"; 北 / 北 `běi` [peɪ] "north"; 不 / 不 `bù` [pu] "not, no" | VOICELESS UNASPIRATED [p] — like the *p* of English 'spin', NOT the *b* of 'bin' (voiced) and NOT the aspirated *p* of 'pin'. English learners habitually voice it; the correct target has no vocal-fold vibration before release and no aspiration after. Contrasts with `p` [pʰ] by aspiration only (北 *běi* [peɪ] vs 配 *pèi* [pʰeɪ]). Occurs before any vowel except the `ü`-finals reserved for `j q x`. Identical in Pǔtōnghuà and Guóyǔ. |
| 2 | `p` | `ㄆ` | `/pʰ/` | p ㄆ — voiceless aspirated bilabial stop | bilabial | stop | aspirated | voiceless | 朋友 / 朋友 `péngyou` [pʰə́ŋ.joʊ] "friend"; 票 / 票 `piào` [pʰjaʊ] "ticket"; 怕 / 怕 `pà` [pʰa] "to fear" | VOICELESS ASPIRATED [pʰ] with a strong puff of air, like the *p* of English 'pin'. The aspiration is the sole cue distinguishing it from `b` [p]; in connected/unstressed position the aspiration may weaken but never neutralises with `b`. Same in both standards. |
| 3 | `m` | `ㄇ` | `/m/` | m ㄇ — bilabial nasal | bilabial | nasal | n/a | voiced | 妈妈 / 媽媽 `māma` [ma.ma] "mother, mum"; 马 / 馬 `mǎ` [ma] "horse"; 吗 / 嗎 `ma` [ma] "(yes/no question particle, neutral tone)" | Plain voiced bilabial nasal [m], stable in all positions. One of the very few initials that can carry a syllable by itself in interjections (呣 *m*, 呒). The neutral-tone particle 吗/嗎 *ma* is a high-frequency reduced realisation. Identical in Pǔtōnghuà and Guóyǔ. |
| 4 | `f` | `ㄈ` | `/f/` | f ㄈ — voiceless labiodental fricative | labiodental | fricative | n/a | voiceless | 饭 / 飯 `fàn` [fan] "cooked rice, meal"; 风 / 風 `fēng` [fəŋ] "wind"; 飞 / 飛 `fēi` [feɪ] "to fly" | Voiceless labiodental [f]; has NO voiced partner ([v] is not phonemic — loanword *v* is rendered `f` or `w`). `f` does not combine with the medial -u- the way English does; in Pinyin it precedes `a, o, e, ei, en, eng, u` and the glide -o in `fo`. Some northern/older speakers and certain dialect substrates show f↔h or f↔hw alternations, but Standard Mandarin keeps a clean [f]. Same in both standards. |
| 5 | `d` | `ㄉ` | `/t/` | d ㄉ — voiceless unaspirated alveolar stop | alveolar | stop | unasp. | voiceless | 大 / 大 `dà` [ta] "big"; 弟弟 / 弟弟 `dìdi` [tî.ti] "younger brother"; 的 / 的 `de` [tə] "(possessive/attributive particle, neutral tone)" | VOICELESS UNASPIRATED [t] — like the *t* of English 'stop', not the *d* of 'dop' (voiced) and not the aspirated *t* of 'top'. Contrasts with `t` [tʰ] by aspiration only (大 *dà* [ta] vs 他 *tā* [tʰa]). The ubiquitous neutral-tone particle 的 *de* [tə] is its commonest token. Same in Pǔtōnghuà and Guóyǔ. |
| 6 | `t` | `ㄊ` | `/tʰ/` | t ㄊ — voiceless aspirated alveolar stop | alveolar | stop | aspirated | voiceless | 他 / 他 `tā` [tʰa] "he, him"; 天 / 天 `tiān` [tʰjɛn] "sky, day"; 听 / 聽 `tīng` [tʰiŋ] "to listen" | VOICELESS ASPIRATED [tʰ], like the *t* of English 'top'. Strong aspiration is the cue against `d` [t]. Aspiration may reduce in fast/unstressed speech but the `d`–`t` contrast is preserved. Same in both standards. |
| 7 | `n` | `ㄋ` | `/n/` | n ㄋ — alveolar nasal | alveolar | nasal | n/a | voiced | 你 / 你 `nǐ` [ni] "you (singular)"; 那 / 那 `nà` [na] "that"; 牛奶 / 牛奶 `niúnǎi` [njoʊ.naɪ] "(cow's) milk" | Voiced alveolar nasal [n] as an INITIAL; before `i`/`ü` it is lightly palatalised [nʲ] (你 *nǐ*, 女 *nǚ* [nʲy]). Standard Mandarin keeps `n` distinct from `l` (那 *nà* vs 拉 *lā*), but many southern speakers (and some Taiwan Guóyǔ) merge or confuse n/l. As a CODA -n the alveolar nasal also closes syllables, but that belongs to the finals. Same phoneme in both standards (the southern n/l merger being a recognised regional feature). |
| 8 | `l` | `ㄌ` | `/l/` | l ㄌ — alveolar lateral approximant | alveolar | lateral approximant | n/a | voiced | 来 / 來 `lái` [laɪ] "to come"; 老师 / 老師 `lǎoshī` [laʊ.ʂɻ̩] "teacher"; 了 / 了 `le` [lə] "(aspect/change-of-state particle, neutral tone)" | A clear (non-velarised) voiced alveolar lateral [l] in all positions — Mandarin has NO 'dark l' [ɫ] and `l` does not occur in the coda. Distinct from `n` (来 *lái* vs 奶 *nǎi*). The aspect particle 了/了 *le* [lə] is its most frequent token. Same in both standards; n/l confusion is a southern-substrate feature, not standard. |
| 9 | `g` | `ㄍ` | `/k/` | g ㄍ — voiceless unaspirated velar stop | velar | stop | unasp. | voiceless | 高 / 高 `gāo` [kaʊ] "tall, high"; 个 / 個 `gè` [kɤ] "(general measure word)"; 狗 / 狗 `gǒu` [koʊ] "dog" | VOICELESS UNASPIRATED [k] — like the *k* of English 'sky', not the *g* of 'guy' (voiced) and not the aspirated *k* of 'kite'. Contrasts with `k` [kʰ] by aspiration only (高 *gāo* [kaʊ] vs 考 *kǎo* [kʰaʊ]). NEVER occurs before `i` [i]/`ü` [y] — that environment is filled by the palatal `j` (historically g + front vowel → j). Same in both standards. |
| 10 | `k` | `ㄎ` | `/kʰ/` | k ㄎ — voiceless aspirated velar stop | velar | stop | aspirated | voiceless | 看 / 看 `kàn` [kʰan] "to look, to watch"; 口 / 口 `kǒu` [kʰoʊ] "mouth"; 咖啡 / 咖啡 `kāfēi` [kʰa.feɪ] "coffee" | VOICELESS ASPIRATED [kʰ], like the *k* of English 'kite'. Aspiration is the cue against `g` [k]. Like `g`, `k` NEVER occurs before `i`/`ü` (that slot is held by `q`). Same in both standards. |
| 11 | `h` | `ㄏ` | `/x/` | h ㄏ — voiceless velar (dorsal) fricative | velar | fricative | n/a | voiceless | 好 / 好 `hǎo` [xaʊ] "good"; 喝 / 喝 `hē` [xɤ] "to drink"; 和 / 和 `hé` [xɤ] "and (PRC *hé*; Taiwan reading *hàn*)" | A VELAR (dorsal) fricative [x], typically further back and rougher than English [h] — closer to the *ch* of German 'Bach' or Scots 'loch', though many speakers use a softer [h~ɦ]. NEVER occurs before `i`/`ü` (that slot is held by `x` [ɕ]; historically h + front vowel → x). The word 和 'and' is read *hé* in Pǔtōnghuà but commonly *hàn* in Taiwan Guóyǔ — a lexical, not phonemic, difference. Same `h` phoneme in both standards. |
| 12 | `j` | `ㄐ` | `/tɕ/` | j ㄐ — voiceless unaspirated alveolo-palatal affricate | alveolo-palatal | affricate | unasp. | voiceless | 鸡 / 雞 `jī` [tɕi] "chicken"; 家 / 家 `jiā` [tɕja] "home, family"; 几 / 幾 `jǐ` [tɕi] "how many; several" | VOICELESS UNASPIRATED alveolo-palatal affricate [tɕ] — the blade of the tongue against the alveolo-palatal region, like a softer English 'j' but VOICELESS and UNASPIRATED (closest to the *j/dy* in 'did you' but with no voicing). Contrasts with `q` [tɕʰ] by aspiration only (鸡 *jī* [tɕi] vs 七 *qī* [tɕʰi]). `j q x` are in COMPLEMENTARY DISTRIBUTION with `z c s` / `zh ch sh` / `g k h`: they occur ONLY before `i` [i] and `ü` [y] (and the glides j/ɥ). Pinyin drops the umlaut after `j` (because only `ü`, never `u`, can follow): `ju` = `jü` = [tɕy]. Same in both standards. |
| 13 | `q` | `ㄑ` | `/tɕʰ/` | q ㄑ — voiceless aspirated alveolo-palatal affricate | alveolo-palatal | affricate | aspirated | voiceless | 七 / 七 `qī` [tɕʰi] "seven"; 去 / 去 `qù` [tɕʰy] "to go"; 请 / 請 `qǐng` [tɕʰiŋ] "please; to invite" | VOICELESS ASPIRATED alveolo-palatal affricate [tɕʰ], the aspirated partner of `j`; NOT the English 'ch' [tʃ] (which is retroflexed/postalveolar — that is Mandarin `ch`). Aspiration distinguishes it from `j` (七 *qī* [tɕʰi] vs 鸡 *jī* [tɕi]). Occurs ONLY before `i`/`ü`; `qu` = `qü` = [tɕʰy]. The word 企 is read *qǐ* in Pǔtōnghuà but *qì* in Taiwan Guóyǔ (lexical tone difference, not phonemic). Same `q` phoneme in both standards. |
| 14 | `x` | `ㄒ` | `/ɕ/` | x ㄒ — voiceless alveolo-palatal fricative | alveolo-palatal | fricative | n/a | voiceless | 西 / 西 `xī` [ɕi] "west"; 谢谢 / 謝謝 `xièxie` [ɕjɛ̂.ɕjɛ] "thank you"; 学 / 學 `xué` [ɕɥɛ] "to study, to learn" | VOICELESS alveolo-palatal fricative [ɕ] — between English 's' and 'sh', made with the tongue blade raised toward the hard palate. It is the fricative member of the `j q x` palatal series. Occurs ONLY before `i`/`ü`; `xu` = `xü` = [ɕy], `xue` = `xüe` = [ɕɥɛ]. Do not retroflex it (that would be `sh` [ʂ]) and do not make it a plain [s]. Same in both standards. |
| 15 | `zh` | `ㄓ` | `/ʈʂ/` | zh ㄓ — voiceless unaspirated retroflex affricate | retroflex | affricate | unasp. | voiceless | 中国 / 中國 `Zhōngguó` [ʈʂʊŋ.kwɔ] "China"; 这 / 這 `zhè` [ʈʂɤ] "this"; 知道 / 知道 `zhīdào` [ʈʂɻ̩.taʊ] "to know" | VOICELESS UNASPIRATED RETROFLEX affricate [ʈʂ] — tongue tip curled up toward the back of the alveolar ridge, like the 'dr' in American 'drip' but voiceless and unaspirated. Contrasts with `ch` [ʈʂʰ] by aspiration only (这 *zhè* vs 车 *chē*). In the syllable `zhi` the following 'i' is NOT [i] but the retroflex APICAL vowel [ɻ̩] (`zhi` = [ʈʂɻ̩]). DE-RETROFLEXION: in much Taiwan Guóyǔ (and casual northern/southern speech) `zh` merges toward the dental `z` [ts], so 知道 may sound like [tsɹ̩.taʊ]; this is a recognised surface feature of Guóyǔ, not a separate phoneme. Same underlying phoneme in both standards. |
| 16 | `ch` | `ㄔ` | `/ʈʂʰ/` | ch ㄔ — voiceless aspirated retroflex affricate | retroflex | affricate | aspirated | voiceless | 吃 / 吃 `chī` [ʈʂʰɻ̩] "to eat"; 车 / 車 `chē` [ʈʂʰɤ] "car, vehicle"; 茶 / 茶 `chá` [ʈʂʰa] "tea" | VOICELESS ASPIRATED RETROFLEX affricate [ʈʂʰ], the aspirated partner of `zh`; the closest English approximation is a strongly aspirated, retroflexed 'ch'. Aspiration distinguishes it from `zh` (吃 *chī* vs 知 *zhī*). In `chi` the vowel is the apical [ɻ̩] (`chi` = [ʈʂʰɻ̩]). Subject to DE-RETROFLEXION toward `c` [tsʰ] in Taiwan Guóyǔ and casual speech (吃 *chī* → [tsʰɹ̩]). Same phoneme in both standards. |
| 17 | `sh` | `ㄕ` | `/ʂ/` | sh ㄕ — voiceless retroflex fricative | retroflex | fricative | n/a | voiceless | 是 / 是 `shì` [ʂɻ̩] "to be (is/am/are)"; 山 / 山 `shān` [ʂan] "mountain"; 书 / 書 `shū` [ʂu] "book" | VOICELESS RETROFLEX fricative [ʂ] — like English 'sh' but with the tongue tip curled back, darker and more 'hollow'. The fricative member of the retroflex series; its voiced partner is `r` [ʐ]. In `shi` the vowel is apical [ɻ̩] (`shi` = [ʂɻ̩]). Strongly subject to DE-RETROFLEXION toward `s` [s] in Taiwan Guóyǔ and casual speech (是 *shì* → [sɹ̩]). Same phoneme in both standards. |
| 18 | `r` | `ㄖ` | `/ʐ/` | r ㄖ — voiced retroflex fricative / approximant | retroflex | fricative ~ approximant | n/a | voiced | 人 / 人 `rén` [ʐən] ~ [ɻən] "person"; 日 / 日 `rì` [ʐɻ̩] ~ [ɻɻ̩] "sun, day"; 热 / 熱 `rè` [ʐɤ] ~ [ɻɤ] "hot" | The ONLY voiced obstruent initial. It ranges from a voiced retroflex fricative [ʐ] (a 'buzzed' English 'zh'/'measure' sound made with retroflexion) to a frictionless retroflex approximant [ɻ] (close to American English 'r'); careful Beijing speech tends to [ʐ], casual speech to [ɻ]. It is the voiced counterpart of `sh` in the retroflex series. In `ri` the vowel is apical [ɻ̩] (`ri` = [ʐɻ̩]). In Taiwan Guóyǔ initial `r` is often DE-RETROFLEXED/weakened toward [z] or a glide-like [ɻ̞]~[j]/[ʐ̞], and 儿/er-rhotacisation (erhua) is largely absent — but the INITIAL `r` and the erhua coda -r [ɚ] are distinct elements (the coda belongs to the finals). Same phoneme in both standards, with Guóyǔ realising it more weakly. |
| 19 | `z` | `ㄗ` | `/ts/` | z ㄗ — voiceless unaspirated dental affricate | dental/alveolar | affricate | unasp. | voiceless | 在 / 在 `zài` [tsaɪ] "at, in; (progressive marker)"; 字 / 字 `zì` [tsɹ̩] "(written) character, word"; 走 / 走 `zǒu` [tsoʊ] "to walk, to go" | VOICELESS UNASPIRATED dental affricate [ts] — like the 'ts' in English 'cats' but NOT voiced (it is NOT English 'z' [z]). Contrasts with `c` [tsʰ] by aspiration only (在 *zài* vs 菜 *cài*). Made with the tongue tip at/behind the upper teeth, NOT retroflexed (contrast `zh`) and NOT palatal (contrast `j`). In `zi` the vowel is the dental APICAL vowel [ɹ̩] (`zi` = [tsɹ̩]), not [i]. NEVER occurs before `i` [i]/`ü` [y] (that slot is the palatal `j`). Same in both standards; note de-retroflexed `zh` in Guóyǔ can MERGE toward this `z`. |
| 20 | `c` | `ㄘ` | `/tsʰ/` | c ㄘ — voiceless aspirated dental affricate | dental/alveolar | affricate | aspirated | voiceless | 菜 / 菜 `cài` [tsʰaɪ] "vegetable; dish (of food)"; 次 / 次 `cì` [tsʰɹ̩] "(measure word: time, occurrence)"; 从 / 從 `cóng` [tsʰʊŋ] "from; to follow" | VOICELESS ASPIRATED dental affricate [tsʰ], the aspirated partner of `z` — a strongly aspirated 'ts'. Aspiration distinguishes it from `z` (菜 *cài* vs 在 *zài*). Pinyin 'c' is a notorious learner trap: it is NEVER [k] or [s] but always [tsʰ]. In `ci` the vowel is the dental apical [ɹ̩] (`ci` = [tsʰɹ̩]). NEVER before `i`/`ü`. Same in both standards. |
| 21 | `s` | `ㄙ` | `/s/` | s ㄙ — voiceless dental fricative (sibilant) | dental/alveolar | fricative | n/a | voiceless | 四 / 四 `sì` [sɹ̩] "four"; 三 / 三 `sān` [san] "three"; 岁 / 歲 `suì` [sweɪ] "year(s) of age" | VOICELESS dental/alveolar sibilant [s] — like English 's' (never voiced [z]). The fricative member of the dental `z c s` series; it is NOT retroflex (contrast `sh` [ʂ]) and NOT palatal (contrast `x` [ɕ]). In `si` the vowel is the dental apical [ɹ̩] (`si` = [sɹ̩]), not [i]. NEVER before `i` [i]/`ü` [y]. Taiwan Guóyǔ's de-retroflexed `sh` can merge toward this `s` (是 *shì* → [sɹ̩], homophonous with parts of the s-row). Same `s` phoneme in both standards. |

### Zero Initial (零声母)

| Field | Value |
|---|---|
| Chinese name | 零声母 (*líng shēngmǔ*) |
| Pinyin | `líng shēngmǔ` |
| English | zero / null initial |

A syllable with NO onset consonant — the final stands alone. Phonetically the vowel may begin with a light glottal onset [ʔ] or a weak glide, but there is no consonantal initial. In Hanyu Pinyin a zero-initial syllable is spelled with the bare final, except that initial `i`/`u`/`ü` are respelled with `y`/`w` (the SEMIVOWEL convention): `i`→`yi`, `in`→`yin`, `ie`→`ye`, `u`→`wu`, `uo`→`wo`, `ü`→`yu`, `üe`→`yue`, etc. Zhuyin simply omits the onset letter and writes the medial/rhyme glyphs.

| 汉字 (简) | 汉字 (繁) | Pinyin | Zhuyin | IPA | Gloss |
|---|---|---|---|---|---|
| 爱 | 愛 | `ài` | `ㄞˋ` | [aɪ] | to love |
| 我 | 我 | `wǒ` | `ㄨㄛˇ` | [wɔ] | I, me |
| 鱼 | 魚 | `yú` | `ㄩˊ` | [y] | fish |
| 一 | 一 | `yī` | `ㄧ` | [i] | one |

**Allophony.** A zero-initial vowel is commonly preceded by a faint glottal stop [ʔ] in careful or emphatic speech and by frictionless onset in connected speech; the `i`/`u`/`ü`-initial syllables surface with their corresponding glides [j w ɥ] (`yi` [ji]~[i], `wu` [wu]~[u], `yu` [ɥy]~[y]). In casual fast speech a zero-initial syllable after another may take a linking glide. Identical in Pǔtōnghuà and Guóyǔ.

### Natural Classes

Groupings of the initials by shared phonological features, drawn from the source data.

| Class | Members |
|---|---|
| Stops / plosives | `b`, `p`, `d`, `t`, `g`, `k` |
| Affricates | `z`, `c`, `zh`, `ch`, `j`, `q` |
| Fricatives | `f`, `s`, `sh`, `r`, `x`, `h` |
| Nasals | `m`, `n` |
| Lateral | `l` |
| Approximant / rhotic | `r` |
| Obstruents | `b`, `p`, `d`, `t`, `g`, `k`, `z`, `c`, `zh`, `ch`, `j`, `q`, `f`, `s`, `sh`, `r`, `x`, `h` |
| Sonorants | `m`, `n`, `l` |
| Voiceless | `b`, `p`, `d`, `t`, `g`, `k`, `z`, `c`, `zh`, `ch`, `j`, `q`, `f`, `s`, `sh`, `x`, `h` |
| Voiced | `m`, `n`, `l`, `r` |
| Sibilants | `z`, `c`, `s`, `zh`, `ch`, `sh`, `r`, `j`, `q`, `x` |

**Stops.** Three places (bilabial `b`/`p`, alveolar `d`/`t`, velar `g`/`k`), each a VOICELESS UNASPIRATED vs VOICELESS ASPIRATED pair: `b` [p] / `p` [pʰ], `d` [t] / `t` [tʰ], `g` [k] / `k` [kʰ]. None is voiced — Mandarin has no /b d ɡ/ in the English sense.

**Affricates.** Three parallel affricate places, each unaspirated/aspirated: DENTAL `z` [ts] / `c` [tsʰ], RETROFLEX `zh` [ʈʂ] / `ch` [ʈʂʰ], ALVEOLO-PALATAL `j` [tɕ] / `q` [tɕʰ]. All voiceless; the contrast within each pair is aspiration.

**Fricatives.** Labiodental `f` [f]; the three sibilant fricatives that match the affricate places — dental `s` [s], retroflex `sh` [ʂ], alveolo-palatal `x` [ɕ]; the dorsal/velar `h` [x]; and `r` [ʐ~ɻ], the retroflex VOICED fricative/approximant that is the system's only voiced obstruent.

**Nasals.** Bilabial `m` [m] and alveolar `n` [n] as INITIALS. (The velar nasal [ŋ] occurs only as a syllable CODA — `-ng` — never as an initial, and so is treated under finals, not here.)

**Lateral.** A single lateral approximant `l` [l]; Mandarin distinguishes `l` from `n` as initials (拉 *lā* vs 那 *nà*), unlike many southern Sinitic varieties that merge them.

**Rhotic.** Initial `r` is the retroflex [ʐ] (fricative) ~ [ɻ] (approximant); it is the voiced counterpart of `sh` in the retroflex series. (A separate r-element, the rhotacising coda 儿 -r [ɚ] of erhua 儿化, belongs to the finals, not to the initials.)

**Voiceless note.** ALL obstruents except `r` are phonetically voiceless. The `b`/`d`/`g`/`j`/`z`/`zh` series are voiceless UNASPIRATED (lenis), NOT voiced; English speakers must suppress the voicing they would give 'b d g'.

**Voiced note.** Only the sonorants `m n l` and the obstruent `r` are voiced. `r` [ʐ~ɻ] is the sole voiced obstruent in the inventory.

#### Aspiration Pairs

SIX aspiration pairs carry the laryngeal contrast of the system. The members differ ONLY in aspiration (and never in voicing). This is the Mandarin analog of the English voicing contrast, and it is the most common pronunciation error for English/Romance learners.

| Pair | Unaspirated | Aspirated | Minimal pair |
|---|---|---|---|
| b / p | `b` [p] | `p` [pʰ] | 北 *běi* [peɪ] "north" vs 配 *pèi* [pʰeɪ] "to match" |
| d / t | `d` [t] | `t` [tʰ] | 大 *dà* [ta] "big" vs 他 *tā* [tʰa] "he" |
| g / k | `g` [k] | `k` [kʰ] | 高 *gāo* [kaʊ] "tall" vs 考 *kǎo* [kʰaʊ] "test" |
| z / c | `z` [ts] | `c` [tsʰ] | 在 *zài* [tsaɪ] "at" vs 菜 *cài* [tsʰaɪ] "vegetable" |
| zh / ch | `zh` [ʈʂ] | `ch` [ʈʂʰ] | 这 *zhè* "this" vs 车 *chē* "car" |
| j / q | `j` [tɕ] | `q` [tɕʰ] | 鸡 *jī* [tɕi] "chicken" vs 七 *qī* [tɕʰi] "seven" |

#### The Three Sibilant Series

The signature of the Mandarin onset: THREE sibilant series with the same affricate–affricate–fricative shape at three places. The palatal `j q x` is in COMPLEMENTARY DISTRIBUTION with the other two series (and with `g k h`): it occurs ONLY before `i` [i] and `ü` [y], where `z c s` / `zh ch sh` / `g k h` never appear, so the three series never contrast in the same vowel environment.

| Series | Unaspirated affricate | Aspirated affricate | Fricative | Voiced | Articulation |
|---|---|---|---|---|---|
| Dental | `z` [ts] | `c` [tsʰ] | `s` [s] | — | apical, behind the upper teeth |
| Retroflex | `zh` [ʈʂ] | `ch` [ʈʂʰ] | `sh` [ʂ] | `r` [ʐ] | tongue tip curled up |
| Alveolo-palatal | `j` [tɕ] | `q` [tɕʰ] | `x` [ɕ] | — | blade against the alveolo-palatal region, before high front vowels |

**Mnemonic** (by aspiration + place): unaspirated affricates `j`/`z`/`zh`, aspirated affricates `q`/`c`/`ch`, fricatives `x`/`s`/`sh`, voiced `r`.

**The ten sibilants** across the three series (dental `z c s`, retroflex `zh ch sh r`, palatal `j q x`) have an APICAL-vowel residue written `-i`: `zi ci si` = [tsɹ̩ tsʰɹ̩ sɹ̩] with the dental apical vowel [ɹ̩], and `zhi chi shi ri` = [ʈʂɻ̩ ʈʂʰɻ̩ ʂɻ̩ ʐɻ̩] with the retroflex apical vowel [ɻ̩] (this `-i` is NOT the vowel [i]).

#### Complementary Distribution (`j q x`)

| Occur ONLY before `i`/`ü` | NEVER before `i`/`ü` |
|---|---|
| `j`, `q`, `x` | `z`, `c`, `s`, `zh`, `ch`, `sh`, `g`, `k`, `h` |

`j q x` [tɕ tɕʰ ɕ] occur ONLY before the high front vocoids `i` [i] and `ü` [y] (and their glides); `z c s`, `zh ch sh` and `g k h` NEVER occur before `i` [i]/`ü` [y]. Because the environments are mutually exclusive, `j q x` do not phonemically contrast with `z c s` / `zh ch sh` / `g k h` — historically the palatals arose from the merger of older velars (`g k h`) and dental sibilants (`z c s`) before front vowels. Pinyin even drops the umlaut after `j q x` (because only `ü` can follow): `ju` = [tɕy], `qu` = [tɕʰy], `xu` = [ɕy], so written `ju`/`qu`/`xu` = `jü`/`qü`/`xü`.

#### Gaps (no native phoneme)

| Missing element | Status in Mandarin |
|---|---|
| Voiced stops [b d ɡ] | NOT present — the Pinyin letters `b d g` are voiceless unaspirated [p t k] |
| [v] | NOT present — the `f`-row has no voiced partner; loan *v* → [w] or `f` |
| [θ] | NOT present — borrowed as `s` or as the apical `-i` |
| [ð] | NOT present |
| voiced dental [z] | NOT present — Pinyin `z` = [ts], an affricate, not English 'zoo' |
| [dʒ] | NOT present — no postalveolar voiced affricate |
| [ʒ] | NOT present — no English 'measure' fricative |
| [ŋ] as INITIAL | NOT present — the velar nasal exists only as the coda `-ng` |

There is also NO syllable-initial consonant cluster of any kind.

### Summary Notes

**Aspiration, not voicing.** RESTATE: Mandarin's obstruent contrast is ASPIRATION, not voicing. Pinyin `b d g j z zh` = voiceless UNASPIRATED [p t k tɕ ts ʈʂ]; `p t k q c ch` = voiceless ASPIRATED [pʰ tʰ kʰ tɕʰ tsʰ ʈʂʰ]. There are NO voiced stops/affricates; the lone voiced obstruent is `r` [ʐ~ɻ]. English-speaker errors: voicing `b`/`d`/`g`/`z`/`zh`, and under-aspirating `p`/`t`/`k`/`c`/`ch`.

**Three sibilant series relationship.** The dental `z c s` [ts tsʰ s], retroflex `zh ch sh` [ʈʂ ʈʂʰ ʂ] and palatal `j q x` [tɕ tɕʰ ɕ] are THREE versions of the same affricate–affricate–fricative pattern at three places. `j q x` are in COMPLEMENTARY DISTRIBUTION with both `z c s` and `zh ch sh` (and with `g k h`): `j q x` appear ONLY before `i`/`ü`, where the others never appear.

**Apical vowels after sibilants.** The Pinyin `-i` after `z c s` and `zh ch sh r` is NOT the vowel [i]: it is a syllabic APICAL vowel — dental [ɹ̩] after `z c s` (`zi ci si` = [tsɹ̩ tsʰɹ̩ sɹ̩]) and retroflex [ɻ̩] after `zh ch sh r` (`zhi chi shi ri` = [ʈʂɻ̩ ʈʂʰɻ̩ ʂɻ̩ ʐɻ̩]). Real [i] appears only after `j q x` and the other initials (`ji` = [tɕi], `ni` = [ni]).

**Taiwan Guóyǔ de-retroflexion.** In 國語 Guóyǔ (and casual mainland speech) the retroflex series `zh ch sh r` is widely DE-RETROFLEXED toward the dental series: `zh`→`z` [ts], `ch`→`c` [tsʰ], `sh`→`s` [s], `r`→weakened/[z]~[ɻ̞]. Guóyǔ also has little or no ERHUA (儿化, the -r/[ɚ] coda) and fewer neutral tones. These are SURFACE realisations and lexical habits; the toneless Pinyin SPINE (and hence the Peshitta reader tiers) is unchanged — the underlying initial inventory is identical to Pǔtōnghuà's.

**-ng is coda only.** The velar nasal [ŋ] (Pinyin `-ng`) is NOT an initial; it occurs only as a syllable coda and is documented under finals. Likewise the erhua coda -r [ɚ] is a final, not the initial `r`.

### Companion Files

- `Chinese/chinese_pronunciation_guide.md`
- `Chinese/Peshita_Chinese/Pinyin/`
- `Chinese/Peshita_Chinese/Zhuyin/`
- `Chinese/Peshita_Chinese/Hanzi_Simplified/`
- `Chinese/Peshita_Chinese/Hanzi_Traditional/`

*Section signed: Shin.*

## Vowels & Nuclei

The Mandarin Chinese vowel / nucleus inventory — the 韵腹 (`yùnfù`, "rime belly"), the vowel core of the final 韵母 (`yùnmǔ`). This section covers the MONOPHTHONGAL vowel phonemes that fill the nucleus slot, the two APICAL ("buzzing") vowels written pinyin `-i`, the rhotacized `er` 儿/兒 final /ɚ/, and the three medial glides `i`/`u`/`ü` (/j w ɥ/) that fill the pre-nuclear slot.

The single most important fact about Mandarin vowels — sharply unlike the English and Korean systems, and even unlike Japanese — is that vowel quality is RADICALLY CONTEXT-CONDITIONED WITHIN THE FINAL: the same phoneme is realized very differently depending on the surrounding medial and coda, so /a/, /ɤ/ ("e"), and the apical and zero nuclei in particular are best understood as abstract underlying targets whose surface value the rest of the rime determines. Mandarin therefore has a SMALL set of contrastive nuclei but a LARGE set of surface vowel allophones. There is NO phonemic vowel length (unlike English /ː/ and Japanese short/long), NO lax/tense (checked/free) class system, and NO English-style schwa-as-reduction set — but there IS a pervasive [ə] that surfaces as a contextual realization of /ɤ/ and as the unstressable nucleus of neutral-tone (轻声/輕聲 `qīngshēng`) syllables.

TONE rides on the nucleus but is documented in its own section. Two reference standards are documented in parallel, mirroring the GA/RP framing of the English guide and the 標準語/関西弁 framing of the Japanese guide:

- **普通话 / 普通話 `Pǔtōnghuà`** — PRC Standard Mandarin (Beijing-based, Simplified characters, Hanyu Pinyin).
- **国语 / 國語 `Guóyǔ`** — Taiwan Standard Mandarin (Traditional characters, Zhuyin/Bopomofo).

For vowel QUALITY the two standards agree on the phonemic system; they diverge mainly in (a) erhua / rhotacization, which is heavy in `Pǔtōnghuà` but minimal in `Guóyǔ`, and (b) some surface tendencies (e.g. Taiwan apical vowels and final `-o`/`-e` qualities). IPA follows the 2015 revision; /slashes/ mark phonemic transcription and [brackets] mark phonetic detail. Pinyin is the deterministic toneless spine; example words give BOTH 简体字/簡體字 (Simplified) and 繁體字 (Traditional) Hanzi plus Zhuyin. These cross-reference the six shipped Peshitta reader tiers — Scholarly, Pretty (language-neutral Latin), Toneless Pinyin, Zhuyin/Bopomofo, and Hanzi in Simplified and Traditional. **The four reader tiers built on the romanized/transcription spine (Pretty, Toneless Pinyin, Zhuyin, and the toneless source generally) are TONELESS; the language itself is fully tonal, and citation tones cited below are NOT present in the toneless source.**

### Vowel System Overview

Mandarin's nuclear vowel system, analyzed phonemically. Traditional analyses posit a SMALL set of underlying vowel phonemes — commonly /a/, /ə~ɤ/ (the "e" phoneme), /i/, /u/, /y/ (`ü`), plus the open-mid /o/ and front /ɛ/ (`ê`) — whose surface qualities are heavily determined by the medial and coda within the final. Layered on top are the two APICAL vowels (the "buzzed" `-i` of `zi`/`zhi` etc.), which most analyses treat as syllabic continuations of the preceding sibilant rather than as independent vowel phonemes, and the rhotacized `er` /ɚ/. Crucially, Mandarin has NO phonemic vowel length, NO checked/free (lax/tense) opposition, and NO stress-driven reduction inventory of the English kind; instead, the system trades a large lax/tense vowel space for a large set of POSITIONALLY-determined allophones plus a four-way LEXICAL TONE contrast (documented separately). The result is fewer contrastive nuclei than English but more surface vowel colors than Japanese's five clean qualities.

#### Core Nuclei

The contrastive nuclear vowels with their pinyin spelling, Zhuyin, and broad phonetic value. Qualities shift with context (see each vowel's allophony notes).

| Phoneme | Pinyin | Zhuyin | Description |
|---|---|---|---|
| /a/ | `a` | `ㄚ` | Low vowel; surfaces front [a], central [A~ɐ], or back [ɑ] depending on the coda/medial. |
| /ɤ/ | `e` | `ㄜ` | The "e" phoneme: unrounded back/central mid; the most chameleonic vowel, realized [ɤ], [ə], [ɛ], or [e] by context. |
| /ɛ/ | `ê` / `-ie`, `-üe` | `ㄝ` | Open-mid front unrounded; chiefly the nucleus of `ie`/`üe` and the standalone interjection `ê`. |
| /o/ | `o` | `ㄛ` | Mid back rounded; native chiefly after labials `b`/`p`/`m`/`f` and in `-uo`, and the interjection `o`. |
| /i/ | `i` (true vowel) | `ㄧ` | Close front unrounded; also the medial glide /j/. |
| /u/ | `u` | `ㄨ` | Close back rounded; also the medial glide /w/. |
| /y/ | `ü` / `u` (after `j q x y`) | `ㄩ` | Close FRONT ROUNDED; also the medial glide /ɥ/. |

#### By Height

| Height | Vowels |
|---|---|
| High / close | `i` /i/, `u` /u/, `ü` /y/ |
| Mid | `e` /ɤ/, `ê` /ɛ/, `o` /o/ |
| Low / open | `a` /a/ |

The three high vowels form a tidy point system /i u y/ (front-unrounded, back-rounded, front-rounded). The mid layer is split by backness and rounding: /ɤ/ (unrounded, the "e" phoneme), /ɛ/ (front, `ê`), /o/ (back rounded). A single low /a/ anchors the bottom but ranges from front [a] to back [ɑ] by context. There is no near-close/near-open lax layer (no /ɪ ʊ ɛ æ/-type class) as in English.

#### By Backness

| Backness | Vowels |
|---|---|
| Front unrounded | `i` /i/, `ê` /ɛ/ |
| Front rounded | `ü` /y/ |
| Central | `e` /ɤ/ (often central [ə]), `a` /a/ (often central [A]) |
| Back | `u` /u/, `o` /o/, `a` → [ɑ] before back coda |

Mandarin notably HAS a front-rounded vowel `ü` /y/ — the typological feature shared with French/German/Korean and absent from English/Japanese. The "e" phoneme /ɤ/ is the unrounded back-central counterpart that English lacks entirely; mispronouncing it as schwa or as English STRUT is a common error.

#### By Rounding

| Rounding | Vowels |
|---|---|
| Rounded | `u` /u/, `ü` /y/, `o` /o/ |
| Unrounded | `a` /a/, `e` /ɤ/, `ê` /ɛ/, `i` /i/ |

Two rounding contrasts are crucial: (1) the front pair `i` /i/ (unrounded) vs `ü` /y/ (rounded) — `i`/`ü` minimal-pair territory (例 `lì` vs 律 `lǜ`; 区/區 `qū` has /y/); and (2) the back unrounded `e` /ɤ/ vs back rounded `o` /o/. Rounding the front /y/ wrongly to /u/, or unrounding it to /i/, are both audible errors.

#### Apical and Rhotic Vowels

Beyond the core nuclei, Mandarin has two APICAL ("buzzing") syllabic vowels and one RHOTACIZED vowel, all written with ordinary pinyin letters but phonetically special.

| Type | Phone | Context | Note |
|---|---|---|---|
| Apical dental | [ɹ̩] (also [ɿ]) | after `z c s` (`zi ci si` 资/資 词/詞 思) | A syllabic prolongation of the dental sibilant /s ts tsʰ/; written pinyin `-i` but NOT the vowel /i/. |
| Apical retroflex | [ɻ̩] (also [ʐ̩]/[ʅ]) | after `zh ch sh r` (`zhi chi shi ri` 知 吃 诗/詩 日) | A syllabic prolongation of the retroflex /ʂ ʈʂ ʈʂʰ ʐ/; also written pinyin `-i` but again NOT /i/. |
| Rhotic | /ɚ/ (also [ɐɚ̯]) | `er` final 儿/兒; product of erhua 儿化/兒化 | A single rhotacized central vowel, the only coda-like rhotic vowel in the system. |

#### Contrast with English, Japanese, and Korean

Mandarin sits between English and Japanese in inventory size but is distinctive in HOW its vowels behave.

- **Versus English:** Mandarin has NO lax/tense (checked/free) class system, NO phonemic length, NO r-coloured START/NORTH/NURSE series (its single rhotic vowel is `er` /ɚ/ plus erhua), and NO stress-reduction schwa inventory — but it ADDS a four-way LEXICAL TONE contrast that English lacks entirely, plus a front-rounded /y/ and the unrounded back /ɤ/ that English has no symbol-match for.
- **Versus Japanese:** Both are CJK and both have small clean-looking inventories, but Japanese has phonemic LENGTH and an unrounded high back /ɯ/, while Mandarin instead has front-rounded /y/, the apical vowels, erhua, and far MORE context-driven vowel allophony (Japanese vowels keep nearly constant quality; Mandarin's /a ɤ/ do not).
- **Versus Korean:** Mandarin shares the front-rounded vowel territory and a high unrounded back-ish vowel /ɤ/ comparable in spirit to Korean ㅡ /ɯ/, but Mandarin's defining extra dimension is again TONE.

The single largest learning hazard unique to Mandarin's vowels is the EXTREME positional conditioning: "a", "e", and "i" each name several different surface vowels.

### Nuclear Vowel Inventory

The contrastive nuclei at a glance, with pinyin, Zhuyin, principal phonetic realizations, and class. Apical and rhotic vowels are listed for completeness.

| IPA | Pinyin | Zhuyin | Name | Phonetic value | Class |
|---|---|---|---|---|---|
| /a/ | `a` | `ㄚ` | low vowel (front~central~back by context) | [a] ~ [A] ~ [ɑ] ~ [ɛ] | core nucleus |
| /ɤ/ | `e` | `ㄜ` | close-mid back unrounded ("the e phoneme") | [ɤ] ~ [ə] ~ [ɛ] ~ [e] | core nucleus |
| /ɛ/ | `ê` (also the `e` of `-ie`, `-üe`) | `ㄝ` | open-mid front unrounded | [ɛ] ~ [e] | core nucleus (marginal as a bare phoneme) |
| /o/ | `o` | `ㄛ` | mid back rounded | [o] ~ [wo] ~ [ʊ] | core nucleus (restricted distribution) |
| /i/ | `i` (true vowel) / `y-` (glide) | `ㄧ` | close front unrounded | [i] (vowel) ~ [j] (medial glide) | core nucleus + medial glide |
| /u/ | `u` (true vowel) / `w-` (glide) | `ㄨ` | close back rounded | [u] (vowel) ~ [w] (medial glide) | core nucleus + medial glide |
| /y/ | `ü` / `u` (after `j q x y`) / `yu-` | `ㄩ` | close front rounded | [y] (vowel) ~ [ɥ] (medial glide) | core nucleus + medial glide |
| [ɹ̩] | `-i` (after `z c s`) | — (bare `ㄗ`/`ㄘ`/`ㄙ` implies it) | apical dental ("buzzed") vowel | [ɹ̩] ~ [ɿ] ~ [z̩] | apical syllabic vowel (allophonic) |
| [ɻ̩] | `-i` (after `zh ch sh r`) | — (bare `ㄓ`/`ㄔ`/`ㄕ`/`ㄖ` implies it) | apical retroflex ("buzzed") vowel | [ɻ̩] ~ [ʅ] ~ [ʐ̩] | apical syllabic vowel (allophonic) |
| /ɚ/ | `er` / `-r` (erhua) | `ㄦ` | rhotacized central vowel | [ɚ] ~ [ɐɚ̯] ~ [ɑɚ̯] | rhotic vowel / erhua coda |

### Per-Vowel Notes and Example Words

Each nucleus with example words giving pinyin, Simplified and Traditional Hanzi, Zhuyin, phonetic IPA, gloss, and a conditioning note, followed by an allophony summary. Citation tones are mentioned where relevant; recall that the toneless reader tiers drop them.

#### /a/ — `a` `ㄚ` — low vowel (front~central~back by context)

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `ba` | 八 | 八 | `ㄅㄚ` | [pa] | eight | Open syllable: clear front-to-central low [a]. (Citation tone T1 `bā`; the Peshitta reader tiers are toneless and would render simply "ba".) |
| `mama` | 妈妈 | 媽媽 | `ㄇㄚ ㄇㄚ` | [ma.ma] | mother | Two full low [a] nuclei; no reduction of the second the way English reduces an unstressed syllable. The neutral-tone second 妈/媽 keeps vowel quality, only losing tone. |
| `fan` | 饭 | 飯 | `ㄈㄢ` | [fan] | rice/meal | Before coronal coda `-n` the /a/ FRONTS toward [a~ɛ] (`an` = [an], `ian` = [jɛn]). |
| `fang` | 房 | 房 | `ㄈㄤ` | [fɑŋ] | house/room | Before the velar coda `-ng` the /a/ BACKS to [ɑ] (`ang` = [ɑŋ]). Contrast 饭/飯 `fan` [fan] vs 房 `fang` [fɑŋ]: SAME phoneme /a/, opposite backness, conditioned purely by the coda. |

**Allophony.** The single phoneme /a/ is the textbook case of Mandarin positional vowel conditioning. Its surface backness tracks the rime: FRONT [a] in open finals (`a`, `ba`) and before front-conditioning material; FRONTED to [a~ɛ] before coronal `-n` (`an` [an], and notably `ian` [jɛn] / `üan` [ɥɛn] where it raises to [ɛ]); BACKED to [ɑ] before velar `-ng` (`ang` [ɑŋ]) and after the back glide in `-ao`/`-uo` environments; CENTRAL [A] in diphthongs (`ai`, `ao`) and after medials. There is no length contrast and no devoicing. Diphthongs/triphthongs and nasal finals built on /a/ (`ai`, `ao`, `an`, `ang`, `ian`, `uan`…) are catalogued in the finals section.

#### /ɤ/ — `e` `ㄜ` — close-mid back unrounded ("the e phoneme")

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `he` | 喝 | 喝 | `ㄏㄜ` | [xɤ] | to drink | The CITATION value of bare `e`: an unrounded back [ɤ] (lips spread, tongue back) — emphatically NOT English schwa and NOT a rounded [o]. A classic learner trap. |
| `ge` | 个 | 個 | `ㄍㄜ` | [kɤ] | (general classifier) | The most frequent measure word; bare /ɤ/. In rapid neutral-tone use (一个/一個 `yí ge`) it weakens toward [ə], showing the `e`↔schwa alternation. |
| `hen` | 很 | 很 | `ㄏㄣ` | [xən] | very | Before coronal `-n`, /ɤ/ → central [ə]: `en` = [ən], not [ɤn]. Same in `eng` = [əŋ]. |
| `bie` | 别 | 別 | `ㄅㄧㄝ` | [pjɛ] | don't / other | After the front glide `i`/`ü` the "e" raises and fronts to [ɛ]: `ie` = [jɛ], `üe` = [ɥɛ]. (Pinyin writes this "e", but its quality here is the `ê` /ɛ/ value — see the `ê` entry.) |

**Allophony.** The "e" phoneme /ɤ/ is the MOST context-variable vowel in Mandarin and the chief source of confusion in the pinyin letter "e". Surface realizations: (1) bare/citation and after non-front onsets → unrounded back [ɤ] (`he` 喝, `ge` 个/個, `e` 鹅/鵝) — the value English speakers must learn from scratch, NOT schwa; (2) before coronal `-n`/`-ng` → central [ə] (`en` [ən], `eng` [əŋ]); (3) after a front glide `i`/`ü` → front [ɛ] (`ie` [jɛ], `üe` [ɥɛ]); (4) in the diphthong `ei` → [e] (`ei` [ei̯]). It also surfaces as [ə] as the reduced nucleus of NEUTRAL-tone syllables (轻声/輕聲), the nearest Mandarin gets to English reduction — but this is tone-driven, not a separate weak-vowel phoneme. No length, no devoicing.

#### /ɛ/ — `ê` `ㄝ` — open-mid front unrounded

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `ê` | 欸 | 欸 | `ㄝ` | [ɛ] | (interjection: "hey/eh") | The rare STANDALONE `ê`, written with the circumflex in pinyin precisely to distinguish it from ordinary `e` /ɤ/; an open-mid front [ɛ]. Almost the only place bare /ɛ/ is written. |
| `ye` | 也 | 也 | `ㄧㄝ` | [jɛ] | also | The medial /j/ + `ê`: `ie`/`ye` = [jɛ]. Here the pinyin letter "e" is NOT /ɤ/ but this front /ɛ/ — the spelling is a digraph trap. |
| `yue` | 月 | 月 | `ㄩㄝ` | [ɥɛ] | moon/month | The medial /ɥ/ (ü-glide) + `ê`: `üe`/`yue` = [ɥɛ]. Front-rounded glide onto a front-unrounded nucleus. |
| `xue` | 学 | 學 | `ㄒㄩㄝ` | [ɕɥɛ] | to study | After `j`/`q`/`x` the written "ue" is /yɛ/ → [ɥɛ] (the `ü` is unmarked in pinyin after `j q x y`). Shows `ê` as the nucleus of `-üe`. |

**Allophony.** /ɛ/ is the open-mid front vowel that pinyin writes "ê" in its rare standalone form (the interjection `ê` 欸) and, far more commonly, writes as plain "e" inside the digraphs `-ie`/`-ye` and `-üe`/`-yue`. Its Zhuyin symbol `ㄝ` is distinct from the `ㄜ` used for /ɤ/, which makes Bopomofo clearer than pinyin on this point: `ㄝ` /ɛ/ vs `ㄜ` /ɤ/. Phonetically [ɛ], sometimes closer [e] in careful speech. Many analyses treat the `-ie`/`-üe` nucleus as an allophone of the /ɤ/ "e" phoneme fronted by the preceding glide rather than as an independent phoneme; either way the SURFACE value is front [ɛ], crucially different from the back [ɤ] of bare `e`. No length, no devoicing.

#### /o/ — `o` `ㄛ` — mid back rounded (restricted distribution)

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `bo` | 波 | 波 | `ㄅㄛ` | [pwo] | wave | After a labial `b`/`p`/`m`/`f`, written "o" is phonetically [(w)o] with a slight on-glide: `bo` ≈ [pwo]. Bopomofo writes it `ㄅㄛ`, but many speakers realize `bo`/`po`/`mo`/`fo` with an audible [w]. |
| `po` | 婆 | 婆 | `ㄆㄛ` | [pʰwo] | old woman / mother-in-law | Same labial-conditioned [wo]; aspirated onset `p` /pʰ/. |
| `duo` | 多 | 多 | `ㄉㄨㄛ` | [two] | many/much | The productive home of /o/ is the final `-uo` = [wo]: medial /w/ + /o/. Zhuyin `ㄉㄨㄛ`. Most non-labial syllables use `-uo`, not bare `-o`. |
| `o` | 哦 | 哦 | `ㄛ` | [o] | (interjection: "oh") | The bare interjection `o` 哦/喔 is a fairly pure mid back rounded [o] — one of the few clean bare-/o/ environments. |

**Allophony.** /o/ is a mid back ROUNDED vowel with RESTRICTED distribution. It occurs (1) after the labials `b p m f`, where pinyin spells "o" but the realization carries a [w] on-glide ([pwo] etc.) — historically these are reduced `-uo` syllables; (2) in the final `-uo` = [wo] (`duo`, `guo`, `zuo`), its main productive context; and (3) as the bare interjection `o` 哦/喔 [o]. It also surfaces as the rounded back element [ʊ~o] of the diphthongs `ao` [ɑʊ̯] and `ou` [ou̯] (catalogued under finals). It does NOT occur after the alveolo-palatals or as a free nucleus the way /ɤ/ does; bare "e" /ɤ/ and "o" /o/ are the unrounded/rounded back-mid pair. No length, no devoicing. Taiwan `Guóyǔ` and PRC `Pǔtōnghuà` agree on /o/ quality.

#### /i/ — `i` `ㄧ` — close front unrounded (true vowel + medial glide /j/)

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `ni` | 你 | 你 | `ㄋㄧ` | [ni] | you | Plain close front [i] as a true nuclear vowel. Distinct from the apical `-i` of `zi`/`zhi` (see those entries): 你 `ni` has REAL [i], 知 `zhi` does NOT. |
| `ji` | 鸡 | 雞 | `ㄐㄧ` | [tɕi] | chicken | /i/ after the alveolo-palatal `j` /tɕ/; the high front vowel is exactly the environment that selects `j q x` (vs `z c s` / `g k h`). Clean [i]. |
| `ya` | 鸭 | 鴨 | `ㄧㄚ` | [ja] | duck | Syllable-initial `i` becomes the MEDIAL GLIDE /j/, spelled "y-": `ia`/`ya` = [ja]. Same phoneme /i/, now non-syllabic. |
| `lian` | 脸 | 臉 | `ㄌㄧㄢ` | [ljɛn] | face | Medial /j/ before the nasal final: `ian` = [jɛn] (note the /a/→[ɛ] raising conditioned by the front glide). Zhuyin `ㄌㄧㄢ`. |

**Allophony.** /i/ is the close front unrounded vowel, a stable [i] (no English-style lax [ɪ] counterpart). As a TRUE VOWEL it is the nucleus of `ni`, `ji`, `mi` etc. and the head of diphthongs/triphthongs. In the PRE-NUCLEAR (medial) slot it is the on-glide /j/, spelled "y-" word-initially and "i-" after a consonant (`ya`/`ia` [ja], `yan`/`ian` [jɛn], `yao`/`iao` [jɑʊ̯]). CRITICAL: the letter "i" after `z c s` and `zh ch sh r` is NOT this vowel — it is the apical buzz [ɹ̩]/[ɻ̩] (see the two apical entries below). So pinyin "i" is a two-valued letter: real [i] after most onsets, but apical [ɹ̩/ɻ̩] after the sibilant series. No length, no devoicing; /i/ is the trigger for the `j`/`q`/`x` ~ `z`/`c`/`s` complementary distribution.

#### /u/ — `u` `ㄨ` — close back rounded (true vowel + medial glide /w/)

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `wu` | 五 | 五 | `ㄨ` | [u] | five | Bare /u/ as a syllable (zero initial, spelled "wu"); a strongly rounded, protruded close back [u] — unlike Japanese /ɯ/, this IS the rounded cardinal-ish [u]. |
| `bu` | 不 | 不 | `ㄅㄨ` | [pu] | not | True nuclear [u] after a labial. (Sandhi note: 不 `bù` → `bú` before a T4 syllable — a tone change, not a vowel change.) |
| `wo` | 我 | 我 | `ㄨㄛ` | [wo] | I/me | Syllable-initial `u` becomes the MEDIAL GLIDE /w/, spelled "w-": `uo`/`wo` = [wo]. Same /u/ phoneme, non-syllabic on-glide. |
| `guan` | 关 | 關 | `ㄍㄨㄢ` | [kwan] | to close / pass | Medial /w/ + nasal final: `uan` = [wan]. Zhuyin `ㄍㄨㄢ`. Shows /u/ filling the pre-nuclear glide slot before a full rime. |

**Allophony.** /u/ is the close back ROUNDED vowel — genuinely rounded and protruded (contrast Japanese unrounded /ɯ/: Mandarin /u/ must be rounded). As a TRUE VOWEL it is the nucleus of `wu`, `bu`, `gu` and the back element of diphthongs (`ou`, `ao`). In the medial slot it is the on-glide /w/, spelled "w-" word-initially and "u-" after a consonant (`wo`/`uo` [wo], `wan`/`uan` [wan], `wei`/`ui` [wei̯]). It also surfaces lightly centralized [ʊ] as the off-glide of `ou`/`ao`. After the labials `b p m f` the rounded `-u` and `-o` overlap historically (see /o/). No length, no devoicing. CAUTION: do not confuse "u" after `j q x y`, which is actually the front-rounded /y/ (`ü`) written without the umlaut — see the `ü` entry.

#### /y/ — `ü` `ㄩ` — close front rounded (true vowel + medial glide /ɥ/)

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `lü` | 绿 | 綠 | `ㄌㄩ` | [ly] | green | The umlaut is KEPT after `l`/`n` because `lu`/`lü` and `nu`/`nü` contrast: 路 `lu` [lu] "road" vs 绿/綠 `lü` [ly] "green". A true close FRONT ROUNDED [y] (lips rounded as for [u], tongue front as for [i]). |
| `nü` | 女 | 女 | `ㄋㄩ` | [ny] | woman/female | Minimal pair with 怒 `nu` [nu] "angry". One of the two onsets (`l`, `n`) where pinyin must print the `ü` diaeresis. |
| `qu` | 去 | 去 | `ㄑㄩ` | [tɕʰy] | to go | After `j q x` the "u" is ALWAYS /y/ (no umlaut written, because /u/ never occurs there): `qu` = /tɕʰy/ [tɕʰy], NOT [tɕʰu]. A top pronunciation trap for the pinyin letter "u". |
| `yu` | 鱼 | 魚 | `ㄩ` | [y] | fish | Syllable-initially `ü` is spelled "yu-": `yu` = [y]. As a medial glide it is /ɥ/ (`yue`/`üe` [ɥɛ], `yuan`/`üan` [ɥɛn]). Zhuyin uses the dedicated symbol `ㄩ` throughout. |

**Allophony.** /y/ is the close FRONT ROUNDED vowel — the typological "extra" vowel that English and Japanese lack (compare French "tu", German "ü"). Pinyin spells it three ways: "ü" (with diaeresis) only after `l` and `n`, where it contrasts with /u/ (`lu`/`lü`, `nu`/`nü`); plain "u" after `j q x` (and as the glide after `y`), because /u/ is impossible there so no ambiguity arises (`ju qu xu yu` = /tɕy tɕʰy ɕy y/); and "yu-" word-initially. In the medial slot it is the front-rounded on-glide /ɥ/ (`üe`/`yue` [ɥɛ], `üan`/`yuan` [ɥɛn], `ün`/`yun` [yn]). Zhuyin's single symbol `ㄩ` is unambiguous where pinyin's "u/ü" is not. Learner errors: unrounding /y/ to [i], or backing it to [u]. No length, no devoicing.

#### [ɹ̩] — `-i` (after `z c s`) — apical dental ("buzzed") vowel

Zhuyin has no separate symbol; the bare `ㄗ`/`ㄘ`/`ㄙ` implies it.

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `zi` | 字 | 字 | `ㄗ` | [tsɹ̩] | character/word | The pinyin "i" here is NOT [i] — it is a syllabic continuation of the dental sibilant: a buzzed [ɹ̩] with the tongue still in /s/ position. Zhuyin writes just `ㄗ` (no vowel letter), making the analysis explicit. |
| `ci` | 词 | 詞 | `ㄘ` | [tsʰɹ̩] | word/term | Aspirated dental affricate `c` /tsʰ/ + apical [ɹ̩]. Compare 词/詞 `ci` [tsʰɹ̩] with a hypothetical *[tsʰi] — the latter is not a Mandarin syllable; `c` never precedes real /i/. |
| `si` | 四 | 四 | `ㄙ` | [sɹ̩] | four | Fricative `s` /s/ + apical [ɹ̩]. Contrast 四 `si` [sɹ̩] (dental buzz) with 西 `xi` [ɕi] (real [i] after `x`) — the same pinyin letter "i", two utterly different vowels. |

**Allophony.** The DENTAL apical vowel [ɹ̩] (older notation [ɿ]) is the buzzing nucleus that occurs ONLY after the dental sibilants `z` /ts/, `c` /tsʰ/, `s` /s/ (`zi ci si`). It is best analyzed not as the vowel /i/ but as a syllabic prolongation of the preceding fricative — the tongue stays in dental/alveolar position and the syllable is carried by a voiced [z̩]-like buzz. Pinyin's choice to spell it "-i" is purely orthographic convention (so every syllable has a vowel letter); Zhuyin instead writes the initial alone (`ㄗ ㄘ ㄙ`) with no vowel sign, which transparently reflects the "empty rime" analysis. It must NOT be pronounced as [i]. It pairs with the retroflex apical [ɻ̩] (next entry); the two are in complementary distribution by sibilant series. No length, no tone-driven reduction beyond the normal.

#### [ɻ̩] — `-i` (after `zh ch sh r`) — apical retroflex ("buzzed") vowel

Zhuyin has no separate symbol; the bare `ㄓ`/`ㄔ`/`ㄕ`/`ㄖ` implies it.

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `zhi` | 知 | 知 | `ㄓ` | [ʈʂɻ̩] | to know | The pinyin "i" is a retroflex buzz: the tongue stays curled back in /ʂ/ position. Zhuyin `ㄓ` writes no vowel. NOT [ʈʂi]. |
| `chi` | 吃 | 吃 | `ㄔ` | [ʈʂʰɻ̩] | to eat | Aspirated retroflex affricate `ch` /ʈʂʰ/ + retroflex apical [ɻ̩]. |
| `shi` | 是 | 是 | `ㄕ` | [ʂɻ̩] | to be | One of the highest-frequency Mandarin syllables; `sh` /ʂ/ + retroflex buzz. Contrast 是 `shi` [ʂɻ̩] with 西 `xi` [ɕi] and 四 `si` [sɹ̩] — three different "-i" values. |
| `ri` | 日 | 日 | `ㄖ` | [ʐɻ̩] | sun/day | The voiced retroflex `r` /ʐ~ɻ/ + retroflex apical: `ri` ≈ [ʐɻ̩], essentially a held retroflex buzz. |

**Allophony.** The RETROFLEX apical vowel [ɻ̩] (older notation [ʅ]) is the buzzing nucleus that occurs ONLY after the retroflex series `zh` /ʈʂ/, `ch` /ʈʂʰ/, `sh` /ʂ/, `r` /ʐ~ɻ/ (`zhi chi shi ri`). Like its dental partner [ɹ̩] it is a syllabic continuation of the preceding sibilant — tongue curled back, no true vowel target — and pinyin's "-i" spelling is orthographic only; Zhuyin writes the bare initial (`ㄓ ㄔ ㄕ ㄖ`). The two apical vowels are in complementary distribution: dental [ɹ̩] after `z`/`c`/`s`, retroflex [ɻ̩] after `zh`/`ch`/`sh`/`r`. **TAIWAN NOTE:** `Guóyǔ` speakers often de-retroflex (`zh`/`ch`/`sh`/`r` → `z`/`c`/`s`), which can collapse the retroflex apical toward the dental one in casual speech; the toneless pinyin spelling stays unchanged. Never pronounce as [i].

#### /ɚ/ — `er` `ㄦ` — rhotacized central vowel (`er` final + erhua)

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `er` | 二 | 二 | `ㄦ` | [ɚ] | two | The `er` final as a full syllable: a single rhotacized central vowel [ɚ], the only r-coloured vowel in Mandarin. (Citation tone T4 `èr`.) |
| `er` | 儿 | 兒 | `ㄦ` | [ɚ] | child / diminutive suffix | The morpheme behind ERHUA: as a standalone word [ɚ], but as a suffix it fuses with the preceding final and rhotacizes it rather than forming its own syllable. |
| `huar` | 花儿 | 花兒 | `ㄏㄨㄚㄦ` | [xwaɚ̯] | flower (erhua) | ERHUA: 花 `hua` [xwa] + 儿/兒 `-r` rhotacizes the rime to [xwaɚ̯] — one syllable, not two. Characteristic of Beijing/`Pǔtōnghuà`; largely ABSENT in Taiwan `Guóyǔ` (花 `huā` with no `-r`). |
| `yìdiǎnr` | 一点儿 | 一點兒 | `ㄧ ㄉㄧㄢㄦ` | [i tjɑɚ̯] | a little (erhua) | Erhua restructures the rime: 点/點 `dian` [tjɛn] loses its `-n` coda and rhotacizes → [tjɑɚ̯]. Shows that erhua can DELETE a coda. `Pǔtōnghuà`-heavy; Taiwan typically 一點 `yìdiǎn` with no `-r`. |

**Allophony.** /ɚ/ is the single rhotacized (r-coloured) vowel of Mandarin — a central vowel with simultaneous tongue retroflexion/bunching, Zhuyin `ㄦ`. It appears (1) as the independent `er`-syllable (二 `èr`, 而 `ér`, 耳 `ěr`) with no initial, and (2) as the ERHUA / 儿化/兒化 suffix `-r`, which does NOT add a syllable but rhotacizes (and may restructure) the preceding final: `-n` and `-i` codas are typically dropped, `-ng` nasalizes the rhotic, and the nucleus colors to [ɚ] (花儿/花兒 `huār` [xwaɚ̯], 这儿/這兒 `zhèr` [ʈʂɚ̯], 玩儿/玩兒 `wánr` [waɚ̯]). Erhua is a HALLMARK of Beijing-based `Pǔtōnghuà` and is heavily used in northern speech; Taiwan `Guóyǔ` uses it minimally, so the same word often appears un-rhotacized there. This is Mandarin's only r-colouring — there is no English-style START/NORTH/NURSE series. The Peshitta reader tiers, being toneless and source-driven, follow the underlying pinyin; erhua is a connected-speech feature documented more fully in the sandhi/connected-speech section.

### Medial Glides (介音 `jièyīn`) — `i`/`u`/`ü` (/j w ɥ/)

Mandarin finals have a pre-nuclear MEDIAL (介音 `jièyīn`) slot that can hold one of three GLIDES, which are the non-syllabic counterparts of the high vowels /i u y/. These are not separate phonemes from the vowels — they are the same /i u y/ realized as on-glides when another vowel follows in the same syllable. They are central to the final inventory: the four traditional "rime classes" (四呼 `sìhū`) are defined by them — open (无介音/無介音, no glide), even / 齐齿/齊齒 (`i`-medial), closed / 合口 (`u`-medial), and rounded / 撮口 (`ü`-medial).

| Vowel | Glide | Pinyin | Zhuyin | Rime class (四呼) |
|---|---|---|---|---|
| /i/ | /j/ | `i-` / `y-` | `ㄧ` | 齐齿呼 / 齊齒呼 `qíchǐhū` ("even-teeth", `i`-medial) |
| /u/ | /w/ | `u-` / `w-` | `ㄨ` | 合口呼 `hékǒuhū` ("closed-mouth", `u`-medial) |
| /y/ | /ɥ/ | `ü-` / `yu-` | `ㄩ` | 撮口呼 `cuōkǒuhū` ("rounded-mouth", `ü`-medial) |
| (none) | — | — | — | 开口呼 / 開口呼 `kāikǒuhū` ("open-mouth", no medial: `a`, `e`, `ai`, `an`, `ang`…) |

#### /j/ — `i-` / `y-` `ㄧ` — the `i`-medial glide

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `jia` | 家 | 家 | `ㄐㄧㄚ` | [tɕja] | home/family | Medial /j/ between onset and nucleus: `ia` = [ja]. |
| `yao` | 要 | 要 | `ㄧㄠ` | [jɑʊ̯] | to want | Word-initial `i`-glide spelled "y-": `iao`/`yao` = [jɑʊ̯] (a triphthong with /j/ medial). |

齐齿呼 / 齊齒呼 `qíchǐhū`, the "even-teeth" (`i`-medial) rime class. /j/ also conditions vowel fronting in `ian` [jɛn], `iong` [jʊŋ].

#### /w/ — `u-` / `w-` `ㄨ` — the `u`-medial glide

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `hua` | 话 | 話 | `ㄏㄨㄚ` | [xwa] | speech/words | Medial /w/: `ua` = [wa]. |
| `wei` | 为 | 為 | `ㄨㄟ` | [wei̯] | for / to be | Word-initial `u`-glide spelled "w-": `uei` (pinyin "wei"/"-ui") = [wei̯]. |

合口呼 `hékǒuhū`, the "closed-mouth" (`u`-medial) rime class — rounded back on-glide.

#### /ɥ/ — `ü-` / `yu-` `ㄩ` — the `ü`-medial glide

| Pinyin | 简体字 | 繁體字 | Zhuyin | IPA | Gloss | Note |
|---|---|---|---|---|---|---|
| `yue` | 月 | 月 | `ㄩㄝ` | [ɥɛ] | moon/month | Front-rounded medial /ɥ/: `üe`/`yue` = [ɥɛ]. |
| `yuan` | 元 | 元 | `ㄩㄢ` | [ɥɛn] | first / yuan (currency) | `üan`/`yuan` = [ɥɛn]: front-rounded glide + raised /a/→[ɛ] + `-n`. |

撮口呼 `cuōkǒuhū`, the "rounded-mouth" (`ü`-medial) rime class — the front-rounded on-glide, found only before a small set of rimes (`üe`, `üan`, `ün`, and bare `ü`).

**Open class.** The fourth rime class is 开口呼 / 開口呼 `kāikǒuhū`, the "open-mouth" class with NO medial glide (`a`, `e`, `ai`, `an`, `ang`…). Together the 四呼 (open, `i`-, `u`-, `ü`-medial) organize the entire final inventory; the medials are what make a final "belong" to each class.

**Glide vs. vowel.** Phonemically the glides /j w ɥ/ are not extra segments but the high vowels /i u y/ in non-syllabic position. Pinyin shows this with the `i`↔`y` and `u`↔`w` spelling alternations (`i`→`yi`/`y-`, `u`→`wu`/`w-`, `ü`→`yu-`); Zhuyin uses the same `ㄧ ㄨ ㄩ` symbols for medial and nuclear roles alike.

### Vowel Quality Is Determined WITHIN the Final

Unlike Japanese (near-constant vowel quality) and unlike the fixed lexical-set qualities of English, Mandarin nuclear vowels — above all /a/, /ɤ/ ("e") and the high vowels — have surface qualities that are predicted by the rest of the rime (medial glide and coda). The phonemes are abstract targets; the final spells out the realization. This is why a compact phoneme set yields a large set of surface vowel colors and why the SAME pinyin vowel letter can denote several phones.

**Key conditioning patterns:**

| Phoneme / letter | Conditioning |
|---|---|
| /a/ | FRONTS before coronal `-n` (`an` [an], `ian` [jɛn]→[ɛ]) and BACKS before velar `-ng` (`ang` [ɑŋ]); central [A] in `ai`/`ao`. |
| /ɤ/ ("e") | Back [ɤ] bare, central [ə] before `-n`/`-ng`, front [ɛ] after `i-`/`ü-` glides (`ie`/`üe`), and [e] in `ei`. |
| pinyin `i` | Real [i] after most onsets, but apical [ɹ̩]/[ɻ̩] after `z c s` / `zh ch sh r`. |
| pinyin `u` | Back rounded [u] generally, but front-rounded /y/ after `j q x y`. |
| /o/ | Surfaces with a [w] on-glide after labials (`bo` [pwo]) and is the nucleus of `-uo` [wo]. |
| erhua /ɚ/ | Recolors and may restructure any final it attaches to. |

**Implication for readers.** Because of this, the Peshitta toneless-pinyin spine and the Zhuyin transcode are interpreted through these conditioning rules: the letters are stable, the phonetic values context-dependent. The Hanzi tiers (Simplified/Traditional) are a downstream character lookup and impose a citation tone that is NOT in the toneless source.

### 普通话 `Pǔtōnghuà` vs 国语 `Guóyǔ` — Vowel-Relevant Differences

The two standards share the vowel PHONEME system; surface differences relevant to this section are:

| Standard | Vowel-relevant profile |
|---|---|
| 普通话 / 普通話 `Pǔtōnghuà` | PRC Standard Mandarin (Beijing-based; Simplified characters; Hanyu Pinyin). Heavy ERHUA (花儿 `huār`, 一点儿 `yìdiǎnr`); full retroflex apical [ɻ̩] for `zh`/`ch`/`sh`/`r`; robust use of the back [ɤ] for bare `e`. |
| 国语 / 國語 `Guóyǔ` | Taiwan Standard Mandarin (Traditional characters; Zhuyin/Bopomofo). MINIMAL erhua (花 `huā`, 一點 `yìdiǎn` without `-r`); frequent DE-RETROFLEXION (`zh`/`ch`/`sh`/`r` → `z`/`c`/`s`), which can blur the retroflex vs dental apical contrast; some lexical pronunciation differences. The TONELESS pinyin/Zhuyin spelling is unchanged by these surface differences. |

**Shared.** Both agree on the seven core nuclei /a ɤ ɛ o i u y/, the medial glides /j w ɥ/, the front-rounded /y/, and the apical-vowel analysis. The divergences are surface/lexical, not phonemic.

### IPA Symbol Summary

Quick reference of the Mandarin nuclear vowels, apical vowels, the rhotic, and the medial glides, with pinyin/Zhuyin correspondences and principal realizations. Default values are `Pǔtōnghuà` (Beijing-based); `Guóyǔ` (Taiwan) variants noted inline. Mandarin has NO phonemic length and NO checked/free class system; TONE (documented separately) rides on these nuclei.

| Group | Members |
|---|---|
| Core nuclei | /a/, /ɤ/, /ɛ/, /o/, /i/, /u/, /y/ |
| Apical vowels | [ɹ̩] (dental, after `z c s`), [ɻ̩] (retroflex, after `zh ch sh r`) |
| Rhotic | /ɚ/ (`er` / erhua) |
| Medial glides | /j/ (`i`-medial), /w/ (`u`-medial), /ɥ/ (`ü`-medial) |

#### Principal Realizations

| Vowel | Zhuyin | Phoneme | Principal realizations |
|---|---|---|---|
| `a` | `ㄚ` | /a/ | [a] front (open / before `-n`) ~ [A] central (in `ai`/`ao`) ~ [ɑ] back (before `-ng`) ~ [ɛ] (`ian`/`üan`); low vowel, quality set by the rime. |
| `e` | `ㄜ` | /ɤ/ | [ɤ] back bare (喝 `he`) ~ [ə] before `-n`/`-ng` (很 `hen`) ~ [ɛ] after `i-`/`ü-` glide (别/別 `bie`) ~ [e] in `ei`; the "e" phoneme — NOT English schwa, NOT rounded. |
| `ê` | `ㄝ` | /ɛ/ | [ɛ] open-mid front; bare `ê` 欸 and the nucleus of `-ie`/`-üe` ([jɛ]/[ɥɛ]). Zhuyin `ㄝ` is distinct from `ㄜ`. |
| `o` | `ㄛ` | /o/ | [o] mid back rounded; after labials `bo`/`po`/`mo`/`fo` = [(p)wo]; nucleus of `-uo` [wo]; bare interjection `o` 哦. |
| `i` | `ㄧ` | /i/ | [i] close front unrounded as a true vowel (你 `ni`, 鸡/雞 `ji`); medial glide /j/ (家 `jia`). NOT the apical `-i` of `zi`/`zhi`. |
| `u` | `ㄨ` | /u/ | [u] close back ROUNDED (五 `wu`) — genuinely rounded, unlike Japanese /ɯ/; medial glide /w/ (我 `wo`). After `j q x y`, "u" is /y/, not /u/. |
| `ü` | `ㄩ` | /y/ | [y] close FRONT ROUNDED (绿/綠 `lü`, 去 `qu`, 鱼/魚 `yu`); medial glide /ɥ/ (月 `yue`). The vowel English/Japanese lack. Written "u" after `j q x y`, "ü" after `l n`. |
| `-i` (`z c s`) | `ㄗ`/`ㄘ`/`ㄙ` | [ɹ̩] | [ɹ̩]~[ɿ] dental apical buzz (字 `zi`, 四 `si`); a syllabic sibilant, NOT [i]; Zhuyin writes `ㄗ`/`ㄘ`/`ㄙ` alone. |
| `-i` (`zh ch sh r`) | `ㄓ`/`ㄔ`/`ㄕ`/`ㄖ` | [ɻ̩] | [ɻ̩]~[ʅ] retroflex apical buzz (知 `zhi`, 是 `shi`, 日 `ri`); NOT [i]; Zhuyin writes `ㄓ`/`ㄔ`/`ㄕ`/`ㄖ` alone; de-retroflexed in casual Taiwan `Guóyǔ`. |
| `er` | `ㄦ` | /ɚ/ | [ɚ]~[ɐɚ̯] rhotacized central vowel; the `er` syllable (二 `èr`) and the erhua suffix `-r` (花儿/花兒 `huār`); heavy in `Pǔtōnghuà`, minimal in `Guóyǔ`. |

**No length, no class.** Mandarin has NO phonemic vowel LENGTH (unlike the English /ː/ system and Japanese short/long) and NO lax/tense (checked/free) class system (unlike English). Vowel contrasts are carried by QUALITY plus medial/coda context, and crucially by the four LEXICAL TONES (documented in the tones/suprasegmentals section, not here).

**Context warning.** The single most important warning: Mandarin vowel LETTERS are not vowel SOUNDS one-to-one. "a" is [a]/[ɑ]/[ɛ] by coda; "e" is [ɤ]/[ə]/[ɛ]/[e] by context; "i" is [i] OR the apical buzz [ɹ̩]/[ɻ̩]; "u" is [u] OR front-rounded /y/. Read the rime, not just the letter.

**Front-rounded warning.** `ü` /y/ is a close FRONT ROUNDED vowel — round the lips as for [u] but keep the tongue forward as for [i]. Unrounding it to [i] or backing it to [u] are the two most audible errors; it is also invisibly hidden under the letter "u" after `j q x y` (`qu`/`xu`/`yu` = /tɕʰy ɕy y/).

**Schwa note.** There is no English-style weak/reduced vowel inventory. The schwa-like [ə] that appears is a CONTEXTUAL realization of /ɤ/ (before `-n`/`-ng` and in neutral-tone 轻声/輕聲 syllables), not a separate phoneme; neutral-tone reduction is tone-driven (documented under tones), not a vowel class.

---

*Section compiled by Shin.*

## Finals (韵母)

The finals (`韵母` / `韻母` *yùnmǔ*) of Standard Mandarin (`标准汉语` / `標準漢語`) are the complete RIME system that, together with the initials (`声母` / `聲母` *shēngmǔ*), exhausts the toneless syllable. A Mandarin syllable is **(initial)(final) + tone**, and the final itself has the internal structure **(medial glide) + nucleus + (coda)**:

- **MEDIAL** (`介音` *jièyīn*) ∈ { i /j/, u /w/, ü /ɥ/ }
- **NUCLEUS** ∈ { a /a/, o /o/, e /ɤ/, ê /ɛ/, i /i/, u /u/, ü /y/, apical -i [ɹ̩]/[ɻ̩], er /ɚ/ }
- **CODA** ∈ { -i/-o offglide, -n /n/, -ng /ŋ/, -r /ɚ/ (erhua) }

There are **NO coda obstruents** and **NO consonant clusters**: the only true codas are the two nasals /n/ and /ŋ/ plus the rhotic -er, so every final ends in a vowel, a glide, /n/, /ŋ/, or rhotacization. This inventory is documented in parallel for the two reference standards that frame the whole guide — `普通话` Pǔtōnghuà (PRC Standard Mandarin, Beijing-based phonology, SIMPLIFIED characters, Hanyu Pinyin) and `國語` Guóyǔ (Taiwan Standard Mandarin, TRADITIONAL characters, Zhuyin/Bopomofo) — which share an **IDENTICAL phonemic rime system**; they diverge only at the surface (Taiwan Guoyu has little or no ERHUA, so the rhotic `儿化` rimes below are essentially a Pǔtōnghuà phenomenon, and Taiwan de-retroflexion shifts the apical -i after zh/ch/sh/r toward the [ɹ̩] dental value). Phonemic transcription is in /slashes/, phonetic detail in [brackets], IPA per the 2015 revision.

The classic pedagogical organisation is the `四呼` *sì hū* ("four callings"):

- `开口呼` *kāikǒuhū* — open mouth, no medial
- `齐齿呼` *qíchǐhū* — even-teeth, i-medial /j/
- `合口呼` *hékǒuhū* — closed mouth, u-medial /w/
- `撮口呼` *cuōkǒuhū* — rounded mouth, ü-medial /ɥ/

Mandarin counts roughly **35–38 finals** depending on how the apical -i, ê, êr, and the marginal/erhua rimes are tallied. Each entry below gives pinyin, zhuyin (`注音` / `注音符號`), IPA, and a worked example as Hanzi (SIMPLIFIED + TRADITIONAL) with pinyin and gloss.

> **Note — the LANGUAGE is tonal; the reader tiers are toneless.** These rimes are the deterministic phonetic spine of the Chinese Peshitta reader tiers — the TONELESS PINYIN tier and its ZHUYIN transcode are built directly from this final-by-final mapping, and this section plus the initials section underpin the full syllable chart and the Peshitta pinyin transducer. The reader tiers are **toneless by design** (the Peshitta source IPA carries no tone); the language itself is **fully tonal** and tone is documented in the tones section — the finals listed here are the tone-bearing rimes onto which the four lexical tones and the neutral tone dock.

**Structural model note.** This section is the Mandarin analog of the Japanese guide's vowel/diphthong slot, but vastly expanded: Japanese has no phonemic diphthongs (its V+V are separate moras), whereas Mandarin's rime system is the heart of its phonology, with genuine diphthongs, triphthongs, and nasal-coda rimes generated by a **medial × nucleus × coda** combinatorics. Where the English guide enumerates diphthongs by Wells lexical set, this section enumerates Mandarin finals by the native `四呼` medial classes and by rime shape (simple / diphthong / triphthong / nasal), the organisation used in every Hanyu Pinyin and Zhuyin pedagogy.

---

### Final Structure: (medial) + nucleus + (coda)

The final decomposes as **`(medial) + nucleus + (coda)`**. The three component slots are itemized below.

#### Medials (介音 jièyīn)

The three high-vowel onglides that open the `齐齿` / `合口` / `撮口` final classes. A medial is phonemically the non-syllabic counterpart of /i u y/.

| Pinyin | Zhuyin | IPA | 四呼 class | Note |
|---|---|---|---|---|
| `i` | `ㄧ` | `/j/` | `齐齿呼` qíchǐhū (even-teeth) | Palatal onglide; spelled `y-` when it begins a zero-initial syllable (yi, ya, ye, yao, you, yan, yin, yang, ying, yong). |
| `u` | `ㄨ` | `/w/` | `合口呼` hékǒuhū (closed-mouth) | Labio-velar onglide; spelled `w-` in zero-initial syllables (wu, wa, wo, wai, wei, wan, wen, wang, weng). |
| `ü` | `ㄩ` | `/ɥ/` | `撮口呼` cuōkǒuhū (rounded-mouth) | Labio-palatal onglide; written `yu-` in zero-initial syllables (yu, yue, yuan, yun) and loses its umlaut to plain `u` after j/q/x/y (see Spelling Conventions). |

#### Nuclei (韵腹 yùnfù)

The syllable nucleus (`韵腹` *yùnfù*), the obligatory, most sonorous element.

| Pinyin | IPA | Note |
|---|---|---|
| `a` | `/a/` | Low central [a]; backs to [ɑ] before -ng and fronts to [æ]/[ɛ] before -n and after the i-medial (ian). |
| `o` | `/o/` | Mid back rounded; chiefly after b p m f (bo po mo fo, phonetically [pwo] etc.) and in the diphthong/triphthong rimes ao, ou, iao, iou. |
| `e` | `/ɤ/` | Close-mid back UNROUNDED [ɤ] in the open final `e` (he, ge); see ê for the front value used in ie/üe. |
| `ê` | `/ɛ/` | Open-mid front unrounded; the standalone `ㄝ` is rare (`诶` ê), but this is the nucleus heard in -ie and -üe (bie, lüe) and in -ei. |
| `i` | `/i/` | Close front unrounded — the TRUE [i] of bi, di, ji (NOT the apical -i, which is a separate rime, see below). |
| `u` | `/u/` | Close back rounded [u] (bu, gu, hu). |
| `ü` | `/y/` | Close front rounded [y] (nü, lü, ju, qu, xu, yu). |

#### Codas (韵尾 yùnwěi)

The optional rime ending (`韵尾` *yùnwěi*). Mandarin permits only vocalic offglides, two nasals, and the rhotic; there are **NO stop or obstruent codas**.

| Pinyin | IPA | Note |
|---|---|---|
| `-i` | `/i̯/` | Front offglide closing ai, ei, uai, uei. |
| `-o / -u` | `/u̯/` | Back/rounded offglide closing ao, ou, iao, iou (pinyin spells the offglide as -o in ao/iao but -u in ou/iou). |
| `-n` | `/n/` | Alveolar nasal coda (an, en, in, ün, …). |
| `-ng` | `/ŋ/` | Velar nasal coda (ang, eng, ing, ong, …). |
| `-r` | `/ɚ/` | Rhotic `儿化` erhua coda that restructures the rime; productive in Pǔtōnghuà, largely absent in Taiwan Guoyu. |

---

### Spelling Conventions

Hanyu Pinyin uses several abbreviated/contextual spellings for finals; the transducer must expand these to the underlying phonemic rime. Zhuyin, being non-Latin, writes the full rime and so exposes the underlying form directly.

| Rule | Detail | Zhuyin |
|---|---|---|
| `iou → -iu` | After an initial, the triphthong iou /jou̯/ is written `-iu` (`liu` 流, `jiu` 九); standalone it is `you`. The medial nucleus -o- is suppressed in spelling but present phonetically and in Zhuyin. | `ㄧㄡ` |
| `uei → -ui` | After an initial, the triphthong uei /wei̯/ is written `-ui` (`gui` 贵, `dui` 对); standalone it is `wei`. The medial -e- is suppressed in spelling but present (Zhuyin ㄨㄟ). | `ㄨㄟ` |
| `uen → -un` | After an initial, uen /wən/ is written `-un` (`lun` 论, `dun` 顿); standalone it is `wen`. The schwa is suppressed in spelling but present (Zhuyin ㄨㄣ). | `ㄨㄣ` |
| `ü → u after j q x y` | The front-rounded vowel ü loses its umlaut after j, q, x and as initial y because /u/ never occurs there, so no ambiguity arises: `ju` /tɕy/ 居, `qu` /tɕʰy/ 去, `xu` /ɕy/ 须, `yu` /y/ 鱼; likewise juan/quan/xuan/yuan = /-ɥɛn/ and jun/qun/xun/yun = /-yn/. The umlaut is RETAINED after n and l, where it contrasts with plain u: `nü` 女 /ny/ vs `nu` 奴 /nu/, `lü` 绿 /ly/ vs `lu` 路 /lu/. | `ㄩ` |
| `i/u/ü → y-/w-/yu- word-initially` | A final beginning with a medial glide and no preceding initial is respelled with y/w: i→yi, ia→ya, ie→ye, iou→you, ian→yan, in→yin, ing→ying, iong→yong; u→wu, ua→wa, uo→wo, uai→wai, uei→wei, uan→wan, uen→wen, uang→wang, ueng→weng; ü→yu, üe→yue, üan→yuan, ün→yun. | `n/a` |
| `apical -i is not the vowel /i/` | The `i` written after z c s and zh ch sh r is NOT /i/ but a syllabic apical/retroflex approximant: `zi ci si` = [ɹ̩] (dental/apical), `zhi chi shi ri` = [ɻ̩] (retroflex). Pinyin reuses the letter i; Zhuyin writes NOTHING after the initial (`ㄓ` = zhi, `ㄗ` = zi). | `（无 / 無 — bare initial）` |
| `o vs uo after labials` | After b p m f the rime written `-o` (bo po mo fo) is phonetically [pwo]/[pʰwo]/[mwo]/[fwo] — i.e. it contains the same [wo] glide as uo elsewhere — so `bo` and `duo` share the [wo] nucleus though spelled differently. Zhuyin writes `ㄅㄛ` (bo) vs `ㄉㄨㄛ` (duo). | — |

---

### Finals by Group

#### Simple Finals (单韵母 / 單韻母 dānyùnmǔ)

Single-vowel (monophthong) nuclei with no medial and no coda, plus the two apical "buzzed" rimes and the rhotic `er`. These are the `开口呼` (open-mouth) simple finals.

| Pinyin | Zhuyin | IPA | 四呼 | Example (简 / 繁) | Pinyin | Gloss | Note |
|---|---|---|---|---|---|---|---|
| `a` | `ㄚ` | `/a/` | `开口呼` | `八` / `八` | `bā` | eight | — |
| `o` | `ㄛ` | `/o/` | `开口呼` | `波` / `波` | `bō` | wave | Occurs chiefly after b p m f, phonetically [pwo]; standalone `o` /ɔ/ is an interjection (`哦`). |
| `e` | `ㄜ` | `/ɤ/` | `开口呼` | `饿` / `餓` | `è` | hungry | Close-mid back UNROUNDED [ɤ]; a frequent foreign-accent error is to round it to [o] or centralize to [ə]. |
| `ê` | `ㄝ` | `/ɛ/` | `开口呼` | `诶` / `誒` | `ê` | hey (interjection) | Marginal as a standalone syllable; its real importance is as the nucleus of -ie and -üe and as the offglide target of -ei. |
| `i` | `ㄧ` | `/i/` | `齐齿呼` | `一` / `一` | `yī` | one | True front [i]; written `yi` when standalone. Distinct from apical -i. |
| `u` | `ㄨ` | `/u/` | `合口呼` | `五` / `五` | `wǔ` | five | Written `wu` when standalone. |
| `ü` | `ㄩ` | `/y/` | `撮口呼` | `鱼` / `魚` | `yú` | fish | Front-rounded [y]; written `yu` standalone and `u` after j q x y (see Spelling Conventions). |
| `-i` (apical, dental) | `（ㄗ/ㄘ/ㄙ 后无符号）` | `[ɹ̩]` | `开口呼` | `四` / `四` | `sì` | four | Syllabic apical/dental approximant after z c s only (zi ci si); the `i` is orthographic, not the vowel /i/. |
| `-i` (apical, retroflex) | `（ㄓ/ㄔ/ㄕ/ㄖ 后无符号）` | `[ɻ̩]` | `开口呼` | `十` / `十` | `shí` | ten | Syllabic retroflex approximant after zh ch sh r (zhi chi shi ri). In Taiwan Guoyu de-retroflexion shifts this toward [ɹ̩]. |
| `er` | `ㄦ` | `/ɚ/` (~[aɚ̯]) | `开口呼` | `二` / `二` | `èr` | two | The rhotacized standalone rime (`er` 儿/兒, `èr` 二, `ěr` 耳); also the source of the `儿化` erhua suffix -r. Takes NO initial. |

#### Diphthong Finals (复韵母 / 複韻母 fùyùnmǔ)

Two-vowel rimes that glide from a fuller nucleus to a higher offglide (these are the open-mouth diphthongs; the medial-bearing diphthongs ia, ie, ua, uo, üe appear under the medial groups below). Mandarin diphthongs are **single gliding nuclei, NOT V+V sequences**.

| Pinyin | Zhuyin | IPA | 四呼 | Example (简 / 繁) | Pinyin | Gloss | Note |
|---|---|---|---|---|---|---|---|
| `ai` | `ㄞ` | `/ai̯/` | `开口呼` | `爱` / `愛` | `ài` | love | — |
| `ei` | `ㄟ` | `/ei̯/` | `开口呼` | `黑` / `黑` | `hēi` | black | — |
| `ao` | `ㄠ` | `/au̯/` | `开口呼` | `好` / `好` | `hǎo` | good | The offglide is back-rounded [u̯]; pinyin spells it `-o`, Zhuyin `ㄠ`. |
| `ou` | `ㄡ` | `/ou̯/` | `开口呼` | `狗` / `狗` | `gǒu` | dog | — |

#### Triphthong Finals (三合元音 sānhé yuányīn)

Medial + nucleus + offglide, a glide on both sides of the nucleus. All four arise by combining an i- or u-medial with a diphthong rime. Two of them (`iou`, `uei`) are SPELLING-CONTRACTED after an initial (see Spelling Conventions).

| Pinyin | Zhuyin | IPA | 四呼 | Standalone | Example (简 / 繁) | Pinyin | Gloss | Spelling note |
|---|---|---|---|---|---|---|---|---|
| `iao` | `ㄧㄠ` | `/jau̯/` | `齐齿呼` | `yao` | `小` / `小` | `xiǎo` | small | — |
| `iou` (`-iu`) | `ㄧㄡ` | `/jou̯/` | `齐齿呼` | `you` | `六` / `六` | `liù` | six | Written `-iu` after an initial (liu, jiu, qiu, xiu); standalone `you`. |
| `uai` | `ㄨㄞ` | `/wai̯/` | `合口呼` | `wai` | `快` / `快` | `kuài` | fast | — |
| `uei` (`-ui`) | `ㄨㄟ` | `/wei̯/` | `合口呼` | `wei` | `对` / `對` | `duì` | correct / toward | Written `-ui` after an initial (gui, dui, hui, zui); standalone `wei`. |

#### i-Medial Finals (齐齿呼 qíchǐhū)

Finals carrying the i-medial /j/ (excluding the already-listed iao and iou). Spelled with initial `y-` when there is no onset initial. Combines the /j/ onglide with simple, diphthong, and nasal rimes.

| Pinyin | Zhuyin | IPA | Type | Standalone | Example (简 / 繁) | Pinyin | Gloss | Note |
|---|---|---|---|---|---|---|---|---|
| `ia` | `ㄧㄚ` | `/ja/` | medial+nucleus | `ya` | `家` / `家` | `jiā` | home / family | — |
| `ie` | `ㄧㄝ` | `/jɛ/` | medial+nucleus (ê) | `ye` | `也` / `也` | `yě` | also | Nucleus is the front [ɛ] (ê), not the back [ɤ] of plain e. |
| `ian` | `ㄧㄢ` | `/jɛn/` | medial+nasal | `yan` | `天` / `天` | `tiān` | sky / day | The -a- raises to [ɛ] between the i-medial and -n, so ian = [jɛn], NOT [jan]. |
| `in` | `ㄧㄣ` | `/in/` | nucleus+nasal | `yin` | `心` / `心` | `xīn` | heart | Phonemically /jən/ → surfaces as [in]; pinyin/zhuyin treat i as the nucleus. |
| `iang` | `ㄧㄤ` | `/jaŋ/` | medial+nasal | `yang` | `想` / `想` | `xiǎng` | to think / want | — |
| `ing` | `ㄧㄥ` | `/iŋ/` | nucleus+nasal | `ying` | `明` / `明` | `míng` | bright | Phonemically /jəŋ/ → [iŋ]. |
| `iong` | `ㄩㄥ` | `/jʊŋ/` | medial+nasal | `yong` | `用` / `用` | `yòng` | to use | Despite the spelling "io", the nucleus is the rounded [ʊ]; Zhuyin writes it `ㄩㄥ` (ü-onset), reflecting the [ɥ]/[j]+[ʊŋ] articulation. |

#### u-Medial Finals (合口呼 hékǒuhū)

Finals carrying the u-medial /w/ (excluding the already-listed uai and uei). Spelled with initial `w-` when there is no onset initial. The labial-onset rime `-o` (bo po mo fo) phonetically belongs here as [wo].

| Pinyin | Zhuyin | IPA | Type | Standalone | Example (简 / 繁) | Pinyin | Gloss | Note |
|---|---|---|---|---|---|---|---|---|
| `ua` | `ㄨㄚ` | `/wa/` | medial+nucleus | `wa` | `花` / `花` | `huā` | flower | — |
| `uo` | `ㄨㄛ` | `/wo/` | medial+nucleus | `wo` | `国` / `國` | `guó` | country | Shares its [wo] nucleus with the labial-onset -o (bo/po/mo/fo). |
| `uan` | `ㄨㄢ` | `/wan/` | medial+nasal | `wan` | `短` / `短` | `duǎn` | short | — |
| `uen` (`-un`) | `ㄨㄣ` | `/wən/` | medial+nasal | `wen` | `论` / `論` | `lùn` | to discuss / theory | Written `-un` after an initial (lun, dun, sun, zhun); standalone `wen`. |
| `uang` | `ㄨㄤ` | `/waŋ/` | medial+nasal | `wang` | `黄` / `黃` | `huáng` | yellow | — |
| `ueng` | `ㄨㄥ` | `/wəŋ/` | medial+nasal | `weng` | `翁` / `翁` | `wēng` | old man | Occurs ONLY as the standalone syllable `weng` (no onset initial); when /wəŋ/ would follow an initial it surfaces as `-ong`. |
| `ong` | `ㄨㄥ` | `/ʊŋ/` | nucleus+nasal | (none; always after an initial) | `红` / `紅` | `hóng` | red | The post-initial counterpart of weng; phonemically /wəŋ/ but realised with a rounded [ʊ] nucleus, [ʊŋ]. Distinct from -eng [əŋ]. |

#### ü-Medial Finals (撮口呼 cuōkǒuhū)

Finals carrying the ü-medial /ɥ/. Occur after j q x (umlaut dropped → u), after n l (umlaut retained → ü), and standalone as `yu-`. Only four such finals exist.

| Pinyin | Zhuyin | IPA | Type | Standalone | Example (简 / 繁) | Pinyin | Gloss | Note / spelling note |
|---|---|---|---|---|---|---|---|---|
| `üe` | `ㄩㄝ` | `/ɥɛ/` | medial+nucleus (ê) | `yue` | `学` / `學` | `xué` | to study | Written `-ue` after j q x y (jue, que, xue, yue) and `-üe` after n l (nüe, lüe). |
| `üan` | `ㄩㄢ` | `/ɥɛn/` | medial+nasal | `yuan` | `元` / `元` | `yuán` | first / yuan (currency) | Written `-uan` after j q x y (juan, quan, xuan, yuan); the -a- raises to [ɛ], so üan = [ɥɛn]. |
| `ün` | `ㄩㄣ` | `/yn/` | nucleus+nasal | `yun` | `云` / `雲` | `yún` | cloud | Written `-un` after j q x y (jun, qun, xun, yun) — note this `-un` is /yn/, distinct from the u-medial `-un` = /wən/. |
| `ü` (üe-class simple) | `ㄩ` | `/y/` | nucleus | `yu` | `去` / `去` | `qù` | to go | The simple ü listed under Simple Finals is the bare `撮口呼` vowel; repeated here for the four-class completeness of cuōkǒuhū. |

#### Open-Mouth Nasal Finals (开口呼鼻韵母)

The no-medial nasal finals: nucleus + /n/ or /ŋ/. These complete the nasal-final set whose medial-bearing members appear under the i/u/ü groups above.

| Pinyin | Zhuyin | IPA | 四呼 | Example (简 / 繁) | Pinyin | Gloss | Note |
|---|---|---|---|---|---|---|---|
| `an` | `ㄢ` | `/an/` | `开口呼` | `看` / `看` | `kàn` | to look / watch | — |
| `en` | `ㄣ` | `/ən/` | `开口呼` | `很` / `很` | `hěn` | very | — |
| `ang` | `ㄤ` | `/aŋ/` | `开口呼` | `忙` / `忙` | `máng` | busy | The -a- backs to [ɑ] before -ng: ang = [ɑŋ]. |
| `eng` | `ㄥ` | `/əŋ/` | `开口呼` | `冷` / `冷` | `lěng` | cold | Contrast with -ong [ʊŋ]; -eng is the unrounded [əŋ]. |

---

### Medial × Rime Combinatorics

The Mandarin final inventory is generated by combining the four `四呼` medial classes (Ø, i-, u-, ü-) with the available nuclei/codas. **Not every cell is filled; the gaps are systematic.** This table is the combinatoric skeleton the syllable chart and the Peshitta pinyin transducer expand.

| 四呼 class | Medial | Finals |
|---|---|---|
| `开口呼` (open-mouth) | Ø | `a`, `o`, `e`, `ê`, `-i(apical)`, `er`, `ai`, `ei`, `ao`, `ou`, `an`, `en`, `ang`, `eng` |
| `齐齿呼` (even-teeth) | i- /j/ | `i`, `ia`, `ie`, `iao`, `iou(-iu)`, `ian`, `in`, `iang`, `ing`, `iong` |
| `合口呼` (closed-mouth) | u- /w/ | `u`, `ua`, `uo`, `uai`, `uei(-ui)`, `uan`, `uen(-un)`, `uang`, `ueng`, `ong` |
| `撮口呼` (rounded-mouth) | ü- /ɥ/ | `ü`, `üe`, `üan`, `ün` |

**Systematic gaps.** There is no \*io; \*iai is marginal/archaic (`崖` has the standard Pǔtōnghuà reading `yá`, with the older/variant reading `yái` as the lone near-survivor of the -iai rime); no \*üng/\*üong (the rounded-front medial does not combine with -ng except via iong, written `io-` but Zhuyin `ㄩㄥ`). `-ong` is classed as `合口呼`: it is the post-initial counterpart of `weng` (合口 /wəŋ/ → [ʊŋ]), carrying the rounded /w/-type onset, so it is listed in the `合口` set rather than among the open-mouth nasals (which are exactly an/en/ang/eng). The apical `-i` and `er` take no medial and no other rime.

**Count summary.** Counting strictly by the four `四呼` arrays above: open-mouth `开口呼` = **14** (6 simples a/o/e/ê/-i(apical)/er — the two apical -i collapsed to one — + 4 diphthongs ai/ei/ao/ou + 4 nasals an/en/ang/eng, with -ong excluded as 合口), the **10** `齐齿` finals, the **10** `合口` finals (incl. -ong as the post-initial counterpart of weng), and the **4** `撮口` finals = **38 finals**.

> **NOTE on de-duplication.** The worked Finals-by-Group entries list bare `ü` twice — once under Simple Finals (`鱼` yú) and once under `撮口呼` (`去` qù) for four-class completeness — and split the apical `-i` into its dental [ɹ̩] and retroflex [ɻ̩] sub-rimes. De-duplicating bare `ü` and collapsing the two apical -i into one, and/or excluding the marginal `ê`/`êr`, yields the commonly cited **35–37**.

---

### Erhua Rime Restructuring (儿化)

`儿化` / `兒化` *érhuà* — the suffixation of the rhotic `-r` /ɚ/ (the `er` morpheme, `儿`/`兒`) onto a final, which does NOT simply append [ɚ] but **RESTRUCTURES** the rime: codas /n/ and the front offglide -i are typically dropped, the velar coda /ŋ/ nasalizes-and-rhotacizes the vowel, and the apical -i and -i nucleus are replaced by [ɚ]. Erhua is a robust feature of Beijing/Pǔtōnghuà phonology (diminutive, lexical, and grammatical) and is largely **ABSENT** from Taiwan Guoyu, so the Peshitta toneless-pinyin spine treats `-r` as an optional Pǔtōnghuà overlay, not a core rime. Pinyin simply adds `-r`; Zhuyin adds `ㄦ`.

| Input final | Result IPA | Rule | Example (简 / 繁) | Pinyin | Example IPA | Gloss |
|---|---|---|---|---|---|---|
| `a / o / e / u / ü` | [aɚ̯] / [oɚ̯] / [ɤɚ̯] / [uɚ̯] / [yɚ̯] | vowel + [ɚ] offglide (simple append) | `花儿` / `花兒` | `huār` | [xwaɚ̯] | flower (dim.) |
| `-ai / -ei / -an / -en` (coda -i or -n dropped) | [aɚ̯] / [əɚ̯] / [aɚ̯] / [əɚ̯] | front offglide -i and nasal coda -n are DELETED, then [ɚ] is added | `一点儿` / `一點兒` | `yìdiǎnr` | [i˥˩tjaɚ̯] | a little (bit) |
| `-i` (apical, after z c s zh ch sh r) / `-i` (in ji, qi, …) | [ɚ] / [jɚ] | the apical [ɹ̩]/[ɻ̩] is wholly replaced by [ɚ]; the true [i] nucleus inserts a glide | `事儿` / `事兒` | `shìr` | [ʂɚ˥˩] | matter / affair |
| `-ng` finals (ang eng ing ong …) | nasalized rhotacized vowel, e.g. [ɑ̃ɚ̯] / [ə̃ɚ̯] / [ʊ̃ɚ̯] | the velar nasal coda /ŋ/ is lost as a segment but its nasality spreads onto the rhotacized vowel (vowel nasalization + [ɚ]) | `空儿` / `空兒` | `kòngr` | [kʰʊ̃ɚ̯˥˩] | free time |
| `-in / -ün` (front nasals) | [jɚ] / [ɥɚ] | the -n is dropped and the high front medial glide is retained before [ɚ] | `今儿` / `今兒` | `jīnr` | [tɕjɚ˥] | today (colloq.) |

**Taiwan note.** In `國語` Guóyǔ erhua is rare and largely confined to a handful of lexicalized items (e.g. `這兒`/`那兒` are usually replaced by `這裡`/`那裡` zhèlǐ/nàlǐ); the de-retroflexed accent further reduces audible rhotacization. The toneless-pinyin reader tier therefore mirrors the Pǔtōnghuà form while flagging erhua as optional.

---

### Reference Standards

Both standards share **ONE phonemic final inventory**; the divergences are surface/lexical (erhua presence, retroflexion degree) and never alter the toneless pinyin spelling on which the Peshitta reader tiers are built.

| Standard | Label | Script tier | Rime notes |
|---|---|---|---|
| `普通话` Pǔtōnghuà | PRC Standard Mandarin | SIMPLIFIED `简体字` + Hanyu Pinyin | Full erhua system; retroflex apical -i [ɻ̩] after zh ch sh r is maintained; the rime inventory and IPA values above are the Pǔtōnghuà reference. |
| `國語` Guóyǔ | Taiwan Standard Mandarin | TRADITIONAL `繁體字` + Zhuyin/Bopomofo `注音符號` | Phonemically identical rime inventory. Surface differences: minimal erhua (the rhotic rimes above are essentially absent); de-retroflexion pulls the apical -i of zhi/chi/shi/ri toward the dental [ɹ̩]; -eng/-ing and -en/-in may merge for some speakers; some lexical readings differ (e.g. `和` hàn ~ hé) but the toneless rime spelling is unchanged. |

---

### Note: the Peshitta reader tiers are TONELESS

The six Chinese Peshitta tiers (Scholarly, Pretty, Toneless Pinyin, Zhuyin, Hanzi-Simplified, Hanzi-Traditional) draw their phonetic spine from this final inventory: the deterministic **TONELESS PINYIN** tier writes each rime in its standard pinyin spelling (expanding the `-iu`/`-ui`/`-un` contractions per Spelling Conventions when reconstructing the underlying form), the **ZHUYIN** tier is a one-to-one transcode of that pinyin (using the full `ㄧㄡ`/`ㄨㄟ`/`ㄨㄣ` rime symbols), and the two Hanzi tiers are a downstream character lookup that unavoidably imposes a citation tone per character (an artifact, not a Peshitta source feature). Because the source IPA carries no tone, the reader tiers are toneless; the finals here are nonetheless the **tone-bearing rimes of the living language**, onto which the four lexical tones + neutral tone dock (documented in the tones section).

**Companion files (repo-relative):**

- `Chinese/chinese_pronunciation_guide.md`
- `Chinese/Peshita_Chinese/Pinyin/`
- `Chinese/Peshita_Chinese/Zhuyin/`
- `Chinese/Peshita_Chinese/Hanzi_Simplified/`
- `Chinese/Peshita_Chinese/Hanzi_Traditional/`

*Section authored by Shin.*

## The Pinyin Syllable Chart (声母 × 韵母)

拼音音节表（声母 × 韵母）— The Pinyin Syllable Chart (Initial × Final Matrix)

Systematic **INITIAL** (声母 *shēngmǔ*) **× FINAL** (韵母 *yùnmǔ*) combination matrix — the Mandarin analog of a consonant×vowel (CV) table. Because Mandarin is an isolating, tonal, one-syllable-per-morpheme language with a small, highly constrained syllable canon ((C)(G)V(C)+TONE, no clusters, codas only /n ŋ ɚ/), the natural unit tabulated here is the **TONELESS SYLLABLE** (the 声母+韵母 cell), not a bare phoneme: each licit cell gives the standard Hanyu Pinyin spelling, the Zhuyin/Bopomofo transcode, and a toneless IPA. Mandarin admits only ~400 distinct TONELESS syllables (≈1,300 once the four lexical tones + neutral are layered on), so the matrix is overwhelmingly **GAPS**: most initial×final pairings are phonotactically ILLEGAL and are marked accordingly. The matrix encodes the language's signature co-occurrence restrictions — `j`/`q`/`x` occur ONLY before high front i-/ü- finals (and never before u-/back finals), while the homorganic-looking `g`/`k`/`h`, `z`/`c`/`s`, and `zh`/`ch`/`sh` series NEVER occur before those same i-/ü- finals; the so-called "apical vowels" written `-i` are NOT /i/ but [ɹ̩] after `z`/`c`/`s` and [ɻ̩] after `zh`/`ch`/`sh`/`r`; and the zero-initial finals are respelled with `y-`/`w-` glide letters (i→yi, u→wu, ü→yu, ie→ye, uo→wo, etc.). This chart deliberately omits tone — both because the matrix tabulates the toneless syllable spine and because the downstream Peshitta READER TIERS are toneless by design — but **TONE is a fully contrastive, lexical feature of the LANGUAGE itself** (mā/má/mǎ/mà 妈/麻/马/骂) and is documented richly in the suprasegmentals and tone sections; here only citation/example glosses occasionally cite a tone for identification. Reference standard: 普通话 *Pǔtōnghuà* (Beijing-based PRC Standard Mandarin). Read every cell together with its row phonetic note and the co-occurrence-restrictions block.

- **Reference standard:** *Pǔtōnghuà* (普通话) — PRC Standard Mandarin, Beijing-based phonology; Hanyu Pinyin; Simplified characters (ISO 639-3 `cmn`)
- **Secondary reference standard:** *Guóyǔ* (國語) — Taiwan Standard Mandarin; Zhuyin/Bopomofo (pedagogical); Traditional characters
- **Transcription level:** toneless broad phonetic IPA per cell (phonemic backbone with the principal vowel-conditioned surface allophones noted per row)
- **Unit of analysis:** the toneless Mandarin **SYLLABLE** (声母 initial + 韵母 final), the contrastive minimal unit of the chart; tone is a separate, fully lexical layer documented elsewhere

### Syllable Inventory Counts

| Inventory | Count | Note |
|---|---|---|
| Toneless syllables | ≈400 distinct toneless syllables (the cells of this chart) | Commonly cited as ~410–415 including rare/colloquial forms. |
| Tone-bearing syllables | ≈1,300 | Once the four lexical tones (and the neutral tone) are layered on — but no toneless syllable carries all five, and many carry only one or two, so the product is far below 400×5. |

> **Note:** The small toneless inventory + heavy phonotactic gapping is why this matrix is mostly empty cells. The ~1,300 figure is a **LANGUAGE** fact (tone is contrastive); the chart itself stays toneless because it tabulates the syllable spine and feeds the toneless Peshitta reader tiers.

### Romanization & Script Systems

| System | Name | Description |
|---|---|---|
| Hanyu Pinyin | 汉语拼音 (Hanyu Pinyin) | Official PRC romanization (1958), Latin letters; the deterministic phonetic spine and the default in this chart and in the Pinyin reader tier. Tones marked with diacritics (ā á ǎ à) in the LANGUAGE, but **OMITTED here** (toneless chart). |
| Zhuyin / Bopomofo | 注音符号 / 注音符號 (Zhuyin Fuhao, Bopomofo) | Taiwan pedagogical phonetic script, 37 letters (ㄅㄆㄇㄈ…) + tone marks; given per cell as the indigenous-script transcode of the pinyin. Bare/toneless Zhuyin conventionally defaults to Tone 1, so "toneless Zhuyin" is mildly ambiguous in a way toneless Pinyin is not — flagged here, tone marks deliberately not shown. |
| Wade–Giles | Wade–Giles | Older romanization (e.g. pinyin b/p/d/t/g/k = WG p/p'/t/t'/k/k'; pinyin zh/ch/j/q = WG ch/ch'); noted where a cell's traditional spelling differs markedly. Not used in the reader tiers. |

**Spelling conventions.** Pinyin abbreviates several full finals after certain initials: `iou`→`-iu` (liù 六), `uei`→`-ui` (huí 回), `uen`→`-un` (lún 轮); the ü dots drop after `j`/`q`/`x`/`y` (`ju`=jü, `qu`=qü, `xu`=xü, `yu`=yü) but are **KEPT** after `n`/`l` (nü 女, lü 绿). These are spelling rules, not sound changes; the IPA column restores the underlying form.

### Finals Used as Columns

The column headers of the matrix below are a **REPRESENTATIVE diagnostic set** chosen to expose every major co-occurrence restriction (the simple nuclei a o e i u ü, the special apical `-i`, plus sample diphthong/nasal finals ai ao an ang):

| | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|
| `a` | `o` | `e` | `i` | `u` | `ü` | `-i (apical)` | `ai` | `ao` | `an` | `ang` |

> **Note:** Mandarin has ~35–38 finals — far more than fit one printable row of cells — so the column headers are a diagnostic subset. The full final inventory (`ei ou`; `iao iou/-iu uai uei/-ui`; `en eng ong ian in iang ing iong uan un/uen uang ueng üan ün`; `er`) is enumerated in the Finals Inventory below and in the dedicated finals section; **each matrix row's "Other legal finals" column lists ALL the finals that initial legally takes**, not only the representative columns.

### Finals Inventory (韵母)

The full inventory of finals, organized by class. Phonemic = /slashes/; the Zhuyin transcode follows.

#### Simple Nuclei

| Pinyin | Phonemic | Zhuyin | Note |
|---|---|---|---|
| `a` | /a/ | `ㄚ` | |
| `o` | /o/ | `ㄛ` | Chiefly after b p m f and as interjection. |
| `e` | /ɤ/ | `ㄜ` | |
| `ê` | /ɛ/ | `ㄝ` | Rare standalone; nucleus of ie/üe. |
| `i` | /i/ | `ㄧ` | True high front [i]; **NOT** the apical `-i`. |
| `u` | /u/ | `ㄨ` | |
| `ü` | /y/ | `ㄩ` | |

#### Apical Vowels

| Environment | Phonetic | Example | Note |
|---|---|---|---|
| `-i` after z c s | [ɹ̩] (syllabic dental approximant) | zi ci si 资雌思 | |
| `-i` after zh ch sh r | [ɻ̩] (syllabic retroflex approximant) | zhi chi shi ri 知吃诗日 | |

> **Note:** Written with the **SAME letter** ⟨`i`⟩ as the high-front /i/, but phonetically a syllabic continuation of the preceding sibilant, never [i]. Zhuyin writes these as the bare initial with no vowel letter (`ㄓ` = zhi, `ㄗ` = zi).

#### Diphthongs, Medial-Glide & Nasal Finals

| Class | Finals (pinyin /IPA/ Zhuyin) |
|---|---|
| Rhotic | `er` /ɚ/ `ㄦ` — the rhotic syllable (二 èr) and the basis of **ERHUA** (儿化 -r suffixation: 花儿 huār); takes the zero initial only. |
| Diphthongs | `ai` /ai/ `ㄞ`, `ei` /ei/ `ㄟ`, `ao` /au/ `ㄠ`, `ou` /ou/ `ㄡ` |
| i-medial finals | `ia` /ja/ `ㄧㄚ`, `ie` /jɛ/ `ㄧㄝ`, `iao` /jau/ `ㄧㄠ`, `iou(-iu)` /jou/ `ㄧㄡ`, `ian` /jɛn/ `ㄧㄢ`, `in` /in/ `ㄧㄣ`, `iang` /jaŋ/ `ㄧㄤ`, `ing` /iŋ/ `ㄧㄥ`, `iong` /jʊŋ/ `ㄩㄥ` |
| u-medial finals | `ua` /wa/ `ㄨㄚ`, `uo` /wo/ `ㄨㄛ`, `uai` /wai/ `ㄨㄞ`, `uei(-ui)` /wei/ `ㄨㄟ`, `uan` /wan/ `ㄨㄢ`, `uen(-un)` /wən/ `ㄨㄣ`, `uang` /waŋ/ `ㄨㄤ`, `ueng` /wəŋ/ `ㄨㄥ` |
| ü-medial finals | `üe` /ɥɛ/ `ㄩㄝ`, `üan` /ɥɛn/ `ㄩㄢ`, `ün` /yn/ `ㄩㄣ` |
| n-nasal finals | `an` /an/ `ㄢ`, `en` /ən/ `ㄣ` |
| ng-nasal finals | `ang` /aŋ/ `ㄤ`, `eng` /əŋ/ `ㄥ`, `ong` /ʊŋ/ `ㄨㄥ` |

> **Note:** Codas are restricted to /n/, /ŋ/, and the rhotic /ɚ/ — no other consonant may close a syllable, and there are **NO consonant clusters** anywhere. Medial glides i/u/ü = /j w ɥ/.

### Initials Inventory (声母)

**21 consonant initials + the zero initial (∅).** NO voicing contrast in Mandarin; the laryngeal contrast is **ASPIRATION** (unaspirated b d g z zh j vs aspirated p t k c ch q). The matrix rows below are grouped: labials (b p m f), alveolars (d t n l), and the **three sibilant series that are in complementary distribution by following vowel** — velars g k h (+ back/open finals), dental sibilants z c s (+ back/open finals & apical `-i`), retroflexes zh ch sh r (+ back/open finals & apical `-i`), alveolo-palatals j q x (ONLY before i-/ü- finals) — plus the zero-initial (y/w-spelled) row.

### Co-occurrence Restrictions

This block is the load-bearing key to the whole chart; read every cell against it.

| Restriction | Statement |
|---|---|
| **j/q/x only before high front** | `j` /tɕ/, `q` /tɕʰ/, `x` /ɕ/ occur **ONLY** before the high front vocoids — the i-finals (i, ia, ie, iao, iou, ian, in, iang, ing, iong) and the ü-finals (ü, üe, üan, ün). They **NEVER** occur before a, o, e, u, the apical `-i`, or any u-medial/back final. Because the ü dots are dropped after j/q/x, a written ⟨`ju qu xu`⟩ is always /tɕy tɕʰy ɕy/ (= jü qü xü), never /u/. |
| **g/k/h, z/c/s, zh/ch/sh/r never before high front i-/u-** | Conversely, `g`/`k`/`h`, `z`/`c`/`s`, and `zh`/`ch`/`sh`/`r` **NEVER** occur before the front i-/ü- finals. They take a, o (rare), e, u, the back/open diphthong & nasal finals, and — for z/c/s and zh/ch/sh/r — the **APICAL `-i`**. This complementary distribution (j/q/x vs g/k/h ~ z/c/s ~ zh/ch/sh) is the central gapping principle of the whole chart: the four series carve up the vowel space so cleanly that some analyses treat j/q/x as allophones of the others. |
| **Apical -i only after sibilants** | The apical final `-i` ([ɹ̩]/[ɻ̩]) occurs **ONLY** after z c s (→[ɹ̩]) and zh ch sh r (→[ɻ̩]). It NEVER follows any other initial and never stands alone. The high-front /i/ ([i]) occurs after b p m d t n l and j q x — but crucially NOT after z c s zh ch sh r (those take the apical `-i` instead). So the single letter ⟨`i`⟩ spells two completely different sounds depending on the initial: `zi` [tsɹ̩] vs `di` [ti]. |
| **f and the labials** | `f` /f/ takes only a small set of finals (a o u and the an/en/ang/eng/ou nasals etc.); b p m f generally do NOT take ü-finals, and `o` /o/ as a simple nucleus occurs almost exclusively after b p m f (bo po mo fo) — elsewhere /o/ surfaces inside uo (e.g. duo, guo). |
| **r — zero in finals** | `r` /ʐ~ɻ/ patterns with the retroflex series (takes back/open finals + apical `-i`) but, being the voiced member, has gaps the voiceless zh/ch/sh fill (no "rai", etc.). |
| **Zero-initial y/w respelling** | A syllable with no onset consonant but a high vocoid onset is **RESPELLED**: initial i→yi/y- (i→yi, ie→ye, ia→ya, iou→you, in→yin, ing→ying, iang→yang, iong→yong), initial u→wu/w- (u→wu, uo→wo, uan→wan, uei→wei, uen→wen, ueng→weng), initial ü→yu/yu- (ü→yu, üe→yue, üan→yuan, ün→yun). The y/w are ORTHOGRAPHIC glide markers, **not added consonants** — phonetically these are glide-initial or bare-vowel finals. Pure a/o/e/ai/ao/an/ang/ou/en/eng/er/ê take the bare zero initial with no y/w (a 啊, en 恩, ai 哀, ang 昂, er 二). |

### Phonology Notes

- **No voicing — aspiration instead.** Mandarin obstruents are uniformly **VOICELESS**; the contrast within each pair is aspiration: `b` [p] / `p` [pʰ], `d` [t] / `t` [tʰ], `g` [k] / `k` [kʰ], `z` [ts] / `c` [tsʰ], `zh` [ʈʂ] / `ch` [ʈʂʰ], `j` [tɕ] / `q` [tɕʰ]. The Pinyin "voiced" letters (b d g) denote **UNASPIRATED voiceless stops**, a frequent source of L2 error. Only m n l r ng (and the glides) are truly voiced.
- **Tone is lexical but off-chart.** Tone is the LANGUAGE'S signature contrast (4 lexical tones T1 ˥ / T2 ˧˥ / T3 ˨˩˦ / T4 ˥˩ + neutral 轻声), fully contrastive at the syllable level (mā 妈 / má 麻 / mǎ 马 / mà 骂). This **CHART is toneless on purpose** — it tabulates the toneless syllable spine and feeds the toneless Peshitta reader tiers — so no tone diacritic appears in the pinyin/zhuyin/IPA cells. Tone, tone sandhi (T3+T3→T2+T3; 一/不 sandhi), erhua, and the neutral tone are documented in the suprasegmentals / tone sections, **NOT here**.
- **Apical-vowel realization.** The `-i` after sibilants is a SYLLABIC continuation of the consonant's frication/approximation: [ɹ̩] (dental, after z c s) and [ɻ̩] (retroflex, after zh ch sh r). Some descriptions write [z̩]/[ʐ̩] or [ɿ]/[ʅ] (Sinological IPA). Treat them as the vocalic nucleus of an otherwise onset-only syllable, **never** as [i].
- **e allophony.** The nucleus written ⟨`e`⟩ is /ɤ/ in open syllables (e 饿, ge, ke, he, ze, ce, se, zhe, che, she, re, de, te, ne, le) but surfaces as [ɛ]/[e] inside ie/üe and as [ə] inside en/eng/uen/uei. The chart's IPA restores the contextual quality.
- **o distribution.** Standalone simple /o/ `ㄛ` occurs essentially only after labials (bo po mo fo, where it is phonetically [u̯ɔ]) and as interjections (o 哦, yo); elsewhere the back-mid rounded vowel appears as the nucleus of `-uo` (duo guo zhuo wo).
- **n/l keep the ü umlaut.** After `n` and `l`, BOTH u-finals and ü-finals exist and contrast, so the umlaut is mandatory in spelling: `nu` 努 /nu/ vs `nü` 女 /ny/; `lu` 路 /lu/ vs `lü` 绿 /ly/. This is the **only** environment where the ü dots are orthographically required.
- **Retroflex series is apical.** `zh ch sh r` are apico-postalveolar/retroflex [ʈʂ ʈʂʰ ʂ ʐ~ɻ], distinct from the alveolo-palatal `j q x` [tɕ tɕʰ ɕ]. In Putonghua they are robustly distinguished from the dentals z c s; their MERGER toward z c s is the principal Guoyu/southern surface difference (see Secondary-Standard Notes).

### Secondary Standard Notes (Putonghua vs Guoyu)

The toneless **SYLLABLE INVENTORY** — i.e. the set of legal cells in this chart — is essentially **SHARED** between Putonghua (普通话) and Taiwan Guoyu (國語); the differences are surface-phonetic, suprasegmental, and lexical, and **DO NOT** change the toneless pinyin spelling:

1. **Retroflex realization.** Putonghua keeps a sharp `zh/ch/sh/r` [ʈʂ ʈʂʰ ʂ ʐ] vs `z/c/s` [ts tsʰ s] contrast; much Taiwan Guoyu (and southern Mainland speech) **DE-RETROFLEXES**, merging zh→z, ch→c, sh→s, and weakening r→[z] or a glide/zero (so 是 shì may sound like sì, 知道 like zīdào). The chart gives the Putonghua retroflex values as citation.
2. **Erhua.** Pervasive in Beijing Putonghua (花儿 huār, 一点儿 yìdiǎnr), nearly **ABSENT** in Guoyu (花 huā).
3. **Apical `-i`.** Realized identically in spelling; the retroflex apical [ɻ̩] flattens toward the dental [ɹ̩] in de-retroflexing accents.
4. **Lexical/tonal differences.** Fewer neutral tones and some lexical pronunciation differences in Guoyu (垃圾 lèsè vs lājī, 和 hàn vs hé, 企 qì vs qǐ) — lexical/tonal, not syllable-structural.

> **Net:** same chart, different surface retroflex and erhua behavior. In a fully de-retroflexed accent the four cells {zhi chi shi ri} and {zi ci si} can collapse, and the apical-vowel distinction [ɻ̩]~[ɹ̩] neutralizes; but the **STANDARD** (both PRC and Taiwan prescriptive) maintains the contrast, so it is kept distinct in this matrix.

### Matrix Legend

| Field | Meaning |
|---|---|
| Cell fields | Each licit cell gives: **pinyin** (toneless), **zhuyin** (Bopomofo, tone unmarked), **ipa** (toneless broad transcription). |
| Illegal marker | `—` marks a phonotactically **ILLEGAL** or unattested initial×final pairing (the majority of the grid). |
| Representative vs full | The column finals are a diagnostic subset for quick comparison; each row's "Other legal finals" column includes the row's full legal final set, so absences there are real gaps. |

### Initial × Final Matrix (声母 × 韵母)

Each licit cell gives the **toneless pinyin**, the **Zhuyin** transcode, and the **toneless IPA** (phonemic backbone /…/ realized phonetically per row). `—` = phonotactically illegal/unattested. Columns are the representative diagnostic finals; the final column enumerates every other legal final for that initial.

| Initial | Zhuyin | IPA | Series | `a` | `o` | `e` | `i` | `u` | `ü` | `-i (apical)` | `ai` | `ao` | `an` | `ang` | Other legal finals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `b` | `ㄅ` | [p] | labial | `ba` `ㄅㄚ` [pa] | `bo` `ㄅㄛ` [pwo] | — | `bi` `ㄅㄧ` [pi] | `bu` `ㄅㄨ` [pu] | — | — | `bai` `ㄅㄞ` [pai] | `bao` `ㄅㄠ` [pau] | `ban` `ㄅㄢ` [pan] | `bang` `ㄅㄤ` [paŋ] | bei ㄅㄟ [pei], ben ㄅㄣ [pən], beng ㄅㄥ [pəŋ], bie ㄅㄧㄝ [pjɛ], biao ㄅㄧㄠ [pjau], bian ㄅㄧㄢ [pjɛn], bin ㄅㄧㄣ [pin], bing ㄅㄧㄥ [piŋ] |
| `p` | `ㄆ` | [pʰ] | labial | `pa` `ㄆㄚ` [pʰa] | `po` `ㄆㄛ` [pʰwo] | — | `pi` `ㄆㄧ` [pʰi] | `pu` `ㄆㄨ` [pʰu] | — | — | `pai` `ㄆㄞ` [pʰai] | `pao` `ㄆㄠ` [pʰau] | `pan` `ㄆㄢ` [pʰan] | `pang` `ㄆㄤ` [pʰaŋ] | pei ㄆㄟ [pʰei], pou ㄆㄡ [pʰou], pen ㄆㄣ [pʰən], peng ㄆㄥ [pʰəŋ], pie ㄆㄧㄝ [pʰjɛ], piao ㄆㄧㄠ [pʰjau], pian ㄆㄧㄢ [pʰjɛn], pin ㄆㄧㄣ [pʰin], ping ㄆㄧㄥ [pʰiŋ] |
| `m` | `ㄇ` | [m] | labial | `ma` `ㄇㄚ` [ma] | `mo` `ㄇㄛ` [mwo] | `me` `ㄇㄜ` [mɤ] | `mi` `ㄇㄧ` [mi] | `mu` `ㄇㄨ` [mu] | — | — | `mai` `ㄇㄞ` [mai] | `mao` `ㄇㄠ` [mau] | `man` `ㄇㄢ` [man] | `mang` `ㄇㄤ` [maŋ] | mei ㄇㄟ [mei], mou ㄇㄡ [mou], men ㄇㄣ [mən], meng ㄇㄥ [məŋ], mie ㄇㄧㄝ [mjɛ], miao ㄇㄧㄠ [mjau], miu ㄇㄧㄡ [mjou], mian ㄇㄧㄢ [mjɛn], min ㄇㄧㄣ [min], ming ㄇㄧㄥ [miŋ] |
| `f` | `ㄈ` | [f] | labial | `fa` `ㄈㄚ` [fa] | `fo` `ㄈㄛ` [fwo] | — | — | `fu` `ㄈㄨ` [fu] | — | — | — | — | `fan` `ㄈㄢ` [fan] | `fang` `ㄈㄤ` [faŋ] | fei ㄈㄟ [fei], fou ㄈㄡ [fou], fen ㄈㄣ [fən], feng ㄈㄥ [fəŋ] (no fai, no fao, no fi-) |
| `d` | `ㄉ` | [t] | alveolar | `da` `ㄉㄚ` [ta] | — | `de` `ㄉㄜ` [tɤ] | `di` `ㄉㄧ` [ti] | `du` `ㄉㄨ` [tu] | — | — | `dai` `ㄉㄞ` [tai] | `dao` `ㄉㄠ` [tau] | `dan` `ㄉㄢ` [tan] | `dang` `ㄉㄤ` [taŋ] | dei ㄉㄟ [tei], dou ㄉㄡ [tou], den ㄉㄣ [tən], deng ㄉㄥ [təŋ], dong ㄉㄨㄥ [tʊŋ], die ㄉㄧㄝ [tjɛ], diao ㄉㄧㄠ [tjau], diu ㄉㄧㄡ [tjou], dian ㄉㄧㄢ [tjɛn], ding ㄉㄧㄥ [tiŋ], duo ㄉㄨㄛ [two], dui ㄉㄨㄟ [twei], duan ㄉㄨㄢ [twan], dun ㄉㄨㄣ [twən] |
| `t` | `ㄊ` | [tʰ] | alveolar | `ta` `ㄊㄚ` [tʰa] | — | `te` `ㄊㄜ` [tʰɤ] | `ti` `ㄊㄧ` [tʰi] | `tu` `ㄊㄨ` [tʰu] | — | — | `tai` `ㄊㄞ` [tʰai] | `tao` `ㄊㄠ` [tʰau] | `tan` `ㄊㄢ` [tʰan] | `tang` `ㄊㄤ` [tʰaŋ] | tou ㄊㄡ [tʰou], teng ㄊㄥ [tʰəŋ], tong ㄊㄨㄥ [tʰʊŋ], tie ㄊㄧㄝ [tʰjɛ], tiao ㄊㄧㄠ [tʰjau], tian ㄊㄧㄢ [tʰjɛn], ting ㄊㄧㄥ [tʰiŋ], tuo ㄊㄨㄛ [tʰwo], tui ㄊㄨㄟ [tʰwei], tuan ㄊㄨㄢ [tʰwan], tun ㄊㄨㄣ [tʰwən] |
| `n` | `ㄋ` | [n] | alveolar | `na` `ㄋㄚ` [na] | — | `ne` `ㄋㄜ` [nɤ] | `ni` `ㄋㄧ` [ni] | `nu` `ㄋㄨ` [nu] | `nü` `ㄋㄩ` [ny] | — | `nai` `ㄋㄞ` [nai] | `nao` `ㄋㄠ` [nau] | `nan` `ㄋㄢ` [nan] | `nang` `ㄋㄤ` [naŋ] | nei ㄋㄟ [nei], nou ㄋㄡ [nou], nen ㄋㄣ [nən], neng ㄋㄥ [nəŋ], nong ㄋㄨㄥ [nʊŋ], nie ㄋㄧㄝ [njɛ], niao ㄋㄧㄠ [njau], niu ㄋㄧㄡ [njou], nian ㄋㄧㄢ [njɛn], nin ㄋㄧㄣ [nin], niang ㄋㄧㄤ [njaŋ], ning ㄋㄧㄥ [niŋ], nuo ㄋㄨㄛ [nwo], nuan ㄋㄨㄢ [nwan], nüe ㄋㄩㄝ [nɥɛ] |
| `l` | `ㄌ` | [l] | alveolar | `la` `ㄌㄚ` [la] | — | `le` `ㄌㄜ` [lɤ] | `li` `ㄌㄧ` [li] | `lu` `ㄌㄨ` [lu] | `lü` `ㄌㄩ` [ly] | — | `lai` `ㄌㄞ` [lai] | `lao` `ㄌㄠ` [lau] | `lan` `ㄌㄢ` [lan] | `lang` `ㄌㄤ` [laŋ] | lei ㄌㄟ [lei], lou ㄌㄡ [lou], leng ㄌㄥ [ləŋ], long ㄌㄨㄥ [lʊŋ], lia ㄌㄧㄚ [lja], lie ㄌㄧㄝ [ljɛ], liao ㄌㄧㄠ [ljau], liu ㄌㄧㄡ [ljou], lian ㄌㄧㄢ [ljɛn], lin ㄌㄧㄣ [lin], liang ㄌㄧㄤ [ljaŋ], ling ㄌㄧㄥ [liŋ], luo ㄌㄨㄛ [lwo], luan ㄌㄨㄢ [lwan], lun ㄌㄨㄣ [lwən], lüe ㄌㄩㄝ [lɥɛ] |
| `g` | `ㄍ` | [k] | velar (back/open finals only) | `ga` `ㄍㄚ` [ka] | — | `ge` `ㄍㄜ` [kɤ] | — | `gu` `ㄍㄨ` [ku] | — | — | `gai` `ㄍㄞ` [kai] | `gao` `ㄍㄠ` [kau] | `gan` `ㄍㄢ` [kan] | `gang` `ㄍㄤ` [kaŋ] | gei ㄍㄟ [kei], gou ㄍㄡ [kou], gen ㄍㄣ [kən], geng ㄍㄥ [kəŋ], gong ㄍㄨㄥ [kʊŋ], gua ㄍㄨㄚ [kwa], guo ㄍㄨㄛ [kwo], guai ㄍㄨㄞ [kwai], gui ㄍㄨㄟ [kwei], guan ㄍㄨㄢ [kwan], gun ㄍㄨㄣ [kwən], guang ㄍㄨㄤ [kwaŋ] |
| `k` | `ㄎ` | [kʰ] | velar (back/open finals only) | `ka` `ㄎㄚ` [kʰa] | — | `ke` `ㄎㄜ` [kʰɤ] | — | `ku` `ㄎㄨ` [kʰu] | — | — | `kai` `ㄎㄞ` [kʰai] | `kao` `ㄎㄠ` [kʰau] | `kan` `ㄎㄢ` [kʰan] | `kang` `ㄎㄤ` [kʰaŋ] | kou ㄎㄡ [kʰou], ken ㄎㄣ [kʰən], keng ㄎㄥ [kʰəŋ], kong ㄎㄨㄥ [kʰʊŋ], kua ㄎㄨㄚ [kʰwa], kuo ㄎㄨㄛ [kʰwo], kuai ㄎㄨㄞ [kʰwai], kui ㄎㄨㄟ [kʰwei], kuan ㄎㄨㄢ [kʰwan], kun ㄎㄨㄣ [kʰwən], kuang ㄎㄨㄤ [kʰwaŋ] |
| `h` | `ㄏ` | [x] | velar (back/open finals only) | `ha` `ㄏㄚ` [xa] | — | `he` `ㄏㄜ` [xɤ] | — | `hu` `ㄏㄨ` [xu] | — | — | `hai` `ㄏㄞ` [xai] | `hao` `ㄏㄠ` [xau] | `han` `ㄏㄢ` [xan] | `hang` `ㄏㄤ` [xaŋ] | hei ㄏㄟ [xei], hou ㄏㄡ [xou], hen ㄏㄣ [xən], heng ㄏㄥ [xəŋ], hong ㄏㄨㄥ [xʊŋ], hua ㄏㄨㄚ [xwa], huo ㄏㄨㄛ [xwo], huai ㄏㄨㄞ [xwai], hui ㄏㄨㄟ [xwei], huan ㄏㄨㄢ [xwan], hun ㄏㄨㄣ [xwən], huang ㄏㄨㄤ [xwaŋ] |
| `j` | `ㄐ` | [tɕ] | alveolo-palatal (high-front i-/ü- finals ONLY) | — | — | — | `ji` `ㄐㄧ` [tɕi] | `ju` `ㄐㄩ` [tɕy] | `ju` (=jü) `ㄐㄩ` [tɕy] | — | — | — | — | — | jia ㄐㄧㄚ [tɕja], jie ㄐㄧㄝ [tɕjɛ], jiao ㄐㄧㄠ [tɕjau], jiu ㄐㄧㄡ [tɕjou], jian ㄐㄧㄢ [tɕjɛn], jin ㄐㄧㄣ [tɕin], jiang ㄐㄧㄤ [tɕjaŋ], jing ㄐㄧㄥ [tɕiŋ], jiong ㄐㄩㄥ [tɕjʊŋ], jue ㄐㄩㄝ [tɕɥɛ], juan ㄐㄩㄢ [tɕɥɛn], jun ㄐㄩㄣ [tɕyn] |
| `q` | `ㄑ` | [tɕʰ] | alveolo-palatal (high-front i-/ü- finals ONLY) | — | — | — | `qi` `ㄑㄧ` [tɕʰi] | `qu` `ㄑㄩ` [tɕʰy] | `qu` (=qü) `ㄑㄩ` [tɕʰy] | — | — | — | — | — | qia ㄑㄧㄚ [tɕʰja], qie ㄑㄧㄝ [tɕʰjɛ], qiao ㄑㄧㄠ [tɕʰjau], qiu ㄑㄧㄡ [tɕʰjou], qian ㄑㄧㄢ [tɕʰjɛn], qin ㄑㄧㄣ [tɕʰin], qiang ㄑㄧㄤ [tɕʰjaŋ], qing ㄑㄧㄥ [tɕʰiŋ], qiong ㄑㄩㄥ [tɕʰjʊŋ], que ㄑㄩㄝ [tɕʰɥɛ], quan ㄑㄩㄢ [tɕʰɥɛn], qun ㄑㄩㄣ [tɕʰyn] |
| `x` | `ㄒ` | [ɕ] | alveolo-palatal (high-front i-/ü- finals ONLY) | — | — | — | `xi` `ㄒㄧ` [ɕi] | `xu` `ㄒㄩ` [ɕy] | `xu` (=xü) `ㄒㄩ` [ɕy] | — | — | — | — | — | xia ㄒㄧㄚ [ɕja], xie ㄒㄧㄝ [ɕjɛ], xiao ㄒㄧㄠ [ɕjau], xiu ㄒㄧㄡ [ɕjou], xian ㄒㄧㄢ [ɕjɛn], xin ㄒㄧㄣ [ɕin], xiang ㄒㄧㄤ [ɕjaŋ], xing ㄒㄧㄥ [ɕiŋ], xiong ㄒㄩㄥ [ɕjʊŋ], xue ㄒㄩㄝ [ɕɥɛ], xuan ㄒㄩㄢ [ɕɥɛn], xun ㄒㄩㄣ [ɕyn] |
| `z` | `ㄗ` | [ts] | dental sibilant (back/open finals + apical -i) | `za` `ㄗㄚ` [tsa] | — | `ze` `ㄗㄜ` [tsɤ] | — | `zu` `ㄗㄨ` [tsu] | — | `zi` `ㄗ` [tsɹ̩] | `zai` `ㄗㄞ` [tsai] | `zao` `ㄗㄠ` [tsau] | `zan` `ㄗㄢ` [tsan] | `zang` `ㄗㄤ` [tsaŋ] | zei ㄗㄟ [tsei], zou ㄗㄡ [tsou], zen ㄗㄣ [tsən], zeng ㄗㄥ [tsəŋ], zong ㄗㄨㄥ [tsʊŋ], zuo ㄗㄨㄛ [tswo], zui ㄗㄨㄟ [tswei], zuan ㄗㄨㄢ [tswan], zun ㄗㄨㄣ [tswən] |
| `c` | `ㄘ` | [tsʰ] | dental sibilant (back/open finals + apical -i) | `ca` `ㄘㄚ` [tsʰa] | — | `ce` `ㄘㄜ` [tsʰɤ] | — | `cu` `ㄘㄨ` [tsʰu] | — | `ci` `ㄘ` [tsʰɹ̩] | `cai` `ㄘㄞ` [tsʰai] | `cao` `ㄘㄠ` [tsʰau] | `can` `ㄘㄢ` [tsʰan] | `cang` `ㄘㄤ` [tsʰaŋ] | cou ㄘㄡ [tsʰou], cen ㄘㄣ [tsʰən], ceng ㄘㄥ [tsʰəŋ], cong ㄘㄨㄥ [tsʰʊŋ], cuo ㄘㄨㄛ [tsʰwo], cui ㄘㄨㄟ [tsʰwei], cuan ㄘㄨㄢ [tsʰwan], cun ㄘㄨㄣ [tsʰwən] |
| `s` | `ㄙ` | [s] | dental sibilant (back/open finals + apical -i) | `sa` `ㄙㄚ` [sa] | — | `se` `ㄙㄜ` [sɤ] | — | `su` `ㄙㄨ` [su] | — | `si` `ㄙ` [sɹ̩] | `sai` `ㄙㄞ` [sai] | `sao` `ㄙㄠ` [sau] | `san` `ㄙㄢ` [san] | `sang` `ㄙㄤ` [saŋ] | sou ㄙㄡ [sou], sen ㄙㄣ [sən], seng ㄙㄥ [səŋ], song ㄙㄨㄥ [sʊŋ], suo ㄙㄨㄛ [swo], sui ㄙㄨㄟ [swei], suan ㄙㄨㄢ [swan], sun ㄙㄨㄣ [swən] |
| `zh` | `ㄓ` | [ʈʂ] | retroflex (back/open finals + apical -i) | `zha` `ㄓㄚ` [ʈʂa] | — | `zhe` `ㄓㄜ` [ʈʂɤ] | — | `zhu` `ㄓㄨ` [ʈʂu] | — | `zhi` `ㄓ` [ʈʂɻ̩] | `zhai` `ㄓㄞ` [ʈʂai] | `zhao` `ㄓㄠ` [ʈʂau] | `zhan` `ㄓㄢ` [ʈʂan] | `zhang` `ㄓㄤ` [ʈʂaŋ] | zhei ㄓㄟ [ʈʂei], zhou ㄓㄡ [ʈʂou], zhen ㄓㄣ [ʈʂən], zheng ㄓㄥ [ʈʂəŋ], zhong ㄓㄨㄥ [ʈʂʊŋ], zhua ㄓㄨㄚ [ʈʂwa], zhuo ㄓㄨㄛ [ʈʂwo], zhuai ㄓㄨㄞ [ʈʂwai], zhui ㄓㄨㄟ [ʈʂwei], zhuan ㄓㄨㄢ [ʈʂwan], zhun ㄓㄨㄣ [ʈʂwən], zhuang ㄓㄨㄤ [ʈʂwaŋ] |
| `ch` | `ㄔ` | [ʈʂʰ] | retroflex (back/open finals + apical -i) | `cha` `ㄔㄚ` [ʈʂʰa] | — | `che` `ㄔㄜ` [ʈʂʰɤ] | — | `chu` `ㄔㄨ` [ʈʂʰu] | — | `chi` `ㄔ` [ʈʂʰɻ̩] | `chai` `ㄔㄞ` [ʈʂʰai] | `chao` `ㄔㄠ` [ʈʂʰau] | `chan` `ㄔㄢ` [ʈʂʰan] | `chang` `ㄔㄤ` [ʈʂʰaŋ] | chou ㄔㄡ [ʈʂʰou], chen ㄔㄣ [ʈʂʰən], cheng ㄔㄥ [ʈʂʰəŋ], chong ㄔㄨㄥ [ʈʂʰʊŋ], chua ㄔㄨㄚ [ʈʂʰwa], chuo ㄔㄨㄛ [ʈʂʰwo], chuai ㄔㄨㄞ [ʈʂʰwai], chui ㄔㄨㄟ [ʈʂʰwei], chuan ㄔㄨㄢ [ʈʂʰwan], chun ㄔㄨㄣ [ʈʂʰwən], chuang ㄔㄨㄤ [ʈʂʰwaŋ] |
| `sh` | `ㄕ` | [ʂ] | retroflex (back/open finals + apical -i) | `sha` `ㄕㄚ` [ʂa] | — | `she` `ㄕㄜ` [ʂɤ] | — | `shu` `ㄕㄨ` [ʂu] | — | `shi` `ㄕ` [ʂɻ̩] | `shai` `ㄕㄞ` [ʂai] | `shao` `ㄕㄠ` [ʂau] | `shan` `ㄕㄢ` [ʂan] | `shang` `ㄕㄤ` [ʂaŋ] | shei ㄕㄟ [ʂei], shou ㄕㄡ [ʂou], shen ㄕㄣ [ʂən], sheng ㄕㄥ [ʂəŋ], shua ㄕㄨㄚ [ʂwa], shuo ㄕㄨㄛ [ʂwo], shuai ㄕㄨㄞ [ʂwai], shui ㄕㄨㄟ [ʂwei], shuan ㄕㄨㄢ [ʂwan], shun ㄕㄨㄣ [ʂwən], shuang ㄕㄨㄤ [ʂwaŋ] (no shong) |
| `r` | `ㄖ` | [ʐ~ɻ] | retroflex (back/open finals + apical -i; voiced member) | — | — | `re` `ㄖㄜ` [ʐɤ] | — | `ru` `ㄖㄨ` [ʐu] | — | `ri` `ㄖ` [ʐɻ̩] | — | `rao` `ㄖㄠ` [ʐau] | `ran` `ㄖㄢ` [ʐan] | `rang` `ㄖㄤ` [ʐaŋ] | rou ㄖㄡ [ʐou], ren ㄖㄣ [ʐən], reng ㄖㄥ [ʐəŋ], rong ㄖㄨㄥ [ʐʊŋ], rua ㄖㄨㄚ [ʐwa] (rare), ruo ㄖㄨㄛ [ʐwo], rui ㄖㄨㄟ [ʐwei], ruan ㄖㄨㄢ [ʐwan], run ㄖㄨㄣ [ʐwən] (gaps: no ra, rai, rei, ro) |
| `∅` (zero) | `（无声母 / y- w-）` | (none — bare vowel or glide onset) | zero initial | `a` `ㄚ` [a] | `o` `ㄛ` [o] | `e` `ㄜ` [ɤ] | `yi` (=i) `ㄧ` [i] | `wu` (=u) `ㄨ` [u] | `yu` (=ü) `ㄩ` [y] | — | `ai` `ㄞ` [ai] | `ao` `ㄠ` [au] | `an` `ㄢ` [an] | `ang` `ㄤ` [aŋ] | ei ㄟ [ei], ou ㄡ [ou], en ㄣ [ən], eng ㄥ [əŋ], er ㄦ [ɚ]; ya ㄧㄚ [ja], ye ㄧㄝ [jɛ], yao ㄧㄠ [jau], you ㄧㄡ [jou], yan ㄧㄢ [jɛn], yin ㄧㄣ [in], yang ㄧㄤ [jaŋ], ying ㄧㄥ [iŋ], yong ㄩㄥ [jʊŋ]; wa ㄨㄚ [wa], wo ㄨㄛ [wo], wai ㄨㄞ [wai], wei ㄨㄟ [wei], wan ㄨㄢ [wan], wen ㄨㄣ [wən], wang ㄨㄤ [waŋ], weng ㄨㄥ [wəŋ]; yue ㄩㄝ [ɥɛ], yuan ㄩㄢ [ɥɛn], yun ㄩㄣ [yn] |

### Per-Row Phonetic & Example Notes

Each initial with its name, an example word (showing **both Simplified & Traditional** where they differ), and the row's distributional note.

| Initial | Name | Example (Simp / Trad) | Phonetic note |
|---|---|---|---|
| `b` [p] | unaspirated voiceless bilabial plosive | 八 bā (八 / 八) "eight"; 包 bāo "wrap" | Voiceless **UNASPIRATED** [p] (not voiced [b]). Takes a o ai ei ao ou an en ang eng + i-finals i ie iao ian in ing; takes u but NOT ü; the simple nucleus o appears here (bo [pwo]). No apical `-i`, no j/q/x-style front-only restriction. |
| `p` [pʰ] | aspirated voiceless bilabial plosive | 怕 pà "fear"; 朋 péng (朋 / 朋) "friend" | Aspirated [pʰ]. Same final set as b: a o ai ei ao ou an en ang eng, i ie iao ian in ing, u; no ü, no apical `-i`. |
| `m` [m] | voiced bilabial nasal | 妈 mā (妈 / 媽) "mother"; 门 mén (门 / 門) "door" | Voiced nasal [m]. Wide final set incl. o (mo). No ü, no apical `-i`. (The interjection m/hm aside.) |
| `f` [f] | voiceless labiodental fricative | 飞 fēi (飞 / 飛) "fly"; 风 fēng (风 / 風) "wind" | Voiceless [f]. The most restricted labial: takes a o u and a/o/e-class nasals & diphthongs, but **NO i-finals** (no "fi"), no ü, no apical `-i`. Standalone o appears (fo 佛). |
| `d` [t] | unaspirated voiceless alveolar plosive | 大 dà "big"; 东 dōng (东 / 東) "east" | Voiceless **UNASPIRATED** [t] (not [d]). Broad final set: a e i u, ai ei ao ou, an en ang eng ong, ia(rare) ie iao iu ian, uo uan ui un, etc. No ü, no apical `-i`; o only inside uo (duo). |
| `t` [tʰ] | aspirated voiceless alveolar plosive | 他 tā "he"; 天 tiān "sky" | Aspirated [tʰ]. Same shape as d (minus a few accidental gaps). No ü, no apical `-i`. |
| `n` [n] | voiced alveolar nasal | 你 nǐ "you"; 女 nǚ (女 / 女) "woman" | Voiced nasal [n]. One of only two initials (with l) that take **BOTH u and ü** — so the umlaut is mandatory: nu 努 vs nü 女. Otherwise broad final set; no apical `-i`. |
| `l` [l] | voiced alveolar lateral approximant | 来 lái (来 / 來) "come"; 绿 lǜ (绿 / 綠) "green" | Voiced lateral [l]. The other initial taking **BOTH u and ü**: lu 路 vs lü 绿 — umlaut mandatory. Broadest final set of the alveolars; no apical `-i`. |
| `g` [k] | unaspirated voiceless velar plosive | 高 gāo "tall"; 国 guó (国 / 國) "country" | Voiceless **UNASPIRATED** [k]. Velar series: takes a e u, back/open diphthongs & nasals, and u-medial finals (gua guo guai gui guan gun guang) — but **NEVER the front i-/ü- finals** (no "gi", no "gü"); those belong to j/q/x. No apical `-i`. |
| `k` [kʰ] | aspirated voiceless velar plosive | 开 kāi (开 / 開) "open"; 看 kàn "look" | Aspirated [kʰ]. Same distribution as g: back/open + u-medial finals; **NO front i-/ü- finals**, no apical `-i`. |
| `h` [x] | voiceless velar/uvular fricative | 好 hǎo "good"; 红 hóng (红 / 紅) "red" | Voiceless dorsal fricative [x] (~[h] for some speakers). Velar series distribution: back/open + u-medial finals; **NO front i-/ü- finals** (no "hi", no "hü"), no apical `-i`. |
| `j` [tɕ] | unaspirated voiceless alveolo-palatal affricate | 鸡 jī (鸡 / 雞) "chicken"; 居 jū (居 / 居) "reside" | Voiceless **UNASPIRATED** [tɕ]. Occurs **ONLY** before i-finals and ü-finals — and the ü dots DROP after j, so written ⟨`ju`⟩ = jü = [tɕy], NOT [tɕu]. Never before a/o/e/u/back finals or apical `-i`. Complementary with g/z/zh. |
| `q` [tɕʰ] | aspirated voiceless alveolo-palatal affricate | 七 qī "seven"; 去 qù "go" | Aspirated [tɕʰ]. Same i-/ü-only distribution as j; ⟨`qu`⟩ = qü = [tɕʰy]. Never before back/open finals or apical `-i`. |
| `x` [ɕ] | voiceless alveolo-palatal fricative | 西 xī "west"; 学 xué (学 / 學) "study" | Voiceless [ɕ]. Same i-/ü-only distribution as j/q; ⟨`xu`⟩ = xü = [ɕy]. Never before back/open finals or apical `-i`. |
| `z` [ts] | unaspirated voiceless dental sibilant affricate | 字 zì "character"; 走 zǒu "walk" | Voiceless **UNASPIRATED** [ts]. Takes back/open + u-medial finals AND the apical `-i`: zi = [tsɹ̩] (NOT [tsi]). **NEVER** before front i-/ü- finals (no [tsi] with true [i], no "zü"), no standalone high [i]/[y]. Complementary with j (and zh). |
| `c` [tsʰ] | aspirated voiceless dental sibilant affricate | 菜 cài "vegetable"; 词 cí (词 / 詞) "word" | Aspirated [tsʰ]. Same distribution as z: back/open + u-medial finals + apical `-i` (ci = [tsʰɹ̩]). Never before front i-/ü- finals. |
| `s` [s] | voiceless dental sibilant fricative | 四 sì "four"; 思 sī "think" | Voiceless [s]. Same distribution as z/c: back/open + u-medial finals + apical `-i` (si = [sɹ̩]). Never before front i-/ü- finals. |
| `zh` [ʈʂ] | unaspirated voiceless retroflex affricate | 中 zhōng (中 / 中) "middle"; 知 zhī (知 / 知) "know" | Voiceless **UNASPIRATED** retroflex [ʈʂ]. Takes back/open + u-medial finals AND the retroflex apical `-i`: zhi = [ʈʂɻ̩] (NOT [ʈʂi]). **NEVER** before front i-/ü- finals. In de-retroflexing Guoyu/southern speech zh→z (see Accent Notes). |
| `ch` [ʈʂʰ] | aspirated voiceless retroflex affricate | 吃 chī "eat"; 车 chē (车 / 車) "vehicle" | Aspirated retroflex [ʈʂʰ]. Same distribution as zh: back/open + u-medial finals + retroflex apical `-i` (chi = [ʈʂʰɻ̩]). Never before front i-/ü- finals; ch→c when de-retroflexed. |
| `sh` [ʂ] | voiceless retroflex fricative | 是 shì "to be"; 书 shū (书 / 書) "book" | Voiceless retroflex [ʂ]. Same distribution as zh/ch: back/open + u-medial finals + retroflex apical `-i` (shi = [ʂɻ̩]). Never before front i-/ü- finals; sh→s when de-retroflexed (是 shì → sì). |
| `r` [ʐ~ɻ] | voiced retroflex fricative/approximant | 人 rén (人 / 人) "person"; 日 rì "day/sun" | Voiced retroflex [ʐ] (or approximant [ɻ]) — the **only voiced obstruent-class initial**. Patterns with zh/ch/sh (back/open + u-medial finals + retroflex apical `-i`: ri = [ʐɻ̩]) but has gaps the voiceless zh/ch/sh fill: no "ra", no "rai", no "rei", no "ro" (though "rao", "ran", "rang" etc. are fine). Never before front i-/ü- finals. Weakens to [z]/glide/zero in de-retroflexing accents. |
| `∅` (zero initial) | zero initial — y-/w-/yu- orthographic respelling | 一 yī "one" (=i); 五 wǔ "five" (=u); 雨 yǔ (雨 / 雨) "rain" (=ü); 爱 ài "love"; 二 èr "two" | No onset consonant. High-vocoid finals are **RESPELLED** with y/w/yu as glide markers: i-→yi/y-, u-→wu/w-, ü-→yu-. The y/w add **NO consonant** — phonetically these are glide-initial [j]/[w]/[ɥ] or bare-vowel syllables. Pure a/o/e/ai/ei/ao/ou/an/en/ang/eng/er/ê take the bare zero initial with no letter. This row carries the apical-vowel-less true [i]/[u]/[y] standalone syllables and the er/erhua base. |

### Special Syllables

#### Apical-Only Syllables

The ONLY seven (× tones) syllables built on the apical vowels; onset-only syllables whose nucleus is the apical vowel.

| Pinyin | IPA | Zhuyin | Example |
|---|---|---|---|
| `zhi` | [ʈʂɻ̩] | `ㄓ` | 知 zhī "know" |
| `chi` | [ʈʂʰɻ̩] | `ㄔ` | 吃 chī "eat" |
| `shi` | [ʂɻ̩] | `ㄕ` | 是 shì "to be" |
| `ri` | [ʐɻ̩~ɻɻ̩] | `ㄖ` | 日 rì "day/sun" |
| `zi` | [tsɹ̩] | `ㄗ` | 字 zì "character" |
| `ci` | [tsʰɹ̩] | `ㄘ` | 词 cí (词 / 詞) "word" |
| `si` | [sɹ̩] | `ㄙ` | 四 sì "four" |

> **Note:** Zhuyin writes these as the **bare initial letter, no vowel symbol** (`ㄓ` ㄔ ㄕ ㄖ ㄗ ㄘ ㄙ). The ⟨`i`⟩ is a spelling placeholder; do **not** read it as [i].

#### Syllabic-Consonant Interjections

| Members | IPA | Note |
|---|---|---|
| `hm`, `hng`, `m`, `n`, `ng` (颟/嗯/哼 interjections) | [m̩], [ŋ̩], etc. | Marginal exclamative syllables with a syllabic nasal and no standard final; outside the regular initial×final system and **not** given matrix rows. |

#### er & Erhua

| Members | Note |
|---|---|
| `er` 儿/二 /ɚ/ `ㄦ`; plus the productive 儿化 `-r` suffix | The `er` syllable takes only the **zero initial**. Erhua **RESTRUCTURES** the rime of the host syllable (drops -i/-n codas, rhotacizes the vowel: 花儿 huār, 玩儿 wánr→[wɑɚ]) and is a Putonghua hallmark; documented in the suprasegmentals/erhua section, not as a chart row. |

### Accent Notes (Putonghua vs Guoyu)

- **Retroflex realization.** The chart gives **PUTONGHUA** (Beijing) citation values, which maintain a robust contrast between the RETROFLEX series zh/ch/sh/r [ʈʂ ʈʂʰ ʂ ʐ] and the DENTAL series z/c/s [ts tsʰ s], with the two apical vowels [ɻ̩] (retroflex) vs [ɹ̩] (dental) kept distinct. In much **TAIWAN GUOYU** (國語) and across southern Mainland Mandarin, **DE-RETROFLEXION** applies: zh→z, ch→c, sh→s, and r→[z]/glide/zero, so 是 shì can merge with sì, 知 zhī with zī, and the retroflex apical [ɻ̩] flattens toward the dental [ɹ̩]. This is a **SURFACE realization difference only** — it does NOT change the toneless pinyin spelling of the syllable, so the chart's cells are valid for both standards; only the phonetic value of the retroflex rows shifts.
- **Erhua.** **ERHUA** (儿化, the rhotic `-r` suffix, /ɚ/) is pervasive in Beijing Putonghua (花儿 huār, 一点儿 yìdiǎnr, 玩儿 wánr) and restructures the host rime (dropping -i/-n codas, rhotacizing the vowel). Taiwan Guoyu uses little or no erhua (花 huā). Erhua is not tabulated as chart cells; it operates on top of the finals and is documented in the suprasegmentals/erhua section.
- **Aspiration, not voicing.** Across all standards the stop/affricate contrast is **ASPIRATION** (b/p, d/t, g/k, z/c, zh/ch, j/q are unaspirated/aspirated voiceless pairs), never voicing — an invariant of the chart in both Putonghua and Guoyu.
- **Lexical tone differences.** Guoyu and Putonghua differ in a handful of **LEXICAL** tones/readings (垃圾 lèsè vs lājī, 和 hàn vs hé as conjunction, 企 qì vs qǐ, 期 qí vs qī, 法 fǎ vs fà) and in fewer neutral-toned syllables in Guoyu. These are lexical-tonal facts of the LANGUAGE; they do not affect this toneless syllable chart but are noted in the tone/lexicon sections.

### Unicode Reference

Codepoints for the scripts used in this chart. Hanzi shown in both Simplified and Traditional.

| Item | Codepoints / Range | Detail |
|---|---|---|
| Pinyin base letters | Basic Latin `U+0041`–`U+007A` | The special letter ü = `U+00FC` (LATIN SMALL LETTER U WITH DIAERESIS), Ü = `U+00DC`. |
| Pinyin tone marks | (used in the LANGUAGE, not in this toneless chart) | macron ā `U+0101` / `U+0100`, acute á `U+00E1`, caron/háček ǎ `U+01CE` / ǐ `U+01D0` / ǒ `U+01D2` / ǔ `U+01D4`, grave à `U+00E0`; ǘ `U+01D8`, ǚ `U+01DA`, ǜ `U+01DC`, ǖ `U+01D6` on ü; also formed with combining marks `U+0304` (macron), `U+0301` (acute), `U+030C` (caron), `U+0300` (grave). |
| Zhuyin/Bopomofo block | `U+3105`–`U+312F` | e.g. ㄅ `U+3105`, ㄆ `U+3106`, ㄇ `U+3107`, ㄈ `U+3108` … ㄓ `U+3113`, ㄗ `U+3117`, ㄐ `U+3110`, ㄚ `U+311A`, ㄧ `U+3127`, ㄨ `U+3128`, ㄩ `U+3129`, ㄦ `U+3126`; Bopomofo Extended `U+31A0`–`U+31BF` (for dialect sounds). |
| Zhuyin tone marks | (not shown here) | ˊ `U+02CA` (T2), ˇ `U+02C7` (T3), ˋ `U+02CB` (T4), ˙ `U+02D9` (neutral, written before the syllable); T1 unmarked. |
| Hanzi (CJK) | `U+4E00`–`U+9FFF`; Ext A `U+3400`–`U+4DBF`; Ext B `U+20000`–`U+2A6DF` (+ further extensions) | Both Simplified and Traditional forms live in this block, e.g. 国 `U+56FD` vs 國 `U+570B`; 妈 `U+5988` vs 媽 `U+5ABD`. |
| Radicals | Kangxi Radicals `U+2F00`–`U+2FDF`; CJK Radicals Supplement `U+2E80`–`U+2EFF` | |

> **Note:** Zhuyin syllables are **SEQUENCES of code points** (initial + medial + final letters, e.g. `zhuang` = ㄓ `U+3113` + ㄨ `U+3128` + ㄤ `U+3124`), not single precomposed glyphs. Tone-marked pinyin vowels exist both precomposed and as base+combining-mark sequences.

### Cross-Reference

- **Companion files:** `Chinese/chinese_pronunciation_guide.md`, `Chinese/Peshita_Chinese/Pinyin/`, `Chinese/Peshita_Chinese/Hanzi-Simplified/`, `Chinese/Peshita_Chinese/Hanzi-Traditional/`
- **Related sections:** phonological inventory · consonants (initials) · vowels (finals) · syllable structure · phonological rules · suprasegmentals (tones) · orthography (grapheme–phoneme) · unicode reference
- **Reader-tiers note:** The Chinese Peshitta ships **SIX reader tiers**: Scholarly + Pretty (language-neutral Latin, reused byte-identical from English), **TONELESS PINYIN** (the deterministic phonetic spine drawn from exactly the legal cells of THIS chart), **ZHUYIN/BOPOMOFO** (a fixed pinyin↔zhuyin transcode of the same syllable stream), and **HANZI** in **SIMPLIFIED** and **TRADITIONAL** (a downstream, frozen one-character-per-syllable transcription lookup off the pinyin stream). Because Hanzi is logographic and cannot phonetically spell foreign input, the native phonetic engine is **PINYIN, not Hanzi**. Rendering Aramaic into Mandarin requires phonotactic repair with **FORCED EPENTHESIS** — clusters and illegal codas (everything but /n ŋ ɚ/) are broken up by inserting syllables drawn from exactly the legal cells tabulated here. The tiers are **TONELESS** because the Peshitta source IPA carries no tone; the Hanzi tier unavoidably imposes a citation tone per character (an artifact, documented loudly, **NOT** a source feature).

---

*Section compiled by Shin.*

## Tones & Suprasegmentals

Prosodic and suprasegmental features of Standard Mandarin (标准汉语 / 標準漢語), documented in parallel for two reference standards: 普通话 *Pǔtōnghuà* (PRC Standard Mandarin, Beijing-based phonology, **simplified** characters, Hanyu Pinyin) and 國語 *Guóyǔ* (Taiwan Standard Mandarin, **traditional** characters, Zhuyin/Bopomofo). The single most important fact about Mandarin suprasegmentals is its TYPE: Mandarin is a **TONE language** with **four contrastive lexical tones plus a neutral tone**, in which EVERY full syllable carries a lexically specified tone (声调 / 聲調 *shēngdiào*) — a pitch CONTOUR that is part of the word and is contrastive (妈 / 媽 *mā* 'mother' / 麻 *má* 'hemp' / 马 / 馬 *mǎ* 'horse' / 骂 / 罵 *mà* 'scold', segmentally identical, distinguished SOLELY by tone). This is sharply contrastive with the other guides in this set. Unlike ENGLISH, Mandarin has NO lexical STRESS of the contrastive English type (no `/ˈrecord/`–`/reˈcord/` minimal pairs), no stress-timed compression, and no vowel reduction to schwa in the English sense; prominence is organized around tone, neutral-tone destressing, and intonation. Unlike JAPANESE pitch accent (at most ONE pitch DROP per word, docked to a mora, with the rest filled in by rule) and unlike KOREAN (which has no word-level tone at all, only phrase-level pitch), Mandarin assigns an INDEPENDENT TONE to EACH syllable — the whole pitch shape of every syllable is lexically stored, not predicted from a single accent kernel. Mandarin is best described as **syllable-timed-tending** with the syllable as the tone-bearing unit. Additional suprasegmental processes are TONE SANDHI (rule-governed tone change in connected speech — third-tone sandhi, 一 *yī* and 不 *bù* sandhi), the NEUTRAL TONE (轻声 / 輕聲 *qīngshēng*), ERHUA (儿化 / 兒化, rhotacization of a final by `-r`), and sentence-level INTONATION overlaid on the lexical tones (question intonation, sentence-final particles).

> **Important:** Tone is fully documented here because it describes the **language**; the Chinese Peshitta READER TIERS are emitted **TONELESS** (the Peshitta source IPA carries no tone), so the tonal detail in this section is a property of Mandarin itself, not of the toneless reader tiers — see [The Reader Tiers Are Toneless](#the-reader-tiers-are-toneless) below.

### Typological Summary

Mandarin's suprasegmental type is stated up front and contrasted explicitly with the parallel guides, because the single biggest learner error is importing English STRESS (or assuming Japanese/Korean-style under-specification) into Mandarin, where TONE is the contrastive word-level pitch property on EVERY syllable.

| Statement | Description |
|---|---|
| **Mandarin IS** | A TONE language: FOUR lexical tones (T1 阴平 / 陰平 high-level `55`, T2 阳平 / 陽平 rising `35`, T3 上声 / 上聲 low-dipping `214`, T4 去声 / 去聲 high-falling `51`) + a NEUTRAL tone (轻声 / 輕聲), with an independent CONTRASTIVE tone on EACH full syllable. The syllable is the tone-bearing unit; rhythm is syllable-timed-tending. |
| **Mandarin is NOT** | NOT a stress-accent language (no contrastive lexical STRESS of the English `/ˈrecord/`–`/reˈcord/` type, no stress-timed compression, no schwa reduction). NOT a pitch-accent language like Japanese (Japanese specifies at most ONE drop per word and predicts the rest; Mandarin stores a full tone on EVERY syllable). NOT prosodically flat at the word level like Standard Korean (which has no word-level tone or stress). |

#### Contrast With the Companion Guides

| Compared with | How Mandarin differs |
|---|---|
| **English** | ENGLISH = stress-accent, stress-timed, with phonemic lexical STRESS (`/ˈrecord/` noun vs `/reˈcord/` verb) and heavy vowel reduction to schwa. Mandarin has NONE of this kind of contrast: its word-level contrast is TONE (妈/麻/马/骂 · 媽/麻/馬/罵), realized as a pitch CONTOUR on the syllable, not loudness/duration on a stressed syllable; full vowels are retained (the chief reduction is the NEUTRAL TONE, a tonal/durational phenomenon, not English schwa reduction). |
| **Japanese** | JAPANESE has LEXICAL PITCH ACCENT — at most ONE pitch DROP (downstep) per word, docked to a mora, with the surrounding pitch predictable by rule; a word has at most one 'tonal event'. MANDARIN assigns a FULL, independent tone to EVERY syllable — one tone per syllable, not one accent per word — and these tones are CONTOURS (rising, falling, dipping), not just H/L levels. Mandarin's tone sandhi (T3 + T3 → T2 + T3) is a tonal-phonology rule with no Japanese pitch-accent equivalent. |
| **Korean** | KOREAN (Seoul 표준어) has NEITHER lexical stress NOR lexical tone — pitch lives entirely at the phrase level. MANDARIN differs maximally: it HAS a contrastive word-level pitch property on EVERY syllable (the lexical tone), giving dense minimal sets (妈麻马骂 · 媽麻馬罵) that have no Korean word-level equivalent. |
| **Other tone languages** | Like Cantonese (6+ tones) and other Sinitic languages, Mandarin is a CONTOUR-tone language (tones are pitch glides, not only level registers) where tone is part of every syllable's lexical identity. Mandarin's four-tone system is comparatively small among Sinitic varieties. |

### Tones

Mandarin's SIGNATURE feature: **four lexical (full) tones plus a neutral tone**. Each full syllable carries one of the four tones; tone is LEXICAL and CONTRASTIVE — it distinguishes otherwise identical syllables. Tones are described by (a) the traditional NAME (声调 / 聲調 name), (b) the CHAO TONE-LETTER pitch contour (a 5-level scale, `1` = lowest, `5` = highest), (c) the conventional CONTOUR NUMBERS (e.g. `55`, `35`, `214`, `51`), and (d) the notation in each writing system: Pinyin DIACRITICS, Zhuyin/Bopomofo TONE MARKS, and TONE NUMBERS (`1`–`4`, `0`/`5` for neutral).

#### Notation Systems

Three parallel ways Mandarin tone is written, all equivalent. The toneless spelling (the bare pinyin or zhuyin letters) is the same across Pǔtōnghuà and Guóyǔ; only the tone overlay differs, and the Peshitta reader tiers omit it entirely.

| System | Description |
|---|---|
| **Chao tone letters** | A 5-point pitch scale (Chao Yuen Ren, 1930): `1` = lowest, `5` = highest. A tone is written as a sequence of levels with IPA tone letters (`˥` = 5, `˦` = 4, `˧` = 3, `˨` = 2, `˩` = 1) or as the digit sequence (the 'contour number'). E.g. high-level = `˥` (`55`); rising = `˧˥` (`35`); low-dipping = `˨˩˦` (`214`); high-falling = `˥˩` (`51`). |
| **Pinyin diacritics** | Hanyu Pinyin marks tone with a DIACRITIC over the main vowel: T1 macron `ā` (`U+0101`), T2 acute `á` (`U+00E1`), T3 caron/háček `ǎ` (`U+01CE`), T4 grave `à` (`U+00E0`); the NEUTRAL tone is unmarked (`a`, sometimes a preceding middot `·a`). Tone-placement rule: the mark goes on `a` > `o`/`e` > `i`/`u`, with the later of `i`/`u` in a cluster (e.g. `iu` → `iù`, `ui` → `uǐ`); over `i` the dot is replaced (`ǐ`, not `i̇̌`). |
| **Zhuyin tone marks** | Zhuyin/Bopomofo (注音符號) writes the tone mark AFTER the syllable's symbols: T1 is UNMARKED (no mark); T2 = `ˊ` (`U+02CA`); T3 = `ˇ` (`U+02C7`); T4 = `ˋ` (`U+02CB`); NEUTRAL = `˙` (`U+02D9`), written BEFORE the syllable in Taiwan convention. NOTE the asymmetry with pinyin: pinyin leaves the NEUTRAL tone unmarked and marks T1; zhuyin leaves T1 unmarked and marks the neutral tone. |
| **Tone numbers** | An ASCII-friendly system widely used in dictionaries and computing: append `1`/`2`/`3`/`4` for the four tones and `0` (or `5`) for the neutral tone, e.g. `ma1 ma2 ma3 ma4 ma0`. This is the notation that keys the Peshitta's tone-bearing Hanzi lookup internally even though the SHIPPED reader tiers are toneless. |

#### The Four Lexical Tones

| Tone | Name (pinyin) | 简体 / 繁體 | Gloss | Contour | Chao | Number | Pinyin mark | Zhuyin mark | Tone № | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| **T1** | *yīnpíng* | 阴平 / 陰平 | 'dark/high level' (first tone) | HIGH-LEVEL: a steady high pitch held flat at the top of the range. | `˥` | `55` | `ā` (macron) | (unmarked) | `1` | 妈 / 媽 `mā` `ㄇㄚ` [ma˥] 'mother' |
| **T2** | *yángpíng* | 阳平 / 陽平 | 'light/rising level' (second tone) | RISING: pitch glides from mid up to high (like the English questioning 'huh?'). | `˧˥` | `35` | `á` (acute) | `ˊ` | `2` | 麻 / 麻 `má` `ㄇㄚˊ` [ma˧˥] 'hemp / numb' |
| **T3** | *shǎngshēng* (also *shàngshēng*) | 上声 / 上聲 | 'rising/third tone' (the low-dipping tone) | LOW-DIPPING (low fall-rise): pitch starts mid-low, dips to the bottom, then rises — in FULL (isolation / phrase-final) form. In most connected-speech contexts it surfaces as a 'HALF-THIRD' (低降 low-falling, `˨˩`, ~`21`) without the final rise — see [Full vs Half-Third](#full-vs-half-third). | `˨˩˦` (full); `˨˩` (half-third) | `214` (full); `21` (half-third) | `ǎ` (caron / háček) | `ˇ` | `3` | 马 / 馬 `mǎ` `ㄇㄚˇ` [ma˨˩˦] (full, in isolation) 'horse' |
| **T4** | *qùshēng* | 去声 / 去聲 | 'departing/fourth tone' (the falling tone) | HIGH-FALLING: pitch glides sharply from high down to low (an emphatic, falling 'NO!' contour). | `˥˩` | `51` | `à` (grave) | `ˋ` | `4` | 骂 / 罵 `mà` `ㄇㄚˋ` [ma˥˩] 'scold / curse' |

#### The Neutral Tone — 轻声 / 輕聲 (*qīngshēng*)

The neutral tone (轻声 / 輕聲 *qīngshēng*, 'light tone', the neutral / toneless syllable) is **short, weak, and destressed**: it has NO independent contour of its own; it is reduced in duration and intensity, and its PITCH is determined by the PRECEDING full tone. It is the closest Mandarin analog to English unstressing, but it is a tonal/durational reduction, **not** vowel-quality reduction to schwa (though the vowel may centralize slightly).

| Property | Value |
|---|---|
| Tone number | `0` (or `5`) |
| Pinyin mark | unmarked (no diacritic); a leading middot `·ma` is sometimes used pedagogically |
| Zhuyin mark | `˙` (placed BEFORE the syllable in Taiwan convention, e.g. `˙ㄇㄚ`) |

**Pitch realized by the preceding tone:**

| After tone | Neutral pitch | Example |
|---|---|---|
| T1 (`55`) | mid-low, ~`2` | 妈妈 / 媽媽 *māma* 'mom' → [ma˥ ma˨] |
| T2 (`35`) | mid, ~`3` | 爷爷 / 爺爺 *yéye* 'grandpa' → [je˧˥ je˧] |
| T3 (`214`) | mid-high, ~`4` (after a half-third low) | 椅子 / 椅子 *yǐzi* 'chair' → [i˨˩ tsɹ̩˦] |
| T4 (`51`) | low, ~`1` | 爸爸 / 爸爸 *bàba* 'dad' → [pa˥˩ pa˩] |

**Examples:**

| 简体 | 繁體 | Pinyin | IPA | Gloss |
|---|---|---|---|---|
| 吗 | 嗎 | `ma` | [ma] (neutral) | yes/no question particle |
| 的 | 的 | `de` | [tɤ] (neutral) | attributive/possessive particle |
| 桌子 | 桌子 | `zhuōzi` | [ʈʂwo˥ tsɹ̩] | 'table' — the suffix 子 *zi* is neutral |

> **Note:** Whether a syllable is neutral is partly LEXICAL (particles 的 了 吗/嗎 呢, suffixes 子 头/頭, reduplicated kin terms) and partly variable by register and standard — see [Pǔtōnghuà vs Guóyǔ](#pǔtōnghuà-vs-guóyǔ-suprasegmental-differences) (Taiwan Guóyǔ uses the neutral tone LESS and often restores a full citation tone).

#### Minimal Sets — Tone as the Sole Contrast

The canonical demonstration of lexical tone: segmentally identical syllables distinguished SOLELY by tone — the Mandarin analog of English stress minimal pairs (`record`/`record`), but the cue is TONE, not stress, and a SINGLE syllable carries a four- or five-way contrast (impossible in English, Japanese, or Korean at the word level).

**`ma` — the textbook five-way set:**

| 简体 | 繁體 | Pinyin | Tone | IPA | Gloss |
|---|---|---|---|---|---|
| 妈 | 媽 | `mā` | T1 (`55`) | [ma˥] | 'mother' |
| 麻 | 麻 | `má` | T2 (`35`) | [ma˧˥] | 'hemp / numb' |
| 马 | 馬 | `mǎ` | T3 (`214`) | [ma˨˩˦] | 'horse' |
| 骂 | 罵 | `mà` | T4 (`51`) | [ma˥˩] | 'scold' |
| 吗 | 嗎 | `ma` | neutral | [ma] | question particle |

> **Note:** The famous 妈麻马骂(吗) / 媽麻馬罵(嗎) set. Often cited as a sentence mnemonic: 妈妈骑马，马慢，妈妈骂马 / 媽媽騎馬，馬慢，媽媽罵馬 *Māma qí mǎ, mǎ màn, māma mà mǎ* '(My) mom rides a horse; the horse is slow; (my) mom scolds the horse.'

**`yi` — four-way:**

| 简体 | 繁體 | Pinyin | Tone | IPA | Gloss |
|---|---|---|---|---|---|
| 一 | 一 | `yī` | T1 (`55`) | [i˥] | 'one' |
| 姨 | 姨 | `yí` | T2 (`35`) | [i˧˥] | 'aunt (mother's sister)' |
| 椅 | 椅 | `yǐ` | T3 (`214`) | [i˨˩˦] | 'chair' |
| 亿 | 億 | `yì` | T4 (`51`) | [i˥˩] | 'hundred million' |

**`shi` — four-way:**

| 简体 | 繁體 | Pinyin | Tone | IPA | Gloss |
|---|---|---|---|---|---|
| 诗 | 詩 | `shī` | T1 (`55`) | [ʂɻ̩˥] | 'poem' |
| 十 | 十 | `shí` | T2 (`35`) | [ʂɻ̩˧˥] | 'ten' |
| 史 | 史 | `shǐ` | T3 (`214`) | [ʂɻ̩˨˩˦] | 'history' |
| 是 | 是 | `shì` | T4 (`51`) | [ʂɻ̩˥˩] | 'to be / yes' |

> **Note:** Apical vowel `-i` = [ɻ̩] after `sh`. This four-way set underlies the famous tone-illustrating tongue-twisters.

**`tang` — illustrating tone over a fuller rime:**

| 简体 | 繁體 | Pinyin | Tone | IPA | Gloss |
|---|---|---|---|---|---|
| 汤 | 湯 | `tāng` | T1 (`55`) | [tʰaŋ˥] | 'soup' |
| 糖 | 糖 | `táng` | T2 (`35`) | [tʰaŋ˧˥] | 'sugar / candy' |
| 躺 | 躺 | `tǎng` | T3 (`214`) | [tʰaŋ˨˩˦] | 'to lie down' |
| 烫 | 燙 | `tàng` | T4 (`51`) | [tʰaŋ˥˩] | 'scalding hot' |

#### The Tone-Bearing Unit

The TONE-BEARING UNIT in Mandarin is the **SYLLABLE** (more precisely its voiced rime — the nucleus and any voiced coda). Every full syllable carries exactly one of the four tones; the neutral tone is the absence of an independent tonal target. Because Mandarin is near one-syllable-per-morpheme/character, tone is effectively a property of each morpheme/character. Contrast: Japanese docks pitch to the MORA (and only one drop per word); Mandarin specifies a full contour per syllable.

**IPA notation:** Tone is written with IPA tone letters after the syllable rime (e.g. [ma˥], [ma˧˥], [ma˨˩˦], [ma˥˩]) or with superscript Chao digits (`ma⁵⁵`, `ma³⁵`, `ma²¹⁴`, `ma⁵¹`). Diacritic letter-tones (`mā má mǎ mà`) are pinyin, not IPA.

### Tone Sandhi

TONE SANDHI (变调 / 變調 *biàndiào*) is the rule-governed CHANGE of a syllable's tone in connected speech, conditioned by neighboring tones. It is Mandarin's most important connected-speech process and the chief reason that the CITATION tones above are not always what is actually said. The major patterns are: (1) THIRD-TONE sandhi (T3 + T3 → T2 + T3, plus the half-third reduction), (2) the special sandhi of 一 *yī* 'one', and (3) the special sandhi of 不 *bù* 'not'. (The broader connected-speech inventory — including the neutral-tone and erhua interactions and the role of sentence particles — is also collected in the Connected Speech and Tone Sandhi section.) Crucially, sandhi **NEVER changes the underlying TONELESS spelling** — pinyin/zhuyin letters are constant — and the Peshitta reader tiers, being toneless, are unaffected.

#### Third-Tone Sandhi

The most famous Mandarin sandhi: a third tone (T3, `214`) immediately before ANOTHER third tone becomes a SECOND tone (T2, `35`). The change is OBLIGATORY in natural speech. Pinyin is conventionally written with the UNDERLYING T3 marks (`nǐ hǎo`), but it is PRONOUNCED `ní hǎo`.

**Rule:** `T3 + T3 → T2 + T3` (the first T3 surfaces as T2/rising; the second keeps its T3, usually as a full or half-third).

| 简体 | 繁體 | Underlying | Surface | IPA (surface) | Gloss |
|---|---|---|---|---|---|
| 你好 | 你好 | `nǐ hǎo` | `ní hǎo` | [ni˧˥ xau˨˩˦] | 'hello' (lit. 'you good') — first 你 *nǐ* (T3) → T2 before 好 *hǎo* (T3) |
| 很好 | 很好 | `hěn hǎo` | `hén hǎo` | [xən˧˥ xau˨˩˦] | 'very good' — 很 *hěn* (T3) → T2 before 好 *hǎo* (T3) |
| 雨伞 | 雨傘 | `yǔ sǎn` | `yú sǎn` | [y˧˥ san˨˩˦] | 'umbrella' — 雨 *yǔ* (T3) → T2 before 伞 *sǎn* (T3) |

**Strings of three or more T3 syllables:** sandhi applies according to prosodic grouping (which syllables form a unit). The textbook case 我也很好 / 我也很好 *wǒ yě hěn hǎo* 'I'm also fine' is most often grouped `[wǒ] [yě hěn hǎo]` or applied left-to-right, surfacing as `wǒ yé hén hǎo` (or `wó yé hén hǎo`), with only the LAST T3 keeping a full third tone.

| 简体 | 繁體 | Underlying | Surface | Gloss |
|---|---|---|---|---|
| 我也很好 | 我也很好 | `wǒ yě hěn hǎo` | `wǒ yé hén hǎo` (≈ `wó yé hén hǎo`) | 'I'm fine too' — all but the final T3 raise to T2; the exact pattern depends on phrasing/tempo. |

#### Full vs Half-Third

Even when NOT followed by another T3, an underlying T3 is usually NOT pronounced with its full dipping `214` contour in connected speech. A non-final T3 (before T1, T2, T4, or a neutral syllable) is realized as a **'HALF-THIRD'** (半上 *bàn shǎng*): the LOW-FALLING part only, ~`21` (`˨˩`), WITHOUT the final rise. The FULL `214` contour appears mainly in ISOLATION and at the END of a prosodic phrase.

- **Half-third contexts:** T3 before T1/T2/T4/neutral → half-third [˨˩] (low, no rise).
- **Full-third contexts:** T3 in isolation, or phrase-finally / before a pause → full [˨˩˦] (dips then rises).

| 简体 | 繁體 | Pinyin | IPA (surface) | Gloss |
|---|---|---|---|---|
| 好的 | 好的 | `hǎo de` | [xau˨˩ tɤ] | 'OK' — 好 *hǎo* is a HALF-THIRD (low, no rise) before the neutral 的 *de* |
| 美国 | 美國 | `Měiguó` | [mei˨˩ kwo˧˥] | 'America' — 美 *Měi* is a HALF-THIRD (`˨˩`) before T2 国 *guó* |
| 马 | 馬 | `mǎ` | [ma˨˩˦] | 'horse' in ISOLATION — the FULL `214` dip-rise appears |

#### 一 *yī* Sandhi

一 *yī* 'one' (citation T1, `55`) changes tone according to the FOLLOWING syllable's tone. (When used as a pure counting numeral, in dates/ordinals, or in isolation, it keeps T1.)

**Rules:**

- 一 *yī* + T1/T2/T3 → *yì* (T4, `51`): the high-level becomes high-falling before a non-T4 syllable.
- 一 *yī* + T4 → *yí* (T2, `35`): becomes rising before a falling tone.
- 一 *yī* between syllables (e.g. in 看一看 *kàn yi kàn* 'take a look') → neutral / weak.

| 简体 | 繁體 | Underlying | Surface | IPA (surface) | Gloss |
|---|---|---|---|---|---|
| 一天 | 一天 | `yī tiān` | `yì tiān` | [i˥˩ tʰjɛn˥] | 'one day' — 一 → *yì* (T4) before T1 天 *tiān* |
| 一年 | 一年 | `yī nián` | `yì nián` | [i˥˩ njɛn˧˥] | 'one year' — 一 → *yì* (T4) before T2 年 *nián* |
| 一起 | 一起 | `yī qǐ` | `yì qǐ` | [i˥˩ tɕʰi˨˩˦] | 'together' — 一 → *yì* (T4) before T3 起 *qǐ* |
| 一个 | 一個 | `yī gè` | `yí ge` | [i˧˥ kɤ] | 'one (item)' — 一 → *yí* (T2) before T4 个 *gè* (which here is also neutralized) |
| 一定 | 一定 | `yī dìng` | `yí dìng` | [i˧˥ tiŋ˥˩] | 'certainly' — 一 → *yí* (T2) before T4 定 *dìng* |

#### 不 *bù* Sandhi

不 *bù* 'not' (citation T4, `51`) changes to *bú* (T2, `35`) ONLY before another T4. Before T1/T2/T3 it keeps its T4. In some compounds and the A-not-A and potential-complement constructions it is also reduced to a neutral tone.

**Rules:**

- 不 *bù* + T4 → *bú* (T2, `35`).
- 不 *bù* + T1/T2/T3 → *bù* stays T4 (`51`).
- 不 *bù* as an infix (e.g. 看不见 / 看不見 *kàn bu jiàn* 'cannot see') → often neutral.

| 简体 | 繁體 | Underlying | Surface | IPA (surface) | Gloss |
|---|---|---|---|---|---|
| 不是 | 不是 | `bù shì` | `bú shì` | [pu˧˥ ʂɻ̩˥˩] | 'is not / no' — 不 → *bú* (T2) before T4 是 *shì* |
| 不对 | 不對 | `bù duì` | `bú duì` | [pu˧˥ twei˥˩] | 'incorrect' — 不 → *bú* (T2) before T4 对 *duì* |
| 不好 | 不好 | `bù hǎo` | `bù hǎo` | [pu˥˩ xau˨˩˦] | 'not good' — 不 stays *bù* (T4) before T3 好 *hǎo* |
| 不来 | 不來 | `bù lái` | `bù lái` | [pu˥˩ lai˧˥] | 'not come' — 不 stays *bù* (T4) before T2 来 *lái* |

#### Other Sandhi Notes

Additional tone-change phenomena documented more fully in the Connected Speech and Tone Sandhi section:

- 七 *qī* 'seven' and 八 *bā* 'eight' historically showed sandhi before T4 (→ T2) in some traditional/older norms; in modern Pǔtōnghuà they are usually kept as T1 and this sandhi is optional/recessive.
- Reduplicated and bound forms with 子 *zi*, 头 / 頭 *tou*, and kin reduplications (妈妈 / 媽媽, 弟弟 / 弟弟) trigger neutral tone on the second element.
- Tone sandhi is computed over PROSODIC domains (foot/phrase), so the grouping of words affects which sandhi applies — especially in chains of T3 (see [Third-Tone Sandhi](#third-tone-sandhi) above).
- Sandhi is a SURFACE process: dictionaries and the toneless reader tiers store the UNDERLYING tone (or no tone at all); the spelling never changes.

### Neutral-Tone Distribution

The NEUTRAL TONE (轻声 / 輕聲 *qīngshēng*) is treated here as a suprasegmental process (its pitch realization is in [The Neutral Tone](#the-neutral-tone--轻声--輕聲-qīngshēng) above). A neutral syllable is short, weak, destressed, and pitchless on its own, taking its pitch from the preceding full tone. Neutral-toning is the principal way Mandarin DESTRESSES a syllable, and it is the nearest functional analog to English weak forms / unstressing — though it reduces TONE and DURATION rather than vowel QUALITY (no schwa-reduction system).

#### Where the Neutral Tone Occurs

| Category | Examples | Note |
|---|---|---|
| **Grammatical particles** | 的 *de* (attributive), 了 *le* (perfective/inchoative), 吗 / 嗎 *ma* (Y/N question), 呢 *ne* (continued-question), 吧 *ba* (suggestion), 着 / 著 *zhe* (durative), 过 / 過 *guo* (experiential), 地 *de* (adverbial), 得 *de* (complement) | These function words are ALWAYS or almost always neutral. |
| **Reduplicated kin terms & reduplications** | 妈妈 / 媽媽 *māma* 'mom', 爸爸 / 爸爸 *bàba* 'dad', 哥哥 / 哥哥 *gēge* 'older brother', 弟弟 / 弟弟 *dìdi* 'younger brother', 看看 / 看看 *kànkan* 'take a look' | The SECOND (repeated) syllable is neutral. |
| **Certain suffixes** | 子 *zi* (桌子 *zhuōzi* 'table', 椅子 *yǐzi* 'chair'), 头 / 頭 *tou* (木头 / 木頭 *mùtou* 'wood'), 们 / 們 *men* (我们 / 我們 *wǒmen* 'we' — often neutral), 么 / 麼 *me* (什么 / 什麼 *shénme* 'what') | Nominalizing/pluralizing suffixes typically go neutral. |
| **Directional/resultative second syllables & some disyllables** | 知道 / 知道 *zhīdao* 'know', 朋友 / 朋友 *péngyou* 'friend', 喜欢 / 喜歡 *xǐhuan* 'like', 东西 / 東西 *dōngxi* 'thing', 起来 / 起來 *qǐlai* (directional complement) | Many high-frequency disyllabic words lexically neutralize the second syllable; membership varies by standard. |

#### Contrastive Function of the Neutral Tone

Neutral-toning can be CONTRASTIVE (lexically distinguishing words), so it is not purely phonetic.

| 简体 | 繁體 | Neutral | Full | Gloss |
|---|---|---|---|---|
| 东西 | 東西 | `dōngxi` (西 neutral) = 'thing / stuff' | `dōngxī` (西 full T1) = 'east and west / east-west (direction)' | neutral vs full tone distinguishes two meanings |
| 地道 | 地道 | `dìdao` (道 neutral) = 'genuine / authentic' | `dìdào` (道 full T4) = 'tunnel / underground passage' | neutral-toning is lexically contrastive here |

> **Note:** Neutral-tone membership is one of the most variable areas between the two standards: Taiwan 國語 *Guóyǔ* uses FEWER neutral tones and frequently restores a full citation tone where Pǔtōnghuà neutralizes (e.g. 蝴蝶 *húdié* in Guóyǔ vs 蝴蝶 *húdie* often neutral in Pǔtōnghuà; 喜欢 / 喜歡 *xǐhuān* vs *xǐhuan*) — see [Pǔtōnghuà vs Guóyǔ](#pǔtōnghuà-vs-guóyǔ-suprasegmental-differences).

### Erhua — 儿化 / 兒化 (*érhuà*)

ERHUA (儿化 / 兒化 *érhuà*), 'r-coloring' or rhotacization, is a suprasegmental/phonological process by which a suffixed 儿 / 兒 (`-r`, pinyin `-r`, the rhotic 儿 / 兒 *ér*) MERGES with and RHOTACIZES the preceding syllable's final, restructuring the rime rather than adding a separate syllable. The result is a single syllable whose rime ends in a rhotic [ɚ]/[ɻ]; the tone of the base syllable is retained. Erhua is a hallmark of Beijing-based Pǔtōnghuà and is largely ABSENT from Taiwan 國語 *Guóyǔ*.

**Phonetics:** The added `-r` is the retroflex/rhotic coda [ɚ ~ ɻ]; depending on the original final, erhua may (a) simply add r-coloring, (b) DELETE a coda (front `-i`, `-n` drop; `-ng` may nasalize and rhotacize), or (c) modify the nucleus. The syllable count does NOT increase: 花儿 / 花兒 *huār* is ONE syllable, not 'hua + er'.

**IPA notation:** Rhotic coda [ɚ] / r-colored vowel [˞] (e.g. [a˞], [ɤ˞]) or [ɻ] coda; the standalone 儿 / 兒 *ér* 'son/child' is [ɚ˧˥] (T2).

| 简体 | 繁體 | Pinyin | IPA | Gloss |
|---|---|---|---|---|
| 花儿 | 花兒 | `huār` | [xwa˞˥] | 'flower' — simple r-coloring of the `-a` final |
| 一点儿 | 一點兒 | `yìdiǎnr` | [i˥˩ tjɑ˞˨˩˦] | 'a little' — the `-n` coda is DELETED and the vowel rhotacized |
| 玩儿 | 玩兒 | `wánr` | [wɑ˞˧˥] | 'to play' — `-n` drops, rime rhotacized; one syllable |
| 这儿 | 這兒 | `zhèr` | [ʈʂɚ˥˩] | 'here' — base 这 *zhè* + `r` → [ʈʂɚ] |
| 小孩儿 | 小孩兒 | `xiǎoháir` | [ɕjau˨˩ xaɚ˧˥] | 'child' — final `-i` absorbed into the rhotic |
| 味儿 | 味兒 | `wèir` | [weɚ˥˩] | 'smell/flavor' — colloquial Beijing erhua |

**Functions:** Erhua can be (a) purely colloquial/register (Beijing flavor), (b) DIMINUTIVE/affectionate, or (c) lexically/grammatically DISTINCTIVE (e.g. 画 / 畫 *huà* 'to paint (verb)' vs 画儿 / 畫兒 *huàr* 'a painting (noun)'; 头 / 頭 *tóu* 'head' vs 头儿 / 頭兒 *tóur* 'boss/leader'), where erhua also nominalizes or changes meaning.

> **Note:** The standard reference for erhua is Pǔtōnghuà; Taiwan Guóyǔ has LITTLE OR NO erhua (it is perceived as a Beijing/northern feature) and typically uses the non-erhua form (e.g. 一点 / 一點 *yìdiǎn* rather than 一点儿 / 一點兒 *yìdiǎnr*) — see [Pǔtōnghuà vs Guóyǔ](#pǔtōnghuà-vs-guóyǔ-suprasegmental-differences). The Peshitta reader tiers do not encode erhua.

### Stress & Prominence

Mandarin has **NO contrastive LEXICAL STRESS** of the English type (there are no minimal pairs distinguished by stress placement alone the way `/ˈrecord/`–`/reˈcord/` are). 'Stress' in Mandarin is better understood as PROMINENCE that arises from (a) full TONE realization vs neutral-tone DESTRESSING, (b) duration and pitch-range, and (c) sentence-level focus/intonation — NOT from a lexically stored stressed syllable with vowel reduction.

#### How Prominence Works

| Mechanism | Description |
|---|---|
| **Tone vs neutral tone** | A full-toned syllable is inherently more prominent (longer, with a full pitch contour) than a NEUTRAL-toned one. The neutral tone is the primary destressing device; e.g. in 桌子 *zhuōzi* 'table', 桌 *zhuō* (full T1) is prominent and 子 *zi* (neutral) is reduced. This is the Mandarin functional analog of English stressed-vs-unstressed, achieved tonally. |
| **Disyllabic foot prominence** | In disyllabic words both syllables usually keep full tones, but there is a mild rhythmic prominence pattern (often weak-strong or strong-weak by lexical/prosodic factors). Mandarin disyllables do NOT reduce the weak member to schwa; both vowels stay full unless one is lexically neutral. |
| **Sentence stress / focus** | At the sentence level, the FOCUSED (new-information or contrastive) word receives PROMINENCE via expanded pitch range, increased duration, and intensity — without changing its lexical tone's identity. This is intonational/focus prominence layered on top of the lexical tones (see [Focus](#focus)). |

**Contrast with English:** ENGLISH stress is phonemic and drives vowel reduction (schwa). MANDARIN has neither: prominence does not relocate to create minimal pairs, and unstressed syllables are reduced by NEUTRAL-TONING (loss of tone + shortening), not by vowel-quality reduction to schwa. The closest Mandarin has to English 'weak forms' is the set of obligatorily neutral particles (的 了 吗/嗎 呢).

> **Note:** Some loanword and emphatic patterns can shift perceived prominence, but no analysis posits contrastive lexical stress for Standard Mandarin.

### Intonation

INTONATION in Mandarin is sentence-level pitch (and pitch-range, duration, and tempo) used for sentence-type, focus, and attitude — **OVERLAID** on the lexical tones rather than replacing them. This is the crucial difference from English: because each syllable already carries a contrastive tone, Mandarin intonation cannot freely reshape the pitch of every syllable. Instead it works through (a) GLOBAL pitch-range and register adjustments (e.g. raising the overall register and the final syllable for questions, sometimes called 'tone raising' or expansion), (b) DECLINATION (gradual lowering across the utterance), (c) FOCUS prominence (pitch-range expansion on the focused word + post-focal compression), and above all (d) SENTENCE-FINAL PARTICLES (语气词 / 語氣詞 *yǔqìcí*) that carry much of the grammatical/attitudinal load that English assigns to intonation and inversion. The lexical tones are preserved; intonation modulates the SCALE on which they are realized.

#### Tone–Intonation Interaction

The key principle: intonation is realized as adjustments to the pitch RANGE and REGISTER within which the lexical tone contours are produced (the 'superposition' / 'small ripples on a big wave' model — local tone contours ride on a global intonation contour). A question's final rise does NOT erase a final T4's fall; rather, the T4 is realized HIGHER in the range or with a compressed/raised endpoint, so the falling tone is still falling but produced at a raised register. This layering is the Mandarin solution to having both lexical tone AND sentence intonation.

**IPA notation:** Global movements: `↗` rise, `↘` fall, `→` level; the local syllable tones keep their tone letters (`˥` `˧˥` `˨˩˦` `˥˩`); a raised final register may be shown as an upshifted contour. Phrase/IP boundaries `|` and `‖`.

#### Intonation Patterns

| Type | Contour | Symbol | Example |
|---|---|---|---|
| **Declarative / statement** — 陈述句 / 陳述句 (*chénshùjù*) | Overall DECLINATION with a low/falling end; lexical tones realized in a gradually lowering register. | `↘` (global) | 他是学生。 / 他是學生。 `Tā shì xuésheng.` [tʰa˥ ʂɻ̩˥˩ ɕɥɛ˧˥ ʂɤŋ ↘] 'He is a student.' — neutral statement, declining register; 生 *sheng* often neutral. |
| **Particle yes/no question** (with 吗 / 嗎 *ma*) — 是非问句 / 是非問句 | Raised final register; 吗 / 嗎 *ma* carries the question; lexical tones preserved. | `↗` (mild, global) + 吗 / 嗎 | 他是学生吗？ / 他是學生嗎？ `Tā shì xuésheng ma?` [tʰa˥ ʂɻ̩˥˩ ɕɥɛ˧˥ ʂɤŋ ma ↗] 'Is he a student?' — the particle 吗 / 嗎 *ma* + a slightly raised final register mark the polar question. |
| **Intonation-only yes/no question** (no 吗 / 嗎) — echo/confirmation | RAISED overall register / raised final, no particle — the intonational statement↔question contrast. | `↗` (global, stronger) | 他是学生？ / 他是學生？ `Tā shì xuésheng?` [tʰa˥ ʂɻ̩˥˩ ɕɥɛ˧˥ ʂɤŋ ↗] 'He's a student?' — no 吗 / 嗎; a raised register + raised final turns the statement into a (surprised/confirming) question. The lexical tones still surface (e.g. 生 stays in its register), only the global scale is raised. |
| **A-not-A question** — 正反问句 / 正反問句 (*zhèngfǎn wènjù*) | Neutral/declarative-like register; the question is GRAMMATICAL (verb + 不 + verb), not intonational. | `→` / `↘` | 你是不是学生？ / 你是不是學生？ `Nǐ shì bu shì xuésheng?` [ni˨˩ ʂɻ̩˥˩ pu ʂɻ̩˥˩ ɕɥɛ˧˥ ʂɤŋ] 'Are you a student (or not)?' — the A-not-A frame 是不是 marks the question structurally; intonation can stay statement-like (不 here is reduced/neutral). |
| **Content (wh-) question** — 特指问句 / 特指問句 (with 谁 / 誰, 什么 / 什麼, 哪儿 / 哪兒, etc.) | Often FALLING/declarative register; prominence (focus) on the interrogative word. | `↘` with focus peak on the question word | 你是谁？ / 你是誰？ `Nǐ shì shéi?` [ni˨˩ ʂɻ̩˥˩ ʂei˧˥ ↘] 'Who are you?' — the interrogative 谁 / 誰 *shéi* is the focus; the contour can be statement-like (a final rise is NOT required because the wh-word marks the question). |
| **Continuation / non-final** (listing, conjoined clause) | Sustained or slightly raised, 'more to come'; the final clause then falls. | `→` / `↗` (non-final), `↘` (final) | 我买了苹果、橘子和葡萄。 / 我買了蘋果、橘子和葡萄。 `Wǒ mǎi le píngguǒ, júzi hé pútao.` [wo˨˩ mai˨˩ lɤ pʰiŋ˧˥ kwo˨˩˦ ↗ tɕy˧˥ tsɹ̩ ↗ xɤ˧˥ pʰu˧˥ tʰau ↘] 'I bought apples, oranges, and grapes.' — non-final list items sustain/rise; the final item falls. |

**Sentence-final particles modulate attitude — 语气词 / 語氣詞 (*yǔqìcí*):** the neutral-toned particle takes a final rise/fall conveying attitude (`↗` / `↘` on the particle).

| 简体 | 繁體 | Pinyin | IPA | Gloss |
|---|---|---|---|---|
| 好吧。 | 好吧。 | `Hǎo ba.` | [xau˨˩ pa ↘] | 'OK then.' — 吧 *ba* softens to a suggestion/acquiescence (falling/settling). |
| 是吧？ | 是吧？ | `Shì ba?` | [ʂɻ̩˥˩ pa ↗] | 'Right?' — 吧 *ba* with a rise seeks confirmation. |
| 走吧！ | 走吧！ | `Zǒu ba!` | [tsou˨˩ pa] | 'Let's go!' — 吧 *ba* forms a hortative/suggestion. |
| 你呢？ | 你呢？ | `Nǐ ne?` | [ni˨˩ nɤ ↗] | 'And you?' — 呢 *ne* forms a follow-up question with a rise. |
| 太好了！ | 太好了！ | `Tài hǎo le!` | [tʰai˥˩ xau˨˩ lɤ] | 'Wonderful!' — 了 *le* + expanded pitch range exclaims. |

#### Focus

FOCUS (new/contrastive information) is marked prosodically by EXPANDING the pitch range and increasing the duration/intensity of the focused word (sentence stress), and by COMPRESSING the pitch range of POST-FOCAL material (post-focal reduction) — all WITHOUT changing the focused syllable's lexical tone identity. Focus can also be marked grammatically (是…的 *shì…de* cleft, 连 / 連…也 / 都 'even', word order).

| Focus | Example |
|---|---|
| Neutral (broad focus) | 我明天去北京。 / 我明天去北京。 *Wǒ míngtiān qù Běijīng.* 'I'm going to Beijing tomorrow.' |
| Narrow focus on object | 我明天去【北京】。 — narrow focus on 北京 *Běijīng* ('it's BEIJING I'm going to'): pitch range expands on 北京, and any post-focal material is compressed; the tones of 北 *Běi* (T3, half-third) and 京 *jīng* (T1) keep their shapes but are realized in an expanded range. |

#### Functions Overview

| Function | Description |
|---|---|
| **Grammatical** | Distinguishes statement (declining/falling register) from intonation-only question (raised register), but much sentence-type marking is GRAMMATICAL — question particle 吗 / 嗎, A-not-A frames, wh-words, and sentence-final particles 吧 / 呢 / 啊 — relieving intonation of the load it carries in English. |
| **Focus & information** | Pitch-range EXPANSION on the focused word + POST-FOCAL COMPRESSION marks focus/new information; works with 是…的 clefts and word order rather than relocating a stress nucleus. |
| **Attitudinal** | Final rise/fall on sentence-final particles (吧, 呢, 啊, 嘛) plus global pitch range convey suggestion, confirmation-seeking, surprise, doubt, impatience, affection. |
| **Discourse** | Declination, phrasing, and particle choice manage turn-taking, topic structure, and the topic-prominent information flow characteristic of Mandarin. |

### Pǔtōnghuà vs Guóyǔ Suprasegmental Differences

The two REFERENCE STANDARDS differ in several SUPRASEGMENTAL respects even though they share the four-tone + neutral system and the same toneless spelling. The differences are surface/lexical (which tone a given character takes, how much neutral-toning and erhua occur) and DO NOT change the phonemic tone inventory or the toneless reader tiers.

| Feature | 普通话 *Pǔtōnghuà* (PRC) | 國語 *Guóyǔ* (Taiwan) | Note |
|---|---|---|---|
| **Neutral tone (轻声 / 輕聲) frequency** | Uses the neutral tone FREELY and on many disyllables (喜欢 *xǐhuan*, 蝴蝶 *húdie*, 先生 *xiānsheng*, 衣服 *yīfu*). | Uses FEWER neutral tones, often restoring a full citation tone (喜歡 *xǐhuān*, 蝴蝶 *húdié*, 先生 *xiānshēng*, 衣服 *yīfú*). | One of the most audible Pǔtōnghuà–Guóyǔ differences; affects rhythm and perceived prominence. |
| **Erhua (儿化 / 兒化)** | (Beijing-based) has frequent erhua (一点儿 *yìdiǎnr*, 玩儿 *wánr*, 这儿 *zhèr*, 好玩儿 *hǎowánr*). | Has LITTLE OR NO erhua, using the plain final (一點 *yìdiǎn*, 玩 *wán*, 這裡 *zhèlǐ* 'here'). | Erhua is perceived as a northern/Beijing feature; its near-absence is a salient marker of Taiwan Guóyǔ. |
| **Lexical tone differences** (same character, different tone) | 垃圾 *lājī* 'garbage'; 和 *hé* 'and'; 企 *qǐ* (企业 *qǐyè*); 期 *qī*; 危 *wēi*; 法 *fǎ* (法国 *Fǎguó*). | 垃圾 *lèsè*; 和 *hàn* (colloquial 'and'); 企 *qì* (企業 *qìyè*); 期 *qí*; 危 *wéi*; 法 *fà* (法國 *Fàguó*). | A set of well-known characters carry DIFFERENT citation tones across the two standards — a lexical, not systemic, difference. Example 垃圾: Pǔtōnghuà *lājī* vs Guóyǔ *lèsè* (different reading entirely). |
| **Third-tone sandhi & tone realization** | Robust T3 sandhi and clear half-third; Beijing tones have a wide pitch range. | Same `T3 + T3 → T2 + T3` rule, but Guóyǔ T3 is often realized with a less pronounced dip and a somewhat compressed overall range; some speakers' tone contours differ subtly in slope. | The sandhi RULE is shared; the phonetic realization (range, slope) differs by standard and accent. |
| **De-retroflexion** (interacts with rime/prosody) | Maintains the retroflex initials zh/ch/sh/r and the apical retroflex rime `-i` [ɻ̩]. | Much Taiwan Guóyǔ shows DE-RETROFLEXION (zh/ch/sh/r → z/c/s/-), affecting the apical-rime quality though not the tone itself. | Documented in detail in the Consonants and Dialect Differences sections; noted here because it changes the segmental host on which the tone rides. |

**Shared:** BOTH standards have the SAME four lexical tones + neutral tone, the SAME pinyin/zhuyin tone notations, the SAME third-tone / 一 / 不 sandhi RULES, and the SAME toneless underlying spelling. The differences above are surface/lexical.

### The Reader Tiers Are Toneless

CRITICAL distinction for this guide: **tones describe the LANGUAGE (Mandarin)**, and are documented exhaustively here; but the Chinese Peshitta **READER TIERS are emitted TONELESS** by design.

**Why toneless:** The Peshitta SOURCE IPA (the Aramaic phonetic spine) carries NO tone. Mapping it into Mandarin produces a TONELESS phonetic representation: the reader tiers are deliberately atonal because there is no tonal information in the source to encode. Tone is a property of Mandarin words, not of the transliterated Aramaic.

**Tier behavior:**

| Tier | Tone behavior |
|---|---|
| **Toneless Pinyin** | Bare pinyin letters with NO tone diacritics (the deterministic phonetic spine). |
| **Zhuyin / Bopomofo** | A transcode of the toneless pinyin, likewise WITHOUT tone marks. |
| **Hanzi** (Simplified 简体字 & Traditional 繁體字) | A downstream transcription-character lookup. Because every Hanzi inherently carries a CITATION tone, the Hanzi tier UNAVOIDABLY imposes a tone per character — but this is an ARTIFACT of using tone-bearing characters to write atonal source material, NOT a source feature. Readers should treat the Hanzi-tier tones as incidental. |
| **Scholarly & Pretty** (language-neutral Latin) | Toneless by construction. |

**Implication:** All TONE SANDHI (third-tone, 一, 不), NEUTRAL-TONE distribution, ERHUA, and INTONATION described in this section are facts about spoken Mandarin and are **NOT** encoded in the toneless reader tiers (except the incidental citation tones forced by the Hanzi lookup). A reader using the Peshitta tiers consults THIS section for the tonal and prosodic reality of the language.

### Comparison to Other Systems

Explicit cross-system placement of Mandarin prosody, since this guide is one of a parallel set (English, French, Spanish, Korean, Japanese, …). The single sentence to remember: **MANDARIN = a TONE language** (4 lexical tones + neutral, one contrastive tone per syllable); **JAPANESE = lexical PITCH ACCENT** (one drop per word); **KOREAN = no word-level stress/tone** (phrase-level pitch only); **ENGLISH = lexical STRESS** (stress-timed, with schwa reduction).

| Feature | Mandarin | Japanese | Korean | English |
|---|---|---|---|---|
| **Word-level prominence type** | LEXICAL TONE — one contrastive pitch CONTOUR on EVERY syllable (妈/麻/马/骂) | LEXICAL PITCH ACCENT — at most one contrastive pitch DROP per word (箸/橋) | NONE at the word level — no lexical stress, no lexical tone | LEXICAL STRESS — contrastive stressed syllable (`/ˈrecord/`–`/reˈcord/`) |
| **Phonetic correlate of the contrast** | PITCH CONTOUR (level/rising/dipping/falling) on the syllable's rime | PITCH (a drop), docked to a mora; NOT loudness | Phrase-edge pitch only; no word prominence | Loudness + duration + pitch + full vowel quality on the stressed syllable |
| **Vowel reduction (schwa)** | NONE of the English kind; reduction is via the NEUTRAL TONE (loss of tone + shortening), full vowels otherwise | NONE (full vowels; only high-vowel DEVOICING) | NONE (full vowels) | EXTENSIVE (unstressed → schwa) |
| **Rhythmic timing** | SYLLABLE-TIMED-tending; the SYLLABLE is the tone-bearing unit | MORA-TIMED (counts moras) | Syllable-timed-tending | STRESS-TIMED (compress unstressed syllables to a beat) |
| **Minimal pairs by suprasegment** | YES, by TONE — dense four/five-way sets (妈麻马骂吗; shī/shí/shǐ/shì) | YES, by PITCH ACCENT (箸 ha\shi / 橋 hashi\ / 端 hashi) | NO (Standard) — except peripheral pitch-accent dialects | YES, by STRESS (record N/V, present N/V) |
| **Connected-speech tonal/pitch changes** | TONE SANDHI (T3 + T3 → T2 + T3; 一 / 不 sandhi); neutral-toning; erhua | Downstep/catathesis; compound-accent rules; high-vowel devoicing | AP-tune assignment + IP boundary tones (phrase-level only) | Weak forms, vowel reduction, pre-fortis clipping, nuclear-tone choice |
| **Sentence-type marking** | Mostly GRAMMATICAL (吗 / 嗎, A-not-A, wh-words, final particles 吧 / 呢) + raised register for particle-less questions; tones preserved | Question particle か + final RISE; final particles ね / よ | IP boundary tone carries a very heavy load | Inversion/do-support + nuclear intonation |

### Cross-References

| Topic | Reference |
|---|---|
| **Tones** | The four-tone + neutral inventory, Chao letters, and notation systems defined here key the tone framework in the meta material and the tone columns throughout the guide; the consonant–vowel IPA matrix is given TONELESS, with tone supplied from this section. |
| **Consonants** | Tone rides on the VOICED rime; the (un)aspirated initials and the retroflex/apical series (zh/ch/sh/r → apical `-i` [ɻ̩]) host the tone. De-retroflexion in Guóyǔ changes the segmental host but not the tone; see Consonants and Dialect Differences. |
| **Vowels & finals** | Tone-bearing units are the rimes (nucleus + medial glide + coda /n ŋ/ or rhotic /ɚ/); erhua RESTRUCTURES the rime (deletes `-i`/`-n`, rhotacizes the nucleus) while preserving the tone — see Vowels, Diphthongs/Finals, and Syllable Structure. |
| **Syllable structure** | Each (C)(G)V(C) syllable carries exactly one tone (~400 toneless / ~1300 tone-bearing syllables, near one-syllable-per-morpheme/character); the tone-bearing-unit discussion underpins the syllable chart. |
| **Connected speech & tone sandhi** | Tone sandhi (third-tone, 一, 不), neutral-tone distribution, erhua, fusion/reduction, and the role of sentence-final particles are ALSO collected — with surface-result examples — in the Connected Speech and Tone Sandhi section; this section gives the systematic tonal definitions and the sandhi rules in depth. |
| **Phonological rules** | Tone sandhi is the principal tonal phonological rule; segmental rules (assimilation, the apical-vowel rule, erhua rime restructuring) are detailed in Phonological Rules. |
| **Dialect differences** | The Pǔtōnghuà vs Guóyǔ neutral-tone, erhua, lexical-tone, and de-retroflexion contrasts are expanded in Dialect Differences; this section gives the prosody-specific contrasts. |
| **Orthography** | Pinyin tone DIACRITICS (`ā á ǎ à`) and Zhuyin tone MARKS (`ˊ ˇ ˋ ˙`) — and the Hanzi tier's incidental citation tones — are detailed in Orthography & Grapheme–Phoneme; Hanzi is non-phonemic (carries no tone information in the glyph beyond the lexical reading), whereas pinyin/zhuyin ARE phonemic and can mark tone. |

**Companion files:**

- `Chinese/chinese_pronunciation_guide.md`
- `Chinese/Peshita_Chinese/Scholarly/`
- `Chinese/Peshita_Chinese/Pretty/`
- `Chinese/Peshita_Chinese/Pinyin/`
- `Chinese/Peshita_Chinese/Zhuyin/`
- `Chinese/Peshita_Chinese/Hanzi-Simplified/`
- `Chinese/Peshita_Chinese/Hanzi-Traditional/`

> **Reader-tiers note:** The Chinese Peshitta ships SIX reader tiers — Scholarly and Pretty (language-neutral Latin), TONELESS PINYIN (the deterministic phonetic spine), ZHUYIN / BOPOMOFO (a transcode of the toneless pinyin), and HANZI in SIMPLIFIED (简体字) and TRADITIONAL (繁體字) (a downstream transcription-character lookup). The reader tiers are TONELESS because the Peshitta source IPA carries NO tone; the Hanzi tiers unavoidably impose a citation tone per character (an artifact, not a source feature). All TONE, TONE SANDHI, NEUTRAL-TONE, ERHUA, and INTONATION information lives in THIS section and describes the LANGUAGE, not the toneless reader tiers — see [The Reader Tiers Are Toneless](#the-reader-tiers-are-toneless) above.

---

*Section compiled by Shin.*

## Syllable Structure

Syllable structure in Standard Mandarin Chinese (标准汉语 / 標準漢語), documented in parallel for the two reference standards: 普通话 Pǔtōnghuà (PRC Standard Mandarin, Beijing-based phonology, Simplified characters, Hanyu Pinyin) and 國語 Guóyǔ (Taiwan Standard Mandarin, Traditional characters, Zhuyin/Bopomofo). The Mandarin syllable is small, rigid, and famously CV-favoring: it has the maximal shape (C)(G)V(C) plus an obligatory lexical TONE, with NO consonant clusters anywhere and codas restricted to /n/, /ŋ/ (`-ng`), and the rhotic /ɚ/ (`er` / 儿化 érhua). The syllable is the central phonological constituent of Mandarin and is near-isomorphic with the morpheme and with the written character: one 汉字 / 漢字 hanzi ≈ one syllable ≈ (usually) one morpheme. The toneless syllable inventory is tiny — roughly 400 distinct (C)(G)V(C) shapes — expanding to about 1300 distinct syllables once the four tones plus the neutral tone are counted; this small, fully enumerable inventory is exactly what makes a deterministic pinyin/zhuyin transducer possible. Because Mandarin tolerates no clusters and only nasal/rhotic codas, foreign words are repaired by HEAVY VOWEL EPENTHESIS and coda deletion onto legal syllables (基督 Jīdū 'Christ', 巴拉巴 Bālābā 'Barabbas'), the same forced operation the Peshitta Pinyin and Zhuyin reader tiers perform. This section is the Mandarin equivalent of the Peshitta guide's syllable_structure section.

> **NOTE:** the language is fully TONAL and tone is documented as an obligatory syllable component here; the toneless quality belongs only to the Peshitta reader tiers, which strip tone because the Aramaic source IPA carries none.

**IPA template:** `(C)(G)V(C) + T`

**Pinyin template:** `(声母 initial)(介音 medial)(韵腹 nucleus)(韵尾 coda) + 声调 tone`

**Maximal syllable:** `CGVC + T` — e.g. 双 `shuāng` /ʂwaŋ/ T1, 想 `xiǎng` /ɕjaŋ/ T3, 选 `xuǎn` /ɕɥɛn/ T3 (onset + medial glide + nucleus + nasal coda + tone)

**Minimal syllable:** `V + T` — a bare toned nucleus, e.g. 啊 `ā` /a/ T1, 饿 `è` /ɤ/ T4

**Preferred syllable:** `CV + T` — onset + nucleus + tone; the statistically dominant and least-marked shape, e.g. 他 `tā`, 妈 `mā`

**Obligatory tone:** Every full (non-neutral) syllable carries exactly one of four lexical tones (T1 阴平/陰平 [˥], T2 阳平/陽平 [˧˥], T3 上声/上聲 [˨˩˦], T4 去声/去聲 [˥˩]); some grammatical/affixal syllables carry the neutral tone (轻声/輕聲). Tone is a structural component of the syllable, not a suprasegmental add-on: `mā` 妈/媽, `má` 麻, `mǎ` 马/馬, `mà` 骂/罵 are four different syllables/morphemes sharing the segmental shape /ma/.

### Reference Standards

| Standard | Description |
|---|---|
| 普通话 Pǔtōnghuà | PRC Standard Mandarin, Beijing-based phonology; written in SIMPLIFIED characters (简体字) and romanized with Hanyu Pinyin (汉语拼音). |
| 國語 Guóyǔ | Taiwan Standard Mandarin; written in TRADITIONAL characters (繁體字) and taught with Zhuyin/Bopomofo (注音符號). |

The SYLLABLE STRUCTURE proper — the (C)(G)V(C) template, the no-cluster phonotactics, the /n ŋ ɚ/-only codas, the obligatory tone — is identical across both standards; the toneless segmental spelling is shared. The standards differ in SURFACE realization riding on this skeleton, not in the skeleton itself: Guóyǔ has little or no érhua (so it rarely generates the /ɚ/-coda / rime-restructured syllables that Pǔtōnghuà does), shows frequent DE-RETROFLEXION (`zh ch sh r` → `z c s -`, e.g. 是 `shì` → sì-like), keeps fewer neutral tones (so more syllables surface with a full tone), and carries some lexical tone/segment differences (垃圾 `lājī` vs `lèsè`; 和 `hé` vs `hàn`; 企 `qǐ` vs `qì`). These are surface/lexical and do not change the toneless pinyin spine on which both tiers are built. The two standards also key the two hanzi script tiers (Simplified ↔ Pǔtōnghuà, Traditional ↔ Guóyǔ).

### Components

| Slot | Chinese term | Status | Min C | Max C |
|---|---|---|---|---|
| Initial (onset) | 声母 / 聲母 shēngmǔ | optional | 0 | 1 |
| Medial (on-glide) | 介音 jièyīn | optional | — | 1 glide |
| Nucleus (main vowel) | 韵腹 / 韻腹 yùnfù | **required** | — | 1 vowel |
| Coda | 韵尾 / 韻尾 yùnwěi | optional | 0 | 1 |
| Tone | 声调 / 聲調 shēngdiào | **required** (full syllables) | — | 1 tone |

The nucleus and tone are the only mandatory components.

#### Initial (声母 / 聲母 shēngmǔ)

The optional single onset consonant — Mandarin has NO onset clusters whatsoever (no /pl/, /st/, /spr/, etc.). The slot is filled by one of the 21 initial consonants, or it is empty (the ZERO INITIAL 零声母, where the syllable begins with a medial glide or directly with the nucleus). The contrast among stops/affricates is ASPIRATION, not voicing: `b` /p/ vs `p` /pʰ/, `d` /t/ vs `t` /tʰ/, `g` /k/ vs `k` /kʰ/, `z` /ts/ vs `c` /tsʰ/, `zh` /ʈʂ/ vs `ch` /ʈʂʰ/, `j` /tɕ/ vs `q` /tɕʰ/. The alveolo-palatals `j` /tɕ/, `q` /tɕʰ/, `x` /ɕ/ are in COMPLEMENTARY DISTRIBUTION with the dentals `z/c/s`, retroflexes `zh/ch/sh` and velars `g/k/h` — they occur only before the high front vocoids `i` /i/ and `ü` /y/ — so an initial both selects and is selected by the following final.

- **Minimum consonants:** 0
- **Maximum consonants:** 1
- **No clusters:** Mandarin permits no consonant clusters in any position. The only consonant SEQUENCE within a syllable is an initial followed (after the vowel) by a nasal coda (e.g. CVN as in 班 `bān`, CVNG as in 帮/幫 `bāng`); these are onset + coda around the nucleus, never a cluster. Foreign clusters are repaired by epenthesis of a default vowel, each broken-out consonant spawning a new (C)V syllable — the core operation of the pinyin/zhuyin reader-tier transducer (see Loanword Adaptation and Constraints).

**Initial inventory** (21 initials + the zero initial):

| Pinyin | IPA | Zhuyin | Class |
|---|---|---|---|
| `b` / `p` | /p/, /pʰ/ | `ㄅ` `ㄆ` | labial stops |
| `d` / `t` | /t/, /tʰ/ | `ㄉ` `ㄊ` | alveolar stops |
| `g` / `k` | /k/, /kʰ/ | `ㄍ` `ㄎ` | velar stops |
| `z` / `c` | /ts/, /tsʰ/ | `ㄗ` `ㄘ` | dental affricates |
| `zh` / `ch` | /ʈʂ/, /ʈʂʰ/ | `ㄓ` `ㄔ` | retroflex affricates |
| `j` / `q` | /tɕ/, /tɕʰ/ | `ㄐ` `ㄑ` | alveolo-palatal affricates (before `i`/`ü` only) |
| `f` | /f/ | `ㄈ` | fricative |
| `s` | /s/ | `ㄙ` | fricative |
| `sh` | /ʂ/ | `ㄕ` | fricative |
| `r` | /ʐ~ɻ/ | `ㄖ` | fricative |
| `x` | /ɕ/ | `ㄒ` | fricative |
| `h` | /x/ | `ㄏ` | fricative |
| `m` | /m/ | `ㄇ` | nasal |
| `n` | /n/ | `ㄋ` | nasal |
| `l` | /l/ | `ㄌ` | lateral |
| ∅ | — | — | zero initial 零声母 (syllable begins with a medial glide `y-`/`w-` or directly with the nucleus) |

**Examples:**

| IPA | Pinyin | Zhuyin | Initial | 汉字 (Simp.) | 漢字 (Trad.) | Gloss |
|---|---|---|---|---|---|---|
| /pʰa/ | `pā` | `ㄆㄚ` | `p` /pʰ/ (aspirated) | 趴 | 趴 | lie prone — aspiration contrast with `b` /p/ (八 `bā` 'eight') |
| /tɕi/ | `jī` | `ㄐㄧ` | `j` /tɕ/ (alveolo-palatal, only before high front `i`/`ü`) | 鸡 | 雞 | chicken — `j/q/x` select a following `i` or `ü` |
| /ʈʂɻ̩/ | `zhī` | `ㄓ` | `zh` /ʈʂ/ (retroflex) | 知 | 知 | know — retroflex initial; the apical 'buzzed' vowel [ɻ̩] is written `-i` (de-retroflexed to zī-like in much Guóyǔ) |
| /wo/ | `wǒ` | `ㄨㄛ` | ∅ zero initial (medial /w/ spelled `w-`) | 我 | 我 | I/me — zero-initial syllable; the /u/ medial is written `w-` word-initially |
| /a/ | `ā` | `ㄚ` | ∅ zero initial (bare nucleus) | 啊 | 啊 | ah! — onsetless, glideless syllable: a bare toned vowel |

#### Medial (介音 jièyīn — medial glide / on-glide)

The optional pre-nuclear glide between the initial and the nucleus — one of three high vocoids acting as on-glides: `i` /j/, `u` /w/, `ü` /ɥ/ (the rounded front glide). The medial is the head of the 四呼 (four classes of finals): 开口呼 (no medial), 齐齿呼 (`i-`/j- medial), 合口呼 (`u-`/w- medial), 撮口呼 (`ü-`/ɥ- medial). In zero-initial syllables the medial surfaces in spelling as `y-` (for `i`/`ü`) or `w-` (for `u`): `i+an → yan`, `u+an → wan`, `ü+an → yuan`; after `j/q/x` the `ü` medial drops its umlaut (`ju` = /tɕy/, `jue` = /tɕɥɛ/). Only ONE medial may appear; there is no cluster of glides.

**Medial glides:**

| Pinyin | IPA | Zhuyin | Class (四呼) | Spelling notes |
|---|---|---|---|---|
| `i` | /j/ | `ㄧ` | 齐齿呼 (palatal on-glide) | spelled `i`, or `y-` word-initially |
| `u` | /w/ | `ㄨ` | 合口呼 (labiovelar on-glide) | spelled `u`, or `w-` word-initially |
| `ü` | /ɥ/ | `ㄩ` | 撮口呼 (rounded palatal on-glide) | spelled `ü`/`u`, `yu-` word-initially, `u` after `j/q/x/y` |

**Examples:**

| IPA | Pinyin | Zhuyin | Medial | 汉字 (Simp.) | 漢字 (Trad.) | Gloss |
|---|---|---|---|---|---|---|
| /tjɛn/ | `tiān` | `ㄊㄧㄢ` | `i` /j/ (齐齿呼) | 天 | 天 | sky/heaven — initial `t` + medial /j/ + nucleus + /n/ coda + T1 |
| /kwo/ | `guó` | `ㄍㄨㄛ` | `u` /w/ (合口呼) | 国 | 國 | country (as in 中国/中國) — initial `g` + medial /w/ + nucleus + T2 |
| /ɕɥɛn/ | `xuǎn` | `ㄒㄩㄢ` | `ü` /ɥ/ (撮口呼; written `u` after `x`) | 选 | 選 | choose/elect — initial `x` + rounded front glide /ɥ/ + nucleus + /n/ coda + T3 |
| /jɛn/ | `yán` | `ㄧㄢ` | `i` /j/ in a zero-initial syllable (spelled `y-`) | 言 | 言 | speech/word — zero initial, /j/ medial written `y-`, nucleus + /n/ coda + T2 |

#### Nucleus (韵腹 / 韻腹 yùnfù — the rime nucleus / main vowel)

The obligatory vocalic core — the only mandatory part of the rime and, with the tone, of the syllable. It is a single vowel drawn from /a o ɤ ɛ i u y/ (pinyin `a o e ê i u ü`), realized with heavy allophony conditioned by the medial and coda: `e` /ɤ/ vs /ə/ (in `-en`, `-eng`), `a` fronting to /ɛ/~/æ/ before /n/ with an `i`/`ü` medial, `o` /o/ chiefly after labials and in `-uo`/`-ou`. A nucleus may also combine with the medial and/or a vocalic off-glide to form DIPHTHONGS (`ai` /ai/, `ei` /ei/, `ao` /au/, `ou` /ou/) and TRIPHTHONGS (`iao` /jau/, `iou`→`-iu` /jou/, `uai` /wai/, `uei`→`-ui` /wei/). The two APICAL ('buzzed') vowels, both written `-i`, are special syllabic continuants that fill the nucleus only after the dental and retroflex sibilants: [ɹ̩] after `z/c/s` (`zi` 资, `ci` 词, `si` 思) and [ɻ̩] after `zh/ch/sh/r` (`zhi` 知, `chi` 吃, `shi` 是, `ri` 日).

- **Required:** yes
- **No syllabic obstruents:** There are no syllabic-consonant nuclei of the English 'bottle/button' type. The closest analogues are the APICAL vowels [ɹ̩]/[ɻ̩] (written `-i`), which are syllabic vocoid continuants, not consonant nuclei, and which exist solely to give the sibilant initials `z/c/s/zh/ch/sh/r` a citation rime.

**Nuclei:**

| Pinyin | IPA | Zhuyin | Description |
|---|---|---|---|
| `a` | /a/ | `ㄚ` | low central, the most open nucleus |
| `o` | /o/ | `ㄛ` | mid back rounded, after labials and in `-uo`/`-ou` |
| `e` | /ɤ/ | `ㄜ` | mid back unrounded; reduces to /ə/ in `-en` /ən/, `-eng` /əŋ/ |
| `ê` / `e` (in `-ie`, `-üe`, `-ian`) | /ɛ/ | `ㄝ` | mid front |
| `i` | /i/ | `ㄧ` | high front unrounded |
| `u` | /u/ | `ㄨ` | high back rounded |
| `ü` | /y/ | `ㄩ` | high front rounded |
| `-i` | [ɹ̩] | — | apical dental vowel, only after `z/c/s` |
| `-i` | [ɻ̩] | — | apical retroflex vowel, only after `zh/ch/sh/r` |

**Examples:**

| IPA | Pinyin | Zhuyin | Nucleus | 汉字 (Simp.) | 漢字 (Trad.) | Gloss |
|---|---|---|---|---|---|---|
| /a/ | `ā` | `ㄚ` | /a/ | 啊 | 啊 | ah! — the bare low nucleus |
| /ɤ/ | `è` | `ㄜ` | /ɤ/ | 饿 | 餓 | hungry — the mid back unrounded nucleus `e` |
| /ai/ | `ài` | `ㄞ` | /a/ + off-glide /i/ (diphthong `ai`) | 爱 | 愛 | love — falling diphthong nucleus |
| /sɹ̩/ | `sī` | `ㄙ` | apical dental [ɹ̩] (written `-i`) | 思 | 思 | think — the buzzed dental vowel after `s`; no [i] is pronounced |
| /ʂɻ̩/ | `shì` | `ㄕ` | apical retroflex [ɻ̩] (written `-i`) | 是 | 是 | to be — the buzzed retroflex vowel after `sh`; de-retroflexed toward sì in much Guóyǔ |

#### Coda (韵尾 / 韻尾 yùnwěi — the rime coda / off-glide or final consonant)

The optional final element of the rime. Mandarin codas are extraordinarily restricted: a syllable may end in (a) nothing (open syllable), (b) a vocalic off-glide /i/ or /u/ forming a diphthong/triphthong (`ai`, `ei`, `ao`, `ou`, and the tri- forms), (c) the nasal /n/ (`-n`) or /ŋ/ (`-ng`), or (d) the rhotic /ɚ/ of 儿/兒 `er` and 儿化 érhua. There are NO obstruent codas (no final stops, no final /m/, no /s/, etc.) and NO consonant clusters in the coda. The two nasal codas are the only true consonantal finals; /ŋ/ (`-ng`) never occurs as an initial. The rhotic /ɚ/ appears either as the standalone syllable `er` (儿/兒, `ér`/`èr`) or as the érhua suffix `-r` that rhotacizes and restructures a preceding rime (花儿/花兒 `huār`, 一点儿/一點兒 `yìdiǎnr`) — Pǔtōnghuà uses it freely; Guóyǔ rarely does.

- **Minimum consonants:** 0
- **Maximum consonants:** 1
- **No obstruent codas:** Unlike Middle Chinese (which had `-p -t -k -m`), Standard Mandarin has lost all stop codas and the bilabial nasal /m/; only /n/, /ŋ/, and /ɚ/ remain. This is why every foreign coda other than a nasal mappable to `-n`/`-ng` must be resolved by epenthesis in the reader tiers.

**Permitted codas:**

| Coda | Type | Examples |
|---|---|---|
| ∅ | open syllable, no coda | 他 `tā`, 是 `shì` |
| /i/ or /u/ | vocalic off-glide — forms a diphthong/triphthong, not a consonant coda | 爱/愛 `ài`, 高 `gāo` |
| /n/ | alveolar nasal, written `-n` | 山 `shān`, 人 `rén` |
| /ŋ/ | velar nasal, written `-ng`; never an onset | 帮/幫 `bāng`, 风/風 `fēng` |
| /ɚ/ | rhotic — the `er` syllable and the érhua suffix `-r` | 儿/兒 `ér`, 花儿/花兒 `huār` |

**Examples:**

| IPA | Pinyin | Zhuyin | Coda | 汉字 (Simp.) | 漢字 (Trad.) | Gloss |
|---|---|---|---|---|---|---|
| /ʂan/ | `shān` | `ㄕㄢ` | /n/ | 山 | 山 | mountain — alveolar nasal coda |
| /fəŋ/ | `fēng` | `ㄈㄥ` | /ŋ/ (`-ng`) | 风 | 風 | wind — velar nasal coda (`e` reduces to /ə/ in `-eng`) |
| /ɚ/ | `èr` | `ㄦ` | rhotic /ɚ/ as a standalone syllable | 二 | 二 | two — the `er` syllable; rhotacized rime with no onset |
| /xwaɚ/ | `huār` | `ㄏㄨㄚㄦ` | érhua `-r` /ɚ/ rhotacizing the rime | 花儿 | 花兒 | flower (érhua) — Pǔtōnghuà 花儿 `huār`; Guóyǔ 花 `huā` without `-r` |

#### Tone (声调 / 聲調 shēngdiào — lexical tone)

The OBLIGATORY suprasegmental component that lexically distinguishes otherwise identical syllables. Every full syllable bears one of four contour tones — T1 阴平/陰平 high-level [˥] (55), T2 阳平/陽平 rising [˧˥] (35), T3 上声/上聲 low-dipping [˨˩˦] (214), T4 去声/去聲 high-falling [˥˩] (51) — and grammatical/affixal syllables may carry the NEUTRAL tone 轻声/輕聲 (short, pitch from context). Tone is contrastive and is treated as a structural slot of the syllable here, because changing only the tone yields a different word. Pinyin marks tone with vowel diacritics (`ā á ǎ à`, neutral unmarked); Zhuyin marks it with tone signs (T1 unmarked, `ˊ` T2, `ˇ` T3, `ˋ` T4, `˙` neutral).

> **IMPORTANT:** this obligatory tone is a feature of the LANGUAGE; the Peshitta reader tiers are toneless by design (the Aramaic source IPA carries no tone), so they drop these marks.

**The five tones:**

| Tone | Chinese name | Contour | Pinyin mark | Zhuyin mark | Example |
|---|---|---|---|---|---|
| T1 | 阴平 / 陰平 | high-level [˥] (55) | `◌̄` | unmarked | `mā` 妈/媽 'mother' |
| T2 | 阳平 / 陽平 | rising [˧˥] (35) | `◌́` | `ˊ` | `má` 麻 'hemp' |
| T3 | 上声 / 上聲 | low-dipping [˨˩˦] (214) | `◌̌` | `ˇ` | `mǎ` 马/馬 'horse' |
| T4 | 去声 / 去聲 | high-falling [˥˩] (51) | `◌̀` | `ˋ` | `mà` 骂/罵 'scold' |
| Neutral | 轻声 / 輕聲 | short, context pitch | unmarked | `˙` | `ma` 吗/嗎 (question particle) |

**Minimal set** — segmental shape /ma/, distinguished only by tone:

| Tone | Pinyin | 汉字 (Simp.) | 漢字 (Trad.) | Gloss |
|---|---|---|---|---|
| T1 | `mā` | 妈 | 媽 | mother |
| T2 | `má` | 麻 | 麻 | hemp |
| T3 | `mǎ` | 马 | 馬 | horse |
| T4 | `mà` | 骂 | 罵 | scold |
| Neutral | `ma` | 吗 | 嗎 | yes-no question particle |

Five syllables, one segmental shape /ma/, distinguished only by tone — the canonical demonstration that tone is a structural component of the Mandarin syllable. **The Peshitta reader tiers would render all of these as toneless `ma`.**

### Phonotactics

Mandarin syllable phonotactics are tight and fully enumerable. There are no consonant clusters in any position; the only intra-syllable consonant pairing is initial + nasal/rhotic coda around a nucleus. Codas are limited to /n/, /ŋ/, /ɚ/. There is at most one medial glide and at most one off-glide. Crucially, initials and finals do not combine freely — there are systematic CO-OCCURRENCE constraints (see below). The result is a small inventory: about 400 distinct toneless syllables, expanding to roughly 1300 once tone is counted.

**Inventory counts:**

| Inventory | Count |
|---|---|
| Toneless syllables | ≈ 400 distinct (C)(G)V(C) segmental shapes |
| Toned syllables | ≈ 1300 distinct tone-bearing syllables (segmental shape × legal tones) |

This is far smaller than the open-ended syllable inventories of cluster-rich languages like English; the closed, enumerable set is what lets a deterministic pinyin ↔ zhuyin ↔ hanzi transducer operate.

**Morpheme ↔ syllable ↔ character isomorphism:** Mandarin is strongly monosyllabic at the morpheme level: there is a near one-to-one correspondence morpheme ↔ syllable ↔ character (字). One hanzi is written per syllable and usually corresponds to one morpheme; polysyllabic words are written as strings of single-syllable characters (e.g. 中国/中國 `zhōng-guó` = 中 + 国/國, two syllables, two characters, two morphemes). This isomorphism is why the hanzi reader tiers can be generated by mapping each transduced syllable to a character.

#### Initial–Final Co-occurrence

Initials and finals are NOT freely combinable; their co-occurrence is governed by the place of the initial and the frontness/roundedness of the medial. The main constraints:

| # | Constraint |
|---|---|
| 1 | `j` /tɕ/, `q` /tɕʰ/, `x` /ɕ/ occur ONLY before a high front vocoid — the `i` /i/ or `ü` /y/ medial/nucleus (`ji`, `qi`, `xi`, `ju`, `qu`, `xu`, `jian`, `xue`, …); they never precede `a`, `o`, `e`, `u` directly. They are in complementary distribution with `z/c/s`, `zh/ch/sh`, and `g/k/h`. |
| 2 | Conversely `z/c/s`, `zh/ch/sh`, `g/k/h` NEVER occur before the `i` /i/ or `ü` /y/ medial (no \*`gi`, \*`ki`, \*`zi`-with-[i], \*`zhü`); where an apical `-i` appears after `z/c/s/zh/ch/sh` it is the buzzed [ɹ̩]/[ɻ̩], not [i]. |
| 3 | `f` /f/ does not take the `i` /j/ or `ü` /ɥ/ medial (no \*`fi`, \*`fü`, \*`fian`); it pairs only with 开口 (`a`, `o`, `u`) finals. |
| 4 | The retroflexes `zh/ch/sh/r` and the dentals `z/c/s` do not take the `ü` /y/ medial (no \*`zhü`, \*`cü`). |
| 5 | The labials `b/p/m` and `f` generally avoid the 合口 `-uo` etc. except in limited rimes; `b/p/m` take `-o` (`bo`, `po`, `mo`) where other initials take `-uo`. |
| 6 | The velar nasal /ŋ/ (`-ng`) is a coda only and never an initial; `r` /ʐ~ɻ/ never appears as a coda. |
| 7 | `ü` /y/ as a free nucleus follows only `j/q/x`, `y`, `n`, `l` (`ju`, `qu`, `xu`, `yu`, `nü`, `lü`); after `j/q/x/y` the umlaut is dropped in spelling (`ju` = /tɕy/). |

### Syllable Types

| Type | Description | IPA example | Pinyin | Zhuyin | 汉字 (Simp.) | 漢字 (Trad.) | Frequency |
|---|---|---|---|---|---|---|---|
| V (+T) | Bare toned nucleus; no initial, medial, or coda (the minimal syllable) | /a/ T1 | `ā` | `ㄚ` | 啊 | 啊 | Occasional (interjections, particles, vowel-initial syllables) |
| CV (+T) | Initial + nucleus + tone — the canonical, statistically dominant Mandarin syllable | /tʰa/ T1 | `tā` | `ㄊㄚ` | 他 | 他 | Most common |
| GV (+T) | Medial glide + nucleus, zero initial — the glide is spelled `y-`/`w-` word-initially | /wo/ T3 | `wǒ` | `ㄨㄛ` | 我 | 我 | Common |
| CGV (+T) | Initial + medial glide + nucleus (open syllable with on-glide) | /kwo/ T2 | `guó` | `ㄍㄨㄛ` | 国 | 國 | Common |
| VC (+T) | Nucleus + coda, zero initial, no medial (nasal- or rhotic-closed) | /an/ T1 | `ān` | `ㄢ` | 安 | 安 | Common |
| CVC (+T) | Initial + nucleus + nasal coda — closed syllable; coda is only /n/ or /ŋ/ | /ʂan/ T1 | `shān` | `ㄕㄢ` | 山 | 山 | Very common |
| CGVC (+T) | Initial + medial glide + nucleus + nasal coda — the maximal (C)(G)V(C) syllable | /ʂwaŋ/ T1 | `shuāng` | `ㄕㄨㄤ` | 双 | 雙 | Common |
| CVV / CGVV (+T) (diphthong / triphthong) | Initial (+ medial) + nucleus + vocalic off-glide — the coda slot is filled by /i/ or /u/, making a diphthong (`ai`, `ei`, `ao`, `ou`) or triphthong (`iao`, `uai`, …) | /kau/ T1 ; /tɕjau/ T1 | `gāo` / `jiāo` | `ㄍㄠ` / `ㄐㄧㄠ` | 高 / 教 | 高 / 教 | Very common |
| ér / -r (+T) (rhotic er / érhua) | The rhotic /ɚ/ as a standalone syllable (`er`) or as the érhua suffix `-r` that restructures a preceding rime (Pǔtōnghuà; rare in Guóyǔ) | /ɚ/ T2 ; /xwaɚ/ T1 | `ér` / `huār` | `ㄦ` / `ㄏㄨㄚㄦ` | 儿 / 花儿 | 兒 / 花兒 | `er` common; érhua frequent in Pǔtōnghuà, rare in Guóyǔ |

### Syllabification

**Principle:** Character/morpheme-aligned syllabification with no cross-syllable resyllabification — each hanzi is exactly one syllable, and because there are no clusters to redistribute, syllable boundaries are essentially fixed and there is no Maximal-Onset tug-of-war.

In a multisyllabic word each syllable is self-contained: its (C)(G)V(C) structure is complete within the character, and a coda nasal/rhotic stays with its own syllable rather than re-attaching as the onset of the next (西安 `Xī'ān` is xi.an, two syllables, NOT \*`xian`). Pinyin uses the apostrophe (隔音符号) to mark a syllable break before a vowel-initial syllable when ambiguity could arise (`Xī'ān` 西安, `pí'ǎo` 皮袄). Zhuyin avoids the problem entirely by writing each syllable as its own glyph block. The only 'parsing' decisions are tone-sandhi adjustments and érhua rime-restructuring, neither of which moves a segment across a syllable boundary.

| Word | Pinyin | Zhuyin | Syllable parse | Note |
|---|---|---|---|---|
| 西安 | `Xī'ān` | `ㄒㄧ ㄢ` | xī \| ān | two syllables xi + an; the apostrophe blocks the wrong reading \*`xian` 先. No resyllabification of the onsetless second syllable. |
| 中国 / 中國 | `Zhōngguó` | `ㄓㄨㄥ ㄍㄨㄛ` | zhōng \| guó | two characters = two syllables = two morphemes; the /ŋ/ coda of zhōng stays put, guó begins fresh |
| 你好 | `nǐ hǎo` | `ㄋㄧˇ ㄏㄠˇ` | nǐ \| hǎo → (sandhi) ní hǎo | T3+T3 sandhi raises the first to T2 (ní hǎo); a connected-speech tone change, not a segmental resyllabification |
| 一点儿 / 一點兒 | `yìdiǎnr` | `ㄧˋ ㄉㄧㄢˇ ㄦ` | yì \| diǎn(r) | Pǔtōnghuà érhua: the `-r` rhotacizes/restructures the diǎn rime within its own syllable; Guóyǔ says yìdiǎn without `-r` |

### Loanword Adaptation

Because Mandarin syllables admit NO consonant clusters and only the codas /n ŋ ɚ/, foreign words with clusters or with non-nasal codas are forced onto legal (C)(G)V(C) syllables by HEAVY VOWEL EPENTHESIS and CODA DELETION/REASSIGNMENT: a vowel is inserted to give each stray consonant its own syllable, illegal codas are dropped or carried into a following epenthetic syllable, and each resulting syllable is assigned a citation tone and written with a chosen character. This is exactly the operation the Pinyin and Zhuyin reader tiers perform when transducing an Aramaic/IPA reading into legal Mandarin syllables — the consonant-final, cluster-bearing Aramaic source is repaired into a string of open or nasal-closed Mandarin syllables.

**Default epenthetic vowel:** /a/, /i/, /u/, /o/, /ɤ/ are all used depending on the source consonant and the target character; `-a` (巴 `bā`, 拉 `lā`), `-i` (西 `xī`, 利 `lì`), `-u` (杜 `dù`), the apical `-i` [ɹ̩]/[ɻ̩] after sibilants, and final nasal `-n`/`-ng` are the common landing rimes.

**Operations:**

| Operation | Description |
|---|---|
| CLUSTER BREAKING | Insert a vowel between adjacent consonants so each gets its own onset (Christ /kr.../ → Jī-dū 基督). |
| CODA RESOLUTION | A final stop/obstruent is either dropped or given an epenthetic vowel as a new syllable's nucleus; a final nasal may map to `-n`/`-ng` (e.g. `-m` → `-n`). |
| TONE & CHARACTER ASSIGNMENT | Each legal syllable receives a citation tone and is written with a transcription character chosen for sound (and sometimes auspicious meaning). |

**Examples:**

| Source | IPA source | Pinyin | Zhuyin | 汉字 (Simp.) | 漢字 (Trad.) | Syll. | Note |
|---|---|---|---|---|---|---|---|
| Greek/Aramaic 'Christ' (Χριστός / ܡܫܝܚܐ via the title) | /krɪst/ (Western form) | `Jīdū` | `ㄐㄧ ㄉㄨ` | 基督 | 基督 | 2 | ji-du: the /kr/ cluster and the /st/ coda are dissolved into two clean open CV syllables 基 `jī` + 督 `dū`; all codas deleted, two characters/morphemes |
| Aramaic/Greek 'Barabbas' (ܒܪ ܐܒܐ / Βαραββᾶς) | /baˈrabbas/ | `Bālābā` | `ㄅㄚ ㄌㄚ ㄅㄚ` | 巴拉巴 | 巴拉巴 | 3 | ba-la-ba: each consonant is given its own `-a` syllable, the geminate and final `-s` are dropped; three open CV syllables 巴 + 拉 + 巴 |
| English/Aramaic 'Christ' as a place-marker example with a coda | — | — | — | — | — | 0 | General principle: no Mandarin syllable can host /str/, /kl/, final /t/, /s/, /m/, etc.; every such piece becomes its own legal (C)(G)V(C) syllable — the same forced epenthesis the Peshitta Pinyin/Zhuyin tiers apply to Aramaic. |
| English 'Mark' (the Evangelist 马可/馬可) | /mɑːrk/ | `Mǎkě` | `ㄇㄚˇ ㄎㄜˇ` | 马可 | 馬可 | 2 | ma-ke: the rhotic and final /k/ are resolved by an epenthetic `-e` syllable; 马/馬 `mǎ` + 可 `kě`, two characters |

### Constraints

- The syllable is the central phonological unit and is maximally (C)(G)V(C) + TONE: an optional initial consonant (声母), an optional medial glide (介音 `i`/`u`/`ü` = /j w ɥ/), an obligatory nucleus (韵腹), an optional coda (韵尾), and an obligatory lexical tone. The nucleus and tone are the only mandatory components.
- There are NO consonant clusters anywhere — no onset clusters and no coda clusters. The only intra-syllable consonant pairing is an initial together with a single nasal/rhotic coda around the nucleus (CVN, CVNG). Foreign clusters are repaired by vowel epenthesis.
- Codas are restricted to /n/ (`-n`), /ŋ/ (`-ng`), and the rhotic /ɚ/ (`er` / 儿化 érhua), plus the vocalic off-glides /i u/ of diphthongs/triphthongs. There are NO obstruent codas (Middle Chinese `-p -t -k` are gone) and NO final /m/ (merged to `-n`). /ŋ/ is a coda only and is never an initial; `r` /ʐ~ɻ/ is an initial only and is never a coda.
- The toneless inventory is small and fully enumerable — about 400 distinct (C)(G)V(C) shapes — expanding to roughly 1300 distinct syllables once the four tones plus neutral tone are counted. This closed inventory is what makes a deterministic pinyin/zhuyin/hanzi transducer feasible.
- Mandarin is strongly monosyllabic at the morpheme level: there is a near one-to-one correspondence morpheme ↔ syllable ↔ character (字). One hanzi is written per syllable; this isomorphism lets the hanzi reader tiers be generated character-by-character from the transduced syllables.
- Initials and finals do NOT co-occur freely. `j` /tɕ/ `q` /tɕʰ/ `x` /ɕ/ appear ONLY before the high front `i` /i/ or `ü` /y/ and are in complementary distribution with `z/c/s`, `zh/ch/sh`, `g/k/h`; conversely `z/c/s/zh/ch/sh/g/k/h` never precede `i`/`ü`. `f` does not take an `i`/`ü` medial. `ü` as a nucleus follows only `j/q/x/y/n/l`. These co-occurrence rules constrain the legal syllable set.
- TONE is an obligatory, contrastive component of the full syllable: T1 [˥] (55), T2 [˧˥] (35), T3 [˨˩˦] (214), T4 [˥˩] (51), plus the neutral tone 轻声/輕聲. Minimal sets like `mā`/`má`/`mǎ`/`mà` 妈麻马骂 (媽麻馬罵) prove tone is structural, not decorative. Tone sandhi (T3+T3→T2+T3; 一 `yī` and 不 `bù` sandhi) and the neutral tone are connected-speech adjustments that do not alter the segmental syllable skeleton.
- The two APICAL ('buzzed') vowels [ɹ̩] (after `z/c/s`) and [ɻ̩] (after `zh/ch/sh/r`), both spelled `-i`, are the only syllabic vocoids of their kind and exist solely to give the sibilant initials a citation rime; they are NOT [i] and never combine with other initials.
- Syllabification is character-aligned with no cross-boundary resyllabification: each syllable is self-contained (西安 = xi.an, not xian), pinyin uses the apostrophe 隔音符号 to mark vowel-initial syllable breaks, and zhuyin writes each syllable as its own glyph block. There is no Maximal-Onset competition because there are no clusters to reassign.
- The two reference standards share this syllable skeleton; they differ only in surface realization — Guóyǔ has little or no érhua and frequent de-retroflexion (`zh/ch/sh/r` → `z/c/s/-`), fewer neutral tones, and some lexical tone/segment differences (垃圾 `lājī`/`lèsè`; 和 `hé`/`hàn`) — none of which change the toneless pinyin spine the reader tiers are built on.
- Loanwords and any non-Mandarin input (including Aramaic) are forced onto legal syllables by HEAVY VOWEL EPENTHESIS plus coda deletion/reassignment, then assigned a tone and a transcription character: 基督 `Jīdū` 'Christ', 巴拉巴 `Bālābā` 'Barabbas', 马可/馬可 `Mǎkě` 'Mark'. This is the exact mechanism the Peshitta Pinyin and Zhuyin reader tiers use to host Aramaic, and what the downstream Hanzi (Simplified/Traditional) tier looks up — the Hanzi tier unavoidably imposes a citation tone per character (an artifact, since the Aramaic source carries none).

> **Cross-reference:** This section underpins the TONELESS PINYIN and ZHUYIN/BOPOMOFO reader tiers, and through them the SIMPLIFIED and TRADITIONAL HANZI transcription tiers, among the six Chinese Peshitta reader tiers (Scholarly, Pretty, Toneless Pinyin, Zhuyin/Bopomofo, Hanzi-Simplified, Hanzi-Traditional). The (C)(G)V(C) template, the no-cluster phonotactics, the /n ŋ ɚ/-only codas, the ~400/~1300 enumerable inventory, the initial × final co-occurrence rules, and the forced-vowel-epenthesis behavior specified here drive the transducer that maps a phonemic Aramaic reading into legal Mandarin syllables and composes them into pinyin, then transcodes to zhuyin and looks up characters. The reader tiers are TONELESS because the Peshitta source IPA carries no tone (tones are documented for the LANGUAGE in the suprasegmentals/tones section but stripped in the tiers); the Hanzi tiers nonetheless impose a per-character citation tone as an unavoidable artifact. See the companion files `Chinese/chinese_pronunciation_guide.md` and the tiers under `Chinese/Peshita_Chinese/Pinyin/`, `Chinese/Peshita_Chinese/Zhuyin/`, `Chinese/Peshita_Chinese/Hanzi_Simplified/` and `Chinese/Peshita_Chinese/Hanzi_Traditional/`. Initial/final segmental and allophonic detail lives in the consonants/finals sections; tone melodies and sandhi in the suprasegmentals/tones section of this guide.

---

*Section prepared by Shin.*

## Phonological Rules & Tone Sandhi

Active connected-speech, tonal, and allophonic processes of Standard Mandarin (标准汉语 / 標準漢語 `Biāozhǔn Hànyǔ`), documented in parallel for the two reference standards: 普通话 / 普通話 `Pǔtōnghuà` (PRC Standard Mandarin, Beijing-based phonology, Simplified characters, Hanyu Pinyin) and 國語 `Guóyǔ` (Taiwan Standard Mandarin, Traditional characters, Zhuyin/Bopomofo). Mandarin's signature processes are **TONAL** — they manipulate the four lexical tones plus the neutral tone in connected speech (变调 / 變調 `biàndiào`, tone sandhi) — alongside a small set of segmental/allophonic rules: the strictly complementary distribution of the `j/q/x`, `z/c/s`, and `zh/ch/sh` series; retroflex realization and Taiwan de-retroflexion; 儿化 / 兒化 `érhuà` rime restructuring; 轻声 / 輕聲 `qīngshēng` neutral-tone reduction; and the orthographic `ü→u` rule after `j/q/x/y`. Because Mandarin syllables are **(C)(G)V(C)+TONE** with codas limited to /n ŋ ɚ/ and **NO consonant clusters**, there is essentially no consonantal liaison across word boundaries of the English/French type — the most important cross-syllable phenomena are tonal, not segmental.

The phonemic system is **SHARED** by both standards; Pǔtōnghuà/Guóyǔ divergences are surface or lexical (erhua frequency, de-retroflexion, neutral-tone frequency, a handful of citation tones) and **DO NOT** change the toneless pinyin spelling that anchors the Peshitta reader tiers. Each rule below lists its name (汉字 + pinyin + English), category, description, environment, an example with Simplified + Traditional Hanzi and pinyin showing the change plus IPA, and notes. IPA uses **/slashes/** for underlying phonemic forms and **[brackets]** for surface forms; tones are given as Chao tone-letters (˥ ˧˥ ˨˩˦ ˥˩) and/or pitch numerals (55, 35, 214, 51). Standard scope is marked `both`, `Pǔtōnghuà`, or `Guóyǔ`; where a process applies in both but differs, the divergence is noted.

> **Note on the Peshitta reader tiers:** The LANGUAGE is fully tonal and all of the tone-sandhi rules below render tones in full. The Peshitta **reader tiers are toneless by design** — they carry no tone to manipulate — so the tonal rules document the language but never touch those tiers. Tone sandhi is a **PRONUNCIATION** rule, not an orthographic one: pinyin keeps the underlying tone marks (你好 stays spelled `nǐ hǎo`), and the toneless tier that anchors the Peshitta reader is therefore stable across all of these rules.

### Rules at a Glance

| # | Rule | Category | Process | Standards |
|---|---|---|---|---|
| 1 | 三声变调 / 三聲變調 `sānshēng biàndiào` — third-tone sandhi | tone sandhi / connected speech | `T3 + T3 → T2 + T3` (214 → 35 before 214) | both |
| 2 | 半三声 / 半三聲 `bàn sānshēng` — half-third tone | tone sandhi / allophony | `T3 → [21]` before non-T3 (low, no final rise) | both |
| 3 | 一字变调 / 一字變調 `yī-zì biàndiào` — sandhi of 一 `yī` | tone sandhi / lexical morpheme | `yī → yì (T4)` bef. T1/T2/T3; `→ yí (T2)` bef. T4 | both |
| 4 | 不字变调 / 不字變調 `bù-zì biàndiào` — sandhi of 不 `bù` | tone sandhi / lexical morpheme | `bù (T4) → bú (T2)` before T4 | both |
| 5 | 轻声 / 輕聲 `qīngshēng` — neutral-tone reduction | prosody / tonal reduction | lexical tone → short, light, pitch set by preceding tone | both |
| 6 | 儿化 / 兒化 `érhuà` — rhotacization / rime restructuring | morphophonology / suffixal rhotacization | `-r` suffix rhotacizes & restructures the rime | both |
| 7 | 尖团音的互补分布 / 尖團音的互補分佈 `jiān-tuán yīn hùbǔ fēnbù` — `j/q/x ~ z/c/s ~ zh/ch/sh` distribution | phonotactics / complementary distribution | `j/q/x` only before /i y/; others never there | both |
| 8 | 卷舌音的实现 / 卷舌音的實現 `juǎnshé yīn de shíxiàn` — retroflex realization | allophony / place of articulation | `zh/ch/sh/r` = retroflex; written `-i` = [ʐ̩~ɻ̩] | both |
| 9 | 去卷舌化 `qù-juǎnshé huà` — Taiwan de-retroflexion | allophony / standard divergence | `zh/ch/sh/r → z/c/s/-` (merge toward dentals) | Guóyǔ |
| 10 | `ü→u` 拼写规则 / 拼寫規則 `ü→u pīnxiě guīzé` — `ü`-to-`u` spelling | orthography / pinyin spelling rule | /y/ written `u` after `j/q/x/y`; `ü` after `n/l` | both |
| 11 | 音节缩合 / 音節縮合 `yīnjié suōhé` — syllable contraction | connected speech / fast-speech reduction | disyllabic sequence → one fused syllable (合音) | both |
| 12 | 无连音 / 無連音 `wú liányīn` — absence of liaison | phonotactics / connected speech (negative rule) | syllable seam preserved; **no** resyllabification | both |
| 13 | 鼻音韵尾的同化 / 鼻音韻尾的同化 `bíyīn yùnwěi de tónghuà` — coda-nasal place assimilation | allophony / assimilation (casual) | coda /n/ → [m]/[ŋ] before homorganic stop (gradient) | both |
| 14 | 规则排序 / 規則排序 `guīzé páixù` — rule ordering | meta / rule interaction & ordering | order: lexical tone → 一/不 → T3 sandhi → 儿化 → casual | both |

---

### Rule 1: 三声变调 / 三聲變調 (`sānshēng biàndiào`) — third-tone sandhi (T3 + T3 → T2 + T3)

*Category: tone sandhi / connected speech — Standards: `both`*

The most pervasive tone-sandhi rule of Mandarin. A full third tone (上声 / 上聲, low-dipping 214 ˨˩˦) is realized with its full dipping-then-rising contour only in isolation or utterance-finally. When two third tones are adjacent, the **FIRST** T3 changes to a rising tone identical to the second tone (35 ˧˥), so the sequence surfaces as **T2 + T3**: 你好 `nǐ hǎo` → `ní hǎo`, 很好 `hěn hǎo` → `hén hǎo`, 老板 / 老闆 `lǎobǎn` → `láobǎn`. In longer strings of T3 syllables the rule applies **iteratively**, conditioned by prosodic/foot grouping (e.g. 我也很好 `wǒ yě hěn hǎo` → `wǒ yé hén hǎo`, with the rightmost T3 retained). The sandhi T2 is phonetically very close to, but historically distinct from, a lexical T2.

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 你好 / 你好 |
| Pinyin (underlying) | `nǐ hǎo` |
| Pinyin (surface) | `ní hǎo` |
| IPA | `/ni²¹⁴ xau²¹⁴/` → `[ni³⁵ xau²¹⁴]` (`[ni˧˥ xau˨˩˦]`) |

**Environment:** A third-tone syllable immediately followed by another third-tone syllable, within or across words; applies iteratively in T3 strings, scoped by prosodic phrasing.

**Notes:** Pinyin orthography is **NOT** rewritten for sandhi — 你好 stays spelled `nǐ hǎo`; the change is a pronunciation rule the reader applies. The output T2 is the **SANDHI** third tone, not a lexical second tone. Because the Peshitta reader tiers are toneless, this rule never affects them; it is documented for the LANGUAGE. Both standards share the rule, though Guóyǔ has somewhat fewer obligatory T3 contexts overall.

---

### Rule 2: 半三声 / 半三聲 (`bàn sānshēng`) — half-third tone (low non-rising allophone)

*Category: tone sandhi / allophony — Standards: `both`*

A non-final third tone that is followed by a tone **OTHER** than another T3 (i.e. before T1, T2, T4, or a neutral tone) does not realize its full dipping-rising 214 contour. Instead it is truncated to a low, level-to-slightly-falling **'half-third'** [21]/[211] (˨˩) — the dip without the final rise. Thus the T3 in 好人 `hǎorén` (T3+T2), 老师 / 老師 `lǎoshī` (T3+T1), 努力 `nǔlì` (T3+T4), and 喜欢 / 喜歡 `xǐhuan` (T3+neutral) is a low half-third, not a full 214. The full 214 surfaces only utterance-finally or in isolation/citation.

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 老师 / 老師 |
| Pinyin (underlying) | `lǎoshī` |
| Pinyin (surface) | `lǎoshī` (T3 → half-third [21]) |
| IPA | `/lau²¹⁴ ʂɻ̩⁵⁵/` → `[lau²¹ ʂɻ̩⁵⁵]` (`[lau˨˩ ʂɻ̩˥]`) |

**Environment:** Third-tone syllable in non-final position before a non-T3 tone (T1/T2/T4/neutral); blocked when the following syllable is also T3 (then full third-tone sandhi to T2 applies instead).

**Notes:** Half-third and the T3→T2 sandhi are **complementary**: before T3, T3 becomes rising 35; before any other tone (or pause-internally) it becomes low 21. Both are part of the same 上声 / 上聲 surface allophony. Rule-ordering: evaluate whether the following tone is T3 first (→ T2 sandhi); otherwise apply half-third. Shared by both standards.

---

### Rule 3: 一字变调 / 一字變調 (`yī-zì biàndiào`) — tone sandhi of 一 `yī` ('one')

*Category: tone sandhi / lexical morpheme — Standards: `both`*

The numeral 一 has the citation/isolation tone `yī` (T1, 55) — used when counting, reading digits, or word-finally (e.g. 第一 `dìyī`, 万一 / 萬一 `wànyī`). In running combination it changes tone by the tone of the **FOLLOWING** syllable: before T1, T2, or T3 it becomes T4 `yì` (51); before a T4 it dissimilates to T2 `yí` (35). Thus 一天 `yìtiān` (before T1), 一年 `yìnián` (before T2), 一起 `yìqǐ` (before T3), but 一定 `yídìng` and 一样 / 一樣 `yíyàng` (before T4). When 一 is sandwiched as a reduplication infix it goes **neutral** (看一看 `kàn yi kàn`).

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 一定 / 一起 (both identical in S & T) |
| Pinyin (underlying) | `yī dìng` / `yī qǐ` |
| Pinyin (surface) | `yídìng` (yī→yí before T4) / `yìqǐ` (yī→yì before T3) |
| IPA — 一定 | `/i⁵⁵ tiŋ⁵¹/` → `[i³⁵ tiŋ⁵¹]` (`[i˧˥ tiŋ˥˩]`) |
| IPA — 一起 | `/i⁵⁵ tɕʰi²¹⁴/` → `[i⁵¹ tɕʰi²¹⁴]` (`[i˥˩ tɕʰi˨˩˦]`) |

**Environment:** The morpheme 一 immediately before another tone-bearing syllable; → `yì` (T4) before T1/T2/T3, → `yí` (T2) before T4; citation `yī` (T1) when final or read as a digit; neutral in 'V-一-V' frames.

**Notes:** Unlike third-tone sandhi, the 一/不 changes **ARE** conventionally reflected in many pinyin teaching materials (`yídìng`, `yìtiān`), but the canonical dictionary/toneless spelling remains `yi`, so the Peshitta toneless tier is unaffected. Shared by both standards.

---

### Rule 4: 不字变调 / 不字變調 (`bù-zì biàndiào`) — tone sandhi of 不 `bù` ('not')

*Category: tone sandhi / lexical morpheme — Standards: `both`*

The negator 不 has citation tone `bù` (T4, 51) before T1, T2, T3, and in isolation: 不高 `bù gāo`, 不来 / 不來 `bù lái`, 不好 `bù hǎo`. Before another T4 it dissimilates to `bú` (T2, 35): 不是 `búshì`, 不对 / 不對 `búduì`, 不要 `búyào`. In potential/reduplicative 'A-不-A' frames it reduces to a **neutral** tone (是不是 `shì bu shì`, 好不好 `hǎo bu hǎo`).

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 不是 / 不是 |
| Pinyin (underlying) | `bù shì` |
| Pinyin (surface) | `búshì` (bù→bú before T4) |
| IPA | `/pu⁵¹ ʂɻ̩⁵¹/` → `[pu³⁵ ʂɻ̩⁵¹]` (`[pu˧˥ ʂɻ̩˥˩]`) |

**Environment:** The morpheme 不 immediately before a tone-bearing syllable: stays T4 before T1/T2/T3; → `bú` (T2) before T4; neutral inside 'A-不-A' frames.

**Notes:** Parallel to 一 but simpler: 不 only ever lowers its T4 to T2, and only before another T4. Ordering: 一/不 sandhi and third-tone sandhi can co-occur in a phrase and are evaluated on their own triggering segments. Shared by both standards.

---

### Rule 5: 轻声 / 輕聲 (`qīngshēng`) — neutral-tone reduction

*Category: prosody / tonal reduction — Standards: `both`*

Certain syllables lose their lexical tone and are pronounced **SHORT, light, and unstressed**, with a pitch determined by the **PRECEDING** tone. The pitch targets are:

| Preceding tone | Neutral-tone pitch target |
|---|---|
| after T1 (55) | low-falling (˨ ~2) |
| after T2 (35) | mid (˧ ~3) |
| after T3 (214) | half-high (˦ ~4, the rising-context allophone) |
| after T4 (51) | low (˩ ~1) |

The neutral tone occurs on: grammatical particles (的 `de`, 了 `le`, 吗 / 嗎 `ma`, 呢 `ne`, 着 / 著 `zhe`, 过 / 過 `guo`); the second half of many reduplications (妈妈 / 媽媽 `māma`, 看看 `kànkan`); some suffixes (子 `zi`, 头 / 頭 `tou`, 们 / 們 `men`); and many disyllabic words' second syllable (东西 / 東西 `dōngxi` 'thing', 朋友 `péngyou`, 喜欢 / 喜歡 `xǐhuan`). The vowel also tends to centralize/reduce.

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 妈妈 / 媽媽   ·   东西 / 東西 |
| Pinyin (underlying) | `māmā` / `dōngxī` |
| Pinyin (surface) | `māma` / `dōngxi` (2nd syllable neutral) |
| IPA — 妈妈 / 媽媽 | `/ma⁵⁵ ma⁵⁵/` → `[ma⁵⁵ ma²]` (`[ma˥ ma˨]`) |
| IPA — 东西 / 東西 | `/tuŋ⁵⁵ ɕi⁵⁵/` → `[tuŋ⁵⁵ ɕi²]` (vs. 东西 / 東西 `dōngxī` 'east-west' with full T1) |

**Environment:** Particles, certain suffixes (子/头/们 · 子/頭/們), reduplicated second elements, and lexically specified second syllables; pitch target assigned by the preceding syllable's tone.

**Notes:** Pǔtōnghuà has **MORE** obligatory neutral tones than Guóyǔ; Taiwan Guóyǔ frequently retains a full citation tone where the mainland uses 轻声 / 輕聲 (e.g. 东西 / 東西 often `[ɕi⁵⁵]` in Taiwan; 蝴蝶 `húdié` keeps T2 vs. mainland 蝴蝶 `húdie`). Some pairs are disambiguated only by neutral vs. full tone (东西 / 東西 `dōngxi` 'thing' vs. `dōngxī` 'east-west'). Pinyin marks a neutral syllable by writing it **WITHOUT** a tone mark.

---

### Rule 6: 儿化 / 兒化 (`érhuà`) — rhotacization / erhua rime restructuring

*Category: morphophonology / suffixal rhotacization — Standards: `both`*

The diminutive/colloquial suffix 儿 / 兒 (`-r`) does **not** add a syllable; it **RHOTACIZES** the preceding final, adding a retroflex [ɚ]/[ɻ] coloring and **RESTRUCTURING** the rime. Effects depend on the original coda:

| Original rime/coda | Erhua effect | Example |
|---|---|---|
| open final | simply add [ɚ] | 花 `huā` → 花儿 / 花兒 `huār` [xwaɚ̯] |
| front coda /-i/ or /-n/ | coda **DELETED**, replaced by rhotacization | 一点 / 一點 `yìdiǎn` → 一点儿 / 一點兒 `yìdiǎnr` [tjɑɚ̯]; 玩 `wán` → 玩儿 / 玩兒 `wánr` |
| velar nasal /-ŋ/ | coda deleted, vowel **NASALIZED** + rhotacized | 空 `kòng` → 空儿 / 空兒 `kòngr` [kʰʊ̃ɚ̯] |
| apical vowels and /i y/ | insert a transitional [ɚ] | 字 `zì` → 字儿 / 字兒 `zìr` [tsɚ] |

Erhua can also be lexically/grammatically meaningful (头 / 頭 `tóu` 'head' vs. 头儿 / 頭兒 `tóur` 'boss/leader'; 画 / 畫 `huà` 'to paint' vs. 画儿 / 畫兒 `huàr` 'a painting').

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 一点儿 / 一點兒   ·   花儿 / 花兒 |
| Pinyin (underlying) | `yìdiǎn` + `r` / `huā` + `r` |
| Pinyin (surface) | `yìdiǎnr` (coda `-n` deleted) / `huār` (open rime + [ɚ]) |
| IPA — 一点儿 / 一點兒 | `/i tjɛn²¹⁴/`+r → `[i tjɑɚ̯²¹⁴]` |
| IPA — 花儿 / 花兒 | `/xwa⁵⁵/`+r → `[xwaɚ̯⁵⁵]` (`[xwaɚ̯˥]`) |

**Environment:** Final-position 儿 / 兒 suffix attaching to the preceding syllable's rime; coda /-i -n/ deleted, /-ŋ/ deleted with nasalization, open rimes gain [ɚ].

**Notes:** **MAJOR** Pǔtōnghuà/Guóyǔ divergence: erhua is characteristic of Beijing-based Pǔtōnghuà and abundant in the mainland standard; Taiwan Guóyǔ uses **very LITTLE** erhua, generally preferring the non-rhotacized form or a different word (一点儿 / 一點兒 `yìdiǎnr` → 一點 `yìdiǎn`; 哪儿 / 哪兒 `nǎr` → 哪裡 `nǎlǐ`). The pinyin tier writes the suffix simply as `r` appended to the toneless final, so the restructuring is a pronunciation rule, not an orthographic one. Erhua interacts with neutral tone (the `-r` suffix is itself toneless).

---

### Rule 7: 尖团音的互补分布 / 尖團音的互補分佈 (`jiān-tuán yīn hùbǔ fēnbù`) — complementary distribution of `j/q/x` ~ `z/c/s` ~ `zh/ch/sh`

*Category: phonotactics / complementary distribution — Standards: `both`*

The alveolo-palatal series `j` /tɕ/, `q` /tɕʰ/, `x` /ɕ/ occurs **ONLY** before the high front vocoids `i` /i/ and `ü` /y/ (and their glides /j ɥ/). In exactly those environments the dental series `z/c/s`, the retroflex series `zh/ch/sh`, and the velars `g/k/h` do **NOT** occur. Conversely, `j/q/x` never occur before /a o e u/ or before the apical vowels. The three series are therefore in near-complementary distribution and were historically a merger of two older series (the 尖音 / 尖音 'sharp' dentals + the 团音 / 團音 'round' velars) into one palatal set. This is why pinyin can spell `ji/qi/xi` and `ju/qu/xu` unambiguously: only the palatal reading is possible there.

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 鸡 / 雞   ·   西 / 西   ·   居 / 居 |
| Pinyin (underlying) | `jī` / `xī` / `jū` |
| Pinyin (surface) | `jī` [tɕi], `xī` [ɕi], `jū` [tɕy] — never `*zi`/`*zhi`/`*gi` here |
| IPA — 鸡 / 雞 | `jī` `/tɕi⁵⁵/` [tɕi˥] |
| IPA — 西 | `xī` `/ɕi⁵⁵/` [ɕi˥] |
| IPA — 居 | `jū` `/tɕy⁵⁵/` [tɕy˥] |

**Environment:** `j/q/x` → only before /i y/ (high front); `z/c/s`, `zh/ch/sh`, `g/k/h` → before all other nuclei but never before the /i y/ glide+vowel of the palatal type; the gap is filled exclusively by `j/q/x`.

**Notes:** Because of this gap, the `ü` after `j/q/x` is unambiguous and is written `u` (see the `ü→u` rule). The merger erased the historic 尖/团 (尖/團) distinction in standard Mandarin (some opera registers and dialects keep 尖音 `zi/ci/si` before /i/). Shared by both standards; both Pǔtōnghuà and Guóyǔ have the merged palatal series.

---

### Rule 8: 卷舌音的实现 / 卷舌音的實現 (`juǎnshé yīn de shíxiàn`) — retroflex realization of `zh/ch/sh/r`

*Category: allophony / place of articulation — Standards: `both`*

The retroflex series `zh` /ʈʂ/, `ch` /ʈʂʰ/, `sh` /ʂ/, `r` /ʐ~ɻ/ is articulated with the tongue tip curled up toward the post-alveolar/pre-palatal region. After these initials, the high front vowel slot is filled by the **APICAL/retroflex** vowel written `-i` and realized [ʐ̩]/[ɻ̩] (`zhi` [ʈʂɻ̩], `chi`, `shi`, `ri`), **NOT** [i]. The initial `r` is a voiced retroflex that ranges between a fricative [ʐ] and an approximant [ɻ] depending on speaker and position (日 `rì`, 人 `rén`). Parallel to this, the dental sibilants `z/c/s` take the apical vowel [ɹ̩] before written `-i` (`zi` [tsɹ̩], `ci`, `si`).

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 是 / 是   ·   人 / 人 |
| Pinyin (underlying) | `shì` / `rén` |
| Pinyin (surface) | `shì` [ʂɻ̩], `rén` [ʐən]~[ɻən] |
| IPA — 是 | `shì` `/ʂɻ̩⁵¹/` [ʂɻ̩˥˩] |
| IPA — 人 | `rén` `/ʐən³⁵/` [ʐən˧˥]~[ɻən˧˥] |

**Environment:** `zh/ch/sh/r` as syllable initials; the following written `-i` is the retroflex apical vowel [ʐ̩~ɻ̩]; `r` ranges [ʐ]~[ɻ].

**Notes:** The apical vowels are why pinyin `-i` has **THREE** values: [i] after `j/q/x` and most initials, [ɹ̩] after `z/c/s`, [ʐ̩~ɻ̩] after `zh/ch/sh/r`. This rule defines the canonical Pǔtōnghuà target; Taiwan Guóyǔ frequently de-retroflexes (next rule). Shared as the underlying system; surface realization differs by standard.

---

### Rule 9: 去卷舌化 (`qù-juǎnshé huà`) — Taiwan de-retroflexion (`zh/ch/sh/r → z/c/s/-`)

*Category: allophony / standard divergence — Standards: `Guóyǔ`*

In Taiwan Guóyǔ (and much southern Mainland speech), the retroflex series merges toward the dental series: `zh` /ʈʂ/ → [ts], `ch` /ʈʂʰ/ → [tsʰ], `sh` /ʂ/ → [s], and initial `r` /ʐ/ weakens toward [z] or a glide/zero. Thus 是 `shì` is commonly [sɹ̩] rather than [ʂɻ̩], 知道 `zhīdào` → [tsɹ̩ tau], 日本 `Rìběn` → [zɹ̩ pən]~[ɻ̩…]. This is a **SURFACE** realization difference: the underlying category and the toneless pinyin spelling (`zh/ch/sh/r`) are unchanged, and careful/formal Guóyǔ can restore the retroflexes.

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 知道 / 知道 |
| Pinyin (underlying) | `zhīdào` |
| Pinyin (surface) | Pǔtōnghuà [ʈʂɻ̩ tau] vs. Guóyǔ [tsɹ̩ tau] (de-retroflexed) |
| IPA | `/ʈʂɻ̩⁵⁵ tau⁵¹/` → Pǔtōnghuà [ʈʂɻ̩˥ tau˥˩]; Guóyǔ [tsɹ̩˥ tau˥˩] |

**Environment:** Retroflex initials `zh/ch/sh/r` in casual Taiwan Guóyǔ and many southern accents; gradient and style-sensitive (more retroflex in careful speech).

**Notes:** **PRINCIPAL** Pǔtōnghuà/Guóyǔ segmental divergence (alongside erhua and neutral-tone frequency). Because de-retroflexion is non-contrastive at the level of the standard (it merges, not splits), it does not alter the pinyin spelling or the Peshitta toneless tier. Pǔtōnghuà prescribes the full retroflex; Guóyǔ tolerates/prefers the dental merger.

---

### Rule 10: `ü→u` 拼写规则 / 拼寫規則 (`ü→u pīnxiě guīzé`) — `ü`-to-`u` spelling after `j/q/x/y`

*Category: orthography / pinyin spelling rule — Standards: `both`*

An **ORTHOGRAPHIC** (not phonetic) rule of Hanyu Pinyin. The rounded high front vowel `ü` /y/ is written with the umlaut as `ü` only after `n` and `l`, where it **CONTRASTS** with plain `u` (努 `nǔ` /nu/ vs. 女 `nǚ` /ny/; 路 `lù` /lu/ vs. 绿 / 綠 `lǜ` /ly/). After `j`, `q`, `x` — which can only take the front vowel (by the complementary-distribution rule) — and after the zero-initial spelling `y`, the umlaut is redundant and is **DROPPED**: 居 is written `ju` not `jü`, 区 / 區 `qu`, 须 / 須 `xu`, 鱼 / 魚 `yu`, 元 `yuan`, 云 / 雲 `yun`. The vowel is still /y/, pronounced [y], despite the bare `u` spelling.

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 鱼 / 魚   ·   女 / 女 |
| Pinyin (underlying) | /y/ rime |
| Pinyin (surface) | 鱼 / 魚 `yú` (spelled `u`, = /y/) vs. 女 `nǚ` (umlaut kept, = /y/), cf. 努 `nǔ` = /u/ |
| IPA — 鱼 / 魚 | `yú` `/y³⁵/` [y˧˥] |
| IPA — 女 | `nǚ` `/ny²¹⁴/` [ny˨˩˦] |
| IPA — 努 | `nǔ` `/nu²¹⁴/` [nu˨˩˦] |

**Environment:** Underlying /y/ (`ü`) after `j/q/x/y` → spelled `u` (no umlaut); after `n/l` → spelled `ü` (umlaut retained for contrast); after the zero initial → `yu-`.

**Notes:** Purely a spelling convention — the phoneme /y/ is unchanged; only `n/l` need the umlaut because there the `u`/`ü` contrast is live. Zhuyin sidesteps the issue entirely (ㄩ is the dedicated /y/ letter: 鱼 / 魚 `ㄩˊ`, 女 `ㄋㄩˇ`). Shared by both standards (Pinyin convention; Guóyǔ pedagogy uses Zhuyin but the same phonemic facts hold).

---

### Rule 11: 音节缩合 / 音節縮合 (`yīnjié suōhé`) — syllable contraction in fast speech

*Category: connected speech / fast-speech reduction — Standards: `both`*

In rapid casual speech, frequent disyllabic sequences may **CONTRACT** into a single syllable (合音 `héyīn`), blending segments and tones. Classic cases: 不用 `bùyòng` → 甭 `béng` [pəŋ]; 这一 / 這一 `zhè yī` → 这 / 這 `zhèi`; 那一 `nà yī` → `nèi`; 不知道 `bù zhīdào` → [pʈʂ̩…] with the middle syllable elided; 知道 `zhīdào` often [tsau]/[ʈʂau] with apical loss; 怎么 / 怎麼 `zěnme` → [tsəm]; 豆腐 `dòufu` and similar collapse vowels. Tones merge to a composite contour. This is gradient and rate-dependent, suppressed in careful speech.

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 不用 → 甭 / 不用 → 甭 |
| Pinyin (underlying) | `bùyòng` |
| Pinyin (surface) | `béng` (lexicalized contraction) |
| IPA | 不用 `/pu⁵¹ jʊŋ⁵¹/` → 甭 [pəŋ³⁵] (`[pəŋ˧˥]`) |

**Environment:** High-frequency disyllabic collocations in fast/casual speech; an unstressed (often neutral-tone) syllable is reduced or fused into its neighbor.

**Notes:** Some contractions are fully **LEXICALIZED** with their own character (甭 `béng`; 别 / 別 = 不要 lexicalized in some analyses) while most are purely phonetic fast-speech variants. Common to both standards as a casual-register phenomenon; the careful citation forms are identical. Does not affect the toneless pinyin/Peshitta tier (the underlying spelling is the full form).

---

### Rule 12: 无连音 / 無連音 (`wú liányīn`) — absence of consonantal liaison

*Category: phonotactics / connected speech (negative rule) — Standards: `both`*

Unlike English (linking-R, resyllabification) or French (liaison/enchaînement), Mandarin has essentially **NO** consonantal liaison across syllable/word boundaries. Syllable boundaries are robustly maintained because (a) codas are limited to /n ŋ ɚ/ and never re-link as the onset of a following vowel-initial syllable, and (b) there are no consonant clusters to simplify across the seam. A coda /n/ or /ŋ/ stays in its own syllable rather than becoming the onset of the next; where ambiguity could arise, the **apostrophe** is used in pinyin (西安 `Xī'ān`, not `*Xian`; 皮袄 / 皮襖 `pí'ǎo`). The dominant cross-boundary phenomena are **TONAL** (sandhi) and prosodic, not segmental linking.

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 西安 / 西安 |
| Pinyin (underlying) | `xī` + `ān` |
| Pinyin (surface) | `Xī'ān` (apostrophe marks the seam — **NOT** `*Xiān`) |
| IPA | 西安 `/ɕi⁵⁵ an⁵⁵/` [ɕi.an] (two clear syllables, no liaison) vs. 仙 `xiān` `/ɕjɛn⁵⁵/` [ɕjɛn] (one syllable) |

**Environment:** Any word/syllable boundary, including coda-nasal + vowel-initial syllable sequences; the syllable seam is preserved, no resyllabification or glide insertion of the liaison type.

**Notes:** The pinyin apostrophe (隔音符号 / 隔音符號 `géyīn fúhào`) exists precisely to **block** the resyllabification that liaison languages allow. This 'negative' rule is important for the Peshitta tiers: syllable integrity is preserved, so toneless pinyin segments map one-to-one to syllables/morphemes/Hanzi. Shared by both standards.

---

### Rule 13: 鼻音韵尾的同化 / 鼻音韻尾的同化 (`bíyīn yùnwěi de tónghuà`) — coda-nasal place assimilation (gradient)

*Category: allophony / assimilation (casual) — Standards: `both`*

In casual fast speech, a coda /n/ may assimilate in place to a following consonant, and the /n/–/ŋ/ contrast can be partially neutralized before homorganic stops: 面包 / 麵包 `miànbāo` may surface with [m]-colored coda [mjɛm pau], 很高 `hěn gāo` with a velar-colored coda [xəŋ kau]. This is gradient and optional; in careful speech the lexical coda (/n/ vs /ŋ/) is preserved, and the contrast **IS** phonemic (山 `shān` vs 商 `shāng`; 因 `yīn` vs 英 `yīng`). Mandarin only has the two nasal codas, so assimilation is limited to these.

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 面包 / 麵包 |
| Pinyin (underlying) | `miànbāo` |
| Pinyin (surface) | `miànbāo` → casual [mjɛm.pau] (coda `n` → [m] before `b`) |
| IPA | 面包 / 麵包 `/mjɛn⁵¹ pau⁵⁵/` → [mjɛm˥˩ pau˥] (casual, gradient) |

**Environment:** Syllable-final /n/ (and, weakly, /ŋ/) before a following stop/nasal of a different place, in casual connected speech; suppressed in careful speech where /n/~/ŋ/ stays contrastive.

**Notes:** Much weaker and less systematic than English nasal assimilation because Mandarin codas are already restricted to /n ŋ/. The /n/~/ŋ/ contrast is robustly maintained in careful speech and remains in the spelling (`-n` vs `-ng`), so the toneless tier is unaffected. Both standards; northern speakers may merge `-in`/`-ing`, `-en`/`-eng` in fast speech, southern accents more so.

---

### Rule 14: 规则排序 / 規則排序 (`guīzé páixù`) — rule ordering of Mandarin sandhi processes

*Category: meta / rule interaction & ordering — Standards: `both`*

Mandarin's tonal and segmental rules interact in a partly ordered way. A working order:

1. Assign **LEXICAL** tones and identify 轻声 / 輕聲 neutral-tone syllables (which then do not trigger tone sandhi).
2. Apply the **一/不** lexical sandhi on those specific morphemes.
3. Apply **THIRD-TONE** sandhi iteratively over T3 strings, bottom-up by prosodic foot, choosing T3→T2 before another T3 and the half-third [21] elsewhere.
4. Apply **儿化 / 兒化** rhotacization and rime restructuring.
5. Apply gradient, rate-dependent **casual** processes (nasal assimilation, syllable contraction, de-retroflexion in Guóyǔ) **last**.

Crucially, a syllable that has gone **NEUTRAL** no longer counts as a T3 for sandhi, and the sandhi-derived T2 is what surfaces, not the lexical T3.

| Field | Value |
|---|---|
| 汉字 / 漢字 (Simplified / Traditional) | 我想买五把雨伞 / 我想買五把雨傘 |
| Pinyin (underlying) | `wǒ xiǎng mǎi wǔ bǎ yǔsǎn` (all T3) |
| Pinyin (surface) | `wó xiáng mái wú bá yú sǎn` (iterative T3→T2, rightmost T3 retained) |
| IPA | `/wo²¹⁴ ɕjaŋ²¹⁴ mai²¹⁴ wu²¹⁴ pa²¹⁴ y²¹⁴ san²¹⁴/` → `[wo³⁵ ɕjaŋ³⁵ mai³⁵ wu³⁵ pa³⁵ y³⁵ san²¹⁴]` |

**Environment:** Whole-utterance scope; ordering matters most for T3 strings interacting with neutral tone, and for 一/不 sitting next to other tones.

**Notes:** Prosodic phrasing (foot/phrase boundaries) conditions where the rightmost full T3 lands in long T3 strings, so the output can vary with how a speaker chunks the phrase. Ordering is shared by both standards; the gradient stage (5) is where most Pǔtōnghuà/Guóyǔ surface divergence (erhua, de-retroflexion, neutral-tone frequency) appears.

---

### Summary

These processes split into **TONAL** rules (third-tone sandhi & the half-third allophone, 一/不 sandhi, neutral-tone reduction) and **SEGMENTAL/orthographic** rules (`j-q-x` complementary distribution, retroflex realization, Taiwan de-retroflexion, erhua restructuring, `ü→u` spelling, syllable contraction, the absence of liaison). The tonal rules are Mandarin's signature and apply to the **LANGUAGE** in full; they never touch the Peshitta **READER TIERS**, which are toneless by design and carry no tone to manipulate.

The principal Pǔtōnghuà/Guóyǔ divergences here are surface, not phonemic:

| Feature | 普通话 / 普通話 Pǔtōnghuà | 國語 Guóyǔ (Taiwan) |
|---|---|---|
| 儿化 / 兒化 erhua | abundant | very little (prefers non-rhotacized form) |
| retroflex `zh/ch/sh/r` | full retroflexes | frequent de-retroflexion (→ `z/c/s/-`) |
| 轻声 / 輕聲 neutral tone | more obligatory contexts | more full citation tones |

Both share the same phonemic inventory and the same **toneless pinyin spelling**. Tone sandhi is a **PRONUNCIATION** rule, not an orthographic one — pinyin keeps the underlying tone marks (你好 stays `nǐ hǎo`), and the toneless tier that anchors the Peshitta reader is therefore stable across all of these rules. Gradient, rate-dependent processes (casual nasal assimilation, syllable contraction) apply in fast speech and are suppressed in careful citation style.

---

*Compiled by Shin.*

## Pǔtōnghuà vs. Guóyǔ (Mainland vs. Taiwan Standard)

Systematic differences between the two **reference standards** of Modern Standard Mandarin (标准汉语 / 標準漢語), expressed in IPA together with 汉字/漢字 (Simplified + Traditional) and pinyin/zhuyin. The two traditions documented in parallel are **普通话 Pǔtōnghuà** — the PRC standard, based on Beijing phonology, written in SIMPLIFIED characters and romanized with 汉语拼音 Hanyu Pinyin — and **國語 Guóyǔ** — the Taiwan standard, written in TRADITIONAL characters and taught with 注音符號 Zhuyin/Bopomofo. As with the Eastern (Madnhaya) and Western (Serto) traditions of Syriac, General American and Received Pronunciation in English, or Tokyo and Kansai in Japanese, neither standard is intrinsically more correct: they are two coexisting codifications of ONE language (Mandarin, ISO 639-3 `cmn`). The crucial point is that the differences are SURFACE and LEXICAL, not systemic: both standards share the same phonemic inventory (21 initials + zero initial, ~35–38 finals, four tones + neutral), so the differences DO NOT change the toneless pinyin spine that drives the Peshitta reader tiers. The most salient divisions are (1) ERHUA (儿化/兒化) — pervasive in Pǔtōnghuà, rare in Guóyǔ; (2) DE-RETROFLEXION — much Taiwan speech merges retroflex `zh/ch/sh/r` into dental `z/c/s/(zero)`; (3) NEUTRAL-TONE frequency — high in Pǔtōnghuà, lower in Guóyǔ; plus specific lexical tone/pronunciation splits (垃圾, 和, 企, 法, 究 …), everyday VOCABULARY, and the SCRIPT divide (Simplified vs Traditional). The OTHER major Sinitic varieties — Yue/Cantonese, Wu/Shanghainese, Min/Hokkien, Hakka, Gan, Xiang — are popularly called "dialects" (方言) but are largely mutually UNINTELLIGIBLE; they are treated below as clearly secondary ASIDES, effectively sister languages within Sinitic. Phonemic transcriptions use /slashes/; phonetic detail uses [brackets]; tone is shown with Chao tone letters (˥˧˩) and/or the (55)(35)(214)(51) pitch numerals.

> **Note on tone and the reader tiers.** Mandarin is a **tonal** language and tones are rendered fully throughout this section (Chao letters + pitch numerals). The Peshitta **reader tiers are TONELESS**, however: the deterministic spine is the plain (toneless) pinyin, so none of the differences below — erhua, de-retroflexion, neutral-vs-full tone, or per-character T-splits — ever changes the reader spelling. They affect at most the Hanzi tier's per-character **citation tone**.

### Reference standards

- **普通话 Pǔtōnghuà** — the PRC standard ("common speech"), codified 1955–56 on Beijing-dialect phonology, the northern dialect base, and modern vernacular literary norms. Script: SIMPLIFIED characters (简体字); romanization: 汉语拼音 Hanyu Pinyin (official 1958). Phonetically it has HEAVY ERHUA (儿化: 花儿 `huār`, 这儿 `zhèr`, 一点儿 `yìdiǎnr`), MAINTAINS the full retroflex series `zh` /ʈʂ/, `ch` /ʈʂʰ/, `sh` /ʂ/, `r` /ʐ~ɻ/ distinct from dental `z` /ts/, `c` /tsʰ/, `s` /s/, makes ABUNDANT use of the neutral tone (轻声: 桌子 `zhuōzi`, 喜欢 `xǐhuan`, 我们 `wǒmen`), and follows the prescriptive "standard" tone/reading of each character per 《现代汉语词典》 and 《普通话异读词审音表》.
- **國語 Guóyǔ** — the Taiwan standard ("national language"), historically the same Republic-of-China standard but diverging in everyday realization. Script: TRADITIONAL characters (繁體字 / 正體字); taught and dictionary-keyed with 注音符號 Zhuyin/Bopomofo (`ㄅㄆㄇㄈ…`). Phonetically it has LITTLE OR NO erhua (花 `huā`, 這裡 `zhèlǐ`, 一點 `yìdiǎn` rather than `-r` forms), shows widespread DE-RETROFLEXION in casual speech (`zh/ch/sh` → `z/c/s`; 是 `shì` → [sɹ̩], 知道 `zhīdào` → [tsɹ̩...]), uses FEWER neutral tones (many suffixes keep a full tone), and codifies a number of DIFFERENT "standard" readings in 《重編國語辭典》 (垃圾 `lèsè`, 和 `hàn`, 企 `qì`, 法 `fǎ`, 期 `qí` …). The phonemic system is identical; the differences are surface, lexical, and orthographic.

| Label | Standard |
|---|---|
| 普通话 Pǔtōnghuà | PRC standard — Beijing-based, SIMPLIFIED characters (简体字), 汉语拼音 pinyin |
| 國語 Guóyǔ | Taiwan standard — TRADITIONAL characters (繁體字/正體字), 注音符號 zhuyin/bopomofo |

### Differences

| Feature | 普通话 Pǔtōnghuà | 國語 Guóyǔ | Examples (Simplified / Traditional) | Explanation |
|---|---|---|---|---|
| **ERHUA (儿化 / 兒化)** — rhotacized finals (the signature northern badge) | PERVASIVE: a final `-r` (儿) rhotacizes the rime, restructuring it; productive in vocabulary, diminutives, and grammatical particles. **IPA:** 花儿 [xwa˥˥ɚ̯] `huār` 'flower'; 一点儿 [i˥˩tjaɚ̯˨˩˦] `yìdiǎnr` 'a little'; 这儿 [ʈʂɤɚ̯˥˩] `zhèr` 'here'; 玩儿 [wa˧˥ɚ̯] `wánr` 'to play' (the `-n` coda is absorbed into rhotacization) | RARE / largely ABSENT: the bare (non-erhua) form is used; `-r` endings sound markedly "Mainland/Beijing". **IPA:** 花 [xwa˥˥] `huā` 'flower'; 一點 [i˥˥tjɛn˨˩˦] `yìdiǎn` 'a little'; 這裡 [ʈʂɤ˥˩li˨˩˦] (~de-retroflexed [tsɤ˥˩...]) `zhèlǐ` 'here'; 玩 [wan˧˥] `wán` 'to play' | 'flower': Simp 花儿 / Trad 花兒 — `huār` `ㄏㄨㄚㄦ` vs 花 `huā` `ㄏㄨㄚ`; 'a little': Simp 一点儿 / Trad 一點兒 — `yìdiǎnr` vs 一點 `yìdiǎn` `ㄧㄉㄧㄢˇ`; 'here': Simp 这儿 / Trad 這兒 — `zhèr` `ㄓㄜㄦ` vs 這裡 `zhèlǐ` `ㄓㄜˋㄌㄧˇ` | The single most audible regional marker. ERHUA (儿化) attaches a rhotacizing `-r` (the 儿/兒 morpheme, /ɚ/) to a final, restructuring the rime: it deletes a high-front coda or glide, can nasalize the vowel (when /n ŋ/ is present), and centralizes the nucleus, so 花儿 `huār` is one syllable [xwaɚ̯], not two. In Pǔtōnghuà (Beijing-based) erhua is everywhere — in lexical items (馅儿 `xiànr` 'filling', 空儿 `kòngr` 'free time'), diminutives (小孩儿 `xiǎoháir`), and even where it changes meaning (白面 `báimiàn` 'flour' vs 白面儿 `báimiànr` 'heroin', slang). Guóyǔ speakers use it sparingly to not at all, preferring the bare form (一點 `yìdiǎn`, 這裡 `zhèlǐ`) and substituting non-erhua words (玩 instead of 玩儿). Crucially, in the toneless Peshitta reader spine erhua is NOT generated — the reader tiers use the plain finals — so this difference, like the others, never alters the deterministic toneless pinyin. |
| **DE-RETROFLEXION** — merger of retroflex `zh/ch/sh/r` into dental `z/c/s` | RETROFLEX series MAINTAINED and distinct: `zh` /ʈʂ/, `ch` /ʈʂʰ/, `sh` /ʂ/, `r` /ʐ~ɻ/ vs dental `z` /ts/, `c` /tsʰ/, `s` /s/. **IPA:** 是 `shì` [ʂɻ̩˥˩] 'to be'; 知道 `zhīdào` [ʈʂɻ̩˥˥tɑʊ˥˩] 'to know'; 山 `shān` [ʂan˥˥] 'mountain'; 人 `rén` [ʐən˧˥] 'person' | WIDESPREAD merger in casual speech: `zh`→`z`, `ch`→`c`, `sh`→`s`, and `r` often weakened/de-retroflexed (toward [z]~zero); the retroflex/dental contrast is partly or wholly neutralized for many speakers. **IPA:** 是 `shì` → [sɹ̩˥˩] (≈ 'sì'); 知道 `zhīdào` → [tsɹ̩˥˥tɑʊ˥˩] (≈ 'zīdào'); 山 `shān` → [san˥˥] (≈ 'sān'); 人 `rén` often [zən˧˥]~[ən˧˥] | 'to be' 是 (Simp/Trad 是): `shì` [ʂɻ̩] vs many-Taiwan [sɹ̩] (sounds like 四 `sì`); 'mountain' 山 (Simp/Trad 山): `shān` [ʂan] vs Taiwan often [san] (sounds like 三 `sān`); 'to eat' 吃 (Simp 吃 / Trad 吃): `chī` [ʈʂʰɻ̩] vs Taiwan often [tsʰɹ̩] (toward 'cī') | In much Taiwan (and southern-Mainland) speech the RETROFLEX initials `zh` /ʈʂ/, `ch` /ʈʂʰ/, `sh` /ʂ/, `r` /ʐ/ are de-retroflexed and merge with the DENTAL/apical series `z` /ts/, `c` /tsʰ/, `s` /s/. The result is that pairs the standard keeps apart can fall together: 是 `shì` vs 四 `sì`, 山 `shān` vs 三 `sān`, 知 `zhī` vs 资 `zī`. This is a SUBSTRATE effect — Southern Min and Hakka (the heritage languages of Taiwan) lack a retroflex series — and it is a feature of pronunciation, not of the standard: formal Guóyǔ, like Pǔtōnghuà, prescribes the retroflexes, and they remain in careful/broadcast speech. Because the contrast is preserved in the SPELLING, the toneless pinyin spine still writes 是 as `shi` and 山 as `shan`; the merger is a surface realization layered on top. (Pǔtōnghuà speakers in the north sometimes have the opposite tendency — hyper-retroflexion — but the standard keeps the two series distinct.) |
| **NEUTRAL TONE (轻声 / 輕聲)** frequency — high in Pǔtōnghuà, lower in Guóyǔ | FREQUENT neutral tone: many second syllables of disyllables, suffixes (子, 头, 们), reduplications, and grammatical particles lose their lexical tone and become short/toneless. **IPA:** 桌子 `zhuōzi` [ʈʂwo˥˥tsɹ̩] 'table' (子 neutral); 喜欢 `xǐhuan` [ɕi˨˩xwan] 'to like' (欢 neutral); 我们 `wǒmen` [wo˨˩mən] 'we' (们 neutral); 木头 `mùtou` [mu˥˩tʰoʊ] 'wood' (头 neutral) | FEWER neutral tones: the same syllables frequently keep their FULL lexical tone, so words sound more "evenly stressed". **IPA:** 桌子 `zhuōzǐ` [ʈʂwo˥˥tsɹ̩˨˩˦] (子 keeps T3); 喜歡 `xǐhuān` [ɕi˨˩˦xwan˥˥] (歡 keeps T1); 木頭 `mùtóu` [mu˥˩tʰoʊ˧˥] (頭 keeps T2) | 'table' (Simp/Trad 桌子): `zhuōzi` (子 neutral) vs `zhuōzǐ` (子 = T3) `ㄓㄨㄛ ㄗˇ`; 'to like' (Simp 喜欢 / Trad 喜歡): `xǐhuan` (欢 neutral) vs `xǐhuān` (歡 = T1) `ㄒㄧˇ ㄏㄨㄢ`; 'wood' (Simp 木头 / Trad 木頭): `mùtou` (头 neutral) vs `mùtóu` (頭 = T2) `ㄇㄨˋ ㄊㄡˊ` | The NEUTRAL TONE (轻声/輕聲) — a short, unstressed syllable whose pitch is determined by the preceding tone rather than carrying a lexical tone of its own — is far MORE common in Pǔtōnghuà than in Guóyǔ. Pǔtōnghuà neutralizes a large set of second syllables: the suffixes 子/头/们, reduplicated kinship terms (妈妈 `māma`, 爸爸 `bàba`), directional and aspect complements, and many lexicalized compounds. Guóyǔ retains the full citation tone on many of these (桌子 `zhuōzǐ` with 子 as T3, 木頭 `mùtóu` with 頭 as T2), giving Taiwan speech a more level, less "swallowed" rhythm. This is one reason the two standards differ audibly even on identical words and identical characters. As with erhua, the Peshitta reader tiers are TONELESS, so neutral-vs-full-tone never affects the spelling — but the Hanzi tier's per-character citation tone will reflect whichever standard's reading is chosen. |
| **Lexical TONE/READING splits** — individual characters with different "standard" readings | Prescriptive Mainland readings per 《现代汉语词典》 / 《普通话异读词审音表》. **IPA:** 垃圾 `lājī` [la˥˥tɕi˥˥] 'garbage'; 和 `hé` [xɤ˧˥] 'and'; 企业 `qǐyè` [tɕʰi˨˩˦jɛ˥˩] 'enterprise'; 法国 `Fǎguó` [fa˨˩˦kwo˧˥] 'France'; 期 `qī` [tɕʰi˥˥] '(time) period'; 究 `jiū` [tɕjoʊ˥˥] 'investigate' | Different codified readings per 《重編國語辭典》 (Taiwan Ministry of Education). **IPA:** 垃圾 `lèsè` [lɤ˥˩sɤ˥˩] 'garbage'; 和 `hàn` [xan˥˩] 'and' (also `hé` in formal); 企業 `qìyè` [tɕʰi˥˩jɛ˥˩] 'enterprise'; 法國 `Fàguó` [fa˥˩kwo˧˥] 'France'; 期 `qí` [tɕʰi˧˥] '(time) period'; 究 `jiù` [tɕjoʊ˥˩] 'investigate' | 'garbage' 垃圾 (Simp/Trad 垃圾): `lājī` `ㄌㄚ ㄐㄧ` vs `lèsè` `ㄌㄜˋ ㄙㄜˋ` (the most famous split); 'and' 和 (Simp/Trad 和): `hé` `ㄏㄜˊ` vs colloquial-Taiwan `hàn` `ㄏㄢˋ` (conjunction); 'enterprise' 企 (Simp 企业 / Trad 企業): `qǐ` (T3) `ㄑㄧˇ` vs `qì` (T4) `ㄑㄧˋ`; 'France/law' 法 (Simp 法国 / Trad 法國): `Fǎ` (T3) `ㄈㄚˇ` vs `Fà` (T4) `ㄈㄚˋ` in 法國; 'period' 期 (Simp/Trad 期): `qī` (T1) `ㄑㄧ` vs `qí` (T2) `ㄑㄧˊ` | Beyond systematic phonology, the two standards simply ASSIGN DIFFERENT "correct" readings to a number of individual characters and words. The textbook case is 垃圾 'garbage': Pǔtōnghuà `lājī` vs Guóyǔ `lèsè` — same two characters, entirely different pronunciation. Others: the conjunction 和 'and' is `hé` on the Mainland but commonly `hàn` in spoken Taiwan; 企 is `qǐ` (T3) vs `qì` (T4) (so 企业/企業 'enterprise' is `qǐyè` vs `qìyè`); 法 is `Fǎ` (T3) vs `Fà` (T4) in 法國 'France'; 期 'period' is `qī` (T1) vs `qí` (T2); 究 is `jiū` (T1) vs `jiù` (T4); 微 is `wēi` vs `wéi` for some speakers; 攻击/攻擊 'attack' is `gōngjī` vs `gōngjí`. These are lexical, character-by-character facts codified in the two countries' standard dictionaries, NOT predictable sound laws. They affect the Hanzi tier's citation tone but, because the toneless reader spine carries no tone, they leave the Peshitta toneless pinyin unchanged (a T3-vs-T4 split on 企 still spells `qi`). |
| **VOCABULARY** — divergent everyday words and loan strategies | Mainland lexicon and (often) phonetic/calque loan strategy: 土豆 `tǔdòu` 'potato'; 西红柿 `xīhóngshì` 'tomato'; 出租车 `chūzūchē` 'taxi'; 自行车 `zìxíngchē` 'bicycle'; 软件 `ruǎnjiàn` 'software'; 信息 `xìnxī` 'information'; 星期一 `xīngqīyī` 'Monday' | Taiwan lexicon and (often) different coinage, sometimes transliteration or a different native compound: 馬鈴薯 `mǎlíngshǔ` 'potato'; 番茄 `fānqié` 'tomato'; 計程車 `jìchéngchē` 'taxi'; 腳踏車 `jiǎotàchē` 'bicycle'; 軟體 `ruǎntǐ` 'software'; 資訊 `zīxùn` 'information'; 星期一 / 禮拜一 `lǐbàiyī` 'Monday' | 'potato': Simp 土豆 (`tǔdòu`) vs Trad 馬鈴薯 (`mǎlíngshǔ`) — note 土豆 means 'peanut' in some Taiwan usage; 'taxi': Simp 出租车 (`chūzūchē`) vs Trad 計程車 (`jìchéngchē`); HK uses 的士 `díshì`; 'software': Simp 软件 (`ruǎnjiàn`) vs Trad 軟體 (`ruǎntǐ`); 'hardware' Simp 硬件 vs Trad 硬體; 'information': Simp 信息 (`xìnxī`) vs Trad 資訊 (`zīxùn`); 'bicycle': Simp 自行车 (`zìxíngchē`) vs Trad 腳踏車 (`jiǎotàchē`) | A non-exhaustive sample of LEXICAL divergence between the two standards (parallel to GA 'truck'/RP 'lorry' or Tokyo ありがとう/Kansai おおきに). Both varieties share the vast common core, but everyday items differ — 土豆 vs 馬鈴薯 'potato', 出租车 vs 計程車 'taxi', 自行车 vs 腳踏車 'bicycle' — and the two communities often coined different terms for modern/technical concepts (软件/軟體 'software', 信息/資訊 'information', 网络/網路 'network', 数据/資料 'data'). A few words are "false friends": 土豆 is 'potato' on the Mainland but commonly 'peanut' in Taiwan; 窝心 `wōxīn` is positive ('heartwarming') in Taiwan but negative ('aggravating') on the Mainland. These are vocabulary differences, not phonology, but, like the script split, they immediately signal which standard a text or speaker uses. |
| **SCRIPT** — Simplified (简体字) vs Traditional (繁體字) characters | SIMPLIFIED characters (简体字), PRC reform of the 1950s–60s (also used in Singapore/Malaysia); reduced stroke counts and merged/abbreviated forms: 国 `guó` 'country'; 爱 `ài` 'love'; 龙 `lóng` 'dragon'; 听 `tīng` 'listen'; 学 `xué` 'study'; 体 `tǐ` 'body'; 后 `hòu` (covers 後 'after' and 后 'queen') | TRADITIONAL characters (繁體字 / 正體字), the historical forms preserved in Taiwan, Hong Kong, and Macau; fuller component structure, more semantic transparency: 國 `guó` 'country'; 愛 `ài` 'love'; 龍 `lóng` 'dragon'; 聽 `tīng` 'listen'; 學 `xué` 'study'; 體 `tǐ` 'body'; 後 `hòu` 'after' vs 后 `hòu` 'queen' (kept distinct) | 'country': Simp 国 / Trad 國 (`guó`) — both `ㄍㄨㄛˊ`, identical sound; 'love': Simp 爱 / Trad 愛 (`ài`) — Simplified drops the 心 'heart' component; 'dragon': Simp 龙 / Trad 龍 (`lóng`); 'listen': Simp 听 / Trad 聽 (`tīng`); 'body': Simp 体 / Trad 體 (`tǐ`) | The most VISIBLE difference is purely ORTHOGRAPHIC and does not touch pronunciation at all. Pǔtōnghuà is written in SIMPLIFIED characters (简体字) — the PRC's 1950s–60s reform that cut stroke counts (国 for 國, 爱 for 愛, 龙 for 龍, 听 for 聽) and, in some cases, merged distinct characters into one (后 now writes both 'queen' 后 and 'after' 後; 干 covers 乾/幹/干). Guóyǔ is written in TRADITIONAL characters (繁體字, called 正體字 'orthodox' in Taiwan) — the inherited forms also used in Hong Kong and Macau, which keep fuller component structure and the original character distinctions. The reading (sound and tone) of 国 and 國 is identical (`guó`); the difference is glyph shape, not phonology. In Unicode both belong to CJK Unified Ideographs (`U+4E00`–`U+9FFF` and extensions); many simp/trad pairs are encoded at separate code points (国 `U+56FD` vs 國 `U+570B`). The Peshitta ships BOTH a Simplified and a Traditional Hanzi reader tier precisely to serve both standards from the one toneless pinyin spine. |

### Asides: the other major Sinitic branches (方言)

CLEARLY SECONDARY. The varieties below are the other major branches of SINITIC (汉语族 / 漢語族) — popularly called "dialects" (方言 `fāngyán`) in Chinese but, by the linguistic criterion of mutual intelligibility, effectively SEPARATE LANGUAGES: a Mandarin speaker cannot understand spoken Cantonese, Shanghainese, or Hokkien without learning them. They are NOT part of the two Mandarin reference standards above and are NOT targets of the six Chinese reader tiers (Scholarly + Pretty [two language-neutral Latin tiers], Toneless Pinyin, Zhuyin/Bopomofo, Simplified Hanzi, Traditional Hanzi). They share the Sinitic descent and most of the written Hanzi tradition, but their phonology — and often their tone systems, syllable codas, and core vocabulary — differs profoundly. Everything here is for orientation only.

| Topolect | Key feature | IPA illustration |
|---|---|---|
| **粤语 / 粵語 — Yue** (Cantonese 广东话/廣東話, 廣州話; Guangdong, Hong Kong, Macau, diaspora) | The most widely known non-Mandarin Sinitic language; SIX tones (some count 9 with the "entering" tone split), and conservative CODA inventory keeping final `-p -t -k` stops and final `-m` (all lost in Mandarin) | 九 'nine' [kɐu˧˥] `gau2`; 香港 'Hong Kong' Hēunggóng [hœːŋ˥ kɔːŋ˧˥]; checked syllables 一 [jɐt˥] `jat1`, 十 [sɐp˨] `sap6`, 六 [lʊk˨] `luk6`; final `-m` in 心 [sɐm˥] `sam1` 'heart' |
| **吴语 / 吳語 — Wu** (Shanghainese 上海话/上海話, Suzhou, Wenzhou; Shanghai + Jiangsu/Zhejiang) | Retains a VOICED obstruent series (the Middle Chinese voicing contrast Mandarin lost) and has a reduced, largely predictable tone system driven by tone sandhi over whole phrases | Shanghainese 上海 'Shanghai' [zɑ̃˩˩ he˧˧] Zånhe; voiced initials e.g. 爬 [ba] vs 怕 [pʰa] vs 把 [pa] (three-way voiced/aspirated/plain, vs Mandarin's two-way); pervasive phrasal tone sandhi flattening citation tones |
| **闽语 / 閩語 — Min** (Hokkien 闽南话/閩南話, Taiwanese 台語; Fujian, Taiwan, SE Asia) | The most internally divergent Sinitic branch; splits from the rest BEFORE Middle Chinese, has a literary-vs-colloquial reading split (文白异读), entering-tone stops, and elaborate tone sandhi "circles" | Hokkien 台灣/臺灣 'Taiwan' Tâi-oân [tai˧˧ uan˧˥]; literary vs colloquial readings of one character, e.g. 人 lîn (literary) vs lâng (colloquial); checked syllables 國 kok, 十 cha̍p; thanks 多謝 to-siā / 感謝 kám-siā |
| **客家话 / 客家話 — Hakka** (客語; scattered across Guangdong, Fujian, Jiangxi, Taiwan, diaspora) | A geographically dispersed but internally coherent branch; conservative consonant codas (`-p -t -k`, `-m -n -ŋ`) and typically six tones | Hakka 客家 'Hakka' Hak-kâ [hak̚˨ ka˧]; 'thank you' 承蒙你 sṳ̀n-mèn-n̂; checked finals 一 yit, 食 sṳ̍t 'eat'; final `-m` kept in 心 sîm 'heart' |
| **赣语 / 贛語 — Gan** (江西话; Jiangxi) and **湘语 / 湘語 — Xiang** (湖南话; Hunan) | Two further primary Sinitic branches of central-southern China; Gan adjoins Hakka and Wu, Xiang ("Old" vs "New") varies in whether it retains voiced initials | Gan (Nanchang 南昌話) keeps entering-tone stops; Xiang — Old Xiang (e.g. Shuangfeng) preserves voiced obstruents like Wu, while New Xiang (e.g. Changsha 長沙話) has largely lost them under Mandarin influence |

#### Notes on each branch

- **Yue (粤语 / 粵語).** Yue, of which Cantonese (Guangzhou/Hong Kong speech) is the prestige form, is the best-known Sinitic language after Mandarin, with a large diaspora and its own film/music tradition. Phonologically it is far more conservative than Mandarin in its syllable structure: it KEEPS the Middle Chinese final stop codas `-p -t -k` (the "entering tone" 入聲) and the final nasal `-m`, all of which Mandarin has lost (Mandarin allows only `-n` and `-ng`). Its tone system is also much larger — commonly analyzed as SIX contrastive tones (or NINE if the three entering-tone variants on `-p/-t/-k` syllables are counted separately) against Mandarin's four. Cantonese is written with shared Hanzi plus its own colloquial characters (係 `hai6` 'to be', 唔 `m4` 'not', 嘅 `ge3`), and is mutually UNINTELLIGIBLE with Mandarin in speech.
- **Wu (吴语 / 吳語).** Wu, whose flagship is Shanghainese (上海话), is spoken across Shanghai, southern Jiangsu, and Zhejiang. Its hallmark is the preservation of a VOICED obstruent series — a three-way initial contrast (voiceless unaspirated / voiceless aspirated / VOICED, e.g. 把/怕/爬) where Mandarin has only the two-way aspiration contrast (`b`/`p`), because Mandarin merged the old voiced stops into voiceless. Wu tone behaves very differently too: citation tones are heavily overridden by phrase-level TONE SANDHI, so the melody of a multi-syllable word is set by its first syllable rather than syllable-by-syllable. It is mutually unintelligible with Mandarin and internally diverse (Suzhou, Wenzhou, etc., differ greatly among themselves).
- **Min (闽语 / 閩語).** Min (Hokkien/Southern Min being the most prominent sub-branch, and the basis of Taiwanese 台語) is the most divergent Sinitic group — it branched off so early that it cannot be derived neatly from Middle Chinese the way the others can. Its signature features are a thoroughgoing LITERARY-vs-COLLOQUIAL reading split (文白異讀: most characters have a "reading" pronunciation and a separate everyday "speech" pronunciation, e.g. 人 lîn vs lâng), retention of the entering-tone final stops (`-p -t -k -ʔ`), and famously complex tone-sandhi "chains" in which nearly every non-final syllable shifts tone. It is written with Hanzi plus the Latin-based Pe̍h-ōe-jī (白話字) romanization, and is wholly unintelligible to a Mandarin speaker.
- **Hakka (客家话 / 客家話).** Hakka (客家話/客語) is spoken by the "guest families" (客家) dispersed through the hills of Guangdong, Fujian, Jiangxi, and elsewhere, with a substantial community in Taiwan. Despite its scattered geography it is fairly internally coherent. Like Cantonese and Min it is conservative in keeping the full set of final stop codas (`-p -t -k`) and nasal codas (`-m -n -ŋ`) that Mandarin lost, and it typically has around six tones. It is mutually unintelligible with Mandarin and is recognized as one of Taiwan's national languages alongside Mandarin and the indigenous Formosan languages.
- **Gan (赣语 / 贛語) and Xiang (湘语 / 湘語).** Gan (赣语, Jiangxi) and Xiang (湘语, Hunan) round out the conventional list of major Sinitic branches (Mandarin, Yue, Wu, Min, Hakka, Gan, Xiang — sometimes Jin 晋语 and Pinghua 平話 are split off as additional groups). Gan, spoken mainly in Jiangxi, shares features with neighboring Hakka and Wu. Xiang divides into "Old Xiang" (which, like Wu, preserves Middle Chinese voiced initials) and "New Xiang" (which has lost them, partly under Mandarin pressure). Both are spoken by tens of millions, both are mutually unintelligible with Mandarin, and both are included here only to complete the picture of how internally diverse Sinitic is beyond the single Mandarin standard.

### Summary

Pǔtōnghuà (普通话, PRC, SIMPLIFIED characters, pinyin) and Guóyǔ (國語, Taiwan, TRADITIONAL characters, zhuyin) are two codifications of ONE language sharing an identical phonemic system (21 initials + zero, ~35–38 finals, four tones + neutral); their differences are SURFACE, LEXICAL, and ORTHOGRAPHIC, and they do NOT change the toneless pinyin spine that drives the Peshitta reader tiers. The most audible badges are: ERHUA (儿化/兒化) — heavy in Pǔtōnghuà (花儿 `huār`, 一点儿 `yìdiǎnr`, 这儿 `zhèr`) but rare in Guóyǔ (花 `huā`, 一點 `yìdiǎn`, 這裡 `zhèlǐ`); DE-RETROFLEXION — much Taiwan speech merges retroflex `zh/ch/sh/r` into dental `z/c/s` (是 `shì`→[sɹ̩]≈四, 山 `shān`→[san]≈三), a Southern-Min/Hakka substrate effect, while both standards prescribe the retroflexes; lower NEUTRAL-TONE frequency in Guóyǔ (桌子 `zhuōzǐ`, 木頭 `mùtóu` keep full tones vs Pǔtōnghuà neutral `zhuōzi`, `mùtou`); and per-character LEXICAL splits — 垃圾 `lājī` vs `lèsè` (the iconic case), 和 `hé` vs `hàn` 'and', 企 `qǐ` vs `qì`, 法 `Fǎ` vs `Fà` (法國), 期 `qī` vs `qí`, 究 `jiū` vs `jiù` — plus VOCABULARY (土豆/馬鈴薯 'potato', 出租车/計程車 'taxi', 软件/軟體 'software', 信息/資訊 'information') and the SCRIPT divide (国/國, 爱/愛, 龙/龍 — same sound, different glyph). All of these affect at most the Hanzi tier's per-character CITATION tone, never the toneless reader spelling. The ASIDES stand clearly apart: the other major SINITIC branches — Yue/Cantonese (粤语, 6+ tones, final `-p/-t/-k` and `-m`), Wu/Shanghainese (吴语, a retained voiced-obstruent series and phrasal sandhi), Min/Hokkien (闽语, the most divergent branch, with 文白異讀 literary/colloquial reading splits and entering-tone stops), Hakka (客家话, conservative codas, ~6 tones), Gan (赣语) and Xiang (湘语) — are called "dialects" (方言) but are largely mutually UNINTELLIGIBLE with Mandarin, effectively sister languages within Sinitic, included here for orientation only and outside the scope of the two Mandarin reference standards and the six toneless-pinyin-anchored reader tiers.

---

*Compiled by Shin.*

## Orthography: Hanzi, Pinyin & Zhuyin

Mandarin Chinese is written with HANZI (`汉字` / `漢字`), a LOGOGRAPHIC script in which each character is an indivisible sign standing — in the overwhelmingly default case — for one SYLLABLE and one MORPHEME at once (`字` zì 'character' ≈ `音节` yīnjié 'syllable' ≈ `语素` yǔsù 'morpheme'). This near one-to-one alignment of glyph, syllable, and meaning is the structural signature of the script and the consequence of Mandarin's analytic, one-syllable-per-morpheme typology. Crucially, Hanzi are DEEPLY NON-PHONEMIC: a character's shape encodes meaning and, at best, a partial and unreliable phonetic hint, but it does NOT spell out the sound the way an alphabet does — you cannot reliably read aloud a character you have never met, and nothing in the glyph marks TONE at all.

To pin sound to script, Mandarin therefore relies on two SHALLOW, fully PHONEMIC auxiliary systems read off the standard syllable inventory: `汉语拼音` (Hànyǔ Pīnyīn, the official PRC Latin romanization, 1958) and `注音符号` (Zhùyīn Fúhào / Bopomofo, the Taiwan phonetic alphabet). Both spell every legal Mandarin syllable transparently (initial + final + tone) and stand in a near-mechanical correspondence to each other and to the IPA. This guide documents the two standards in parallel — `普通话` Pǔtōnghuà (PRC, SIMPLIFIED characters `简体字`, Pinyin) and `國語` Guóyǔ (Taiwan, TRADITIONAL characters `繁體字`, Zhuyin) — which also key the two Hanzi script tiers. It lays out the logographic principle, the `六書` (liùshū) six classical character types (especially `形声` phono-semantic compounds, ~80–90% of characters), radicals (`部首`) and components, stroke order (`笔顺`), the unreliability of phonetic components, the SIMPLIFIED↔TRADITIONAL relationship and its mostly-but-not-fully-deterministic conversion, the full Pinyin spelling/tone-diacritic rules, the 37-symbol Zhuyin system, the older Wade–Giles romanization, a Pinyin↔Zhuyin↔IPA correspondence table, sample radicals, and the grapheme↔phoneme split between the non-phonemic Hanzi and the phonemic Pinyin/Zhuyin. Both reference standards share the SAME phonemic system; their differences are in CHARACTER SET (simplified vs traditional), DEFAULT TRANSCRIPTION (Pinyin vs Zhuyin), and a thin layer of surface/lexical pronunciation — none of which changes the toneless spelling that the Peshitta reader tiers are built on.

**Reference standards:**

| Label | Standard | Characters | Transcription |
|---|---|---|---|
| Pǔtōnghuà (PTH) | `普通话` — PRC Standard Mandarin, Beijing-based phonology; the mainland and Singapore norm. The Chinese Peshitta's primary phonetic tier (TONELESS PINYIN) and its SIMPLIFIED Hanzi tier follow this standard. | SIMPLIFIED `简体字` (jiǎntǐzì) | `汉语拼音` (Hànyǔ Pīnyīn), official 1958 Latin romanization with tone diacritics |
| Guóyǔ (GUO) | `國語` — Taiwan Standard Mandarin (cf. also `華語` Huáyǔ overseas), the major alternative norm. Shares the IDENTICAL phonemic system, the SAME initials/finals/tones, and the SAME toneless syllable spellings as Pǔtōnghuà. The Peshitta's ZHUYIN tier and TRADITIONAL Hanzi tier follow this standard. | TRADITIONAL `繁體字` (fántǐzì) | `注音符號` (Zhùyīn Fúhào / Bopomofo) |

Guóyǔ's differences from Pǔtōnghuà are in the CHARACTER SET (traditional glyphs), the pedagogical TRANSCRIPTION (Zhuyin rather than Pinyin), the near-absence of ERHUA (`儿化`/`兒化`), frequent DE-RETROFLEXION (zh/ch/sh/r tending toward z/c/s in casual speech), fewer neutral tones, and a handful of lexical tone/reading differences (`垃圾` lājī vs lèsè 'garbage'; `和` hé vs hàn 'and'; `企` qǐ vs qì) — NONE of which alters the toneless spelling that keys the reader tiers.

### General Principles

Six principles govern how the script maps glyph to sound.

#### Logographic: one character ≈ one syllable ≈ one morpheme

Hanzi are LOGOGRAPHIC (more precisely morphosyllabic): each character writes one MORPHEME and, by Mandarin's one-syllable-per-morpheme typology, one SYLLABLE. The glyph carries MEANING directly; it does not decompose into letters for individual phonemes. There is no native way to 'sound out' an unknown character from its shape — a learner who does not know `鬱` yù 'depressed/luxuriant' cannot read it aloud, whereas a learner who does not know an English word can still attempt its phonemes. This is the polar opposite of the shallow Pinyin/Zhuyin systems and the deep heart of why the script is non-phonemic.

| Example | Reading | Phonetic | Gloss |
|---|---|---|---|
| `山` | shān | /ʂan˥/ | one glyph = one syllable = one morpheme 'mountain' |
| `水` | shuǐ | /ʂwei˨˩˦/ | a single pictographic morpheme-syllable 'water' |
| `好` | hǎo | /xau˨˩˦/ | 'good' |
| `你好` | nǐ hǎo | — | 'hello' = two characters = two syllables = two morphemes |
| `咖啡` | kāfēi | — | 'coffee' — rare polysyllabic loan, still one-syllable-per-char (the two chars individually meaningless, used purely for sound) |
| `葡萄` | pútáo | — | 'grape' — same pattern |

#### The 六書 (liùshū): six character types

The traditional `六書` (liùshū, 'six writings') classify how characters are formed. Only the first four make characters; the last two describe usage.

| # | Type | Romanization | Principle |
|---|---|---|---|
| 1 | `象形` | xiàngxíng | PICTOGRAMS depict an object |
| 2 | `指事` | zhǐshì | SIMPLE INDICATIVES point at an abstract idea |
| 3 | `会意` / `會意` | huìyì | COMPOUND INDICATIVES join meanings |
| 4 | `形声` / `形聲` | xíngshēng | PHONO-SEMANTIC COMPOUNDS — by far the largest class, ~80–90% of all characters — pair a SEMANTIC component (radical, hinting meaning) with a PHONETIC component (hinting sound) |
| 5 | `转注` / `轉注` | zhuǎnzhù | 'derivative cognates' — a principle of extended use, not a new shape |
| 6 | `假借` | jiǎjiè | 'phonetic loan / rebus' — a principle of extended use, not a new shape |

| Type | Examples |
|---|---|
| `象形` pictogram | `日` rì 'sun', `月` yuè 'moon', `木` mù 'tree', `山` shān 'mountain', `人` rén 'person' |
| `指事` indicative | `一` yī 'one', `二` èr 'two', `上` shàng 'above', `下` xià 'below', `本` běn 'root' (`木` + a mark at the base) |
| `会意` compound-meaning | `明` míng 'bright' (`日`+`月`), `休` xiū 'rest' (`人` person + `木` tree = leaning on a tree), `好` hǎo 'good' (`女` woman + `子` child) |
| `形声` phono-semantic (the ~80%+ majority) | `河` hé 'river' = `氵` water + `可` kě (sound); `清` qīng 'clear' = `氵` water + `青` qīng (sound); `妈`/`媽` mā = `女` + `马`/`馬` mǎ; `铜`/`銅` tóng 'copper' = `钅`/`釒` metal + `同` tóng (sound) |
| `假借` rebus loan | `來`/`来` lái 'come' originally pictured a wheat plant, borrowed for the homophonous verb 'to come' |

#### Radicals and components

Characters are built from recurring COMPONENTS; the indexing component is the `部首` (bùshǒu, 'radical' or section-header), traditionally the 214 KANGXI RADICALS (`康熙部首`). In a `形声` compound the radical is usually the SEMANTIC part and gives the rough meaning domain (`氵`=water, `木`=tree/wood, `钅`/`釒`=metal, `口`=mouth/speech, `心`/`忄`=heart/emotion, `扌`=hand/action). Many radicals have a free-standing full form and a bound combining form (`水`→`氵`, `手`→`扌`, `人`→`亻`, `心`→`忄`, `火`→`灬`, `金`→`钅`/`釒`). Dictionaries are ordered by radical + residual stroke count. The radical narrows meaning but, like the phonetic, only hints — it never spells the sound.

| Radical (bound form) | Domain | Examples |
|---|---|---|
| `氵` (water, from `水`) | water | `河` hé river, `海` hǎi sea, `江` jiāng river, `湖` hú lake, `洗` xǐ wash |
| `口` (mouth) | mouth/speech | `吃` chī eat, `叫` jiào call, `听`/`聽` tīng listen, `唱` chàng sing |
| `心`/`忄` (heart) | emotion | `想` xiǎng think, `怕` pà fear, `忙` máng busy, `情` qíng emotion |
| `亻` (person, bound form of `人`) | person | `你` nǐ you, `他` tā he, `们`/`們` men (plural), `住` zhù live |
| `扌` (hand, bound form of `手`) | hand/action | `打` dǎ hit, `拿` ná hold, `找` zhǎo seek, `推` tuī push |

#### Stroke order (笔顺 / 筆順)

Every character is written as an ordered sequence of STROKES (`笔画`/`筆畫` bǐhuà) following a conventional STROKE ORDER (`笔顺`/`筆順` bǐshùn). The canonical rules: top before bottom, left before right, horizontal before crossing vertical, outside before inside, inside before closing the enclosure, center before flanking symmetric sides. Stroke order is not merely calligraphic etiquette: it determines residual stroke COUNT (used for dictionary lookup) and the shape of cursive/handwritten forms, and it is what handwriting and IME recognition expect. The basic stroke types (`横` héng ─, `竖`/`豎` shù │, `撇` piě ノ, `捺` nà ㇏, `点`/`點` diǎn 丶, plus hooks `钩`/`鉤` and turns `折`) are themselves named units.

| Character | Reading | Stroke account | Rule illustrated |
|---|---|---|---|
| `十` | shí 'ten' | 2 strokes: horizontal ─ then vertical │ | horizontal before crossing vertical |
| `木` | mù 'tree' | 4 strokes: ─ │ ノ ㇏ (horizontal, vertical, left-falling, right-falling) | top/left ordering |
| `国`/`國` | guó 'country' | inner content written first, then the bottom of the `囗` enclosure closed LAST | inside before closing the enclosure |
| `永` | yǒng 'eternal' | the classic `永字八法` (Eight Principles of Yong) exemplar | contains the eight fundamental stroke types |

#### Unreliability of the phonetic component

The PHONETIC component of a `形声` character is only a PARTIAL clue to the sound, and an unreliable one. Sound change over ~3,000 years has eroded once-regular correspondences, so a shared phonetic now yields characters that may agree on the initial, the final, the tone, all, or NONE. The clue degrades along a spectrum from exact to misleading, it never marks tone, and it never applies to meaning. This residual phonetic hinting is the closest Hanzi come to being phonographic, and it is precisely why a fully explicit phonemic layer (Pinyin/Zhuyin) is required to fix pronunciation.

| Degree | Phonetic | Derived characters | What survives |
|---|---|---|---|
| RELIABLE | `青` qīng | `清` qīng (clear), `晴` qíng (fine weather), `请`/`請` qǐng (please), `情` qíng (feeling) | initial + final agree, tone varies |
| PARTIAL | `马`/`馬` mǎ | `妈`/`媽` mā, `骂`/`罵` mà, `吗`/`嗎` ma | same rime, tone all different |
| MISLEADING | `也` yě | `他` tā, `地` dì, `池` chí | the once-shared sound has diverged so far the hint is useless today |
| TONE NEVER ENCODED | `包` bāo | `饱`/`飽` bǎo, `抱` bào, `跑` pǎo, `泡` pào | four different tones (and `跑`/`泡` change the initial) |

#### Hanzi non-phonemic vs Pinyin/Zhuyin phonemic

There are two grapheme→phoneme regimes in the system, at opposite ends of orthographic depth. HANZI are DEEP / NON-PHONEMIC: the glyph→sound map is unpredictable, many-to-many (polyphony: one char, several readings; homophony: many chars, one sound), and silent on tone. PINYIN and ZHUYIN are SHALLOW / PHONEMIC: each spells the syllable's initial + final + tone explicitly and near-mechanically (one spelling ≈ one pronunciation), so reading them aloud is essentially a lookup. The Peshitta exploits exactly this: its phonetic spine is TONELESS PINYIN (deterministic), with Zhuyin a transcode of it, while the Hanzi tiers are a downstream character lookup that unavoidably imposes a citation tone per character.

| Phenomenon | Illustration |
|---|---|
| polyphony (`多音字` duōyīnzì) | `行` = xíng 'walk/OK' / háng 'row, firm'; `长`/`長` = cháng 'long' / zhǎng 'grow, chief'; `重` = zhòng 'heavy' / chóng 'again'; `乐`/`樂` = lè 'happy' / yuè 'music' |
| homophony | yì is written `一` `易` `益` `义`/`義` `议`/`議` `亿`/`億` `译`/`譯` `异`/`異` `翼` … (hundreds of distinct morphemes share one toneless syllable, disambiguated only by the character) |
| Pinyin transparency | `<zhuang>` always = /ʈʂwaŋ/ (initial zh + final uang); `<qi>` always = /tɕʰi/ — no exceptions to learn |
| Zhuyin transparency | `ㄓㄨㄤ` = zhuang, `ㄑㄧ` = qi — a one-to-one transcode of the Pinyin |

### Hanzi (汉字 / 漢字)

`汉字` / `漢字` (Hànzì) are the LOGOGRAPHIC characters of Chinese, each an indivisible sign carrying a MEANING and (by Mandarin's typology) one SYLLABLE; they are the deep, non-phonemic core of the writing system. Literacy is conventionally pegged at ~3,000–3,500 characters for a newspaper; the PRC's `通用规范汉字表` (General Standard Chinese Characters table, 2013) lists 8,105, of which the first 3,500 (`一级字表`) cover everyday use; large dictionaries hold tens of thousands. Each character occupies one square em (`方块字` fāngkuàizì) and is composed of strokes arranged into recurring components, one of which is the indexing radical. The vast majority are `形声` phono-semantic compounds, giving partial and unreliable sound hints; the script never marks tone.

- **Character-types summary:** Of the `六書`, the `形声` (xíngshēng) phono-semantic compound dominates the inventory (commonly cited at ~80–90%); `象形` pictograms, `指事` indicatives, and `会意` compound-indicatives together account for most of the rest of the high-frequency basic characters from which phono-semantics are built.
- **Polyphony note:** `多音字` (duōyīnzì) — characters with more than one reading — must be resolved by word, context, and convention (`行` xíng/háng, `重` zhòng/chóng, `长`/`長` cháng/zhǎng, `都` dōu/dū, `还`/`還` hái/huán, `觉`/`覺` jué/jiào). This is the Mandarin analog of resolving a kanji's on/kun readings, though far less pervasive than in Japanese.
- **Structural note:** Most characters are `形声` (xíngshēng): a SEMANTIC radical (`部首`) hints at the meaning domain while a PHONETIC component hints at the sound — e.g. characters containing `青` qīng often read qīng/qíng (`清` `晴` `请`/`請` `情` `蜻`), and characters with `工` gōng often read gōng/jiāng/hóng (`功` `攻` `红`/`紅` `江` `项`/`項`). The hint is partial, never tonal, and frequently eroded by sound change; it applies to the on-reading equivalent only and never to meaning.
- **Two script tiers:** The same character generally exists in two standardized GLYPH FORMS: `繁體字` (fántǐzì, TRADITIONAL — Taiwan, Hong Kong, Macau, much of the diaspora) and `简体字` (jiǎntǐzì, SIMPLIFIED — mainland China, Singapore, Malaysia). The two forms are the same character of the same reading and meaning, drawn differently; many characters were left untouched by simplification and are identical in both (`人` `山` `水` `好` `你` `我` `不` `是` `都` the same in both systems).
- **Unicode:** CJK Unified Ideographs `U+4E00`–`U+9FFF`, with Extension A (`U+3400`–`U+4DBF`) and Extensions B–I in the Supplementary Ideographic Plane (`U+20000`–`U+3FFFF`), plus CJK Compatibility Ideographs (`U+F900`–`U+FAFF`). Kangxi Radicals occupy `U+2F00`–`U+2FDF` and the CJK Radicals Supplement `U+2E80`–`U+2EFF`; both simplified and traditional glyphs are unified in the same blocks (form selection is by font/locale or variation selectors, not separate codepoints, except where a true variant is separately encoded).

### Simplified vs Traditional

The PRC's character SIMPLIFICATION reform (`汉字简化` hànzì jiǎnhuà), promulgated in the 1956 `方案` and the 1964/1986 `简化字总表` (Complete List of Simplified Characters, ~2,235 simplified characters), reduced stroke counts to raise literacy. The reform produced SIMPLIFIED forms (`简体字`) now standard on the mainland and in Singapore/Malaysia, alongside the unchanged TRADITIONAL forms (`繁體字`) retained in Taiwan, Hong Kong, and Macau. The two systems encode the SAME language with the SAME readings and meanings; only the glyph shapes (and a handful of merged codepoints) differ.

#### Simplification methods

| Method | Description | Examples (Traditional → Simplified) |
|---|---|---|
| structural simplification of components | Replacing a complex component with a simpler standardized one, often reused across many characters. | `言` → `讠` (speech): `說`→`说` shuō, `話`→`话` huà, `語`→`语` yǔ · `金` → `钅` (metal): `銅`→`铜` tóng, `鐵`→`铁` tiě, `錢`→`钱` qián · `門` → `门` (gate): `們`→`们` men, `問`→`问` wèn, `間`→`间` jiān · `馬` → `马` (horse): `媽`→`妈` mā, `嗎`→`吗` ma, `罵`→`骂` mà |
| adopting cursive / `草书` forms as print | Regularizing a long-standing handwritten cursive abbreviation into the printed form. | `書`→`书` shū, `東`→`东` dōng, `車`→`车` chē, `長`→`长` cháng, `為`→`为` wèi |
| retaining a distinctive part | Keeping only a characteristic portion of the full character. | `飛`→`飞` fēi, `聲`→`声` shēng, `醫`→`医` yī, `廠`→`厂` chǎng, `習`→`习` xí |
| reviving an older / variant simpler form | Restoring an ancient or vulgar variant that was simpler than the standard traditional form. | `雲`→`云` yún (`云` was the original; `雨` was added later), `從`→`从` cóng, `塵`→`尘` chén, `眾`→`众` zhòng |
| new phono-semantic re-formation | Coining a simpler `形声` character with the same reading. | `驚`→`惊` jīng (`忄` + `京` jīng), `護`→`护` hù, `億`→`亿` yì, `藝`→`艺` yì |

#### One-to-many merges

Some simplifications MERGED several distinct traditional characters into ONE simplified glyph (because the traditional forms were homophonous or near-homophonous). This makes SIMPLIFIED→TRADITIONAL conversion AMBIGUOUS: one simplified character maps to several traditional characters chosen by word/meaning. TRADITIONAL→SIMPLIFIED is comparatively (though not perfectly) deterministic.

| Simplified | Traditional candidates | Disambiguation by word |
|---|---|---|
| `发` | `發` fā 'emit/develop' OR `髮` fà 'hair' | `理发`/`理髮` lǐfà 'haircut' uses `髮`; `发展`/`發展` fāzhǎn 'develop' uses `發` |
| `干` | `干` gān 'dry/relate-to' OR `乾` gān 'dry' OR `幹` gàn 'do/trunk' | `饼干`/`餅乾` bǐnggān 'biscuit' = `乾`; `干部`/`幹部` gànbù 'cadre' = `幹`; `干涉` gānshè 'interfere' = `干` |
| `里` | `里` lǐ 'inside/li (unit)' OR `裏`/`裡` lǐ 'inside' | `这里`/`這裡` zhèlǐ 'here' uses `裡`/`裏`; `里` alone is the village/distance unit |
| `面` | `面` miàn 'face/side' OR `麵` miàn 'noodles/flour' | `面条`/`麵條` miàntiáo 'noodles' uses `麵` |
| `后` | `后` hòu 'queen/empress' OR `後` hòu 'behind/after' | `皇后` huánghòu 'empress' = `后`; `以后`/`以後` yǐhòu 'after' = `後` |
| `几` | `几` jī 'small table' OR `幾` jǐ 'how many/several' | `几乎`/`幾乎` jīhū 'almost'; `几个`/`幾個` jǐ ge 'a few' |

#### Regional usage

| Glyph tier | Where official | Companion transcription |
|---|---|---|
| SIMPLIFIED `简体字` | `中国大陆` (mainland China), `新加坡` (Singapore), `马来西亚` (Malaysia) | Pinyin |
| TRADITIONAL `繁體字` | `台湾` (Taiwan), `香港` (Hong Kong), `澳门` (Macau), large parts of the overseas Chinese community | Zhuyin (Taiwan) |

**Conversion note:** Conversion is MOSTLY-BUT-NOT-FULLY deterministic and is handled by tools such as OpenCC (`开放中文转换` / `開放中文轉換`). TRADITIONAL→SIMPLIFIED is largely a one-way table; SIMPLIFIED→TRADITIONAL must resolve the one-to-many merges (`发`, `干`, `里`, `面`, `后`, `几`, `钟`/`鐘`·`鍾`, `历`/`歷`·`曆`, `系`/`係`·`繫`) by word-level context, and also handle region-specific vocabulary and glyph preferences (Taiwan vs Hong Kong traditional standards differ in some characters). This is exactly why the Peshitta keeps both Hanzi tiers as downstream lookups off the toneless phonetic spine rather than deriving one mechanically from the other.

### Pinyin (汉语拼音)

Hanyu Pinyin (`汉语拼音`, Hànyǔ Pīnyīn) is the official PRC romanization (adopted 1958, ISO 7098), the international standard for transcribing Mandarin and the PRIMARY phonetic system of this guide. It is SHALLOW and PHONEMIC: each syllable is spelled as INITIAL + FINAL + TONE, with a near-mechanical map to the IPA. It uses the 26 Latin letters (v is used only for the ü of typing/loanwords; ê and ü add diacritics) plus four tone diacritics. The Peshitta's phonetic spine is the TONELESS form of Pinyin (initials + finals, no tone marks).

#### Spelling rules

| Rule | Description | Examples |
|---|---|---|
| j q x (+ y) + i/ü drop the umlaut | After j, q, x (and y), the vowel ü is written as plain u because ü never contrasts with u there. After n and l, the umlaut is KEPT because it contrasts. | `居` jū = /tɕy˥/ (written `ju`, not `jü`); `去` qù = /tɕʰy˥˩/; `女` nǚ = /ny˨˩˦/ (umlaut kept; cf. `努` nǔ /nu˨˩˦/); `绿`/`綠` lǜ = /ly˥˩/ (cf. `路` lù /lu˥˩/) |
| zero-initial syllables: i→y, u→w, ü→yu | When a final beginning with the glide i/u/ü has NO initial consonant, the spelling adds y/w (or yu) to mark the syllable boundary: i→yi, in→yin, ing→ying, ie→ye, iao→yao; u→wu, uo→wo, uang→wang; ü→yu, üe→yue, üan→yuan, ün→yun. | `一` yī (final i); `雨` yǔ (final ü → yu); `我` wǒ (final uo → wo); `王` wáng (final uang → wang); `月` yuè (final üe → yue) |
| abbreviated finals iou→iu, uei→ui, uen→un | After an initial consonant, the triphthong/medial finals iou, uei, and uen lose their middle vowel in spelling (the dropped vowel still surfaces phonetically, esp. under T3). | `六` liù = l + iou = /ljou˥˩/; `对`/`對` duì = d + uei = /twei˥˩/; `论`/`論` lùn = l + uen = /lwən˥˩/ |
| apical (buzzing) vowel written -i | After z c s and zh ch sh r, the letter i does NOT spell /i/ but the syllabic apical vowel: [ɹ̩] after z/c/s, [ɻ̩] after zh/ch/sh/r. It is purely a spelling convention reusing the letter i. | `字` zì = /tsɹ̩˥˩/ (NOT /tsi/); `四` sì = /sɹ̩˥˩/; `知` zhī = /ʈʂɻ̩˥/; `日` rì = /ʐɻ̩˥˩/ |
| syllable-divider apostrophe | An apostrophe `'` separates syllables where the join would otherwise be ambiguous, especially before a syllable starting with a, o, or e. | `西安` Xī'ān (Xi + an, 2 syllables) ≠ `仙` xiān (1 syllable); `天安门`/`天安門` Tiān'ānmén; `平安` píng'ān 'safe' |
| erhua (`儿化`/`兒化`) -r suffix | The rhotacizing suffix `儿`/`兒` is written -r appended to the syllable and rhotacizes the final ([ɚ]/[ɻ] coloring), often restructuring or deleting the rime. Common in Beijing/Putonghua, rare in Taiwan Guoyu. | `花儿`/`花兒` huār 'flower' = hua + r; `一点儿`/`一點兒` yìdiǎnr 'a little'; `这儿`/`這兒` zhèr 'here'; `玩儿`/`玩兒` wánr 'to play' |

#### Tone diacritics

Tone is marked by a diacritic over the MAIN vowel of the final. The standard placement rule: put the mark on a/e if present; else on o (in ou); else on the LAST of i/u; over i the mark replaces the dot (ī í ǐ ì). The neutral tone is UNMARKED (sometimes a leading dot in dictionaries).

| Tone | Name | Pitch | Diacritic | Examples |
|---|---|---|---|---|
| T1 | `阴平`/`陰平` | high level ˥ (55) | macron ◌̄ | mā `妈`/`媽` 'mother'; tiān `天` 'sky'; shū `书`/`書` 'book' |
| T2 | `阳平`/`陽平` | rising ˧˥ (35) | acute ◌́ | má `麻` 'hemp'; rén `人` 'person'; guó `国`/`國` 'country' |
| T3 | `上声`/`上聲` | low-dipping ˨˩˦ (214) | caron ◌̌ | mǎ `马`/`馬` 'horse'; nǐ `你` 'you'; hǎo `好` 'good' |
| T4 | `去声`/`去聲` | high falling ˥˩ (51) | grave ◌̀ | mà `骂`/`罵` 'scold'; shì `是` 'to be'; dà `大` 'big' |
| neutral | `轻声`/`輕聲` | short, context pitch | (none) | ma `吗`/`嗎` (question particle); de `的` (possessive); le `了` (aspect) |

**Placement examples:**

| Spelling | Why |
|---|---|
| hǎo | mark on a |
| duì | no a/e, no o → mark the last of iu, i.e. i |
| liù | no a/e/o → mark u |
| guó | mark on o, the main vowel |
| xuě `雪` | mark on e |

**Unicode note (Pinyin tone vowels):**

| Vowel | T1 (macron) | T2 (acute) | T3 (caron) | T4 (grave) |
|---|---|---|---|---|
| a | ā `U+0101` | á `U+00E1` | ǎ `U+01CE` | à `U+00E0` |
| e | ē `U+0113` | é `U+00E9` | ě `U+011B` | è `U+00E8` |
| i | ī `U+012B` | í `U+00ED` | ǐ `U+01D0` | ì `U+00EC` |
| o | ō `U+014D` | ó `U+00F3` | ǒ `U+01D2` | ò `U+00F2` |
| u | ū `U+016B` | ú `U+00FA` | ǔ `U+01D4` | ù `U+00F9` |
| ü | ǖ `U+01D6` | ǘ `U+01D8` | ǚ `U+01DA` | ǜ `U+01DC` |

Bare ü = `U+00FC`.

### Zhuyin / Bopomofo (注音符号 / 注音符號)

Zhuyin (popularly Bopomofo, after its first four symbols `ㄅㄆㄇㄈ` bo-po-mo-fo) is Taiwan's standard PHONETIC alphabet, introduced in 1918 and used pervasively in primary education, dictionaries, and IME input. It comprises 37 SYMBOLS — 21 initials + 16 medials/finals (rimes) — derived from fragments of ancient Chinese characters, plus tone marks. Like Pinyin it is SHALLOW and PHONEMIC, spelling each syllable as initial(+medial)+final, written left-to-right or top-to-bottom alongside the Hanzi. It is a transparent transcode of the same syllable inventory; the Peshitta's Zhuyin tier is generated from the toneless Pinyin spine.

**Structure:** A syllable is written as up to three symbols: an INITIAL (`声母` symbol, e.g. `ㄅ` b, `ㄓ` zh), an optional MEDIAL glide (`ㄧ` i/y, `ㄨ` u/w, `ㄩ` ü/yu), and a FINAL/rime (`ㄚ` a, `ㄢ` an, `ㄤ` ang, …). Zero-initial syllables begin with the medial or final directly (no y/w device is needed, unlike Pinyin). The apical 'buzzing' vowel after `ㄓㄔㄕㄖ` / `ㄗㄘㄙ` is written with NO separate vowel symbol (the initial stands alone), unlike Pinyin's -i.

#### Symbol inventory (37 symbols)

**Initials (21):**

| Zhuyin | Pinyin | IPA | Zhuyin | Pinyin | IPA | Zhuyin | Pinyin | IPA |
|---|---|---|---|---|---|---|---|---|
| `ㄅ` | b | /p/ | `ㄆ` | p | /pʰ/ | `ㄇ` | m | /m/ |
| `ㄈ` | f | /f/ | `ㄉ` | d | /t/ | `ㄊ` | t | /tʰ/ |
| `ㄋ` | n | /n/ | `ㄌ` | l | /l/ | `ㄍ` | g | /k/ |
| `ㄎ` | k | /kʰ/ | `ㄏ` | h | /x/ | `ㄐ` | j | /tɕ/ |
| `ㄑ` | q | /tɕʰ/ | `ㄒ` | x | /ɕ/ | `ㄓ` | zh | /ʈʂ/ |
| `ㄔ` | ch | /ʈʂʰ/ | `ㄕ` | sh | /ʂ/ | `ㄖ` | r | /ʐ~ɻ/ |
| `ㄗ` | z | /ts/ | `ㄘ` | c | /tsʰ/ | `ㄙ` | s | /s/ |

**Medials (3):**

| Zhuyin | Pinyin | IPA |
|---|---|---|
| `ㄧ` | i / y | /j/ |
| `ㄨ` | u / w | /w/ |
| `ㄩ` | ü / yu | /ɥ/ |

**Finals / rimes (13):**

| Zhuyin | Pinyin | IPA | Zhuyin | Pinyin | IPA |
|---|---|---|---|---|---|
| `ㄚ` | a | /a/ | `ㄛ` | o | /o/ |
| `ㄜ` | e | /ɤ/ | `ㄝ` | ê | /ɛ/ |
| `ㄞ` | ai | /ai/ | `ㄟ` | ei | /ei/ |
| `ㄠ` | ao | /au/ | `ㄡ` | ou | /ou/ |
| `ㄢ` | an | /an/ | `ㄣ` | en | /ən/ |
| `ㄤ` | ang | /aŋ/ | `ㄥ` | eng | /əŋ/ |
| `ㄦ` | er | /ɚ/ | | | |

#### Tone marks

Tone is written with small marks placed beside/above the syllable. T1 is UNMARKED (the default), and the NEUTRAL tone is marked with a leading dot `˙` ABOVE the syllable — the REVERSE of Pinyin, where T1 is marked and neutral is bare.

| Tone | Mark | Codepoint | Example |
|---|---|---|---|
| T1 | (none) | — | `ㄇㄚ` = mā `妈`/`媽` |
| T2 | `ˊ` | `U+02CA` | `ㄇㄚˊ` = má `麻` |
| T3 | `ˇ` | `U+02C7` | `ㄇㄚˇ` = mǎ `马`/`馬` |
| T4 | `ˋ` | `U+02CB` | `ㄇㄚˋ` = mà `骂`/`罵` |
| neutral | `˙` (placed before/above) | `U+02D9` | `˙ㄇㄚ` = ma `吗`/`嗎` |

#### Zhuyin examples

| Word | Pinyin | Zhuyin | Note |
|---|---|---|---|
| `你好` | nǐ hǎo | `ㄋㄧˇ ㄏㄠˇ` | |
| `中文` | zhōngwén | `ㄓㄨㄥ ㄨㄣˊ` | |
| `謝謝`/`谢谢` | xièxie | `ㄒㄧㄝˋ ㄒㄧㄝ˙` | second syllable neutral |
| `學`/`学` | xué | `ㄒㄩㄝˊ` | medial `ㄩ` ü |

**Unicode:** Bopomofo block `U+3100`–`U+312F` (the 37 standard symbols), with Bopomofo Extended `U+31A0`–`U+31BF` (for Minnan/Hakka). Tone marks use spacing modifier letters: `ˊ` `U+02CA`, `ˇ` `U+02C7`, `ˋ` `U+02CB`, `˙` `U+02D9` (T1 unmarked).

### Wade–Giles & Other Romanizations

Older and alternative romanizations remain visible in names, place-names, and pre-1980s scholarship. WADE–GILES (`威妥玛拼音`, 1859/1892) was the dominant English-language system before Pinyin; it marks ASPIRATION with an apostrophe/spiritus (p vs p', t vs t', k vs k', ch vs ch') and uses hs-, ts-/tz-, j (=Pinyin r), and the umlauted ü, with tones as superscript numbers. It survives in fossilized spellings (Peking = Běijīng, Taipei = Táiběi, Tsingtao = Qīngdǎo, Kungfu = gōngfu, Mao Tse-tung = Máo Zédōng, Chiang Kai-shek). GWOYEU ROMATZYH (`国语罗马字`/`國語羅馬字`, 1928) ingeniously spells TONE into the letters themselves (no diacritics) but is complex and little used. The Yale system and Tongyong Pinyin (`台湾` 2002–2008) are further variants. Hanyu Pinyin has superseded all of these for Mandarin transcription, and is the basis of this guide.

| Pinyin | Wade–Giles | Note |
|---|---|---|
| b / p | p / p' | Pinyin uses a plain-vs-extra letter pair (b/p, both voiceless) for the UNASPIRATED/ASPIRATED contrast /p/ vs /pʰ/; Wade–Giles marks the same aspiration contrast with an apostrophe (p vs p'). Neither system encodes voicing — Mandarin has no voicing contrast. |
| d / t | t / t' | tao `道` = Wade tao; t'ao `桃` = Pinyin táo. |
| g / k | k / k' | Kungfu (Wade) = gōngfu (Pinyin). |
| j / q | ch / ch' | before i/ü; Wade ch overlaps with zh/ch territory, disambiguated by the following vowel. |
| zh / ch | ch / ch' | before a/o/e/u; same Wade ch/ch' as j/q, hence ambiguous without the rime. |
| x | hs | Hsinhua = Xīnhuá; hsi = xi. |
| z / c | ts / ts' (tz / tz' before -u) | Tsingtao = Qīngdǎo; tzŭ = zì (WG breve ŭ for the apical vowel). |
| r | j | jen = rén `人`; jih = rì `日`. |
| you / yan | yu / yen | Peking-spelling-era artifacts; Pinyin regularized the finals. |

### Pinyin ↔ Zhuyin ↔ IPA Correspondence

Correspondence of the toneless syllable building blocks across the two phonemic systems and the IPA: Pinyin spelling ↔ Zhuyin symbol ↔ IPA, for initials, medials, and representative finals. Both systems map near-mechanically to the IPA; tone is added separately. This table is the engine behind transcoding the Peshitta's toneless Pinyin spine into the Zhuyin tier.

#### Initials

| Pinyin | Zhuyin | IPA | Example |
|---|---|---|---|
| b | `ㄅ` | /p/ | `爸` bà `ㄅㄚˋ` |
| p | `ㄆ` | /pʰ/ | `怕` pà `ㄆㄚˋ` |
| m | `ㄇ` | /m/ | `妈`/`媽` mā `ㄇㄚ` |
| f | `ㄈ` | /f/ | `发`/`發` fā `ㄈㄚ` |
| d | `ㄉ` | /t/ | `大` dà `ㄉㄚˋ` |
| t | `ㄊ` | /tʰ/ | `他` tā `ㄊㄚ` |
| n | `ㄋ` | /n/ | `你` nǐ `ㄋㄧˇ` |
| l | `ㄌ` | /l/ | `来`/`來` lái `ㄌㄞˊ` |
| g | `ㄍ` | /k/ | `高` gāo `ㄍㄠ` |
| k | `ㄎ` | /kʰ/ | `口` kǒu `ㄎㄡˇ` |
| h | `ㄏ` | /x/ | `好` hǎo `ㄏㄠˇ` |
| j | `ㄐ` | /tɕ/ | `鸡`/`雞` jī `ㄐㄧ` |
| q | `ㄑ` | /tɕʰ/ | `七` qī `ㄑㄧ` |
| x | `ㄒ` | /ɕ/ | `西` xī `ㄒㄧ` |
| zh | `ㄓ` | /ʈʂ/ | `中` zhōng `ㄓㄨㄥ` |
| ch | `ㄔ` | /ʈʂʰ/ | `吃` chī `ㄔ` |
| sh | `ㄕ` | /ʂ/ | `是` shì `ㄕˋ` |
| r | `ㄖ` | /ʐ~ɻ/ | `日` rì `ㄖˋ` |
| z | `ㄗ` | /ts/ | `字` zì `ㄗˋ` |
| c | `ㄘ` | /tsʰ/ | `次` cì `ㄘˋ` |
| s | `ㄙ` | /s/ | `四` sì `ㄙˋ` |

#### Medials

| Pinyin | Zhuyin | IPA | Example |
|---|---|---|---|
| i (y-) | `ㄧ` | /j/ | `天` tiān `ㄊㄧㄢ` |
| u (w-) | `ㄨ` | /w/ | `国`/`國` guó `ㄍㄨㄛˊ` |
| ü (yu-) | `ㄩ` | /ɥ/ | `月` yuè `ㄩㄝˋ` |

#### Finals

| Pinyin | Zhuyin | IPA | Example |
|---|---|---|---|
| a | `ㄚ` | /a/ | `啊` a `ㄚ` |
| o | `ㄛ` | /o/ | `我` wǒ `ㄨㄛˇ` |
| e | `ㄜ` | /ɤ/ | `饿`/`餓` è `ㄜˋ` |
| ê | `ㄝ` | /ɛ/ | `诶` ê `ㄝ` (rare standalone) |
| ai | `ㄞ` | /ai/ | `爱`/`愛` ài `ㄞˋ` |
| ei | `ㄟ` | /ei/ | `黑` hēi `ㄏㄟ` |
| ao | `ㄠ` | /au/ | `好` hǎo `ㄏㄠˇ` |
| ou | `ㄡ` | /ou/ | `口` kǒu `ㄎㄡˇ` |
| an | `ㄢ` | /an/ | `安` ān `ㄢ` |
| en | `ㄣ` | /ən/ | `很` hěn `ㄏㄣˇ` |
| ang | `ㄤ` | /aŋ/ | `忙` máng `ㄇㄤˊ` |
| eng | `ㄥ` | /əŋ/ | `冷` lěng `ㄌㄥˇ` |
| er | `ㄦ` | /ɚ/ | `二` èr `ㄦˋ` |
| i (apical, after z/c/s zh/ch/sh/r) | (no symbol; initial stands alone) | [ɹ̩] / [ɻ̩] | `字` zì `ㄗˋ`, `知` zhī `ㄓ` |
| ong | `ㄨㄥ` | /ʊŋ/ | `中` zhōng `ㄓㄨㄥ` |
| in | `ㄧㄣ` | /in/ | `心` xīn `ㄒㄧㄣ` |
| ing | `ㄧㄥ` | /iŋ/ | `明` míng `ㄇㄧㄥˊ` |
| ün | `ㄩㄣ` | /yn/ | `云`/`雲` yún `ㄩㄣˊ` |

### Sample Radicals

A sample of common `部首` (bùshǒu, radicals) from the 214 Kangxi set, with their meaning domain, bound combining form where applicable, and example characters (simplified / traditional) showing the radical's semantic hint. The radical narrows meaning; it never spells the sound.

| Radical | Meaning domain | Examples (Simplified / Traditional) |
|---|---|---|
| `水` / `氵` | water/liquid | `河` hé river, `海` hǎi sea, `酒` jiǔ wine, `汉`/`漢` hàn (the Han / Chinese) |
| `火` / `灬` | fire/heat | `烧`/`燒` shāo burn, `热`/`熱` rè hot, `灯`/`燈` dēng lamp, `烤` kǎo roast |
| `木` | tree/wood | `林` lín forest, `树`/`樹` shù tree, `桌` zhuō table, `桥`/`橋` qiáo bridge |
| `金` / `钅` (`釒`) | metal/gold | `银`/`銀` yín silver, `钢`/`鋼` gāng steel, `钟`/`鐘` zhōng bell/clock, `针`/`針` zhēn needle |
| `人` / `亻` | person | `你` nǐ you, `他` tā he, `住` zhù live, `信` xìn letter/trust |
| `口` | mouth/opening/speech | `吃` chī eat, `唱` chàng sing, `叫` jiào call, `和` hé and |
| `心` / `忄` | heart/mind/emotion | `想` xiǎng think, `爱`/`愛` ài love, `怕` pà fear, `忙` máng busy |
| `手` / `扌` | hand/action | `打` dǎ hit, `拿` ná hold, `找` zhǎo seek, `提` tí lift |
| `言` / `讠` | speech/word | `说`/`說` shuō speak, `话`/`話` huà speech, `语`/`語` yǔ language, `谢`/`謝` xiè thank |
| `女` | woman/female | `妈`/`媽` mā mother, `好` hǎo good, `姐` jiě elder sister, `她` tā she |
| `日` | sun/day | `明` míng bright, `时`/`時` shí time, `早` zǎo early, `晚` wǎn late |
| `艹` (`艸`) | grass/plant | `花` huā flower, `草` cǎo grass, `茶` chá tea, `药`/`藥` yào medicine |
| `辶` (`辵`) | movement/road | `这`/`這` zhè this, `进`/`進` jìn enter (from `走` base), `过`/`過` guò pass, `道` dào way |
| `贝` / `貝` | shell/money/value | `买`/`買` mǎi buy, `贵`/`貴` guì expensive, `财`/`財` cái wealth, `贸`/`貿` mào trade |

### Reader Tiers (toneless by design)

The Chinese Peshitta ships SIX companion reader tiers; this orthography section underpins the four CHINESE-derived tiers. Because Mandarin has a small, fixed syllable inventory ((C)(G)V(C) + tone, no consonant clusters, codas only /n ŋ/ + er), Aramaic source forms are first mapped onto the legal toneless Mandarin syllable spine, then transcoded into the script tiers.

| # | Tier | Description |
|---|---|---|
| 1 | Scholarly | language-neutral Latin transliteration of the Aramaic |
| 2 | Pretty | simplified language-neutral Latin |
| 3 | Toneless Pinyin | the deterministic phonetic spine — initials + finals, NO tone marks; the output of the Pinyin spelling rules in this section |
| 4 | Zhuyin / Bopomofo | `注音符号` — a mechanical transcode of the toneless Pinyin spine via the Pinyin↔Zhuyin table |
| 5 | Hanzi — SIMPLIFIED | `简体字` — a downstream transcription-character lookup, Putonghua standard |
| 6 | Hanzi — TRADITIONAL | `繁體字` — the same lookup in traditional glyphs, Guoyu standard |

**Toneless note:** The reader tiers are TONELESS BY DESIGN because the Peshitta source IPA carries NO tone, and Pinyin/Zhuyin can spell a syllable with the tone marks omitted. The two Hanzi tiers, however, UNAVOIDABLY impose a citation tone per character (a character is inseparable from its lexical tone) — this is an ARTIFACT of using a real-language script, not a feature of the toneless source. Tones are fully documented for the LANGUAGE elsewhere in this guide; only the reader tiers are toneless.

**Epenthesis note:** Because Mandarin forbids consonant clusters and all codas except /n ŋ/ (and er), an Aramaic cluster or coda must be broken up into legal syllables by inserting an epenthetic vowel and choosing the nearest licit initial/final — e.g. an Aramaic 'shl-' onset is split across two syllables (sh… + …l…), and a final like '-t' or '-m' becomes its own CV syllable. The specific vowel choices and syllable splits are governed by the rules detailed in the syllable-structure and connected-speech sections; the result is a legal toneless Pinyin string that then drives the Zhuyin and Hanzi tiers.

### Notes

- Hanzi (`汉字`/`漢字`) are LOGOGRAPHIC and morphosyllabic: one character ≈ one syllable ≈ one morpheme, encoding MEANING directly and giving at most a partial, unreliable phonetic hint. They are DEEPLY NON-PHONEMIC and mark NO tone — you cannot reliably read aloud an unfamiliar character.
- Of the `六書` (liùshū) six character types, `形声`/`形聲` (xíngshēng) phono-semantic compounds dominate (~80–90%): a semantic RADICAL (`部首`) hints at meaning and a PHONETIC component hints at sound (`清`/`晴`/`请`/`情` all qīng/qíng from `青`). The hint is partial (may match initial, final, both, or none), never tonal, and frequently eroded by sound change (`他` tā, `地` dì, `池` chí all from `也` yě).
- Two GLYPH tiers: `简体字` (jiǎntǐzì, SIMPLIFIED — PRC/Singapore) and `繁體字` (fántǐzì, TRADITIONAL — Taiwan/HK/Macau). The 1956–64 PRC reform produced ~2,235 simplified characters by component simplification, cursive adoption, part-retention, and re-formation; many characters are unchanged in both (`人` `山` `水` `好` `你` `是`).
- SIMPLIFIED→TRADITIONAL conversion is MOSTLY-BUT-NOT-FULLY deterministic because some simplifications MERGED several traditional characters into one (`发`=`發`/`髮`, `干`=`乾`/`幹`/`干`, `里`=`裏`/`裡`/`里`, `面`=`麵`/`面`, `后`=`後`/`后`, `几`=`幾`/`几`); the right traditional form is chosen by word context. TRADITIONAL→SIMPLIFIED is largely a one-way table. Tools like OpenCC handle this with word-level disambiguation.
- PINYIN (`汉语拼音`, official PRC 1958) and ZHUYIN (`注音符号`, Taiwan, 37 symbols `ㄅㄆㄇㄈ`…) are SHALLOW and PHONEMIC: each spells a syllable as initial(+medial)+final+tone with a near-mechanical IPA map. They are the opposite of Hanzi — reading them aloud is a lookup. The Peshitta's phonetic spine is TONELESS Pinyin; Zhuyin is a transcode of it.
- Pinyin spelling conventions to know: ü→u after j/q/x/y (ju qu xu yu) but kept after n/l (nü lü); zero-initial i→yi, u→wu, ü→yu; abbreviated finals iou→iu, uei→ui, uen→un; apical -i ([ɹ̩]/[ɻ̩]) after z/c/s and zh/ch/sh/r; the syllable-divider apostrophe (Xī'ān ≠ xiān); erhua -r (`花儿` huār).
- TONE is marked by diacritic in Pinyin (ā á ǎ à; neutral unmarked) and by mark in Zhuyin (T1 unmarked, ˊ ˇ ˋ, neutral ˙). Pinyin placement: mark a/e, else o, else the last of i/u. Hanzi marks no tone at all — the citation tone the Hanzi reader tiers carry is an artifact of using real characters, not a source feature.
- Older romanizations survive in fixed names: WADE–GILES marks aspiration with an apostrophe (p/p', t/t', k/k', ch/ch'), uses hs- (=x), ts-/tz- (=z/c), j (=r) — Peking, Tsingtao, Kungfu, Chiang Kai-shek. Gwoyeu Romatzyh spells tone into the letters. Hanyu Pinyin has superseded all of these and is this guide's basis.
- Both reference standards share the SAME phonemic system and the SAME toneless syllable spellings; `普通话` Pǔtōnghuà (PRC, simplified, Pinyin) and `國語` Guóyǔ (Taiwan, traditional, Zhuyin) differ in CHARACTER SET, default TRANSCRIPTION, erhua/de-retroflexion/neutral-tone frequency, and a few lexical readings (`垃圾` lājī~lèsè, `和` hé~hàn) — never in the spelling that keys the reader tiers.
- Unicode: CJK Unified Ideographs `U+4E00`–`U+9FFF` (+ Ext A `U+3400`–`U+4DBF`, Ext B+ `U+20000`+, Compatibility `U+F900`–`U+FAFF`); Bopomofo `U+3100`–`U+312F` (+ Extended `U+31A0`–`U+31BF`); Kangxi Radicals `U+2F00`–`U+2FDF`; CJK Radicals Supplement `U+2E80`–`U+2EFF`; Pinyin uses Latin with precomposed/combining tone vowels (ā `U+0101`, ǎ `U+01CE`, etc.) and the Zhuyin tone marks ˊ ˇ ˋ ˙.

## Connected Speech & Tone Sandhi

The boundary processes of connected (running) speech in Standard Mandarin (`标准汉语` / `標準漢語`), organised around its signature mechanism: TONE INTERACTION (`变调` *biàndiào*, tone sandhi) and a set of tone-bearing function-word and morpheme alternations, rather than the segmental, schwa-centred vowel reduction that drives English connected speech. This is the Mandarin analog of the English guide's `weak_forms_and_connected_speech` slot and the Japanese guide's `connected_speech_and_sandhi` slot, but the central mechanism differs sharply from English. English reshapes word boundaries by REDUCING unstressed function words to a schwa-centred "weak form"; Mandarin has NO weak forms, NO schwa, and essentially NO contrastive vowel reduction. What changes across a Mandarin boundary in running speech is overwhelmingly TONE:

1. the obligatory and productive sandhi rules — third-tone sandhi (T3+T3 → T2+T3) and its "half-third" lowering, plus the lexically specific sandhi of `一` *yī* and `不` *bù* — that recompute the citation tones of adjacent syllables;
2. the NEUTRAL TONE (`轻声`/`輕聲` *qīngshēng*), a short, toneless, pitch-from-context realisation of grammatical particles, reduplicants, and certain suffixes, which is the nearest Mandarin counterpart to an English unstressed weak syllable;
3. ERHUA (`儿化`/`兒化`), the rhotic suffix `-儿` *-r* that fuses with and restructures the preceding rime at a morpheme boundary; and
4. genuinely fast-speech, register-graded phenomena — syllable fusion and contraction (`这样`→`酱` *zhèyàng*→*jiàng*, `不用`→`甭` *búyòng*→*béng*), neutral-toning of more syllables, and the role of sentence-final particles (`的 了 吗 呢 啊 吧 啦`) that carry intonation and discourse meaning at the utterance edge.

Because the orthography is LOGOGRAPHIC (each `汉字`/`漢字` spells a tone-bearing morpheme-syllable in its CITATION tone), the gap between the written character string and the surface IPA+tone is bridged almost entirely by these tonal recomputations — the segments stay put; the tones move.

**Applies to:** Spontaneous and fluent connected speech in both reference standards. The OBLIGATORY tonal sandhi (third-tone sandhi T3+T3→T2+T3, the half-third before non-T3 tones, and the contextual sandhi of `一` and `不`) is not optional fast-speech reduction and not register-bound: it is automatic Mandarin phonology and surfaces already at careful, formal, read-aloud, and even slow citation-of-a-phrase tempo — wherever the tonal environment is met. Pinyin orthography conventionally writes the UNDERLYING citation tones (`你好` is spelled `nǐ hǎo` even though it is said `ní hǎo`), so the sandhi must be applied by the reader; only a few teaching materials write the surface result. The NEUTRAL TONE is partly lexical (`吗 了 的` are always neutral) and partly register-graded (some disyllables optionally neutral-tone their second syllable more in fast/casual speech). ERHUA is largely lexical and dialect-bound (robust in Beijing `普通话`; sparse in Taiwan `國語`). The genuinely PHONETIC / fast-speech layer — extra neutral-toning, syllable fusion and contraction (`这样`→`酱`, `不用`→`甭`, `知道`→`zhīdao` reduced), and the heavier reliance on final particles — is gradient and rate/register-dependent in the English manner: it increases with speed and informality and recedes in slow, emphatic, hyper-articulate speech. Crucially, even at the fastest rate, a full Mandarin vowel does not reduce to schwa or lose its quality the way an English weak-form vowel does; what a syllable can do is lose its TONE (become neutral), have its tone RECOMPUTED by sandhi, or, in casual contraction, FUSE with a neighbour into a single new syllable.

### Reference Standards

| Standard | Name | Characters | Romanisation / Pedagogy | Section-specific behaviour |
|---|---|---|---|---|
| **Putonghua** | `普通话` (*Pǔtōnghuà*), PRC Standard Mandarin on a Beijing phonological base | SIMPLIFIED | Hanyu Pinyin | The default for all surface IPA + tone-value notation here. Has robust ERHUA (`儿化`), a full neutral-tone (`轻声`) inventory, and applies third-tone, `一`, and `不` sandhi as described. Tone letters follow Chao's 5-point scale (T1 ˥ 55, T2 ˧˥ 35, T3 ˨˩˦ 214, T4 ˥˩ 51). |
| **Guoyu** | `國語` (*Guóyǔ*), Taiwan Standard Mandarin | TRADITIONAL | Zhuyin/Bopomofo (`注音符號`) for pedagogy | Shares the SAME phonemic and tonal system and the SAME obligatory third-tone / `一` / `不` sandhi, but differs in this section's domain in three ways: (1) ERHUA is largely ABSENT (`花儿` is usually just `花` *huā*; `一点儿` → `一點` *yìdiǎn*); (2) the NEUTRAL TONE is used LESS — many syllables Beijing neutral-tones keep a full citation tone in Taiwan (e.g. `知道` *zhīdào* with a full T4 `道` vs Beijing *zhīdao*; `東西` *dōngxī* 'thing' often *dōngxi* in both but with weaker neutralisation in Taiwan); (3) some lexical tone differences feed sandhi differently (e.g. `期` *qí* vs *qī*, `企` *qì* vs *qǐ*, `攜`/`携` *xī* vs *xié*), and the half-third tendency is similar. The underlying toneless spelling is identical; the divergences are surface tonal/erhua realisations. |

**No-reduction note:** There is NO schwa and essentially NO English-style vowel-reduction weak-form system in Mandarin — the action is TONAL, not segmental. Mandarin function words (the structural particles `的 了 吗 呢 吧 啊 着 过 地 得`; `和` *hé* 'and', `在` *zài*, `把` *bǎ*, `被` *bèi*, `给` *gěi*, `跟` *gēn*, `对` *duì*, etc.) are NOT pronounced with reduced vowels; their vowels keep full quality. What distinguishes their connected-speech form from a stressed lexical form is the loss or recomputation of TONE: the high-frequency grammatical particles surface in the NEUTRAL TONE (`轻声` *qīngshēng*) — short, unstressed, with no inherent pitch target, its actual pitch determined by the preceding tone (low after T1/T2/T4-onset contexts, slightly higher after T3) and its vowel kept full but brief. This neutral-tone behaviour is the closest Mandarin parallel to an English unstressed weak syllable, but it is a TONE phenomenon, not a vowel-quality reduction: `妈妈` *māma*, `吗` *ma*, `了` *le*, `的` *de*, `子` *zi*, `头` *tou* keep [a ə ɤ i ou] qualities, merely toneless and short. The two genuine analogs to the English strong↔weak alternation are therefore (a) the TONE SANDHI rules that change a syllable's surface contour from its citation value (T3→T2 before T3; `一`/`不` shifting tone by environment), and (b) the citation↔neutral-tone and fast-speech FUSION choices (`这样`→`酱`, `不用`→`甭`, `知道`→`zhīdao`), which change tone and syllable count, not vowel quality. The only segmental drift in fast speech is incidental (slight centralisation of an already-short neutral-tone vowel, allophonic coda lenition) — never the systematic schwa-collapse of English.

### Boundary Phenomena

The seven connected-speech phenomena fall into the categories below. They are documented one per subsection: definition, ordered rules, IPA/sandhi notation, and a sample-word table (showing BOTH simplified & traditional, underlying vs surface Pinyin, and IPA with full tone letters).

| # | Phenomenon | Category |
|---|---|---|
| 1 | `第三声变调` (third-tone sandhi, T3+T3 → T2+T3) | obligatory tone sandhi |
| 2 | `半三声` (half-third tone, T3 before a non-T3 tone) | obligatory tone sandhi |
| 3 | `一` *yī* `变调` (sandhi of `一` 'one') | lexical tone sandhi |
| 4 | `不` *bù* `变调` (sandhi of `不` 'not') | lexical tone sandhi |
| 5 | `轻声` (neutral tone in running speech) | neutral tone |
| 6 | `儿化` (erhua — rhotic `-儿` `-r` suffix) | rhotacisation |
| 7 | `快速语流的音节融合・缩约` (fast-speech syllable fusion & contraction) | contraction |
| — | `句末语气词` (sentence-final particles & utterance-edge phenomena) | final particles |

#### 1. `第三声变调` — Third-Tone Sandhi (T3+T3 → T2+T3)

**Category:** obligatory tone sandhi

The single most characteristic Mandarin connected-speech process. When a third tone (T3, citation 214, low-dipping) is immediately followed by ANOTHER third tone, the FIRST T3 changes to a rising tone identical to T2 (35): T3 + T3 → T2 + T3. The change is obligatory and automatic at every tempo, but Pinyin orthography writes the underlying T3 diacritics, so the reader must apply it: `你好` is spelled `nǐ hǎo` (ǎ ǎ) yet pronounced `ní hǎo` (T2 T3). It applies across word and phrase boundaries, not only inside words, and it is purely tonal — the segments and vowels are unchanged.

**Rules:**

1. **Core rule:** a non-final T3 immediately before another T3 becomes T2 (35).
2. **Domain/grouping in longer strings:** when three or more T3 syllables are adjacent, the application depends on PROSODIC grouping (foot/phrase structure), and more than one parse is often possible. For a `[σσ]σ` left-branching group, sandhi applies within the first foot then across: `我很好` *wǒ hěn hǎo* can be (wǒ hěn)(hǎo) → *wó hén hǎo*, with both leading T3s raised; a right-branching `很[勇敢]` (hěn)(yónggǎn) raises only where each T3+T3 pair meets → *hěn yóng gǎn* with the medial T3 raised.
3. The output T2 from sandhi behaves like a lexical T2 and can itself feed nothing further (T2 is not a sandhi trigger).
4. Independent of, and applied before, the `一`/`不` rules and neutral-toning.
5. A T3 followed by a NEUTRAL-tone syllable that is underlyingly T3 (e.g. `想想` *xiǎngxiang*) typically also shows the T2 raising on the first syllable.

**Sandhi notation:** `T3 → T2 / __ T3` (Chao: `214 → 35 / __ 214`); long strings parsed by prosodic foot before application.

| Simplified | Traditional | Pinyin (underlying) | Pinyin (surface) | IPA | Note |
|---|---|---|---|---|---|
| `你好` | `你好` | `nǐ hǎo` | `ní hǎo` | [ni˧˥ xau˨˩˦] | 'hello' — first T3 `你` *nǐ* raises to T2 before T3 `好` *hǎo*; the textbook case of T3+T3→T2+T3; spelled `nǐ hǎo` but said `ní hǎo`. |
| `很好` | `很好` | `hěn hǎo` | `hén hǎo` | [xən˧˥ xau˨˩˦] | 'very good' — `很` *hěn* → T2 before `好` *hǎo*; same rule across a degree-adverb + adjective boundary. |
| `我也想` | `我也想` | `wǒ yě xiǎng` | `wó yé xiǎng` | [wo˧˥ je˧˥ ɕjaŋ˨˩˦] | 'I also want (to)' — a three-T3 string; under the common left-grouping (wǒ yě)(xiǎng) both leading T3s raise to T2, only the final `想` keeps T3; alternative parses possible, but the final T3 never raises. |
| `好懂` | `好懂` | `hǎo dǒng` | `háo dǒng` | [xau˧˥ tʊŋ˨˩˦] | 'easy to understand' — `好` *hǎo* → T2 before `懂` *dǒng*; the sandhi crosses the adverb+verb boundary inside the phrase. |
| `买水果` | `買水果` | `mǎi shuǐguǒ` | `mǎi shuíguǒ` | [mai˨˩˦ ʂwei˧˥ kwo˨˩˦] | 'buy fruit' — within `水果` *shuǐguǒ* the first T3 `水` *shuǐ* raises to T2 before `果` *guǒ*; the verb `买` *mǎi* stays a full/half T3 (next syllable `水` is T2 after sandhi, no further raising). |

#### 2. `半三声` — Half-Third Tone (T3 before a non-T3 tone)

**Category:** obligatory tone sandhi

When a third tone is NOT phrase-final and is followed by a tone OTHER than T3 (i.e. before T1, T2, T4, or a neutral tone), it does not realise its full dipping-then-rising 214 contour. Instead the rise is dropped and only the low falling portion is produced: a low [21] "half-third" (`半上` *bànshǎng*). The full 214 surfaces only in isolation or phrase-finally; in running speech most non-final T3s are this half-third. Like full T3 sandhi this is automatic and tonal, with the segments unchanged; Pinyin still writes ǎ.

**Rules:**

1. T3 → [21] (low-falling, no final rise) / `__ {T1, T2, T4, neutral}`.
2. T3 → [214] (full dip-rise) / `__ pause` or phrase-finally (citation form).
3. T3 → [35] (=T2) / `__ T3` (the full third-tone sandhi above takes precedence in that environment).
4. So the realisation of an underlying T3 is three-way conditioned: full 214 finally, 35 before T3, and 21 (half-third) before everything else. The half-third is the statistically commonest realisation of T3 in connected speech.

**Sandhi notation:** `T3 → [21] / __ {˥, ˧˥, ˥˩, neutral}`; `T3 → [214] / __ ##`; `T3 → [35] / __ [214]`.

| Simplified | Traditional | Pinyin (underlying) | Pinyin (surface) | IPA | Note |
|---|---|---|---|---|---|
| `北京` | `北京` | `Běijīng` | `Běijīng` | [pei˨˩ tɕiŋ˥] | 'Beijing' — `北` *běi* (T3) before `京` *jīng* (T1) is a half-third [21], a low fall with no rise; the spelling keeps ě. |
| `美国` | `美國` | `Měiguó` | `Měiguó` | [mei˨˩ kwo˧˥] | 'America' — `美` *měi* (T3) before `国` *guó* (T2) → half-third [21]; the following T2 is unaffected. |
| `请坐` | `請坐` | `qǐng zuò` | `qǐng zuò` | [tɕʰiŋ˨˩ tswo˥˩] | 'please sit' — `请` *qǐng* (T3) before `坐` *zuò* (T4) → half-third [21] low fall; contrast with full 214 if `请` were said alone. |
| `你们` | `你們` | `nǐmen` | `nǐmen` | [ni˨˩ mən] | 'you (plural)' — `你` *nǐ* (T3) before the NEUTRAL-tone suffix `们` *men* → half-third [21]; the neutral `们` takes a low pitch after it. |
| `好的` | `好的` | `hǎo de` | `hǎo de` | [xau˨˩ tə] | 'okay / alright' — `好` *hǎo* (T3) before neutral `的` *de* → half-third [21]; shows the half-third also applies before a neutral tone, not only before T1/T2/T4. |

#### 3. `一` *yī* `变调` — Tone Sandhi of `一` 'one'

**Category:** lexical tone sandhi

The numeral `一` *yī* 'one' has the citation tone T1 (55) but changes its tone by the tone of the FOLLOWING syllable in connected speech: it becomes T4 (51) before T1, T2, or T3, and T2 (35) before T4. It keeps citation T1 only in isolation, when said as a pure number/digit (counting, ordinals `第一`, phone numbers, dates `一月`), or phrase-finally. This is a lexically specified sandhi tied to this one morpheme; it is obligatory and the spelling in many texts shows the surface result (`yì` / `yí`), unlike third-tone sandhi which is usually written underlyingly.

**Rules:**

1. `一` → T4 (*yì*, 51) / `__ {T1, T2, T3}`.
2. `一` → T2 (*yí*, 35) / `__ T4` (including a T4 that has itself come from sandhi).
3. `一` → T1 (*yī*, 55) in isolation, in pure counting/enumeration, in ordinals (`第一` *dìyī*), and in fixed citation uses (`一二三` *yī èr sān*).
4. When `一` is sandwiched between two reduplicated verbs/measure words it neutralises (`看一看` *kàn yi kàn* → neutral `一` *yi*).
5. Interacts with `不` and third-tone sandhi but is computed on `一`'s own following-syllable environment.

**Sandhi notation:** `一` /i/ : `T1(55) → T4(51) / __ {˥, ˧˥, ˨˩˦}`; `T1(55) → T2(35) / __ ˥˩`; `T1(55)` elsewhere (counting/final).

| Simplified | Traditional | Pinyin (underlying) | Pinyin (surface) | IPA | Note |
|---|---|---|---|---|---|
| `一天` | `一天` | `yī tiān` | `yì tiān` | [i˥˩ tʰjɛn˥] | 'one day' — `一` before T1 `天` *tiān* → T4 (*yì*); the falling 51 contour. |
| `一年` | `一年` | `yī nián` | `yì nián` | [i˥˩ njɛn˧˥] | 'one year' — `一` before T2 `年` *nián* → T4 (*yì*). |
| `一起` | `一起` | `yī qǐ` | `yì qǐ` | [i˥˩ tɕʰi˨˩˦] | 'together' — `一` before T3 `起` *qǐ* → T4 (*yì*); the following T3 keeps its (here phrase-final) full 214. |
| `一个` | `一個` | `yī gè` | `yí ge` | [i˧˥ kə] | 'one (of something)' — `一` before T4 `个` *gè* → T2 (*yí*); note the measure word `个` here is commonly further reduced to neutral tone (*ge*). |
| `看一看` | `看一看` | `kàn yī kàn` | `kàn yi kàn` | [kʰan˥˩ i kʰan˥˩] | 'take a look' — in the V-`一`-V reduplication the medial `一` NEUTRALISES (*yi*, toneless) rather than taking T2/T4; a special reduplication context. |

#### 4. `不` *bù* `变调` — Tone Sandhi of `不` 'not'

**Category:** lexical tone sandhi

The negator `不` *bù* has citation tone T4 (51) but changes to T2 (35) when immediately followed by another T4 syllable: `不` → *bú* before T4. Before T1, T2, or T3 it keeps T4 (*bù*). Like `一`-sandhi this is a lexically specified, obligatory alternation on a single morpheme, and the surface tone is conventionally written (`bú` vs `bù`). In addition, when `不` stands BETWEEN two repeated syllables (a potential-complement infix, V-`不`-C), it neutralises to a toneless `不` *bu*.

**Rules:**

1. `不` → T2 (*bú*, 35) / `__ T4` (including a sandhi-derived T4).
2. `不` → T4 (*bù*, 51) / `__ {T1, T2, T3}` and phrase-finally / in isolation.
3. `不` → neutral (*bu*) when infixed in a potential complement: `吃不饱` *chī bu bǎo*, `看不见` *kàn bu jiàn*, `来不及` *lái bu jí*.
4. Interacts with `一` and third-tone sandhi but is computed on `不`'s own following environment; e.g. in `不一定` *bù yīdìng* the `不` sees the (T1→here) `一` and the `一` separately undergoes its own sandhi.

**Sandhi notation:** `不` /pu/ : `T4(51) → T2(35) / __ ˥˩`; `T4(51)` elsewhere; → neutral / V_C potential-complement infix.

| Simplified | Traditional | Pinyin (underlying) | Pinyin (surface) | IPA | Note |
|---|---|---|---|---|---|
| `不是` | `不是` | `bù shì` | `bú shì` | [pu˧˥ ʂʐ̩˥˩] | 'is not / no' — `不` before T4 `是` *shì* → T2 (*bú*); the canonical `不`-sandhi case. |
| `不要` | `不要` | `bù yào` | `bú yào` | [pu˧˥ jau˥˩] | "don't / do not want" — `不` before T4 `要` *yào* → T2 (*bú*); cf. the regional fast-speech stacked-graph fusion `不要`→`嫑` *biáo* in the contraction entry (the separate morpheme `别` *bié* 'don't' is NOT a fusion of `不要`). |
| `不好` | `不好` | `bù hǎo` | `bù hǎo` | [pu˥˩ xau˨˩˦] | 'not good' — `不` before T3 `好` *hǎo* keeps T4 (*bù*); no change before non-T4. |
| `不来` | `不來` | `bù lái` | `bù lái` | [pu˥˩ lai˧˥] | 'not coming' — `不` before T2 `来` *lái* keeps T4 (*bù*). |
| `看不见` | `看不見` | `kàn bù jiàn` | `kàn bu jiàn` | [kʰan˥˩ pu tɕjɛn˥˩] | 'cannot see' — the infixed `不` in the potential complement V-`不`-C NEUTRALISES to toneless *bu* rather than taking T2 before the T4 `见` *jiàn*. |

#### 5. `轻声` — Neutral Tone in Running Speech

**Category:** neutral tone

The neutral tone (`轻声`/`輕聲` *qīngshēng*) is a short, unstressed, toneless realisation of a syllable: it has NO inherent pitch target and NO lexical tone contour; its actual pitch is determined by the PRECEDING tone, and its vowel is kept (full quality) but brief, sometimes slightly centralised. It is the nearest Mandarin counterpart to an English unstressed weak syllable — but it is a TONE phenomenon (loss of tone), not a vowel reduction. Some words are LEXICALLY neutral (the grammatical particles `的 了 吗 呢 着 过 子 们`; reduplicants), while others are register/dialect graded (more neutral-toning in Beijing fast speech, less in Taiwan).

**Pitch realisation by preceding tone:**

| Preceding tone | Preceding contour | Neutral-tone pitch | Chao value |
|---|---|---|---|
| T1 | 55 (high level) | low | [2] |
| T2 | 35 (rising) | mid | [3] |
| T3 | 21 (half-third) | half-high (slight rise) | [4] |
| T4 | 51 (falling) | low | [1] |

**Rules:**

1. Pitch realisation by preceding tone (see table above): after T1 → low [2]; after T2 → mid [3]; after T3 (half-third 21) → half-high [4]; after T4 → low [1].
2. **ALWAYS neutral:** structural particles `的` *de* / `地` *de* / `得` *de*, aspect `了` *le* / `着` *zhe* / `过` *guo*, question `吗` *ma* / `呢` *ne* / `吧` *ba*, plural `们` *men*, the diminutive/nominal suffixes `子` *zi* / `头` *tou*, and the second half of many reduplicated kin terms (`妈妈` *māma*, `爸爸` *bàba*, `哥哥` *gēge*).
3. **Lexically neutral in disyllables:** `东西` *dōngxi* 'thing', `朋友` *péngyou*, `喜欢` *xǐhuan*, `知道` *zhīdào*→*zhīdao*, `时候` *shíhou*.
4. **Reduplicated verbs/adjectives** neutral-tone the second copy: `看看` *kànkan*, `慢慢` *mànman(r)*.
5. The neutral-tone vowel keeps quality but is short; it never becomes schwa-only the way an English weak vowel does.
6. Taiwan `國語` retains full citation tones for many of the disyllabic cases in (3).

**Sandhi notation:** `σ → [toneless, short]`; pitch = f(preceding tone): `/T1_/` [2], `/T2_/` [3], `/T3_/` [4], `/T4_/` [1].

| Simplified | Traditional | Pinyin (underlying) | Pinyin (surface) | IPA | Note |
|---|---|---|---|---|---|
| `妈妈` | `媽媽` | `māma` | `māma` | [ma˥ ma˨] | 'mum' — reduplicated kin term; second `妈` is neutral (toneless), realised low [2] after the T1 first syllable; vowel [a] kept, just short. |
| `朋友` | `朋友` | `péngyou` | `péngyou` | [pʰəŋ˧˥ jou˧] | 'friend' — `友` is neutral (underlying T3 `友` *yǒu*), realised mid [3] after the T2 first syllable; spelled `péngyou` (no tone mark on *you*). |
| `你呢` | `你呢` | `nǐ ne` | `nǐ ne` | [ni˨˩ nə˦] | 'and you?' — the question particle `呢` *ne* is always neutral; after the half-third `你` *nǐ* [21] it is realised half-high [4]; shows the after-T3 pitch rule. |
| `看了` | `看了` | `kàn le` | `kàn le` | [kʰan˥˩ lə˩] | 'looked / (have) seen' — aspect particle `了` *le* is always neutral; after T4 `看` *kàn* [51] it is realised low [1]. |
| `东西` | `東西` | `dōngxī` | `dōngxi` | [tʊŋ˥ ɕi˨] | 'thing' (vs `dōngxī` 'east-west') — lexicalised neutral on `西`; the neutral-toned reading carries the 'thing' meaning, a tone-only minimal contrast; Beijing neutral-tones it more strongly than Taiwan. |

#### 6. `儿化` — Erhua (the rhotic suffix `-儿` `-r` at a morpheme boundary)

**Category:** rhotacisation

Erhua (`儿化`/`兒化`) is the suffixation of a rhotic `儿` *-r* (an /ɚ/-colouring, IPA [ɚ ~ ɻ]) that FUSES with the preceding rime at a morpheme boundary, rhotacising and often RESTRUCTURING that final rather than adding a separate syllable. It is written as a second character `儿` (`花儿`) but is NOT a full syllable of its own: it merges into the host's rime. Erhua is a hallmark of Beijing `普通话` (diminutive, affective, or lexically required), is sparse or absent in Taiwan `國語`, and reshapes the rime in regular ways (dropping a high-front coda, nasalising-then-rhotacising a nasal coda, inserting a schwa-glide after high vowels).

**Rules (rime restructuring on adding `-r`):**

1. Open low/back rimes simply rhotacise: `花儿` *huā+r* → [xwaɚ̯] / [xwar].
2. Coda /-i/ and /-n/ DELETE, then rhotacise: `玩儿` *wán+r* → *wár* [waɚ̯] (n dropped); `一点儿` *diǎn+r* → *diǎr* [tjaɚ̯]; `小孩儿` *hái+r* → *hár*.
3. Coda /-ng/ → nasalised rhotacised vowel: `空儿` *kòng+r* → *kòr̃* [kʰʊ̃ɚ̯].
4. High vowels /i y/ insert an [ɚ]-glide (an epenthetic schwa-r): `鸡儿` *jī+r* → *jiēr* [tɕjɚ]; `鱼儿` *yú+r* → *yúr* [yɚ].
5. Apical vowels (`zi ci si` / `zhi chi shi ri`) → the apical drops and a plain [ɚ] surfaces: `字儿` *zì+r* → [tsɚ], `事儿` *shì+r* → [ʂɚ].
6. Erhua does NOT change the host's tone; the tone rides on the rhotacised rime.
7. Lexically obligatory in some words (`这儿` *zhèr* 'here', `那儿` *nàr* 'there', `哪儿` *nǎr* 'where'), diminutive/affective elsewhere.

**Sandhi notation:** `rime + /ɚ/ → rhotacised rime [Vɚ̯ / Vɻ]`; coda {i, n} → ∅ before `-r`; coda ŋ → Ṽɚ̯; high V → Vɚ; tone preserved on the fused rime.

| Simplified | Traditional | Pinyin (underlying) | Pinyin (surface) | IPA | Note |
|---|---|---|---|---|---|
| `花儿` | `花兒` | `huā + ér` | `huār` | [xwaɚ̯˥] | 'flower' — open rime `-ua` simply rhotacises; `儿` is not a separate syllable; T1 rides on the fused rime; Taiwan `國語` would just say `花` *huā*. |
| `一点儿` | `一點兒` | `yī diǎn + ér` | `yìdiǎr` | [i˥˩ tjaɚ̯˨˩˦] | 'a little' — the `-n` coda of `点` *diǎn* DELETES before `-r`, giving *diǎr*; also shows `一`→*yì* (T4) sandhi before the (T3) `点`; Taiwan: `一點` *yìdiǎn* (no erhua). |
| `玩儿` | `玩兒` | `wán + ér` | `wár` | [waɚ̯˧˥] | 'to play / have fun' — `-n` of `玩` *wán* deletes before `-r` → *wár*; T2 preserved; one of the most frequent Beijing erhua words. |
| `这儿` | `這兒` | `zhè + ér` | `zhèr` | [ʈʂɚ˥˩] | 'here' — lexically OBLIGATORY erhua in Beijing `普通话`; the apical-ish rime of `这` *zhè* fuses to a plain rhotic [ɚ]; T4 preserved; Taiwan uses `這裡` *zhèlǐ* instead. |
| `空儿` | `空兒` | `kòng + ér` | `kòngr` | [kʰʊ̃ɚ̯˥˩] | 'free time' — the `-ng` coda becomes a NASALISED rhotacised vowel [ʊ̃ɚ̯] (the velar nasal is lost as a segment but nasalises the rime); T4 preserved. |

#### 7. `快速语流的音节融合・缩约` — Fast-Speech Syllable Fusion & Contraction

**Category:** contraction

In casual, fast speech two (occasionally three) syllables FUSE into a single new syllable, blending their segments and resolving to one tone. This is genuinely rate- and register-graded (the English-like layer of this section): the full forms are the careful/written norm, the fused forms the casual spoken variant. Some fusions are common enough to have their own conventional stacked characters (`这样`→`酱` *zhèyàng*→*jiàng*, `不用`→`甭` *búyòng*→*béng*, and the regional/Sichuanese `不要`→`嫑` *búyào*→*biáo*). NOTE: not every disyllable+single-graph pairing is a phonetic fusion — `别` *bié* 'don't' is a separate free negative-imperative morpheme, NOT a contraction of `不要` (there is no segmental path from [pu.jau] to [pjɛ]); it is listed below only to be excluded. Unlike the obligatory tone sandhi, true fusions change syllable count and segmental shape, not merely tone.

**Rules:**

1. **Demonstrative + `样`:** `这样` *zhèyàng* → `酱` *jiàng*; the [...ʈʂ...] + [...j...aŋ] collapse to a single [tɕ...aŋ] syllable. (The colloquial fusion of `怎么样`/`怎样` is usually written `咋` *zǎ*.)
2. **`不` + verb fusions written as single STACKED graphs:** `不用` *búyòng* → `甭` *béng* 'needn't' (literally `不` over `用`); the regional/Sichuanese `不要` *búyào* → `嫑` *biáo* (literally `不` over `要`). NOT a fusion: `不要` → `别` *bié* is a category error — `别` is an independent lexical negative imperative, not a phonetic contraction of `不`+`要`.
3. **High-frequency disyllables reduce the second syllable to neutral or near-zero:** `知道` *zhīdào* → *zhīdao*, `豆腐` *dòufu*, `我们` *wǒmen* → fast [wəm̩] (the one marginal place a centralised [ə]-like vowel surfaces — see note), `这个` *zhège* → *zhèige*/*jè*.
4. **`一` + measure fusions:** `一个` *yīgè* → [jak]-like fast blends.
5. The fused syllable takes ONE tone, usually inherited from the more prominent source syllable.
6. These are optional and recede entirely in careful speech, where the full disyllable returns.

**Sandhi notation:** `σ1 σ2 → σ_fused` (segments blended, one resolved tone); e.g. `这样` [ʈʂɤ˥˩.jaŋ˥˩] → `酱` [tɕjaŋ˥˩]; `不用` [pu˧˥.jʊŋ˥˩] → `甭` [pəŋ˧˥].

| Simplified | Traditional | Pinyin (underlying) | Pinyin (surface) | IPA | Note |
|---|---|---|---|---|---|
| `这样` → `酱` | `這樣` → `醬` | `zhèyàng` | `jiàng` | [tɕjaŋ˥˩] | '(like) this / in this way' — the two syllables `这样` fuse into one casual syllable conventionally written `酱` *jiàng*; T4 retained; pure fast-speech, never in careful reading. |
| `不用` → `甭` | `不用` → `甭` | `búyòng` | `béng` | [pəŋ˧˥] | 'needn't / no need' — `不用` contracts to the single morpheme-character `甭` *béng* (literally written as `不`+`用` stacked); takes T2; lexicalised fusion. |
| `不要` → `嫑` | `不要` → `嫑` | `búyào` | `biáo` | [pjau˧˥] | 'don't (do)' — a genuine STACKED-graph fusion of `不` over `要`, read *biáo*; REGIONAL / Sichuanese, NOT Standard Mandarin (`普通话`/`國語`), so used only colloquially. Contrast `别` *bié* 'don't', which is a separate lexical negative imperative and NOT a contraction of `不要`. |
| `知道` | `知道` | `zhīdào` | `zhīdao` | [ʈʂʐ̩˥ tau˨] | 'know' — the second syllable `道` reduces from full T4 `道` *dào* to NEUTRAL *dao* in fast Beijing speech; the neutral `道` takes low pitch [2] after the T1 `知` (per the after-tone rule: after T1 → [2]); Taiwan `國語` keeps the full T4 *zhīdào* — a clean Putonghua/Guoyu divergence. |
| `我们` | `我們` | `wǒmen` | `wǒm` (fast) | [wəm̩] | 'we' — in very fast speech `我们` (already `们` neutral) can compress toward a single syllable, the half-third `我` and neutral `们` blending; recovers to *wǒmen* in careful speech. **EXCEPTION FLAG:** this fast-speech fusion is the one marginal place a centralised [ə]-like vowel appears in Mandarin — it is NOT the systematic English-style schwa reduction (which Mandarin lacks), but an incidental centralisation of an already-short neutral-tone vowel under heavy compression. |

#### `句末语气词` — Sentence-Final Particles & Utterance-Edge Phenomena

**Category:** final particles

Mandarin carries much of its mood, aspect, and discourse meaning in SENTENCE-FINAL PARTICLES (`句末语气词` *jùmò yǔqìcí*): `吗` *ma* (yes/no question), `呢` *ne* (continuation/topic Q), `吧` *ba* (suggestion/softening), `啊`/`呀`/`哪` *a* (exclamation/softening), `了` *le* (change of state), `啦` *la* (=`了`+`啊`), `嘛` *ma* (obviousness). These are all NEUTRAL-toned and sit at the utterance edge, where they (a) take their pitch from the preceding tone like any neutral syllable, and (b) crucially HOST the sentence intonation, since lexical tone otherwise constrains pitch. The particle `啊` *a* additionally undergoes regular SANDHI to the final segment of the preceding syllable.

**Rules:**

1. All final particles are neutral-toned: their pitch follows the preceding tone (after-T1 low … after-T3 half-high).
2. Sentence intonation (overall rise for questions, fall for statements) is realised largely ON these toneless particles and on the global pitch register, since the body of the sentence is locked by lexical tones.
3. **`啊` *a*-sandhi** (fusion with the preceding coda/vowel): after `-i`/`-ü`/front V → `呀` *ya* [ja]; after `-u`/`-ao`/`-ou` → `哇` *wa* [wa]; after `-n` → `哪` *na* [na]; after `-ng` → [ŋa]; after apical `-i` (`zi`/`zhi`) → [ɚ/ʐa].
4. `了` + `啊` → `啦` *la*; `呢` + `啊` → `哪`/`呐` *na*; these are written fusions.
5. The particles never bear stress and never block the global intonation contour they host.
6. Taiwan `國語` uses the same particles, with `喔` *o* / `耶` *ye* more frequent and slightly fuller realisations.

**Sandhi notation:** final particle = neutral σ at edge, pitch = f(preceding tone) + global intonation; `啊` /a/ → [ja] / `_i,y`; [wa] / `_u,o`; [na] / `_n`; [ŋa] / `_ŋ`.

| Simplified | Traditional | Pinyin (underlying) | Pinyin (surface) | IPA | Note |
|---|---|---|---|---|---|
| `你好吗` | `你好嗎` | `nǐ hǎo ma` | `ní hǎo ma` | [ni˧˥ xau˨˩˦ ma˦] | 'how are you?' — third-tone sandhi `你`→*ní*, full T3 on `好` (now phrase-internal before neutral, often half-third), and the neutral question particle `吗` *ma* hosting the question intonation; *ma* takes half-high [4] after the T3. |
| `走吧` | `走吧` | `zǒu ba` | `zǒu ba` | [tsou˨˩ pa˦] | 'let's go' — suggestion particle `吧` *ba* is neutral; after the half-third `走` *zǒu* [21] it is realised half-high [4]; *ba* softens the imperative and carries the gentle falling intonation. |
| `好啊` | `好啊` | `hǎo a` | `hǎo wa` | [xau˨˩˦ wa˦] | 'sure! / okay!' — the exclamatory `啊` *a* undergoes a-sandhi after the `-o`/`-u` offglide of `好` *hǎo*, surfacing as `哇` *wa* [wa]; neutral, half-high [4] after T3. |
| `是啊` | `是啊` | `shì a` | `shì ya` | [ʂʐ̩˥˩ ja˩] | "yeah / that's right" — `啊` after the apical/`-i` context of `是` *shì* surfaces as `呀` *ya* [ja]; neutral, low [1] after the T4. |
| `下雨了` | `下雨了` | `xià yǔ le` | `xià yǔ le` | [ɕja˥˩ y˨˩˦ lə˦] | "it's raining (now)" — change-of-state `了` *le* is neutral and utterance-final; after the (here final-ish) T3 `雨` *yǔ* it takes half-high [4]; `了` carries the 'new situation' meaning and the statement's falling edge. |

### Process Classification

Mandarin connected-speech phenomena split into three tiers by how obligatory and tempo-bound they are.

| Tier | Processes | Obligatoriness & tempo | Locus | Pinyin spelling |
|---|---|---|---|---|
| **1. Obligatory tone sandhi** | third-tone sandhi (T3+T3→T2+T3), the half-third (T3→21 before non-T3), the lexical sandhi of `一` and `不` | automatic at EVERY tempo, including careful citation of a phrase | purely tonal (segments unchanged) | usually written UNDERLYINGLY in Pinyin, so the reader recomputes it |
| **2. Neutral tone & erhua** | lexical-neutral particles (`吗 了 的`), obligatory erhua (`这儿`), plus register-graded extra neutral-toning and diminutive erhua | partly fixed, partly scaling with informality; far heavier in Beijing `普通话` than in Taiwan `國語` | tonal / rime-internal | neutral marked by absence of a tone mark; erhua by `-r`/`儿` |
| **3. Fast-speech layer** | syllable fusion/contraction (`酱`, `甭`, regional `嫑`), extra neutralisation (`知道`→*zhīdao*), final-particle reliance & `啊`-sandhi | gradient and rate/register-dependent (the English manner); recedes to full forms in slow, emphatic speech | tonal + syllabic | full forms in the careful/written norm |

Across all three tiers the constant is that the changes are TONAL and syllabic, never the schwa-style vowel-quality reduction of English.

### Process Ordering

The tonal computations apply in a definable order on a tone string. First the half-third / full-third distinction is set by environment, then third-tone sandhi (T3+T3→T2+T3) raises non-final T3s, with longer T3 strings parsed by PROSODIC FOOT before raising (so `我也想` / `我很好` admit more than one grouping but never raise the final T3). The `一` and `不` sandhi are computed on their own following-syllable environment, interleaved with third-tone sandhi where they meet. Neutral-toning is assigned to lexical/grammatical neutral syllables and then the neutral syllable's pitch is read off the (possibly already sandhi-ed) preceding tone. Erhua fuses at the rime without altering tone. Finally, in casual speech, fusion/contraction can collapse adjacent syllables and the sentence-final particle hosts the global intonation.

**General cascade:**

> half-third / full-third assignment → third-tone & `一`/`不` sandhi (foot-parsed) → neutral-tone assignment + pitch realisation → erhua rime fusion → (fast speech) syllable fusion → intonation on the final particle.

### Rate & Register

The obligatory tone sandhi (third-tone, half-third, `一`, `不`) does NOT scale with rate — it is present in slow careful speech as much as in fast speech, and is what a learner must apply to read Pinyin aloud correctly. By contrast the neutral-tone density, erhua frequency, syllable fusions (`酱`, `甭`), and final-particle reductions ARE gradient: they increase with speech rate and informality and recede in slow, emphatic, hyper-articulate, or read-aloud-for-clarity delivery, where full citation tones and full disyllables are restored. Dictionaries and Pinyin orthography list the underlying citation tones; the IPA of natural running speech requires the sandhi (always) and the neutral/erhua/fusion processes (in casual register) to sound native. Note again: no amount of speed reduces a Mandarin full vowel to schwa — speed adds neutral-toning and fusion, not English-style vowel reduction.

### Dialect Variation (`普通话` vs `國語`)

Putonghua (`普通话`) vs Guoyu (`國語`) diverge mainly in the non-obligatory tiers.

| Feature | `普通话` Putonghua (Beijing base) | `國語` Guoyu (Taiwan) |
|---|---|---|
| **Erhua** | robust and lexically required (`这儿` *zhèr*, `一点儿` *yìdiǎnr*, `玩儿` *wár*) | largely ABSENT (`這裡` *zhèlǐ*, `一點` *yìdiǎn*, `玩` *wán*) |
| **Neutral tone** | used more — many disyllables neutral-toned (`知道` *zhīdao*; many `子`-suffixed words) | used less — many keep full citation tones (`知道` *zhīdào*; `星期`) |
| **Obligatory T3 / `一` / `不` sandhi** | applied identically | applied identically |
| **Lexical tone differences feeding sandhi** | `期` *qī*, `企` *qǐ*, `携` *xié*, `和` 'and' *hé* | `期` *qí*, `企` *qì*, `携` *xī*, `和` 'and' *hàn* (feeds sandhi with the local citation tone, but the rules are unchanged) |
| **Final particles** | shared inventory | shared, with slightly fuller realisations and `喔` *o* / `耶` *ye* more often |

### Contrast with English

The contrast with the English `weak_forms_and_connected_speech` section is the key point: Mandarin has NO English-style weak forms and NO vowel reduction. English collapses unstressed function words to a schwa-centred weak form (/ə/, syllabic consonants, cliticisation) and reshapes boundaries by segmental assimilation, elision, linking-r, and yod-coalescence. Mandarin keeps every vowel at full quality and instead recomputes TONE: the obligatory third-tone / `一` / `不` sandhi (the productive core), the neutral tone (the nearest analog to an English unstressed weak syllable, but a loss of TONE not vowel quality), erhua rime-fusion, and casual syllable fusion. Where English has rhoticity-driven linking-r/intrusive-r/flapping, Mandarin's only rhotic boundary process is erhua (a rime-internal /ɚ/-suffix, not a between-word liaison). Where English elides /t d h/ and reduces schwa, Mandarin fuses whole syllables (`这样`→`酱`) and neutral-tones particles — operating on the suprasegmental tier, not the segmental one. In one phrase `你好吗` the work is all tonal (`你`→*ní* by T3 sandhi, neutral `吗` hosting question intonation), with not a single vowel reduced — the mirror image of an English phrase like "how're you" where the action is all segmental reduction.

### Cross-Reference

This section is the Mandarin counterpart to the English guide's `weak_forms_and_connected_speech` (file `English/english_pronunciation_guide.json`) and the Japanese guide's `connected_speech_and_sandhi` (file `Japanese/japanese_pronunciation_guide.json`). UNLIKE the English weak forms — gradient, optional, schwa-centred vowel reductions of function words — the Mandarin core (third-tone sandhi, half-third, `一`/`不` sandhi) is OBLIGATORY, purely TONAL, and present at every tempo; only the neutral-tone density, erhua, syllable fusion, and final-particle reductions are gradient and register-bound in the English manner. Like Japanese (`連声`/`連濁` rendaku/renjō are lexical and surface at every tempo) Mandarin keeps full vowel quality and acts above the segment — but where Japanese acts on consonants (voicing, gemination, /N/-assimilation), Mandarin acts on TONE. Read this section together with the Mandarin guide's `tones_and_tone_system` section (the citation T1–T4 + neutral values these rules recompute), the `finals_and_rimes` section (the rime structures erhua restructures and the apical `-i` vowels), the `initials` section (the `j`/`q`/`x` and `zh`/`ch`/`sh` series that feed `啊`-sandhi and fusion), and the `orthography_and_scripts` section (Pinyin's underlying-tone spelling, Zhuyin tone marks, and the simplified/traditional Hanzi that spell each syllable in its citation tone). Where the English guide opposes GA vs RP (chiefly rhoticity) and the Japanese guide opposes Standard Tokyo vs Kansai, the Mandarin guide opposes `普通话` Putonghua (simplified, Pinyin, erhua-rich, more neutral tone) vs `國語` Guoyu (traditional, Zhuyin, little erhua, fewer neutral tones).

**Companion materials:** the six Chinese Peshitta reader tiers (`Chinese/Peshita_Chinese/Scholarly/`, `Chinese/Peshita_Chinese/Pretty/`, `Chinese/Peshita_Chinese/Pinyin/`, `Chinese/Peshita_Chinese/Zhuyin/`, `Chinese/Peshita_Chinese/Hanzi_Simplified/`, `Chinese/Peshita_Chinese/Hanzi_Traditional/`) and the prose guide `Chinese/chinese_pronunciation_guide.md`.

> **CRITICAL — reader tiers are TONELESS:** the Peshitta reader tiers are TONELESS by design — the source IPA carries no tone, so the toneless-Pinyin tier is the deterministic phonetic spine and the Zhuyin tier transcodes it without tone marks; the Hanzi tiers unavoidably impose a per-character citation tone (an artifact of using tone-bearing characters, not a source feature). The rich tone sandhi documented here describes the LANGUAGE; it does NOT apply to the toneless reader tiers, where there are no tones to sandhi.

---

*Section compiled by Shin.*

## Sample Words in IPA

35 illustrative Mandarin Chinese words/morphemes transcribed in IPA for the reference standard — **Standard Mandarin** (标准汉语 / 標準漢語) in its two co-standard realizations, **普通话** *Pǔtōnghuà* (PRC, Beijing-based, **simplified** characters, Hanyu Pinyin) and **國語** *Guóyǔ* (Taiwan, **traditional** characters, Zhuyin/Bopomofo) — modeled on the English guide's GA/RP columns, the Japanese guide's Tokyo/Kansai columns, and the Peshitta guide's parallel Eastern/Western tradition columns. Because Mandarin is a **TONAL**, analytic, monosyllabic-morpheme, **logographic** language (not stress-timed, not pitch-accent), every entry marks tone explicitly with Chao tone letters / tone numerals on each syllable, names the tone pattern, and shows tone sandhi where it applies.

The words are chosen to exercise the full segmental system: all four initial obstruent series and their aspiration contrast (b/p 不送气/送气, d/t, g/k, z/c dental, zh/ch retroflex, j/q alveolo-palatal), the three sibilant-fricative places (s/sh/x), the rhotic initial r [ʐ~ɻ], the apical ("buzzing") vowels -i [ɹ̩] / [ɻ̩], the er/erhua rhotacized rime [ɚ] / [ɻ], the medial glides i/u/ü [j w ɥ], the diphthongs and triphthongs (ai ei ao ou / iao iou uai uei), the nasal finals (-n vs -ng), all four lexical tones plus the neutral tone (轻声), and the major connected-speech sandhi rules. Two simp≠trad pairs (`发`/`發`, `国`/`國`) make the script-tier divergence explicit.

Each entry gives the word in both `汉字` (simplified) and `漢字` (traditional), the `pinyin` (tone diacritics), the `zhuyin` (Bopomofo with tone marks), the IPA (with Chao tone letters / numerals), the tone pattern, a gloss, the phenomena it illustrates, and a detailed note. The array as a whole forms a verifiable coverage matrix for the Standard Mandarin phonological system, and maps onto the six shipped Peshitta reader tiers (Scholarly + Pretty Latin, **TONELESS** Pinyin, Zhuyin/Bopomofo, and Hanzi in Simplified and Traditional).

*Words were selected illustratively (not corpus-sliced) to guarantee complete coverage: collectively they realize all 21 initials plus the zero initial, and the full finals system — the apical vowels -i [ɹ̩] (zi ci si) and [ɻ̩] (zhi chi shi ri), the er-rime [ɚ] and erhua [ɻ], the medial glides /j w ɥ/, diphthongs (ai ei ao ou) and triphthongs (iao iou uai uei), and the nasal-coda finals -n /n/ vs -ng /ŋ/. All five tonal categories are present: T1 阴平 ˥ (55), T2 阳平 ˧˥ (35), T3 上声 ˨˩˦ (214), T4 去声 ˥˩ (51), and the neutral tone 轻声. The reference standard is shared between Pǔtōnghuà and Guóyǔ; where the two diverge on the surface (Taiwan de-retroflexion zh/ch/sh→z/c/s, little/no erhua, fewer neutral tones, and lexical tone differences) the divergence is given in the note.*

> **Reader-tier note (toneless spine).** The **LANGUAGE itself is tonal**, and every tone is rendered fully below (Chao tone letters ˥ ˧˥ ˨˩˦ ˥˩ plus the neutral tone, with parenthetical 5-point numerals). The **TONELESS Peshitta reader tiers** (the toneless Pinyin tier in particular) **strip every tone mark shown here**: that citation tone is an artifact of the per-character lookup, not a feature carried by the toneless reader spine. Tone is documented here for the language, not for the toneless tiers.

**Total sample words:** 35

### How tone is written across the tiers

Tone is **lexical and contrastive** in Mandarin — the same toneless syllable distinguishes meaning by pitch contour alone. The textbook minimal set is `妈/媽` *mā* (T1, 'mother') / `麻` *má* (T2, 'hemp') / `马/馬` *mǎ* (T3, 'horse') / `骂/罵` *mà* (T4, 'scold') / `吗/嗎` *ma* (neutral, question particle). The five categories and how each notation tier renders them:

| Category | Chao tone letter (numeral) | Pinyin mark | Zhuyin (Bopomofo) mark | Realization note |
|---|---|---|---|---|
| T1 阴平 (high-level) | `˥` (55) | `ā` (macron) | unmarked (e.g. `ㄇㄚ`) | steady high level |
| T2 阳平 (rising) | `˧˥` (35) | `á` (acute) | `ˊ` after the syllable (`ㄇㄚˊ`) | high-rising |
| T3 上声 (low-dipping) | `˨˩˦` (214) | `ǎ` (caron) | `ˇ` after the syllable (`ㄇㄚˇ`) | full dip in isolation/phrase-final; low **half-third** `˨˩` (21) before another tone |
| T4 去声 (high-falling) | `˥˩` (51) | `à` (grave) | `ˋ` after the syllable (`ㄇㄚˋ`) | sharp high-falling |
| neutral 轻声 (toneless) | short, context-set value (e.g. `·¹`–`·⁴`) | **unmarked** | `˙` written **before** the syllable (`˙ㄇㄚ`) | no inherent contour; light/short pitch set by the preceding tone |

*Each Hanzi carries one citation tone; in the toneless Peshitta reader tiers this citation tone is an unavoidable artifact of the character lookup, not a feature of the toneless source.*

### Sample Words Table

`/slashes/` = phonemic, `[brackets]` = phonetic. Both `汉字` (simplified) and `漢字` (traditional) are shown; where they are identical the cell repeats the glyph. The IPA carries Chao tone letters with parenthetical 5-point numerals.

| # | 汉字 (simp) | 漢字 (trad) | Pinyin | Zhuyin | IPA | Tone pattern | Gloss |
|---|---|---|---|---|---|---|---|
| 1 | `妈` | `媽` | `mā` | `ㄇㄚ` | /ma˥/ [ma˥] (T1, 55) | T1 阴平 high-level (55) | 'mother' (often 妈妈 *māma*) |
| 2 | `麻` | `麻` | `má` | `ㄇㄚˊ` | /ma˧˥/ [ma˧˥] (T2, 35) | T2 阳平 rising (35) | 'hemp; numb' |
| 3 | `马` | `馬` | `mǎ` | `ㄇㄚˇ` | /ma˨˩˦/ [ma˨˩˦] (T3, 214) | T3 上声 low-dipping (214) | 'horse' |
| 4 | `骂` | `罵` | `mà` | `ㄇㄚˋ` | /ma˥˩/ [ma˥˩] (T4, 51) | T4 去声 high-falling (51) | 'to scold' |
| 5 | `吗` | `嗎` | `ma` | `˙ㄇㄚ` | /ma/ [ma·] (neutral 轻声, short mid/low) | neutral 轻声 (toneless, context-set pitch) | yes/no question particle |
| 6 | `爸爸` | `爸爸` | `bàba` | `ㄅㄚˋ ˙ㄅㄚ` | /pa˥˩ pa/ [pa˥˩ pa·¹] (T4 + neutral) | T4 去声 + neutral 轻声 (reduplication) | 'dad, papa' |
| 7 | `怕` | `怕` | `pà` | `ㄆㄚˋ` | /pʰa˥˩/ [pʰa˥˩] (T4, 51) | T4 去声 high-falling (51) | 'to fear, be afraid' |
| 8 | `弟弟` | `弟弟` | `dìdi` | `ㄉㄧˋ ˙ㄉㄧ` | /ti˥˩ ti/ [ti˥˩ ti·¹] (T4 + neutral) | T4 去声 + neutral 轻声 | 'younger brother' |
| 9 | `天` | `天` | `tiān` | `ㄊㄧㄢ` | /tʰjɛn˥/ [tʰjɛn˥] (T1, 55) | T1 阴平 high-level (55) | 'sky, day' |
| 10 | `哥哥` | `哥哥` | `gēge` | `ㄍㄜ ˙ㄍㄜ` | /kɤ˥ kɤ/ [kɤ˥ kɤ·²] (T1 + neutral) | T1 阴平 + neutral 轻声 | 'older brother' |
| 11 | `看` | `看` | `kàn` | `ㄎㄢˋ` | /kʰan˥˩/ [kʰan˥˩] (T4, 51) | T4 去声 high-falling (51) | 'to look, see, read' |
| 12 | `字` | `字` | `zì` | `ㄗˋ` | /tsɹ̩˥˩/ [tsɹ̩˥˩] (T4, 51) | T4 去声 high-falling (51) | '(written) character, word' |
| 13 | `词` | `詞` | `cí` | `ㄘˊ` | /tsʰɹ̩˧˥/ [tsʰɹ̩˧˥] (T2, 35) | T2 阳平 rising (35) | 'word, term' |
| 14 | `四` | `四` | `sì` | `ㄙˋ` | /sɹ̩˥˩/ [sɹ̩˥˩] (T4, 51) | T4 去声 high-falling (51) | 'four' (4) |
| 15 | `知` | `知` | `zhī` | `ㄓ` | /ʈʂɻ̩˥/ [ʈʂɻ̩˥] (T1, 55) | T1 阴平 high-level (55) | 'to know' (知道 *zhīdào*) |
| 16 | `吃` | `吃` | `chī` | `ㄔ` | /ʈʂʰɻ̩˥/ [ʈʂʰɻ̩˥] (T1, 55) | T1 阴平 high-level (55) | 'to eat' |
| 17 | `是` | `是` | `shì` | `ㄕˋ` | /ʂɻ̩˥˩/ [ʂɻ̩˥˩] (T4, 51) | T4 去声 high-falling (51) | 'to be (am/is/are)' |
| 18 | `日` | `日` | `rì` | `ㄖˋ` | /ʐɻ̩˥˩/ [ʐɻ̩˥˩] ~ [ɻɻ̩˥˩] (T4, 51) | T4 去声 high-falling (51) | 'sun, day' |
| 19 | `鸡` | `雞` | `jī` | `ㄐㄧ` | /tɕi˥/ [tɕi˥] (T1, 55) | T1 阴平 high-level (55) | 'chicken' |
| 20 | `七` | `七` | `qī` | `ㄑㄧ` | /tɕʰi˥/ [tɕʰi˥] (T1, 55) | T1 阴平 high-level (55) | 'seven' (7) |
| 21 | `西` | `西` | `xī` | `ㄒㄧ` | /ɕi˥/ [ɕi˥] (T1, 55) | T1 阴平 high-level (55) | 'west' |
| 22 | `鱼` | `魚` | `yú` | `ㄩˊ` | /y˧˥/ [y˧˥] (T2, 35) | T2 阳平 rising (35) | 'fish' |
| 23 | `湖` | `湖` | `hú` | `ㄏㄨˊ` | /xu˧˥/ [xu˧˥] (T2, 35) | T2 阳平 rising (35) | 'lake' |
| 24 | `飞` | `飛` | `fēi` | `ㄈㄟ` | /fei̯˥/ [fei̯˥] (T1, 55) | T1 阴平 high-level (55) | 'to fly' |
| 25 | `老` | `老` | `lǎo` | `ㄌㄠˇ` | /lau̯˨˩˦/ [lau̯˨˩˦] (T3, 214) | T3 上声 low-dipping (214) | 'old' |
| 26 | `听` | `聽` | `tīng` | `ㄊㄧㄥ` | /tʰiŋ˥/ [tʰiŋ˥] (T1, 55) | T1 阴平 high-level (55) | 'to listen, hear' |
| 27 | `熊` | `熊` | `xióng` | `ㄒㄩㄥˊ` | /ɕjʊŋ˧˥/ [ɕjʊŋ˧˥] (T2, 35) | T2 阳平 rising (35) | 'bear' (animal) |
| 28 | `二` | `二` | `èr` | `ㄦˋ` | /ɚ˥˩/ [ɚ˥˩] (T4, 51) | T4 去声 high-falling (51) | 'two' (2) |
| 29 | `花儿` | `花兒` | `huār` | `ㄏㄨㄚㄦ` | /xwaɻ˥/ [xwaɻ˥] (T1, 55, erhua) | T1 阴平 high-level (55) on the rhotacized rime | 'flower' (+ diminutive 儿 -r) |
| 30 | `你好` | `你好` | `nǐ hǎo` | `ㄋㄧˇ ㄏㄠˇ` | /ni˧˥ xau̯˨˩˦/ [ni˧˥ xau̯˨˩˦] (citation T3+T3 → **sandhi** T2+T3) | T3 + T3 → T2 + T3 (third-tone sandhi) | 'hello' (lit. 'you good') |
| 31 | `一定` | `一定` | `yídìng` | `ㄧˊ ㄉㄧㄥˋ` | /i˧˥ tiŋ˥˩/ [i˧˥ tiŋ˥˩] (一 *yī* → **sandhi** *yí* before T4) | 一 *yī* (T1) → T2 before T4; 定 *dìng* T4 | 'certainly, definitely' |
| 32 | `不是` | `不是` | `búshì` | `ㄅㄨˊ ㄕˋ` | /pu˧˥ ʂɻ̩˥˩/ [pu˧˥ ʂɻ̩˥˩] (不 *bù* → **sandhi** *bú* before T4) | 不 *bù* (T4) → T2 before T4; 是 *shì* T4 | 'is not, no, incorrect' |
| 33 | `我的` | `我的` | `wǒ de` | `ㄨㄛˇ ˙ㄉㄜ` | /wo˨˩˦ tɤ/ [wo˨˩(˦) tɤ·⁴] (T3 + neutral particle 的) | T3 (half-third before neutral) + neutral 轻声 | 'my, mine' (我 'I' + possessive 的) |
| 34 | `发` | `發` | `fā` | `ㄈㄚ` | /fa˥/ [fa˥] (T1, 55) | T1 阴平 high-level (55) | 'to send out, issue, develop' (see merger note) |
| 35 | `国` | `國` | `guó` | `ㄍㄨㄛˊ` | /kwo˧˥/ [kwo˧˥] (T2, 35) | T2 阳平 rising (35) | 'country, nation' (中国 *Zhōngguó* 'China') |

### Per-word phenomena and notes

Each entry below lists the phonemic phenomena it illustrates and a detailed note (segmental coverage, aspiration vs voicing, sandhi behaviour, and 普通话/國語 surface differences). `/slashes/` = phonemic, `[brackets]` = phonetic.

#### The canonical tone minimal set: 妈 / 麻 / 马 / 骂 / 吗

The clearest demonstration that **tone alone is contrastive** in Mandarin: five entries on identical /ma/ segments differing only in tone.

**1. `妈` / `媽` `mā` `ㄇㄚ` — /ma˥/ [ma˥] (T1, 55)**
- m /m/ (bilabial nasal initial)
- a /a/ (open nucleus, the simple final -a)
- tone: T1 阴平 high-level ˥
- *Note:* First member of the canonical tone minimal set 妈/麻/马/骂/吗 (*mā/má/mǎ/mà/ma*). Shows the bilabial nasal initial m and the bare open final -a [a], with the level high T1. Same segments /ma/ as the next three entries — only the tone differs, the textbook demonstration that tone is contrastive in Mandarin. Identical in Pǔtōnghuà and Guóyǔ; `媽` is the traditional form, `妈` the simplified.

**2. `麻` / `麻` `má` `ㄇㄚˊ` — /ma˧˥/ [ma˧˥] (T2, 35)**
- m /m/
- a /a/
- tone: T2 阳平 high-rising ˧˥
- *Note:* Second member of the 妈/麻/马/骂/吗 set. The high-rising T2 ˧˥ (35) contrasts minimally with T1 妈 on identical /ma/ segments. `麻` is the same in simplified and traditional (no simplification). Zhuyin marks T2 with the post-syllable symbol `ˊ`.

**3. `马` / `馬` `mǎ` `ㄇㄚˇ` — /ma˨˩˦/ [ma˨˩˦] (T3, 214)**
- m /m/
- a /a/
- tone: T3 上声 low-dipping ˨˩˦ (full contour in isolation)
- *Note:* Third member of the 妈/麻/马/骂/吗 set. In **isolation** or phrase-finally T3 surfaces with its full low-dipping ˨˩˦ (214) contour; before another full tone it reduces to a low **half-third** [˨˩] (see 你好). `馬` (traditional) → `马` (simplified) is one of the most visibly reduced character simplifications. Zhuyin tone symbol `ˇ`.

**4. `骂` / `罵` `mà` `ㄇㄚˋ` — /ma˥˩/ [ma˥˩] (T4, 51)**
- m /m/
- a /a/
- tone: T4 去声 high-falling ˥˩
- *Note:* Fourth member of the 妈/麻/马/骂/吗 set. The sharply high-falling T4 ˥˩ (51) completes the four-way lexical tone contrast on identical /ma/. `罵` (traditional) → `骂` (simplified). Zhuyin tone symbol `ˋ`.

**5. `吗` / `嗎` `ma` `˙ㄇㄚ` — /ma/ [ma·] (neutral 轻声, short mid/low)**
- m /m/
- a /a/
- tone: **NEUTRAL** 轻声 (no lexical tone)
- *Note:* Fifth member, the **neutral-tone** member of the 妈/麻/马/骂/吗 set. As a sentence-final grammatical particle 吗 carries no lexical tone — its short, light pitch is set by the preceding syllable (e.g. 好吗? *hǎo ma*, 是吗? *shì ma*). Pinyin leaves it **unmarked**; Zhuyin writes the neutral dot `˙` **before** the syllable. `嗎` (traditional) → `吗` (simplified).

#### Aspiration contrasts (b/p, d/t, g/k) and neutral-tone reduplication

The core Mandarin obstruent distinction is **aspiration, not voicing**: each unaspirated/aspirated stop pair is exemplified minimally.

**6. `爸爸` / `爸爸` `bàba` `ㄅㄚˋ ˙ㄅㄚ` — /pa˥˩ pa/ [pa˥˩ pa·¹] (T4 + neutral)**
- b /p/ (**unaspirated** bilabial stop)
- a /a/
- tone: T4 on syllable 1; **NEUTRAL** 轻声 on reduplicated syllable 2
- neutral-tone reduplication (kin term)
- *Note:* Shows the **unaspirated** stop b = /p/ (voiceless, no aspiration — contrast aspirated p = /pʰ/ in 怕 *pà*). The reduplicated second 爸 is **neutral-toned** (a typical kin-term pattern, cf. 妈妈 *māma*, 哥哥 *gēge*): light and short, here taking a low pitch after a T4. `爸` is identical in simplified and traditional. The b/p aspiration contrast (not voicing) is the core Mandarin obstruent distinction.

**7. `怕` / `怕` `pà` `ㄆㄚˋ` — /pʰa˥˩/ [pʰa˥˩] (T4, 51)**
- p /pʰ/ (**aspirated** bilabial stop)
- a /a/
- tone: T4 去声 ˥˩
- *Note:* The **aspirated** counterpart to 爸 b /p/: p = /pʰ/ with a strong puff of air. Minimal aspiration contrast 爸 [pa] ~ 怕 [pʰa] — Mandarin's stop initials contrast by **aspiration, never by voicing**. Same in simplified and traditional. Zhuyin `ㄆ` = /pʰ/.

**8. `弟弟` / `弟弟` `dìdi` `ㄉㄧˋ ˙ㄉㄧ` — /ti˥˩ ti/ [ti˥˩ ti·¹] (T4 + neutral)**
- d /t/ (**unaspirated** alveolar stop)
- i /i/ (close front vowel as a plain final)
- tone: T4 + **NEUTRAL** on reduplication
- *Note:* Shows the **unaspirated** alveolar stop d = /t/ (contrast aspirated t = /tʰ/ in 天 *tiān*) and the plain high-front final i = [i] (NOT the apical -i of zi/zhi). The reduplicated 弟 is neutral-toned. Same character in simplified and traditional. Zhuyin `ㄉ` = /t/, `ㄧ` = /i/.

**9. `天` / `天` `tiān` `ㄊㄧㄢ` — /tʰjɛn˥/ [tʰjɛn˥] (T1, 55)**
- t /tʰ/ (**aspirated** alveolar stop)
- medial i /j/ (palatal on-glide)
- final -ian /jɛn/ (note the [ɛ] allophone before -n)
- coda -n /n/ (alveolar nasal final)
- tone: T1 阴平 ˥
- *Note:* The **aspirated** counterpart to 弟 d /t/: t = /tʰ/. Also shows the medial glide i = /j/, the front-raised nucleus in -ian (the /a/ raises to [ɛ] before the alveolar /n/ → [jɛn], not *[jan]), and the -n coda. Contrast the -n final here with the -ng final of 听 *tīng* / 行 *xíng*. Same in simplified and traditional. Zhuyin `ㄊ` = /tʰ/, `ㄧㄢ` = -ian.

**10. `哥哥` / `哥哥` `gēge` `ㄍㄜ ˙ㄍㄜ` — /kɤ˥ kɤ/ [kɤ˥ kɤ·²] (T1 + neutral)**
- g /k/ (**unaspirated** velar stop)
- e /ɤ/ (close-mid back unrounded vowel, the final -e)
- tone: T1 + **NEUTRAL** on reduplication
- *Note:* Shows the **unaspirated** velar stop g = /k/ (contrast aspirated k = /kʰ/ in 看 *kàn*) and the distinctive Mandarin final -e = [ɤ] (an unrounded back vowel, NOT [e] and NOT [ə]). The reduplicated 哥 is neutral. Same in simplified and traditional. Zhuyin `ㄍ` = /k/, `ㄜ` = /ɤ/.

**11. `看` / `看` `kàn` `ㄎㄢˋ` — /kʰan˥˩/ [kʰan˥˩] (T4, 51)**
- k /kʰ/ (**aspirated** velar stop)
- a /a/
- final -an /an/ (open nucleus before -n coda)
- coda -n /n/
- tone: T4 去声 ˥˩
- *Note:* The **aspirated** counterpart to 哥 g /k/: k = /kʰ/. Also gives the -an final [an] (plain back-ish [a] before alveolar -n) for contrast with -ang [aŋ] (帮 *bāng*) and with -ian [jɛn] (天 *tiān*). Same in simplified and traditional. Zhuyin `ㄎ` = /kʰ/.

#### The three sibilant places: dental (z/c/s), retroflex (zh/ch/sh/r), alveolo-palatal (j/q/x)

Three parallel triads contrast PLACE plus the matching apical-vowel quality. The dental and retroflex apical "-i" vowels [ɹ̩] / [ɻ̩] are *not* the true high front [i].

**12. `字` / `字` `zì` `ㄗˋ` — /tsɹ̩˥˩/ [tsɹ̩˥˩] (T4, 51)**
- z /ts/ (**unaspirated** dental affricate)
- apical final -i = [ɹ̩] (the dental "buzzing" apical vowel after z/c/s)
- tone: T4 去声 ˥˩
- *Note:* Shows the **unaspirated** dental affricate z = /ts/ AND the special **apical** final -i, which after z/c/s is NOT [i] but the syllabic dental approximant [ɹ̩] (a continuation of the [s]-place, "buzzing"). Contrast with the retroflex apical [ɻ̩] in 是 *shì* and with true [i] in 弟 *dì*. Same in simplified and traditional. Zhuyin `ㄗ` = /ts/ (the apical -i is inherent, written with no vowel letter).

**13. `词` / `詞` `cí` `ㄘˊ` — /tsʰɹ̩˧˥/ [tsʰɹ̩˧˥] (T2, 35)**
- c /tsʰ/ (**aspirated** dental affricate)
- apical final -i = [ɹ̩]
- tone: T2 阳平 ˧˥
- *Note:* The **aspirated** counterpart to 字 z /ts/: c = /tsʰ/, again with the dental apical [ɹ̩] final. The z/c aspiration pair on identical apical-vowel finals. `詞` (traditional) → `词` (simplified). Zhuyin `ㄘ` = /tsʰ/.

**14. `四` / `四` `sì` `ㄙˋ` — /sɹ̩˥˩/ [sɹ̩˥˩] (T4, 51)**
- s /s/ (dental fricative)
- apical final -i = [ɹ̩]
- tone: T4 去声 ˥˩
- *Note:* Completes the dental series z/c/s on the apical [ɹ̩] final: s = /s/. The triad 字 *zì* [tsɹ̩] / 词 *cí* [tsʰɹ̩] / 四 *sì* [sɹ̩] shows unaspirated affricate ~ aspirated affricate ~ fricative all sharing the dental apical vowel. Same in simplified and traditional. Zhuyin `ㄙ` = /s/.

**15. `知` / `知` `zhī` `ㄓ` — /ʈʂɻ̩˥/ [ʈʂɻ̩˥] (T1, 55)**
- zh /ʈʂ/ (**unaspirated retroflex** affricate)
- apical final -i = [ɻ̩] (the **retroflex** apical vowel after zh/ch/sh/r)
- tone: T1 阴平 ˥
- *Note:* Shows the **unaspirated** retroflex affricate zh = /ʈʂ/ and the **retroflex** apical final -i = [ɻ̩] (tongue-tip curled, distinct from the dental [ɹ̩] of 字 *zì*). **Taiwan Guóyǔ often DE-RETROFLEXES** zh→z, so colloquial Taiwan 知 may sound [tsɹ̩] (merging toward 资 *zī*) — a key 普通话/國語 surface difference. Same in simplified and traditional. Zhuyin `ㄓ` = /ʈʂ/.

**16. `吃` / `吃` `chī` `ㄔ` — /ʈʂʰɻ̩˥/ [ʈʂʰɻ̩˥] (T1, 55)**
- ch /ʈʂʰ/ (**aspirated retroflex** affricate)
- apical final -i = [ɻ̩]
- tone: T1 阴平 ˥
- *Note:* The **aspirated** counterpart to 知 zh /ʈʂ/: ch = /ʈʂʰ/, with the retroflex apical [ɻ̩]. The zh/ch retroflex aspiration pair. Taiwan de-retroflexion may render ch→c [tsʰ]. Same in simplified and traditional. Zhuyin `ㄔ` = /ʈʂʰ/.

**17. `是` / `是` `shì` `ㄕˋ` — /ʂɻ̩˥˩/ [ʂɻ̩˥˩] (T4, 51)**
- sh /ʂ/ (**retroflex** fricative)
- apical final -i = [ɻ̩]
- tone: T4 去声 ˥˩
- *Note:* Shows the retroflex fricative sh = /ʂ/ on the retroflex apical [ɻ̩]. The retroflex triad 知 *zhī* [ʈʂɻ̩] / 吃 *chī* [ʈʂʰɻ̩] / 是 *shì* [ʂɻ̩] parallels the dental 字/词/四 triad, the contrast being PLACE (retroflex vs dental) plus the matching apical-vowel quality. Taiwan de-retroflexion: sh→s [s]. Same in simplified and traditional. Zhuyin `ㄕ` = /ʂ/.

**18. `日` / `日` `rì` `ㄖˋ` — /ʐɻ̩˥˩/ [ʐɻ̩˥˩] ~ [ɻɻ̩˥˩] (T4, 51)**
- r /ʐ~ɻ/ (voiced retroflex fricative / approximant initial)
- apical final -i = [ɻ̩]
- tone: T4 去声 ˥˩
- *Note:* The rhotic initial r, the voiced counterpart of sh in the retroflex series, ranging [ʐ] (fricative) ~ [ɻ] (approximant) by speaker/register, here before the retroflex apical [ɻ̩]; the variant [ɻɻ̩˥˩] is an approximant onset [ɻ] over the syllabic retroflex apical [ɻ̩]. This is the **only voiced obstruent-like initial** in Mandarin (the system is otherwise an aspiration, not voicing, contrast). Taiwan Guóyǔ, where it de-retroflexes, realizes r as the dental [z] specifically (e.g. 日 may sound [zɹ̩]); this is the 普通话/國語 surface difference. Same in simplified and traditional. Zhuyin `ㄖ` = /ʐ~ɻ/.

**19. `鸡` / `雞` `jī` `ㄐㄧ` — /tɕi˥/ [tɕi˥] (T1, 55)**
- j /tɕ/ (**unaspirated alveolo-palatal** affricate)
- i /i/ (true high front vowel, conditioning j/q/x)
- tone: T1 阴平 ˥
- *Note:* Shows the **unaspirated** alveolo-palatal affricate j = /tɕ/, which occurs **only before high front i/ü** (in complementary distribution with z/zh/g). Here the final i is true [i] (NOT an apical vowel — apical -i never follows j/q/x). `雞` (traditional) → `鸡` (simplified). Zhuyin `ㄐ` = /tɕ/.

**20. `七` / `七` `qī` `ㄑㄧ` — /tɕʰi˥/ [tɕʰi˥] (T1, 55)**
- q /tɕʰ/ (**aspirated alveolo-palatal** affricate)
- i /i/
- tone: T1 阴平 ˥
- *Note:* The **aspirated** counterpart to 鸡 j /tɕ/: q = /tɕʰ/, also only before i/ü. The j/q alveolo-palatal aspiration pair on true [i]. Same in simplified and traditional. Zhuyin `ㄑ` = /tɕʰ/.

**21. `西` / `西` `xī` `ㄒㄧ` — /ɕi˥/ [ɕi˥] (T1, 55)**
- x /ɕ/ (alveolo-palatal fricative)
- i /i/
- tone: T1 阴平 ˥
- *Note:* Completes the alveolo-palatal series before i/ü: x = /ɕ/. The triad 鸡 *jī* [tɕi] / 七 *qī* [tɕʰi] / 西 *xī* [ɕi] mirrors the dental and retroflex sibilant triads but at the alveolo-palatal place. (j/q/x are in complementary distribution with z/c/s and zh/ch/sh and g/k/h, so they never minimally contrast with those before the same vowel.) Same in simplified and traditional. Zhuyin `ㄒ` = /ɕ/.

#### Vowels, fricatives, diphthongs, and nasal codas

**22. `鱼` / `魚` `yú` `ㄩˊ` — /y˧˥/ [y˧˥] (T2, 35)**
- zero initial, written yu- for ü
- ü /y/ (close front **rounded** vowel)
- tone: T2 阳平 ˧˥
- *Note:* Shows the front rounded vowel ü = /y/ (the third high vowel after i and u). With a zero initial it is spelled `yu` in pinyin (the umlaut is dropped), but the vowel is [y]. After j/q/x the dots are also dropped (居 *jū* = /tɕy/). ü also functions as the medial glide /ɥ/ (e.g. 月 *yuè* /ɥɛ/). `魚` (traditional) → `鱼` (simplified). Zhuyin `ㄩ` = /y/.

**23. `湖` / `湖` `hú` `ㄏㄨˊ` — /xu˧˥/ [xu˧˥] (T2, 35)**
- h /x/ (voiceless velar fricative)
- u /u/ (close back rounded vowel)
- tone: T2 阳平 ˧˥
- *Note:* Shows the initial h = /x/ — a velar **fricative** in Standard Mandarin (not the glottal [h] of English), often [h]~[x] in fast speech — and the plain back-rounded final u = [u]. Same in simplified and traditional. Zhuyin `ㄏ` = /x/, `ㄨ` = /u/.

**24. `飞` / `飛` `fēi` `ㄈㄟ` — /fei̯˥/ [fei̯˥] (T1, 55)**
- f /f/ (labiodental fricative)
- diphthong -ei /ei̯/
- tone: T1 阴平 ˥
- *Note:* Shows the labiodental fricative f = /f/ and the falling diphthong -ei [ei̯] (contrast -ai [ai̯] in 爱 *ài*). The off-glide is written with the non-syllabic diacritic [i̯] (a glide off the nucleus, using the backbone's vowel set /a e i o u/), NOT an English-style lax [ɪ]. `飛` (traditional) → `飞` (simplified). Zhuyin `ㄈ` = /f/, `ㄟ` = -ei.

**25. `老` / `老` `lǎo` `ㄌㄠˇ` — /lau̯˨˩˦/ [lau̯˨˩˦] (T3, 214)**
- l /l/ (lateral approximant initial)
- diphthong -ao /au̯/
- tone: T3 上声 ˨˩˦ (full contour, phrase-final)
- *Note:* Shows the lateral l = /l/ and the falling diphthong -ao [au̯] (contrast -ou [ou̯] in 都 *dōu*). The nucleus is the backbone vowel /a/ (NOT back [ɑ]) and the off-glide is the non-syllabic [u̯] (NOT English lax [ʊ]). Phrase-finally the T3 shows its full low-dipping ˨˩˦ contour. Same in simplified and traditional. Zhuyin `ㄌ` = /l/, `ㄠ` = -ao.

**26. `听` / `聽` `tīng` `ㄊㄧㄥ` — /tʰiŋ˥/ [tʰiŋ˥] (T1, 55)**
- t /tʰ/
- final -ing /iŋ/
- coda -ng /ŋ/ (velar nasal final)
- tone: T1 阴平 ˥
- *Note:* Shows the **velar** nasal coda -ng = /ŋ/, contrasting minimally-ish with the alveolar -n: -ing [iŋ] (here) vs -in [in] (心 *xīn*). The -n vs -ng coda distinction is the only Mandarin coda contrast besides er. `聽` (traditional, 22 strokes) → `听` (simplified) is a dramatic reduction. Zhuyin `ㄥ` = -ng coda (here `ㄧㄥ` = -ing).

**27. `熊` / `熊` `xióng` `ㄒㄩㄥˊ` — /ɕjʊŋ˧˥/ [ɕjʊŋ˧˥] (T2, 35)**
- x /ɕ/
- medial i /j/ + final -iong /jʊŋ/
- coda -ng /ŋ/
- tone: T2 阳平 ˧˥
- *Note:* Shows the complex final -iong = [jʊŋ] (medial glide + back nucleus + velar nasal), one of the rarer rimes, plus the velar -ng coda again. Same in simplified and traditional. Zhuyin `ㄩㄥ` here writes -iong; note the pinyin spelling 'iong' vs Zhuyin's `ㄩ`(ü)`ㄥ` reflects the rounded on-glide.

#### The er-rime and erhua (儿化)

**28. `二` / `二` `èr` `ㄦˋ` — /ɚ˥˩/ [ɚ˥˩] (T4, 51)**
- zero initial
- the er-rime /ɚ/ (rhotacized vowel, its own syllable)
- tone: T4 去声 ˥˩
- *Note:* The standalone **er-rime** = [ɚ] (a rhotacized/r-colored central vowel), the only Mandarin syllable that is a bare rhotacized vowel and the segmental basis of erhua. Contrast with erhua, where -r is a **suffix** fused onto another rime (see 花儿 *huār*). Same in simplified and traditional. Zhuyin `ㄦ` = /ɚ/.

**29. `花儿` / `花兒` `huār` `ㄏㄨㄚㄦ` — /xwaɻ˥/ [xwaɻ˥] (T1, 55, erhua)**
- h /x/
- medial u /w/ (rounded on-glide)
- **ERHUA 儿化**: suffix 儿 -r rhotacizes the rime → [xwaɻ]
- tone: T1 阴平 ˥ (the erhua suffix carries no separate tone)
- *Note:* **ERHUA 儿化**: the suffix 儿 -r fuses with the preceding rime 花 *huā* into a single rhotacized syllable [xwaɻ] — 儿 does **not** add a syllable or its own tone. Also shows the medial glide u = /w/. Erhua is characteristic of Beijing/Northern 普通话 and is **largely absent in Taiwan Guóyǔ**, where 花 would simply be *huā* [xwa] with no rhotacization. `花兒` (traditional) → `花儿` (simplified). Pinyin appends 'r'; Zhuyin appends `ㄦ`.

#### Connected-speech sandhi: third-tone, 一 yī, 不 bù, and the neutral tone

The Pinyin entries below show **citation** tone diacritics; the **surface (post-sandhi)** tone is given in the IPA and explained in the note. (The toneless reader tiers carry neither.)

**30. `你好` / `你好` `nǐ hǎo` `ㄋㄧˇ ㄏㄠˇ` — /ni˧˥ xau̯˨˩˦/ [ni˧˥ xau̯˨˩˦] (citation T3+T3 → sandhi T2+T3)**
- n /n/ (alveolar nasal initial)
- h /x/
- diphthong -ao /au̯/
- **THIRD-TONE SANDHI**: T3 + T3 → T2 + T3
- tone: surface T2 on 你, full T3 on 好
- *Note:* THE textbook **third-tone sandhi**: both 你 *nǐ* and 好 *hǎo* are citation T3 (214), but a T3 immediately before another T3 raises to T2 (35), so 你好 is pronounced *ní hǎo* [ni˧˥ xau̯˨˩˦]. Pinyin convention still **writes** the underlying diacritics (*nǐ hǎo*); the surface tone is shown in the IPA. Also shows initial n /n/ (contrast l /l/ in 老 *lǎo*). Same characters in simplified and traditional.

**31. `一定` / `一定` `yídìng` `ㄧˊ ㄉㄧㄥˋ` — /i˧˥ tiŋ˥˩/ [i˧˥ tiŋ˥˩] (一 yī → sandhi yí before T4)**
- **一 yī TONE SANDHI**: *yī* (T1) → *yí* (T2) before a T4 syllable
- d /t/, final -ing /iŋ/, coda -ng /ŋ/
- tone: surface T2 + T4
- *Note:* **一 yī sandhi**: the numeral 一 is citation T1, but before a T4 syllable (定 *dìng*) it shifts to T2 → *yídìng* [i˧˥ tiŋ˥˩]. (Before T1/T2/T3 it would instead become T4 *yì*, as in 一天 *yìtiān*, 一年 *yìnián*, 一起 *yìqǐ*.) Same characters in simplified and traditional.

**32. `不是` / `不是` `búshì` `ㄅㄨˊ ㄕˋ` — /pu˧˥ ʂɻ̩˥˩/ [pu˧˥ ʂɻ̩˥˩] (不 bù → sandhi bú before T4)**
- **不 bù TONE SANDHI**: *bù* (T4) → *bú* (T2) before a T4 syllable
- b /p/ (unaspirated), u /u/
- sh /ʂ/, apical -i [ɻ̩]
- tone: surface T2 + T4
- *Note:* **不 bù sandhi**: the negator 不 is citation T4, but before another T4 syllable (是 *shì*) it raises to T2 → *búshì* [pu˧˥ ʂɻ̩˥˩]. (Before T1/T2/T3 it stays T4: 不喝 *bù hē*, 不来 *bù lái*, 不好 *bù hǎo*.) Reuses the unaspirated b /p/ and retroflex sh /ʂ/. Same characters in simplified and traditional.

**33. `我的` / `我的` `wǒ de` `ㄨㄛˇ ˙ㄉㄜ` — /wo˨˩˦ tɤ/ [wo˨˩(˦) tɤ·⁴] (T3 + neutral particle 的)**
- w /w/ (medial/zero-onset glide), final -o /wo/
- d /t/, final -e /ɤ/
- **NEUTRAL TONE 轻声** on the grammatical particle 的 *de*
- tone: T3 + **NEUTRAL**
- *Note:* Shows the **neutral tone 轻声** on the ubiquitous structural particle 的 *de* (the possessive/attributive marker) — 的 is always toneless and pinyin leaves it unmarked. Before a neutral syllable the preceding T3 (我 *wǒ*) typically surfaces as a low **half-third** [˨˩] without the final rise. Also shows the -uo/-o rime [wo] and final -e [ɤ]. Same characters in simplified and traditional. Zhuyin writes the neutral dot `˙` before 的.

#### Simplified ≠ Traditional showcases

**34. `发` / `發` `fā` `ㄈㄚ` — /fa˥/ [fa˥] (T1, 55)**
- f /f/, a /a/
- tone: T1 阴平 ˥
- **SIMP≠TRAD merger showcase**: 发 collapses two traditional characters
- *Note:* **SIMPLIFIED≠TRADITIONAL showcase #1**: the single simplified `发` corresponds to **two distinct traditional characters** with different sounds/meanings — `發` *fā* (T1, 'to send out, issue, develop', as here) and `髮` *fà* (T4, 'hair'). The simplified script merges them into `发`, so `发` is read *fā* or *fà* by context (头发 *tóufa* 'hair' uses 髮/发). A classic **one-to-many** simplification. Zhuyin `ㄈㄚ` = *fā*.

**35. `国` / `國` `guó` `ㄍㄨㄛˊ` — /kwo˧˥/ [kwo˧˥] (T2, 35)**
- g /k/ (unaspirated), medial u /w/, final -uo /wo/
- tone: T2 阳平 ˧˥
- **SIMP≠TRAD showcase**: `國` (trad) → `国` (simp)
- *Note:* **SIMPLIFIED≠TRADITIONAL showcase #2**: `國` (traditional, the `囗` 'enclosure' radical around `或`) → `国` (simplified, `囗` around `玉` 'jade'), a **one-to-one** structural simplification (unlike 发, no merger). The **sound** *guó* [kwo˧˥] is identical in both; only the glyph differs — exactly the kind of script-tier divergence the Peshitta Simplified vs Traditional Hanzi tiers encode. Also shows g /k/ + medial u /w/ + -uo rime. Zhuyin `ㄍㄨㄛˊ`.

### Coverage Matrix

The 35 words form a verifiable coverage matrix for the Standard Mandarin phonological system. Each sub-matrix below lists the inventory cell and the array keyword(s) realizing it.

#### Initial inventory (21 initials + zero initial — all covered)

| Initial | IPA | Realizing keyword(s) |
|---|---|---|
| b (unasp. bilabial stop) | /p/ | 爸爸 *bàba*; 不是 *búshì* |
| p (asp. bilabial stop) | /pʰ/ | 怕 *pà* |
| m (bilabial nasal) | /m/ | 妈/麻/马/骂/吗 *mā/má/mǎ/mà/ma* |
| f (labiodental fricative) | /f/ | 飞 *fēi*; 发 *fā* |
| d (unasp. alveolar stop) | /t/ | 弟弟 *dìdi*; 一定 …*dìng*; 我的 …*de* |
| t (asp. alveolar stop) | /tʰ/ | 天 *tiān*; 听 *tīng* |
| n (alveolar nasal) | /n/ | 你好 *nǐ hǎo* (你 *nǐ*) |
| l (lateral) | /l/ | 老 *lǎo* |
| g (unasp. velar stop) | /k/ | 哥哥 *gēge*; 国 *guó* |
| k (asp. velar stop) | /kʰ/ | 看 *kàn* |
| h (velar fricative) | /x/ | 湖 *hú*; 花儿 *huār*; 你好 …*hǎo* |
| j (unasp. alveolo-palatal affricate) | /tɕ/ | 鸡 *jī* |
| q (asp. alveolo-palatal affricate) | /tɕʰ/ | 七 *qī* |
| x (alveolo-palatal fricative) | /ɕ/ | 西 *xī*; 熊 *xióng* |
| z (unasp. dental affricate) | /ts/ | 字 *zì* |
| c (asp. dental affricate) | /tsʰ/ | 词 *cí* |
| s (dental fricative) | /s/ | 四 *sì* |
| zh (unasp. retroflex affricate) | /ʈʂ/ | 知 *zhī* |
| ch (asp. retroflex affricate) | /ʈʂʰ/ | 吃 *chī* |
| sh (retroflex fricative) | /ʂ/ | 是 *shì*; 不是 …*shì* |
| r (retroflex rhotic) | /ʐ~ɻ/ | 日 *rì* |
| zero initial (y-/w-/yu- spellings) | — | 鱼 *yú* (ü); 二 *èr*; 一定 *yí-* (一); 我的 *wǒ* (我) |

*All 21 initials plus the zero initial are realized by at least one dedicated keyword. The core Mandarin obstruent contrast is **aspiration (not voicing)**: each unaspirated/aspirated pair is exemplified minimally — b 爸 [pa] ~ p 怕 [pʰa]; d 弟 [ti] ~ t 天 [tʰjɛn]; g 哥 [kɤ] ~ k 看 [kʰan]; z 字 [tsɹ̩] ~ c 词 [tsʰɹ̩]; zh 知 [ʈʂɻ̩] ~ ch 吃 [ʈʂʰɻ̩]; j 鸡 [tɕi] ~ q 七 [tɕʰi]. The three sibilant PLACES are contrasted across the parallel triads 字/词/四 (dental z/c/s), 知/吃/是 (retroflex zh/ch/sh), 鸡/七/西 (alveolo-palatal j/q/x), with r 日 [ʐ~ɻ] as the sole voiced rhotic. (j/q/x occur only before high front i/ü and are in complementary distribution with z/c/s, zh/ch/sh, and g/k/h, so they form no minimal pair with those across the same vowel.)*

#### Finals inventory (all types covered)

**Simple vowel finals**

| Final | IPA | Realizing keyword(s) |
|---|---|---|
| -a | [a] | 妈/麻/马/骂/吗; 爸爸; 发 |
| -o / -uo | [wo] | 我的 (我 *wǒ*); 国 (*guó*); 花儿 (within -ua) |
| -e | [ɤ] | 哥哥; 我的 (的 *de*) |
| -i (true high front) | [i] | 弟弟; 鸡; 七; 西; 听 (in -ing) |
| -u | [u] | 湖; 不是 (不 *bù*) |
| -ü | [y] | 鱼 *yú* |

**Apical vowel -i**

| Type | IPA | Realizing keyword(s) |
|---|---|---|
| dental (after z/c/s) | [ɹ̩] | 字 *zì*; 词 *cí*; 四 *sì* |
| retroflex (after zh/ch/sh/r) | [ɻ̩] | 知 *zhī*; 吃 *chī*; 是 *shì*; 日 *rì*; 不是 (是 *shì*) |

**er-rime and erhua**

| Type | IPA | Realizing keyword(s) |
|---|---|---|
| er-rime (standalone syllable) | [ɚ] | 二 *èr* |
| erhua (suffix 儿 fused onto rime) | [ɻ] | 花儿 *huār* [xwaɻ] |

**Medial glides**

| Glide | IPA | Realizing keyword(s) |
|---|---|---|
| i (palatal) | /j/ | 天 *tiān* (-ian); 熊 *xióng* (-iong) |
| u (labiovelar) | /w/ | 花儿 *huār* (-ua); 国 *guó* (-uo); 我的 (我 *wǒ* -uo) |
| ü (rounded palatal) | /ɥ/ | 鱼 (ü as nucleus; ü-glide e.g. 月 *yuè* noted in 鱼 entry) |

**Diphthongs**

| Diphthong | IPA | Realizing keyword(s) |
|---|---|---|
| -ei | [ei̯] | 飞 *fēi* |
| -ao | [au̯] | 老 *lǎo*; 你好 (好 *hǎo*) |
| -ai | [ai̯] | noted via contrast in 飞 entry (爱 *ài*) |
| -ou | [ou̯] | noted via contrast in 老 entry (都 *dōu*) |

**Triphthong / glide finals**

| Final | IPA | Realizing keyword(s) |
|---|---|---|
| -uo | [wo] | 国 *guó*; 我 *wǒ* |
| -ua | [wa] | 花(儿) *huā(r)* |
| -ian | [jɛn] | 天 *tiān* |
| -iong | [jʊŋ] | 熊 *xióng* |

**Nasal-coda finals**

| Coda | IPA | Realizing keyword(s) |
|---|---|---|
| -n (alveolar) | /n/ | 天 *tiān* (-ian); 看 *kàn* (-an) |
| -ng (velar) | /ŋ/ | 听 *tīng* (-ing); 熊 *xióng* (-iong); 一定 (定 *dìng* -ing) |

*All major finals **types** are realized: the simple vowel finals -a -o/-uo -e -i -u -ü; both apical -i vowels (dental [ɹ̩] after z/c/s, retroflex [ɻ̩] after zh/ch/sh/r); the er-rime [ɚ] as a standalone syllable AND erhua [ɻ] as a fused suffix; all three medial glides /j w ɥ/; the falling diphthongs -ei [ei̯] -ao [au̯] (with -ai [ai̯] and -ou [ou̯] contrasted in notes; off-glides written with the non-syllabic diacritic over the backbone vowels /i u/, nuclei /a e/, NOT English lax [ɪ ʊ ɑ]); glide/triphthong rimes -uo -ua -ian -iong; and the two-way nasal coda contrast -n /n/ vs -ng /ŋ/ across multiple rimes. The only Mandarin codas are /n/, /ŋ/ and the rhotacizing er/儿 — all present.*

#### Tone inventory (all five categories covered)

| Tone category | Chao (numeral) | Realizing keyword(s) |
|---|---|---|
| T1 阴平 high-level | ˥ (55) | 妈 *mā*; 天 *tiān*; 哥 *gē*; 知 *zhī*; 吃 *chī*; 鸡 *jī*; 七 *qī*; 西 *xī*; 飞 *fēi*; 听 *tīng*; 花儿 *huār*; 发 *fā* |
| T2 阳平 rising | ˧˥ (35) | 麻 *má*; 词 *cí*; 鱼 *yú*; 湖 *hú*; 熊 *xióng*; 国 *guó*; 你 (surface, sandhi) *ní*; 一 (surface, sandhi) *yí*; 不 (surface, sandhi) *bú* |
| T3 上声 low-dipping / half-third | ˨˩˦ (214) / ˨˩ | 马 *mǎ*; 老 *lǎo*; 好 *hǎo*; 你 *nǐ* (citation); 我 *wǒ* (half-third before neutral) |
| T4 去声 high-falling | ˥˩ (51) | 骂 *mà*; 爸 *bà*; 怕 *pà*; 弟 *dì*; 看 *kàn*; 字 *zì*; 四 *sì*; 是 *shì*; 日 *rì*; 二 *èr*; 定 *dìng*; (发/髮 *fà* sense, noted) |
| neutral 轻声 (toneless) | short, context-set | 吗 *ma*; 爸 (2nd, 爸爸); 弟 (2nd, 弟弟); 哥 (2nd, 哥哥); 的 *de* (我的) |

*All four lexical tones plus the neutral tone are exemplified, anchored by the canonical minimal set 妈 *mā* (T1) / 麻 *má* (T2) / 马 *mǎ* (T3) / 骂 *mà* (T4) / 吗 *ma* (neutral) on identical /ma/ segments — the clearest demonstration that tone alone is contrastive. T3 is shown both in its full low-dipping isolation contour (马, 老, 好 phrase-finally) and as a reduced half-third before a neutral syllable (我的). The neutral tone is shown on grammatical particles (吗, 的) and on the reduplicated second syllables of kin terms (爸爸, 弟弟, 哥哥).*

#### Sandhi & erhua showcase (all five connected-speech phenomena covered)

| Phenomenon | Realizing keyword(s) |
|---|---|
| third-tone sandhi (T3+T3 → T2+T3) | 你好 *nǐ hǎo* → *ní hǎo* |
| 一 *yī* sandhi | 一定 *yídìng* (一 → *yí*, T2, before T4); → *yì* before T1/T2/T3 noted: 一天/一年/一起 |
| 不 *bù* sandhi | 不是 *búshì* (不 → *bú*, T2, before T4); stays *bù* before T1/T2/T3 noted: 不喝/不来/不好 |
| erhua 儿化 | 花儿 *huār* [xwaɻ] (suffix 儿 fuses, no added syllable/tone); contrasted with standalone er-rime 二 *èr* [ɚ] |
| neutral tone 轻声 | 的 *de* (我的); 吗 *ma*; 爸爸/弟弟/哥哥 (reduplication) |

*All five connected-speech phenomena from the brief are exemplified with dedicated entries: third-tone sandhi (你好), 一 *yī* sandhi (一定, with the *yì* variant noted), 不 *bù* sandhi (不是, with the unchanged-*bù* environment noted), erhua (花儿, contrasted with the standalone er-rime 二), and the neutral tone (的, 吗, and kin-term reduplication). Pinyin entries show **citation** tone diacritics; the **surface (post-sandhi)** tone is given in each IPA and explained in the note.*

#### Simplified vs Traditional examples

| Type | Pair | Detail |
|---|---|---|
| one-to-many merger (simp collapses 2+ trad chars) | `发` = `發` + `髮` | `发` = `發` *fā* ('send/issue/develop') + `髮` *fà* ('hair'); the simplification **merges** two distinct traditional characters and their tones (*fā*/*fà*) |
| one-to-one structural simplification (sound unchanged) | `国` ← `國` | *guó* [kwo˧˥] in both; only the glyph differs (`囗`+`或` → `囗`+`玉`) |

**Other trad≠simp glyphs shown across the array:** `妈`←`媽`, `马`←`馬`, `骂`←`罵`, `吗`←`嗎`, `词`←`詞`, `知`=`知` (unchanged), `鸡`←`雞`, `鱼`←`魚`, `飞`←`飛`, `听`←`聽`, `花儿`←`花兒`.

*Both brief-mandated simp≠trad pairs are present as dedicated showcase entries: 发/發 (the one-to-**many** merger type, where one simplified glyph spans two traditional characters and even two readings *fā*/*fà*) and 国/國 (the one-to-**one** type, where the sound *guó* is unchanged and only the glyph is restructured). Every entry carries BOTH `汉字` (simplified) and `漢字` (traditional), so the array also incidentally exhibits a dozen further trad≠simp glyph reductions (媽/馬/罵/嗎/詞/雞/魚/飛/聽/花兒…), matching the Peshitta reader's parallel Simplified-Hanzi and Traditional-Hanzi tiers. These character-tier differences do NOT change the toneless pinyin/zhuyin spelling, which is shared between 普通话 and 國語.*

*Section compiled by Shin.*

## Unicode Reference

Unicode codepoint reference for every IPA symbol, suprasegmental mark, Bopomofo (注音/`ㄅㄆㄇㄈ`) letter, and 汉字/漢字 (Hànzì) example used throughout this Mandarin Chinese pronunciation guide. Each entry gives the symbol, its Unicode codepoint (`U+XXXX`), decimal value, official Unicode character name, and its phonetic or orthographic role in Standard Mandarin, documented in parallel for the guide's two reference standards: 普通话 Pǔtōnghuà (PRC Standard Mandarin, Beijing-based phonology, **SIMPLIFIED** characters, Hanyu Pinyin) and 國語 Guóyǔ (Taiwan Standard Mandarin, **TRADITIONAL** characters, Zhuyin/Bopomofo). All IPA codepoints follow the IPA 2015 revision conventions.

The most distinctive Mandarin entries are the THREE sibilant series — the **RETROFLEX** `[ʈʂ ʈʂʰ ʂ ʐ ɻ]` (Pinyin `zh ch sh r`), the **ALVEOLO-PALATAL** `[tɕ tɕʰ ɕ]` (Pinyin `j q x`), and the **DENTAL** `[ts tsʰ]` (Pinyin `z c`) — plus the voiceless velar fricative `[x]` (Pinyin `h`), the back unrounded vowel `[ɤ]` (Pinyin `e`), the close front rounded `[y]` (Pinyin `ü`), the rhotacized `[ɚ]` (`er`/儿化), and the two **APICAL** syllabic vowels `[ɹ̩]` (after `z c s`) and `[ɻ̩]` (after `zh ch sh r`), each carrying the COMBINING VERTICAL LINE BELOW (syllabic ring). Mandarin has **NO voicing contrast** in its obstruents; the contrast is **ASPIRATION**, marked with the MODIFIER LETTER SMALL H `ʰ`.

Mandarin is fully **TONAL**: tone is notated three ways here — the Chao TONE-LETTER bars `˥˦˧˨˩` (`U+02E5`–`U+02E9`), the PINYIN tone DIACRITICS (`ā á ǎ à` over `a e i o u ü`, precomposed and as combining marks over the base), and the ZHUYIN/Bopomofo tone marks (`ˊ ˇ ˋ ˙`, T1 left unmarked).

> **Note carefully:** the LANGUAGE documented here is fully tonal, but the Chinese Peshitta **READER TIERS** (toneless Pinyin, its Zhuyin transcode, and the Simplified/Traditional Hanzi lookup) are **TONELESS by design** because the Peshitta source IPA carries no tone — the Hanzi tier nevertheless imposes a citation tone per character as an unavoidable artifact. Toneless Pinyin uses the PLAIN base letters `a e i o u ü` with NO diacritic.

Verify IPA rendering with a font supporting IPA Extensions and combining marks (e.g. Charis SIL, Doulos SIL, Gentium), and Chinese/Bopomofo rendering with a CJK-complete font (e.g. Noto Sans/Serif CJK SC/TC, Source Han, PingFang, Microsoft YaHei, 標楷體 DFKai-SB).

### IPA Consonant Symbols

The 21 Mandarin initials (声母 shēngmǔ) plus the zero initial, given in IPA. Mandarin obstruents have **NO voicing contrast** — the systematic contrast is **ASPIRATION** (`b`/`p` = `/p/` vs `/pʰ/`, etc.), marked with the spacing diacritic `ʰ` (`U+02B0`). The plain stops `p t k`, fricatives `f s x`, nasals `m n`, and lateral `l` reuse Basic Latin letters; the retroflex letters `ʈ ʂ ʐ ɻ`, the curl letter `ɕ`, and the affricate elements come from IPA Extensions (`U+0250`–`U+02AF`) and Spacing Modifier Letters. The affricates `ʈʂ ʈʂʰ tɕ tɕʰ ts tsʰ` are **DIGRAPHS** (no single codepoint); the IPA tie bar `U+0361` may be written over them (`ʈ͡ʂ t͡ɕ t͡s`).

Three sibilant series are in complementary distribution: **DENTAL** `z c s` `/ts tsʰ s/`, **RETROFLEX** `zh ch sh r` `/ʈʂ ʈʂʰ ʂ ʐ/`, and **ALVEOLO-PALATAL** `j q x` `/tɕ tɕʰ ɕ/` (the palatals occur ONLY before the high front vowels `i`/`ü`). In Taiwan 國語, frequent **DE-RETROFLEXION** merges `zh ch sh r` → `z c s` (surface only; the toneless spelling is unchanged).

| Symbol | Codepoint | Decimal | Name | Pinyin | Zhuyin | IPA Role |
|---|---|---|---|---|---|---|
| p | `U+0070` | 112 | LATIN SMALL LETTER P | `b` | `ㄅ` | voiceless UNASPIRATED bilabial plosive `/p/` (Pinyin `b`, 八 bā 'eight'); the lax member of the `b`/`p` aspiration pair — NOT voiced `[b]`, which Mandarin lacks |
| pʰ | `U+0070 + U+02B0` | 112 + 688 | LATIN SMALL LETTER P + MODIFIER LETTER SMALL H (digraph) | `p` | `ㄆ` | voiceless ASPIRATED bilabial plosive `/pʰ/` (Pinyin `p`, 怕 pà 'fear'); aspiration `ʰ` `U+02B0` is the contrastive feature vs unaspirated `b` `/p/` |
| t | `U+0074` | 116 | LATIN SMALL LETTER T | `d` | `ㄉ` | voiceless UNASPIRATED alveolar plosive `/t/` (Pinyin `d`, 大 dà 'big'); also the stop element of the affricate digraphs `ts ʈʂ tɕ` |
| tʰ | `U+0074 + U+02B0` | 116 + 688 | LATIN SMALL LETTER T + MODIFIER LETTER SMALL H (digraph) | `t` | `ㄊ` | voiceless ASPIRATED alveolar plosive `/tʰ/` (Pinyin `t`, 他 tā 'he') |
| k | `U+006B` | 107 | LATIN SMALL LETTER K | `g` | `ㄍ` | voiceless UNASPIRATED velar plosive `/k/` (Pinyin `g`, 高 gāo 'tall'); in complementary distribution with the palatal `tɕ` before high front vowels |
| kʰ | `U+006B + U+02B0` | 107 + 688 | LATIN SMALL LETTER K + MODIFIER LETTER SMALL H (digraph) | `k` | `ㄎ` | voiceless ASPIRATED velar plosive `/kʰ/` (Pinyin `k`, 开 kāi / 開 'open') |
| ts | `U+0074 + U+0073` | 116 + 115 | LATIN SMALL LETTER T + LATIN SMALL LETTER S (digraph) | `z` | `ㄗ` | voiceless UNASPIRATED **DENTAL** affricate `/ts/` (Pinyin `z`, 在 zài 'at'); the tie-bar ligature `t͡s` may be written; before the apical vowel `ɹ̩` in 字 zì |
| tsʰ | `U+0074 + U+0073 + U+02B0` | 116 + 115 + 688 | LATIN SMALL LETTER T + LATIN SMALL LETTER S + MODIFIER LETTER SMALL H (digraph) | `c` | `ㄘ` | voiceless ASPIRATED **DENTAL** affricate `/tsʰ/` (Pinyin `c`, 才 cái 'only then'); NOT the English `[k]`/`[s]` value of orthographic `c` |
| ʈʂ | `U+0288 + U+0282` | 648 + 642 | LATIN SMALL LETTER T WITH RETROFLEX HOOK + LATIN SMALL LETTER S WITH HOOK (digraph) | `zh` | `ㄓ` | voiceless UNASPIRATED **RETROFLEX** affricate `/ʈʂ/` (Pinyin `zh`, 中 zhōng 'middle'); the tie-bar ligature `ʈ͡ʂ` may be written; de-retroflexed to `ts` in much Taiwan 國語 |
| ʈʂʰ | `U+0288 + U+0282 + U+02B0` | 648 + 642 + 688 | LATIN SMALL LETTER T WITH RETROFLEX HOOK + LATIN SMALL LETTER S WITH HOOK + MODIFIER LETTER SMALL H (digraph) | `ch` | `ㄔ` | voiceless ASPIRATED **RETROFLEX** affricate `/ʈʂʰ/` (Pinyin `ch`, 吃 chī 'eat'); de-retroflexed to `tsʰ` in much Taiwan 國語 |
| tɕ | `U+0074 + U+0255` | 116 + 597 | LATIN SMALL LETTER T + LATIN SMALL LETTER C WITH CURL (digraph) | `j` | `ㄐ` | voiceless UNASPIRATED **ALVEOLO-PALATAL** affricate `/tɕ/` (Pinyin `j`, 家 jiā 'home'); occurs ONLY before high front `i`/`ü`; the tie-bar ligature `t͡ɕ` may be written |
| tɕʰ | `U+0074 + U+0255 + U+02B0` | 116 + 597 + 688 | LATIN SMALL LETTER T + LATIN SMALL LETTER C WITH CURL + MODIFIER LETTER SMALL H (digraph) | `q` | `ㄑ` | voiceless ASPIRATED **ALVEOLO-PALATAL** affricate `/tɕʰ/` (Pinyin `q`, 去 qù 'go'); NOT the English `[kw]` value of orthographic `q` — a frequent learner pitfall |
| f | `U+0066` | 102 | LATIN SMALL LETTER F | `f` | `ㄈ` | voiceless labiodental fricative `/f/` (Pinyin `f`, 飞 fēi / 飛 'fly') |
| s | `U+0073` | 115 | LATIN SMALL LETTER S | `s` | `ㄙ` | voiceless **DENTAL** fricative `/s/` (Pinyin `s`, 三 sān 'three'); paired with the dental affricates `ts tsʰ`; before the apical vowel `ɹ̩` in 思 sī |
| ʂ | `U+0282` | 642 | LATIN SMALL LETTER S WITH HOOK | `sh` | `ㄕ` | voiceless **RETROFLEX** fricative `/ʂ/` (Pinyin `sh`, 是 shì 'to be'); the fricative element of `ʈʂ`; de-retroflexed to `s` in much Taiwan 國語; distinct from postalveolar `ʃ`, which Mandarin lacks |
| ʐ | `U+0290` | 656 | LATIN SMALL LETTER Z WITH RETROFLEX HOOK | `r` | `ㄖ` | voiced **RETROFLEX** fricative `/ʐ/` (Pinyin `r`, 人 rén 'person'); the voiced counterpart of `ʂ`; many speakers realize it as the retroflex approximant `ɻ` instead (see `ɻ` entry) — both transcribe Pinyin `r` |
| ɻ | `U+027B` | 635 | LATIN SMALL LETTER TURNED R WITH HOOK | `r` | `ㄖ` | voiced **RETROFLEX** approximant `/ɻ/`; the approximant realization of the Pinyin `r` initial (热 rè 'hot') for speakers who do not use the fricative `ʐ`; also the basis of the rhotacized coda/erhua (see `ɚ` entry) |
| ɕ | `U+0255` | 597 | LATIN SMALL LETTER C WITH CURL | `x` | `ㄒ` | voiceless **ALVEOLO-PALATAL** fricative `/ɕ/` (Pinyin `x`, 西 xī 'west'); occurs ONLY before high front `i`/`ü`; the fricative element of `tɕ`; NOT the postalveolar `ʃ` and NOT the English `[ks]` value of orthographic `x` |
| x | `U+0078` | 120 | LATIN SMALL LETTER X | `h` | `ㄏ` | voiceless **VELAR** fricative `/x/` (Pinyin `h`, 好 hǎo 'good'); a back velar friction, NOT the English glottal `[h]` — though `[h]` is a common allophone; the IPA value of `x` is NOT the `[ks]` of orthographic `x` |
| m | `U+006D` | 109 | LATIN SMALL LETTER M | `m` | `ㄇ` | voiced bilabial nasal `/m/` (Pinyin `m`, 妈 mā / 媽 'mother'); also a coda only marginally (the interjection 呒/嘸) |
| n | `U+006E` | 110 | LATIN SMALL LETTER N | `n` | `ㄋ` | voiced alveolar nasal `/n/` (Pinyin `n`, 你 nǐ 'you'); one of only two true nasal CODAS (`-n`, e.g. 安 ān), the other being `-ng` `/ŋ/` |
| l | `U+006C` | 108 | LATIN SMALL LETTER L | `l` | `ㄌ` | voiced alveolar lateral approximant `/l/` (Pinyin `l`, 来 lái / 來 'come'); occurs only as an initial, never as a coda in Standard Mandarin |
| ŋ | `U+014B` | 331 | LATIN SMALL LETTER ENG | `-ng` | `ㄥ / ㄤ` | voiced velar nasal `/ŋ/`; in Mandarin it is exclusively a CODA (the `-ng` finals `ang eng ing ong`, 中 zhōng), NEVER an initial; from Latin Extended-A |

### IPA Vowel Symbols

Vowel qualities of the Mandarin finals (韵母 yùnmǔ). The nuclei are `a o e ê i u ü` = `/a o ɤ ɛ i u y/`; medials are `i u ü` = the glides `/j w ɥ/`; the only vocalic coda is the rhotacized `/ɚ/` (`er` / 儿化 erhua). The cardinal-quality letters `a o e i u` reuse Basic Latin; the back unrounded `ɤ` (rams horn), open-mid `ɛ` (open e), close front rounded `y`, rhotic schwa `ɚ`, and turned-h `ɥ` come from IPA Extensions.

Two special **APICAL** ('buzzed') syllabic vowels are written `-i` in Pinyin: `[ɹ̩]` after `z c s` (`zi ci si`) and `[ɻ̩]` after `zh ch sh r` (`zhi chi shi ri`) — each is the SYLLABIC continuation of the preceding sibilant, marked with the COMBINING VERTICAL LINE BELOW `◌̩` (`U+0329`, the 'syllabic ring'); they are NOT the vowel `/i/`. The neutral mid central `ə` appears in unstressed neutral-tone syllables and as a transition vowel.

| Symbol | Codepoint | Decimal | Name | Pinyin | Zhuyin | IPA Role |
|---|---|---|---|---|---|---|
| a | `U+0061` | 97 | LATIN SMALL LETTER A | `a` | `ㄚ` | open central/front unrounded vowel `/a/` (Pinyin `a`, 妈 mā / 媽 'mother'); fronts to `[a]` before `-n`/`-i` and backs to `[ɑ]` before `-ng`/`-u` allophonically |
| o | `U+006F` | 111 | LATIN SMALL LETTER O | `o` | `ㄛ` | close-mid/open-mid back rounded vowel `/o/` (Pinyin `o`, 我 wǒ 'I'); chiefly after labials (`bo po mo fo`) and in the diphthong `ou`; phonetically often `[ʷɔ]` |
| ɤ | `U+0264` | 612 | LATIN SMALL LETTER RAMS HORN | `e` | `ㄜ` | close-mid **BACK UNROUNDED** vowel `/ɤ/` (Pinyin `e` in open syllables, 饿 è / 餓 'hungry', 喝 hē 'drink'); a hallmark Mandarin vowel with no English equivalent — like 'o' but with spread, not rounded, lips; the rams-horn letter, NOT the rounded `o` |
| ɛ | `U+025B` | 603 | LATIN SMALL LETTER OPEN E | `ê / -ie / -üe` | `ㄝ` | open-mid front unrounded vowel `/ɛ/` (Pinyin `ê` 欸, and the nucleus of `-ie` 谢 xiè / 謝 and `-üe` 月 yuè); the Bopomofo `ㄝ`; distinct from the rams-horn `ɤ` that writes plain Pinyin `e` |
| i | `U+0069` | 105 | LATIN SMALL LETTER I | `i` | `ㄧ` | close front unrounded vowel `/i/` (Pinyin `i`, 一 yī 'one', 你 nǐ 'you'); as a medial it is the glide `j` (see `j` entry); NOT the apical `-i` of `zi`/`zhi` (see `ɹ̩`, `ɻ̩`) |
| u | `U+0075` | 117 | LATIN SMALL LETTER U | `u` | `ㄨ` | close back rounded vowel `/u/` (Pinyin `u`, 五 wǔ 'five', 不 bù 'not'); as a medial it is the glide `w` (see `w` entry) |
| y | `U+0079` | 121 | LATIN SMALL LETTER Y | `ü` (also `u` after `j q x y`) | `ㄩ` | close front **ROUNDED** vowel `/y/` (Pinyin `ü`, 女 nǚ 'woman', 绿 lǜ / 綠 'green'; spelled plain `u` after `j q x y`, e.g. 居 jū); the IPA letter `y` is this rounded vowel, NOT the English consonant 'y' (which is the glide `j`) |
| ɥ | `U+0265` | 613 | LATIN SMALL LETTER TURNED H | `ü-` (medial) | `ㄩ` (as glide) | voiced labial-palatal approximant `/ɥ/`; the GLIDE realization of the `ü` medial (Pinyin `-üan`/`-üe`/`-ün`, 月 yuè `/ɥɛ/`, 全 quán `/tɕʰɥɛn/`); the rounded counterpart of `j` |
| j | `U+006A` | 106 | LATIN SMALL LETTER J | `i-` (medial) | `ㄧ` (as glide) | voiced palatal approximant `/j/`; the GLIDE realization of the `i` medial (Pinyin `-ia`/`-ie`/`-iao`/`-ian`, 家 jiā `/tɕja/`, 谢 xiè `/ɕjɛ/`); the IPA value of `j`, NOT the affricate of English orthographic 'j' |
| w | `U+0077` | 119 | LATIN SMALL LETTER W | `u-` (medial) | `ㄨ` (as glide) | voiced labial-velar approximant `/w/`; the GLIDE realization of the `u` medial (Pinyin `-ua`/`-uo`/`-uai`/`-uan`, 我 wǒ `/wo/`, 关 guān / 關 `/kwan/`) |
| ɚ | `U+025A` | 602 | LATIN SMALL LETTER SCHWA WITH HOOK | `er / -r` (儿化) | `ㄦ` | rhotacized mid central vowel `/ɚ/`; the standalone `er` final (儿 ér / 兒, 二 èr 'two') and the rhotic coda of 儿化 **ERHUA** (花儿 huār / 花兒, 一点儿 yìdiǎnr / 一點兒); restructures the rime by rhotacizing it; rare/absent in Taiwan 國語 (little erhua) |
| ɹ̩ | `U+0279 + U+0329` | 633 + 809 | LATIN SMALL LETTER TURNED R + COMBINING VERTICAL LINE BELOW (syllabic) | `-i` (after `z c s`) | (no separate symbol; `ㄗㄘㄙ` stand alone) | syllabic **APICAL DENTAL** approximant/vowel `[ɹ̩]` — the 'buzzed' apical vowel written `-i` after `z c s` (字 zì, 词 cí / 詞, 思 sī); the COMBINING VERTICAL LINE BELOW (syllabicity / 'syllabic ring') marks it as the syllable nucleus; sometimes transcribed `[ɿ]` or `[z̩]`; this is NOT the vowel `/i/` |
| ɻ̩ | `U+027B + U+0329` | 635 + 809 | LATIN SMALL LETTER TURNED R WITH HOOK + COMBINING VERTICAL LINE BELOW (syllabic) | `-i` (after `zh ch sh r`) | (no separate symbol; `ㄓㄔㄕㄖ` stand alone) | syllabic **APICAL RETROFLEX** approximant/vowel `[ɻ̩]` — the 'buzzed' apical vowel written `-i` after `zh ch sh r` (知 zhī, 吃 chī, 是 shì, 日 rì); the COMBINING VERTICAL LINE BELOW marks syllabicity; sometimes transcribed `[ʅ]` or `[ʐ̩]`; this is NOT the vowel `/i/` |
| ə | `U+0259` | 601 | LATIN SMALL LETTER SCHWA | `e` (neutral) / `-en`, `-eng` transition | `ㄜ` (reduced) / `ㄣ ㄥ` | mid central unrounded vowel `/ə/`; the reduced nucleus of NEUTRAL-TONE 轻声 syllables (的 de, 了 le, 吗 ma / 嗎) and the transitional vowel within the finals `-en` `/ən/` and `-eng` `/əŋ/` |
| ɛ̃ (allophonic) | `U+025B + U+0303` | 603 + 771 | LATIN SMALL LETTER OPEN E + COMBINING TILDE | (nasalized rime allophone) | — | nasalized vowel (illustrative); in rapid speech a vowel before a nasal coda may be nasalized and the coda weakened/dropped; the COMBINING TILDE `◌̃` (`U+0303`) marks nasalization; documented for completeness of the rime allophony |

### Tone Symbols

Mandarin's **SIGNATURE** feature is **LEXICAL TONE** — four contrastive tones plus the neutral tone (声调 shēngdiào). Tone is notated three complementary ways in this guide:

1. The **Chao TONE-LETTER bars** `˥˦˧˨˩` (`U+02E5`–`U+02E9`) draw the pitch CONTOUR as a 5-point scale: T1 = `˥` (55 high-level), T2 = `˧˥` (35 rising), T3 = `˨˩˦` (214 dipping), T4 = `˥˩` (51 falling).
2. **PINYIN tone DIACRITICS** sit over the vowel: macron `ā` (T1), acute `á` (T2), caron `ǎ` (T3), grave `à` (T4), unmarked = neutral (e.g. 吗 ma). They exist as PRECOMPOSED letters (`ā` `U+0101`…) and can also be built from a base vowel + a COMBINING mark (`U+0304` macron, `U+0301` acute, `U+030C` caron, `U+0300` grave).
3. **ZHUYIN/Bopomofo tone marks:** T1 unmarked, T2 `ˊ` (`U+02CA`), T3 `ˇ` (`U+02C7`), T4 `ˋ` (`U+02CB`), neutral `˙` (`U+02D9`) placed BEFORE the syllable.

> **CRITICAL:** tone is fully part of the LANGUAGE, but the Chinese Peshitta **READER TIERS are TONELESS** — toneless Pinyin uses the PLAIN base letters `a e i o u ü` with NO diacritic.

#### Chao Tone-Letter Bars

The 5-point pitch scale from which the four-tone contours are drawn (`U+02E5`–`U+02E9`, Spacing Modifier Letters).

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| ˥ | `U+02E5` | 741 | MODIFIER LETTER EXTRA-HIGH TONE BAR | pitch level 5 (extra-high); T1 阴平/陰平 high-level is `˥` (Chao 55), 妈 mā / 媽 'mother'; also the top target of T2's rise and the start of T4's fall |
| ˦ | `U+02E6` | 742 | MODIFIER LETTER HIGH TONE BAR | pitch level 4 (high); an intermediate target used in transcribing contours and the upper part of T2/T4 |
| ˧ | `U+02E7` | 743 | MODIFIER LETTER MID TONE BAR | pitch level 3 (mid); the starting point of T2's rise `˧˥` (35) and a common pitch of the neutral tone after T1/T2 |
| ˨ | `U+02E8` | 744 | MODIFIER LETTER LOW TONE BAR | pitch level 2 (low); part of T3's dip `˨˩˦` (214) and the 'half-third' low (`˨˩`, 21) realization of a non-final T3 |
| ˩ | `U+02E9` | 745 | MODIFIER LETTER EXTRA-LOW TONE BAR | pitch level 1 (extra-low); the trough of T3 `˨˩˦` (214) and the endpoint of T4's fall `˥˩` (51), 骂 mà / 罵 'scold' |

#### Pinyin Tone Diacritics (Precomposed)

Precomposed Pinyin tone-marked vowels (Tone 1 macron, Tone 2 acute, Tone 3 caron, Tone 4 grave) over `a e i o u ü`, plus the syllabic `ḿ`/`ǹ` used for the interjections 呣/嗯. Toneless Pinyin (the Peshitta reader tier) uses the PLAIN unmarked base letters.

| Symbol | Codepoint | Decimal | Name | Tone | Example |
|---|---|---|---|---|---|
| ā | `U+0101` | 257 | LATIN SMALL LETTER A WITH MACRON | Tone 1 (high-level) | 妈 mā / 媽 'mother' |
| á | `U+00E1` | 225 | LATIN SMALL LETTER A WITH ACUTE | Tone 2 (rising) | 麻 má 'hemp' |
| ǎ | `U+01CE` | 462 | LATIN SMALL LETTER A WITH CARON | Tone 3 (dipping) | 马 mǎ / 馬 'horse' |
| à | `U+00E0` | 224 | LATIN SMALL LETTER A WITH GRAVE | Tone 4 (falling) | 骂 mà / 罵 'scold' |
| ē | `U+0113` | 275 | LATIN SMALL LETTER E WITH MACRON | Tone 1 | 诶 ē / 誒 |
| é | `U+00E9` | 233 | LATIN SMALL LETTER E WITH ACUTE | Tone 2 | 鹅 é / 鵝 'goose' |
| ě | `U+011B` | 283 | LATIN SMALL LETTER E WITH CARON | Tone 3 | 恶 ě / 噁 (retching) |
| è | `U+00E8` | 232 | LATIN SMALL LETTER E WITH GRAVE | Tone 4 | 饿 è / 餓 'hungry' |
| ī | `U+012B` | 299 | LATIN SMALL LETTER I WITH MACRON | Tone 1 | 衣 yī 'clothes' (`i` as nucleus) |
| í | `U+00ED` | 237 | LATIN SMALL LETTER I WITH ACUTE | Tone 2 | 姨 yí 'aunt' |
| ǐ | `U+01D0` | 464 | LATIN SMALL LETTER I WITH CARON | Tone 3 | 你 nǐ 'you' |
| ì | `U+00EC` | 236 | LATIN SMALL LETTER I WITH GRAVE | Tone 4 | 意 yì 'meaning' |
| ō | `U+014D` | 333 | LATIN SMALL LETTER O WITH MACRON | Tone 1 | 喔 ō (interjection) |
| ó | `U+00F3` | 243 | LATIN SMALL LETTER O WITH ACUTE | Tone 2 | 哦 ó (interjection) |
| ǒ | `U+01D2` | 466 | LATIN SMALL LETTER O WITH CARON | Tone 3 | 我 wǒ 'I' |
| ò | `U+00F2` | 242 | LATIN SMALL LETTER O WITH GRAVE | Tone 4 | 哦 ò (interjection) |
| ū | `U+016B` | 363 | LATIN SMALL LETTER U WITH MACRON | Tone 1 | 屋 wū 'house' (`u` as nucleus) |
| ú | `U+00FA` | 250 | LATIN SMALL LETTER U WITH ACUTE | Tone 2 | 无 wú / 無 'none' |
| ǔ | `U+01D4` | 468 | LATIN SMALL LETTER U WITH CARON | Tone 3 | 五 wǔ 'five' |
| ù | `U+00F9` | 249 | LATIN SMALL LETTER U WITH GRAVE | Tone 4 | 物 wù 'thing' |
| ǖ | `U+01D6` | 470 | LATIN SMALL LETTER U WITH DIAERESIS AND MACRON | Tone 1 over `ü` | (ǖ; rare, e.g. dialect/pedagogical) |
| ǘ | `U+01D8` | 472 | LATIN SMALL LETTER U WITH DIAERESIS AND ACUTE | Tone 2 over `ü` | 驴 lǘ / 驢 'donkey' |
| ǚ | `U+01DA` | 474 | LATIN SMALL LETTER U WITH DIAERESIS AND CARON | Tone 3 over `ü` | 女 nǚ 'woman' |
| ǜ | `U+01DC` | 476 | LATIN SMALL LETTER U WITH DIAERESIS AND GRAVE | Tone 4 over `ü` | 绿 lǜ / 綠 'green' |
| ü | `U+00FC` | 252 | LATIN SMALL LETTER U WITH DIAERESIS | neutral/toneless `ü` base | the unmarked `ü`; toneless reader tier (女 nü, 绿 lü) |
| ḿ | `U+1E3F` | 7743 | LATIN SMALL LETTER M WITH ACUTE | Tone 2 syllabic `m` | 呣 ḿ (interjection 'what?'); the rare syllabic-nasal syllable |
| ǹ | `U+01F9` | 505 | LATIN SMALL LETTER N WITH GRAVE | Tone 4 syllabic `n` | 嗯 ǹ (interjection); syllabic-nasal syllable |

#### Pinyin Combining Tone Marks

When a Pinyin tone vowel is NOT available as a precomposed character (or for decomposition/normalization), the tone is built from a base vowel followed by one of these non-spacing COMBINING marks from the Combining Diacritical Marks block (`U+0300`–`U+036F`), e.g. `a` + `U+0304` = `ā`.

| Symbol | Codepoint | Decimal | Name | Tone | Role |
|---|---|---|---|---|---|
| ◌̄ | `U+0304` | 772 | COMBINING MACRON | Tone 1 (阴平/陰平, high-level) | combining over the vowel to form `ā ē ī ō ū ǖ` |
| ◌́ | `U+0301` | 769 | COMBINING ACUTE ACCENT | Tone 2 (阳平/陽平, rising) | combining over the vowel to form `á é í ó ú ǘ` |
| ◌̌ | `U+030C` | 780 | COMBINING CARON | Tone 3 (上声/上聲, dipping) | combining over the vowel to form `ǎ ě ǐ ǒ ǔ ǚ` |
| ◌̀ | `U+0300` | 768 | COMBINING GRAVE ACCENT | Tone 4 (去声/去聲, falling) | combining over the vowel to form `à è ì ò ù ǜ` |
| ◌̈ | `U+0308` | 776 | COMBINING DIAERESIS | `ü` umlaut (not a tone) | combining over `u` to form `ü` (the `/y/` vowel); combined with a tone mark for `ǖ ǘ ǚ ǜ` |

#### Neutral Tone & Miscellaneous

The NEUTRAL tone 轻声/輕聲 is unmarked in Pinyin (plain letter, no diacritic) but written with a leading dot in Zhuyin. A raised/middle dot is also used pedagogically and as a Pinyin syllable separator.

| Symbol | Codepoint | Decimal | Name | Role |
|---|---|---|---|---|
| ˙ | `U+02D9` | 729 | DOT ABOVE | ZHUYIN NEUTRAL-TONE mark (轻声/輕聲); placed BEFORE the bopomofo syllable, e.g. `˙ㄇㄚ` for 吗/嗎 ma; in Pinyin the neutral tone is simply left UNMARKED |
| · | `U+00B7` | 183 | MIDDLE DOT | used as a Pinyin SYLLABLE SEPARATOR / pedagogical neutral-tone dot (e.g. 西安 Xī'ān is split with an apostrophe, while some dictionaries mark neutral tone with a preceding middle dot, `·le`) |
| ' | `U+0027` | 39 | APOSTROPHE | Pinyin SYLLABLE-BOUNDARY apostrophe, written before a syllable starting with `a`, `o`, or `e` to avoid ambiguity (西安 Xī'ān, not Xian; 棉袄 mián'ǎo / 棉襖) |

### Bopomofo Characters (注音符號)

注音符號 Zhùyīn Fúhào (Bopomofo, `ㄅㄆㄇㄈ`), the phonetic alphabet used in Taiwan 國語 pedagogy and as the guide's Zhuyin reader tier (transcoded from the toneless Pinyin). The 37 base letters fall in the Bopomofo block `U+3100`–`U+312F`: 21 initials (`ㄅ`…`ㄙ`), 3 medials/glides (`ㄧㄨㄩ`), and the rimes/finals (`ㄚ`…`ㄦ`). Tone is added with the marks listed above (T1 unmarked, `ˊ ˇ ˋ ˙`). The apical `-i` of the `ㄓ`/`ㄗ` rows has no separate Bopomofo letter — the initial stands alone.

#### Initials (声母)

| Char | Codepoint | Decimal | Name | Pinyin | IPA | Example |
|---|---|---|---|---|---|---|
| `ㄅ` | `U+3105` | 12549 | BOPOMOFO LETTER B | `b` | `/p/` | `ㄅㄚ` 八 bā |
| `ㄆ` | `U+3106` | 12550 | BOPOMOFO LETTER P | `p` | `/pʰ/` | `ㄆㄚ` 怕 pà |
| `ㄇ` | `U+3107` | 12551 | BOPOMOFO LETTER M | `m` | `/m/` | `ㄇㄚ` 妈/媽 mā |
| `ㄈ` | `U+3108` | 12552 | BOPOMOFO LETTER F | `f` | `/f/` | `ㄈㄟ` 飞/飛 fēi |
| `ㄉ` | `U+3109` | 12553 | BOPOMOFO LETTER D | `d` | `/t/` | `ㄉㄚ` 大 dà |
| `ㄊ` | `U+310A` | 12554 | BOPOMOFO LETTER T | `t` | `/tʰ/` | `ㄊㄚ` 他 tā |
| `ㄋ` | `U+310B` | 12555 | BOPOMOFO LETTER N | `n` | `/n/` | `ㄋㄧ` 你 nǐ |
| `ㄌ` | `U+310C` | 12556 | BOPOMOFO LETTER L | `l` | `/l/` | `ㄌㄞ` 来/來 lái |
| `ㄍ` | `U+310D` | 12557 | BOPOMOFO LETTER G | `g` | `/k/` | `ㄍㄠ` 高 gāo |
| `ㄎ` | `U+310E` | 12558 | BOPOMOFO LETTER K | `k` | `/kʰ/` | `ㄎㄞ` 开/開 kāi |
| `ㄏ` | `U+310F` | 12559 | BOPOMOFO LETTER H | `h` | `/x/` | `ㄏㄠ` 好 hǎo |
| `ㄐ` | `U+3110` | 12560 | BOPOMOFO LETTER J | `j` | `/tɕ/` | `ㄐㄧㄚ` 家 jiā |
| `ㄑ` | `U+3111` | 12561 | BOPOMOFO LETTER Q | `q` | `/tɕʰ/` | `ㄑㄩ` 去 qù |
| `ㄒ` | `U+3112` | 12562 | BOPOMOFO LETTER X | `x` | `/ɕ/` | `ㄒㄧ` 西 xī |
| `ㄓ` | `U+3113` | 12563 | BOPOMOFO LETTER ZH | `zh` | `/ʈʂ/` | `ㄓㄨㄥ` 中 zhōng (`ㄓ` alone = `zhi` `/ʈʂɻ̩/`) |
| `ㄔ` | `U+3114` | 12564 | BOPOMOFO LETTER CH | `ch` | `/ʈʂʰ/` | `ㄔ` 吃 chī |
| `ㄕ` | `U+3115` | 12565 | BOPOMOFO LETTER SH | `sh` | `/ʂ/` | `ㄕ` 是 shì |
| `ㄖ` | `U+3116` | 12566 | BOPOMOFO LETTER R | `r` | `/ʐ~ɻ/` | `ㄖㄣˊ` 人 rén |
| `ㄗ` | `U+3117` | 12567 | BOPOMOFO LETTER Z | `z` | `/ts/` | `ㄗ` 字 zì (`ㄗ` alone = `zi` `/tsɹ̩/`) |
| `ㄘ` | `U+3118` | 12568 | BOPOMOFO LETTER C | `c` | `/tsʰ/` | `ㄘㄞˊ` 才 cái |
| `ㄙ` | `U+3119` | 12569 | BOPOMOFO LETTER S | `s` | `/s/` | `ㄙㄢ` 三 sān (`ㄙ` alone = `si` `/sɹ̩/`) |

#### Medials & Finals (介音 / 韵母)

| Char | Codepoint | Decimal | Name | Pinyin | IPA | Example |
|---|---|---|---|---|---|---|
| `ㄧ` | `U+3127` | 12583 | BOPOMOFO LETTER I | `i / yi` (medial `j`) | `/i/`, glide `/j/` | `ㄧ` 一 yī |
| `ㄨ` | `U+3128` | 12584 | BOPOMOFO LETTER U | `u / wu` (medial `w`) | `/u/`, glide `/w/` | `ㄨˇ` 五 wǔ |
| `ㄩ` | `U+3129` | 12585 | BOPOMOFO LETTER IU | `ü / yu` (medial `ɥ`) | `/y/`, glide `/ɥ/` | `ㄋㄩˇ` 女 nǚ |
| `ㄚ` | `U+311A` | 12570 | BOPOMOFO LETTER A | `a` | `/a/` | `ㄚ` 啊 a |
| `ㄛ` | `U+311B` | 12571 | BOPOMOFO LETTER O | `o` | `/o/` | `ㄨㄛˇ` 我 wǒ |
| `ㄜ` | `U+311C` | 12572 | BOPOMOFO LETTER E | `e` | `/ɤ/` | `ㄜˋ` 饿/餓 è |
| `ㄝ` | `U+311D` | 12573 | BOPOMOFO LETTER EH | `ê / -ie -üe` nucleus | `/ɛ/` | `ㄧㄝˋ` 页/頁 yè |
| `ㄞ` | `U+311E` | 12574 | BOPOMOFO LETTER AI | `ai` | `/ai/` | `ㄌㄞˊ` 来/來 lái |
| `ㄟ` | `U+311F` | 12575 | BOPOMOFO LETTER EI | `ei` | `/ei/` | `ㄈㄟ` 飞/飛 fēi |
| `ㄠ` | `U+3120` | 12576 | BOPOMOFO LETTER AU | `ao` | `/au/` | `ㄍㄠ` 高 gāo |
| `ㄡ` | `U+3121` | 12577 | BOPOMOFO LETTER OU | `ou` | `/ou/` | `ㄉㄡˋ` 豆 dòu |
| `ㄢ` | `U+3122` | 12578 | BOPOMOFO LETTER AN | `an` | `/an/` | `ㄙㄢ` 三 sān |
| `ㄣ` | `U+3123` | 12579 | BOPOMOFO LETTER EN | `en` | `/ən/` | `ㄖㄣˊ` 人 rén |
| `ㄤ` | `U+3124` | 12580 | BOPOMOFO LETTER ANG | `ang` | `/aŋ/` | `ㄈㄤˊ` 房 fáng |
| `ㄥ` | `U+3125` | 12581 | BOPOMOFO LETTER ENG | `eng` | `/əŋ/` | `ㄓㄨㄥ` 中 zhōng (with `ㄨ` = `ong`) |
| `ㄦ` | `U+3126` | 12582 | BOPOMOFO LETTER ER | `er / -r` 儿化 | `/ɚ/` | `ㄦˊ` 儿/兒 ér; `ㄦˋ` 二 èr |

#### Zhuyin Tone Marks

| Char | Codepoint | Decimal | Name | Tone | Note |
|---|---|---|---|---|---|
| (unmarked) | — | — | TONE 1 (no mark) | Tone 1 阴平/陰平 high-level | T1 is left unmarked in Zhuyin (unlike Pinyin's macron `ā`) |
| `ˊ` | `U+02CA` | 714 | MODIFIER LETTER ACUTE ACCENT | Tone 2 阳平/陽平 rising | placed at upper-right of the syllable, e.g. `ㄇㄚˊ` 麻 má |
| `ˇ` | `U+02C7` | 711 | CARON | Tone 3 上声/上聲 dipping | e.g. `ㄇㄚˇ` 马/馬 mǎ |
| `ˋ` | `U+02CB` | 715 | MODIFIER LETTER GRAVE ACCENT | Tone 4 去声/去聲 falling | e.g. `ㄇㄚˋ` 骂/罵 mà |
| `˙` | `U+02D9` | 729 | DOT ABOVE | Neutral tone 轻声/輕聲 | placed BEFORE the syllable, e.g. `˙ㄇㄚ` 吗/嗎 ma |

### Unicode Blocks Used

The Unicode blocks from which every symbol in this guide is drawn — the IPA blocks for the phonetic transcription and tone letters, the Latin tone-diacritic blocks for Pinyin, the Bopomofo blocks for the Zhuyin reader tier, and the CJK Ideograph and Radical blocks for the Simplified and Traditional 汉字/漢字 reader tiers. The two main Bopomofo blocks and the kana-style ranges are nearly gap-free; 汉字/漢字 are drawn from the large CJK Unified Ideographs block plus its extensions.

**NOTE on block extents:** the Bopomofo block is allotted `U+3100`–`U+312F` but the first ASSIGNED letter is `ㄅ` at `U+3105` (`U+3100`–`U+3104` are reserved); the Kangxi Radicals block `U+2F00`–`U+2FDF` has its last assigned radical at `U+2FD5`; the CJK Radicals Supplement `U+2E80`–`U+2EFF` runs through `U+2EF3`. Verify Bopomofo/Hanzi rendering with a CJK-complete font (Noto Sans/Serif CJK SC for 简体, TC for 繁體; Source Han; PingFang; Microsoft YaHei; 標楷體 DFKai-SB) and IPA with Charis SIL / Doulos SIL / Gentium.

| Block | Range | Usage |
|---|---|---|
| Basic Latin | `U+0000–U+007F` | Plain consonant letters (`p t k f s x m n l`) and the vowel letters `a e i o u`, plus the digraph elements (`t s`) of the affricates `ts`/`tsʰ`; the entire (toneless) Hanyu Pinyin reader tier and the apostrophe syllable-separator live in this block. |
| Latin-1 Supplement | `U+0080–U+00FF` | Pinyin tone vowels with acute/grave `á à é è í ì ó ò ú ù`, the `ü` umlaut vowel (`U+00FC`) for `/y/`, and the middle dot `·` (`U+00B7`) used as a Pinyin separator / neutral-tone dot. |
| Latin Extended-A | `U+0100–U+017F` | Pinyin macron (Tone 1) and caron (Tone 3) vowels: `ā` (`U+0101`), `ē` (`U+0113`), `ī` (`U+012B`), `ō` (`U+014D`), `ū` (`U+016B`), `ǎ` (`U+01CE`), `ě` (`U+011B`), `ǐ` (`U+01D0`), `ǒ` (`U+01D2`), `ǔ` (`U+01D4`); also `ŋ` velar nasal eng (`U+014B`) for the `-ng` coda. |
| Latin Extended-B | `U+0180–U+024F` | The tone-marked `ü` letters: `ǖ` (`U+01D6`), `ǘ` (`U+01D8`), `ǚ` (`U+01DA`), `ǜ` (`U+01DC`); and `ǹ` (`U+01F9`, Tone-4 syllabic `n` for 嗯). |
| IPA Extensions | `U+0250–U+02AF` | Specialized IPA letters for the Mandarin initials and finals: the retroflex `ʈ` (`U+0288`), `ʂ` (`U+0282`), `ʐ` (`U+0290`), `ɻ` (`U+027B`); the alveolo-palatal `ɕ` (`U+0255`); the velar fricative is plain `x` (Basic Latin); the schwa `ə` (`U+0259`) and rhotic schwa `ɚ` (`U+025A`); the back-unrounded `ɤ` (`U+0264`); the open-e `ɛ` (`U+025B`); the turned-r `ɹ` (`U+0279`) for the apical vowel; and the glides `ɥ` (`U+0265`, turned h). |
| Spacing Modifier Letters | `U+02B0–U+02FF` | Spacing diacritics that occupy their own width: aspiration `ʰ` (`U+02B0`, the contrastive feature of `p t k c ch q`); the Zhuyin/Pinyin-alternative tone modifiers `ˊ` acute (`U+02CA`), `ˇ` caron (`U+02C7`), `ˋ` grave (`U+02CB`), `˙` dot-above neutral (`U+02D9`), `ˉ` macron (`U+02C9`); and the Chao TONE-BAR letters `˥` (`U+02E5`) … `˩` (`U+02E9`) used to draw the four-tone pitch contours. |
| Combining Diacritical Marks | `U+0300–U+036F` | Non-spacing marks attaching to the preceding base: the Pinyin tone marks — combining macron `◌̄` (`U+0304`, T1), acute `◌́` (`U+0301`, T2), caron `◌̌` (`U+030C`, T3), grave `◌̀` (`U+0300`, T4) — and the diaeresis `◌̈` (`U+0308`) for `ü`; the SYLLABICITY mark `◌̩` (`U+0329`, the 'syllabic ring') for the apical vowels `ɹ̩ ɻ̩`; and the tilde `◌̃` (`U+0303`) for nasalized rime allophones. |
| CJK Radicals Supplement | `U+2E80–U+2EFF` | Supplementary CJK radical glyphs (`U+2E80`–`U+2EF3` assigned), including SIMPLIFIED-form radicals such as `⻌` simplified walk (`U+2ECC`); used to describe the 部首 components of 汉字/漢字 (semantic+phonetic 形声 structure). |
| Kangxi Radicals | `U+2F00–U+2FDF` | The 214 canonical 康熙部首 Kangxi radicals (`U+2F00`–`U+2FD5` assigned): `⼀` one (`U+2F00`), `⼈` man (`U+2F08`), `⼝` mouth (`U+2F1D`), `⼥` woman (`U+2F25`), `⽔` water (`U+2F54`), `⽕` fire (`U+2F55`); the indexing radicals by which 汉字/漢字 are organized in dictionaries (distinct from the unified-ideograph forms used in running text). |
| Bopomofo | `U+3100–U+312F` | The 注音符號 Zhuyin/Bopomofo phonetic letters (first assigned `ㄅ` at `U+3105`): the 21 initials `ㄅㄆㄇㄈ`…`ㄙ` (`U+3105`–`U+3119`), the rimes/medials `ㄚㄛㄜㄝ ㄞㄟㄠㄡ ㄢㄣㄤㄥ ㄦ` (`U+311A`–`U+3126`), and `ㄧㄨㄩ` (`U+3127`–`U+3129`); the Zhuyin reader tier (transcoded from toneless Pinyin). |
| Bopomofo Extended | `U+31A0–U+31BF` | Extended Bopomofo letters (`U+31A0`–`U+31BF`, e.g. `ㆠ` BU at `U+31A0` … `ㆿ` AH at `U+31BF`) for non-Mandarin Sinitic varieties (Minnan/Hokkien, Hakka, etc.); not used for Standard Mandarin but part of the Zhuyin script family. |
| CJK Unified Ideographs | `U+4E00–U+9FFF` | The core 汉字/漢字 (Hànzì) — the logographic characters of the Simplified and Traditional reader tiers: 一 (`U+4E00`), 人 (`U+4EBA`), 水 (`U+6C34`), 妈 (`U+5988`) / 媽 (`U+5ABD`), 马 (`U+9A6C`) / 馬 (`U+99AC`), 你 (`U+4F60`), 好 (`U+597D`), 汉 (`U+6C49`) / 漢 (`U+6F22`), 语 (`U+8BED`) / 語 (`U+8A9E`); each character ≈ one syllable + morpheme. |
| CJK Unified Ideographs Extension A | `U+3400–U+4DBF` | Rarer and historical 汉字/漢字 (`㐀` `U+3400` … `䶿` `U+4DBF`) beyond the core block; occasionally needed for uncommon surnames, place names, and classical characters in the Hanzi reader tiers. |
| CJK Unified Ideographs Extension B | `U+20000–U+2A6DF` | Supplementary-plane 汉字/漢字 (`𠀀` `U+20000` … `𪛟` `U+2A6DF`) for very rare and historical characters; further extensions (C, D, E, F, G, H) continue beyond `U+2A6DF` and are not enumerated here. Requires a font with SIP coverage to render. |

---

*编订 / Compiled by Shin.*

## Cross-Reference to the Companion Guides

Cross-reference relating this Mandarin Chinese (官话 / 官話, Standard Mandarin 标准汉语 / 標準漢語) IPA pronunciation guide to its **seven** companion guides: the two Indo-European guides — **English** and **Spanish** — the three Afroasiatic Semitic guides — **Classical Syriac (Peshitta)**, **Biblical Aramaic**, and **Biblical Hebrew** — and the two other East Asian guides, **Korean** (한국어) and **Japanese** (日本語). Mandarin is the THIRD CJK-region guide (after Korean and Japanese) and, far more pointedly, the FIRST TONAL guide in the entire family (four contrastive lexical tones plus a neutral tone), the FIRST LOGOGRAPHIC guide (written in 汉字 / 漢字 Hanzi, where each character ≈ one syllable and one morpheme, in two character standards — Simplified 简体字 and Traditional 繁體字), and the FIRST ANALYTIC / ISOLATING guide (minimal inflection, grammar carried by word order and free function words / particles, with a strong one-syllable-per-morpheme tendency).

Genetically Mandarin is **Sino-Tibetan › Sinitic** — a large, securely established family — so it is unrelated to all the Indo-European and Semitic guides and, crucially, unrelated to its fellow CJK guides Korean and Japanese as well: the CJK grouping is areal and graphic (centuries of Hanzi-based literary contact, shared Sino-vocabulary in Korean and Japanese), NOT genetic. Where the Semitic guides cross-reference one another within a single family, and the Indo-European guides cross-reference one another as branches of one stock, this section is contrastive on every front: it documents the wide typological gap between Mandarin and BOTH the Indo-European and the Semitic blocks, AND the sharp contrast between Mandarin and its fellow CJK guides — Korean and Japanese are agglutinative, rigidly head-final SOV, with phonographic native scripts (featural Hangul / moraic kana) and prosody that is non-lexical (Korean) or pitch-accent (Japanese), whereas Mandarin is analytic/isolating, SVO and topic-prominent, written logographically, and bears a full system of contrastive LEXICAL TONE.

The shared descriptive apparatus (IPA 2015, phonemic vs phonetic notation, articulatory place/manner classification) is what lets all eight guides be read against one another. This is a contrastive bridge, NOT a claim of genetic relationship: Mandarin is related to none of the other seven; only the IPA framework is fully shared. Mandarin is documented here in TWO parallel reference standards — **普通话 Pǔtōnghuà** (PRC Standard Mandarin, Beijing-based phonology, Simplified characters, Hanyu Pinyin) and **國語 Guóyǔ** (Taiwan Standard Mandarin, Traditional characters, Zhuyin/Bopomofo) — the Mandarin analogue of the English guide's GA/RP pairing, the Spanish guide's Castilian/Latin-American pairing, the Korean guide's South/North pairing, and the Japanese guide's Tokyo/Kansai pairing.

### Shared Framework

All eight guides (Mandarin, Korean, Japanese, English, Spanish, Peshitta, Biblical Aramaic, Biblical Hebrew) are built on the same descriptive linguistic apparatus, which makes their pronunciation data directly comparable even though Mandarin is unrelated to every one of the other seven.

- **Primary and sole pronunciation system is the International Phonetic Alphabet (IPA), 2015 revision**; orthography is never the authoritative phonetic record — and Mandarin orthography is especially unreliable as a sound record because it is LOGOGRAPHIC (each 汉字 / 漢字 writes a morpheme/syllable but its citation pronunciation, and above all its TONE, is not recoverable from the glyph; many characters are 多音字 with more than one reading, e.g. `行` háng 'row' vs xíng 'to go', `重` zhòng 'heavy' vs chóng 'repeat'), so IPA — supplemented by the toneless pinyin/zhuyin spine — is indispensable.
- **Phonemic transcriptions are written between /slashes/; narrow phonetic transcriptions between [brackets].** Mandarin leans on this distinction for its apical 'buzzed' vowels (the pinyin `-i` written [ɹ̩] after z/c/s as in `资` zī, and [ɻ̩] after zh/ch/sh/r as in `知` zhī), for retroflex realizations, and for erhua (儿化 / 兒化) rhotacization (`花` huā → `花儿` / `花兒` huār [xwɑɚ̯]).
- **Consonants are classified by place, manner, and — for Mandarin — by ASPIRATION rather than voicing** (the IPA pulmonic consonant chart). This is a fundamental cross-guide difference: the Indo-European and Semitic guides and Japanese use a TWO-WAY VOICING contrast (/p/ vs /b/), Korean uses a THREE-WAY lax/tense/aspirated laryngeal system, but Mandarin obstruents have NO voicing contrast at all — the contrast in each stop/affricate pair is unaspirated vs aspirated (b /p/ vs p /pʰ/, d /t/ vs t /tʰ/, g /k/ vs k /kʰ/, z /ts/ vs c /tsʰ/, zh /ʈʂ/ vs ch /ʈʂʰ/, j /tɕ/ vs q /tɕʰ/).
- **Vowels are classified by height, backness, and roundedness** (the IPA vowel chart); Mandarin's nuclei /a o ɤ ɛ i u y/ combine with the medial glides /j w ɥ/ and the codas /n ŋ/ into a system of ~35–38 finals, built from a small set of monophthongs plus diphthongs (ai ei ao ou) and triphthongs (iao iou uai uei). Mandarin has NO phonemic vowel length (unlike English, Japanese, and the Semitic guides) — vowel duration tracks tone and stress, not lexical contrast — and it adds the front rounded vowel /y/ (pinyin ü, as in `鱼` / `魚` yú [y]) shared with conservative Korean but absent from English, Spanish, Japanese, and the Semitic guides.
- **Suprasegmental marks are shared where relevant:** aspiration `ʰ` (heavily used, since aspiration not voicing is the obstruent contrast), the tie bar `◌͡◌` for affricates ([t͡s t͡sʰ ʈ͡ʂ ʈ͡ʂʰ t͡ɕ t͡ɕʰ]), the syllabic ring `◌̩` for the apical vowels [ɹ̩ ɻ̩], and the rhotic hook for erhua [ɚ]. Crucially, Mandarin uses NO stress mark (`ˈ`) as its primary suprasegmental and NO Japanese-style downstep — instead its signature suprasegmental is LEXICAL TONE, notated with the IPA tone-letter staves (˥ ˦ ˧ ˨ ˩) or Chao tone numerals: T1 阴平 / 陰平 high-level ˥ (55) `妈` / `媽` mā, T2 阳平 / 陽平 rising ˧˥ (35) `麻` má, T3 上声 / 上聲 low-dipping ˨˩˦ (214) `马` / `馬` mǎ, T4 去声 / 去聲 high-falling ˥˩ (51) `骂` / `罵` mà, plus the short, context-dependent NEUTRAL tone 轻声 / 輕聲 (`吗` / `嗎` ma).
- **Each guide documents two parallel reference traditions of one language:** Mandarin uses 普通话 Pǔtōnghuà (PRC, Beijing-based, Simplified characters, Hanyu Pinyin) and 國語 Guóyǔ (Taiwan, Traditional characters, Zhuyin/Bopomofo); Korean uses Standard South Korean (표준어, Seoul) and North Korean (문화어, Pyongyang); Japanese uses Standard/Common Japanese (標準語/共通語, Tokyo-type 東京式) and Kansai/Keihan (関西弁/京阪式); English uses General American (GA) and Received Pronunciation (RP/SSBE); Spanish uses its own paired reference standards (Castilian/Latin-American); the Semitic guides use Eastern/Western (Peshitta) or reconstructed reading traditions (e.g. Tiberian for Hebrew and Biblical Aramaic).

> **Note:** Because the framework is identical, an IPA symbol means the same articulatory target in every guide. /m/, /n/, /s/, /f/, /l/, /j/, /w/ denote the same sounds in Mandarin as in Korean, Japanese, English, Spanish, Syriac, Aramaic, or Hebrew; only the phoneme inventories, distributions, allophonic rules, the laryngeal organization (aspiration vs voicing vs three-way), the syllable architecture, and the suprasegmental systems differ. Mandarin's three most distinctive contributions to the set are **(1) LEXICAL TONE** — Mandarin is the FIRST guide whose every syllable bears a contrastive pitch contour (four tones plus neutral), so that 妈/麻/马/骂 (媽/麻/馬/罵) mā/má/mǎ/mà = 'mother/hemp/horse/scold' differ in tone alone; **(2) an ASPIRATION-not-voicing obstruent system** with the unusual three-way coronal place split among affricates (dental z/c /ts tsʰ/ vs retroflex zh/ch /ʈʂ ʈʂʰ/ vs alveolo-palatal j/q /tɕ tɕʰ/); and **(3) a LOGOGRAPHIC script** in which the written form carries morpheme and (citation) syllable but not a recoverable tone — the reason the Peshitta Hanzi reader tiers unavoidably impose an artifact citation tone. None of the three has a true counterpart in any other guide: the closest prosodic neighbors are Japanese pitch accent (one downstep per word, not a contour on every syllable) and the lexical stress of the Indo-European guides, but a full system of per-syllable contrastive tone is Mandarin-specific here.

### Typological Contrasts

Each row sets Mandarin against its three companion blocks — its fellow CJK guides (Korean, Japanese), the Indo-European guides (English, Spanish), and the Semitic guides (Syriac, Biblical Aramaic, Biblical Hebrew). Mandarin is genetically unrelated to all of them; only the IPA framework is shared.

#### Language family

| Block | Description |
|---|---|
| **Mandarin** | Sino-Tibetan › Sinitic. Mandarin (官话 / 官話) is the largest Sinitic branch; ISO 639-3 `cmn`, within the macrolanguage Chinese (`zho`). Sino-Tibetan is a large, securely established family, but it includes NONE of the companion guides — Mandarin has no proven genetic tie to any of them, not even to its fellow CJK guides Korean and Japanese. |
| **Korean** | Koreanic; Korean is almost universally treated as a language ISOLATE. Its deep Sino-Korean vocabulary and former Hanja use are the fruit of CONTACT with Chinese, not kinship — so although both are CJK-region, Korean and Mandarin are documented here as areal/typological neighbors, not relatives. |
| **Japanese** | Japonic (Japanese with the Ryukyuan languages), a small family with no securely demonstrated wider relatives. Like Korean, Japanese borrowed massive Sino-Japanese (漢語) vocabulary and the 漢字 script from Chinese — again contact, not common descent. |
| **Indo-European** | English is Indo-European › Germanic › West Germanic; Spanish is Indo-European › Italic › Romance (Ibero-Romance). The two IE guides are related to one another (branches of one stock) but NOT to Mandarin. |
| **Semitic** | Syriac and Biblical Aramaic are Afroasiatic › Semitic › Northwest Semitic (Aramaic branch); Biblical Hebrew is Northwest Semitic (Canaanite branch). The Semitic three are closely related to one another but unrelated to Mandarin and to the Indo-European and CJK guides. |

#### Position in the guide family (firsts)

| Block | Description |
|---|---|
| **Mandarin** | Mandarin is the THIRD East Asian / CJK-region guide (after Korean and Japanese) but the FIRST TONAL guide of the whole set (four contrastive lexical tones + a neutral tone), the FIRST LOGOGRAPHIC guide (written in 汉字 / 漢字, each character ≈ one morpheme/syllable, in two character standards Simplified 简体字 / Traditional 繁體字), and the FIRST ANALYTIC / ISOLATING guide (minimal inflection; grammar via word order + free particles; near one-to-one morpheme↔syllable↔character). It is therefore the family's first window onto contrastive lexical tone, onto logographic writing, and onto isolating morphology. |
| **Korean** | Korean was the FIRST non-Indo-European, non-Semitic, East Asian, isolate, agglutinative, featural-script guide, organized by a three-way laryngeal contrast. Against it, Mandarin contrasts on morphology (analytic/isolating vs agglutinative), word order (SVO vs SOV), script (logographic Hanzi vs featural Hangul syllable blocks), laryngeal system (aspiration-only vs lax/tense/aspirated), and prosody (lexical tone vs accentual-phrase intonation with no lexical pitch or stress). |
| **Japanese** | Japanese was the FIRST guide written in a moraic syllabary (kana), the first mixed multi-script guide (漢字 + ひらがな + カタカナ), the first mora-timed, and the first with lexical PITCH ACCENT. Mandarin and Japanese SHARE the use of 漢字/汉字 as a (or the) native script — the one strong graphic resemblance in the set — but Mandarin uses Hanzi as its sole, fully logographic system (no kana companion), and its prosody is a full per-syllable TONE system, not Japanese's single per-word downstep. |
| **Indo-European** | English and Spanish are fusional Indo-European languages written in the segmental Latin alphabet — part of the established 'core' against which Mandarin's tonal, logographic, isolating novelty is measured. |
| **Semitic** | Peshitta, Biblical Aramaic, and Biblical Hebrew are root-and-pattern Afroasiatic languages written in right-to-left abjads — themselves a strong contrast to the IE guides, and even further from Mandarin's logographic script, isolating morphology, and lexical tone. |

#### Morphological type

| Block | Description |
|---|---|
| **Mandarin** | ANALYTIC / ISOLATING: minimal inflection — verbs do not conjugate for person/number/tense and nouns do not decline; grammatical relations are carried by WORD ORDER and free function words/particles. Aspect and mood are marked by separable particles (`了` le perfective/inchoative, `着` / `著` zhe durative, `过` / `過` guo experiential, `的` de attributive/nominalizer), plurality on pronouns by `们` / `們` men, and Mandarin is a CLASSIFIER (measure-word) language (`三本书` / `三本書` sān běn shū 'three [CL] book(s)'). There is a strong ONE-SYLLABLE-PER-MORPHEME tendency, each morpheme normally written with its own character. Compare a single Mandarin clause `他 已经 把 书 看 完 了` / `他 已經 把 書 看 完 了` (tā yǐjīng bǎ shū kàn wán le, 'he has already finished reading the book') — six free words plus a particle, no inflection. |
| **Korean** | AGGLUTINATIVE: transparent suffixes and particles string onto a stem (`가다` 'go' → `가시었습니다` ga-si-eoss-seumnida). Mandarin is at the opposite pole — it adds free particles, not bound agglutinated suffixes, and keeps morphemes as separate (often monosyllabic) words. |
| **Japanese** | AGGLUTINATIVE in the same one-suffix-one-meaning style (`食べる` taberu → `食べさせられませんでした` tabe-sase-rare-masen-deshita). Like Korean, structurally the opposite of Mandarin's isolating profile. |
| **Indo-European** | English is concatenative/fusional with strong analytic tendencies (and is, of the IE two, the closer in spirit to Mandarin's reliance on word order and function words); Spanish is more richly fusional, packing tense/aspect/person/number into single endings (Spanish *hablábamos*). Neither reaches Mandarin's near-total absence of inflection. |
| **Semitic** | Root-and-pattern (templatic, nonconcatenative): meaning is built from a discontinuous triconsonantal root interleaved with vowel/consonant templates (k-t-b → *katab, ktib, maktub*). This interdigitation is the structural antithesis of Mandarin's isolating, one-morpheme-one-syllable design — Semitic and Mandarin morphology lie at opposite ends of the typological space, with the agglutinative CJK guides in between. |

#### Basic word order

| Block | Description |
|---|---|
| **Mandarin** | Basically SVO (Subject–Verb–Object) and strongly TOPIC-PROMINENT (the topic, often fronted, organizes the clause: `这本书我看过` / `這本書我看過` 'this book, I've read [it]'). It uses both PREpositions and POSTpositions (coverbs like `把` bǎ, `被` bèi precede; localizers like `上` shàng 'on', `里` / `裡` lǐ 'in' follow), relative clauses and most modifiers PRECEDE the head noun (with `的` de), and Mandarin is freely pro-drop. It is verb-MEDIAL like the Indo-European guides, not verb-final like the CJK guides nor verb-initial like the Semitic guides. |
| **Korean** | Rigidly head-final SOV with postpositions, prenominal relative clauses, and pro-drop. Mandarin shares the prenominal-modifier and pro-drop traits but is verb-MEDIAL SVO, not verb-final — a clear split from its CJK neighbor. |
| **Japanese** | Also rigidly head-final SOV with postpositions and prenominal relatives. As with Korean, Mandarin's SVO order separates it from both other CJK guides despite the shared CJK label. |
| **Indo-European** | English and Spanish are basically SVO and use prepositions; Romance allows freer subject placement than English. Mandarin's unmarked SVO aligns it with the IE block on this single axis — though Mandarin's strong topic-prominence and serial-verb constructions still set it apart. |
| **Semitic** | Classical Syriac, Biblical Aramaic, and Biblical Hebrew tend toward VSO (verb-initial), especially in narrative (Hebrew *wayyiqtol* chains). Mandarin's verb-MEDIAL SVO is thus distinct from the Semitic verb-INITIAL tendency and from the CJK verb-FINAL pattern — it sits with the Indo-European guides in the middle of the word-order spectrum. |

#### Writing system, structure, and direction

| Block | Description |
|---|---|
| **Mandarin** | A LOGOGRAPHIC system: 汉字 / 漢字 (Hanzi), where each character writes one MORPHEME and (citation) SYLLABLE — a near one-to-one character↔syllable↔morpheme correspondence (`马` / `馬` mǎ 'horse', `妈` / `媽` mā 'mother'). Characters are built from radicals (部首) and components, mostly 形声 / 形聲 phono-semantic compounds (`妈` / `媽` = `女` semantic + `马` / `馬` mǎ phonetic), written with conventional stroke order (笔顺 / 筆順). Two character STANDARDS are documented in parallel — SIMPLIFIED 简体字 (PRC, with Pǔtōnghuà) and TRADITIONAL 繁體字 (Taiwan/HK/Macau, with Guóyǔ): `马`/`馬`, `妈`/`媽`, `汉`/`漢`, `语`/`語`, `国`/`國`, `学`/`學`. Mandarin is normally written left-to-right (横排 / 橫排); traditional vertical top-to-bottom right-to-left columns (直排 / 豎排) persist in Taiwan/HK literary typesetting. The CRITICAL graphic fact for cross-reference: the glyph carries the morpheme but NOT a recoverable tone (and many are 多音字 with multiple readings), so pinyin (汉语拼音 / 漢語拼音, tone diacritics) and zhuyin/bopomofo (注音符號, 37 letters `ㄅㄆㄇㄈ` + tone marks) annotate pronunciation. Mandarin is the only guide whose native script is fully logographic. |
| **Korean** | Hangul (한글), left-to-right, a FEATURAL alphabet whose jamo compose into square SYLLABLE BLOCKS (onset/medial/coda). Korean writes sounds fully and phonemically; Mandarin writes morphemes and leaves tone unwritten in the glyph. Both are non-Latin native scripts needing their own reader tier, but they are structurally opposite (sound-writing alphabet vs morpheme-writing logographs). |
| **Japanese** | A mixed three-script system — logographic 漢字 (kanji) + two moraic kana (ひらがな / カタカナ). Mandarin SHARES the logographic 汉字/漢字 with Japanese (the family's one real script overlap), but uses Hanzi alone, with a single reading per word/sense (no kana, no parallel native/Sino reading layers), and adds the tone the kanji cannot show. |
| **Indo-European** | English and Spanish use the Latin (Roman) alphabet, a segmental alphabet written left-to-right with separate consonant and vowel letters; letter shapes are arbitrary. Neither is syllabic or logographic — the opposite of Mandarin's morpheme-per-glyph design. |
| **Semitic** | Syriac uses the Syriac abjad; Biblical Aramaic and Biblical Hebrew use the Hebrew square abjad — both written RIGHT-to-LEFT, encoding consonants and marking vowels only optionally (Syriac dots; Tiberian niqqud). Mandarin differs on every axis: default left-to-right direction, logographic (not consonantal-alphabetic) design, full syllable/morpheme representation per glyph, and an unwritten tone supplied only by annotation. |

#### Phonological unit and syllable structure

| Block | Description |
|---|---|
| **Mandarin** | The fundamental unit is the SYLLABLE, analysed in the native model as INITIAL (声母 / 聲母 shēngmǔ) + FINAL (韵母 / 韻母 yùnmǔ) + TONE (声调 / 聲調 shēngdiào). The shape is **(C)(G)V(C) + TONE**: an optional initial consonant, an optional medial glide /j w ɥ/, a vowel nucleus, and a coda restricted to /n/, /ŋ/ (-ng), or the rhotic /ɚ/ (er / 儿化 erhua). There are NO consonant clusters and NO other codas. The inventory is famously small and closed: ~400 toneless syllables, expanding to ~1300 tone-bearing syllables, with a near one-to-one syllable↔morpheme↔character mapping. This compact open-ish CV(N) canon means rendering Aramaic into Mandarin requires APPROXIMATION and forced epenthesis (Aramaic clusters and its many coda consonants must be broken up or dropped, since Mandarin permits only -n / -ng / -r codas). |
| **Korean** | Korean's unit is the syllable in syllable blocks; it permits (C)(G)V(C) with codas NEUTRALIZED to 7 sounds. Korean tolerates a wider range of coda consonants (final stops/laterals) than Mandarin's -n/-ng/-er only, so a Korean CVC of the type `밥` bap is impossible as a Mandarin syllable. |
| **Japanese** | Japanese counts by the MORA and is mora-timed, with an open-CV canon and only the moraic `ん` /N/ and sokuon `っ` /Q/ as 'codas'. Mandarin and Japanese are both restrictive at the syllable edge, but Mandarin counts by the (tone-bearing) syllable, allows the nasal codas -n/-ng and the rhotic -er, and has no gemination. |
| **Indo-European** | English is stress-timed and permits heavy clusters at both edges (*strengths* /strɛŋkθs/); Spanish is more syllable-timed but still licenses onset clusters and codas far beyond Mandarin's. Both allow syllable shapes Mandarin's (C)(G)V(N) frame forbids. |
| **Semitic** | Semitic syllables center on the consonantal root and tolerate clusters and codas Mandarin bans. Mandarin's small closed syllable inventory and its three-coda limit are, together with tone, its signature deviation from every companion. |

#### Core laryngeal organization of obstruents

| Block | Description |
|---|---|
| **Mandarin** | An ASPIRATION contrast with NO VOICING — unique in the set. Each stop/affricate pair is unaspirated vs aspirated, all voiceless: b /p/ vs p /pʰ/, d /t/ vs t /tʰ/, g /k/ vs k /kʰ/; z /ts/ vs c /tsʰ/, zh /ʈʂ/ vs ch /ʈʂʰ/, j /tɕ/ vs q /tɕʰ/. There are no voiced obstruent phonemes (the only voiced obstruent-like sound is r /ʐ ~ ɻ/). English speakers must NOT hear pinyin b/d/g as voiced [b d ɡ] (they are unaspirated voiceless [p t k]) and must supply true aspiration on p/t/k. |
| **Korean** | A THREE-WAY laryngeal contrast — lax /k t p tɕ/ vs tense /k͈ t͈ p͈ tɕ͈ s͈/ vs aspirated /kʰ tʰ pʰ tɕʰ/ — also with no phonemic voicing. Korean and Mandarin AGREE in lacking a voicing contrast, but differ in the dimensions used: Korean adds a tense series and a separate aspirated series, while Mandarin has only the two-way unaspirated/aspirated split and no tense fortis series. |
| **Japanese** | A TWO-WAY VOICING contrast (/p t k s/ vs /b d ɡ z/) with no aspiration contrast — exactly the opposite organizing dimension from Mandarin. Where Japanese opposes /k/ to /ɡ/, Mandarin opposes unaspirated /k/ to aspirated /kʰ/ (both voiceless). |
| **Indo-European** | English and Spanish both use a TWO-WAY VOICING contrast (/p/ vs /b/, etc.); English aspirates voiceless stops in stressed onset ([pʰ tʰ kʰ]) ALLOPHONICALLY, while Spanish keeps them unaspirated. Mandarin is the mirror image: it makes aspiration CONTRASTIVE and discards voicing entirely. |
| **Semitic** | The Semitic guides use voicing AND add the EMPHATIC (pharyngealized) set (Teth /tˤ/, Tsade /sˤ/) plus Begadkephat hard~soft spirantization. Mandarin has neither voicing nor emphatics; its distinctive obstruent traits are the aspiration contrast and the three-way coronal place split (dental /ts/ vs retroflex /ʈʂ/ vs alveolo-palatal /tɕ/). |

#### Consonant inventory — coronal affricates/sibilants and the guttural region

| Block | Description |
|---|---|
| **Mandarin** | Mandarin's most crowded zone is the CORONAL affricate/sibilant region, with a THREE-WAY place split found in no companion: DENTAL z/c/s /ts tsʰ s/ (`资` zī, `词` / `詞` cí, `思` sī), RETROFLEX zh/ch/sh/r /ʈʂ ʈʂʰ ʂ ʐ~ɻ/ (`知` zhī, `吃` chī, `是` shì, `日` rì), and ALVEOLO-PALATAL j/q/x /tɕ tɕʰ ɕ/ (`鸡` / `雞` jī, `七` qī, `西` xī) — the last in complementary distribution with the others, occurring before high front /i y/. In the back/glottal zone Mandarin has only h /x/ (a voiceless VELAR fricative, not glottal [h]); it has NO pharyngeals, NO emphatics, NO uvular /q/ (pinyin q is the alveolo-palatal affricate /tɕʰ/, NOT a uvular stop), and NO phonemic glottal stop. Its only nasals are m /m/, n /n/ (and -ng /ŋ/ in codas); its lateral is l /l/. |
| **Korean** | Korean's back zone has only /h/ (lenited/deleted), no pharyngeals/emphatics/uvulars; its single sibilant /s/ (plus tense /s͈/) palatalizes to [ɕ] before /i j/. Mandarin is far richer in the coronal region (three affricate series vs one) and uses velar /x/ rather than glottal /h/. |
| **Japanese** | Japanese has only /h/ ([ç]/[ɸ]/[h]) in the back zone, no pharyngeals/emphatics/uvulars; [ɕ tɕ] are allophones, not phonemes. Mandarin, by contrast, has /tɕ tɕʰ ɕ/ AND /ʈʂ ʈʂʰ ʂ/ AND /ts tsʰ s/ as distinct phoneme series — a much denser coronal system. |
| **Indo-European** | English adds /f v θ ð s z ʃ ʒ tʃ dʒ/ and an approximant rhotic [ɹ]; Spanish adds /f/, velar /x/, and a trill/tap /r ɾ/. Notably Mandarin's h /x/ matches Spanish /x/ (jota) in place, and Mandarin's retroflex zh/ch/sh have no clean IE equivalent (English postalveolar /tʃ ʃ/ is the nearest but not identical). |
| **Semitic** | The Semitic guides add the full guttural/emphatic apparatus — pharyngeals /ħ/ (Heth) and /ʕ/ (Ayin), glottals /ʔ/ (Aleph) and /h/, emphatics /tˤ sˤ/, uvular /q/ (Qoph). Mandarin shares with them essentially none of this: its /x/ is velar (not the glottal /h/ or pharyngeal /ħ/), and ʕ ħ q tˤ sˤ ʔ have no Mandarin counterpart and must be approximated in the Hanzi/pinyin reader tiers. |

#### Vowel inventory and length

| Block | Description |
|---|---|
| **Mandarin** | A medium nuclear inventory /a o ɤ ɛ i u y/ combining with medials /j w ɥ/ and codas /n ŋ/ into ~35–38 FINALS, including diphthongs (ai ei ao ou) and triphthongs (iao iou uai uei). Distinctive features: the front ROUNDED vowel /y/ (pinyin ü, `鱼` / `魚` yú [y]); the unrounded back/central /ɤ/ (pinyin e, `饿` / `餓` è); and the APICAL 'buzzed' syllabic vowels written `-i`, namely [ɹ̩] after z/c/s (`资` zī [tsɹ̩]) and [ɻ̩] after zh/ch/sh/r (`知` zhī [ʈʂɻ̩]) — these are NOT [i]. Mandarin has NO PHONEMIC VOWEL LENGTH (vowel duration follows tone/stress, not lexical contrast). It adds ERHUA (儿化 / 兒化), an -r suffix that rhotacizes the whole final (`一点` / `一點` yìdiǎn → `一点儿` / `一點兒` yìdiǎnr). |
| **Korean** | A 7–8 monophthong system (/a ʌ o u ɯ i e/) with on-glide diphthongs and (conservatively) front rounded /ø y/, no phonemic length, little reduction. Korean and Mandarin OVERLAP on front rounded /y/ (Mandarin ü ~ Korean ㅟ/ㅢ-area) and on lacking phonemic length, but Mandarin adds the apical syllabic vowels and erhua, which Korean lacks. |
| **Japanese** | A compact 5-vowel /a i ɯ e o/ with PHONEMIC LENGTH and high-vowel devoicing. Mandarin diverges sharply: it has no phonemic length, has the front rounded /y/ and the apical vowels Japanese lacks, and its high back vowel is true rounded /u/, not Japanese's unrounded [ɯ̈]. |
| **Indo-European** | English has a large reducing system (~11–12 monophthongs + phonemic diphthongs, pervasive schwa, phonemic length-or-quality); Spanish has a clean 5-vowel /a e i o u/ with no length. Neither IE guide has the front rounded /y/ that Mandarin's ü carries — within this set that vowel aligns Mandarin instead with conservative Korean (ㅟ), the closest companion match. Unlike English, Mandarin has no phonemic length and no nasal vowels (its nasality is in the -n/-ng CODA, not the vowel). |
| **Semitic** | Smaller systems (Peshitta Eastern 7, Western 5; Tiberian 7) with a reduced vowel (shewa) and length that is meaningful in places. Mandarin lacks shewa and lacks phonemic length, has the front rounded /y/ and apical vowels they do not, and builds diphthongs/triphthongs from vowel+glide sequences. |

#### Signature phonological / sandhi rules

| Block | Description |
|---|---|
| **Mandarin** | Mandarin's pronunciation grammar is dominated by TONE SANDHI and connected-speech tone changes — processes with no real counterpart elsewhere: **(1) THIRD-TONE SANDHI**, T3+T3 → T2+T3 (`你好` nǐ hǎo → ní hǎo), and a non-final T3 before another tone reduces to a low 'half-third'; **(2) 一 yī alternation** (→ yì before T1/T2/T3, → yí before T4); **(3) 不 bù alternation** (→ bú before T4); **(4) the NEUTRAL tone** (轻声 / 輕聲) on particles (`的` `了` `吗`/`嗎` `呢`) and some suffixes (`子` `头`/`頭`); and **(5) ERHUA** (儿化 / 兒化) rhotacization that restructures the rime (`花` huā → `花儿` / `花兒` huār). Segmentally there is little allophony beyond the apical-vowel and erhua effects; the action is in the tones. |
| **Korean** | Korean's grammar of pronunciation is a dense stack of obligatory CODA/boundary SANDHI — 연음 liaison, 비음화 nasalization, 유음화 lateralization, 경음화 tensification, 격음화 aspiration, 구개음화 palatalization, ㄴ-첨가 n-insertion, 7-sound coda neutralization. Both Mandarin and Korean are 'rule-rich', but the locus differs entirely: Korean's rules are SEGMENTAL coda sandhi, Mandarin's are TONAL (pitch) sandhi. |
| **Japanese** | Japanese concentrates its rules in following-vowel allophony (/s/→[ɕ], /t/→[t͡ɕ]/[t͡s], /h/→[ç]/[ɸ]), the special moras /N/ /Q/, devoicing, and rendaku. Mandarin's segmental allophony is comparatively light; its signature processes are tonal, which Japanese (a pitch-accent, not tone-sandhi, language) does not have. |
| **Indo-European** | English has assimilation, flapping, and reduction; Spanish has /b d ɡ/ spirantization. Real but segmental — neither involves contour-tone sandhi. |
| **Semitic** | Begadkephat spirantization and gemination are the headline Semitic processes. None of the other guides has anything like Mandarin's tone sandhi: the manipulation of contrastive PITCH CONTOURS in connected speech is Mandarin-specific in this set. |

#### Suprasegmentals: stress, tone, pitch, and prosody

| Block | Description |
|---|---|
| **Mandarin** | Mandarin has LEXICAL, CONTRASTIVE TONE — its defining feature and the family's first true tone system. Every full syllable carries one of FOUR tones, plus a reduced NEUTRAL tone: T1 阴平 / 陰平 high-level ˥ (55) `妈` / `媽` mā; T2 阳平 / 陽平 rising ˧˥ (35) `麻` má; T3 上声 / 上聲 low-dipping ˨˩˦ (214) `马` / `馬` mǎ; T4 去声 / 去聲 high-falling ˥˩ (51) `骂` / `罵` mà; NEUTRAL 轻声 / 輕聲 short, pitch from context, `吗` / `嗎` ma. Tone is the SOLE distinguisher of the classic minimal set 妈/麻/马/骂 (媽/麻/馬/罵) = 'mother/hemp/horse/scold'. Pinyin marks tone with diacritics (ā á ǎ à); Zhuyin with tone marks (ˊ ˇ ˋ ˙, T1 unmarked). Stress exists only weakly and non-contrastively (a phrase-level prominence and the destressing that yields neutral tones); the workload that stress carries in the IE guides is borne in Mandarin by tone. |
| **Korean** | Standard Korean has NO lexical tone and NO lexical stress; prosody is accentual-phrase intonation (commonly LHLH). Mandarin and Korean are maximally opposed prosodically: Mandarin packs a contrastive contour onto every syllable, Korean has no lexical pitch at all (only some Korean dialects, e.g. Gyeongsang, keep lexical pitch — the nearest Korean analogue to Mandarin tone). |
| **Japanese** | Japanese has LEXICAL PITCH ACCENT — at most ONE downstep per word (頭高 / 中高 / 尾高 / 平板), e.g. `箸` ha\shi 'chopsticks' vs `橋` hashi\ 'bridge'. This is the closest companion to Mandarin tone, but it is fundamentally different: Japanese marks one pitch FALL per word, whereas Mandarin assigns a full pitch CONTOUR (level/rising/dipping/falling) to EACH syllable. Pitch accent is a privative single event; Mandarin tone is a per-syllable paradigm of four. |
| **Indo-European** | English has lexical, contrastive STRESS (ˈrecord vs reˈcord) and is stress-timed; Spanish has lexical contrastive stress (*término/termino/terminó*) and is syllable-timed. Both foreground STRESS, which Mandarin demotes — Mandarin substitutes contrastive lexical TONE for the contrastive role stress plays in English and Spanish. |
| **Semitic** | Stress in the Semitic guides is largely predictable from word structure (typically final or penultimate). Mandarin is the only guide of the eight with a full system of contrastive LEXICAL TONE on every syllable — a prosodic profile unlike any companion: Korean has phrase intonation, Japanese a downstep pitch accent, the IE guides stress or phrasing, the Semitic guides predictable stress, and Mandarin alone a four-way tone paradigm per syllable. |

#### Honorifics, classifiers, and other grammatical signatures

| Block | Description |
|---|---|
| **Mandarin** | Mandarin does NOT have the pervasive grammaticalized honorific verb morphology of the other two CJK guides; politeness is mostly LEXICAL (`您` nín polite 'you' vs `你` nǐ; `请` / `請` qǐng 'please'; humble/honorific vocabulary like `贵姓` / `貴姓` guìxìng) rather than encoded in obligatory verb suffixes. Its own grammatical signatures instead are: a rich CLASSIFIER / measure-word system (`个` / `個` ge, `本` běn, `张` / `張` zhāng, `条` / `條` tiáo…), aspect particles (`了` `着`/`著` `过`/`過`) in place of tense inflection, the `把` bǎ disposal and `被` bèi passive constructions, serial-verb and resultative-complement constructions (`看完` kàn wán 'finish reading', `听懂` / `聽懂` tīng dǒng 'understand by listening'), and topic-comment structure. So where Korean and Japanese grammaticalize SOCIAL DEIXIS, Mandarin grammaticalizes CLASSIFICATION and ASPECT — a different organizing logic. |
| **Korean** | Korean has a pervasive honorific/speech-level system (subject `-시-` -si-, addressee speech levels, honorific/humble vocabulary). This is a major CJK feature that Mandarin LACKS as grammaticalized morphology — one of the clearest splits between Mandarin and its East Asian neighbors. |
| **Japanese** | Japanese has the equally pervasive 敬語 keigo system (teineigo/sonkeigo/kenjōgo, お/ご prefixes). Like Korean's, this honorific apparatus has no grammaticalized equivalent in Mandarin, which handles respect lexically. |
| **Indo-European** | English has only lexical politeness; Spanish has a T/V pronoun distinction (*tú/usted*) — closer to Mandarin's 你/您 lexical politeness than to the CJK honorific morphology. Neither has Mandarin's obligatory classifier system. |
| **Semitic** | The Semitic guides have no comparable grammaticalized speech-level or classifier system. Mandarin's classifier-and-aspect grammar is a signature it shares with no companion in this set. |

### Companion Guides

- **Peshitta** — `peshitta_pronunciation_guide.json`. Classical Syriac (Aramaic), the Peshitta reading tradition — the source text this whole project renders. Documents Eastern (Madnhaya) and Western (Serto) traditions in parallel, the Begadkephat spirantization rule, guttural and emphatic consonants, and the Syriac abjad (U+0700–U+074F). Unrelated to Mandarin (Afroasiatic vs Sino-Tibetan) and maximally distant in morphology (root-and-pattern vs analytic/isolating), script (right-to-left consonantal abjad vs logographic Hanzi), syllable structure (clusters/codas vs (C)(G)V(N) with only -n/-ng/-er codas), and prosody (predictable stress vs four-way lexical tone). It shares with Mandarin only a handful of plain IPA consonants (/m n s f l/ and a velar fricative ~ /x/); its pharyngeals, emphatics, glottal stop, and uvular /q/ have no Mandarin counterpart and must be approximated — with forced epenthesis and tone-as-artifact — in the pinyin, zhuyin, and Hanzi reader tiers.
- **Biblical Aramaic** — `biblical_aramaic_pronunciation_guide.json`. Biblical Aramaic / Jewish Literary Aramaic, as preserved in the Tiberian pointing of the Aramaic portions of the Hebrew Bible (Daniel, Ezra). Northwest Semitic (Aramaic branch); uses the Hebrew square abjad with Tiberian niqqud. Shares emphatic/guttural consonants and triconsonantal root morphology with Syriac and Hebrew; unrelated to Mandarin and contrasting with it on every major typological axis (family, morphology, word order, script, syllable shape, prosody). The closest Aramaic relative of the Peshitta's own language, useful to a Mandarin reader as the Semitic backbone behind the rendered text.
- **Biblical Hebrew** — `biblical_hebrew_pronunciation_guide.json`. Biblical (Classical) Hebrew in the Tiberian reading tradition. Northwest Semitic (Canaanite branch); uses the Hebrew square abjad with Tiberian niqqud. Notable for the prefixed definite article `/ha-/` with following gemination, the Tiberian uvular Resh `/ʁ/`, and a 7-vowel system with shewa; unrelated to Mandarin. Useful to a Mandarin reader mainly as a study in how a voicing-plus-emphatic-plus-guttural obstruent system (and a stress-based, cluster-tolerant, atonal prosody) differs from Mandarin's aspiration-based, open-CV(N), tonal profile.
- **English** — `English/english_pronunciation_guide.json`. Modern English (Indo-European > Germanic), documented in General American (GA) and Received Pronunciation (RP/SSBE). Shares with Mandarin the GA/RP-style two-standard format and basic SVO word order; differs sharply in being voicing-based (vs Mandarin aspiration-based — though English allophonic aspiration [pʰ tʰ kʰ] is exactly where Mandarin makes aspiration contrastive), fusional/analytic (vs isolating), stress-timed with lexical STRESS (vs Mandarin lexical TONE), cluster-tolerant (vs Mandarin's three-coda limit), and alphabetic (vs logographic). The English aspiration of stressed-onset stops is the single best entry point for teaching Mandarin's p/t/k vs b/d/g.
- **Spanish** — `Spanish/spanish_pronunciation_guide.json`. Modern Spanish (Indo-European > Italic > Romance), documented in Castilian (distinción) and Latin American (seseo). Shares with Mandarin the velar fricative /x/ (Spanish jota ~ Mandarin h /x/) and unaspirated voiceless stops (Spanish /p t k/ are unaspirated like Mandarin's b/d/g series in being non-aspirated — though Spanish ALSO voices /b d ɡ/, which Mandarin does not). Diverges on family, fusional morphology, lexical STRESS (vs tone), syllable-timing, the trill/tap contrast (Mandarin has neither), a clean 5-vowel system with no front rounded /y/, and the Latin alphabet. A useful comparison for Mandarin's /x/ and for unaspirated stops.
- **Korean** — `Korean/korean_pronunciation_guide.json`. Modern Korean (Koreanic isolate; the FIRST CJK / East Asian guide), documented in Standard South Korean (표준어, Seoul) and North Korean (문화어, Pyongyang). An AREAL CJK neighbor of Mandarin (centuries of Sino-Korean vocabulary and former Hanja use) but NOT a relative, and TYPOLOGICALLY opposite on most axes: Korean is agglutinative, rigidly head-final SOV, honorific-rich, with a three-way lax/tense/aspirated laryngeal system and no lexical tone or stress, written in featural Hangul syllable blocks — whereas Mandarin is analytic/isolating, SVO/topic-prominent, with an aspiration-only obstruent contrast and four-way lexical tone, written in logographic Hanzi. The two AGREE only in lacking a voicing contrast (different solutions: Korean's three-way system vs Mandarin's two-way aspiration) and in sharing a front rounded vowel region. The most instructive contrast for Mandarin as a non-agglutinative, tonal CJK guide.
- **Japanese** — `Japanese/japanese_pronunciation_guide.json`. Modern Japanese (Japonic; the SECOND CJK / East Asian guide), documented in Standard/Common Japanese (標準語/共通語, Tokyo-type 東京式) and Kansai/Keihan (関西弁/京阪式). The companion that SHARES Mandarin's logographic 汉字/漢字 script (Japanese kanji ARE Chinese characters, borrowed with their Sino-Japanese readings) — the one real graphic overlap in the set — yet is otherwise contrastive: Japanese is agglutinative head-final SOV, mora-timed with an open-CV moraic kana system and lexical PITCH ACCENT (one downstep per word), with a two-way VOICING obstruent contrast; Mandarin is analytic/isolating SVO, syllable-based with -n/-ng/-er codas, aspiration-not-voicing, and a per-syllable four-way TONE system, using Hanzi alone (no kana, single reading per word). Japanese pitch accent is the nearest prosodic neighbor to Mandarin tone, which makes it the best comparison for the difference between a one-downstep pitch accent and a four-contour-per-syllable tone system.

### Shared IPA Symbols

IPA symbols organized by how they relate Mandarin to its seven companions. Because Mandarin's obstruent system is built on ASPIRATION rather than voicing and has NO voiced obstruent phonemes, it shares FEWER plain stop/fricative symbols with the voicing-based guides than they share with one another: Mandarin overlaps cleanly on the NASALS, the lateral /l/, /f/, the glides /j w/, and the velar fricative /x/, while its hallmark RETROFLEX and AFFRICATE set (/ʈʂ ʈʂʰ ʂ ʐ/, /ts tsʰ/, /tɕ tɕʰ ɕ/) and its aspirated stops /pʰ tʰ kʰ/ are largely Mandarin-specific in this set. The Semitic-only pharyngeals (/ʕ ħ/), emphatics (/tˤ sˤ/), glottal stop /ʔ/, and uvular /q/ are absent from Mandarin entirely. The symbol denotes the same articulatory target in every guide; the languages differ in how these phonemes pattern, not in what the symbols mean.

| IPA | Name | Mandarin | Others |
|---|---|---|---|
| `m` | voiced bilabial nasal | /m/ — pinyin m, initial only (`妈` / `媽` mā, `马` / `馬` mǎ); not a coda in Mandarin | Korean/Japanese/English/Spanish /m/; Mem / Mim in all three Semitic guides — the same sound everywhere. NOTE: Mandarin uses /m/ only as an onset; the other guides also allow it in coda/closed syllables. |
| `n` | voiced alveolar nasal | /n/ — pinyin n; one of the very few Mandarin CODAS (-n, as in `安` ān, `民` mín) as well as an onset (`你` nǐ) | Korean/Japanese/English/Spanish /n/; Nun in all three Semitic guides. Mandarin's -n is one of only three permitted codas (-n, -ng, -er). |
| `ŋ` | voiced velar nasal | /ŋ/ — pinyin -ng; a CODA only (`中` zhōng, `行` háng/xíng, `风` / `風` fēng), never a Mandarin onset | English /ŋ/ (sing) and Korean /ŋ/ are full coda phonemes (Korean ㅇ in coda) — the closest match to Mandarin's coda -ng; Japanese [ŋ] is an allophone of /N/ and of intervocalic /ɡ/; in Spanish only an allophone of /n/ before velars; not a primary Semitic phoneme. Mandarin, Korean, and English agree in using /ŋ/ as a genuine coda phoneme. |
| `f` | voiceless labiodental fricative | /f/ — pinyin f (`发` / `發` fā, `飞` / `飛` fēi); an onset only | English/Spanish /f/; Japanese has only bilabial [ɸ] (an allophone of /h/), NOT /f/; Korean has no /f/ at all; Semitic spirantized Pe gives /f/. Mandarin sides with the IE and Semitic guides in having a true labiodental /f/, where the other two CJK guides do not. |
| `l` | voiced alveolar lateral approximant | /l/ — pinyin l (`来` / `來` lái, `六` liù); an onset only; Mandarin has /l/ AND a separate rhotic r /ʐ~ɻ/ | English/Spanish /l/; Korean /l ~ ɾ/ is a single liquid; Japanese has NO /l/ (loans map /l/→/r/); Lamadh / Lamed in the Semitic guides. Mandarin keeps /l/ and its rhotic distinct, unlike Japanese (no /l/) and Korean (one liquid). |
| `x` | voiceless velar fricative | /x/ — pinyin h (`好` hǎo, `喝` hē, `火` huǒ); a VELAR fricative, NOT the glottal [h] of most companions | Spanish has /x/ (jota: jamón, gente) — the closest match; otherwise the companions use glottal /h/ (English, Korean, Japanese, Semitic He) where Mandarin uses velar /x/. Mandarin and Spanish are the two guides whose 'h' is a velar fricative. |
| `j` | voiced palatal approximant (glide) | /j/ — the medial glide written i/y (medial in `加` jiā, `谢` / `謝` xiè; syllable-initial y in `一` yī, `也` yě) | Korean /j/ (야 ja); Japanese /j/ (や ya); English /j/ (yes); Spanish /j/ (tiene); Yodh / Yud in the Semitic guides — the same glide everywhere. In Mandarin it functions as a medial within the final, part of the initial+final architecture. |
| `w` | voiced labial-velar approximant (glide) | /w/ — the medial glide written u/w (medial in `国` / `國` guó, `我` wǒ; syllable-initial w in `万` / `萬` wàn) | Korean /w/ (와 wa); Japanese /w/ realized [ɰ]; English /w/ (we); Spanish /w/ (hueso); Waw / Vav (as glide) in the Semitic guides. Mandarin uses /w/ as a final-medial, paired with /j/ and the front-rounded medial /ɥ/ (ü-glide). |
| `y` | close front rounded vowel | /y/ — pinyin ü (and u after j/q/x/y): `鱼` / `魚` yú, `绿` / `綠` lǜ, `居` jū; also the medial glide /ɥ/ (`月` yuè) | Conservative Korean has /y/ (ㅟ) — the closest companion match, the best single front-rounded-vowel correspondence in this set; English, Spanish, Japanese, and the Semitic guides have NO front rounded /y/. Mandarin's ü aligns it specifically with conservative Korean. |
| `p` | voiceless bilabial plosive (Mandarin: unaspirated) | /p/ — pinyin b (`不` bù, `八` bā); UNASPIRATED voiceless [p], NOT voiced [b]; contrasts with aspirated p /pʰ/ | Spanish unaspirated /p/ (the closest realization); English /p/ is aspirated [pʰ] in stressed onset; Korean lax ㅂ /p/ (with tense ㅃ, aspirated ㅍ); Japanese voiceless /p/; Pe (hard allophone) in the Semitic guides. CRUCIAL: pinyin b = unaspirated [p], NOT [b] — a classic learner trap for speakers of voicing-based guides. |
| `pʰ` | voiceless aspirated bilabial plosive | /pʰ/ — pinyin p (`怕` pà, `朋` péng); the ASPIRATED partner of b /p/; aspiration is CONTRASTIVE | English has [pʰ] only ALLOPHONICALLY (stressed onset, e.g. pin); Korean aspirated ㅍ /pʰ/ is a phoneme (in a three-way system); Spanish lacks phonemic aspiration; the Semitic guides lack it. Mandarin (with Korean) makes aspiration CONTRASTIVE, but Mandarin's is a simple two-way unaspirated/aspirated split, unlike Korean's three-way system. |
| `t` | voiceless alveolar plosive (Mandarin: unaspirated) | /t/ — pinyin d (`大` dà, `多` duō); UNASPIRATED voiceless [t], NOT [d]; contrasts with aspirated t /tʰ/ | Spanish dental unaspirated /t/ is closest; English /t/ aspirated [tʰ] (GA intervocalic flap [ɾ]); Korean lax ㄷ /t/; Japanese /t/ ([t͡ɕ]/[t͡s] before high vowels); Taw in the Semitic guides. As with b, pinyin d = unaspirated [t], not voiced [d]. |
| `tʰ` | voiceless aspirated alveolar plosive | /tʰ/ — pinyin t (`他` tā, `听` / `聽` tīng); the ASPIRATED partner of d /t/ | English allophonic [tʰ]; Korean aspirated ㅌ /tʰ/ (phoneme); Spanish/Semitic lack phonemic aspiration. Contrastive in Mandarin and Korean. |
| `k` | voiceless velar plosive (Mandarin: unaspirated) | /k/ — pinyin g (`高` gāo, `个` / `個` gè); UNASPIRATED voiceless [k], NOT [ɡ]; contrasts with aspirated k /kʰ/ | Spanish unaspirated /k/ closest; English aspirated [kʰ] in stressed onset; Korean lax ㄱ /k/; Japanese /k/; Kaph in the Semitic guides. pinyin g = unaspirated [k], not voiced [ɡ]. |
| `kʰ` | voiceless aspirated velar plosive | /kʰ/ — pinyin k (`看` kàn, `开` / `開` kāi); the ASPIRATED partner of g /k/ | English allophonic [kʰ]; Korean aspirated ㅋ /kʰ/ (phoneme); Spanish/Semitic lack phonemic aspiration. Contrastive in Mandarin and Korean. |
| `ts` | voiceless dental affricate (unaspirated) | [t͡s] — pinyin z (`资` / `資` zī, `走` zǒu); the unaspirated DENTAL affricate; contrasts with aspirated c /tsʰ/ | Japanese [t͡s] is the allophone of /t/ before /u/ (つ); German/Italian have /ts/ but no companion here has it as a core onset series. Among the eight, Mandarin's dental-affricate SERIES (z/c) is essentially Mandarin-specific; the nearest is Japanese's single conditioned [t͡s]. |
| `tsʰ` | voiceless aspirated dental affricate | [t͡sʰ] — pinyin c (`词` / `詞` cí, `菜` cài); the ASPIRATED partner of z [t͡s] | No companion has a phonemic aspirated dental affricate; this is a Mandarin-specific contrast (the c of pinyin is NOT [k] or [s] — a frequent misreading by Latin-alphabet readers). |
| `ʈʂ` | voiceless retroflex affricate (unaspirated) | [ʈ͡ʂ] — pinyin zh (`知` zhī, `中` zhōng); the unaspirated RETROFLEX affricate; contrasts with aspirated ch /ʈʂʰ/; reduced toward [ts] in de-retroflexing Guóyǔ | No companion has retroflex affricates; the nearest are English/Spanish postalveolar /tʃ/ (English CHurch) — similar but NOT retroflex. The zh/ch/sh/r retroflex series is one of Mandarin's most distinctive contributions to the set. |
| `ʈʂʰ` | voiceless aspirated retroflex affricate | [ʈ͡ʂʰ] — pinyin ch (`吃` chī, `茶` chá); the ASPIRATED partner of zh [ʈ͡ʂ] | No companion has this sound; nearest is aspirated-onset /tʃ/ in English stressed onset, but that is postalveolar and only allophonically aspirated. Mandarin-specific. |
| `ʂ` | voiceless retroflex fricative | [ʂ] — pinyin sh (`是` shì, `山` shān); the RETROFLEX sibilant; reduced toward [s] in de-retroflexing Guóyǔ | No companion has retroflex /ʂ/; nearest is postalveolar /ʃ/ (English SHip) — similar but not retroflex. Part of Mandarin's signature retroflex series. |
| `ʐ` | voiced retroflex fricative / approximant | [ʐ ~ ɻ] — pinyin r (`日` rì, `人` rén, `热` / `熱` rè); the only voiced-obstruent-like Mandarin sound; the retroflex r, between a fricative [ʐ] and an approximant [ɻ]; also the basis of erhua [ɚ] | English postalveolar/retroflex approximant /ɹ/ (red) is the nearest in articulation (both retroflex-ish approximants), though English /ɹ/ is fully an approximant; no other companion has [ʐ]. Mandarin r is a notorious learner difficulty and has no clean equivalent in the set. |
| `tɕ` | voiceless alveolo-palatal affricate (unaspirated) | [t͡ɕ] — pinyin j (`鸡` / `雞` jī, `家` jiā); the unaspirated ALVEOLO-PALATAL affricate, before high front /i y/ only; contrasts with aspirated q /tɕʰ/ | Korean lax ㅈ /tɕ/ is the same alveolo-palatal place (a phoneme); Japanese [t͡ɕ] is the allophone of /t/ before /i/ (ち) — also alveolo-palatal. Nearest IE companion is postalveolar /tʃ/. The two CJK guides Korean and Japanese share the alveolo-palatal place with Mandarin's j; Mandarin's is unaspirated and contrasts with aspirated q. |
| `tɕʰ` | voiceless aspirated alveolo-palatal affricate | [t͡ɕʰ] — pinyin q (`七` qī, `去` qù, `请` / `請` qǐng); the ASPIRATED partner of j [t͡ɕ]; NOT a uvular or a [k] — a frequent misreading of the letter q | Korean aspirated ㅊ /tɕʰ/ is the same place with phonemic aspiration — the closest match in the set. No IE/Semitic companion has an aspirated alveolo-palatal affricate. pinyin q ≠ /k/ or /kw/; it is /tɕʰ/. |
| `ɕ` | voiceless alveolo-palatal fricative | [ɕ] — pinyin x (`西` xī, `小` xiǎo, `谢` / `謝` xiè); the ALVEOLO-PALATAL sibilant, before high front /i y/ only | Korean [ɕ] is the allophone of /s/ before /i j/; Japanese [ɕ] is the allophone of /s/ before /i/ (し) — both CJK parallels. Nearest IE companion is postalveolar /ʃ/. In Mandarin x = [ɕ], NOT [ks] or [z] (a frequent Latin-alphabet misreading). |

#### Mandarin-Specific or Divergent Features

Features and symbols where Mandarin stands apart from most or all companions — the inverse of the shared set.

- **LEXICAL TONE NOTATION** — the IPA tone letters / Chao numerals ˥ ˧˥ ˨˩˦ ˥˩ (55 / 35 / 214 / 51) for T1–T4 plus the neutral tone: used by NO other guide as a contrastive lexical feature (Japanese uses H/L pitch-accent notation for a single downstep; the others use stress marks `ˈ` `ˌ`). This is the single biggest divergence.
- **APICAL / 'BUZZED' SYLLABIC VOWELS** — [ɹ̩] after z/c/s (`资` zī) and [ɻ̩] after zh/ch/sh/r (`知` zhī), written `-i` in pinyin but NOT the vowel [i]: no companion has these apical syllabic vowels.
- **ERHUA RHOTACIZATION** — the suffix -r /ɚ/ (儿化 / 兒化) that rhotacizes an entire final (`花儿` / `花兒` huār): a Mandarin-specific (and Pǔtōnghuà-characteristic, Guóyǔ-reduced) process with no companion equivalent.
- **THE RETROFLEX SERIES** — /ʈʂ ʈʂʰ ʂ ʐ/ (zh ch sh r): absent from every companion (nearest are postalveolars /tʃ ʃ dʒ/ and the English approximant /ɹ/).
- **THE THREE-WAY CORONAL AFFRICATE SPLIT** — dental /ts tsʰ/ (z c) vs retroflex /ʈʂ ʈʂʰ/ (zh ch) vs alveolo-palatal /tɕ tɕʰ/ (j q): no other guide partitions the coronal affricate space three ways.
- **ASPIRATION-AS-THE-OBSTRUENT-CONTRAST WITH NO VOICING** — Mandarin opposes /p pʰ, t tʰ, k kʰ, ts tsʰ, ʈʂ ʈʂʰ, tɕ tɕʰ/ and has NO voiced obstruent phonemes at all (only r /ʐ~ɻ/ is voiced): the IE/Semitic/Japanese guides use voicing; only Korean also lacks voicing, but with a three-way (not two-way aspiration) system.

#### Semitic-Only Phonemes Absent from Mandarin

Aramaic/Hebrew/Syriac phonemes with NO Mandarin counterpart — the gap a Mandarin reader must bridge by approximation when reading the Peshitta tiers.

- **Pharyngeals** /ʕ/ (Ayin/E) and /ħ/ (Heth/Kheth) — no Mandarin pharyngeals; typically dropped or approximated (ʕ → zero/glide, ħ → h /x/-ward).
- **Emphatic (pharyngealized) consonants** /tˤ/ (Teth) and /sˤ/ (Tsade) — no Mandarin emphatics; approximated by plain t/s-series.
- **Glottal stop** /ʔ/ (Aleph/Alaph) — not a Mandarin phoneme; rendered as a zero-initial syllable onset.
- **Uvular** /q/ (Qoph) — not a Mandarin sound (pinyin q is the alveolo-palatal /tɕʰ/, a false friend); approximated by g/k.
- **Voiced obstruents from Begadkephat spirantization** (/v z ɣ ð/) and the trilled Resh /r/ — Mandarin has no /v z ð/ and no trill; r /ʐ~ɻ/ is the nearest rhotic but is a retroflex, not a trill.

### Reader Tiers

Like the other CJK guides, and going to the same SIX-tier depth as the Chinese Peshitta's design, the Mandarin Peshitta ships SIX reader tiers — two language-neutral Latin tiers plus a deterministic phonetic spine and three native-script/transcode tiers. These are companion materials referenced throughout this guide and should be read alongside the IPA. Because Mandarin permits only the codas -n / -ng / -er and no consonant clusters, rendering Aramaic into the pinyin/zhuyin/Hanzi tiers requires APPROXIMATION and forced vowel epenthesis; and because the Peshitta source IPA carries NO tone, the toneless tiers are **toneless BY DESIGN** — only the two Hanzi tiers unavoidably impose a citation tone per character (an artifact of logographic writing, not a feature of the source).

| # | Tier | Toned? | Description |
|---|---|---|---|
| 1 | **Scholarly** | n/a (Latin) | Language-neutral Latin transcription, the precise scholarly readback. |
| 2 | **Pretty** | n/a (Latin) | Language-neutral Latin transcription, smoothed for readability. |
| 3 | **Toneless Pinyin** (汉语拼音 / 漢語拼音) | TONELESS | The deterministic phonetic SPINE of the Mandarin reader tiers, written WITHOUT tone diacritics because the Peshitta source IPA carries no tone; the authoritative phonetic Mandarin form for this material. |
| 4 | **Zhuyin / Bopomofo** (注音符號) | TONELESS | A one-to-one transcode of the toneless pinyin into the Taiwan native phonetic alphabet (`ㄅㄆㄇㄈ`…), likewise toneless. |
| 5 | **Hanzi — Simplified** (简体字) | tone-bearing (artifact) | A downstream transcription-character lookup keyed to 普通话 Pǔtōnghuà; each character carries an unavoidable citation tone (an artifact of logographic writing). |
| 6 | **Hanzi — Traditional** (繁體字) | tone-bearing (artifact) | The same lookup keyed to 國語 Guóyǔ, in inherited traditional character forms; likewise tone-bearing by the same artifact. |

**Companion directories** (repo-relative):

- `Chinese/Peshita_Chinese/Scholarly/`
- `Chinese/Peshita_Chinese/Pretty/`
- `Chinese/Peshita_Chinese/Pinyin/`
- `Chinese/Peshita_Chinese/Zhuyin/`
- `Chinese/Peshita_Chinese/Hanzi-Simplified/`
- `Chinese/Peshita_Chinese/Hanzi-Traditional/`
- `Chinese/chinese_pronunciation_guide.md`

> **Note:** Toneless Pinyin is the deterministic phonetic spine; Zhuyin/Bopomofo is its faithful transcode (also toneless); the two Hanzi tiers are downstream lookups in Simplified (Pǔtōnghuà) and Traditional (Guóyǔ) forms. The Simplified vs Traditional split is purely orthographic and does NOT change the toneless spelling — e.g. `国`/`國`, `学`/`學`, `汉`/`漢` are the same syllable guó / xué / hàn. Tone is documented in full for the LANGUAGE elsewhere in this guide; in the reader tiers it appears only as the unavoidable per-character citation tone of the two Hanzi tiers, NOT as a property of the source text.

---

> **Note:** Unlike the Semitic guides' cross_reference sections, which trace correspondences WITHIN one family, and the Indo-European guides', which trace correspondences across branches of ONE stock, this section is contrastive across the whole set: Mandarin shares the IPA description framework with all seven companions yet is genetically unrelated to every one of them — it is a Sino-Tibetan › Sinitic language and the THIRD CJK / East Asian guide after Korean and Japanese, but the FIRST TONAL guide (four contrastive lexical tones plus a neutral tone), the FIRST LOGOGRAPHIC guide (汉字 / 漢字, in Simplified 简体字 and Traditional 繁體字 standards), and the FIRST ANALYTIC / ISOLATING guide (minimal inflection, grammar by word order + free particles, near one-morpheme-one-syllable-one-character). Its CJK neighbors are areal contacts, not relatives: Korean and Japanese are both agglutinative, head-final SOV, honorific-rich, with phonographic native scripts (featural Hangul / moraic kana) and prosody that is non-lexical (Korean) or pitch-accent (Japanese), whereas Mandarin is isolating, SVO and topic-prominent, written logographically, and tonal. On the obstruent axis Mandarin stands alone with Korean in lacking voicing — but where Korean has a three-way lax/tense/aspirated system, Mandarin has a two-way unaspirated/aspirated split — and on vowels it sides specifically with CONSERVATIVE KOREAN in having the front rounded /y/ (ü) and with SPANISH in having the velar fricative /x/ (h). Its distinctive profile across the set is: an aspiration-not-voicing obstruent system with a three-way coronal split (dental z/c /ts tsʰ/, retroflex zh/ch/sh/r /ʈʂ ʈʂʰ ʂ ʐ/, alveolo-palatal j/q/x /tɕ tɕʰ ɕ/); a small, closed syllable inventory of shape (C)(G)V(N) with only -n/-ng/-er codas and no clusters; the apical 'buzzed' vowels [ɹ̩]/[ɻ̩] and erhua rhotacization [ɚ]; the front rounded vowel /y/ and no phonemic length; analytic/isolating grammar with classifiers, aspect particles, and topic-comment structure; SVO word order; and — its signature, the family's first — LEXICAL TONE, a contrastive pitch contour on every syllable (妈/麻/马/骂 = 媽/麻/馬/罵 mā/má/mǎ/mà 'mother/hemp/horse/scold'). Throughout, 普通话 Pǔtōnghuà (PRC, Simplified, Pinyin) and 國語 Guóyǔ (Taiwan, Traditional, Zhuyin) are documented in parallel — most visibly in Pǔtōnghuà's fuller erhua and retained retroflexes vs Guóyǔ's reduced erhua and frequent de-retroflexion, plus a handful of lexical tone/reading splits (`垃圾` lājī vs lèsè, `和` hé vs hàn) — as the two reference standards of the language, the Mandarin analogue of the GA/RP, Castilian/Latin-American, South/North-Korean, and Tokyo/Kansai pairings elsewhere in the set. The whole comparison is a contrastive bridge, not a genetic claim: the IPA framework is shared by all eight guides; Mandarin is related to none of them.

---

*Cross-reference section compiled by Shin.*
