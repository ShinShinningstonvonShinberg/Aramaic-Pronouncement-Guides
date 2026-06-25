# Korean IPA Pronunciation Guide

**Version:** 1.0.0
**Date:** 2026-06-25
**Language:** Korean (한국어) (ISO 639-3: `kor`)  
**Encoding:** UTF-8  
**IPA Standard:** IPA (International Phonetic Alphabet, 2015 revision)  
**Reference Standards:** Standard South Korean (표준어) and North Korean (문화어)  

Machine-readable IPA-based pronunciation guide for Modern Korean. All pronunciation data is encoded in the International Phonetic Alphabet (IPA, 2015 revision) as the primary and only phonetic system. Designed for AI-assisted pronunciation, text-to-speech reference, second-language teaching, and language documentation. Two reference standards are documented in parallel: Standard South Korean (표준어 pyojun-eo, educated Seoul speech) and North Korean (문화어 munhwaeo, the Pyongyang-based standard). Korean's signature three-way laryngeal contrast (plain ~ tense ~ aspirated), its seven-sound coda (받침) neutralization, and its dense set of cross-boundary sandhi rules are treated as first-class data throughout.

### Varieties Covered

- **Standard South Korean (표준어 pyojun-eo, ROK)** — South Korea (the educated speech of Seoul and the surrounding capital region, the prescriptive prestige norm of the National Institute of Korean Language and South Korean broadcast media). Basis: defined by the South Korean standard as the modern speech broadly used by educated speakers of Seoul; the de facto basis of dictionaries, schooling, TTS, and broadcasting in the Republic of Korea. **두음법칙 (initial-sound rule): APPLIED.** South Korean orthography and pronunciation apply 두음법칙: word-initial ㄹ is avoided, shifting to ㄴ or to zero, and ㄴ is dropped before /i/ or /j/ — thus 女子 is written and said 여자 (yeoja, not 녀자), 勞動 is 노동 (nodong, not 로동), and 李 is 이 (I, not 리/Ri). This is the single most recognizable orthographic/phonological boundary between the two standards. Key features: applies 두음법칙 (word-initial ㄹ→ㄴ→∅ and ㄴ→∅ before i/j: 여자, 노동, 이); ongoing 애/에 (ㅐ/ㅔ) merger to `[e̞]` among most younger Seoul speakers; ㅚ/ㅟ usually realized as the diphthongs `[we]`/`[wi]` rather than the conservative front rounded monophthongs `[ø]`/`[y]`; an emergent tonogenetic split whereby the onset's laryngeal class (lax vs tense/aspirated) increasingly conditions the pitch of the following syllable in Seoul speech; full standard application of the seven-coda 받침 neutralization and the cross-boundary sandhi set (nasalization, lateralization, tensification, aspiration, palatalization, n-insertion). Analogous to the Eastern (Madnhaya) tradition in the Peshitta guide, General American (GA) in the English guide, and Peninsular Castilian in the Spanish guide — one of two co-equal documented standards.
- **North Korean Standard / Cultured Language (문화어 munhwaeo, DPRK)** — North Korea (the Pyongyang-based standard, the prescriptive norm of the Democratic People's Republic of Korea). Basis: codified after the Korean division as 문화어, declared to be based on the speech of Pyongyang and the surrounding region rather than Seoul; the basis of DPRK dictionaries, schooling and media. **두음법칙 (initial-sound rule): NOT APPLIED.** North Korean orthography and pronunciation retain word-initial ㄹ and ㄴ, not applying 두음법칙 — thus 女子 is written and said 녀자 (nyeoja), 勞動 is 로동 (rodong, hence 'Rodong Sinmun'), and 李 is 리 (Ri). This preservation of initial liquids/nasals is the clearest standard-level marker of the Northern norm. Key features: does NOT apply 두음법칙 (word-initial ㄹ/ㄴ retained: 녀자, 로동, 리); a somewhat more conservative consonant and vowel realization than contemporary Seoul speech; prescriptively maintains some vowel and lexical/orthographic distinctions that have leveled in the South, with its own dictionary, spacing and loanword norms; shares the core Korean system — three-way laryngeal contrast, seven-coda 받침 neutralization, and the cross-boundary sandhi rules; a distinct prescriptive lexicon (purist native coinages preferred over many Sino-Korean and Western loans). Analogous to the Western (Serto) tradition in the Peshitta guide, Received Pronunciation (RP/SSBE) in the English guide, and General Latin American in the Spanish guide — one of two co-equal documented standards.

The central, near-iconic difference between the two reference standards is the 두음법칙 (initial-sound rule): Standard South Korean APPLIES it, so word-initial ㄹ shifts to ㄴ or zero and ㄴ drops before i/j (여자, 노동, 이), while North Korean 문화어 does NOT, retaining initial ㄹ/ㄴ (녀자, 로동, 리). Both standards otherwise share the full Korean backbone — the three-way plain/tense/aspirated laryngeal contrast, the absence of phonemic tone and stress, the seven-sound 받침 coda neutralization, morphophonemic Hangul spelling, and the cross-boundary sandhi processes — and diverge further in some conservative vowel/consonant realizations and in prescriptive lexical, orthographic and loanword norms.

### Companion Files

- `Korean/korean_pronunciation_guide.md`
- `Korean/Peshita_Korean/Scholarly/`
- `Korean/Peshita_Korean/Pretty/`
- `Korean/Peshita_Korean/Hangul/`
- `Korean/Peshita_Korean/Romanized/`
- `peshitta_pronunciation_guide.json`
- `biblical_aramaic_pronunciation_guide.json`
- `biblical_hebrew_pronunciation_guide.json`
- `English/english_pronunciation_guide.json`
- `Spanish/spanish_pronunciation_guide.json`

The Korean Peshitta ships in FOUR reader tiers: Scholarly and Pretty (language-neutral Latin transcription), Hangul (한글 composed syllable blocks), and Romanized (a Revised Romanization read-back of the Hangul). Paths are repo-relative; `Korean/korean_pronunciation_guide.md` is the human-readable companion to this JSON.

### Notes

- Korean is written in Hangul (한글), a native FEATURAL alphabet whose jamo compose into square syllable blocks (left-to-right, top-to-bottom within the block), unlike the right-to-left Semitic companion guides and the linear Latin script of the English and Spanish guides.
- The single most characteristic feature of Korean phonology is the THREE-WAY laryngeal contrast among obstruents — plain/lax vs tense/fortis vs aspirated (e.g. 불 /pul/ 'fire' ≠ 뿔 /p͈ul/ 'horn' ≠ 풀 /pʰul/ 'grass') — and there is NO phonemic voicing contrast: the plain stops ㄱㄷㅂㅈ merely voice to `[ɡ d b dʑ]` allophonically between voiced sounds.
- Korean has NO lexical tone and NO lexical stress in the standard varieties; prosody is organized into Accentual Phrases (AP) with a phrase-level intonational tune (commonly LHLH). Seoul Korean is undergoing a tonogenetic shift in which the onset's laryngeal class conditions the following pitch. Pitch-accent dialects that DO retain lexical pitch — Gyeongsang (동남, South-East) and Hamgyŏng (북동, North-East) — are noted only as asides.
- The syllable coda (받침 batchim) NEUTRALIZES to only seven sounds `[k t p l m n ŋ]`: every written single or cluster coda (including ㄳ ㄵ ㄶ ㄺ ㄻ ㄼ … ) reduces to one of these seven when pronounced in isolation or before a consonant (e.g. 꽃 written with ㅊ is `[꼳]`, 값 with ㅄ is `[갑]`), with cluster codas simplifying so that only one consonant is realized.
- Korean orthography is MORPHOPHONEMIC (relatively deep): Hangul spelling preserves each morpheme's underlying shape, so the pervasive sandhi processes are mostly NOT written and must be derived — e.g. 같이 spelled with ㅌ is said `[가치]` (palatalization), 국물 spelled with ㄱ is said `[궁물]` (nasalization), and 신라 spelled with ㄴㄹ is said `[실라]` (lateralization). IPA, not spelling, is therefore the authoritative pronunciation record.
- Korean's signature suite of cross-boundary sandhi rules — 연음 (liaison/resyllabification), 음절의 끝소리 규칙 (the seven-sound coda rule), 비음화 (nasalization), 유음화 (lateralization), 경음화 (tensification), 격음화 (aspiration / ㅎ-merger), 구개음화 (palatalization), ㄴ-첨가 (n-insertion) and 두음법칙 (the initial-sound rule) — apply automatically at morpheme and word boundaries and are documented in their own section.
- The two reference standards differ centrally in the 두음법칙 (initial-sound rule): Standard South Korean applies it (word-initial ㄹ→ㄴ→∅ and ㄴ→∅ before i/j, giving 여자, 노동, 이), while North Korean 문화어 does NOT, retaining initial ㄹ/ㄴ (녀자, 로동, 리); this guide documents both in parallel.
- The vowel system has roughly 7–8 monophthongs with NO phonemic length; for most younger Seoul speakers the ㅐ/ㅔ (애/에) pair has MERGED to a single mid front `[e̞]`, so 개 and 게 are homophonous.
- The front rounded monophthongs ㅚ /ø/ and ㅟ /y/ are VARIABLE: conservative speakers keep them as monophthongs, but most modern speakers diphthongize them to `[we]` and `[wi]`; this guide notes both realizations.
- Korean has NO onset consonant clusters (the syllable template is (C)(G)V(C) with a single optional onset and an on-glide G), and it lacks several sounds common in the companion languages, notably /f v θ ð z ʃ ʒ/ and any trilled or approximant /r/; the single liquid ㄹ is /l ~ ɾ/.
- The letter ㅇ is dual-purpose: as a syllable ONSET it is a SILENT placeholder (no sound, marking a vowel-initial syllable), and only as a CODA does it carry the velar nasal /ŋ/ — e.g. 영 begins with silent ㅇ and ends with /ŋ/.
- Phonemic transcriptions use / / slashes and phonetic transcriptions use [ ] brackets; the tense (fortis) obstruents are marked with U+0348 (combining double vertical line below), e.g. /k͈ t͈ p͈ tɕ͈ s͈/, aspiration with /ʰ/, and the alveolo-palatal affricates as /tɕ tɕ͈ tɕʰ/.
- Romanization in this guide is secondary to IPA: the Revised Romanization (RR, official South Korea 2000) is used for the Romanized companion tier and most official/signage usage, while McCune–Reischauer (MR, with breves ŏ/ŭ and apostrophes for aspiration) remains the academic/library and North-Korea-related convention.

## Table of Contents

- [How to Read This Guide](#how-to-read-this-guide)
  - [Phonemic vs phonetic notation](#phonemic-vs-phonetic-notation)
  - [How to read the IPA](#how-to-read-the-ipa)
  - [The three-way laryngeal contrast notation](#the-three-way-laryngeal-contrast-notation)
  - [Hangul, jamo, and the RR / MR romanizations](#hangul-jamo-and-the-rr--mr-romanizations)
  - [How the parallel South / North standards are shown](#how-the-parallel-south--north-standards-are-shown)
- [Phonological Inventory](#phonological-inventory)
  - [Consonant Phonemes](#consonant-phonemes)
  - [Vowel Phonemes](#vowel-phonemes)
  - [Glides and Diphthongs](#glides-and-diphthongs)
  - [Cross-References](#cross-references)
- [Consonants](#consonants)
  - [The Three-Way Laryngeal Contrast](#the-three-way-laryngeal-contrast)
  - [Consonant Inventory](#consonant-inventory)
  - [Hangul Letter Codepoints](#hangul-letter-codepoints)
  - [Natural Classes](#natural-classes)
- [Vowels (Monophthongs)](#vowels-monophthongs)
  - [Vowel System Overview](#vowel-system-overview)
  - [Monophthong Inventory](#monophthong-inventory)
  - [Per-Vowel Notes and Example Words](#per-vowel-notes-and-example-words)
  - [Glides and Rising Diphthongs](#glides-and-rising-diphthongs)
  - [The 애/에 Merger](#the-애에-merger)
  - [ㅚ/ㅟ — Monophthong ↔ Diphthong](#ㅚㅟ--monophthong--diphthong)
  - [No Phonemic Vowel Length](#no-phonemic-vowel-length)
  - [Vowel Harmony Vestiges](#vowel-harmony-vestiges)
  - [IPA Symbol Summary](#ipa-symbol-summary)
- [Diphthongs & Glide–Vowel Sequences](#diphthongs--glidevowel-sequences)
  - [Diphthong Inventory](#diphthong-inventory)
  - [j-Series (Palatal On-Glide /j/)](#j-series-palatal-on-glide-j)
  - [w-Series (Labio-Velar On-Glide /w/)](#w-series-labio-velar-on-glide-w)
  - [ɰ-Series (Velar/Unrounded On-Glide /ɰ/)](#ɰ-series-velarunrounded-on-glide-ɰ)
  - [Summary](#summary)
- [Consonant–Vowel IPA Matrix](#consonantvowel-ipa-matrix)
  - [Reference Vowels](#reference-vowels)
  - [CV Matrix](#cv-matrix)
  - [Phonetic Notes](#phonetic-notes)
  - [Accent Notes](#accent-notes)
- [Suprasegmentals](#suprasegmentals)
  - [No Lexical Stress or Tone](#no-lexical-stress-or-tone)
  - [Accentual Phrase](#accentual-phrase)
  - [Tonogenesis in Progress](#tonogenesis-in-progress)
  - [Intonation](#intonation)
  - [Rhythm](#rhythm)
  - [Vowel Length](#vowel-length)
  - [Pitch-Accent Dialects](#pitch-accent-dialects)
  - [Cross-References](#cross-references-1)
- [Syllable Structure](#syllable-structure)
  - [Reference Standards](#reference-standards)
  - [Onset](#onset)
  - [Glide](#glide)
  - [Nucleus](#nucleus)
  - [Coda](#coda)
  - [Syllable Types](#syllable-types)
  - [Syllabification](#syllabification)
  - [Loanword Adaptation](#loanword-adaptation)
  - [Constraints](#constraints)
- [Phonological Rules](#phonological-rules)
  - [Rules at a Glance](#rules-at-a-glance)
  - [Rule 1: 음절의 끝소리 규칙 (eumjeol-ui kkeutsori gyuchik) — coda neutralization / seven-sound batchim rule](#rule-1-음절의-끝소리-규칙-eumjeol-ui-kkeutsori-gyuchik--coda-neutralization--seven-sound-batchim-rule)
  - [Rule 2: 겹받침 단순화 (gyeopbatchim dansunhwa) — consonant-cluster (double batchim) simplification](#rule-2-겹받침-단순화-gyeopbatchim-dansunhwa--consonant-cluster-double-batchim-simplification)
  - [Rule 3: 연음 (yeoneum) — liaison / resyllabification (받침 옮기기)](#rule-3-연음-yeoneum--liaison--resyllabification-받침-옮기기)
  - [Rule 4: 유성음화 / 평음 유성음화 (yuseong-eumhwa) — intervocalic voicing of lax stops](#rule-4-유성음화--평음-유성음화-yuseong-eumhwa--intervocalic-voicing-of-lax-stops)
  - [Rule 5: 비음화 (bieumhwa) — nasalization (obstruent → nasal before a nasal)](#rule-5-비음화-bieumhwa--nasalization-obstruent--nasal-before-a-nasal)
  - [Rule 6: ㄹ의 비음화 (rieul-ui bieumhwa) — ㄹ-nasalization (ㄹ → [n] after most consonants)](#rule-6-ㄹ의-비음화-rieul-ui-bieumhwa--ㄹ-nasalization-ㄹ--n-after-most-consonants)
  - [Rule 7: 유음화 (yueumhwa) — lateralization (ㄴ → [l] adjacent to ㄹ)](#rule-7-유음화-yueumhwa--lateralization-ㄴ--l-adjacent-to-ㄹ)
  - [Rule 8: 경음화 (gyeong-eumhwa) — tensification / fortis (plain obstruent → tense)](#rule-8-경음화-gyeong-eumhwa--tensification--fortis-plain-obstruent--tense)
  - [Rule 9: 격음화 / 자음 축약 (gyeok-eumhwa / jaeum chugyak) — aspiration / ㅎ-coalescence](#rule-9-격음화--자음-축약-gyeok-eumhwa--jaeum-chugyak--aspiration--ㅎ-coalescence)
  - [Rule 10: ㅎ 탈락 / ㅎ 약화 (hieut tallak) — ㅎ-deletion and intervocalic ㅎ-weakening](#rule-10-ㅎ-탈락--ㅎ-약화-hieut-tallak--ㅎ-deletion-and-intervocalic-ㅎ-weakening)
  - [Rule 11: 구개음화 (gugae-eumhwa) — palatalization (ㄷ/ㅌ + i/j → [tɕ]/[tɕʰ])](#rule-11-구개음화-gugae-eumhwa--palatalization-ㄷㅌ--ij--tɕtɕʰ)
  - [Rule 12: ㄴ 첨가 (nieun cheomga) — n-insertion at compound/word boundaries](#rule-12-ㄴ-첨가-nieun-cheomga--n-insertion-at-compoundword-boundaries)
  - [Rule 13: 두음법칙 (dueum beopchik) — initial-sound rule (SOUTH only; the key South↔North split)](#rule-13-두음법칙-dueum-beopchik--initial-sound-rule-south-only-the-key-southnorth-split)
  - [Rule 14: ㅅ → [ɕ] / 경구개음화 앞 (s-palatalization before /i, j/)](#rule-14-ㅅ--ɕ--경구개음화-앞-s-palatalization-before-i-j)
  - [Rule 15: ㄹ의 이음 (rieul-ui ieum) — ㄹ allophony: tap [ɾ] vs. lateral [l]](#rule-15-ㄹ의-이음-rieul-ui-ieum--ㄹ-allophony-tap-ɾ-vs-lateral-l)
  - [Rule 16: 모음 조화 잔존 / ㅢ 약화 (moeum johwa janjon 殘存 'residue/survival' & ㅢ realization) — minor vocalic processes](#rule-16-모음-조화-잔존--ㅢ-약화-moeum-johwa-janjon-殘存-residuesurvival--ㅢ-realization--minor-vocalic-processes)
  - [Notes](#notes)
- [Standard South Korean vs. North Korean](#standard-south-korean-vs-north-korean)
  - [Reference standards](#reference-standards-1)
  - [Differences](#differences)
  - [Asides: regional varieties (방언, bang-eon)](#asides-regional-varieties-방언-bang-eon)
- [Orthography: Hangul & Grapheme–Phoneme Correspondences](#orthography-hangul--graphemephoneme-correspondences)
  - [Reference Standards](#reference-standards-2)
  - [General Principles](#general-principles)
  - [Jamo Inventory](#jamo-inventory)
  - [Syllable-Block Composition](#syllable-block-composition)
  - [Morphophonemic Spelling](#morphophonemic-spelling)
  - [Romanization (RR vs MR)](#romanization-rr-vs-mr)
  - [Reader Tiers](#reader-tiers)
  - [Summary Notes](#summary-notes)
- [Connected Speech & Sandhi](#connected-speech--sandhi)
  - [Reference Standards](#reference-standards-3)
  - [Boundary Phenomena](#boundary-phenomena)
  - [Interaction, Register & Dialect](#interaction-register--dialect)
- [Sample Words in IPA](#sample-words-in-ipa)
  - [Per-Word Notes](#per-word-notes)
  - [Coverage Matrix](#coverage-matrix)
- [Unicode Reference](#unicode-reference)
  - [IPA Consonant Symbols](#ipa-consonant-symbols)
  - [IPA Vowel Symbols](#ipa-vowel-symbols)
  - [Diacritics & Suprasegmentals](#diacritics--suprasegmentals)
  - [Hangul Jamo](#hangul-jamo)
  - [Hangul Unicode Blocks](#hangul-unicode-blocks)
- [Cross-Reference to the Companion Guides](#cross-reference-to-the-companion-guides)
  - [Shared Framework](#shared-framework)
  - [Typological Contrasts](#typological-contrasts)
  - [Companion Guides](#companion-guides)
  - [Shared IPA Symbols](#shared-ipa-symbols)
  - [Reader Tiers](#reader-tiers-1)

## How to Read This Guide

This guide records pronunciation in the International Phonetic Alphabet (IPA, 2015 revision). IPA — not Hangul spelling and not romanization — is the authoritative pronunciation record throughout, because Korean orthography is morphophonemic (relatively deep) and leaves most sandhi unwritten. A few conventions are used throughout.

### Phonemic vs phonetic notation

- **Phonemic transcription** is written between forward slashes: `/ /`. It records the contrastive sound categories (phonemes) of the language, abstracting away from predictable detail — e.g. 불 is `/pul/` 'fire', with the plain (lax) onset given as `/p/`.
- **Phonetic transcription** is written between square brackets: `[ ]`. It records the actual realized sounds, including allophonic detail — e.g. the intervocalic voicing of a plain stop in 부부 `[pubu]`, the tap allophone of ㄹ in 나라 `[naɾa]`, or the surface result of sandhi in 국물 `[궁물]` (nasalization).

### How to read the IPA

- Consonants are described by IPA **place of articulation** (bilabial, alveolar, alveolo-palatal, velar, glottal), **manner of articulation** (plosive, affricate, fricative, nasal, liquid), and — uniquely central to Korean — by **laryngeal class** rather than by voicing, since Korean has no phonemic voicing contrast.
- Vowels are described by **height** (close/mid/open), **backness** (front/central/back), and **roundedness**, over a roughly 7–8-monophthong system. There is **no phonemic vowel length**, so no length mark `ː` is used. The on-glides /j/, /w/ and /ɰ/ (the last only in ㅢ /ɰi/) combine with the monophthongs to form the on-glide diphthongs.
- Korean has **no lexical tone and no lexical stress** in the standard varieties, so no stress mark `ˈ` is used; prosody is organized into Accentual Phrases with a phrase-level tune (commonly LHLH). Where pitch is mentioned it is a phrase-level or emergent-tonogenetic phenomenon, not a lexical stress mark.

### The three-way laryngeal contrast notation

Korean's signature feature is a THREE-WAY laryngeal contrast among the obstruents — plain/lax (lenis) ~ tense/fortis ~ aspirated — which replaces the voicing dimension used in the Latin-script companion guides:

| Laryngeal class | Notation | Stops & affricate | Example |
| --- | --- | --- | --- |
| plain / lax (lenis) | plain symbol | ㄱ /k/, ㄷ /t/, ㅂ /p/, ㅈ /tɕ/ | 불 /pul/ 'fire' |
| tense / fortis | U+0348 (combining double vertical line below) | ㄲ /k͈/, ㄸ /t͈/, ㅃ /p͈/, ㅉ /tɕ͈/, ㅆ /s͈/ | 뿔 /p͈ul/ 'horn' |
| aspirated | `ʰ` | ㅋ /kʰ/, ㅌ /tʰ/, ㅍ /pʰ/, ㅊ /tɕʰ/ | 풀 /pʰul/ 'grass' |

The stops and affricate show all three targets (e.g. /p/ ≠ /p͈/ ≠ /pʰ/); the fricatives show a two-way plain ~ tense contrast (ㅅ /s/ ~ ㅆ /s͈/). The plain obstruents ㄱㄷㅂㅈ /k t p tɕ/ voice to `[ɡ d b dʑ]` intervocalically as a predictable allophonic process, NOT a separate phoneme series, so a voiced symbol in `[ ]` does not signal a distinct phoneme.

### Hangul, jamo, and the RR / MR romanizations

- Korean is written in **Hangul (한글)**, a featural alphabet whose atomic letters — **jamo (자모)** — compose into square syllable blocks. Within a block each jamo plays one of three roles: **초성** (choseong, the onset consonant), **중성** (jungseong, the medial vowel/glide nucleus), and **종성** (jongseong, the optional coda consonant, also called **받침** batchim). Standalone jamo (e.g. ㄱ ㄴ ㅏ) are shown in isolation in this guide.
- Forms are given in **real Unicode 한글** directly; phonemic values follow in `/ /` and phonetic detail in `[ ]`.
- Two Latin romanizations are documented alongside the IPA, and where both are cited they are labelled:
  - **RR — Revised Romanization of Korean** (official in the Republic of Korea since 2000): no diacritics, ASCII-friendly (eo for ㅓ, eu for ㅡ, ae for ㅐ, oe for ㅚ); plain stops g/d/b/j, aspirated k/t/p/ch, tense gg/dd/bb/ss/jj; generally transcribes the surface pronunciation across boundaries. RR is the system used for the Romanized companion tier of this guide.
  - **MR — McCune–Reischauer** (the earlier scholarly standard, 1937): uses the breve for ㅓ (ŏ) and ㅡ (ŭ) and the apostrophe for aspiration (k', t', p', ch'); standard in much academic, library and North-Korea-related literature.
- Romanization is **secondary to IPA** here: RR and MR are provided for cross-referencing and read-back only; the IPA is the authoritative record.

### How the parallel South / North standards are shown

Two co-equal reference standards are documented in parallel:

- **Standard South Korean (표준어, ROK)** — the educated-Seoul prestige norm; **applies 두음법칙** (word-initial ㄹ→ㄴ→∅ and ㄴ→∅ before i/j: 여자, 노동, 이).
- **North Korean 문화어 (DPRK)** — the Pyongyang-based norm; **does NOT apply 두음법칙** (retains initial ㄹ/ㄴ: 녀자, 로동, 리).

Where the two standards differ, both forms are given side by side, labelled ROK (South) and DPRK (North). The central, near-iconic divergence is the 두음법칙 (initial-sound rule); the two standards otherwise share the full Korean backbone (the three-way laryngeal contrast, no phonemic tone or stress, the seven-coda 받침 neutralization, morphophonemic Hangul spelling, and the cross-boundary sandhi set), diverging further only in some conservative vowel/consonant realizations and in prescriptive lexical, orthographic and loanword norms.

## Phonological Inventory

The complete phonemic inventory of Modern Korean (한국어), organized by IPA categories. Documented in parallel for two reference standards: **Standard South Korean — 표준어 (pyojun-eo)**, the educated Seoul norm, and **North Korean — 문화어 (munhwaeo)**, the Pyongyang-based standard. The two standards share an essentially identical segmental inventory of **19 consonants** and **7–8 (conservatively up to 10) vowels**; they diverge chiefly in PRESCRIPTIVE phonology rather than in the phoneme set itself. The single most consequential difference is the **두음법칙 (initial-sound rule)**: South Korean changes word-initial ㄹ→ㄴ→∅ and ㄴ→∅ before /i j/ (女子 여자 *yeoja*, 勞動 노동 *nodong*), whereas North Korean RETAINS the initial liquid/nasal (녀자 *nyeoja*, 로동 *rodong*) — a difference of distribution, not of inventory. The hallmark of the whole system is the **THREE-WAY LARYNGEAL CONTRAST** among obstruents (plain/lax vs tense/fortis vs aspirated) in place of the voicing contrast familiar from English; Korean has NO phonemic voicing. /slashes/ mark phonemes, [brackets] mark phonetic realizations. This section is a SUMMARY; exhaustive per-phoneme entries live in the separate **Consonants** and **Vowels** sections.

### Consonant Phonemes

All 19 consonant phonemes of Modern Korean arranged by place and manner of articulation. The inventory is shared between Standard South Korean (표준어) and North Korean (문화어). Its defining feature is the three-way laryngeal contrast — plain/lax (lenis), tense/fortis, and aspirated — which replaces the voiced/voiceless contrast of European languages: Korean obstruents are phonemically voiceless, and the plain (lenis) series simply VOICES allophonically between voiced sounds (`[k t p tɕ]` → `[ɡ d b dʑ]` intervocalically).

**Total consonant phonemes:** 19  
19 consonant phonemes built around the three-way laryngeal contrast. STOPS/AFFRICATE in three series: plain/lax ㄱ /k/, ㄷ /t/, ㅂ /p/, ㅈ /tɕ/ (4); tense/fortis ㄲ /k͈/, ㄸ /t͈/, ㅃ /p͈/, ㅉ /tɕ͈/ (4); aspirated ㅋ /kʰ/, ㅌ /tʰ/, ㅍ /pʰ/, ㅊ /tɕʰ/ (4) = 12. FRICATIVES: plain ㅅ /s/ and tense ㅆ /s͈/ (only the sibilant has a tense partner), plus glottal ㅎ /h/ = 3. NASALS: ㅁ /m/, ㄴ /n/, ㅇ /ŋ/ = 3. LIQUID: ㄹ /l ~ ɾ/ = 1. Total 12 + 3 + 3 + 1 = 19.

**Key allophones** (not separate phonemes): the plain/lax obstruents /k t p tɕ/ are voiceless `[k t p tɕ]` word-initially and after obstruents, but VOICE to `[ɡ d b dʑ]` between voiced segments (e.g. 바보 *babo* `[pa̠bo]` 'fool', 고기 *gogi* `[ko̞ɡi]` 'meat'); /s/ palatalizes to `[ɕ]` before /i/ or /j/ (시 *si* `[ɕi]` 'poem'), and /s͈/ likewise to `[ɕ͈]`; /h/ weakens or deletes intervocalically (`[ɦ]`~∅) and fuses with an adjacent plain stop into an aspirate (격음화); the liquid /ㄹ/ surfaces as a tap `[ɾ]` as an intervocalic onset, as `[l]` in coda and in the geminate ㄹㄹ (`[lː]`), and assimilates with /n/ (유음화). The velar nasal /ŋ/ (ㅇ) occurs ONLY in the coda; the letter ㅇ in onset position is a SILENT placeholder with no phonetic value. The tense series is transcribed with `U+0348` (combining double vertical line below): /k͈ t͈ p͈ tɕ͈ s͈/.

**Gaps vs Aramaic and European languages:** Korean has NO /f v θ ð z ʃ ʒ/ and no phonemic voicing contrast at all.

**South ↔ North:** the phoneme set is identical; the difference is distributional (두음법칙), so North Korean permits word-initial /ɾ~l/ and /n/ before /i j/ where the South does not.

#### IPA Consonant Chart

IPA consonant chart for Modern Korean (rows = manner, columns = place). The three-way laryngeal contrast is shown WITHIN each obstruent cell in the fixed order **plain / tense / aspirated** (separated by spaces). The tense series uses `U+0348` (combining double vertical line below): k͈ t͈ p͈ tɕ͈ s͈. The chart is shared by Standard South Korean and North Korean.

*Laryngeal column order within each obstruent cell: plain (lax) → tense (fortis) → aspirated.*

| Manner | Bilabial | Alveolar | Alveolo-palatal | Velar | Glottal |
|---|---|---|---|---|---|
| Plosive | p p͈ pʰ | t t͈ tʰ |  | k k͈ kʰ |  |
| Affricate |  |  | tɕ tɕ͈ tɕʰ |  |  |
| Fricative |  | s s͈ |  |  | h |
| Nasal | m | n |  | ŋ |  |
| Liquid |  | l ~ ɾ |  |  |  |

*The plain/tense/aspirated columns are visible WITHIN each obstruent cell: plosives at three places (bilabial ㅂㅃㅍ /p p͈ pʰ/, alveolar ㄷㄸㅌ /t t͈ tʰ/, velar ㄱㄲㅋ /k k͈ kʰ/) and the alveolo-palatal affricate (ㅈㅉㅊ /tɕ tɕ͈ tɕʰ/) each fill all three laryngeal slots; the fricative row is DEFECTIVE, having only plain ㅅ /s/ + tense ㅆ /s͈/ (no aspirated *sʰ) at the alveolar place, plus the unpaired glottal ㅎ /h/. Nasals ㅁㄴㅇ /m n ŋ/ and the single liquid ㄹ /l ~ ɾ/ are laryngeally neutral (sonorants take no three-way contrast). /ŋ/ (ㅇ) is coda-only; onset ㅇ is the silent vowel-carrier and is NOT a phoneme. Phoneme tally: stops p p͈ pʰ t t͈ tʰ k k͈ kʰ (9) + affricates tɕ tɕ͈ tɕʰ (3) + fricatives s s͈ h (3) + nasals m n ŋ (3) + liquid l~ɾ (1) = 19. The glides /j w ɰ/ are NOT counted here — they belong with the vowels/diphthongs. North Korean's affricate is sometimes described as more dental (`[ts]`-type), and some older/North descriptions transcribe the alveolo-palatal series as postalveolar `[tʃ tʃ͈ tʃʰ]`, but the phoneme count is identical to the South.*

#### Notes by Place of Articulation

- **Bilabial** — /p p͈ pʰ m/. The bilabial stop in all three laryngeal series: plain ㅂ /p/ (밥 *bap* 'rice'), tense ㅃ /p͈/ (빵 *ppang* 'bread'), aspirated ㅍ /pʰ/ (팔 *pal* 'arm'). Plain ㅂ /p/ is voiceless `[p]` initially and after an obstruent but voices to `[b]` between voiced segments (아버지 *abeoji* `[a̠bʌdʑi]` 'father'). In coda position all three neutralize to the unreleased `[p̚]` (음절의 끝소리 규칙). Bilabial nasal ㅁ /m/ (몸 *mom* 'body') occurs freely in onset and coda. The glide /w/ has a labial component but is treated in the vowel/glide section, not as a consonant phoneme.
- **Alveolar** — /t t͈ tʰ s s͈ n l~ɾ/. The richest place of articulation. Alveolar/denti-alveolar stops in three series: plain ㄷ /t/ (다 *da*), tense ㄸ /t͈/ (딸 *ttal* 'daughter'), aspirated ㅌ /tʰ/ (탈 *tal* 'mask'); plain /t/ voices to `[d]` intervocalically (구두 *gudu* `[kudu]` 'shoes'). The fricatives are the ONLY series with a two-way (plain~tense) rather than three-way contrast: plain ㅅ /s/ (사 *sa*) and tense ㅆ /s͈/ (싸 *ssa*); both palatalize before /i j/ to `[ɕ]`/`[ɕ͈]` (시 *si* `[ɕi]`, 씨 *ssi* `[ɕ͈i]`). Alveolar nasal ㄴ /n/ (나 *na*). The single liquid ㄹ /l ~ ɾ/ is a tap `[ɾ]` as an intervocalic onset (다리 *dari* `[ta̠ɾi]` 'leg/bridge'), a lateral `[l]` in coda and in geminate ㄹㄹ (달 *dal* `[tal]` 'moon'; 빨리 *ppalli* `[p͈alːi]` 'quickly'); ㄷ/ㅌ palatalize to `[tɕ]`/`[tɕʰ]` before /i j/ across a morpheme boundary (굳이 `[kudʑi]`, 같이 `[kɑtɕʰi]`) — 구개음화. 두음법칙 (South only): word-initial ㄹ→`[n]`→∅ and ㄴ→∅ before /i j/; North retains them.
- **Alveolo-palatal** — /tɕ tɕ͈ tɕʰ/. Korean's single affricate place, realized in the three laryngeal series: plain ㅈ /tɕ/ (자 *ja*), tense ㅉ /tɕ͈/ (짜 *jja*), aspirated ㅊ /tɕʰ/ (차 *cha*). They are alveolo-palatal `[tɕ tɕ͈ tɕʰ]` (sometimes transcribed `[tʃ]` or `[ts]` in older or more conservative/North descriptions, where a more dental `[ts]`-type realization is reported). Plain ㅈ /tɕ/ voices to `[dʑ]` between voiced segments (아주 *aju* `[a̠dʑu]` 'very'). In coda, ㅈ ㅊ neutralize to `[t̚]`. This is also the target of 구개음화: underlying ㄷ/ㅌ + /i j/ surface as `[tɕ]`/`[tɕʰ]`.
- **Velar** — /k k͈ kʰ ŋ/. Velar stops in three series: plain ㄱ /k/ (가 *ga*), tense ㄲ /k͈/ (까 *kka*), aspirated ㅋ /kʰ/ (카 *ka*); plain /k/ voices to `[ɡ]` intervocalically (아기 *agi* `[a̠ɡi]` 'baby'). The velar nasal ㅇ /ŋ/ (강 *gang* `[kaŋ]` 'river') occurs ONLY as a coda and NEVER as an onset; crucially the SAME letter ㅇ in onset position is a purely orthographic SILENT placeholder (아 *a* = bare vowel, no consonant). In coda all velar stops neutralize to unreleased `[k̚]`, and an obstruent /k/ nasalizes to `[ŋ]` before a nasal (국물 `[kuŋmul]`) — 비음화.
- **Glottal** — /h/. The glottal fricative ㅎ /h/ (하 *ha*) is the system's only glottal and has no tense or aspirated counterpart. It voices to `[ɦ]` and frequently WEAKENS or DELETES between voiced segments (좋아 `[tɕo̞a̠]` rather than `[tɕoha̠]`). It also drives 격음화 (aspiration/ㅎ-merger): ㅎ adjacent to a plain stop fuses into the corresponding aspirate (좋고 → `[tɕokʰo]`, 입학 → `[ipʰak̚]`). Before /i j/ it may be realized as a palatal `[ç]` (힘 `[çim]`). ㅎ does not occur as a true pronounced coda — written final ㅎ triggers aspiration or is dropped.

### Vowel Phonemes

The vowel phonemes of Modern Korean. Inventory size is generation-dependent: most younger Standard Seoul speakers have **7** contrasting monophthongs, a conservative count gives **8**, and the most conservative (older Seoul and the prescriptive 표준어/문화어 norm) recognizes up to **10** by treating ㅚ /ø/ and ㅟ /y/ as front rounded monophthongs. Two changes-in-progress drive the variation: (1) the **애/에 MERGER** — ㅐ /ɛ/ and ㅔ /e/ have collapsed to a single mid front `[e̞]` for most speakers under ~40; and (2) the **diphthongization** of ㅚ /ø/ → `[we]` and ㅟ /y/ → `[wi]`, so the front rounded monophthongs survive only in conservative speech. This section summarizes the simple vowels (monophthongs) plus the glides /j w ɰ/ and the on-glide diphthongs they build; the full per-vowel and per-diphthong detail lives in the separate **Vowels** section. The two reference standards (표준어 / 문화어) share this vowel inventory.

**South Seoul (younger) monophthong count:** 7 | **Conservative monophthong count:** 10  
South Seoul (younger speakers) count = 7: ㅏ /a/, ㅓ /ʌ/, ㅗ /o/, ㅜ /u/, ㅡ /ɯ/, ㅣ /i/, and a single merged mid front `[e̞]` from the collapse of ㅐ /ɛ/ + ㅔ /e/ (the 애/에 merger). Adding the still-distinct ㅐ /ɛ/ ~ ㅔ /e/ contrast (kept by older/careful speakers) gives 8. The conservative count = 10 additionally treats ㅚ /ø/ and ㅟ /y/ as front ROUNDED monophthongs; in modern Seoul both are normally diphthongized — ㅚ → `[we]` (merging with ㅞ) and ㅟ → `[wi]` — so the typical realized monophthong system is 8 (애/에 distinct) or 7 (merged). The 애/에 MERGER means 개 'dog' and 게 'crab' are homophones `[ke̞]` for most young Seoulites; prescriptively (and in conservative 표준어/문화어) they remain /kɛ/ vs /ke/. There is NO phonemic vowel length in contemporary speech — an older length contrast (눈 `[nuːn]` 'snow' vs 눈 `[nun]` 'eye') survives only in conservative/elderly speech and the prescriptive norm, and is otherwise lost; younger speakers do not distinguish vowel length. There is NO lexical stress and NO lexical tone in Standard Korean (Seoul); pitch is organized at the level of the Accentual Phrase. GLIDES /j w ɰ/ combine with the monophthongs to form the on-glide diphthongs; ㅢ /ɰi/ uniquely uses the velar approximant /ɰ/. **South ↔ North:** the vowel inventory is the same; North 문화어 is somewhat more conservative prescriptively (e.g. it more firmly maintains the ㅐ/ㅔ distinction and the front rounded monophthongs in the norm), but realized speech trends parallel the South.

#### IPA Vowel Chart

IPA vowel quadrilateral for the Korean monophthongs (rows = height, columns = backness/rounding). The 7–8-vowel core system is shown; the conservative front rounded monophthongs ㅚ /ø/ and ㅟ /y/ are listed in parentheses as they are normally diphthongized in modern Seoul. The back unrounded ㅡ /ɯ/ and the central-back ㅓ /ʌ/ are the typologically notable members.

| Height | Front (unrounded) | Front (rounded) | Central | Back (unrounded) | Back (rounded) |
|---|---|---|---|---|---|
| close | i | (y) |  | ɯ | u |
| mid | e (~ ɛ) | (ø) |  | ʌ | o |
| open |  |  | a |  |  |

*Core monophthongs by height: CLOSE — ㅣ /i/ (front unrounded), ㅡ /ɯ/ (back/high-central unrounded), ㅜ /u/ (back rounded); MID — the merged front mid `[e̞]` (from ㅔ /e/ ~ ㅐ /ɛ/), ㅓ /ʌ/ (back-central unrounded, phonetically often `[ʌ̹]`~`[ɔ̜]` and notably raised/rounded in North/younger Seoul), ㅗ /o/ (back rounded); OPEN — ㅏ /a/ (central-to-front low). Parenthesized (y) ㅟ and (ø) ㅚ are the conservative front ROUNDED monophthongs, kept only in careful/older speech and normally realized as the diphthongs `[wi]` and `[we]`. The two typological signatures are ㅡ /ɯ/ (a close back/central UNROUNDED vowel, the unrounded counterpart of /u/) and ㅓ /ʌ/ (a non-low back unrounded vowel). The 애/에 merger is shown by writing the front-mid cell as 'e (~ ɛ)'. No length marks (ː) are used in the core chart because contemporary Seoul Korean has lost phonemic vowel length.*

#### Monophthong Inventory

| IPA | Jamo | Height | Backness | Rounding | Example | Distribution |
|---|---|---|---|---|---|---|
| /a/ | `ㅏ` | open | central | unrounded | 아 *a*, 말 *mal* 'horse/word', 사 *sa* | The single low vowel, phonetically central-to-front `[a̠]`~`[ä]`. Stable in stressed and unstressed positions (no reduction to schwa). On-glide partner of /j/ → ㅑ /ja/ and /w/ → ㅘ /wa/. Identical in 표준어 and 문화어. |
| /ʌ/ | `ㅓ` | mid (open-mid to mid) | back (central-back) | unrounded | 어 *eo*, 거 *geo*, 사람 *saram* 'person' | Back/central unrounded mid vowel, the Korean vowel most variable across speakers: conservative Seoul `[ʌ]`, with frequent raising/slight rounding toward `[ɔ̜]`~`[ɤ]` in North Korean and many younger Seoul speakers. Romanized 'eo' (RR) / 'ŏ' (MR). On-glide partners: /j/ → ㅕ /jʌ/, /w/ → ㅝ /wʌ/. No length contrast in modern speech (older `[ʌː]` in e.g. 거리 'distance' is lost for the young). |
| /o/ | `ㅗ` | mid (close-mid) | back | rounded | 오 *o*, 손 *son* 'hand', 보 *bo* | Close-mid back rounded vowel `[o̞]`. Contrasts with /u/ in height and with /ʌ/ in rounding; younger speakers may raise it toward /u/, narrowing the /o/~/u/ gap. On-glide partner: /j/ → ㅛ /jo/. (Phonemically /o/ has no w-glide nucleus; orthographically the ㅗ-based w-diphthong blocks ㅘ ㅙ are written on this letter, but their phonemic nucleus is /a ɛ/, not /o/.) Full quality always; no reduction or length contrast. |
| /u/ | `ㅜ` | close | back | rounded | 우 *u*, 문 *mun* 'door', 두 *du* | Close back rounded vowel; in some younger Seoul speech it fronts/centralizes toward `[ʉ]`. On-glide partner: /j/ → ㅠ /ju/. (Phonemically /u/ has no w-glide nucleus; orthographically the ㅜ-based w-diphthong blocks ㅝ ㅞ are written on this letter, but their phonemic nucleus is /ʌ e/, not /u/.) Forms the conservative front rounded ㅟ /y/ ~ realized `[wi]`. No reduction or length contrast. |
| /ɯ/ | `ㅡ` | close | back (high-central) | unrounded | 으 *eu*, 글 *geul* 'writing', 그 *geu* 'that' | Close back/high-central UNROUNDED vowel — a typological signature of Korean and the default epenthetic vowel inserted to break up illicit clusters in loanwords (스트레스 *seuteureseu* 'stress'). Romanized 'eu' (RR) / 'ŭ' (MR). Combines with /ɰ/ only in ㅢ /ɰi/. Often centralized `[ɨ]` and frequently devoiced or elided between voiceless consonants in fast speech. No length contrast. |
| /i/ | `ㅣ` | close | front | unrounded | 이 *i* 'two/tooth', 김 *gim* 'seaweed', 시 *si* 'poem' | Close front unrounded vowel. Triggers PALATALIZATION of a preceding /s s͈/ → `[ɕ ɕ͈]` (시 `[ɕi]`) and of underlying ㄷ/ㅌ → `[tɕ tɕʰ]` across boundaries (구개음화). On-glide partner of /j/ is vacuous (*/ji/ not contrastive); /ɰ/ → ㅢ /ɰi/. Conditions 두음법칙 in the South (word-initial ㄴ/ㄹ drop before /i j/). No reduction or length contrast. |
| /e/ | `ㅔ` | mid (close-mid) | front | unrounded | 에 *e* (locative particle), 게 *ge* 'crab', 네 *ne* 'yes' | Close-mid front unrounded vowel. **Merger status:** merged with ㅐ /ɛ/ to `[e̞]` for most modern Seoul speakers (애/에 merger); distinct in conservative/prescriptive norm. For most speakers under ~40 it has MERGED with ㅐ /ɛ/ to a single mid front `[e̞]`, making 게 'crab' and 개 'dog' homophones; conservatively /e/ (higher) contrasts with /ɛ/ (lower, 개). On-glide partners: /j/ → ㅖ /je/, /w/ → ㅞ /we/ (and ㅚ /ø/ ~ `[we]`). No length contrast. |
| /ɛ/ | `ㅐ` | mid (open-mid) | front | unrounded | 개 *gae* 'dog', 내 *nae* 'my', 새 *sae* 'bird' | Open-mid front unrounded vowel, the lower partner of the ㅔ/ㅐ pair. **Merger status:** merged with ㅔ /e/ to `[e̞]` for most modern Seoul speakers (애/에 merger); distinct in conservative/prescriptive norm. In contemporary Seoul it is MERGED with ㅔ /e/ as `[e̞]`, so 개 'dog' = 게 'crab' = `[ke̞]` for younger speakers; counted as a separate phoneme only in the conservative 8–10-vowel analysis and the prescriptive standard. On-glide partners: /j/ → ㅒ /jɛ/, /w/ → ㅙ /wɛ/. No length contrast. |
| /ø/ | `ㅚ` | mid (close-mid) | front | rounded | 외 *oe*, 회 *hoe* 'meeting/raw fish', 되 *doe* | **Monophthong status:** conservative front rounded monophthong; normally diphthongized to `[we]` in modern Seoul (merging with ㅞ). Front ROUNDED close-mid vowel `[ø]` in conservative/older speech; for most modern speakers realized as the rising diphthong `[we]`, merging with ㅞ /we/. Counted as a monophthong only in the conservative 10-vowel inventory. Romanized 'oe' (RR) / 'oe'~'oi' (MR). Its monophthongal value is best preserved in careful and some regional/North speech. |
| /y/ | `ㅟ` | close | front | rounded | 위 *wi* 'above/stomach', 귀 *gwi* 'ear', 쉬 *swi* | **Monophthong status:** conservative front rounded monophthong; normally diphthongized to `[wi]` in modern Seoul. Front ROUNDED close vowel `[y]` in conservative/older speech; for most modern speakers realized as the rising diphthong `[wi]`. Counted as a monophthong only in the conservative 10-vowel inventory. Romanized 'wi' (RR) / 'wi' (MR). Like ㅚ, its monophthongal pronunciation survives mainly in careful and some regional/North speech. |

### Glides and Diphthongs

The three glides of Korean and the on-glide diphthongs they build with the monophthongs. Korean diphthongs are overwhelmingly RISING (on-glide + vowel): a glide /j/, /w/, or /ɰ/ precedes the vocalic nucleus. There are no true falling (off-glide) diphthongs in the standard analysis. The glides are NOT counted among the vowel phonemes; the full diphthong inventory with per-item detail lives in the separate **Vowels**/diphthongs material.

#### Glides

| IPA | Name | Examples | Notes |
|---|---|---|---|
| /j/ | palatal glide (front semivowel) | 야 *ya*, 여 *yeo*, 요 *yo*, 유 *yu*, 예 *ye*, 얘 *yae* | On-glide of the j-series diphthongs ㅑ /ja/, ㅕ /jʌ/, ㅛ /jo/, ㅠ /ju/, ㅒ /jɛ/, ㅖ /je/. Does not contrast before /i/ (no */ji/). Distinct from the consonant inventory; written with the doubled-stroke vowel jamo. |
| /w/ | labio-velar glide (back rounded semivowel) | 와 *wa*, 왜 *wae*, 워 *wo*, 웨 *we*, 위 *wi* (~ㅟ), 외 *oe* (~`[we]`) | On-glide of the w-series diphthongs ㅘ /wa/, ㅙ /wɛ/, ㅝ /wʌ/, ㅞ /we/, plus the diphthongized realizations of ㅟ /y/ → `[wi]` and ㅚ /ø/ → `[we]`. The labial component is also why /w/ is sometimes linked to the bilabial/velar consonant region, but it is treated as a glide. |
| /ɰ/ | velar (unrounded) approximant glide | 의 *ui* | Occurs in exactly ONE diphthong, ㅢ /ɰi/ (의 *ui*) — the unrounded back on-glide before /i/. ㅢ has variable realization: `[ɰi]` carefully, `[i]` word-medially or after a consonant (희망 `[himaŋ]` 'hope'), and `[e]` in the genitive particle 의 (`[e]`). The unique glide that makes Korean's diphthong system three-way. |

#### Diphthong Summary

| Series | Diphthongs |
|---|---|
| j-series (6) | ㅑ /ja/, ㅕ /jʌ/, ㅛ /jo/, ㅠ /ju/, ㅒ /jɛ/, ㅖ /je/ |
| w-series (4) | ㅘ /wa/, ㅙ /wɛ/, ㅝ /wʌ/, ㅞ /we/ |
| ɰ-series (1) | ㅢ /ɰi/ |
| Diphthongized monophthongs | ㅚ /ø/ → `[we]`, ㅟ /y/ → `[wi]` |

*All standard Korean diphthongs are RISING (on-glide + nucleus): six with /j/, four with /w/, one with /ɰ/ = 11 phonemic diphthongs, to which the modern diphthongal realizations of ㅚ and ㅟ are commonly added. Because ㅐ/ㅔ merge for most speakers, the j-pair ㅒ /jɛ/ ~ ㅖ /je/ and the w-pair ㅙ /wɛ/ ~ ㅞ /we/ (and ㅚ `[we]`) likewise tend to merge to `[je]` and `[we]`. No phonemic vowel length attaches to the diphthongs in contemporary speech.*

### Cross-References

This section is a SUMMARY of the inventory. Per-phoneme articulatory detail, allophony, romanization and example words are given in the **Consonants** and **Vowels** sections; the full set of sound-change processes (연음 liaison, 음절의 끝소리 규칙 coda neutralization, 비음화 nasalization, 유음화 lateralization, 경음화 tensification, 격음화 aspiration, 구개음화 palatalization, ㄴ-첨가 n-insertion, 두음법칙 initial-sound rule) is treated in the **Phonological Rules** section. Suprasegmentals (no lexical stress/tone; Accentual-Phrase prosody; the Gyeongsang and Hamgyŏng pitch-accent dialects) are covered in the **Suprasegmentals** section, and Hangul orthography/Unicode composition in the **Orthography** section.

**Companion files** (repo-relative):

- `Korean/korean_pronunciation_guide.md`
- `Korean/Peshita_Korean/Hangul/`
- `Korean/Peshita_Korean/Romanized/`

**Reader tiers:** the Korean Peshitta ships four reader tiers — Scholarly and Pretty (language-neutral Latin), Hangul (한글 composed syllable blocks), and Revised Romanization (RR readback of the Hangul) — which present the phonemes catalogued here at increasing levels of script-specificity.

## Consonants

The 19 consonant phonemes of Standard Korean (한국어), documented in parallel for two reference standards: Standard South Korean (표준어 *pyojun-eo*, educated Seoul speech) and North Korean (문화어 *munhwaeo*, Pyongyang standard). The defining feature of the Korean consonant system is its three-way **laryngeal contrast** among voiceless obstruents — **plain/lax (lenis)**, **tense/fortis**, and **aspirated** — a typologically rare opposition that replaces the voiced–voiceless contrast familiar from English and Spanish. Korean has **no phonemic voicing**: the plain stops ㄱ ㄷ ㅂ ㅈ are voiceless word-initially but voice allophonically to [ɡ d b dʑ] between voiced sounds, so 'voicing' is never contrastive. The single sibilant series is likewise split only by the plain/tense contrast (ㅅ /s/ vs ㅆ /s͈/). Because Korean spelling (Hangul) is **morphophonemic** and the system is heavily governed by surface phonological rules (coda neutralization to seven sounds, liaison, nasalization, lateralization, tensification, aspiration, palatalization), the underlying phoneme inventory and its rich context-dependent realisations are documented separately: phonemic values are given in /slashes/ and phonetic realisations in [brackets], following IPA (2015 revision). The tense series is marked with `U+0348` (combining double vertical line below): /k͈ t͈ p͈ tɕ͈ s͈/. Gaps relative to English/Aramaic: Korean has no /f v θ ð z ʃ ʒ/ and no native voiced obstruents. South–North differences are almost entirely lexical/orthographic (the 두음법칙 *dueum-beopchik* initial-sound rule) rather than inventorial; the few realisational differences are recorded in the allophony notes.

**Consonant phonemes:** 19 | **Effective phonemes:** 19  
All 19 consonant phonemes correspond one-to-one to 19 base Hangul consonant letters (자모 *jamo*). The five tense consonants are written with **doubled** letters (ㄲ ㄸ ㅃ ㅆ ㅉ, the 쌍자음 *ssang-jaeum* 'twin consonants'). The affricates ㅈ /tɕ/, ㅉ /tɕ͈/, ㅊ /tɕʰ/ are treated as single phonemes. The letter ㅇ is special: as a syllable **onset** it is a silent placeholder carrying no consonant (it merely fills the obligatory initial slot of a syllable block), while as a **coda** it spells the velar nasal /ŋ/ — so it represents a phoneme only in coda position. Letter-to-phoneme mapping is essentially 1:1 underlyingly, but surface realisation is many-to-many because of the coda-neutralization rule (음절의 끝소리 규칙): all coda consonants reduce to seven sounds [k t p l m n ŋ], so e.g. ㄷ ㅌ ㅅ ㅆ ㅈ ㅊ ㅎ all surface as [t̚] in the coda. This effective count is identical for the South Korean and North Korean standards.

### The Three-Way Laryngeal Contrast

**삼중 대립 (예사소리·된소리·거센소리)** — *three-way laryngeal contrast (plain · tense · aspirated)*.

Korean's signature opposition. Where English contrasts voiceless /p/ vs voiced /b/, Korean contrasts **three voiceless series** at each of four oral places (labial, alveolar, palatal/postalveolar, velar) — plus a two-way plain/tense split in the sibilant /s/. The cues are laryngeal and not (chiefly) VOT alone:

- **Plain (예사소리 *yesasori*):** lax, lightly aspirated word-initially, low-pitched on the following vowel, and voiced between voiced sounds.
- **Tense (된소리 *doensori*):** produced with a constricted/stiff glottis, no aspiration, a tense long closure, and a high-pitched, often creaky following vowel.
- **Aspirated (거센소리 *geosensori*):** strong breathy release and a high following pitch.

In modern Seoul Korean the word-initial plain–aspirated VOT distinction is collapsing and is increasingly carried by the **pitch** of the following vowel (the tonogenetic shift).

#### Minimal Sets

Near-minimal triplets (and one pair) illustrating the contrast at each place/manner. Phonetic transcriptions are in [brackets].

| Place / Manner | Plain (예사소리) | Tense (된소리) | Aspirated (거센소리) |
|---|---|---|---|
| Bilabial stop | 불 *bul* [pul] — 'fire' | 뿔 *ppul* [p͈ul] — 'horn' | 풀 *pul* [pʰul] — 'grass / glue' |
| Alveolar stop | 달 *dal* [tal] — 'moon' | 딸 *ttal* [t͈al] — 'daughter' | 탈 *tal* [tʰal] — 'mask / mishap' |
| Velar stop | 갈 *gal* [kal] — "(stem 'grind/go') as in 갈다" | 깔 *kkal* [k͈al] — "(stem 'spread/lay') as in 깔다" | 칼 *kal* [kʰal] — 'knife' |
| Palatal affricate (verb stems) | 자다 *jada* [tɕada] — 'to sleep' | 짜다 *jjada* [t͈ɕ͈ada] ~ [t͈ada] — 'to be salty / to squeeze' | 차다 *chada* [tɕʰada] — 'to be cold / to kick / to be full' |
| Sibilant fricative (plain vs tense only — no aspirated member) | 살 *sal* [sal] — 'flesh' | 쌀 *ssal* [s͈al] — '(uncooked) rice' | — (none) |

> **Note:** The fricative series has only a **two-way** contrast (plain ㅅ /s/ vs tense ㅆ /s͈/); there is no aspirated \*sʰ. /h/ stands outside the three-way system as the only laryngeal fricative.

### Consonant Inventory

The 19 consonant phonemes with their IPA value, Hangul letter (자모), letter name, place, manner, laryngeal class, spelling graphemes, example words (with IPA), and allophony notes.

| # | IPA | Jamo | Name (한글 / RR) | Class | Place | Manner | Spellings | Example Words | Allophony Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `/k/` | `ㄱ` | 기역 (giyeok) | plain | velar | stop | `ㄱ` | 가방 *gabang* [kabaŋ] 'bag'; 고기 *gogi* [koɡi] 'meat'; 한국 *Hanguk* [hanɡuk̚] 'Korea' | Word-initially voiceless and lightly aspirated [k] ~ [k˭]; **intervocalically** and between voiced sounds it voices to [ɡ] (고기 'meat' [koɡi], not [koki]) — this lenition is automatic and non-contrastive. In the coda it is unreleased [k̚] (한국 [hanɡuk̚]) and triggers tensification of a following plain obstruent (경음화). Before a nasal it nasalizes to [ŋ] (비음화: 국물 'broth' [kuŋmul]). Identical in South and North standards. |
| 2 | `/k͈/` | `ㄲ` | 쌍기역 (ssanggiyeok) | tense | velar | stop | `ㄲ` | 꿈 *kkum* [k͈um] 'dream'; 토끼 *tokki* [tʰok͈i] 'rabbit'; 깍두기 *kkakdugi* [k͈ak̚t͈uɡi] 'cubed radish kimchi' | Produced with a stiff/constricted glottis: **never** aspirated and **never** voiced even between vowels (토끼 [tʰok͈i], where the medial stop stays fortis voiceless). The oral closure is longer and tenser than the plain stop and the following vowel begins at higher pitch, often with creaky phonation. Frequently the surface output of 경음화 (tensification): a plain /k/ becomes [k͈] after an obstruent coda. As a coda ㄲ neutralizes to plain [k̚]. Same in South and North. |
| 3 | `/n/` | `ㄴ` | 니은 (nieun) | none | alveolar | nasal | `ㄴ` | 나무 *namu* [namu] 'tree'; 눈 *nun* [nun] 'eye / snow'; 안녕 *annyeong* [annjʌŋ] 'hi / well-being' | Realised [n] in onset and coda. **Lateralizes** to [l] when adjacent to ㄹ (유음화: 신라 'Silla' [ɕilla], 천리 [tɕʰʌlli]). Before /i j/ it may be lightly palatalized [nʲ]. As an onset before a back vowel it stays [n]. **South–North:** the South 두음법칙 (initial-sound rule) **drops** word-initial ㄴ before /i j/ (女子 → 여자 [jʌdʑa]); North **retains** it (녀자 [njʌdʑa]). /n/ is also **inserted** at certain compound boundaries before /i j/ (ㄴ-첨가: 한여름 'midsummer' [hannjʌɾɯm]). |
| 4 | `/t/` | `ㄷ` | 디귿 (digeut) | plain | alveolar | stop | `ㄷ` | 다리 *dari* [taɾi] 'leg / bridge'; 구두 *gudu* [kudu] 'dress shoes'; 듣다 *deutda* [tɯt̚t͈a] 'to listen' | Word-initially voiceless lightly aspirated [t]; **voices** to [d] between voiced sounds (구두 [kudu]). In the coda it is unreleased [t̚] and is the neutralization target for ㄷ ㅌ ㅅ ㅆ ㅈ ㅊ ㅎ (음절의 끝소리 규칙). **Palatalizes** to [tɕ] before the suffix-/morpheme-initial /i/ (구개음화: 굳이 'firmly' [kudʑi], 해돋이 [hɛdoʑi]). Before a nasal it nasalizes to [n] (받는 [pannɯn]). Same in South and North. |
| 5 | `/t͈/` | `ㄸ` | 쌍디귿 (ssangdigeut) | tense | alveolar | stop | `ㄸ` | 딸 *ttal* [t͈al] 'daughter'; 땅 *ttang* [t͈aŋ] 'land / ground'; 이따가 *ittaga* [it͈aɡa] 'in a little while' | Stiff-glottis fortis stop: no aspiration, no intervocalic voicing (이따가 keeps [t͈]). Longer, tenser closure than plain /t/ and a high-onset following vowel. Often the surface result of 경음화 after an obstruent coda. ㄸ never occurs as a coda. Same in South and North. |
| 6 | `/l ~ ɾ/` | `ㄹ` | 리을 (rieul) | none | alveolar | liquid | `ㄹ` | 라디오 *radio* [ɾadio] 'radio'; 바람 *baram* [paɾam] 'wind'; 물 *mul* [mul] 'water'; 빨리 *ppalli* [p͈alli] 'quickly' | Single liquid phoneme with complementary realisations: a **tap** [ɾ] as a single intervocalic onset (바람 [paɾam], 다리 [taɾi]); a **lateral** [l] in the coda (물 [mul]) and in the geminate ㄹㄹ (빨리 [p͈alli]), and syllable-finally before another consonant (where it is the coda [l]). ㄴ adjacent to ㄹ becomes [l] (유음화). After most obstruents/nasals (except ㄹ) a following ㄹ becomes [n] (비음화: 종류 'kind' [tɕoŋnju], 음력 [ɯmnjʌk̚]). **South–North:** the South 두음법칙 changes word-initial ㄹ → ㄴ → ∅ (勞動 → 노동 [nodoŋ]; 利益 → 이익 [iik̚]); North **retains** initial ㄹ (로동 [ɾodoŋ], 리익). Native Korean words historically avoid word-initial ㄹ; it is common only in Sino-Korean and loanwords. |
| 7 | `/m/` | `ㅁ` | 미음 (mieum) | none | bilabial | nasal | `ㅁ` | 머리 *meori* [mʌɾi] 'head / hair'; 이름 *ireum* [iɾɯm] 'name'; 엄마 *eomma* [ʌmma] 'mom' | Stable [m] in onset and coda; always voiced. As a coda it triggers tensification of a following plain obstruent in some lexical/grammatical environments (경음화: 감다 [kamt͈a]) and causes a following ㄹ to become [n] (비음화: 음력 [ɯmnjʌk̚]). Same in South and North. |
| 8 | `/p/` | `ㅂ` | 비읍 (bieup) | plain | bilabial | stop | `ㅂ` | 바다 *bada* [pada] 'sea'; 아버지 *abeoji* [abʌdʑi] 'father'; 밥 *bap* [pap̚] 'cooked rice / meal' | Word-initially voiceless lightly aspirated [p]; **voices** to [b] between voiced sounds (아버지 [abʌdʑi]). In the coda it is unreleased [p̚] (밥 [pap̚]) and triggers tensification of a following plain obstruent (경음화: 밥보다 [pap̚p͈oda]). Before a nasal it nasalizes to [m] (비음화: 밥물 [pammul], 입는 [imnɯn]). Same in South and North. |
| 9 | `/p͈/` | `ㅃ` | 쌍비읍 (ssangbieup) | tense | bilabial | stop | `ㅃ` | 뿔 *ppul* [p͈ul] 'horn'; 빵 *ppang* [p͈aŋ] 'bread'; 오빠 *oppa* [op͈a] 'older brother (of a female)' | Stiff-glottis fortis stop: no aspiration, no intervocalic voicing (오빠 stays [op͈a]); longer/tenser closure and high-onset following vowel. Commonly the surface result of 경음화. ㅃ never occurs as a coda. Same in South and North. |
| 10 | `/s/` | `ㅅ` | 시옷 (siot) | plain | alveolar | fricative | `ㅅ` | 사람 *saram* [saɾam] 'person'; 시간 *sigan* [ɕiɡan] 'time / hour'; 옷 *ot* [ot̚] 'clothes' | Phonetically a relatively lax (not strongly tense) sibilant. **Palatalizes** to the alveolo-palatal [ɕ] before /i/ or the glide /j/ (시간 [ɕiɡan], 쉬다 [ɕɥida]); otherwise plain [s] (사람 [saɾam]). It is not voiced between vowels (unlike the plain stops) — it stays voiceless [s]/[ɕ]. As a **coda** it neutralizes to unreleased [t̚] (옷 [ot̚], 옷장 [ot̚t͈aŋ]). Some analyses treat onset ㅅ before a vowel as slightly aspirated [sʰ]. Same in South and North. |
| 11 | `/s͈/` | `ㅆ` | 쌍시옷 (ssangsiot) | tense | alveolar | fricative | `ㅆ` | 쌀 *ssal* [s͈al] '(uncooked) rice'; 씨 *ssi* [ɕ͈i] 'seed / Mr./Ms.'; 있다 *itda* [it̚t͈a] 'to exist / to have' | The fortis counterpart of ㅅ: a tenser, longer sibilant produced with a constricted glottis (쌀 [s͈al]). Like ㅅ it **palatalizes** to tense [ɕ͈] before /i/ or /j/ (씨 [ɕ͈i]). As a **coda** it neutralizes to plain unreleased [t̚] (있다 [it̚t͈a]). It is the only fricative with a tense member — there is no aspirated \*sʰ. Same in South and North. |
| 12 | `/ŋ/` | `ㅇ` | 이응 (ieung) | none | velar | nasal | `ㅇ` | 강 *gang* [kaŋ] 'river'; 사랑 *sarang* [saɾaŋ] 'love'; 아이 *ai* [ai] 'child (onset ㅇ is silent)' | **Dual-function letter.** As a syllable **onset**, ㅇ is a silent placeholder — it carries no consonant and merely fills the obligatory initial slot of the syllable block (아이 [ai], 우유 [uju]). As a **coda**, ㅇ spells the velar nasal /ŋ/ (강 [kaŋ], 사랑 [saɾaŋ]). Because /ŋ/ cannot begin a syllable, **liaison** (연음) does not move a coda ㅇ to a following onset: 강이 stays [kaŋi], never \*[kani]. Same in South and North. |
| 13 | `/tɕ/` | `ㅈ` | 지읒 (jieut) | plain | alveolo-palatal (postalveolar) | affricate | `ㅈ` | 자다 *jada* [tɕada] 'to sleep'; 아버지 *abeoji* [abʌdʑi] 'father'; 낮 *nat* [nat̚] 'daytime' | Word-initially voiceless lightly aspirated [tɕ]; **voices** to [dʑ] between voiced sounds (아버지 [abʌdʑi]). Place is alveolo-palatal/postalveolar for most Seoul speakers (often transcribed [tʃ ~ tɕ]). As a **coda** it neutralizes to unreleased [t̚] (낮 [nat̚]) and triggers tensification of a following plain obstruent. It is the target of 구개음화 only as the output (ㄷ → [tɕ]); ㅈ itself does not further palatalize. Same in South and North. |
| 14 | `/tɕ͈/` | `ㅉ` | 쌍지읒 (ssangjieut) | tense | alveolo-palatal (postalveolar) | affricate | `ㅉ` | 짜다 *jjada* [t͈ɕ͈ada] 'to be salty / to squeeze'; 가짜 *gajja* [kat͈ɕ͈a] 'fake'; 찌개 *jjigae* [t͈ɕ͈iɡɛ] 'stew' | Stiff-glottis fortis affricate: no aspiration, no intervocalic voicing (가짜 stays [kat͈ɕ͈a]); tenser, longer closure than plain ㅈ and a high-onset following vowel. Often written [t͈ɕ͈] (both elements fortis) or simplified [t͈ɕ]. Commonly the surface result of 경음화. ㅉ never occurs as a coda. Same in South and North. |
| 15 | `/tɕʰ/` | `ㅊ` | 치읓 (chieut) | aspirated | alveolo-palatal (postalveolar) | affricate | `ㅊ` | 차다 *chada* [tɕʰada] 'to kick / to be cold / to be full'; 김치 *gimchi* [kimtɕʰi] 'kimchi'; 꽃 *kkot* [k͈ot̚] 'flower' | Strongly aspirated affricate with a breathy release and high-onset following pitch; **not** voiced between vowels (김치 [kimtɕʰi]). As a **coda** it neutralizes to unreleased [t̚] (꽃 [k͈ot̚], 꽃이 → liaison [k͈otɕʰi] re-exposes the underlying ㅊ). It is the aspirated output of 격음화 when ㅈ/ㄷ meets ㅎ (못하다 → [motʰada] for ㄷ; affricate cases e.g. 맞히다 → [matɕʰida]). Same in South and North. |
| 16 | `/kʰ/` | `ㅋ` | 키읔 (kieuk) | aspirated | velar | stop | `ㅋ` | 칼 *kal* [kʰal] 'knife'; 코 *ko* [kʰo] 'nose'; 부엌 *bueok* [puʌk̚] 'kitchen' | Strongly aspirated velar stop with high-onset following pitch; not voiced intervocalically (키 'height' [kʰi]). As a **coda** it neutralizes to unreleased plain [k̚] (부엌 [puʌk̚], 부엌이 → liaison [puʌkʰi] re-exposes the underlying ㅋ). It is the aspirated output of 격음화 (ㄱ + ㅎ → [kʰ], e.g. 축하 [tɕʰukʰa], 국화 [kukʰwa]). Same in South and North. |
| 17 | `/tʰ/` | `ㅌ` | 티읕 (tieut) | aspirated | alveolar | stop | `ㅌ` | 탈 *tal* [tʰal] 'mask / mishap'; 토끼 *tokki* [tʰok͈i] 'rabbit'; 밭 *bat* [pat̚] 'dry field' | Strongly aspirated alveolar stop with high-onset following pitch; not voiced intervocalically. As a **coda** it neutralizes to unreleased plain [t̚] (밭 [pat̚]). **Palatalizes** to [tɕʰ] before suffix-initial /i/ (구개음화: 같이 'together' [katɕʰi], 붙이다 [putɕʰida]). It is the aspirated output of 격음화 (ㄷ + ㅎ → [tʰ], e.g. 맏형 [matʰjʌŋ]; ㅎ + ㄷ → [tʰ], 좋다 [tɕotʰa]). Same in South and North. |
| 18 | `/pʰ/` | `ㅍ` | 피읖 (pieup) | aspirated | bilabial | stop | `ㅍ` | 풀 *pul* [pʰul] 'grass / glue'; 팔 *pal* [pʰal] 'arm / eight'; 앞 *ap* [ap̚] 'front' | Strongly aspirated bilabial stop with high-onset following pitch; not voiced intervocalically. As a **coda** it neutralizes to unreleased plain [p̚] (앞 [ap̚], 앞에 → liaison [apʰe] re-exposes the underlying ㅍ). It is the aspirated output of 격음화 (ㅂ + ㅎ → [pʰ], e.g. 입학 [ipʰak̚]; ㅎ + ㅂ environments). Same in South and North. |
| 19 | `/h/` | `ㅎ` | 히읗 (hieut) | none | glottal | fricative | `ㅎ` | 하늘 *haneul* [hanɯl] 'sky'; 전화 *jeonhwa* [tɕʌnɦwa] ~ [tɕʌnwa] 'telephone'; 좋다 *jota* [tɕotʰa] 'to be good' | Word-initially a clear voiceless [h] (하늘 [hanɯl]); before /i j/ it fronts toward the palatal [ç] (힘 [çim]), before /u w/ toward [ɸ] (후 [ɸu]). **Intervocalically** and between voiced sounds it weakens to a voiced [ɦ] or is often **deleted** entirely (전화 [tɕʌnwa], 좋아 [tɕoa], 안녕하세요 → casual [annjʌŋasejo]). When ㅎ meets a plain stop/affricate it **merges** into the corresponding aspirate (격음화: 좋다 [tɕotʰa], 놓고 [nokʰo], 많다 [mantʰa], 축하 [tɕʰukʰa]). As a coda ㅎ has no independent realisation: it neutralizes/deletes (좋은 → [tɕoɯn]) or fuses with a following obstruent. Same in South and North. |

### Hangul Letter Codepoints

The 19 base consonant letters (자모) keyed to their Unicode **Hangul Compatibility Jamo** codepoints. Tense letters use the doubled (쌍) forms.

| # | IPA | Jamo | Letter name (한글) | RR | Compatibility-Jamo codepoint |
|---|---|---|---|---|---|
| 1 | `/k/` | `ㄱ` | 기역 | giyeok | `U+3131` |
| 2 | `/k͈/` | `ㄲ` | 쌍기역 | ssanggiyeok | `U+3132` |
| 3 | `/n/` | `ㄴ` | 니은 | nieun | `U+3134` |
| 4 | `/t/` | `ㄷ` | 디귿 | digeut | `U+3137` |
| 5 | `/t͈/` | `ㄸ` | 쌍디귿 | ssangdigeut | `U+3138` |
| 6 | `/l ~ ɾ/` | `ㄹ` | 리을 | rieul | `U+3139` |
| 7 | `/m/` | `ㅁ` | 미음 | mieum | `U+3141` |
| 8 | `/p/` | `ㅂ` | 비읍 | bieup | `U+3142` |
| 9 | `/p͈/` | `ㅃ` | 쌍비읍 | ssangbieup | `U+3143` |
| 10 | `/s/` | `ㅅ` | 시옷 | siot | `U+3145` |
| 11 | `/s͈/` | `ㅆ` | 쌍시옷 | ssangsiot | `U+3146` |
| 12 | `/ŋ/` | `ㅇ` | 이응 | ieung | `U+3147` |
| 13 | `/tɕ/` | `ㅈ` | 지읒 | jieut | `U+3148` |
| 14 | `/tɕ͈/` | `ㅉ` | 쌍지읒 | ssangjieut | `U+3149` |
| 15 | `/tɕʰ/` | `ㅊ` | 치읓 | chieut | `U+314A` |
| 16 | `/kʰ/` | `ㅋ` | 키읔 | kieuk | `U+314B` |
| 17 | `/tʰ/` | `ㅌ` | 티읕 | tieut | `U+314C` |
| 18 | `/pʰ/` | `ㅍ` | 피읖 | pieup | `U+314D` |
| 19 | `/h/` | `ㅎ` | 히읗 | hieut | `U+314E` |

### Natural Classes

Groupings of the consonant phonemes by shared phonological features, drawn from the source data.

| Class | Members |
|---|---|
| Plain / lax | `/k/`, `/t/`, `/p/`, `/tɕ/`, `/s/` |
| Tense / fortis | `/k͈/`, `/t͈/`, `/p͈/`, `/tɕ͈/`, `/s͈/` |
| Aspirated | `/kʰ/`, `/tʰ/`, `/pʰ/`, `/tɕʰ/` |
| Stops | `/k/`, `/t/`, `/p/`, `/k͈/`, `/t͈/`, `/p͈/`, `/kʰ/`, `/tʰ/`, `/pʰ/` |
| Affricates | `/tɕ/`, `/tɕ͈/`, `/tɕʰ/` |
| Fricatives | `/s/`, `/s͈/`, `/h/` |
| Sibilants | `/s/`, `/s͈/`, `/tɕ/`, `/tɕ͈/`, `/tɕʰ/` |
| Nasals | `/m/`, `/n/`, `/ŋ/` |
| Liquid | `/l/` |
| Obstruents | `/k/`, `/t/`, `/p/`, `/tɕ/`, `/k͈/`, `/t͈/`, `/p͈/`, `/tɕ͈/`, `/s͈/`, `/kʰ/`, `/tʰ/`, `/pʰ/`, `/tɕʰ/`, `/s/`, `/h/` |
| Sonorants | `/m/`, `/n/`, `/ŋ/`, `/l/` |
| Coda seven sounds (음절의 끝소리) | `/k/`, `/t/`, `/p/`, `/l/`, `/m/`, `/n/`, `/ŋ/` |

## Vowels (Monophthongs)

The Korean vowel inventory (모음 *moeum*). Modern Standard Seoul Korean has roughly **7–8 contrastive monophthongs** — `/a ʌ o u ɯ i/` plus the front-mid pair `/ɛ e/` that is merging — while a more conservative description counts up to **ten** by adding the front rounded monophthongs ㅚ `/ø/` and ㅟ `/y/`. Two reference standards are documented in parallel, mirroring the GA/RP framing of the English guide and the Castilian/Latin-American framing of the Spanish guide: **표준어** (*pyojun-eo*), educated Standard **SOUTH** Korean (Seoul), and **문화어** (*munhwaeo*), the Pyongyang-based **NORTH** Korean standard. For vowels the two standards agree on the core inventory; they differ mainly in (a) whether the 애/에 (ㅐ/ㅔ) merger has run to completion (more advanced in young Seoul speech) and (b) how robustly ㅚ/ㅟ survive as monophthongs (more conservative in the North).

Three defining properties shape this section:

1. **No phonemic vowel length** — an older `/aː/`~`/a/` length contrast (e.g. 말 'speech' `[maːl]` vs 말 'horse' `[mal]`) has been lost for most speakers under ~60 and is not prescribed for learners here.
2. **No lexical stress and no lexical tone** — so unstressed vowels are **not** reduced to schwa `[ə]`. Every vowel keeps its full quality in every syllable, and prosody is carried by phrase-level intonation, not by vowel reduction.
3. **Essentially no active vowel harmony** — Middle Korean had a robust yang/yin (bright/dark) harmony, but in the modern language it survives only vestigially in ideophones and in the verb-ending alternation 아/어 (*-a*/*-eo*).

IPA follows the 2015 revision; `/slashes/` mark phonemic transcription and `[brackets]` mark phonetic detail. No length mark `/ː/` is used in the prescribed forms because modern Standard Korean vowels are not phonemically long. Hangul medial letters (중성 *jungseong*) and their standalone Compatibility-Jamo codepoints are given for each vowel; Revised Romanization (RR, official South Korea 2000) is the companion romanization, with McCune–Reischauer (MR) noted where it diverges. These transcriptions cross-reference the four shipped reader tiers — Scholarly, Pretty (language-neutral Latin), Hangul (한글 composed blocks), and the RR readback of the Hangul.

### Vowel System Overview

The Korean monophthong phonemes plotted on the height/backness/rounding grid. The conservative maximal system has ten simple vowels arranged in a near-symmetrical pattern: a front unrounded series, a back rounded series, a high central/back unrounded vowel ㅡ `/ɯ/`, the low vowel ㅏ `/a/`, and two front **ROUNDED** vowels ㅚ `/ø/` and ㅟ `/y/` that are typologically marked and are the first to be lost. The everyday modern Seoul system collapses to seven or eight: the 애/에 merger reduces `/ɛ e/` to a single mid front `[e̞]`, and ㅚ/ㅟ are usually diphthongized out of the monophthong set, leaving the stable core `/a ʌ o u ɯ i e/`.

#### By Height

| Height | Vowels |
|---|---|
| High (close) | `/i/`, `/y/`, `/ɯ/`, `/u/` |
| Mid | `/e/`, `/ɛ/`, `/ø/`, `/ʌ/`, `/o/` |
| Low (open) | `/a/` |

*ㅐ `/ɛ/` is, in conservative description, open-mid front and slightly lower than ㅔ `/e/`; in merged modern Seoul both fall together at a single mid `[e̞]`. ㅓ `/ʌ/` is a mid-to-open back/central unrounded vowel, often realized closer to `[ɔ̜]`~`[ə̞]` than to cardinal `[ʌ]`.*

#### By Backness

| Backness | Vowels |
|---|---|
| Front unrounded | `/i/`, `/e/`, `/ɛ/` |
| Front rounded | `/y/`, `/ø/` |
| Central | `/ɯ/`, `/ʌ/`, `/a/` |
| Back rounded | `/u/`, `/o/` |

*ㅡ `/ɯ/` is traditionally a close **back** unrounded vowel but is realized centrally `[ɨ]`~`[ɯ̈]` by many Seoul speakers; ㅓ `/ʌ/` and ㅏ `/a/` are best heard as central. Korean's front-rounded `/y ø/` have no English or Spanish counterpart.*

#### By Rounding

| Rounding | Vowels |
|---|---|
| Rounded | `/o/`, `/u/`, `/ø/`, `/y/` |
| Unrounded | `/a/`, `/ʌ/`, `/ɯ/`, `/i/`, `/e/`, `/ɛ/` |

*Rounding pairs front `/i e/` with front-rounded `/y ø/` and back-unrounded `/ɯ/` with back-rounded `/u/`. The loss of `/y ø/` as monophthongs removes the only front-rounded members.*

#### Contrast with English and Spanish

Korean sits between English and Spanish in complexity. Unlike Spanish (5 stable vowels, no length, no reduction) Korean has 7–10 vowels, a marked front-rounded subsystem, and the ㅡ `/ɯ/` high unrounded vowel absent from both reference languages. Unlike English, Korean has **no** phonemic length in the modern standard, **no** tense/lax (free/checked) class system, and crucially **no** vowel reduction to schwa — so, as in Spanish, unstressed vowels keep full quality. The English schwa `/ə/` and the English diphthong-heavy system have no direct Korean equivalent; Korean diphthongs are uniformly **GLIDE-INITIAL** (rising `/j w/` + vowel) plus the unique ㅢ `/ɰi/`, rather than the vowel-final falling diphthongs of English FACE/GOAT/PRICE.

### Monophthong Inventory

The monophthong phonemes with their Hangul medial letter (중성 *jungseong*), standalone Compatibility-Jamo codepoint, phonetic value, and the RR/MR romanizations. Where MR diverges from RR, both are shown.

| IPA | Jamo | Codepoint | Name | Phonetic | RR | MR |
|---|---|---|---|---|---|---|
| `/a/` | `ㅏ` | `U+314F` | open central (low) unrounded | `[a]` ~ `[ä]` | a | a |
| `/ʌ/` | `ㅓ` | `U+3153` | open-mid back/central unrounded | `[ʌ]` ~ `[ɔ̜]` ~ `[ə̞]` | eo | ŏ |
| `/o/` | `ㅗ` | `U+3157` | close-mid back rounded | `[o]` ~ `[o̞]` | o | o |
| `/u/` | `ㅜ` | `U+315C` | close back rounded | `[u]` ~ `[ʉ]` | u | u |
| `/ɯ/` | `ㅡ` | `U+3161` | close back/central unrounded | `[ɯ]` ~ `[ɨ]` ~ `[ɯ̈]` | eu | ŭ |
| `/i/` | `ㅣ` | `U+3163` | close front unrounded | `[i]` | i | i |
| `/e/` | `ㅔ` | `U+3154` | close-mid front unrounded (ㅔ) | `[e]` ~ `[e̞]` | e | e |
| `/ɛ/` | `ㅐ` | `U+3150` | open-mid front unrounded (ㅐ) | `[ɛ]` ~ `[e̞]` (merged) | ae | ae |
| `/ø/` | `ㅚ` | `U+315A` | close-mid front rounded (cons.) ↔ diphthong `[we]` (modern) | `[ø]` (cons.) ~ `[we]` (Seoul) | oe | oe |
| `/y/` | `ㅟ` | `U+315F` | close front rounded (cons.) ↔ diphthong `[wi]` (modern) | `[y]` (cons.) ~ `[ɥi]` ~ `[wi]` (Seoul) | wi | wi |

### Per-Vowel Notes and Example Words

Each vowel is documented with example words pairing several occurrences to demonstrate that quality is constant (no reduction), followed by its allophony notes.

#### `/a/` — ㅏ — open central (low) unrounded

| Word | RR | IPA | Gloss | Note |
|---|---|---|---|---|
| 아기 | agi | `[aɡi]` | baby | word-initial ㅇ is a silent onset placeholder, so 아 = bare `/a/`; the `/k/` of 기 voices to `[ɡ]` intervocalically. |
| 사람 | saram | `[saɾam]` | person | two `/a/` in a stressed-equivalent first and a phrase-medial second syllable — both are full clear `[a]`, never reduced to `[ə]`; intervocalic ㄹ is the tap `[ɾ]`. |
| 말 | mal | `[mal]` | horse / speech | the historical length minimal pair: 말 'horse' was short `[mal]`, 말 'speech' long `[maːl]`; the length contrast is **lost** for most modern speakers, so both are now `[mal]`. |

*Allophony.* A low, essentially central unrounded vowel; the bare IPA glyph `/a/` denotes the front cardinal, but Korean realizes it centrally, so `[ä]` is the more explicit phonetic value. Very stable across both standards. It is the default 'bright/yang' partner in the 아/어 verb-ending alternation (see Vowel Harmony Vestiges). No length and no reduction: the second `/a/` of 사람 is the same `[a]` as the first.

#### `/ʌ/` — ㅓ — open-mid back/central unrounded

| Word | RR | IPA | Gloss | Note |
|---|---|---|---|---|
| 어머니 | eomeoni | `[ʌmʌni]` | mother | two `/ʌ/` in successive syllables, both full quality; RR writes the digraph 'eo', MR the breve letter 'ŏ'. |
| 서울 | Seoul | `[sʌul]` | Seoul (capital) | the city name; the famous RR spelling 'Seoul' is literally s-eo-u-l, with `/ʌ/` as the 'eo'. |
| 넓다 | neolda | `[nʌlt͈a]` | to be wide | shows `/ʌ/` before a cluster coda ㄼ that simplifies to `[l]`; the following ㄷ tenses to `[t͈]` after the obstruent (경음화). |

*Allophony.* Conventionally transcribed `/ʌ/`, but its phonetic target in Seoul Korean is variable and often **not** cardinal back unrounded `[ʌ]`: many speakers produce a more open central `[ə̞]` or a lightly rounded back `[ɔ̜]`, and there is documented overlap with `/o/` for some North-and-East dialects. It is the 'dark/yin' partner of `/a/` in the 아/어 ending alternation. No length contrast (an older short/long `/ʌ/`~`/ʌː/` distinction is, like all length, lost). RR 'eo' must not be misread by English speakers as a sequence; it is one vowel.

#### `/o/` — ㅗ — close-mid back rounded

| Word | RR | IPA | Gloss | Note |
|---|---|---|---|---|
| 오리 | ori | `[oɾi]` | duck | word-initial bare `/o/` (silent ㅇ onset); intervocalic ㄹ = tap `[ɾ]`. |
| 고기 | gogi | `[koɡi]` | meat | lax ㄱ is voiceless `[k]` initially and voiced `[ɡ]` intervocalically; both `/o/` keep full rounded quality. |
| 도시 | dosi | `[toɕi]` | city | `/o/` before `/i/`-conditioned palatalization of ㅅ to `[ɕ]`. |

*Allophony.* A back rounded mid vowel, default `[o̞]` (lowered close-mid), kept distinct from `/u/` by being lower and from `/ʌ/` by being rounded — though the `/o/`~`/u/` and `/o/`~`/ʌ/` distances are compressing for some young speakers (an ongoing 'o-raising' that pushes `/o/` toward `[u]`). No length and no reduction; the final `/o/` of words like 바보 'fool' `[pabo]` is a full rounded vowel, not the reduced `[oʊ̯]`/`[ə]` an English speaker might substitute.

#### `/u/` — ㅜ — close back rounded

| Word | RR | IPA | Gloss | Note |
|---|---|---|---|---|
| 우유 | uyu | `[uju]` | milk | bare `/u/` then the rising diphthong ㅠ `/ju/`; the two are minimally different (vowel vs glide+vowel). |
| 구두 | gudu | `[kudu]` | dress shoes | two `/u/`, both full close rounded; lax ㄷ voices to `[d]` intervocalically. |
| 물 | mul | `[mul]` | water | `/u/` in a closed syllable with coda ㄹ realized as lateral `[l]`. |

*Allophony.* A close back rounded `[u]`, sometimes fronted/centralized to `[ʉ]` by young Seoul speakers (parallel to the centralization of `/ɯ/`). Distinct from `/o/` by greater height and from `/ɯ/` by rounding (a key minimal contrast: 굴 'oyster' `[kul]` vs 글 'writing' `[kɯl]`). No length contrast and no reduction; the `/u/` of 구두 is identical in both syllables.

#### `/ɯ/` — ㅡ — close back/central unrounded

| Word | RR | IPA | Gloss | Note |
|---|---|---|---|---|
| 그릇 | geureut | `[kɯɾɯt̚]` | bowl / dish | two `/ɯ/`; final ㅅ neutralizes to an unreleased `[t̚]` coda (음절의 끝소리 규칙); RR 'eu', MR 'ŭ'. |
| 음악 | eumak | `[ɯmak̚]` | music | word-initial bare `/ɯ/`; final ㄱ is the unreleased coda `[k̚]`. |
| 스승 | seuseung | `[sɯsɯŋ]` | teacher / master | `/ɯ/` in successive syllables; coda ㅇ is `/ŋ/`. |

*Allophony.* The vowel with no English or Spanish counterpart: a high **UNROUNDED** vowel, classically close back `[ɯ]` but very commonly realized as central `[ɨ]`~`[ɯ̈]` in Seoul. It is the 'default/epenthetic' vowel of Korean — inserted to break up consonant sequences in loanword adaptation (e.g. English 'strike' → 스트라이크 *seuteuraikeu*, with `[ɯ]` propping up each illegal cluster). It frequently **devoices** or fully **elides** between voiceless consonants and word-finally in fast speech (e.g. 습니다 `[sɯmnida]` → `[sɯ̥mnida]`/`[smnida]`). RR 'eu' is one vowel, not a sequence. No length, no reduction-to-schwa (the elision above is deletion, not centralization).

#### `/i/` — ㅣ — close front unrounded

| Word | RR | IPA | Gloss | Note |
|---|---|---|---|---|
| 이 | i | `[i]` | tooth / this / two (二) | a bare `/i/` syllable (silent ㅇ onset); a high-frequency homophone set distinguished only by context. |
| 기린 | girin | `[kiɾin]` | giraffe | two `/i/`, both full close front; note that ㄱ before `/i/` stays a stop `[k]` (no affrication, unlike some languages). |
| 시간 | sigan | `[ɕiɡan]` | time / hour | ㅅ before `/i/` becomes `[ɕ]` — the `/i/`-conditioned palatalization that affects every onset ㅅ. |

*Allophony.* A consistently close, tense front unrounded `[i]` in all positions — there is no lax `[ɪ]` counterpart and no shortening unstressed. `/i/` (and the glide `/j/`) is the **trigger** for several signature Korean processes documented in the consonants/rules section: ㅅ → `[ɕ]` (시 `[ɕi]`), 구개음화 palatalization of ㄷ/ㅌ → `[tɕ]`/`[tɕʰ]` across a morpheme boundary (굳이 → `[kudʑi]`), and ㄴ-insertion at compound boundaries. As an unstressed vowel it does not reduce; as the off-glide target it forms the unique ㅢ `/ɰi/`.

#### `/e/` — ㅔ — close-mid front unrounded

| Word | RR | IPA | Gloss | Note |
|---|---|---|---|---|
| 세 | se | `[se]` | three (native, prenominal counter form) | the 애/에 merger means many young Seoul speakers pronounce this identically to 새 'bird' (ㅐ); see The 애/에 Merger. |
| 베개 | begae | `[peɡɛ]` ~ `[peɡe]` | pillow | contains **both** ㅔ (베) and ㅐ (개); conservative speakers keep `[e]` vs `[ɛ]`, merged speakers say `[peɡe]` with one mid vowel for both. |
| 시계 | sigye | `[ɕiɡje]` ~ `[ɕiɡe]` | clock / watch | the medial ㅖ `/je/` is widely simplified to `[e]` after a consonant, so 계 is commonly `[ɡe]`. |

*Allophony.* Conservatively a close-mid front unrounded vowel, slightly higher than ㅐ `/ɛ/`. In merged modern Seoul it is realized at a single mid `[e̞]` that is indistinguishable from merged ㅐ — the 애/에 merger (see dedicated subsection). The glide-initial ㅖ `/je/` is regularly reduced to plain `[e]` after a consonant onset. No length and no reduction.

#### `/ɛ/` — ㅐ — open-mid front unrounded

| Word | RR | IPA | Gloss | Note |
|---|---|---|---|---|
| 새 | sae | `[sɛ]` ~ `[se]` | bird | conservative `[sɛ]`; for merged speakers identical to 세 `[se]` (ㅔ) — the classic merger minimal pair. |
| 개 | gae | `[kɛ]` ~ `[ke]` | dog | high-frequency word showing initial lax ㄱ = `[k]` before the front-mid vowel. |
| 냄새 | naemsae | `[nɛmsɛ]` ~ `[nemse]` | smell / odor | two ㅐ syllables; for merged speakers both are mid `[e̞]`. |

*Allophony.* Conservatively an open-mid front unrounded vowel, lower than ㅔ `/e/`. For the great majority of Seoul speakers born after roughly 1970, ㅐ and ㅔ have **merged** to a single mid `[e̞]`, so `/ɛ/` and `/e/` are no longer distinguished in production or perception (the 애/에 merger; see its dedicated subsection). The orthographic distinction is fully retained in spelling. Like all Korean vowels, no length and no reduction.

#### `/ø/` — ㅚ — close-mid front rounded (conservative) ↔ diphthong `[we]` (modern)

| Word | RR | IPA | Gloss | Note |
|---|---|---|---|---|
| 외국 | oeguk | `[øɡuk̚]` ~ `[weɡuk̚]` | foreign country | conservative monophthong `[ø]`; modern Seoul diphthong `[we]`; final ㄱ = unreleased `[k̚]`. |
| 참외 | chamoe | `[tɕʰamø]` ~ `[tɕʰamwe]` | Korean melon | shows ㅚ word-finally; the diphthongal `[we]` realization is now the Seoul majority. |
| 회사 | hoesa | `[høsa]` ~ `[hwesa]` | company / firm | very high-frequency word; most Seoul speakers say `[hwesa]`. |

*Allophony.* Phonemically a front **ROUNDED** close-mid monophthong `/ø/` in conservative description (and prescribed as such, with the diphthong `[we]` also explicitly **allowed** by the South Korean standard). In practice the monophthong is recessive: most modern Seoul speakers realize ㅚ as the rising diphthong `[we]`, collapsing it toward ㅞ `/we/`. The North Korean standard is somewhat more conservative in retaining the monophthong. Because merged-ㅐ/ㅔ pushes `[e]`≈`[ɛ]`, the diphthongal ㅚ `[we]`, ㅞ `/we/`, and ㅙ `/wɛ/` also tend to fall together (see ㅚ/ㅟ — Monophthong ↔ Diphthong). RR/MR both write 'oe'.

#### `/y/` — ㅟ — close front rounded (conservative) ↔ diphthong `[wi]` (modern)

| Word | RR | IPA | Gloss | Note |
|---|---|---|---|---|
| 위 | wi | `[y]` ~ `[wi]` | top / above / stomach | bare-syllable ㅟ; conservative monophthong `[y]`, modern Seoul diphthong `[wi]`. |
| 귀 | gwi | `[ky]` ~ `[kɥi]` ~ `[kwi]` | ear | shows ㅟ after a consonant; the on-glide `[ɥ]`/`[w]` realization is now usual. |
| 쥐 | jwi | `[tɕy]` ~ `[tɕwi]` | mouse / rat | ㅟ after an affricate onset; diphthongal `[tɕwi]` is the Seoul majority. |

*Allophony.* Phonemically a front **ROUNDED** close monophthong `/y/` in conservative description, with the diphthong `[ɥi]`~`[wi]` also explicitly **allowed** by the standard. As with ㅚ, the monophthong is recessive and most modern Seoul speakers diphthongize ㅟ to `[wi]` (sometimes with a labio-palatal on-glide `[ɥ]`). The North Korean standard retains the monophthong more robustly. Note that RR romanizes ㅟ as 'wi' precisely because the diphthongal pronunciation has become the norm, even though the letter is historically a single rounded vowel. No length contrast.

### Glides and Rising Diphthongs

Korean has three on-glides used to form rising diphthongs (glide + vowel sharing one syllable nucleus): the palatal `/j/`, the labio-velar `/w/`, and the labio-velar approximant `/ɰ/` that occurs **only** in ㅢ `/ɰi/`. Korean glides are **GLIDE-INITIAL** (the glide precedes the vowel); Korean has no native vowel-final (falling) diphthongs of the English FACE/GOAT/PRICE type. The glide slot is the G of the (C)(G)V(C) syllable template, sitting between an optional onset consonant and the vowel nucleus.

#### `/j/` — palatal on-glide (이중모음 'y-series')

| Jamo | IPA | RR | Example | RR | IPA | Gloss |
|---|---|---|---|---|---|---|
| `ㅑ` | `/ja/` | ya | 야구 | yagu | `[jaɡu]` | baseball |
| `ㅕ` | `/jʌ/` | yeo | 여자 | yeoja | `[jʌdʑa]` | woman (South form; North 녀자) |
| `ㅛ` | `/jo/` | yo | 교실 | gyosil | `[kjoɕil]` | classroom |
| `ㅠ` | `/ju/` | yu | 유리 | yuri | `[juɾi]` | glass |
| `ㅒ` | `/jɛ/` | yae | 얘기 | yaegi | `[jɛɡi]` ~ `[jeɡi]` | talk / story (colloquial) |
| `ㅖ` | `/je/` | ye | 예의 | yeui | `[jeɰi]` ~ `[jei]` | courtesy / manners |

*Notes.* `/j/` is the non-syllabic counterpart of `/i/`. After a consonant onset the y-glide is frequently dropped in casual speech for the front-mid vowels: ㅖ `/je/` → `[e]` (시계 `[ɕiɡe]`) and ㅒ `/jɛ/` → `[ɛ]`~`[e]`. The merged 애/에 quality means ㅒ and ㅖ tend toward a single `[je]`≈`[jɛ]`. `/j/` also conditions palatalization of a preceding ㅅ (샤 `[ɕa]`) and participates in 구개음화 and ㄴ-insertion (see the rules section).

#### `/w/` — labio-velar on-glide (이중모음 'w-series')

| Jamo | IPA | RR | Example | RR | IPA | Gloss |
|---|---|---|---|---|---|---|
| `ㅘ` | `/wa/` | wa | 사과 | sagwa | `[saɡwa]` | apple / apology |
| `ㅝ` | `/wʌ/` | wo | 원 | won | `[wʌn]` | won (currency) / circle |
| `ㅙ` | `/wɛ/` | wae | 왜 | wae | `[wɛ]` ~ `[we]` | why |
| `ㅞ` | `/we/` | we | 웨딩 | weding | `[wediŋ]` | wedding (loanword) |

*Notes.* `/w/` is the non-syllabic counterpart of `/u/` (and `/o/`). Distributional gaps reflect rounding dissimilation: there is no `*/wo/` or `*/wu/` (a rounded glide does not precede a rounded back vowel). The three front-mid w-diphthongs ㅙ `/wɛ/`, ㅞ `/we/`, and the diphthongized ㅚ `[we]` are collapsing toward a **single** `[we]` for most Seoul speakers, mirroring the 애/에 merger of the plain vowels — so 왜, 웨, 외 can sound identical. `/w/` before `/i/` is the labio-velar realization of diphthongized ㅟ.

#### `/ɰ/` — velar approximant on-glide (ㅢ only)

| Jamo | IPA | RR | Example | RR | IPA | Gloss |
|---|---|---|---|---|---|---|
| `ㅢ` | `/ɰi/` | ui | 의사 | uisa | `[ɰisa]` | doctor |

*Notes.* The unique unrounded back on-glide `/ɰ/` occurs **only** in ㅢ. ㅢ has **three** prescribed realizations depending on position:

1. word-initially and as a free morpheme it is the full diphthong `[ɰi]` (의사 `[ɰisa]`);
2. after a consonant onset it simplifies to plain `[i]` (희망 'hope' *huimang* → `[himaŋ]`, 무늬 'pattern' *munui* → `[muni]`);
3. as the **genitive/possessive particle** 의 it is conventionally pronounced `[e]` (나의 'my' *naui* → `[naɰi]` formally, `[nae]` colloquially).

These three readings are standard and prescribed, making ㅢ the most context-dependent letter in the vowel system.

### The 애/에 Merger

**애/에 합류 — the ㅐ/ㅔ (`/ɛ/` vs `/e/`) merger.** Historically Korean distinguished ㅐ `/ɛ/` (open-mid front) from ㅔ `/e/` (close-mid front), a contrast carried by minimal pairs such as 새 `/sɛ/` 'bird' vs 세 `/se/` 'three', 개 `/kɛ/` 'dog' vs 게 `/ke/` 'crab', and 내 `/nɛ/` 'my' vs 네 `/ne/` 'your/yes'. In modern Seoul speech these two vowels have **merged** to a single mid front `[e̞]`. The merger is essentially complete for speakers born after roughly 1970 and is advancing in the North as well, though the spelling distinction is fully preserved.

| Standard | Status |
|---|---|
| South (Seoul, 표준어) | Merger is the norm for younger and middle-aged Seoul speakers: ㅐ and ㅔ are a single `[e̞]` in production **and** perception, so the minimal pairs above are homophones. Older speakers and careful/formal registers may still keep a residual height difference. |
| North (Pyongyang, 문화어) | The merger is reported to be somewhat less advanced in 문화어; a height distinction is more often retained, but the trend is in the same direction. |

**Consequences:**

- The plain minimal pairs 새/세, 개/게, 내/네 become homophonous, disambiguated only by context or by spelling.
- The glide-initial pairs follow suit: ㅒ `/jɛ/` ≈ ㅖ `/je/` → a single `[je]`, and the w-series ㅙ `/wɛ/` ≈ ㅞ `/we/` ≈ diphthongized ㅚ `[we]` → a single `[we]`.
- Because RR distinguishes them in writing (*ae* vs *e*, *yae* vs *ye*, *wae* vs *we* vs *oe*), learners must memorize spellings that no longer reflect a pronunciation difference.

**Learner guidance.** For the four reader tiers, a single mid front target `[e̞]` is acceptable for both ㅐ and ㅔ (and correspondingly for the glide pairs). The conservative two-way `[ɛ]` vs `[e]` distinction is given in this guide's example IPA as the first variant, with the merged `[e]` as the second, so a reader may adopt either; the merged value is recommended as the modern Seoul default.

### ㅚ/ㅟ — Monophthong ↔ Diphthong

**ㅚ/ㅟ — the front-rounded monophthong ↔ diphthong question.** ㅚ and ㅟ are the typologically marked front **ROUNDED** vowels of the conservative inventory: ㅚ `/ø/` (close-mid front rounded) and ㅟ `/y/` (close front rounded). Whether they are **single** vowels (monophthongs) or **glide+vowel** sequences (diphthongs) is the central open question of the Korean vowel system, and the answer differs by speaker, register, and standard.

- **Conservative analysis.** In the conservative/prescriptive description (and historically), ㅚ = `[ø]` and ㅟ = `[y]` are pure monophthongs, giving a 10-vowel system with a full front-rounded series paralleling the front-unrounded `/i e ɛ/`. The South Korean Standard Pronunciation rules list `[ø]` and `[y]` as the primary values.
- **Modern Seoul reality.** Most modern Seoul speakers **diphthongize** both: ㅚ → `[we]` (merging it with ㅞ `/we/` and ㅙ `/wɛ/` under the 애/에 collapse) and ㅟ → `[wi]` (sometimes with a labio-palatal on-glide `[ɥi]`). This is so established that RR **romanizes** the diphthongal outcomes: ㅚ is sometimes read as the `[we]` it has become, and ㅟ is spelled 'wi'. With diphthongization, the productive monophthong inventory drops from 10 to 7–8.

| Standard | Position |
|---|---|
| South (표준어) | Lists the monophthongs `[ø]` `[y]` as standard but **explicitly allows** the diphthongal `[we]` `[wi]` as acceptable variants — codifying the change in progress. |
| North (문화어) | More conservative and retains the monophthongal `[ø]` `[y]` more robustly, especially ㅚ. |

**Interaction with the 애/에 merger.** Diphthongized ㅚ `[we]` lands exactly where ㅞ `/we/` and ㅙ `/wɛ/` are converging under the 애/에 merger, so for many Seoul speakers 외, 웨, and 왜 are **all** `[we]` — a triple merger. This is why a learner can treat ㅚ as `[we]` and ㅟ as `[wi]` with no loss of intelligibility in modern Seoul.

**Learner guidance.** This guide gives the conservative monophthong `[ø]`/`[y]` as the first IPA variant and the modern diphthong `[we]`/`[wi]` as the second. The diphthongal values are recommended as the practical modern Seoul default; the monophthongs are the more correct choice for a North Korean (문화어) or conservative formal target.

### No Phonemic Vowel Length

**음의 길이 — vowel length is NOT phonemic in modern Standard Korean.** Older descriptions of Korean recognized a **phonemic** long/short vowel contrast inherited from Middle Korean, surviving into 20th-century Seoul speech as minimal pairs distinguished by length alone:

| Long | Gloss | Short | Gloss |
|---|---|---|---|
| 말 `[maːl]` | speech / language | 말 `[mal]` | horse |
| 눈 `[nuːn]` | snow | 눈 `[nun]` | eye |
| 밤 `[paːm]` | chestnut | 밤 `[pam]` | night |

**Modern status.** For most speakers born after roughly the mid-20th century the length contrast has been **lost**: the pairs above are homophones, disambiguated only by context. Where vestiges remain, length tends to surface only on the **first** syllable of a word and is neutralized elsewhere, and it is unstable even for older speakers.

**Decision for this guide.** Because the prescribed target is modern Standard Seoul speech, this guide does **not** mark vowel length: no `/ː/` appears in the prescribed IPA. The historical long values are mentioned only in the example notes for 말 (under `/a/`) and here, for completeness. This mirrors the Spanish guide's no-length policy and contrasts with the English guide's contrastive use of `/ː/`.

*Note: This is purely a **length** statement. It does not concern the (separate) loss of lexical tone — Korean has no lexical tone in the standard at all (see the suprasegmentals section); the Gyeongsang and Hamgyŏng pitch-accent dialects are a dialectal aside, not part of the reference standards.*

### Vowel Harmony Vestiges

**모음조화 — vowel harmony is vestigial in modern Korean.** Middle Korean had a robust **vowel harmony** system dividing vowels into 'bright/yang' (양성모음) and 'dark/yin' (음성모음) classes (with neutral ㅣ), requiring suffixes to agree in class with the stem. In the modern language this harmony has largely **collapsed** — it is **not** a productive constraint on the lexicon — but two clear vestiges survive and are worth documenting.

#### 아/어 (-a/-eo) ending harmony

The single most important living remnant. The connective/past suffix surfaces as 아 `/a/` (bright) after a stem whose last vowel is the bright ㅏ `/a/` or ㅗ `/o/`, and as 어 `/ʌ/` (dark) after any other stem vowel.

| Stem | Form | IPA | Note |
|---|---|---|---|
| 막- (*mak-*, 'block') | 막아 *maga* | `[maɡa]` | stem vowel ㅏ `/a/` (bright) → 아 ending |
| 볶- (*bokk-*, 'stir-fry') | 볶아 *bokka* | `[pok͈a]` | stem vowel ㅗ `/o/` (bright) → 아 ending |
| 먹- (*meok-*, 'eat') | 먹어 *meogeo* | `[mʌɡʌ]` | stem vowel ㅓ `/ʌ/` (dark) → 어 ending |
| 굽- (*gup-*, 'roast') | 구워 *guwo* | `[kuwʌ]` | stem vowel ㅜ `/u/` (dark) → 어 ending (with irregular ㅂ→w) |

*This is the one productive harmony rule a learner **must** internalize because it governs verb/adjective conjugation throughout the grammar.*

#### 의성어·의태어 (sound/manner mimetics) harmony

Korean's large class of ideophones (mimetic words) uses the bright/dark vowel pairing **expressively**: bright-vowel forms convey small/light/quick/cute, dark-vowel forms convey large/heavy/slow. The alternation is paradigmatic within the ideophone, not imposed by neighboring morphemes.

| Bright | Dark | Gloss |
|---|---|---|
| 졸졸 *joljol* | 줄줄 *juljul* | trickling (small stream) ↔ streaming (larger flow) |
| 반짝반짝 *banjjak* | 번쩍번쩍 *beonjjeok* | twinkling (small) ↔ flashing (big) |
| 캄캄 *kamkam* | 컴컴 *keomkeom* | pitch-dark (closer/smaller) ↔ pitch-dark (vaster/gloomier) |

**Summary.** Outside the 아/어 endings and the ideophone system, modern Korean does **not** enforce vowel harmony; ordinary roots and Sino-Korean vocabulary freely mix bright and dark vowels. Treat harmony as (1) a productive conjugation rule and (2) an expressive ideophone pattern — not as a general phonotactic constraint.

### IPA Symbol Summary

Quick reference of the Korean vowel and glide phonemes with their main phonetic realizations and Hangul/RR correspondences. Values reflect modern Standard Seoul (표준어) as the default; conservative and North (문화어) variants are noted inline.

**Monophthong phonemes (conservative maximal, 10):** `/a/`, `/ʌ/`, `/o/`, `/u/`, `/ɯ/`, `/i/`, `/e/`, `/ɛ/`, `/ø/`, `/y/`

**Stable core (modern Seoul, 7):** `/a/`, `/ʌ/`, `/o/`, `/u/`, `/ɯ/`, `/i/`, `/e/` (= merged ㅐ/ㅔ)

**Glides (3):** `/j/`, `/w/`, `/ɰ/`

#### Principal Realizations

| Vowel | Principal realization |
|---|---|
| ㅏ `/a/` | `[a]` ~ `[ä]`, low central unrounded; stable; bright/yang member. |
| ㅓ `/ʌ/` | `[ʌ]` ~ `[ɔ̜]` ~ `[ə̞]`, mid back/central unrounded; RR 'eo', MR 'ŏ'; dark/yin member. |
| ㅗ `/o/` | `[o]` ~ `[o̞]`, mid back rounded; some young-speaker o-raising toward `[u]`. |
| ㅜ `/u/` | `[u]` ~ `[ʉ]`, close back rounded; some young-speaker fronting. |
| ㅡ `/ɯ/` | `[ɯ]` ~ `[ɨ]` ~ `[ɯ̈]`, close back/central unrounded; epenthetic/default vowel; often devoiced/elided; RR 'eu', MR 'ŭ'. |
| ㅣ `/i/` | `[i]`, close front unrounded; triggers ㅅ→`[ɕ]` and 구개음화. |
| ㅔ `/e/` | `[e]` ~ `[e̞]`; = merged ㅐ/ㅔ in modern Seoul; RR 'e'. |
| ㅐ `/ɛ/` | `[ɛ]` conservative ~ `[e̞]` merged; RR 'ae'. |
| ㅚ `/ø/` | `[ø]` conservative ~ `[we]` modern Seoul; RR 'oe'. |
| ㅟ `/y/` | `[y]` conservative ~ `[wi]`/`[ɥi]` modern Seoul; RR 'wi'. |

#### Diphthong Inventory

| Series | Jamo → IPA |
|---|---|
| j-series | `ㅑ` `/ja/`, `ㅕ` `/jʌ/`, `ㅛ` `/jo/`, `ㅠ` `/ju/`, `ㅒ` `/jɛ/`, `ㅖ` `/je/` |
| w-series | `ㅘ` `/wa/`, `ㅝ` `/wʌ/`, `ㅙ` `/wɛ/`, `ㅞ` `/we/` |
| ɰ-series | `ㅢ` `/ɰi/` (→ `[i]` after a consonant; → `[e]` as the genitive particle) |
| Diphthongized monophthongs | `ㅚ` → `[we]` (modern), `ㅟ` → `[wi]` (modern) |

- **No length.** No length mark `/ː/` is used: modern Standard Korean vowels are not phonemically long. The historical `/a/`~`/aː/` contrast (말 horse vs speech) is lost for most speakers. This matches the Spanish no-length policy and differs from the English guide's contrastive `/ː/`.
- **No schwa.** There is **no** schwa `/ə/` phoneme and **no** weak/reduced vowel set in Korean: because there is no lexical stress, unstressed vowels keep full quality. (The `[ə̞]`-like realization of `/ʌ/` is a quality variant of a full vowel, not reduction.) ㅡ `/ɯ/`, not `[ə]`, is the epenthetic/default vowel.
- **Merger.** ㅐ `/ɛ/` and ㅔ `/e/` are **merged** to `[e̞]` for most modern Seoul speakers (애/에 merger); the diphthongal ㅚ `[we]`, ㅙ `/wɛ/`, and ㅞ `/we/` converge correspondingly to a single `[we]`.

## Diphthongs & Glide–Vowel Sequences

Unlike English (whose diphthongs are Wells lexical sets that glide from one full vowel quality to another) and Spanish (which has both rising glide+vowel and falling vowel+glide diphthongs), Korean "diphthongs" (이중모음 *ijung-moeum*, 'double vowels') are uniformly ON-GLIDE sequences: a non-syllabic glide `/j/`, `/w/`, or `/ɰ/` followed by a vowel nucleus, all written with a single compound medial (중성 *jungseong*) jamo and pronounced within one syllable block. Korean therefore has only RISING diphthongs (glide → nucleus, sonority rising); it has NO phonemic falling/closing diphthongs of the English FACE/PRICE type — a coda glide does not exist, and what looks like a vowel+vowel sequence across a syllable boundary is two separate syllables, not one diphthong.

The inventory splits into three series by glide:

- the **j-SERIES** (palatal on-glide `/j/`): `ㅑ` /ja/, `ㅕ` /jʌ/, `ㅛ` /jo/, `ㅠ` /ju/, `ㅒ` /jɛ/, `ㅖ` /je/;
- the **w-SERIES** (labio-velar on-glide `/w/`): `ㅘ` /wa/, `ㅙ` /wɛ/, `ㅝ` /wʌ/, `ㅞ` /we/, plus `ㅚ` and `ㅟ` when (as is now usual in Seoul speech) they are realized as the diphthongs [we] and [wi] rather than as the conservative front rounded monophthongs [ø] and [y];
- the **ɰ-SERIES**, a single member `ㅢ` /ɰi/ built on the velar/unrounded glide `/ɰ/`.

Korean has no triphthongs. Because Korean syllable structure is (C)(G)V(C), the glide G occupies the medial-onset slot after any onset consonant and before the nucleus; an onset consonant frequently neutralizes or absorbs a following glide (notably ㅖ/ㅒ → [e]/[ɛ], and the historical loss of /j/ after sibilants). Realizations are essentially identical in Standard South Korean (표준어, ROK) and North Korean (문화어, DPRK); the single IPA value per entry suffices, since the diphthong system itself does not diverge between the standards (any minor allophonic or prescriptive differences are noted in prose).

### Diphthong Inventory

The complete Korean on-glide diphthong inventory, organized by glide series. Each row gives the compound medial jamo, its phonemic value, the Unicode Hangul-Compatibility-Jamo codepoint, the glide and nucleus components, the series, and the Revised Romanization (RR) and McCune–Reischauer (MR) readings.

| Jamo | Phonemic | Codepoint | Glide | Nucleus | Series | RR | MR |
|---|---|---|---|---|---|---|---|
| `ㅑ` | /ja/ | `U+3151` | /j/ | /a/ | j-series | ya | ya |
| `ㅕ` | /jʌ/ | `U+3155` | /j/ | /ʌ/ | j-series | yeo | yŏ |
| `ㅛ` | /jo/ | `U+315B` | /j/ | /o/ | j-series | yo | yo |
| `ㅠ` | /ju/ | `U+3160` | /j/ | /u/ | j-series | yu | yu |
| `ㅒ` | /jɛ/ | `U+3152` | /j/ | /ɛ/ | j-series | yae | yae |
| `ㅖ` | /je/ | `U+3156` | /j/ | /e/ | j-series | ye | ye |
| `ㅘ` | /wa/ | `U+3158` | /w/ | /a/ | w-series | wa | wa |
| `ㅙ` | /wɛ/ | `U+3159` | /w/ | /ɛ/ | w-series | wae | wae |
| `ㅝ` | /wʌ/ | `U+315D` | /w/ | /ʌ/ | w-series | wo | wŏ |
| `ㅞ` | /we/ | `U+315E` | /w/ | /e/ | w-series | we | we |
| `ㅚ` | /we/ | `U+315A` | /w/ | /e/ | w-series | oe | oe |
| `ㅟ` | /wi/ | `U+315F` | /w/ | /i/ | w-series | wi | wi |
| `ㅢ` | /ɰi/ | `U+3162` | /ɰ/ | /i/ | ɰ-series | ui | ŭi |

### j-Series (Palatal On-Glide /j/)

The palatal on-glide `/j/` is the non-syllabic counterpart of `/i/`. Compound medials are built from a base vowel jamo plus an added short stroke.

#### `ㅑ` /ja/ — RR *ya*, MR *ya*

Rising diphthong: palatal on-glide [j] + open vowel [a]; the glide onsets the medial and sonority rises into the [a] nucleus. Compound medial = `ㅏ` /a/ with an added short stroke.

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 야구 | yagu | [jaɡu] | baseball |
| 이야기 | iyagi | [ijaɡi] | story, talk |
| 약 | yak | [jak̚] | medicine |

The Unicode jungseong order places `ㅑ` at index 2 (after `ㅏ` `ㅐ`). The glide [j] is the non-syllabic counterpart of /i/. After most onset consonants the /j/ is fully realized (가 [ka] vs 갸 [kja]), but Standard Korean phonotactics historically banned /j/ after the sibilants `ㅅ ㅈ ㅊ ㅆ ㅉ`, so spellings like 샤 자 차 are pronounced [ɕa~sʲa tɕa tɕʰa] with the palatal already fused into the consonant rather than as a separate [ja]-type glide. Identical in South (표준어) and North (문화어).

#### `ㅕ` /jʌ/ — RR *yeo*, MR *yŏ*

Rising diphthong: palatal on-glide [j] + open-mid back unrounded vowel [ʌ]. Compound medial = `ㅓ` /ʌ/ with an added stroke; very high-frequency, including the polite verb ending -어요 → -여요 type alternations and Sino-Korean morphemes.

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 여자 | yeoja | [jʌdʑa] | woman |
| 여름 | yeoreum | [jʌɾɯm] | summer |
| 영어 | yeongeo | [jʌŋʌ] | English (language) |

The nucleus [ʌ] is somewhat raised/centralized toward [ə]~[ɘ] for many Seoul speakers, so [jʌ] is often heard as [jə]. 여자 'woman' is a textbook case of the 두음법칙 (initial-sound rule): the underlying Sino-Korean morpheme is 女 (historically 녀), and South Korean (ROK) drops the initial `ㄴ` before /j/ → 여자 [jʌdʑa]; North Korean (DPRK) RETAINS it as 녀자 [njʌdʑa]. This is the clearest South↔North divergence touching the j-series. The RR romanization 'yeo' uses the digraph ⟨eo⟩ for /ʌ/; MR writes 'yŏ'.

#### `ㅛ` /jo/ — RR *yo*, MR *yo*

Rising diphthong: palatal on-glide [j] + close-mid back rounded vowel [o]. Compound medial = `ㅗ` /o/ with an added stroke; carries the very common polite sentence-final particle -요.

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 교회 | gyohoe | [kjoɦwe] | church |
| 요리 | yori | [joɾi] | cooking, cuisine |
| 안녕하세요 | annyeonghaseyo | [annjʌŋɦasejo] | hello / how are you (polite) |

The nucleus stays a fully rounded back [o] with no reduction. `ㅛ` is extremely frequent because the polite (해요체 *haeyoche*) sentence ender -요 attaches to countless utterances (안녕하세요, 가요, 좋아요). Intervocalic `ㅎ` in 교회 weakens to voiced [ɦ] (or deletes for many speakers → [kjowe]); the diphthong itself is unaffected. Identical in South and North.

#### `ㅠ` /ju/ — RR *yu*, MR *yu*

Rising diphthong: palatal on-glide [j] + close back rounded vowel [u]. Compound medial = `ㅜ` /u/ with an added stroke.

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 우유 | uyu | [uju] | milk |
| 유리 | yuri | [juɾi] | glass |
| 자유 | jayu | [tɕaju] | freedom |

[u] is a fully back, rounded close vowel (distinct from the unrounded `ㅡ` /ɯ/). The minimal pair 우유 [uju] 'milk' vs the un-glided 우우 shows the [j] clearly. Common in Sino-Korean (유 = 由, 油, 有, 流, etc.). Identical in South and North; the 두음법칙 does not affect `ㅠ` specifically beyond the general ㄹ/ㄴ → ∅ patterns already noted for `ㅕ`.

#### `ㅒ` /jɛ/ — RR *yae*, MR *yae*

Rising diphthong: palatal on-glide [j] + near-open front vowel [ɛ]. Compound medial historically = `ㅑ` + `ㅣ`; the rarest j-series diphthong, largely confined to a few demonstratives and interjections.

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 얘기 | yaegi | [jɛɡi] | talk, chat (contraction of 이야기) |
| 얘 | yae | [jɛ] | this child / hey (you) |
| 쟤 | jyae | [tɕɛ] | that child (over there) |

Two large mergers affect `ㅒ`. First, the 애/에 merger (`ㅐ`/`ㅔ` → [e̞]) means the [ɛ] nucleus of `ㅒ` is for most younger Seoul speakers identical to the [e] of `ㅖ`, so `ㅒ` and `ㅖ` are frequently homophonous as [je]. Second, after an onset consonant the /j/ glide tends to drop, so 쟤 ('that kid') is realized [tɕɛ]~[tɕe], not [tɕjɛ] — illustrating the general rule that ㅖ/ㅒ → [e]/[ɛ] (glide loss) after a consonant. `ㅒ` is very low-frequency overall. Identical in South and North.

#### `ㅖ` /je/ — RR *ye*, MR *ye*

Rising diphthong: palatal on-glide [j] + close-mid front vowel [e]. Compound medial historically = `ㅕ` + `ㅣ`; common in Sino-Korean morphemes (例, 禮, 藝, 豫).

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 예 | ye | [je] | yes; example |
| 시계 | sigye | [ɕiɡje]~[ɕiɡe] | clock, watch |
| 차례 | charye | [tɕʰaɾje] | turn, order; ancestral rite |

Key allophonic rule: `ㅖ` keeps its full [je] only word-initially or after no consonant (예 [je], 예수 [jesu] 'Jesus'); AFTER a consonant other than the 'silent' `ㅇ`, the glide is regularly dropped so `ㅖ` → [e]. Thus 시계 'clock' is standardly [ɕiɡje] but very commonly [ɕiɡe], and 계산 'calculation' is [kjesan]~[kesan]. Standard South Korean prescriptively allows BOTH the [je] and the reduced [e] pronunciation after a consonant. Because of the 애/에 merger `ㅖ` and `ㅒ` collapse toward a single [je]. Identical in South and North.

### w-Series (Labio-Velar On-Glide /w/)

The labio-velar on-glide `/w/` is the non-syllabic counterpart of `/u/`. The w-series compound medials are visibly built from `ㅗ` or `ㅜ` (the rounded vowels) plus a following vowel jamo, with the rounded element supplying the rounding for the glide. This series also absorbs the two historically front-rounded monophthongs `ㅚ` [ø] and `ㅟ` [y] in their now-dominant diphthongal readings.

#### `ㅘ` /wa/ — RR *wa*, MR *wa*

Rising diphthong: labio-velar on-glide [w] + open vowel [a]. Compound medial = `ㅗ` /o/ + `ㅏ` /a/ written side by side; the w is the non-syllabic counterpart of /u/ (the `ㅗ` element supplies the rounding).

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 사과 | sagwa | [saɡwa] | apple; apology |
| 과일 | gwail | [kwaiɭ] | fruit |
| 와요 | wayo | [wajo] | (someone) comes (polite) |

The w-series compound medials are visibly built from `ㅗ` or `ㅜ` (the rounded vowels) plus a following vowel jamo: `ㅘ` = `ㅗ`+`ㅏ`. The glide [w] is fully rounded and back-to-front. Very productive: it also arises by 연음/contraction when a verb stem in `ㅗ` meets the connective -아 (오- + -아 → 와 [wa]). Identical in South and North.

#### `ㅙ` /wɛ/ — RR *wae*, MR *wae*

Rising diphthong: labio-velar on-glide [w] + near-open front vowel [ɛ]. Compound medial = `ㅗ` + `ㅐ`. One of the three jamo (`ㅙ ㅚ ㅞ`) that have merged in pronunciation to [we] for most modern speakers.

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 왜 | wae | [wɛ]~[we] | why |
| 돼지 | dwaeji | [twɛdʑi]~[twedʑi] | pig |
| 괜찮아요 | gwaenchanayo | [kwɛntɕʰanajo]~[kwentɕʰanajo] | it's okay / I'm fine |

THE `ㅙ`/`ㅚ`/`ㅞ` MERGER: because of the 애/에 merger the nuclei of `ㅙ` [wɛ], `ㅚ` [we] and `ㅞ` [we] have collapsed, so for most younger Seoul speakers 왜 (ㅙ), 외 (ㅚ) and 웨 (ㅞ) are all pronounced [we] and are homophones. `ㅙ` thus surfaces as [wɛ] in conservative description but [we] in mainstream modern speech. Distinguishing the three in writing is a common Korean spelling difficulty. Identical phonology in South and North; North prescription is slightly more conservative about the [wɛ]/[we] distinction.

#### `ㅝ` /wʌ/ — RR *wo*, MR *wŏ*

Rising diphthong: labio-velar on-glide [w] + open-mid back unrounded vowel [ʌ]. Compound medial = `ㅜ` /u/ + `ㅓ` /ʌ/ (the `ㅜ` supplies the rounding for the glide).

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 원 | won | [wʌn] | won (currency); circle |
| 더워요 | deowoyo | [tʌwʌjo] | it's hot (weather) |
| 뭐 | mwo | [mwʌ]~[mʌ] | what (contraction of 무엇) |

Parallels `ㅕ` /jʌ/ in the w-series; the nucleus [ʌ] is again often raised toward [ə]. `ㅝ` arises productively from `ㅜ`-stem verbs plus the connective -어 (e.g. 덥- → 더워, and 추워, 고마워). The high-frequency contraction 뭐 'what' (< 무엇) is widely reduced further to [mʌ] in casual speech, dropping the glide. RR 'wo', MR 'wŏ'. Identical in South and North.

#### `ㅞ` /we/ — RR *we*, MR *we*

Rising diphthong: labio-velar on-glide [w] + close-mid front vowel [e]. Compound medial = `ㅜ` /u/ + `ㅔ` /e/; the rarest w-series jamo, found mainly in loanwords and a few native words.

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 웨딩 | weding | [wediŋ] | wedding (loanword) |
| 스웨터 | seuweteo | [sɯwetʰʌ] | sweater (loanword) |
| 궤도 | gwedo | [kwedo] | orbit, track |

`ㅞ` is the natural [we] and is the merger target into which `ㅚ` and (via the 애/에 merger) `ㅙ` collapse: 웨 (ㅞ) = 외 (ㅚ) = 왜 (ㅙ) = [we] for most speakers. It is the lowest-frequency w-series medial in native vocabulary and is encountered mostly in transcriptions of foreign words (웨이터 'waiter', 웹 'web'). Identical in South and North.

#### `ㅚ` /we/ — RR *oe*, MR *oe*

Historically a front rounded MONOPHTHONG [ø] (the conservative value still recognized by Standard Korean), but in modern Seoul speech overwhelmingly realized as the RISING DIPHTHONG [we]; listed here in its diphthongal reading. Compound medial = `ㅗ` /o/ + `ㅣ` /i/.

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 외국 | oeguk | [ø̞ɡuk̚]~[weɡuk̚] | foreign country |
| 회사 | hoesa | [ɸø̞sa]~[ɦwesa] | company, firm |
| 교회 | gyohoe | [kjoɦø̞]~[kjoɦwe] | church |

`ㅚ` is one of the two historically front-rounded monophthongs (with `ㅟ`). Standard Korean (표준어) prescriptively recognizes the monophthong [ø] but explicitly ALSO permits the diphthong [we], which is now the dominant Seoul realization. Once diphthongized, `ㅚ` [we] merges completely with `ㅞ` [we] and (via the 애/에 merger) with `ㅙ`, so 외/웨/왜 are homophones. The RR romanization is 'oe' (reflecting the spelling, not the sound). The conservative monophthong [ø] survives more in older, careful, and some North Korean speech. Note the onset `ㅎ` in 회사 may surface as [ɸ] before a rounded element, or as [ɦ]/[w] in the diphthongal reading.

#### `ㅟ` /wi/ — RR *wi*, MR *wi*

Historically a front rounded MONOPHTHONG [y] (the conservative value still recognized by Standard Korean), but in modern Seoul speech overwhelmingly realized as the RISING DIPHTHONG [wi]; listed here in its diphthongal reading. Compound medial = `ㅜ` /u/ + `ㅣ` /i/.

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 위 | wi | [y]~[wi] | above, top; stomach |
| 가위 | gawi | [ka.y]~[kawi] | scissors |
| 쉬워요 | swiwoyo | [ɕywʌjo]~[ɕwiwʌjo] | it's easy |

The front-rounded counterpart of `ㅚ`. Standard Korean recognizes the conservative monophthong [y] but also permits — and Seoul speech now favors — the diphthong [wi]. After the sibilant `ㅅ` the result is the palatalized [ɕ] plus the glide/vowel (쉬 [ɕy]~[ɕwi]). Because [wi] ends in a front close [i], some descriptions treat `ㅟ` as having a slightly different glide quality from the other w-series members (the lips round for [w] then spread for [i]). RR 'wi', MR 'wi'. The monophthong [y] survives chiefly in conservative and some North Korean speech.

### ɰ-Series (Velar/Unrounded On-Glide /ɰ/)

A single member built on the velar/close-central unrounded glide `/ɰ/`, the non-syllabic counterpart of `ㅡ` /ɯ/. This glide is the rarest in Korean and exists ONLY in this diphthong.

#### `ㅢ` /ɰi/ — RR *ui*, MR *ŭi*

The sole ɰ-series diphthong and the most phonologically complex Korean vowel: an unrounded velar/close central on-glide [ɰ] (the non-syllabic counterpart of `ㅡ` /ɯ/) + close front vowel [i]. Compound medial = `ㅡ` /ɯ/ + `ㅣ` /i/. Famous for having THREE context-dependent readings.

| Word | RR | IPA | Gloss |
|---|---|---|---|
| 의사 | uisa | [ɰisa] | doctor (word-initial → [ɰi]) |
| 회의 | hoeui | [ɦwei]~[ɦwe.i] | meeting (non-initial syllable → [i]) |
| 민주주의의 | minjujuuiui | [mindʑudʑuie] | of democracy (possessive 의 → [e]) |

THREE STANDARD READINGS of `ㅢ` (all sanctioned by 표준어):

1. word-INITIAL or in a stand-alone syllable → the full diphthong [ɰi] (의사 'doctor' [ɰisa], 의자 'chair' [ɰidʑa]);
2. in a NON-INITIAL syllable, or after any onset consonant, → simply [i] (회의 'meeting' [ɦwei], 무늬 'pattern' [muni], 희망 'hope' [çimaŋ]);
3. when `ㅢ` is the POSSESSIVE/genitive particle 의 ('of') → it is pronounced [e] (나의 'my' [nae], 우리의 'our' [uɾie]).

The word 민주주의의 'of democracy' famously chains all the effects: 主義 ...주의's non-initial 의 → [i], and the final particle 의 → [e], giving [mindʑudʑuie]. The glide [ɰ] is the rarest in Korean and exists ONLY in this diphthong. RR 'ui', MR 'ŭi'. South and North agree on the inventory; the three-way reading is a standard-language convention shared by both.

### Summary

*Korean diphthongs are exclusively RISING on-glide + vowel sequences written with compound medial jamo, in three series: j-series (`ㅑ` /ja/, `ㅕ` /jʌ/, `ㅛ` /jo/, `ㅠ` /ju/, `ㅒ` /jɛ/, `ㅖ` /je/), w-series (`ㅘ` /wa/, `ㅙ` /wɛ/, `ㅝ` /wʌ/, `ㅞ` /we/, plus `ㅚ` [we] and `ㅟ` [wi] in their now-dominant diphthongal readings), and the single ɰ-series member `ㅢ` /ɰi/. Korean has NO phonemic falling/closing diphthongs (no English-style FACE/PRICE vowel-to-vowel glides) and NO triphthongs; a coda glide is not part of the (C)(G)V(C) syllable. Three merger/reduction patterns dominate the modern Seoul realization and should be double-checked by any reviewer: (1) the 애/에 merger ([ɛ]≈[e]) which makes `ㅒ`≈`ㅖ` and collapses `ㅙ`/`ㅚ`/`ㅞ` all to [we]; (2) glide-dropping after a consonant, by which ㅖ/ㅒ → [e]/[ɛ] (시계 [ɕiɡe], 쟤 [tɕɛ]) and by which the historical ban on /j/ after sibilants removes the glide in 샤/자/차-type syllables; and (3) the diphthongization of the conservative front-rounded monophthongs `ㅚ` [ø] → [we] and `ㅟ` [y] → [wi], with the monophthongal values surviving chiefly in older, careful, and North Korean (문화어) speech. The triple reading of `ㅢ` ([ɰi] initial / [i] non-initial or post-consonantal / [e] as the possessive particle 의) is the single most reviewer-sensitive point. These materials cross-reference the four reader tiers of the Korean Peshitta — Scholarly and Pretty (language-neutral Latin), Hangul (한글 composed blocks), and Revised Romanization (RR readback of the Hangul).*

## Consonant–Vowel IPA Matrix

Systematic consonant + vowel (CV) syllable matrix pairing each of Korean's 19 consonant phonemes (자음) with a representative 7-vowel column set drawn from the 7–8 monophthongs of modern Seoul speech (8 in conservative speech, ~7 after the 애/에 merger): ㅏ /a/, ㅓ /ʌ/, ㅗ /o/, ㅜ /u/, ㅡ /ɯ/, ㅣ /i/, ㅐ /ɛ/ (the ㅔ /e/ vowel is omitted from the columns because for most younger Seoul speakers ㅐ and ㅔ have merged to [e̞] — the 애/에 merger — and are represented here by the single ㅐ /ɛ/ column; see the Accent Notes below). Each cell gives the composed Hangul syllable block (한글 음절자), its Revised Romanization (RR), and the phonemic IPA; the combinations are read together with each consonant's phonetic note for the principal allophonic realizations (intervocalic voicing of lax stops, ㅅ → [ɕ] before /i/, ㅎ-weakening, ㄹ tap vs lateral, etc.). The matrix is exhaustive over the inventory (19 consonants × 7 vowels = 133 composed CV syllables). Transcriptions are PHONEMIC: voicing of the lax series (ㄱ ㄷ ㅂ ㅈ → [ɡ d b dʑ] between voiced sounds) is an ALLOPHONIC fact noted per row, not encoded in the cell values, since these consonants are voiceless [k t p tɕ] in the absolute word-initial position the matrix represents. Korean has NO phonemic voicing contrast; its signature is instead a THREE-WAY laryngeal contrast among lax, tense (fortis), and aspirated obstruents.

- **Reference accent:** Standard South Korean (Seoul) — 표준어 (pyojun-eo), educated Seoul speech
- **Secondary reference accent:** North Korean (Munhwaeo) — 문화어 (munhwaeo), Pyongyang-based standard
- **Transcription level:** phonemic

### Reference Vowels

The seven reference monophthongs used as columns in the matrix. Each is keyed to its jamo (모음 letter), Revised Romanization (RR), and articulatory description, with example syllables. Vowel qualities use Standard Seoul values; there is no length contrast and no vowel reduction in modern Seoul speech.

| Vowel | Jamo | RR | Name | Example | Note |
|---|---|---|---|---|---|
| /a/ | `ㅏ` | a | open (low) central-to-back unrounded vowel | 가 /ka/ ('edge'); 사 /sa/ in 사람 /saɾam/ ('person') | Stable [a], often slightly back. No length contrast in modern Seoul speech (the older 長/短 vowel-length distinction has been lost); no unstressed reduction — Korean has NO schwa and NO vowel reduction, so /a/ keeps full quality regardless of position in the accentual phrase. |
| /ʌ/ | `ㅓ` | eo | open-mid back unrounded vowel | 거 /kʌ/ ('thing', colloquial); 서울 /sʌul/ ('Seoul') | Romanized ⟨eo⟩ in RR and ⟨ŏ⟩ (o-breve) in McCune–Reischauer. Open-mid back unrounded [ʌ], often realized somewhat lowered/centralized [ʌ̞~ɔ̜] in Seoul; clearly distinct from rounded ㅗ /o/. North Korean 문화어 tends to a more rounded, backed [ɔ]-like value. |
| /o/ | `ㅗ` | o | close-mid back rounded vowel | 고 /ko/ in 고기 /koɡi/ ('meat'); 오 /o/ ('five') | Close-mid back rounded [o]. For many younger Seoul speakers ㅗ /o/ is raising and the unstressed/phrase-medial contrast between ㅗ /o/ and ㅜ /u/ is narrowing, though they remain phonemically distinct. No length contrast, no reduction. |
| /u/ | `ㅜ` | u | close back rounded vowel | 구 /ku/ ('nine'); 우유 /uju/ ('milk') | Close back rounded [u], sometimes centralized/fronted [ʉ] in fast Seoul speech. Its non-syllabic counterpart is the on-glide /w/ in diphthongs (ㅘ /wa/, ㅝ /wʌ/, etc.). |
| /ɯ/ | `ㅡ` | eu | close back unrounded vowel | 그 /kɯ/ ('that'); 음악 /ɯmak/ ('music') | Close unrounded [ɯ], frequently centralized to [ɨ]; the most cross-linguistically marked Korean vowel. Romanized ⟨eu⟩ in RR and ⟨ŭ⟩ (u-breve) in McCune–Reischauer. Often devoiced or elided between voiceless consonants (e.g. 그렇다). Its non-syllabic counterpart is the glide /ɰ/ found only in ㅢ /ɰi/. |
| /i/ | `ㅣ` | i | close front unrounded vowel | 기 /ki/ ('energy, 氣'); 이 /i/ ('two; this; tooth') | Stable close front unrounded [i]. Triggers two important onset alternations in this matrix: ㅅ /s/ → [ɕ] before /i/ (and /j/), and the historical/derivational palatalization 구개음화 of ㄷ ㅌ → [tɕ tɕʰ] before /i j/ across a morpheme boundary. Its non-syllabic counterpart is the on-glide /j/. |
| /ɛ/ | `ㅐ` | ae | near-open / open-mid front unrounded vowel (merged with ㅔ /e/ for most Seoul speakers) | 개 /kɛ/ ('dog'); 새 /sɛ/ ('bird; new') | Historically ㅐ /ɛ/ (open-mid–near-open front) contrasted with ㅔ /e/ (close-mid front), e.g. 개 'dog' vs 게 'crab'. For most speakers born after roughly the 1970s these have MERGED to a single mid front [e̞] — the 애/에 merger — so this single column stands in for both. RR romanizes ㅐ as ⟨ae⟩ and ㅔ as ⟨e⟩; the merger is purely phonetic and does not change the spelling. Conservative and older speakers, and careful North Korean 문화어, may still keep ㅐ /ɛ/ ≠ ㅔ /e/. |

### CV Matrix

Each cell gives the composed Hangul syllable, its Revised Romanization, and the phonemic IPA in the form `한글` RR `/ipa/`. Columns are the seven reference monophthongs; the **Base IPA** column gives the consonant phoneme on its own, and **Series** records its laryngeal/manner class. Cells are PHONEMIC; consult the Phonetic Notes for allophonic realizations (intervocalic voicing, [ɕ] before /i/, palatalization, ㅎ-weakening, ㄹ tap/lateral, silent ㅇ onset).

| Consonant | Jamo | Series | Base IPA | ㅏ /a/ | ㅓ /ʌ/ | ㅗ /o/ | ㅜ /u/ | ㅡ /ɯ/ | ㅣ /i/ | ㅐ /ɛ/ |
|---|---|---|---|---|---|---|---|---|---|---|
| lax (lenis) velar plosive | `ㄱ` | lax (plain/lenis) | /k/ | 가 ga /ka/ | 거 geo /kʌ/ | 고 go /ko/ | 구 gu /ku/ | 그 geu /kɯ/ | 기 gi /ki/ | 개 gae /kɛ/ |
| tense (fortis) velar plosive | `ㄲ` | tense (fortis) | /k͈/ | 까 kka /k͈a/ | 꺼 kkeo /k͈ʌ/ | 꼬 kko /k͈o/ | 꾸 kku /k͈u/ | 끄 kkeu /k͈ɯ/ | 끼 kki /k͈i/ | 깨 kkae /k͈ɛ/ |
| voiced alveolar nasal | `ㄴ` | nasal | /n/ | 나 na /na/ | 너 neo /nʌ/ | 노 no /no/ | 누 nu /nu/ | 느 neu /nɯ/ | 니 ni /ni/ | 내 nae /nɛ/ |
| lax (lenis) alveolar plosive | `ㄷ` | lax (plain/lenis) | /t/ | 다 da /ta/ | 더 deo /tʌ/ | 도 do /to/ | 두 du /tu/ | 드 deu /tɯ/ | 디 di /ti/ | 대 dae /tɛ/ |
| tense (fortis) alveolar plosive | `ㄸ` | tense (fortis) | /t͈/ | 따 tta /t͈a/ | 떠 tteo /t͈ʌ/ | 또 tto /t͈o/ | 뚜 ttu /t͈u/ | 뜨 tteu /t͈ɯ/ | 띠 tti /t͈i/ | 때 ttae /t͈ɛ/ |
| liquid: alveolar lateral approximant ~ tap | `ㄹ` | liquid | /l ~ ɾ/ | 라 ra /ɾa/ | 러 reo /ɾʌ/ | 로 ro /ɾo/ | 루 ru /ɾu/ | 르 reu /ɾɯ/ | 리 ri /ɾi/ | 래 rae /ɾɛ/ |
| voiced bilabial nasal | `ㅁ` | nasal | /m/ | 마 ma /ma/ | 머 meo /mʌ/ | 모 mo /mo/ | 무 mu /mu/ | 므 meu /mɯ/ | 미 mi /mi/ | 매 mae /mɛ/ |
| lax (lenis) bilabial plosive | `ㅂ` | lax (plain/lenis) | /p/ | 바 ba /pa/ | 버 beo /pʌ/ | 보 bo /po/ | 부 bu /pu/ | 브 beu /pɯ/ | 비 bi /pi/ | 배 bae /pɛ/ |
| tense (fortis) bilabial plosive | `ㅃ` | tense (fortis) | /p͈/ | 빠 ppa /p͈a/ | 뻐 ppeo /p͈ʌ/ | 뽀 ppo /p͈o/ | 뿌 ppu /p͈u/ | 쁘 ppeu /p͈ɯ/ | 삐 ppi /p͈i/ | 빼 ppae /p͈ɛ/ |
| lax alveolar (sibilant) fricative | `ㅅ` | fricative | /s/ | 사 sa /sa/ | 서 seo /sʌ/ | 소 so /so/ | 수 su /su/ | 스 seu /sɯ/ | 시 si /ɕi/ | 새 sae /sɛ/ |
| tense (fortis) alveolar (sibilant) fricative | `ㅆ` | tense (fortis) | /s͈/ | 싸 ssa /s͈a/ | 써 sseo /s͈ʌ/ | 쏘 sso /s͈o/ | 쑤 ssu /s͈u/ | 쓰 sseu /s͈ɯ/ | 씨 ssi /ɕ͈i/ | 쌔 ssae /s͈ɛ/ |
| null onset (ㅇ as 초성) — phonemic /ŋ/ only as coda | `ㅇ` | silent onset placeholder / coda nasal | /∅/ (onset) · /ŋ/ (coda) | 아 a /a/ | 어 eo /ʌ/ | 오 o /o/ | 우 u /u/ | 으 eu /ɯ/ | 이 i /i/ | 애 ae /ɛ/ |
| lax (lenis) alveolo-palatal affricate | `ㅈ` | lax (plain/lenis) | /tɕ/ | 자 ja /tɕa/ | 저 jeo /tɕʌ/ | 조 jo /tɕo/ | 주 ju /tɕu/ | 즈 jeu /tɕɯ/ | 지 ji /tɕi/ | 재 jae /tɕɛ/ |
| tense (fortis) alveolo-palatal affricate | `ㅉ` | tense (fortis) | /tɕ͈/ | 짜 jja /tɕ͈a/ | 쩌 jjeo /tɕ͈ʌ/ | 쪼 jjo /tɕ͈o/ | 쭈 jju /tɕ͈u/ | 쯔 jjeu /tɕ͈ɯ/ | 찌 jji /tɕ͈i/ | 째 jjae /tɕ͈ɛ/ |
| aspirated alveolo-palatal affricate | `ㅊ` | aspirated | /tɕʰ/ | 차 cha /tɕʰa/ | 처 cheo /tɕʰʌ/ | 초 cho /tɕʰo/ | 추 chu /tɕʰu/ | 츠 cheu /tɕʰɯ/ | 치 chi /tɕʰi/ | 채 chae /tɕʰɛ/ |
| aspirated velar plosive | `ㅋ` | aspirated | /kʰ/ | 카 ka /kʰa/ | 커 keo /kʰʌ/ | 코 ko /kʰo/ | 쿠 ku /kʰu/ | 크 keu /kʰɯ/ | 키 ki /kʰi/ | 캐 kae /kʰɛ/ |
| aspirated alveolar plosive | `ㅌ` | aspirated | /tʰ/ | 타 ta /tʰa/ | 터 teo /tʰʌ/ | 토 to /tʰo/ | 투 tu /tʰu/ | 트 teu /tʰɯ/ | 티 ti /tʰi/ | 태 tae /tʰɛ/ |
| aspirated bilabial plosive | `ㅍ` | aspirated | /pʰ/ | 파 pa /pʰa/ | 퍼 peo /pʰʌ/ | 포 po /pʰo/ | 푸 pu /pʰu/ | 프 peu /pʰɯ/ | 피 pi /pʰi/ | 패 pae /pʰɛ/ |
| voiceless glottal fricative | `ㅎ` | fricative | /h/ | 하 ha /ha/ | 허 heo /hʌ/ | 호 ho /ho/ | 후 hu /hu/ | 흐 heu /hɯ/ | 히 hi /hi/ | 해 hae /hɛ/ |

### Phonetic Notes

Principal allophonic realizations and example words for each consonant onset. These describe how the phonemic CV cells above surface in actual speech.

| Consonant | Jamo | Example word | Phonetic Note |
|---|---|---|---|
| /k/ | `ㄱ` | 가다 /kada/ ('to go'); 고기 /koki/ → [koɡi] ('meat') | Lax velar stop. Voiceless and lightly aspirated [k] word-initially; VOICES to [ɡ] between voiced sounds (intervocalic, post-nasal, post-ㄹ) — 고기 [koɡi]. RR onset ⟨g⟩. Fronts toward palatal before /i/. |
| /k͈/ | `ㄲ` | 까다 /k͈ada/ ('to peel'); 꼬리 /k͈oɾi/ ('tail') | Tense/fortis velar stop: unaspirated, glottally constricted (tense diacritic = U+0348), high onset pitch. Does NOT voice intervocalically (always voiceless). RR ⟨kk⟩. Contrasts with lax ㄱ /k/ and aspirated ㅋ /kʰ/. |
| /n/ | `ㄴ` | 나 /na/ ('I'); 누나 /nuna/ ('older sister') | Voiced alveolar nasal [n]; stable across vowels. In SOUTH Standard, word-initial ㄴ is dropped before /i j/ in Sino-Korean words by 두음법칙 (女 녀→여); NORTH 문화어 retains it (녀자). Adjacent to ㄹ it lateralizes to [l] (유음화). RR ⟨n⟩. |
| /t/ | `ㄷ` | 다 /ta/ ('all'); 다리 /taɾi/ → [taɾi] ('leg/bridge'), 어디 /ʌti/ → [ʌdi] ('where') | Lax alveolar stop. Voiceless lightly aspirated [t] word-initially; VOICES to [d] between voiced sounds — 어디 [ʌdi]. Before /i j/ across a morpheme boundary it PALATALIZES to [tɕ] (구개음화: 굳이 → [kudʑi]). RR onset ⟨d⟩. |
| /t͈/ | `ㄸ` | 따다 /t͈ada/ ('to pick'); 딸 /t͈al/ ('daughter') | Tense/fortis alveolar stop: unaspirated, glottally tense (U+0348), high onset pitch; never voices. RR ⟨tt⟩. Member of the triplet 달 /tal/ 'moon' ~ 딸 /t͈al/ 'daughter' ~ 탈 /tʰal/ 'mask'. |
| /l ~ ɾ/ | `ㄹ` | 라디오 /ɾadio/ ('radio', word-initial onset realized [ɾ] per the cells); 다리 /taɾi/ ('leg') with intervocalic [ɾ]; 물 /mul/ ('water') with coda [l] | Single liquid phoneme /l ~ ɾ/. As an intervocalic ONSET it is the alveolar TAP [ɾ] (다리 [taɾi]); in the CODA and in geminate ㄹㄹ it is the lateral [l] (물 [mul], 빨리 [p͈alli]). The bare word-initial onset cells above are realized as a tap [ɾ], chiefly in loanwords/foreign names (라디오), since native words rarely begin with ㄹ. SOUTH 두음법칙 changes word-initial ㄹ (Sino-Korean) to ㄴ or ∅ (勞→노, 理→이); NORTH 문화어 keeps initial ㄹ (로동, 리유). RR ⟨r⟩ as onset, ⟨l⟩ as coda. |
| /m/ | `ㅁ` | 마 /ma/ ('yam'); 머리 /mʌɾi/ ('head'); 무 /mu/ ('radish') | Voiced bilabial nasal [m]; stable across all vowels and positions, in both standards. RR ⟨m⟩. |
| /p/ | `ㅂ` | 바다 /pata/ → [pada] ('sea'); 바보 /papo/ → [pabo] ('fool') | Lax bilabial stop. Voiceless lightly aspirated [p] word-initially; VOICES to [b] between voiced sounds — 바보 [pabo]. RR onset ⟨b⟩. |
| /p͈/ | `ㅃ` | 빠르다 /p͈arɯda/ ('to be fast'); 뽀뽀 /p͈op͈o/ ('a kiss', baby-talk) | Tense/fortis bilabial stop: unaspirated, glottally tense (U+0348), high onset pitch; never voices. RR ⟨pp⟩. Contrasts with lax ㅂ /p/ and aspirated ㅍ /pʰ/. |
| /s/ | `ㅅ` | 사 /sa/ ('four'); 사람 /saɾam/ ('person'); 시 /ɕi/ ('poem/city/o'clock') | Lax alveolar sibilant [s]. Crucially, ㅅ → alveolo-palatal [ɕ] before /i/ and /j/: 시 = [ɕi], not [si]. Unlike the lax stops, /s/ does NOT voice intervocalically (stays voiceless [s]). Phonetically /s/ has a slightly tense/aspirated onset that distinguishes it from tense ㅆ /s͈/. RR ⟨s⟩. |
| /s͈/ | `ㅆ` | 싸다 /s͈ada/ ('cheap; to wrap'); 쓰다 /s͈ɯda/ ('to write/use'); 씨 /ɕ͈i/ ('seed; Mr./Ms.') | Tense/fortis sibilant [s͈] (U+0348), glottally constricted; the only fricative in the tense series, and the only place where Korean's three-way contrast is reduced to a two-way s/s͈ fricative contrast (no aspirated counterpart). Like ㅅ it becomes alveolo-palatal [ɕ͈] before /i j/: 씨 = [ɕ͈i]. Never voices. RR ⟨ss⟩. Contrast 살 /sal/ 'flesh' ~ 쌀 /s͈al/ 'uncooked rice'. |
| /∅/ (onset) · /ŋ/ (coda) | `ㅇ` | 아 /a/ ('ah'); 어 /ʌ/ ('uh'); 오 /o/ ('five'); 우유 /uju/ ('milk'); cf. coda 강 /kaŋ/ ('river') | ㅇ in the ONSET slot is SILENT — a graphic placeholder marking a vowel-initial syllable; it adds no consonant. The cells above are therefore bare vowels. ㅇ has the value /ŋ/ (velar nasal) ONLY in the coda (e.g. 강 [kaŋ]). Row included for inventory completeness and to document the onset/coda duality. No RR onset symbol (∅). |
| /tɕ/ | `ㅈ` | 자다 /tɕada/ ('to sleep'); 아주 /atɕu/ → [adʑu] ('very'); 자주 /tɕatɕu/ → [tɕadʑu] ('often') | Lax alveolo-palatal affricate [tɕ]. Voiceless lightly aspirated word-initially; VOICES to [dʑ] between voiced sounds — 아주 [adʑu]. RR onset ⟨j⟩. |
| /tɕ͈/ | `ㅉ` | 짜다 /tɕ͈ada/ ('to be salty; to weave'); 찌다 /tɕ͈ida/ ('to steam') | Tense/fortis affricate [tɕ͈] (U+0348), unaspirated and glottally tense, high onset pitch; never voices. RR ⟨jj⟩. Member of the triplet 자다 /tɕada/ 'sleep' ~ 짜다 /tɕ͈ada/ 'salty' ~ 차다 /tɕʰada/ 'cold'. |
| /tɕʰ/ | `ㅊ` | 차 /tɕʰa/ ('tea; car'); 차다 /tɕʰada/ ('to be cold; to kick') | Aspirated alveolo-palatal affricate [tɕʰ], strong aspiration, high onset pitch; never voices. RR ⟨ch⟩. The aspirated counterpart of lax ㅈ /tɕ/ and tense ㅉ /tɕ͈/. |
| /kʰ/ | `ㅋ` | 코 /kʰo/ ('nose'); 커피 /kʰʌpʰi/ ('coffee') | Aspirated velar stop [kʰ], strong aspiration, high onset pitch; never voices. RR ⟨k⟩. Also arises by 격음화 (aspiration) when ㄱ meets ㅎ across a boundary (좋고 → [tɕokʰo]). |
| /tʰ/ | `ㅌ` | 타다 /tʰada/ ('to ride; to burn'); 토 /tʰo/ ('vomit') | Aspirated alveolar stop [tʰ], strong aspiration, high onset pitch; never voices. RR ⟨t⟩. Before /i j/ across a morpheme boundary it PALATALIZES to [tɕʰ] (구개음화: 같이 → [katɕʰi]). Member of 달/딸/탈 triplet. |
| /pʰ/ | `ㅍ` | 파 /pʰa/ ('green onion'); 피 /pʰi/ ('blood'); 포도 /pʰodo/ ('grape') | Aspirated bilabial stop [pʰ], strong aspiration, high onset pitch; never voices. RR ⟨p⟩. The aspirated counterpart of lax ㅂ /p/ and tense ㅃ /p͈/. |
| /h/ | `ㅎ` | 하다 /hada/ ('to do'); 호수 /hosu/ ('lake'); 해 /hɛ/ ('sun') | Voiceless glottal fricative [h]. WEAKENS or DELETES between voiced sounds — intervocalically and after a nasal or ㄹ it is often [ɦ] or dropped entirely (전화 /tɕʌnhwa/ → [tɕʌnwa] 'telephone'). It also takes coarticulatory colorings: before /i j/ a palatal [ç] (히 [çi], robust and uncontroversial); before /ɯ/ a weak velar fricative [x~h] (흐), which is variable and far less consistent than the [ç] before /i/; before /u o/ rounded toward [ɸ~ʍ]. These colorings are allophonic, so the matrix keeps the phonemic /h/ in-cell (including 히 /hi/, 흐 /hɯ/) and describes them here. Combines with a following lax stop to yield aspiration (격음화: ㅎ+ㄱ → [kʰ]). RR ⟨h⟩. |

### Accent Notes

These notes apply across the matrix; they document the laryngeal contrast, the allophonic processes encoded only descriptively in the cells, and the principal South↔North (표준어 vs 문화어) differences.

#### Three-way laryngeal contrast

Korean's signature feature is a THREE-WAY contrast among voiceless obstruents at each place of articulation, with NO voicing contrast:

- **LAX/PLAIN (lenis)** ㄱ /k/, ㄷ /t/, ㅂ /p/, ㅈ /tɕ/ — slightly aspirated word-initially, low onset pitch, lax phonation.
- **TENSE/FORTIS** ㄲ /k͈/, ㄸ /t͈/, ㅃ /p͈/, ㅉ /tɕ͈/, ㅆ /s͈/ — unaspirated, glottally constricted/'stiff', high onset pitch (the tense diacritic here is `U+0348` COMBINING DOUBLE VERTICAL LINE BELOW).
- **ASPIRATED** ㅋ /kʰ/, ㅌ /tʰ/, ㅍ /pʰ/, ㅊ /tɕʰ/ — strongly aspirated, high onset pitch.

Minimal triplets: 달 /tal/ 'moon' ~ 딸 /t͈al/ 'daughter' ~ 탈 /tʰal/ 'mask'; 자다 /tɕada/ 'to sleep' ~ 짜다 /tɕ͈ada/ 'salty' ~ 차다 /tɕʰada/ 'cold'. In modern Seoul speech this contrast is partly shifting from VOT-based to PITCH-based (incipient tonogenesis): the onset's laryngeal class conditions the pitch of the following vowel (lax → low, tense/aspirated → high), so learners should attend to pitch as well as aspiration.

#### Lax intervocalic voicing

The LAX series ㄱ /k/, ㄷ /t/, ㅂ /p/, ㅈ /tɕ/ is voiceless [k t p tɕ] in absolute word-initial position (the environment the matrix cells represent), but VOICES to [ɡ d b dʑ] between voiced segments — typically intervocalically, and after a nasal or ㄹ within the voiced span. Thus 가구 /kaku/ 'furniture' surfaces [kaɡu], 고기 /koki/ 'meat' surfaces [koɡi], 바보 /papo/ 'fool' surfaces [pabo], 아주 /atɕu/ 'very' surfaces [adʑu]. (After an obstruent coda the regular rule is instead tensification, 경음화, not voicing.) This is ALLOPHONIC, not phonemic — Korean has no /ɡ d b dʑ/ phonemes — so the matrix keeps the voiceless phonemic forms and flags the voicing per row. The TENSE and ASPIRATED series do NOT voice intervocalically.

#### ㅅ-palatalization before /i/

ㅅ /s/ and ㅆ /s͈/ are realized as palato-alveolar/alveolo-palatal [ɕ] and [ɕ͈] before /i/ and the glide /j/: 시 is [ɕi] (not [si]), 시간 /sikan/ 'time' is [ɕiɡan]. The same fronting applies before the on-glide of ㅟ, so 쉬다 'to rest' is [ɕɥida~ɕwida]. Before all other vowels they remain [s]/[s͈]. This is captured in the ㅅ and ㅆ rows: the /i/ cells are shown with the [ɕ] realization noted (시 /ɕi/, 씨 /ɕ͈i/).

#### Silent ㅇ onset (이응)

The letter ㅇ (이응) is a SILENT placeholder when it occupies the onset (초성) slot — it carries no consonant value and the syllable is simply vowel-initial. ㅇ has a phonetic value /ŋ/ ONLY as a coda (종성), e.g. 강 /kaŋ/ 'river'. The ㅇ row in this matrix therefore lists bare vowels (아 /a/, 어 /ʌ/, 오 /o/ …); it is included for systematic completeness of the 19-letter inventory and to document the onset/coda duality, NOT because ㅇ adds a consonant onset.

#### South vs North: 두음법칙 (initial-sound rule)

The principal South↔North difference relevant to onsets is 두음법칙 (initial-sound rule):

- **SOUTH Standard applies it:** word-initial ㄹ → ㄴ → ∅, and ㄴ → ∅ before /i j/ (Sino-Korean 女子 → 여자 /jʌdʑa/ not 녀자; 勞動 → 노동 /nodoŋ/ not 로동; 理由 → 이유 /iju/ not 리유).
- **NORTH 문화어 does NOT apply it** and RETAINS the initial ㄹ/ㄴ (녀자, 로동, 리유).

The matrix shows the bare ㄹ /l~ɾ/ and ㄴ /n/ onsets, which occur freely word-initially in native and loan vocabulary in BOTH standards; the 두음법칙 restriction is specifically a Sino-Korean word-initial phenomenon. Other minor differences: North 문화어 vowels ㅓ/ㅗ are somewhat more rounded/backed, and North preserves a slightly more conservative consonant realization, but the 19-consonant / CV inventory of this matrix is shared.

#### No lexical stress, no lexical tone

Standard Korean has NO lexical stress and NO lexical tone — none of the CV syllables above carries inherent prominence. Prosody is organized into ACCENTUAL PHRASES (AP) with a phrase-level tune (commonly LHLH), and Seoul Korean is undergoing a tonogenetic shift in which the onset consonant's laryngeal class (see Three-way laryngeal contrast) conditions the pitch of the following vowel. Pitch-accent dialects that DO carry lexical pitch — Gyeongsang (동남) and Hamgyŏng (북동) — are outside this Standard reference.

#### Romanization in the cells

RR (Revised Romanization, official South Korea 2000) values are given per cell. Note RR onset spellings: the LAX series is written with voiced letters word-medially but the matrix uses the word-initial citation values (ㄱ=g, ㄷ=d, ㅂ=b, ㅈ=j); aspirated ㅋ=k, ㅌ=t, ㅍ=p, ㅊ=ch; tense ㄲ=kk, ㄸ=tt, ㅃ=pp, ㅉ=jj, ㅆ=ss; ㅅ=s, ㅎ=h, ㄴ=n, ㅁ=m, ㄹ=r, ㅇ-onset=∅. Vowels: ㅏ=a, ㅓ=eo, ㅗ=o, ㅜ=u, ㅡ=eu, ㅣ=i, ㅐ=ae. McCune–Reischauer differs (ㅓ=ŏ, ㅡ=ŭ, aspirates marked with an apostrophe k' t' p' ch').

---

*— Shin*

## Suprasegmentals

Prosodic and suprasegmental features of Modern Standard Korean (한국어), documented in parallel for two reference standards: Standard South Korean — 표준어 (*pyojun-eo*), educated Seoul speech — and North Korean — 문화어 (*munhwaeo*), the Pyongyang-based standard. The single most important fact about Korean suprasegmentals is NEGATIVE: Standard Korean has NEITHER lexical stress NOR lexical tone. No word is distinguished from another by which syllable is "stressed" (there are no stress minimal pairs as in English *record*/*record*, no *esdrújula*/*llana*/*aguda* contrasts as in Spanish *término*/*termino*/*terminó*), and no syllable carries a contrastive high/low/rising lexical pitch as in Mandarin, Japanese, or the Korean PITCH-ACCENT DIALECTS (Gyeongsang, Hamgyŏng). Instead, prosody is organized above the word: the basic unit is the ACCENTUAL PHRASE (강세구), which carries a phrase-level intonational TUNE (commonly described as LHLH); larger Intonation Phrases (억양구) end in pragmatically meaningful BOUNDARY TONES that distinguish statements, questions, commands, and continuation. Seoul Korean is additionally undergoing a TONOGENESIS-IN-PROGRESS in which the laryngeal class of the syllable onset (lax vs aspirated/tense) conditions the F0 (pitch) of the following vowel — a pitch cue that is increasingly replacing the older VOT (Voice Onset Time) cue for the three-way stop contrast. Phonemic VOWEL LENGTH existed in older/prescriptive Standard but is largely lost in modern Seoul speech. These properties make Korean prosody fundamentally a PHRASE-LEVEL, intonational system rather than a word-level stress or tone system.

### No Lexical Stress or Tone

Standard Korean (both 표준어 and 문화어) has NO phonemic word stress and NO phonemic word tone. This is the defining suprasegmental property and must be stated before anything else. A Korean word does not have a fixed, contrastive "accented" syllable; native speakers do not agree on, and do not need, a notion of which syllable of a polysyllabic word is "stressed", because nothing in the lexicon depends on it.

#### No Lexical Stress

There is no contrastive lexical stress. Unlike English (`ˈrecord` noun vs `reˈcord` verb) or Spanish (*público* / *publico* / *publicó*), Korean has no minimal pairs distinguished by stress placement, and dictionaries do not mark stress. Any perceived prominence is a property of the ACCENTUAL PHRASE and its intonational tune, not of the word.

**Contrast with English and Spanish:** Both English and Spanish are stress-accent languages with phonemic lexical stress; Korean is not. Where English realizes prominence through stress (duration + pitch + loudness + full vowel quality) and reduces unstressed vowels to schwa, and Spanish realizes it through duration + pitch with NO vowel reduction, Korean realizes phrase-edge prominence purely through the AP tune and shows NO English-style vowel reduction to schwa (every vowel keeps its full quality regardless of position — in this it patterns with Spanish, not English).

#### No Lexical Tone

There is no contrastive lexical tone in Standard Korean. A given syllable does not carry an inherent high, low, rising, or falling pitch that distinguishes meaning. Pitch in Standard Korean is entirely post-lexical (assigned by the phrase-level intonation system), not lexical.

**Exceptions pointer:** Two regional varieties DO retain lexical pitch and are the genuine exceptions: Gyeongsang (동남 / South-East) and Hamgyŏng (북동 / North-East). These are documented separately under [Pitch-Accent Dialects](#pitch-accent-dialects) and are NOT part of the Seoul/Pyongyang reference standards.

**Historical note:** Middle Korean (15th c.) DID have a lexical pitch-accent / tone system, marked in early Hangul texts with side dots (방점 *bangjeom*): one dot = 거성 (high / 去聲), two dots = 상성 (rising / 上聲), no dot = 평성 (low / 平聲). This system was lost in the central dialect by roughly the 16th–17th centuries, surviving only in the peripheral pitch-accent dialects above. Modern Standard Korean is therefore a language that HAS LOST its earlier tone.

#### What Carries Prominence Instead

Because the word level is prosodically "flat", prominence and meaning-bearing pitch live at the PHRASE level: (1) the Accentual Phrase imposes a fixed melodic template (the LHLH tune) over each phrase regardless of word content; (2) the Intonation Phrase ends in a boundary tone that signals sentence type and attitude. This is why learners must stop hunting for a "stressed syllable" and instead learn the phrasing-and-melody system.

### Accentual Phrase

The ACCENTUAL PHRASE (AP; 강세구 *gangse-gu*, also 음운구 / phonological phrase) is the basic prosodic constituent of Standard Korean above the word. It is the domain over which a single, largely FIXED intonational TUNE is laid down. An AP typically consists of a content word plus its following grammatical particles/endings (e.g., a noun + case particle, or a verb stem + ending), and is the unit within which the connected-speech sandhi rules (liaison 연음, tensification 경음화, etc.) most regularly apply. Several APs group into a larger Intonation Phrase (억양구 *eogyang-gu*).

#### The LHLH Tune

The canonical Seoul AP melody is a four-tone template, conventionally written LHLH (Low–High–Low–High): the phrase RISES into a peak early, dips, and rises again toward the phrase edge. The two L's and two H's dock to the EDGES of the AP, not to any "stressed" syllable — there is no stressed syllable to dock to. The first H usually lands on the second syllable of the AP, and the final H on the AP-final syllable.

**Schematic:** `[ L  H  ( … )  L  H ]` — initial rise (LH) on the first two syllables, a dip, then a final rise (LH) to the AP-final syllable. In a long AP the middle is interpolated between the two LH "pillars".

**Tone-to-syllable mapping:**

| Position | Tone | Detail |
|---|---|---|
| Syllable 1 (AP-initial) | L (low) | UNLESS the onset is aspirated or tense, in which case it surfaces as H (see [Tonogenesis in Progress](#tonogenesis-in-progress), the laryngeally-conditioned high-onset variant HHLH). |
| Syllable 2 | H | the early peak. |
| Medial syllables | (interpolated) | pitch interpolates / declines toward the phrase-medial L. |
| Final syllable (AP-final) | H | the phrase-final rise that delimits the AP edge. |

**Laryngeal variant:** When the AP-initial onset is a TENSE or ASPIRATED consonant (or /s/, /h/), the initial tone is realized HIGH rather than low, giving a HHLH pattern instead of LHLH. When the onset is a LAX (plain) consonant or a sonorant/vowel, the canonical LHLH (low onset) appears. This onset-conditioned choice between a low-onset and high-onset AP tune is exactly the locus of the ongoing tonogenesis (see below).

**IPA / K-ToBI notation:** AP-level pitch targets are commonly annotated in the autosegmental-metrical K-ToBI (Korean ToBI) framework: tonal targets La / Ha (accentual-phrase initial Low/High) and L / H within the AP; phrase-final and IP-final tones use the boundary-tone marks. In running IPA, global pitch rises/falls may be shown with ↗ (rise) and ↘ (fall); AP boundaries with a minor break `|` and IP boundaries with a major break `‖`. Downstep/upstep across APs: `ꜜ`/`↓` and `↑`.

#### Phrasing

How an utterance is divided into APs (and APs into IPs) is itself meaningful. Phrasing groups words that "belong together" and signals syntactic structure. A single string of words can be re-phrased to change which constituents cohere, and faster/more casual speech tends to pack more words into fewer, longer APs (dephrasing), while careful/emphatic speech splits into more, shorter APs.

**Example:**

| Field | Value |
|---|---|
| Utterance | 동생이 새 자전거를 샀어요. |
| IPA | /toŋsɛŋi sɛ tɕadʑʌŋɡʌɾɯl sas͈ʌjo/ |
| Gloss | "(My) younger sibling bought a new bicycle." |

*Phrasing note:* A neutral rendition forms APs roughly as [동생이] [새 자전거를] [샀어요], each carrying its own LHLH tune; the final IP boundary tone on -요 sets the sentence type (here a falling L% for a plain declarative). Emphatic narrow focus on "새" (new) would split it into its own AP and expand its pitch range.

#### Accent Difference

| Standard | Accentual-phrase behavior |
|---|---|
| South 표준어 | The LHLH accentual-phrase model and the K-ToBI framework are based primarily on Seoul 표준어 data. Seoul speech is the locus of the tonogenetic shift (onset-laryngeal class strongly conditions the initial AP tone, and for many younger speakers pitch has overtaken VOT as the primary cue to the lax–aspirated contrast). |
| North 문화어 | Pyongyang 문화어 is also a non-tonal, non-stress system organized in accentual phrases with phrase-level intonation. Descriptions report somewhat different phrase-melody DETAILS and overall intonational "colour" from Seoul (popularly perceived by Southerners as more "sing-song" or sharply rising), and a more conservative consonant system; munhwaeo is less studied in the K-ToBI tradition, so fine-grained AP-tone claims are weaker than for Seoul. |

**Note:** Both standards share the fundamental architecture — no lexical stress/tone, prosody organized in accentual phrases with a phrase tune plus IP boundary tones. The differences are in melodic detail and in how far the Seoul tonogenetic reanalysis has progressed (a Seoul-centred, in-progress change).

### Tonogenesis in Progress

Seoul Korean is undergoing a well-documented sound change often called TONOGENESIS (the birth of tone-like pitch distinctions): the three-way laryngeal contrast of the lax (plain) vs tense vs aspirated stops is being re-cued from a CONSONANT property (VOT, Voice Onset Time) to a PITCH property (the F0 of the following vowel). This is NOT yet lexical tone — pitch is still assigned at the accentual-phrase level — but it is the mechanism by which the AP-initial tone (Low vs High) has become predictable from the onset's laryngeal class, and by which the historical stop contrast is increasingly carried by pitch.

#### The VOT-to-F0 Shift

**Older system:** In the traditional/older Seoul system, the lax–aspirated contrast was cued mainly by VOT: aspirated stops had a long VOT (a long voicing lag with the [ʰ] puff), lax stops a short-to-intermediate VOT, and tense stops a very short VOT with stiff/tense phonation. The pitch of the following vowel was secondary.

**Innovating system:** In the speech of younger Seoul speakers (a change led especially since the late 20th century, and reportedly led by women), the VOT of lax and aspirated stops has MERGED (both now have a relatively long voicing lag), so VOT no longer reliably separates them. The distinction has been RESCUED by F0: the vowel after a LAX onset begins with LOW pitch, while the vowel after an ASPIRATED (and TENSE) onset begins with HIGH pitch. Pitch has thus become the PRIMARY cue to a contrast that used to be primarily about aspiration timing.

**Cue summary:**

| Onset class | Following-vowel F0 | Example |
|---|---|---|
| Lax / plain (ㄱ /k/, ㄷ /t/, ㅂ /p/, ㅈ /tɕ/, and /s/) | LOW onset pitch → AP begins Low (canonical L…) | 갈 /kal/ ("to go", adnominal) — low-onset, e.g. AP tune L H … |
| Aspirated (ㅋ /kʰ/, ㅌ /tʰ/, ㅍ /pʰ/, ㅊ /tɕʰ/, and ㅎ /h/) | HIGH onset pitch → AP begins High (H…) | 칼 /kʰal/ ("knife") — high-onset, e.g. AP tune H H … |
| Tense / fortis (ㄲ /k͈/, ㄸ /t͈/, ㅃ /p͈/, ㅉ /tɕ͈/, ㅆ /s͈/) | HIGH onset pitch (patterns with aspirated for the pitch cue), with additionally tense/constricted phonation and very short VOT | 깔 /k͈al/ ("to spread out", stem 깔다) — high-onset, e.g. AP tune H H … |

#### Minimal Triplet Illustration

The classic Seoul laryngeal triplet, which used to be distinguished by VOT alone, is increasingly distinguished by the PITCH of the following vowel for younger speakers. The three words are segmentally /kal/ except for the onset's laryngeal class.

| Word | IPA | Onset | F0 cue | Gloss |
|---|---|---|---|---|
| 갈 | /kal/ | lax `ㄱ` | LOW following-vowel pitch | adnominal of 가다 "to go" (e.g. 갈 사람 "the person who will go") |
| 칼 | /kʰal/ | aspirated `ㅋ` | HIGH following-vowel pitch | "knife" |
| 깔 | /k͈al/ | tense `ㄲ` | HIGH following-vowel pitch + tense phonation | stem of 깔다 "to spread/lay out" |

**Note:** Lax vs (aspirated/tense) is now primarily a LOW vs HIGH pitch contrast on the following vowel for many Seoul speakers; aspirated vs tense are still separated by phonation/VOT and tenseness, not by this pitch cue (both are high).

#### Status and Scope

**Is it tone yet?** No — this is best described as INCIPIENT or near-tone. The pitch difference is still predictable from the onset consonant (it is post-lexical, allophonic-at-the-phrase-level), not stored independently in the lexicon. It does not (yet) create tonal minimal pairs that are independent of the onset. But because it has reorganized the AP-initial tone around onset laryngeal class, it is the leading edge of a possible drift toward a tonal system, and is one of the most-studied live sound changes in any language.

**Interaction with the AP tune:** This is precisely why the AP tune appears as LHLH after a lax/sonorant onset but as HHLH (high onset) after an aspirated/tense onset (see [The LHLH Tune → Laryngeal variant](#the-lhlh-tune)): the onset's laryngeal class chooses the initial tone of the phrase.

**Accent difference:**

| Standard | Tonogenesis status |
|---|---|
| South 표준어 | The tonogenetic VOT→F0 shift is a SEOUL phenomenon and is advanced among younger speakers; it is the reference case in the literature. |
| North 문화어 | Pyongyang 문화어 is reported to be more CONSERVATIVE and to maintain a clearer VOT-based three-way distinction (the merger of lax/aspirated VOT characteristic of innovating Seoul speech is not described to the same degree for the North); North Korean phonetics is less studied, so this is a tentative contrast. |

**Note:** Older Seoul speakers and conservative styles still rely more on VOT; the F0 cue and the lax/aspirated VOT merger are generation-graded, led by younger and female Seoul speakers.

### Intonation

Intonation is the linguistically structured use of pitch (F0) over the Intonation Phrase (억양구 *eogyang-gu*), the largest prosodic unit, composed of one or more accentual phrases. Because Standard Korean lacks lexical tone and stress, intonation carries an unusually heavy functional load: the IP-final BOUNDARY TONE (경계 성조) is a primary signal of SENTENCE TYPE (declarative, yes/no question, wh-question, command, request, continuation) and of speaker attitude. In the K-ToBI framework these are notated as IP-final boundary tones (e.g., L%, H%, LH%, HL%, LHL%), docked to the final syllable of the phrase — typically the syllable bearing the sentence-final ending (종결어미). Korean is thus a language where "the ending plus its melody" does much of the work that word order and auxiliaries do in English.

#### Structure

The INTONATION PHRASE is the domain of one complete intonation contour, bounded by perceptible breaks and ending in a boundary tone; it contains one or more accentual phrases, each with its own LHLH-type tune, plus an overall declination (gradual pitch lowering) across the IP.

**Components:**

| Component | Description |
|---|---|
| Accentual phrases (강세구) | each with its internal LHLH (or HHLH) tune; multiple APs may chain within one IP |
| Declination | a gradual lowering of overall pitch register across the IP from start to finish |
| Nuclear region | the final AP of the IP, where the meaning-bearing pitch movement concentrates |
| IP-final boundary tone (경계 성조 / boundary tone) | the obligatory final pitch target on the very last syllable (usually the sentence-final ending), which sets sentence type and attitude |

**IPA / K-ToBI notation:** K-ToBI boundary tones are written with `%`: L% (low fall), H% (high rise), LH% (low-rise), HL% (high-low fall), LHL% (rise-fall), HLH% / LHLH% (complex). In plain IPA: ↗ global rise, ↘ global fall, → level/sustained; AP break `|`, IP break `‖`; downstep `ꜜ`/`↓` between APs.

#### Intonation Patterns

| Type | Contour | Boundary tone | Symbol | Description |
|---|---|---|---|---|
| Declarative / statement — 평서문 (*pyeongseomun*) | Final FALL | L% (low boundary tone) | ↘ | A neutral statement ends LOW: each AP carries its LHLH tune, overall declination lowers the register, and the final ending falls to a low boundary tone, conveying finality and completeness. Polite declaratives in -아요/어요 (*-ayo/-eoyo*) and formal -습니다 (*-seumnida*) characteristically fall. |
| Yes/No (polar) question — 판정 의문문 (*panjeong uimunmun*) | Final RISE | H% (high boundary tone) | ↗ | A yes/no question ends with a clear RISE to a high boundary tone. Crucially, Korean polar questions frequently share the SAME segmental form and word order as the corresponding statement — both can end in -아요/어요 (*-ayo/-eoyo*) — so the RISING intonation alone is often what marks the utterance as a question. This is the canonical Korean statement-vs-question intonational minimal contrast (parallel to Spanish ¿María come manzanas? vs María come manzanas.). |
| Wh- (content) question — 설명 의문문 (*seolmyeong uimunmun*) | Often a FALL (or low/mid), with prominence on the wh-word | L% (low) is common, though a rise (H%) is also possible | ↘ (with a pitch peak on the interrogative word) | Content questions contain an interrogative word (누구 "who", 뭐/무엇 "what", 언제 "when", 어디 "where", 왜 "why", 어떻게 "how"), which typically carries a pitch peak. Because the wh-word already marks the utterance as a question, the IP often ENDS in a FALL (L%), like a statement, rather than the polar rise. Notably, the SAME string (e.g., 뭐 먹어요?) can be a wh-question ("What are you eating?") with a fall, or — read with a rise — a yes/no question treating 뭐 as "something" ("Are you eating something?"); intonation disambiguates the two readings. |
| Imperative / command — 명령문 (*myeongnyeongmun*) | Falling (firm) to falling-with-care | L% (often), with reduced final rise | ↘ | Commands (typically in -아/어 (*-a/-eo*), -세요 (*-seyo*) polite, or -어라 (*-eora*) plain) generally take a falling or low-ending contour conveying directive force; politer requests soften the fall and may add a slight final rise. |
| Propositive / suggestion — 청유문 (*cheongyumun*) | Falling or gently rising | L% or LH% | ↘ / ↗ | Suggestions ("let's…", typically -아요/어요 or plain -자 *-ja*) carry a falling-to-mildly-rising contour inviting agreement. |
| Continuation / non-final (listing, conjoined/subordinate clause) | Sustained or rising (non-final, "more to come") | H% or LH% (continuation rise); items before the last in a list rise/sustain | → / ↗ | A non-final IP — an item before the last in a list, or a clause ending in a connective ending such as -고 (*-go* "and"), -아서/어서 (*-aseo/-eoseo* "so/and then"), -지만 (*-jiman* "but") — ends on a sustained or rising tone projecting continuation; the final clause then takes the appropriate terminal contour (a fall for a closed declarative list). |
| Exclamative / emphatic — 감탄문 (*gamtanmun*) | Expanded pitch range, often rise-fall | HL% or LHL% with a widened, raised peak | ↗↘ | Exclamations (often in -군요 / -네요 (*-gunyo / -neyo*)) widen the pitch range and raise the peak, conveying strong feeling — surprise, admiration. Functionally parallel to the English/Spanish rise-fall of heightened involvement. |

**Examples by pattern:**

| Type | Sentence | IPA | Gloss |
|---|---|---|---|
| Declarative | 학생이에요. | /haks͈ɛŋiejo↘/ | "(I/he/she) am/is a student." Final -요 falls to L% (a plain, complete declarative). |
| Yes/No question | 학생이에요? | /haks͈ɛŋiejo↗/ | "Are (you) a student?" Same segments as the statement above; the final rise to H% on -요 does the questioning. |
| Wh- question | 뭐 먹어요? | /mwʌ mʌɡʌjo↘/ | "What are you eating?" (wh-reading): pitch peak on 뭐, falling L% on -요. With a final rise (↗) the same string reads "Are you eating something?" (yes/no). |
| Imperative | 여기 앉으세요. | /jʌɡi an.dʑɯsejo↘/ | "Please sit here." (polite command/request) — -세요 ends low/falling with politeness. |
| Propositive | 같이 가요. | /katɕʰi kajo/ | "Let's go together." (propositive) — context and a gently rising-then-settling tune mark the invitation; the same -아요/어요 string can also be statement, question, or command depending on the boundary tone. |
| Continuation | 사과하고, 배하고, 포도를 샀어요. | /saɡwahaɡo↗ pɛhaɡo↗ pʰodoɾɯl sas͈ʌjo↘/ | "I bought apples, pears, and grapes." — non-final items 사과하고/배하고 rise/sustain; the final 샀어요 falls to L%. |
| Exclamative | 정말 예쁘네요! | /tɕʌŋmal jep͈ɯneːjo/ | "(It's/you're) really pretty!" — expanded high peak with a final rise-fall expressing admiration. |

#### Boundary-Tone Functional Load

Because Korean sentence-final endings (종결어미) are often ambiguous as to sentence type in the speech levels that share an ending across functions — most famously the polite 해요체 (*haeyo-che*) ending -아요/어요, which serves as statement, question, command, AND suggestion — the IP-FINAL BOUNDARY TONE is frequently the SOLE disambiguator. This is a far heavier grammatical role for intonation than in English (which has do-support and subject-auxiliary inversion) and a heavier role than Spanish, making boundary-tone mastery essential for Korean learners.

**해요체 (*haeyo-che*) example** — identical segments 집에 가요 /tɕibe kajo/; only the boundary tone (and pragmatic context) distinguishes the four sentence types:

| Reading | Tone | Meaning |
|---|---|---|
| statement | L% (fall ↘) | "(I) am going home." |
| yes/no question | H% (rise ↗) | "Are (you) going home?" |
| command | L% / short fall ↘ (directive) | "Go home." |
| suggestion / propositive | LH% (gentle rise) | "Let's go home." |

#### Focus

FOCUS / new information is marked prosodically by EXPANDING the pitch range of (and often starting a new AP at) the focused constituent, and by DEPHRASING/compressing the post-focal material (post-focal pitch range is reduced and following APs may lose their own peaks). Because there is no lexical stress to relocate, Korean uses AP boundary placement and pitch-range expansion — together with morphological focus particles such as -은/는 (topic) and -이/가 (which can mark focus) and flexible word order (scrambling) — rather than moving a "nucleus" the way English does.

| Focus | Realization |
|---|---|
| Neutral (broad focus) | 동생이 사과를 먹었어요. /toŋsɛŋi saɡwaɾɯl mʌɡʌs͈ʌjo↘/ — "My sibling ate an apple." |
| Focused object | 동생이 [사과]를 먹었어요. — narrow focus on 사과 "apple" (not something else): 사과 starts its own pitch-expanded AP and the following material is compressed. |
| Focused subject | [동생]이 사과를 먹었어요. — narrow focus on 동생 "sibling" (it was my SIBLING who ate it): pitch range expands on 동생, post-focal material dephrased. |

#### Functions Overview

| Function | Role of intonation |
|---|---|
| Grammatical | Carries a very heavy load: distinguishes sentence types — declarative (L%) vs yes/no question (H%) vs wh-question (often L%) vs command vs suggestion — frequently when the segmental form is IDENTICAL (esp. 해요체 -아요/어요); marks clause/phrase boundaries; signals continuation vs completion. |
| Focus and information | Pitch-range expansion on the focused constituent plus post-focal compression/dephrasing marks new information / contrast; works together with topic/subject particles and scrambling. |
| Attitudinal | Pitch range and contour shape convey politeness, surprise, doubt, irritation, affection, sarcasm; raising the final rise or widening the range softens or intensifies. |
| Discourse | Manages turn-taking and topic structure via AP/IP phrasing, declination resets, and boundary tones. |

#### Accent Difference

| Standard | Intonation behavior |
|---|---|
| South 표준어 | Seoul 표준어 declaratives fall (L%), polar questions rise (H%), wh-questions commonly fall; the K-ToBI boundary-tone inventory (L%, H%, LH%, HL%, LHL% …) is built on Seoul data. A high-rising tendency on declaratives in some younger casual speech parallels English "uptalk". |
| North 문화어 | Pyongyang 문화어 shares the same architecture (boundary tones distinguishing sentence type) but is popularly and descriptively reported to have a more sharply rising, "sing-song" melodic character and somewhat different final-contour shapes; it is less studied in the K-ToBI tradition, so detailed boundary-tone claims are more tentative for the North. |

**Note:** The fundamental inventory — declarative fall (L%), polar-question rise (H%), wh-question fall, continuation rise — is shared by both standards; the differences are in melodic detail, pitch range, and overall intonational "colour".

### Rhythm

Korean rhythm is most often described as SYLLABLE-TIMED-ish (close to syllable-timing) rather than stress-timed: there is no stress-driven compression of "unstressed" syllables, and — critically — NO vowel reduction to schwa (every syllable keeps a full vowel), so syllables tend toward comparable duration and an utterance's length scales with its syllable count. In this Korean patterns WITH Spanish and AGAINST stress-timed English. The label must be applied carefully, however: Korean is sometimes described as having a MORA-like or "phrase-timed" tendency, and rhythm-metric studies place it in an intermediate/ambiguous zone, partly because of systematic durational effects (phrase-final lengthening, the long-vowel residue, and consonant-cluster/coda effects) that break strict syllable isochrony.

#### Timing Unit

The SYLLABLE (음절) is the most natural rhythmic unit, reinforced by the writing system: Hangul composes one spoken syllable into one square block, so Korean speakers have strong syllable awareness. Each (C)(G)V(C) syllable tends to be allotted roughly comparable time, and unstressed-position syllables are NOT compressed or reduced the way English ones are.

**Example:**

| Field | Value |
|---|---|
| Utterance | 어머니가 시장에 가셨어요. |
| IPA | /ʌmʌniɡa ɕidʑaŋe kaɕjʌs͈ʌjo/ |
| Gloss | "Mother went to the market." |

*Note:* Each syllable (어-머-니-가 / 시-장-에 / 가-셨-어-요) receives comparable timing; unstressed syllables keep full vowel quality (no schwa), so the line is evenly paced rather than "galloping" like English.

**IPA notation:** Syllable boundaries may be marked with the period `.` in narrow transcription; phrase-final lengthening with the length mark `ː` or half-long `ˑ` on the final rhyme.

#### No Vowel Reduction

A key rhythmic property shared with Spanish and opposed to English: Korean does NOT reduce unstressed vowels to a centralized schwa. The 8 monophthongs keep their full peripheral quality in every position:

| Jamo | IPA | Note |
|---|---|---|
| `ㅏ` | /a/ | full open vowel |
| `ㅓ` | /ʌ/ | full open-mid back unrounded |
| `ㅗ` | /o/ | full mid back rounded |
| `ㅜ` | /u/ | full close back rounded |
| `ㅡ` | /ɯ/ | FULL high back UNROUNDED vowel, NOT a reduced schwa — learners must not collapse it to /ə/ |
| `ㅣ` | /i/ | full close front |
| `ㅐ` | /ɛ/ | full open-mid front |
| `ㅔ` | /e/ | full close-mid front |

This full-vowel property is the segmental complement of the syllable-timed tendency.

**Contrast:** English "banana" = [bəˈnænə] with two schwas; a Korean word of comparable shape keeps full vowels in every syllable. Do not import English vowel reduction into Korean.

#### Phrase-Final Lengthening

The clearest systematic timing effect: the FINAL syllable of an accentual phrase / intonation phrase is LENGTHENED. This boundary-marking lengthening (rather than stress) is a major durational cue in Korean and is one reason strict syllable isochrony does not hold. It cooperates with the AP-final H tone to delimit phrase edges.

**Example:** In an AP-final position the rhyme is audibly drawn out (e.g., the final syllable before a phrase break carries both the AP-final H and extra duration), whereas the same syllable phrase-medially is shorter.

#### Isochrony

As with the stress-/syllable-timing debate generally, strict acoustic isochrony is not perfectly supported for Korean by measurement. Rhythm-metric studies (e.g., %V, ΔC, nPVI measures) place Korean in an INTERMEDIATE region, closer to syllable-timed than to stress-timed but not as cleanly syllable-timed as Spanish, owing to phrase-final lengthening, the residual long/short vowel distinction in conservative speech, and complex coda/cluster timing. The honest description is: "syllable-timed-tending, with strong phrase-edge (final-lengthening) effects", NOT stress-timed.

**Consequence:** Because syllables are not compressed between "stresses" (there are none) and vowels are not reduced, adding syllables lengthens the utterance proportionally; the salient durational landmarks are PHRASE EDGES (final lengthening), not stress beats.

#### Accent Difference

| Standard | Rhythmic type |
|---|---|
| South 표준어 | Seoul 표준어 is syllable-timed-tending with robust accentual-phrase-final and IP-final lengthening; no vowel reduction. |
| North 문화어 | Pyongyang 문화어 is likewise non-stress-timed and free of vowel reduction; differences from Seoul are matters of melodic colour and tempo rather than rhythmic class. |

**Note:** Both standards share the syllable-timed-tending, reduction-free rhythmic type, contrasting with stress-timed English. The key instruction for English-speaking learners: do NOT reduce vowels to schwa and do NOT impose a stress beat — give each syllable a full vowel and comparable time, and lengthen phrase-finally.

### Vowel Length

Standard Korean had a PHONEMIC LONG/SHORT VOWEL distinction in older/prescriptive descriptions, but it is LARGELY LOST in modern Seoul speech and is not reliably produced or perceived by younger speakers. It is therefore a prescriptive/older-Standard feature that the guide notes for completeness rather than a living contrast of modern Seoul Korean.

#### Historical / Prescriptive Status

Conservative/prescriptive Standard Korean recognized contrastive vowel LENGTH, found chiefly on word-INITIAL syllables (length was neutralized in non-initial position). It produced a number of classic minimal pairs distinguished by long [Vː] vs short [V] alone. The Standard Pronunciation rules (표준 발음법) historically described this distinction, and conservative dictionaries marked long vowels.

**Minimal pairs (short vs long):**

| Spelling | Short | Long | Note |
|---|---|---|---|
| 눈 | 눈 /nun/ "eye" | 눈 /nuːn/ "snow" | homographic in Hangul; distinguished in conservative speech only by vowel length (short = eye, long = snow). |
| 밤 | 밤 /pam/ "night" | 밤 /paːm/ "chestnut" | short = night, long = chestnut. |
| 말 | 말 /mal/ "horse" | 말 /maːl/ "speech/words/language" | short = horse, long = words/speech. |
| 벌 | 벌 /pʌl/ "punishment" | 벌 /pʌːl/ "bee" | short = punishment, long = bee. |

#### Loss in Modern Seoul

In present-day Seoul speech the length contrast has been almost entirely NEUTRALIZED: most speakers — especially those born after roughly the mid-20th century — do not maintain a consistent long/short difference, and the pairs above are now homophones distinguished only by context. Vowel duration in modern Seoul is governed by post-lexical, allophonic factors (notably phrase-final lengthening; see [Rhythm](#rhythm)) rather than by a lexical length feature. Length is therefore best described as a MARGINAL/MORIBUND feature of the modern spoken standard, retained mainly in careful, formal, broadcast, or older speech and in prescriptive norms.

**IPA notation:** Where length is shown at all (conservative transcription), the length mark `ː` follows the long vowel (e.g., 눈 "snow" /nuːn/). Modern Seoul transcriptions typically omit it because the contrast is not maintained.

**Compensatory note:** Some of the former length distinctions partly correlate with the tonogenetic pitch system and with vowel quality in conservative speech, but for practical modern Seoul Korean the long/short contrast can be treated as effectively absent.

#### Accent Difference

| Standard | Vowel-length status |
|---|---|
| South 표준어 | Prescriptive 표준어 historically recognized contrastive length (word-initial), but it is largely lost in actual modern Seoul speech, especially among younger speakers. |
| North 문화어 | North Korean 문화어 is generally described as MORE CONSERVATIVE in retaining phonemic vowel length than Seoul speech; the long/short distinction is reported to be better preserved in the Northern standard's prescriptive norms. |

**Note:** Net guidance: treat vowel length as a historical/prescriptive feature — present in older and Northern norms, largely lost in modern Seoul. Learners of the modern Seoul standard need not produce it to be intelligible, but should be aware of the classic minimal pairs (눈/눈, 말/말) that depended on it.

### Pitch-Accent Dialects

While Standard Korean (Seoul 표준어 and Pyongyang 문화어) is non-tonal and non-stress, TWO peripheral dialect regions DO retain a LEXICAL PITCH-ACCENT system — a genuine word-level pitch contrast inherited from Middle Korean and lost in the central dialect. These are documented here as ASIDES (they are NOT the reference standards), because they are the real counterexamples to the "Korean has no lexical pitch" statement: in these dialects, pitch placement IS contrastive and can form minimal pairs. Their existence is itself evidence that Standard Korean's flatness is an innovation (loss), not an original state.

#### Gyeongsang — 경상도 방언 (동남 방언, South-East)

**Region:** Southeastern South Korea (the Yeongnam area: Busan 부산, Daegu 대구, Ulsan, North/South Gyeongsang provinces).

**System:** A LEXICAL PITCH-ACCENT system: each word has a fixed pitch melody (e.g., High–Low, Low–High, High–High patterns over the first syllables), and the LOCATION/shape of the High is contrastive. Speakers maintain word-level pitch that Seoul speakers lack, which is the salient feature non-Gyeongsang Koreans notice (it sounds "tonal" or "sing-song" to Seoulites).

**Contrastive example — 가가:** A famous Gyeongsang showcase: the string 가가 (and longer chains like 가가가가) can mean different things distinguished by pitch — e.g., "that kid?", "is it that kid?", "take it", depending on the pitch pattern. The exact glosses vary by source, but the point is that PITCH alone disambiguates segmentally identical strings, which is impossible in Standard Seoul Korean.

**Minimal-pair example — 손 /son/:**

| Pitch | Item |
|---|---|
| 손 (High) | one lexical item |
| 손 (Low) | a different lexical item |

*Note:* Gyeongsang distinguishes pairs such as 손 "hand" vs 손 "guest/손님-type" (and similar 2-tone pairs) by pitch where Seoul has no pitch contrast; specific pairs and their tones vary by sub-dialect (Daegu vs Busan differ).

#### Hamgyŏng — 함경도 방언 (북동 방언, North-East)

**Region:** Northeastern North Korea (Hamgyŏng/함경 provinces) and emigrant Korean (Koryo-saram / 육진 Yukchin-related) communities; also the related Yukchin dialect of the far northeast.

**System:** Also a LEXICAL PITCH-ACCENT dialect, the other major variety that preserves Middle-Korean-derived contrastive pitch. Like Gyeongsang it maintains a word-level High/Low accent contrast absent from the standards. It is less accessible/less studied than Gyeongsang owing to its location in North Korea and the diaspora, but is consistently cited as the second pitch-accent area.

**Note:** Hamgyŏng pitch is structurally parallel to Gyeongsang (a register/locus pitch-accent system) and is the northern member of the two surviving pitch-accent zones; details differ in the alignment and number of contrasting melodies.

#### Relation to Standard

These pitch-accent systems are RELICS of the Middle Korean tone/pitch-accent system (cf. the 방점 side-dot notation noted under [No Lexical Tone → Historical note](#no-lexical-tone)) that the central Seoul dialect lost. They confirm that Standard Korean's lack of lexical pitch is a HISTORICAL LOSS, and they are the principled exceptions to every "no lexical tone" statement in this guide. For the Korean Peshitta's reference pronunciations, the STANDARD (Seoul 표준어, with North 문화어 in parallel) non-tonal system is used; Gyeongsang and Hamgyŏng pitch are descriptive asides only.

**IPA notation:** Dialectal lexical pitch is typically shown with the IPA tone diacritics — high `◌́` and low `◌̀` over the vowel (e.g., a High-initial syllable á vs a Low syllable à) — or with H/L tone-letter sequences over the word; this contrasts with the post-lexical, phrase-level ↗/↘ marks used for Standard Korean intonation.

### Cross-References

| Topic | Reference |
|---|---|
| Consonants — laryngeal contrast | The Tonogenesis subsection depends on the three-way laryngeal stop contrast (lax ㄱㄷㅂㅈ /k t p tɕ/, tense ㄲㄸㅃㅉㅆ /k͈ t͈ p͈ tɕ͈ s͈/, aspirated ㅋㅌㅍㅊ /kʰ tʰ pʰ tɕʰ/); see the consonants section for the VOT/phonation details that pitch is replacing. |
| Vowels | The Rhythm and Vowel Length subsections reference the 8-monophthong system (ㅏ /a/, ㅓ /ʌ/, ㅗ /o/, ㅜ /u/, ㅡ /ɯ/, ㅣ /i/, ㅐ /ɛ/, ㅔ /e/, with the 애/에 merger); note especially that ㅡ /ɯ/ is a FULL vowel, not a schwa. |
| Syllable structure | Rhythm and phrase-final lengthening operate over (C)(G)V(C) syllables and the 7-sound coda (받침) neutralization; see the syllable_structure section. |
| Phonological rules | Accentual-phrase phrasing is the domain of the sandhi rules (연음 liaison, 경음화 tensification, 비음화 nasalization, etc.); see the phonological_rules section. |
| Orthography | Hangul's one-block-per-syllable design (한글 syllable blocks) underpins Korean syllable awareness discussed under Rhythm; see the orthography section. |

**Companion files (repo-relative):**

- `Korean/korean_pronunciation_guide.md`
- `Korean/Peshita_Korean/Hangul/`
- `Korean/Peshita_Korean/Romanized/`
- `Korean/Peshita_Korean/Scholarly/`
- `Korean/Peshita_Korean/Pretty/`

**Reader-tiers note:** The Korean Peshitta ships four reader tiers — Scholarly and Pretty (language-neutral Latin), Hangul (한글 composed blocks), and Revised Romanization (RR readback of the Hangul). Suprasegmental information (boundary tones for sentence type, AP phrasing) is not encoded in the Hangul or RR tiers themselves and lives in this guide; readers using those tiers should consult this section for intonation and phrasing.

---

*Section version 1.0.0 — created 2026-06-25. Compiled by Shin.*

## Syllable Structure

Syllable structure patterns in Standard Korean, documented for two reference standards in parallel: Standard South Korean (표준어 *pyojun-eo*, educated Seoul speech) and North Korean (문화어 *munhwaeo*, Pyongyang-based standard). The Korean syllable is maximally (C)(G)V(C): a single optional onset consonant, an optional on-glide /j w/ (and /ɰ/ only in ㅢ), an obligatory vocalic nucleus, and a single optional coda (받침 *batchim*). Korean is in sharp contrast with English: it has NO onset clusters and NO coda clusters in pronunciation, so the maximal pronounced syllable is CGVC and the statistically dominant shapes are CV and CVC. Two facts dominate Korean syllabification: (1) the coda NEUTRALIZES to just seven sounds — [k t p l m n ŋ] — regardless of how it is spelled (음절의 끝소리 규칙), and written cluster codas (겹받침) simplify so that only one consonant is pronounced; and (2) Korean has no lexical stress and no lexical tone, so syllable weight does not drive a stress system. Hangul is written in square SYLLABLE BLOCKS that visually encode this structure (초성 onset / 중성 medial / 종성 coda), and spelling is MORPHOPHONEMIC: the written block preserves the underlying morpheme shape while the pronounced syllable obeys the neutralization, resyllabification (연음), and sandhi rules below. This section is the Korean equivalent of the Peshitta guide's syllable_structure section and underlies the Hangul reader-tier transducer (which must insert an epenthetic ㅡ /ɯ/ to break up loanword consonant clusters that Korean syllables cannot host).

**IPA template:** `(C)(G)V(C)`

**Maximal syllable:** `CGVC`

**Preferred syllable:** `CV`

### Reference Standards

| Standard | Description |
|---|---|
| South | Standard South Korean — 표준어 (*pyojun-eo*), educated Seoul speech. |
| North | North Korean — 문화어 (*munhwaeo*), Pyongyang-based standard. |

**Note:** Syllable structure proper (the (C)(G)V(C) template and the 7-sound coda neutralization) is shared by both standards. The standards differ mainly in word-initial onset distribution via the 두음법칙 (initial-sound rule): South changes word-initial ㄹ→ㄴ→∅ and ㄴ→∅ before i/j (여자 *yeoja* '女子', 노동 *nodong* '勞動'), so native/Sino-Korean words avoid initial ㄹ and initial ㄴ before i/j; North RETAINS them (녀자 *nyeoja*, 로동 *rodong*), permitting onset ㄹ /ɾ/ and ㄴ /n/ before i/j word-initially. See the constraints list and the phonological_rules section for detail.

**Components:**

- **Onset (초성 *choseong*):** 0 to 1 consonant preceding the nucleus *(optional; no clusters)*
- **Glide (G):** an optional on-glide /j w/ (or /ɰ/ only in ㅢ), fused into the compound medial jamo *(optional)*
- **Nucleus (중성 *jungseong*):** V — an obligatory vowel; no syllabic consonants *(required)*
- **Coda (종성 *jongseong* / 받침 *batchim*):** 0 to 1 PRONOUNCED consonant following the nucleus *(optional; neutralizes to 7 sounds)*

### Onset

초성 (*choseong*): 0 or 1 consonant preceding the nucleus — Korean has NO onset clusters whatsoever. Any of the 18 onset-capable consonants may fill the slot; ㅇ in onset position is a SILENT placeholder (a graphic zero-onset marker, NOT the velar nasal), so a syllable written with initial ㅇ is phonemically onsetless. The velar nasal /ŋ/ therefore never occurs as an onset — the symbol ㅇ stands for /ŋ/ only when it is a coda. Plain (lax) onsets ㄱ /k/, ㄷ /t/, ㅂ /p/, ㅈ /tɕ/ voice intervocalically to [ɡ d b dʑ]; ㅅ /s/ palatalizes to [ɕ] before /i/ or /j/; ㄹ as an intervocalic onset is the tap [ɾ]. Standards diverge only word-initially via the 두음법칙 (see Reference Standards / Constraints).

- **Minimum consonants:** 0
- **Maximum consonants:** 1

**No clusters:** Korean permits no consonant clusters in the onset at all (no /pl/, /st/, /spr/, etc.). Foreign clusters are repaired by epenthesis of /ɯ/ (written ㅡ), each inserted vowel spawning a new CV syllable — this is the core operation of the Hangul reader-tier transducer (see Loanword Adaptation and Constraints).

**Onset consonants** — count: 18.

| Jamo | Phonemic |
|---|---|
| `ㄱ` | /k/ |
| `ㄲ` | /k͈/ |
| `ㄴ` | /n/ |
| `ㄷ` | /t/ |
| `ㄸ` | /t͈/ |
| `ㄹ` | /l ~ ɾ/ |
| `ㅁ` | /m/ |
| `ㅂ` | /p/ |
| `ㅃ` | /p͈/ |
| `ㅅ` | /s/ |
| `ㅆ` | /s͈/ |
| `ㅈ` | /tɕ/ |
| `ㅉ` | /tɕ͈/ |
| `ㅊ` | /tɕʰ/ |
| `ㅋ` | /kʰ/ |
| `ㅌ` | /tʰ/ |
| `ㅍ` | /pʰ/ |
| `ㅎ` | /h/ |

**Silent placeholder:** `ㅇ` as an onset is a silent zero-onset placeholder (not /ŋ/); it occupies the choseong slot graphically but adds no consonant (e.g. 아 /a/, 어 /ʌ/, 우 /u/).

**Excluded from onset:** ㅇ-as-/ŋ/ never functions as an onset — /ŋ/ is a coda-only sound.

| Hangul | Phonemic | Phonetic | Onset | Gloss |
|---|---|---|---|---|
| 가 | /ka/ | [ka] | ㄱ /k/ | go (stem 가-) |
| 까 | /k͈a/ | — | ㄲ /k͈/ | (tense onset; e.g. 까다 'to peel') |
| 칼 | /kʰal/ | — | ㅋ /kʰ/ | knife |
| 아 | /a/ | — | ㅇ (silent placeholder) | ah (onsetless syllable) |
| 시 | /ɕi/ | [ɕi] | ㅅ /s/ → [ɕ] before /i/ | poem; o'clock |
| 사람 | /saɾam/ | [saˈɾam] | ㄹ → [ɾ] (intervocalic onset of 2nd syllable) | person |

### Glide

G = an optional on-glide between the onset (or zero-onset) and the vowel: /j/ (palatal) or /w/ (labiovelar), plus /ɰ/ which occurs ONLY in the single medial ㅢ /ɰi/. In Hangul the glide is not written as a separate letter; it is fused into the COMPOUND MEDIAL (중성) jamo: the y-series ㅑ /ja/, ㅕ /jʌ/, ㅛ /jo/, ㅠ /ju/, ㅒ /jɛ/, ㅖ /je/ carry /j/, and the w-series ㅘ /wa/, ㅙ /wɛ/, ㅝ /wʌ/, ㅞ /we/ carry /w/; ㅚ /ø/ and ㅟ /y/ are conservative front rounded monophthongs usually realized as the glide+vowel diphthongs [we], [wi]. The glide is thus structurally part of the nucleus block, but functions as the (G) margin of the (C)(G)V(C) template.

**Glides:** `j`, `w`, `ɰ` (only in ㅢ /ɰi/).

| Hangul | Phonemic | Phonetic | Glide | Gloss |
|---|---|---|---|---|
| 야 | /ja/ | — | j | hey (vocative particle) |
| 와 | /wa/ | — | w | and; wow |
| 의 | /ɰi/ | [ɰi] ~ [i] ~ [e] | ɰ | of (genitive particle 의); the only /ɰ/ medial. Often realized [i] word-internally and [e] as the genitive particle. |

### Nucleus

중성 (*jungseong*): the obligatory vocalic core, ALWAYS present — Korean has no syllabic consonants. The nucleus is one of the monophthongs, or a glide+vowel sequence already encoded inside a compound medial jamo (so a CGV syllable is written with a single composite medial). Korean has no phonemic vowel length in the modern Seoul standard (a length contrast survives marginally and is largely lost for younger speakers) and no English-style vowel reduction. The 애/에 merger means ㅐ /ɛ/ and ㅔ /e/ are realized as a single mid front [e̞] for most younger Seoul speakers.

**Required:** yes.

**No syllabic consonants:** There are NO syllabic-consonant nuclei (nothing like English 'bottle' /l̩/ or 'button' /n̩/). Every Korean syllable contains a full vowel.

#### Monophthong nucleus

A single vowel. The modern Seoul inventory is ~7–8 monophthongs (conservative speakers up to 10, counting ㅚ /ø/ and ㅟ /y/ as monophthongs).

| Jamo | Phonemic |
|---|---|
| `ㅏ` | /a/ |
| `ㅓ` | /ʌ/ |
| `ㅗ` | /o/ |
| `ㅜ` | /u/ |
| `ㅡ` | /ɯ/ |
| `ㅣ` | /i/ |
| `ㅐ` | /ɛ/ |
| `ㅔ` | /e/ |

**Conservative extra monophthongs:**

| Jamo | Phonemic |
|---|---|
| `ㅚ` | /ø/ (often [we]) |
| `ㅟ` | /y/ (often [wi]) |

| Hangul | Phonemic | Phonetic | Nucleus | Gloss |
|---|---|---|---|---|
| 아 | /a/ | — | ㅏ /a/ | ah |
| 어 | /ʌ/ | — | ㅓ /ʌ/ | uh |
| 이 | /i/ | — | ㅣ /i/ | this; tooth; two (Sino) |
| 으 | /ɯ/ | — | ㅡ /ɯ/ | (the epenthetic / connecting vowel; also interjection) |
| 게 | /ke/ | [ke̞] | ㅔ /e/ (merged [e̞]) | crab |
| 개 | /kɛ/ | [ke̞] | ㅐ /ɛ/ (merged [e̞] for most younger Seoul speakers) | dog |

#### Glide+vowel nucleus

A glide+vowel sequence written as a single compound medial. The y-series and w-series jamo bundle the on-glide into the nucleus block; ㅚ and ㅟ are conservatively monophthongal front rounded vowels that are usually diphthongized.

**y-series:**

| Jamo | Phonemic |
|---|---|
| `ㅑ` | /ja/ |
| `ㅕ` | /jʌ/ |
| `ㅛ` | /jo/ |
| `ㅠ` | /ju/ |
| `ㅒ` | /jɛ/ |
| `ㅖ` | /je/ |

**w-series:**

| Jamo | Phonemic |
|---|---|
| `ㅘ` | /wa/ |
| `ㅙ` | /wɛ/ |
| `ㅝ` | /wʌ/ |
| `ㅞ` | /we/ |

**Front rounded or diphthong:**

| Jamo | Realization |
|---|---|
| `ㅚ` | /ø/ → usually [we] |
| `ㅟ` | /y/ → usually [wi] |

**Iotated with eu:**

| Jamo | Phonemic |
|---|---|
| `ㅢ` | /ɰi/ |

| Hangul | Phonemic | Phonetic | Nucleus | Gloss |
|---|---|---|---|---|
| 여자 (South) / 녀자 (North) | South /jʌ.tɕa/ · North /njʌ.tɕa/ | — | ㅕ /jʌ/ | woman (女子). South 여자 by 두음법칙; North retains initial ㄴ as 녀자. |
| 과 | /kwa/ | — | ㅘ /wa/ | lesson; department; and (clausal) |
| 되다 | /twe.ta/ | [twe.da] ~ [tø.da] | ㅚ /ø/ → [we] | to become (citation 되다) |
| 의사 | /ɰi.sa/ | [ɰi.sa] ~ [i.sa] | ㅢ /ɰi/ | doctor |

### Coda

종성 (*jongseong*) / 받침 (*batchim*): 0 or 1 PRONOUNCED consonant after the nucleus. The signature fact of the Korean syllable is that, no matter how the coda is SPELLED, it is realized as only one of SEVEN sounds — [k t p l m n ŋ] — when nothing follows (음절의 끝소리 규칙, the coda-neutralization or seven-sound rule). All aspirated, tense, fricative, and affricate codas neutralize to a plain unreleased stop of the same place ([k̚ t̚ p̚]); ㅎ as a coda has no independent realization. Furthermore, a written CLUSTER coda (겹받침, e.g. ㄳ ㄵ ㄶ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅄ) simplifies so that ONLY ONE of its two consonants is pronounced; the surviving member still neutralizes to one of the seven sounds. There is therefore never more than one consonant pronounced in a Korean coda. Note that the neutralized coda is only the SURFACE form in pre-pause / pre-consonant position: when a vowel-initial syllable follows, the underlying coda RESYLLABIFIES into the next onset (연음) and surfaces faithfully (e.g. 옷 [ot̚] 'clothes' but 옷이 [o.ɕi] 'clothes-NOM').

- **Minimum consonants:** 0
- **Maximum consonants:** 1

**Neutralization outputs (seven sounds):** [k], [t], [p], [l], [m], [n], [ŋ].

**Neutralization rule name:** 음절의 끝소리 규칙 (*eumjeol-ui kkeutsori gyuchik*) — coda neutralization / the seven-sound rule.

#### Single-jamo coda neutralization

How each single written jamo, when it stands as a pre-pause / pre-consonant coda, maps to one of the seven neutralized sounds. Velars → [k]; coronal obstruents and ㅎ → [t]; labials → [p]; the three sonorant classes keep their own values.

| Neutralized sound | Written jamo → realization |
|---|---|
| → [k] | `ㄱ` → [k]; `ㄲ` → [k]; `ㅋ` → [k] |
| → [t] | `ㄷ` → [t]; `ㅌ` → [t]; `ㅅ` → [t]; `ㅆ` → [t]; `ㅈ` → [t]; `ㅊ` → [t]; `ㅎ` → [t] (and ㅎ typically deletes / triggers aspiration before another consonant) |
| → [p] | `ㅂ` → [p]; `ㅍ` → [p] |
| → [l] | `ㄹ` → [l] |
| → [m] | `ㅁ` → [m] |
| → [n] | `ㄴ` → [n] |
| → [ŋ] | `ㅇ` → [ŋ] (this is the ONLY position where ㅇ is the velar nasal /ŋ/) |

| Hangul | Phonemic | Phonetic | Coda written | Coda pronounced | Gloss |
|---|---|---|---|---|---|
| 밖 | /pak̚/ | [pak̚] | `ㄲ` | [k] | outside (밖 spelled with ㄲ, pronounced [pak̚]) |
| 옷 | /ot̚/ | [ot̚] | `ㅅ` | [t] | clothes (ㅅ coda → [t]; cf. 옷이 [o.ɕi]) |
| 부엌 | /pu.ʌk̚/ | [pu.ʌk̚] | `ㅋ` | [k] | kitchen (부엌, ㅋ coda → [k]: [pu.ʌk̚]); shows aspirate coda neutralizing to plain [k] |
| 앞 | /ap̚/ | [ap̚] | `ㅍ` | [p] | front (앞, ㅍ coda → [p]; cf. 앞에 [a.pʰe]) |
| 꽃 | /k͈ot̚/ | [k͈ot̚] | `ㅊ` | [t] | flower (꽃, ㅊ coda → [t]; cf. 꽃이 [k͈o.tɕʰi]) |
| 방 | /paŋ/ | [paŋ] | `ㅇ` | [ŋ] | room (방, ㅇ coda = /ŋ/) |

#### Cluster-coda simplification (겹받침)

겹받침 (*gyeop-batchim*) cluster-coda simplification (자음군 단순화 *jaeumgun dansunhwa*). A written two-consonant coda drops one member in pre-pause / pre-consonant position; the surviving consonant then neutralizes to one of the seven sounds. The general tendency is to keep the FIRST consonant, except ㄺ → [k] and ㄻ → [m] (keep the SECOND), with ㄼ and ㄺ showing lexically and dialectally conditioned variation. When a VOWEL-initial suffix follows, the cluster does NOT simplify: the first consonant stays as the coda and the second resyllabifies into the next onset (e.g. 닭 [tak̚] but 닭이 [tal.ɡi]).

| Cluster | Components | Pronounced | Rule | Example | Example IPA | Gloss |
|---|---|---|---|---|---|---|
| `ㄳ` | ㄱ + ㅅ | [k] | keep ㄱ; ㅅ drops | 넋 | [nʌk̚] | soul/spirit (cf. 넋이 [nʌk.s͈i]) |
| `ㄵ` | ㄴ + ㅈ | [n] | keep ㄴ; ㅈ drops | 앉다 | [an.t͈a] | to sit (앉- → [an]; ㅈ feeds tensification of following ㄷ) |
| `ㄶ` | ㄴ + ㅎ | [n] | keep ㄴ; ㅎ drops (but ㅎ aspirates a following plain stop, 격음화) | 많다 | [man.tʰa] | to be many (많- → [man]; ㅎ + ㄷ → [tʰ]) |
| `ㄺ` | ㄹ + ㄱ | [k] (default) / [l] (before ㄱ-initial suffix, and lexically variable) | keep ㄱ → [k] by default (닭 [tak̚], 읽다 [ik̚.t͈a]); but keep ㄹ → [l] before a ㄱ-initial verb ending (읽고 [il.k͈o]). One of the two classic variation points. | 닭 | [tak̚] | chicken (cf. 닭이 [tal.ɡi]; 읽고 [il.k͈o]) |
| `ㄻ` | ㄹ + ㅁ | [m] | keep ㅁ; ㄹ drops | 삶 | [sam] | life (삶 → [sam]; cf. 삶이 [sal.mi]) |
| `ㄼ` | ㄹ + ㅂ | [l] (default) / [p] (lexical exceptions 밟- and 넓죽/넓둥글-) | keep ㄹ → [l] in most words (여덟 [jʌ.tʌl], 넓다 [nʌl.t͈a]); but keep ㅂ → [p] in the lexical exceptions 밟다 [pap̚.t͈a] and 넓죽하다 [nʌp̚.t͈ɕu.kʰa.da]. The second classic variation point. | 여덟 | [jʌ.tʌl] | eight (여덟 → [jʌ.dʌl]); contrast exception 밟다 [pap̚.t͈a] 'to step on' |
| `ㄽ` | ㄹ + ㅅ | [l] | keep ㄹ; ㅅ drops | 외곬 | [ø.kol] ~ [we.gol] | single track / one way (외곬 → coda [l]) |
| `ㄾ` | ㄹ + ㅌ | [l] | keep ㄹ; ㅌ drops | 핥다 | [hal.t͈a] | to lick (핥- → [hal]; ㅌ feeds tensification) |
| `ㄿ` | ㄹ + ㅍ | [p] | keep ㅍ → [p]; ㄹ drops (rare; e.g. 읊-) | 읊다 | [ɯp̚.t͈a] | to recite/chant (읊- → coda [p]) |
| `ㅀ` | ㄹ + ㅎ | [l] | keep ㄹ; ㅎ drops (but ㅎ aspirates a following plain stop, 격음화) | 싫다 | [ɕil.tʰa] | to dislike (싫- → [ɕil]; ㅎ + ㄷ → [tʰ]) |
| `ㅄ` | ㅂ + ㅅ | [p] | keep ㅂ; ㅅ drops | 값 | [kap̚] | price (값 → [kap̚]; cf. 값이 [kap.s͈i]) |

**Summary:** Default 'keep first consonant' clusters: ㄳ→k, ㄵ→n, ㄶ→n, ㄽ→l, ㄾ→l, ㅀ→l, ㅄ→p. 'Keep second consonant' clusters: ㄻ→m, ㄿ→p. Lexically variable: ㄺ (default→k, but →l before ㄱ-suffix) and ㄼ (default→l, but →p in 밟다 and 넓죽-/넓둥글-).

**Resyllabification caveat:** Cluster simplification applies only before a pause or consonant. Before a vowel-initial suffix the second consonant resyllabifies into the next onset and BOTH consonants surface (닭이 [tal.ɡi], 값을 [kap.s͈ɯl], 앉아 [an.dʑa]).

### Syllable Types

| Type | Description | IPA example | Hangul | Gloss | Frequency |
|---|---|---|---|---|---|
| V | Bare vowel; zero (silent ㅇ) onset, no coda (open). The medial sits with the silent ㅇ placeholder. | /i/ | 이 | this; tooth; two (二) | Common (particles, vowel-initial words) |
| CV | Onset + vowel (open) — the canonical, statistically dominant Korean syllable. | /na/ | 나 | I/me | Most common |
| VC | Vowel + coda (zero onset, closed). | /an/ | 안 | inside; not (안) | Common |
| CVC | Onset + vowel + coda (closed). The other very high-frequency shape. | /pap̚/ (clean /pap/) | 밥 | cooked rice / meal | Very common |
| GV / CGV | On-glide + vowel (with optional onset), written with a compound medial (open). With silent ㅇ it is GV; with a real onset it is CGV. | /ja/ | 야 | hey (야); CGV example: 과 /kwa/ 'lesson' | Common |
| GVC / CGVC | On-glide + vowel + coda (with optional onset), the MAXIMAL pronounced syllable when an onset is present (CGVC). | /kwʌn/ | 권 | volume/book counter (권); GVC example: 영 /jʌŋ/ 'zero' | Common |
| CGVC (maximal) | Onset + glide + vowel + coda — the fullest legal Korean syllable. No clusters in onset or coda. | /kjʌŋ/ | 경 | scripture/sutra; capital (京); also as in 경기 'match' | Common |

### Syllabification

**Principle:** Coda-then-onset assignment with obligatory resyllabification across morpheme/word boundaries (연음), constrained by the strict (C)(G)V(C) template — at most one onset consonant and at most one (pronounced) coda consonant per syllable.

Hangul orthography already segments the underlying string into morphophonemic syllable blocks, but the PRONOUNCED syllabification is recomputed by the sandhi rules. The dominant medial process is 연음 (liaison / resyllabification): when a coda is followed by a vowel-initial syllable (typically a particle or suffix beginning with silent ㅇ), the coda consonant moves to the onset of that following syllable and surfaces FAITHFULLY (undoing neutralization). Conversely, in pre-pause and pre-consonant position the coda neutralizes to the seven sounds and cluster codas simplify. Because no Korean syllable can host an onset cluster or a coda cluster, an underlying string is always parsed so that each syllable is at most (C)(G)V(C).

| Word | Phonemic | Phonetic | Note |
|---|---|---|---|
| 한국어 | /han.ɡu.ɡʌ/ | [han.ɡu.ɡʌ] | han-gug-eo: the ㄱ coda of 국 [kuk̚] in isolation resyllabifies as the onset of 어 and voices intervocalically to [ɡ] → [han.ɡu.ɡʌ] |
| 옷이 | /o.ɕi/ | [o.ɕi] | 연음: 옷 alone is [ot̚] (ㅅ→[t]), but before the nominative -이 the ㅅ moves to onset and surfaces faithfully as /s/ → [ɕ] before /i/ |
| 꽃이 | /k͈o.tɕʰi/ | [k͈o.tɕʰi] | 연음 undoes neutralization: 꽃 alone is [k͈ot̚], but 꽃이 keeps the underlying ㅊ as onset → [k͈o.tɕʰi] |
| 닭이 | /tal.ɡi/ | [tal.ɡi] | before a vowel the ㄺ cluster does NOT simplify: ㄹ stays as coda [l], ㄱ resyllabifies to onset and voices → [tal.ɡi] (vs isolation 닭 [tak̚]) |
| 값을 | /kap.s͈ɯl/ | [kap.s͈ɯl] | ㅄ before the accusative -을: ㅂ stays as coda, ㅅ resyllabifies into onset and tenses to [s͈] → [kap.s͈ɯl] (vs isolation 값 [kap̚]) |
| 독립 | /toŋ.nip̚/ | [toŋ.nip̚] | dok-rip '독립' (independence): consonant assignment interacts with sandhi — ㄹ→[n] after the obstruent (비음화/유음화 environment) and the resulting [n] back-nasalizes the ㄱ coda to [ŋ] |

#### Resyllabification (연음)

**Name:** 연음 (*yeoneum*) — liaison / resyllabification.

A syllable-final consonant (coda) is pronounced as the ONSET of the next syllable when that syllable begins with a vowel (the silent-ㅇ placeholder). Because the consonant then sits in onset/intervocalic position, neutralization is undone (the underlying obstruent surfaces faithfully) and plain lax obstruents voice. For cluster codas, the first consonant remains as the coda and the SECOND resyllabifies into the next onset. This is the single most important parsing operation for converting morphophonemic Hangul into pronounced syllables and is fundamental to the Hangul reader-tier transducer.

| Phrase | IPA | Note |
|---|---|---|
| 음악 | [ɯ.mak̚] | eum-ak '음악' (music): the ㅁ coda of 음 onsets the vowel of 악 → [ɯ.mak̚] |
| 할아버지 | [ha.ɾa.bʌ.dʑi] | harabeoji '할아버지' (grandfather): ㄹ coda → intervocalic onset [ɾ]; ㅂ and ㅈ voice intervocalically to [b], [dʑ] |
| 먹어요 | [mʌ.ɡʌ.jo] | meogeoyo '먹어요' (eat-POLITE): ㄱ coda of 먹 onsets 어 and voices to [ɡ] → [mʌ.ɡʌ.jo] |

**Interacting rules note:** Pronounced syllabification cannot be read off the spelling alone: it is the output of the full rule chain documented in the phonological_rules section — 음절의 끝소리 규칙 (coda neutralization), 자음군 단순화 (cluster simplification), 연음 (liaison), 비음화 (nasalization), 유음화 (lateralization), 경음화 (tensification), 격음화 (aspiration), 구개음화 (palatalization), and ㄴ-첨가 (n-insertion).

### Loanword Adaptation

Because Korean syllables allow NO onset or coda clusters, foreign words with consonant clusters are repaired by epenthesis of /ɯ/ (written ㅡ), inserting a vowel between offending consonants so each consonant gets its own (C)V syllable. A few coda consonants also pick up an epenthetic ㅡ when the source coda is not one of the seven legal sounds or is part of a cluster. This is exactly the operation the Hangul reader tier performs when transducing a Latin/IPA reading into composable Hangul blocks.

**Epenthetic vowel:** ㅡ /ɯ/ (the default minimal vowel; /i/ is used after some palatals/affricates in established loans).

| Source | Source IPA | Hangul | Korean IPA | Note |
|---|---|---|---|---|
| English 'strike' | /straɪk/ | 스트라이크 | [sɯ.tʰɯ.ɾa.i.kʰɯ] | the /str/ onset cluster and final /k/ each get an epenthetic ㅡ: s-tu-ra-i-keu (5 syllables) |
| English 'Christmas' | /ˈkrɪsməs/ | 크리스마스 | [kʰɯ.ɾi.s͈ɯ.ma.s͈ɯ] | keu-ri-seu-ma-seu: epenthesis breaks /kr/ and the /s/ clusters |
| English 'McDonald's' | /məkˈdɑnəldz/ | 맥도날드 | [mɛk̚.t͈o.nal.dɯ] | maek-do-nal-deu: final cluster /ldz/ resolved with epenthetic ㅡ |
| English 'film' | /fɪlm/ | 필름 | [pʰil.lɯm] | pil-leum: /f/→/pʰ/ (no native /f/), and the /lm/ cluster is split by epenthetic ㅡ |

### Constraints

- The maximal Korean syllable is (C)(G)V(C): at most ONE onset consonant, at most one on-glide /j w/ (or /ɰ/ only in ㅢ), an obligatory vowel, and at most ONE pronounced coda consonant. The preferred and most frequent shapes are CV and CVC.
- There are NO onset clusters of any kind. Foreign clusters are repaired by epenthesis of /ɯ/ (written ㅡ), each inserted vowel creating a new CV syllable ('strike' → 스트라이크 [sɯ.tʰɯ.ɾa.i.kʰɯ]). This is the core operation of the Hangul reader-tier transducer.
- ㅇ has two roles depending on position: as an ONSET it is a SILENT zero-onset placeholder (가 vs 아); as a CODA it is the velar nasal /ŋ/ (방 /paŋ/). /ŋ/ therefore NEVER occurs in onset position.
- Every syllable must contain a vocalic nucleus — Korean has NO syllabic consonants (nothing like English 'bottle' /l̩/ or 'button' /n̩/).
- The coda NEUTRALIZES to seven sounds only — [k t p l m n ŋ] (음절의 끝소리 규칙). Aspirated/tense/fricative/affricate codas reduce to a plain unreleased stop of the same place ([k̚ t̚ p̚]); coda ㅎ has no independent value. Single-jamo mapping: velars (ㄱ ㄲ ㅋ)→[k]; coronals & ㅎ (ㄷ ㅌ ㅅ ㅆ ㅈ ㅊ ㅎ)→[t]; labials (ㅂ ㅍ)→[p]; ㄹ→[l]; ㅁ→[m]; ㄴ→[n]; ㅇ→[ŋ].
- Written CLUSTER codas (겹받침) simplify to ONE pronounced consonant (자음군 단순화). Default keep-first: ㄳ→k, ㄵ→n, ㄶ→n, ㄽ→l, ㄾ→l, ㅀ→l, ㅄ→p. Keep-second: ㄻ→m, ㄿ→p. Lexically variable: ㄺ (default→k, but →l before a ㄱ-initial ending, e.g. 읽고 [il.k͈o]); ㄼ (default→l, e.g. 여덟 [jʌ.dʌl], but →p in the exceptions 밟다 [pap̚.t͈a] and 넓죽-/넓둥글-).
- Coda simplification and neutralization apply ONLY before a pause or a consonant. Before a vowel-initial suffix, 연음 (resyllabification) moves the coda (or, for clusters, the SECOND consonant) into the next onset, where it surfaces faithfully and (if a plain obstruent) voices: 옷 [ot̚] but 옷이 [o.ɕi]; 닭 [tak̚] but 닭이 [tal.ɡi]; 값 [kap̚] but 값을 [kap.s͈ɯl].
- There is NO phonemic vowel length in the modern Seoul standard (a residual length contrast is largely lost for younger speakers) and NO English-style vowel reduction; the nucleus keeps full quality regardless of position. ㅐ /ɛ/ and ㅔ /e/ are merged to [e̞] for most younger Seoul speakers (the 애/에 merger).
- The on-glide is not an independent letter; /j w/ are bundled into compound medial jamo (y-series ㅑㅕㅛㅠㅒㅖ; w-series ㅘㅙㅝㅞ), and ㅚ /ø/, ㅟ /y/ are conservative front rounded monophthongs usually diphthongized to [we], [wi]. /ɰ/ occurs only in ㅢ /ɰi/.
- 두음법칙 (initial-sound rule) — SOUTH ONLY: word-initial ㄹ→ㄴ→∅ and ㄴ→∅ before i/j, so Standard South Korean avoids onset ㄹ and onset ㄴ-before-i/j word-initially (여자 yeoja '女子', 노동 nodong '勞動', 이씨 'surname Yi/Lee'). NORTH (문화어) does NOT apply it and retains those onsets (녀자, 로동, 리씨). This is a distribution constraint on the ONSET slot, not a change to the (C)(G)V(C) template.
- There is NO lexical stress and NO lexical tone in Standard Korean, so syllable weight does not feed a stress system; prosody is organized in accentual phrases (AP) with a phrase-level tune. (Pitch-accent dialects Gyeongsang and Hamgyŏng are the exception — asides only.)
- Hangul writes each syllable as a square block (초성 onset / 중성 medial / 종성 coda) and spelling is MORPHOPHONEMIC (it preserves morpheme shape, not surface phonetics); the pronounced syllabification is the output of the full sandhi rule chain (see phonological_rules), not a direct readout of the block.

> **Cross-reference:** This section underpins the Hangul reader tier (한글 composed blocks) and its Revised Romanization (RR) readback among the four Korean Peshitta reader tiers (Scholarly, Pretty, Hangul, RR). The coda-neutralization, cluster-simplification, resyllabification (연음), and loanword-epenthesis behaviors specified here drive the Hangul transducer that maps a phonemic reading into legal (C)(G)V(C) syllable blocks; see the companion files `Korean/korean_pronunciation_guide.md` and the Hangul tier under `Korean/Peshita_Korean/Hangul/`. Full rule formulations live in the phonological_rules section of this guide.

<sub>Maintained by Shin.</sub>

## Phonological Rules

Korean's signature system of largely automatic phonological rules (음운 규칙 *eumun gyuchik*) that map morphophonemic Hangul spelling onto surface pronunciation. Korean orthography is morphophonemic — it preserves the underlying shape of each morpheme rather than its surface phonetics — so this rule set is what the Hangul-to-IPA transducer applies to recover actual pronunciation. The rules are documented in parallel for the two reference standards: **Standard South Korean** (표준어 *pyojun-eo*, educated Seoul speech) and **North Korean** (문화어 *munhwaeo*, Pyongyang standard). The vast majority of these processes are shared by both standards; the principal divergence is 두음법칙 (initial-sound rule), which the South applies and the North does not, plus a few realizational details. Most rules operate within the prosodic/morphological word and at compound and clitic boundaries; some (연음 liaison, 비음화 nasalization, 경음화 tensification) also apply across word boundaries in connected speech. Accent scope is marked 'both', 'South', or 'North'; where a process applies in both but differs in detail, the divergence is noted. IPA examples are given as composed Hangul → surface-pronunciation Revised Romanization (RR) → surface IPA after the rule applies, using /slashes/ for underlying phonemic forms and [brackets] for surface phonetic forms; the RR tier transcribes the actual sound after the rule has applied (tense consonants doubled: kk tt pp ss jj), consistently with the surface IPA. Korean has **NO** phonemic voicing contrast, **NO** lexical stress, and **NO** lexical tone, so these rules are conditioned purely by segmental and morphological environment, not by stress.

### Rules at a Glance

| # | Rule | Process | Accents |
|---|---|---|---|
| 1 | 음절의 끝소리 규칙 — coda neutralization / seven-sound batchim rule | `C(coda) → {[k̚], [t̚], [p̚], [l], [m], [n], [ŋ]} / _{C, #}` | both |
| 2 | 겹받침 단순화 — consonant-cluster (double batchim) simplification | `C₁C₂(coda) → C₁ or C₂ / _{C, #}` | both |
| 3 | 연음 — liaison / resyllabification (받침 옮기기) | `...C(coda).V... → ...∅.CV...` | both |
| 4 | 유성음화 / 평음 유성음화 — intervocalic voicing of lax stops | `/k t p tɕ/ → [ɡ d b dʑ] / V_V` | both |
| 5 | 비음화 — nasalization (obstruent → nasal before a nasal) | `/k t p/(coda) → [ŋ n m] / _[+nasal]` | both |
| 6 | ㄹ의 비음화 — ㄹ-nasalization (ㄹ → [n] after most consonants) | `ㄹ /l/ → [n] / {nasal/obstruent}(coda)_` | both |
| 7 | 유음화 — lateralization (ㄴ → [l] adjacent to ㄹ) | `ㄴ /n/ → [l] / ㄹ_ or _ㄹ ; ㄹㄹ → [ll]` | both |
| 8 | 경음화 — tensification / fortis (plain obstruent → tense) | `/k t p s tɕ/ → [k͈ t͈ p͈ s͈ tɕ͈]` | both |
| 9 | 격음화 / 자음 축약 — aspiration / ㅎ-coalescence | `ㅎ + /k t p tɕ/ → [kʰ tʰ pʰ tɕʰ]` | both |
| 10 | ㅎ 탈락 / ㅎ 약화 — ㅎ-deletion and intervocalic ㅎ-weakening | `ㅎ → ∅ / V_V ; intervocalic ㅎ → [ɦ] ~ ∅` | both |
| 11 | 구개음화 — palatalization (ㄷ/ㅌ + i/j → [tɕ]/[tɕʰ]) | `ㄷ /t/, ㅌ /tʰ/ → [tɕ], [tɕʰ] / _{i, j}` | both |
| 12 | ㄴ 첨가 — n-insertion at compound/word boundaries | `∅ → [n] / C(coda) + {이 야 여 요 유 …}` | both |
| 13 | 두음법칙 — initial-sound rule (the key South↔North split) | word-initial ㄹ/ㄴ → ㄴ/∅ (South); retained (North) | South |
| 14 | ㅅ → [ɕ] — s-palatalization before /i, j/ | `ㅅ /s/ → [ɕ], ㅆ /s͈/ → [ɕ͈] / _{i, j, ɥ}` | both |
| 15 | ㄹ의 이음 — ㄹ allophony: tap [ɾ] vs. lateral [l] | `ㄹ /l/ → [ɾ] / V_V ; → [l] / _{C, #}` | both |
| 16 | 모음 조화 잔존 / ㅢ 약화 — minor vocalic processes | `ㅢ /ɰi/ → [ɰi] ~ [i] ~ [e]` | both |

### Rule 1: 음절의 끝소리 규칙 (eumjeol-ui kkeutsori gyuchik) — coda neutralization / seven-sound batchim rule

The foundational Korean coda rule. Any consonant in syllable-final (받침 *batchim*) position before a consonant or a pause neutralizes to one of only SEVEN possible coda sounds: [k̚ t̚ p̚ l m n ŋ]. The fourteen-plus consonants that can be written as a coda collapse into these seven: the velar series `ㄱ`/`ㄲ`/`ㅋ` → [k̚]; the coronal obstruents `ㄷ`/`ㅌ`/`ㅅ`/`ㅆ`/`ㅈ`/`ㅊ`/`ㅎ` → [t̚]; the labial series `ㅂ`/`ㅍ` → [p̚]; with `ㄹ`→[l], `ㅁ`→[m], `ㄴ`→[n], `ㅇ`→[ŋ] kept distinct. Surface coda obstruents are unreleased (no audible burst), hence the [ ̚ ] diacritic. This rule is fed by 겹받침 단순화 (cluster simplification) and is BLED by 연음 (liaison): when a vowel-initial suffix follows, the coda resyllabifies as an onset instead of neutralizing (낮에 → [na.tɕe], not \*[nat.e]).

**IPA example:** 낮 → RR 'nat' → `[nat̚]` ; 부엌 → RR 'bueok' → `[pu.ʌk̚]` ; 옷 → RR 'ot' → `[ot̚]` ; 빛 → RR 'bit' → `[pit̚]`  
**IPA notation:** `C(coda) → {[k̚], [t̚], [p̚], [l], [m], [n], [ŋ]} / _{C, #}` ; obstruents are unreleased  
**Environment:** Underlying coda consonant before another consonant or before a pause / word boundary; does NOT apply when a vowel-initial particle or suffix follows (liaison applies first)  
**Accents:** both  

### Rule 2: 겹받침 단순화 (gyeopbatchim dansunhwa) — consonant-cluster (double batchim) simplification

When a cluster batchim (`ㄳ ㄵ ㄶ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅄ` etc.) stands before a consonant or pause, only ONE of the two written consonants is pronounced; the other deletes. The survivor is partly lexically conditioned: `ㄳ`→[k̚], `ㄵ`→[n], `ㄶ`→[n], `ㄼ`→[l] (밟 'tread' is the exception → [p̚]: 밟다 [pap̚t͈a]), `ㄽ`→[l], `ㄾ`→[l], `ㅄ`→[p̚], `ㄻ`→[m], `ㄿ`→[p̚]. For `ㄺ` the survivor is usually [k̚] (닭 [tak̚]), but before a ㄱ-initial suffix the ㄹ survives (읽고 [ilk͈o]); for `ㄶ`/`ㅀ` the ㅎ instead triggers aspiration of a following stop (see 격음화) rather than simply deleting. This rule must be ordered to FEED both coda neutralization and the assimilation/tensification rules. Under 연음 (liaison) a cluster batchim splits: the first consonant stays as coda, the second resyllabifies as onset (값이 → [kap.ɕ͈i], the tense ㅅ palatalizing to [ɕ͈] before /i/ per the ㅅ→[ɕ] rule; 닭을 → [tal.ɡɯl]).

**IPA example:** 값 → RR 'gap' → `[kap̚]` ; 닭 → RR 'dak' → `[tak̚]` ; 삶 → RR 'sam' → `[sam]` ; 앉다 → RR 'antta' → `[an.t͈a]` ; 읽고 → RR 'ilkko' → `[il.k͈o]` ; 밟다 → RR 'baptta' → `[pap̚.t͈a]`  
**IPA notation:** `C₁C₂(coda) → C₁ or C₂ / _{C, #}` ; survivor is lexically/rule-determined  
**Environment:** Two-consonant (cluster) batchim before a consonant or pause; splits under liaison before a vowel-initial suffix  
**Accents:** both  

### Rule 3: 연음 (yeoneum) — liaison / resyllabification (받침 옮기기)

When a syllable-final consonant (or the second member of a cluster batchim) is followed by a vowel-initial particle, suffix, or — across a word boundary in close juncture — a vowel-initial word, the coda moves into the onset of the following syllable. Crucially, in this position the consonant is realized in its FULL underlying value, NOT its neutralized coda value: 꽃이 surfaces [k͈otɕʰi] (the ㅊ keeps its aspirated affricate quality), not \*[k͈odi]. Liaison therefore BLEEDS coda neutralization and feeds intervocalic voicing of lax stops. With `ㅇ` (a silent onset placeholder) the coda fills the empty onset slot. A salient exception: a coda ㅎ deletes rather than resyllabifying before a vowel (놓아 → [no.a], see ㅎ-탈락). Liaison is the chief reason Hangul spelling and pronunciation diverge for inflected words.

**IPA example:** 꽃이 → RR 'kkoch-i' → `[k͈o.tɕʰi]` ; 옷을 → RR 'os-eul' → `[o.sɯl]` ; 한국어 → RR 'hangug-eo' → `[han.ɡu.ɡʌ]` ; 깎아 → RR 'kkakk-a' → `[k͈a.k͈a]`  
**IPA notation:** `...C(coda).V... → ...∅.CV... / coda + vowel-initial suffix/particle (no intervening pause)`  
**Environment:** Coda consonant immediately followed by a vowel-initial morpheme (particle, suffix) or vowel-initial word in close juncture; blocked by a pause and by coda ㅎ  
**Accents:** both  

### Rule 4: 유성음화 / 평음 유성음화 (yuseong-eumhwa) — intervocalic voicing of lax stops

The plain (lax/lenis) obstruents `ㄱ` /k/, `ㄷ` /t/, `ㅂ` /p/, `ㅈ` /tɕ/ are voiceless word-initially but VOICE to [ɡ d b dʑ] between voiced sounds — between two vowels, or between a sonorant (nasal or ㄹ) and a vowel. This is fully automatic and allophonic: Korean has no phonemic voicing contrast, so [k] and [ɡ] are the same phoneme `ㄱ`. It is the reason 바보 'fool' sounds like [pabo] (first ㅂ voiceless, second voiced) and why RR writes the same letter as 'g/k', 'd/t', 'b/p', 'j' positionally. The tense and aspirated series do NOT voice. Voicing is fed by 연음 (which places a lax stop intervocalically) and is bled by 경음화 (which converts the stop to tense) and by 비음화/격음화 (which change its manner).

**IPA example:** 바보 → RR 'babo' → `[pa.bo]` ; 부디 → RR 'budi' → `[pu.di]` ; 고기 → RR 'gogi' → `[ko.ɡi]` ; 아주 → RR 'aju' → `[a.dʑu]` ; 한국 → RR 'hanguk' → `[han.ɡuk̚]`  
**IPA notation:** `/k t p tɕ/ → [ɡ d b dʑ] / V_V` , also after `/n m ŋ l/` (sonorant)_V  
**Environment:** Lax obstruent between two voiced segments: V_V, or after a nasal/ㄹ before a vowel; never word-initially after a pause  
**Accents:** both  

### Rule 5: 비음화 (bieumhwa) — nasalization (obstruent → nasal before a nasal)

A neutralized stop coda assimilates in manner to a following nasal, becoming the nasal at its own place of articulation: velar [k̚] → [ŋ] before ㄴ/ㅁ (국물 [kuŋmul]); coronal [t̚] → [n] (받는 [pannɯn], and note `ㅈ ㅊ ㅌ ㅅ ㄷ` all neutralize to [t̚] first, then nasalize to [n]); labial [p̚] → [m] (입맛 [immat̚]). This is the single most pervasive Korean assimilation and applies word-internally and across word boundaries in connected speech. It is FED by coda neutralization and cluster simplification (which deliver a plain stop coda) and interacts with ㄹ-nasalization (a following ㄹ becomes [n], which can then itself trigger nasalization of a preceding stop).

**IPA example:** 국물 → RR 'gungmul' → `[kuŋ.mul]` ; 받는다 → RR 'banneunda' → `[pan.nɯn.da]` ; 입맛 → RR 'immat' → `[im.mat̚]` ; 한국말 → RR 'hangungmal' → `[han.ɡuŋ.mal]`  
**IPA notation:** `/k t p/(coda) → [ŋ n m] / _[+nasal]` (i.e. before ㄴ ㅁ)  
**Environment:** Stop coda [k̚ t̚ p̚] immediately before a nasal ㄴ or ㅁ, within a word or across a boundary  
**Accents:** both  

### Rule 6: ㄹ의 비음화 (rieul-ui bieumhwa) — ㄹ-nasalization (ㄹ → [n] after most consonants)

Word-internal or compound-internal ㄹ in onset position becomes [n] when it follows a consonant that is NOT ㄹ or ㄴ. (1) After a nasal coda ㅁ/ㅇ, ㄹ→[n] directly: 종로 → [tɕoŋno], 심리 → [ɕimni]. (2) After an obstruent coda, ㄹ→[n] AND the obstruent then nasalizes by 비음화: 독립 → underlying /tok.lip/ → ㄹ→n /tok.nip/ → stop nasalizes /toŋ.nip/ → [toŋnip̚]. This rule must be ORDERED before 비음화 so that the newly created [n] can trigger nasalization of the preceding stop (a feeding interaction). It contrasts directly with 유음화 (lateralization): when ㄹ is adjacent to ㄴ, the outcome is [ll], not [nn] (see next rule).

**IPA example:** 종로 → RR 'Jongno' → `[tɕoŋ.no]` ; 독립 → RR 'dongnip' → `[toŋ.nip̚]` ; 심리 → RR 'simni' → `[ɕim.ni]` ; 대통령 → RR 'daetongnyeong' → `[tɛ.tʰoŋ.njʌŋ]`  
**IPA notation:** `ㄹ /l/ → [n] / {nasal, or obstruent}(coda)_` ; the obstruent then nasalizes too  
**Environment:** ㄹ in onset after a coda consonant other than ㄹ/ㄴ; the conditioning obstruent subsequently nasalizes  
**Accents:** both  

### Rule 7: 유음화 (yueumhwa) — lateralization (ㄴ → [l] adjacent to ㄹ)

When ㄴ and ㄹ are adjacent, ㄴ becomes [l], yielding a geminate lateral [ll]. This happens both regressively — ㄴ before ㄹ: 신라 /sin.la/ → [ɕilla] — and progressively — ㄴ after ㄹ: 칼날 /kʰal.nal/ → [kʰallal], 설날 → [sʌllal]. Lateralization and ㄹ-nasalization are in competition for the ㄴ+ㄹ / ㄹ+ㄴ environment: native and most Sino-Korean items lateralize ([ll]), but certain Sino-Korean compounds where the boundary is morphologically salient instead show ㄹ→[n] nasalization (e.g. 생산량 → [sɛŋsannjaŋ], 의견란 → [ɰiɡjʌnnan]). The lexical/morphological split is one of the trickier ordering problems for the transducer; the default for tightly-bound items is lateralization.

**IPA example:** 신라 → RR 'Silla' → `[ɕil.la]` ; 천리 → RR 'cheolli' → `[tɕʰʌl.li]` ; 칼날 → RR 'kallal' → `[kʰal.lal]` ; 설날 → RR 'seollal' → `[sʌl.lal]`  
**IPA notation:** `ㄴ /n/ → [l] / ㄹ_ or _ㄹ` (regressive and progressive); ㄹㄹ → [ll]  
**Environment:** ㄴ immediately adjacent to ㄹ (either order), within a word or tight compound; competes with ㄹ-nasalization at certain morpheme boundaries  
**Accents:** both  

### Rule 8: 경음화 (gyeong-eumhwa) — tensification / fortis (plain obstruent → tense)

A plain obstruent `ㄱ ㄷ ㅂ ㅅ ㅈ` becomes its tense (fortis) counterpart `ㄲ ㄸ ㅃ ㅆ ㅉ` in several environments. (1) **Post-obstruent:** automatically after any neutralized stop coda [k̚ t̚ p̚] — 국밥 [kuk̚p͈ap̚], 식당 [ɕik̚t͈aŋ]. This is the most regular case and is FED by coda neutralization. (2) **After a sonorant-final verb/adjective STEM** before a suffix — 안다 'embrace' /an.ta/ → [ant͈a], 앉다 [ant͈a] (morphologically conditioned; does NOT apply to nouns, cf. 안다 'know' (알- + -ㄴ다) → [anda], no tensification — the ㄷ voices instead). (3) **After the ㄹ of certain Sino-Korean roots** — 갈등 [kalt͈ɯŋ], 발달 [paldal]→[pal.t͈al] (the no-audible-release diacritic is reserved for stop codas, so the coda ㄹ surfaces as a plain lateral [l]). (4) **After the prospective/determiner ending -(으)ㄹ** — 할 것 [halk͈ʌt̚], 갈 데 [kalt͈e]. Tensification BLEEDS intervocalic voicing (a tensed stop never voices).

**IPA example:** 국밥 → RR 'gukppap' → `[kuk̚.p͈ap̚]` ; 식당 → RR 'sikttang' → `[ɕik̚.t͈aŋ]` ; 앉다 → RR 'antta' → `[an.t͈a]` ; 할 것 → RR 'halkkeot' → `[hal.k͈ʌt̚]` ; 갈등 → RR 'galtteung' → `[kal.t͈ɯŋ]`  
**IPA notation:** `/k t p s tɕ/ → [k͈ t͈ p͈ s͈ tɕ͈] / {[k̚ t̚ p̚]_, or sonorant-final verb stem_, or ㄹ of ㄹ-final Sino-roots_, or determiner -ㄹ_}`  
**Environment:** Plain obstruent after a stop coda; after sonorant-final predicate stems; after ㄹ in specified Sino-Korean roots; after the determiner ending -ㄹ  
**Accents:** both  

### Rule 9: 격음화 / 자음 축약 (gyeok-eumhwa / jaeum chugyak) — aspiration / ㅎ-coalescence

When ㅎ is adjacent to a plain stop/affricate `ㄱ ㄷ ㅂ ㅈ` — in either order — the two coalesce into a single aspirated segment [kʰ tʰ pʰ tɕʰ]. (1) **ㅎ before a stop:** 좋고 /tɕoh.ko/ → [tɕokʰo], 놓다 → [notʰa], and from cluster batchim 많다 /manh.ta/ → [mantʰa], 싫고 → [ɕilkʰo]. (2) **Stop before ㅎ** (often across a morpheme boundary): 입학 /ip.hak/ → [ipʰak̚], 축하 /tɕuk.ha/ → [tɕʰukʰa] (note BOTH affected: the k→kʰ here), 맏형 → [matʰjʌŋ]. Aspiration is fed by cluster simplification (which exposes the ㅎ of `ㄶ`/`ㅀ`) and competes with ㅎ-deletion: when ㅎ instead meets a vowel or a sonorant, it deletes rather than aspirating (see next rule).

**IPA example:** 좋고 → RR 'joko' → `[tɕo.kʰo]` ; 놓다 → RR 'nota' → `[no.tʰa]` ; 입학 → RR 'ipak' → `[i.pʰak̚]` ; 축하 → RR 'chuka' → `[tɕʰu.kʰa]` ; 많다 → RR 'manta' → `[man.tʰa]`  
**IPA notation:** `ㅎ + /k t p tɕ/ → [kʰ tʰ pʰ tɕʰ]` (either order); ㅎ coalesces with adjacent plain stop into a single aspirate  
**Environment:** ㅎ immediately adjacent (either order) to a plain stop or affricate ㄱ/ㄷ/ㅂ/ㅈ, word-internally or at a morpheme boundary  
**Accents:** both  

### Rule 10: ㅎ 탈락 / ㅎ 약화 (hieut tallak) — ㅎ-deletion and intervocalic ㅎ-weakening

ㅎ is unstable between voiced segments. (1) A stem-final coda ㅎ (including the ㅎ of `ㄶ` `ㅀ`) **DELETES** before a vowel-initial suffix, and the rest of the cluster (if any) resyllabifies: 좋아 /tɕoh.a/ → [tɕoa], 많이 /manh.i/ → [mani], 싫어 /silh.ʌ/ → [ɕiɾʌ] (the freed ㄹ resyllabifies and surfaces as the intervocalic tap [ɾ]). This crucially BLEEDS liaison of the ㅎ itself and bleeds coda neutralization. (2) **Onset ㅎ** between voiced sounds is widely weakened to a voiced [ɦ] or deleted entirely in casual speech: 전화 → careful [tɕʌnɦwa], casual [tɕʌnwa]; 결혼 → [kjʌɾon]. Word-initially and after a pause, ㅎ is a full [h].

**IPA example:** 좋아 → RR 'joa' → `[tɕo.a]` ; 많이 → RR 'mani' → `[ma.ni]` ; 싫어 → RR 'sireo' → `[ɕi.ɾʌ]` ; 전화 → RR 'jeonhwa' → `[tɕʌ.nwa]` ~ `[tɕʌn.ɦwa]`  
**IPA notation:** `ㅎ → ∅ / V_V` , and `/ sonorant_V` (coda ㅎ before a vowel-initial suffix); intervocalic ㅎ → [ɦ] ~ ∅  
**Environment:** Coda ㅎ before a vowel-initial suffix (categorical deletion); onset ㅎ between voiced segments (gradient weakening/deletion)  
**Accents:** both  

### Rule 11: 구개음화 (gugae-eumhwa) — palatalization (ㄷ/ㅌ + i/j → [tɕ]/[tɕʰ])

A coronal stop ㄷ or ㅌ in coda position becomes the corresponding palato-alveolar affricate when followed across a MORPHEME boundary by the vowel /i/ or a /j/-onset suffix: ㄷ→[tɕ], ㅌ→[tɕʰ]. So 굳이 /kut.i/ → [kudʑi], 같이 /katʰ.i/ → [katɕʰi], 해돋이 → [hɛdodʑi]. A special sub-case: stem-final ㄷ + the suffix 히 first coalesces ㄷ+ㅎ→ㅌ (aspiration) and then palatalizes to [tɕʰ]: 닫히다 → [tatɕʰida]. Palatalization is strictly limited to a heteromorphemic boundary — it does NOT apply morpheme-internally (잔디 'lawn' stays [tɕandi], 느티나무 stays [nɯtʰinamu]). It must be ordered to interact with liaison (which delivers the ㄷ/ㅌ into prevocalic position) and feeds intervocalic voicing.

**IPA example:** 굳이 → RR 'guji' → `[ku.dʑi]` ; 같이 → RR 'gachi' → `[ka.tɕʰi]` ; 해돋이 → RR 'haedoji' → `[hɛ.do.dʑi]` ; 붙이다 → RR 'buchida' → `[pu.tɕʰi.da]`  
**IPA notation:** `ㄷ /t/, ㅌ /tʰ/ → [tɕ], [tɕʰ] / _{이 /i/, 히 (>티), or j-glide of a suffix}`  
**Environment:** Stem-final ㄷ/ㅌ before a suffix beginning in /i/ or /j/ (heteromorphemic only); never word-internally  
**Accents:** both  

### Rule 12: ㄴ 첨가 (nieun cheomga) — n-insertion at compound/word boundaries

At a compound or prefix+stem boundary, when the first element ends in a consonant and the second element begins with /i/ or a /j/-glide (이 야 여 요 유 etc.), an epenthetic [n] is inserted at the onset of the second element: 솜이불 'cotton quilt' → [somnibul], 한여름 'midsummer' → [hannjʌɾɯm]. The inserted [n] then FEEDS downstream rules: it triggers nasalization of a preceding stop (색연필 /sɛk.jʌn.pʰil/ → n-insertion → /sɛk.njʌn.pʰil/ → 비음화 → [sɛŋnjʌnpʰil]) and may lateralize to [l] next to ㄹ (들일 → [tɯllil], 알약 → [alljak̚]). Coda neutralization also feeds it (꽃잎 → 꽃→[k̚…]→ +n → 비음화 → [k͈onnip̚]). n-insertion is partly lexically conditioned and does not apply across all compounds — a known source of variation and a hard case for the transducer.

**IPA example:** 솜이불 → RR 'somnibul' → `[som.ni.bul]` ; 한여름 → RR 'hannyeoreum' → `[han.njʌ.ɾɯm]` ; 색연필 → RR 'saengnyeonpil' → `[sɛŋ.njʌn.pʰil]` ; 꽃잎 → RR 'kkonnip' → `[k͈on.nip̚]`  
**IPA notation:** `∅ → [n] / C(coda) + {이 야 여 요 유 얘 예}` (i- or j-initial second member of a compound)  
**Environment:** Consonant-final first member + i-/j-initial second member at a compound, prefix, or close word boundary; lexically variable  
**Accents:** both  

### Rule 13: 두음법칙 (dueum beopchik) — initial-sound rule (SOUTH only; the key South↔North split)

The single most prominent prescriptive difference between the two standards, affecting word-INITIAL liquids and nasals chiefly in Sino-Korean vocabulary. **SOUTH KOREA applies 두음법칙:** (1) word-initial ㄹ before /i/ or /j/ drops entirely — 리(理)→이, 력(力)→역, so 女子 is written and said 여자 [jʌdʑa], 理由 이유 [iju]; (2) word-initial ㄹ before other vowels becomes ㄴ — 勞動 노동 [nodoŋ], 樂園 낙원 [nakwʌn]; (3) word-initial ㄴ before /i/ or /j/ drops — 女 녀→여, 尿 뇨→요. **NORTH KOREA (문화어) does NOT apply the rule:** it RETAINS the etymological initial ㄹ/ㄴ in both spelling and speech — 녀자 [njʌdʑa], 로동 [ɾodoŋ], 리유 [ɾiju], 락원 [ɾaɡwʌn]. The rule applies only word-initially, so the same root keeps ㄹ medially in compounds in both standards (실패율, 도리). This is the rule the transducer must branch on by target standard.

**IPA example:**
- South: 여자 → RR 'yeoja' → `[jʌ.dʑa]` (cf. North 녀자 `[njʌ.dʑa]`)
- South: 노동 → RR 'nodong' → `[no.doŋ]` (cf. North 로동 `[ro.doŋ]`)
- South: 이발 → RR 'ibal' (cf. North 리발 `[ɾi.bal]`)
- South: 낙원 → RR 'nagwon' (cf. North 락원 `[ɾa.ɡwʌn]`)

**IPA notation:** word-initial `ㄹ → ㄴ → ∅ / _{i, j}` ; word-initial `ㄹ → ㄴ / _{other V}` ; word-initial `ㄴ → ∅ / _{i, j}` (South prescriptive; North: no change)  
**Environment:** Word-initial (and certain compound-initial) ㄹ or ㄴ, mainly in Sino-Korean morphemes; South applies the change, North retains the original consonant  
**Accents:** South  

### Rule 14: ㅅ → [ɕ] / 경구개음화 앞 (s-palatalization before /i, j/)

The alveolar fricatives `ㅅ` /s/ and `ㅆ` /s͈/ are realized as the alveolo-palatal [ɕ] / [ɕ͈] before the high front vowel /i/, before any /j/-glide, and before the labio-palatal glide of `ㅟ`. Thus 시 [ɕi], 씨 [ɕ͈i], 샤 [ɕja], 쉬 [ɕɥi]. This is a fully automatic allophonic adjustment with no phonemic consequence (Korean has no /ʃ/ phoneme distinct from /s/), and it holds in both standards. RR conventionally writes the sequence as 'si/sya/syu' so the spelling does not show the palatal quality.

**IPA example:** 시 → RR 'si' → `[ɕi]` ; 신 → RR 'sin' → `[ɕin]` ; 샤 → RR 'sya' → `[ɕja]` ; 쉬다 → RR 'swida' → `[ɕɥi.da]` ; 씨 → RR 'ssi' → `[ɕ͈i]`  
**IPA notation:** `ㅅ /s/ → [ɕ], ㅆ /s͈/ → [ɕ͈] / _{i, j, ɥ}`  
**Environment:** ㅅ/ㅆ immediately before /i/, a /j/-glide, or the glide of ㅟ; allophonic, automatic  
**Accents:** both  

### Rule 15: ㄹ의 이음 (rieul-ui ieum) — ㄹ allophony: tap [ɾ] vs. lateral [l]

The single liquid phoneme `ㄹ` has two principal surface forms in complementary distribution: a flap/tap [ɾ] as a single intervocalic onset (나라 [naɾa], 다리 [taɾi]), and a clear lateral [l] in coda position (물 [mul], 달 [tal]) and in the geminate produced by ㄹㄹ or by 유음화 (빨리 [p͈alli], 신라 [ɕilla]). Word-initial ㄹ is a marginal case: in native/onomatopoeic and loan words it surfaces as [ɾ] (라디오 [ɾadio]), while in Sino-Korean it is reshaped by 두음법칙 in the South (see that rule). This allophony is automatic and shared by both standards.

**IPA example:** 나라 → RR 'nara' → `[na.ɾa]` ; 다리 → RR 'dari' → `[ta.ɾi]` ; 물 → RR 'mul' → `[mul]` ; 달 → RR 'dal' → `[tal]` ; 빨리 → RR 'ppalli' → `[p͈al.li]`  
**IPA notation:** `ㄹ /l/ → [ɾ] / V_V` (intervocalic onset); `→ [l] / _{C, #}` (coda) and in geminate ㄹㄹ [ll]  
**Environment:** Intervocalic single ㄹ → tap [ɾ]; coda or geminate ㄹ → lateral [l]; allophonic  
**Accents:** both  

### Rule 16: 모음 조화 잔존 / ㅢ 약화 (moeum johwa janjon 殘存 'residue/survival' & ㅢ realization) — minor vocalic processes

Two residual vocalic adjustments. (1) The diphthong `ㅢ` /ɰi/ is realized in full [ɰi] only word-initially with no onset consonant (의사 [ɰisa]); after a consonant onset it reduces to plain [i] (무늬 [muni], 희망 [himaŋ]); in non-initial syllables it is commonly [i] (회의 [hwei]); and as the genitive particle 의 it is standardly read [e] (나의 [nae]). (2) Vestigial vowel harmony survives only in the choice of the connective/past ending allomorph -아/-어 and in ideophones (졸졸 [tɕoltɕol] 'bright' vs. 줄줄 [tɕuldʑul] 'dark'), governed by the historical 양성/음성 (bright/dark) vowel classes rather than being a productive surface rule. Both standards agree here, with the genitive [e] reading being a standard-Seoul prescription.

**IPA example:** 의사 → RR 'uisa' → `[ɰi.sa]` ; 회의 → RR 'hoeui' → `[hwe.i]` ; 무늬 → RR 'muni' → `[mu.ni]` ; 민주주의 → RR 'minjujuui' → `[min.dʑu.dʑu.i]`  
**IPA notation:** `ㅢ /ɰi/ → [ɰi]` word-initial; `→ [i]` non-initial / after C; `→ [e]` as the genitive particle 의  
**Environment:** ㅢ in word-initial vs. post-consonantal vs. particle position; harmony-class allomorph selection in endings and ideophones  
**Accents:** both  

### Notes

Korean phonological rules are highly ORDERED and exhibit classic feeding and bleeding interactions; the Hangul-to-IPA transducer must respect this ordering. A robust default ordering is:

1. **겹받침 단순화** (cluster simplification) and **ㅎ-related coalescence/deletion** expose the relevant coda;
2. **연음** (liaison) applies first wherever a vowel-initial suffix follows, BLEEDING coda neutralization and feeding intervocalic voicing and 구개음화;
3. **음절의 끝소리 규칙** (coda neutralization) then fixes the seven-sound coda before consonants/pause;
4. **assimilations** apply — ㄹ-비음화 feeds 비음화, and 유음화 competes with ㄹ-비음화 by lexical class;
5. **경음화** (tensification) and **격음화** (aspiration) apply, BLEEDING intervocalic voicing;
6. finally **low-level allophony** — lax-stop voicing, ㅅ→[ɕ], and ㄹ tap/lateral selection — fills in surface detail.

**두음법칙** is applied lexically at the word level and is the ONE rule the transducer branches on by standard: SOUTH applies it (여자, 노동, 이유), NORTH does not (녀자, 로동, 리유); a few realizational details (e.g. a slightly more conservative North coda system and vowel qualities) otherwise distinguish 표준어 from 문화어, but the segmental rule set above is overwhelmingly shared. **ㄴ-insertion** and the **유음화/ㄹ-비음화 split** are the chief sites of lexical variation and should be backed by an exception lexicon rather than pure rule application. These rules are documented in parallel with the companion tiers shipped for the Korean Peshitta — Scholarly + Pretty (language-neutral Latin), Hangul (한글, e.g. `Korean/Peshita_Korean/Hangul/`), and Revised Romanization readback of the Hangul — and cross-reference the syllable_structure and orthography_grapheme_phoneme sections of `Korean/korean_pronunciation_guide.md`.

## Standard South Korean vs. North Korean

Systematic differences between the two REFERENCE STANDARDS of Modern Korean, expressed in IPA and Hangul. The two standardized traditions documented in parallel are Standard South Korean — 표준어 (pyojun-eo), the educated-Seoul standard codified by the National Institute of the Korean Language — and North Korean — 문화어 (munhwaeo, 'cultural language'), the Pyongyang-based standard codified by North Korea's language authorities. As with the Eastern (Madnhaya) and Western (Serto) traditions of Syriac, or General American and Received Pronunciation in English, neither standard is intrinsically more correct: they are two coexisting codifications of one language, both descended from the same Hanseong/Seoul prestige speech and overwhelmingly mutually intelligible. The single deepest structural division is the 두음법칙 (dueum beopchik, 'initial-sound rule'): the South changes word-initial `ㄹ`/`ㄴ` in Sino-Korean morphemes (勞動 → 노동, 女子 → 여자), whereas the North retains the etymological initial `ㄹ`/`ㄴ` (로동, 녀자). Korean has NO lexical tone or lexical stress in either standard, so this section carries no pitch contrasts between South and North; pitch-accent and the deeply divergent regional varieties (Gyeongsang, Jeolla, Chungcheong, Hamgyŏng, and especially Jeju) are treated below as clearly secondary ASIDES. Phonemic transcriptions use /slashes/; phonetic detail uses [brackets]. Hangul is given in 한글; readback Romanization follows Revised Romanization (RR) unless McCune–Reischauer (MR) is explicitly noted.

### Reference standards

- **표준어 (pyojun-eo) — Standard South Korean:** 표준어 ('standard language') — educated Seoul speech, codified in the 표준어 규정 (Standard Language Regulations) and 한글 맞춤법 (Hangul Orthography). APPLIES 두음법칙: word-initial `ㄹ` → `ㄴ` → `∅` and `ㄴ` → `∅` before /i, j/ in Sino-Korean roots (로동→노동, 녀자→여자, 리→이). Younger Seoul speakers merge `ㅐ`/`ㅔ` to [e̞] (the 애/에 merger) and largely lose the `ㅚ`/`ㅟ` monophthongs to [we]/[wi]. Liberal loanword borrowing from English, written in Hangul under the 외래어 표기법 (Loanword Orthography). Undergoing an onset-conditioned tonogenetic shift (lenis vs aspirate/tense onsets now cue following pitch), but still NO phonemic tone.
- **문화어 (munhwaeo) — North Korean:** 문화어 ('cultural language') — Pyongyang-based standard, codified in the 조선말규범집 (Joseonmal Gyubeumjip). Does NOT apply 두음법칙: etymological word-initial `ㄹ`/`ㄴ` are written and (prescriptively) pronounced (로동, 녀자, 리씨; 력사 for 역사). Slightly more conservative consonant realizations and a prescriptively firmer, sometimes 'stronger'/more tensed delivery. Purist lexicon — many Sino-Korean and Western loans replaced by native 다듬은 말 (refined words); loanwords leaning Russian where the South leans English. Like the South, NO phonemic tone or stress.

### Differences

| Feature | South (표준어) | North (문화어) | Examples | Explanation |
|---|---|---|---|---|
| 두음법칙 — 초성 `ㄹ` → `ㄴ` → `∅` (initial-sound rule on `ㄹ`) | `ㄹ`-initial Sino-Korean roots shift: `ㄹ` → `ㄴ` → `∅` word-initially — 노동 /no.toŋ/, 이씨 /i.s͈i/, 양심 /jaŋ.ɕim/ | etymological initial `ㄹ` retained in spelling and prescriptive speech — 로동 /ɾo.toŋ/, 리씨 /ɾi.s͈i/, 량심 /ɾjaŋ.ɕim/ | 勞動 'labor': South 노동 (nodong) /no.toŋ/ — North 로동 (rodong) /ɾo.toŋ/; 李氏 'the Lee/Yi clan; surname Lee': South 이씨 (i-ssi) /i.s͈i/ — North 리씨 (ri-ssi) /ɾi.s͈i/; 良心 'conscience': South 양심 (yangsim) /jaŋ.ɕim/ — North 량심 (ryangsim) /ɾjaŋ.ɕim/; 歷史 'history': South 역사 (yeoksa) /jʌk.s͈a/ — North 력사 (ryeoksa) /ɾjʌk.s͈a/ | The defining division of the two standards. In Sino-Korean morphemes whose etymological onset is `ㄹ` /l~ɾ/, South Korean orthography and pronunciation drop or change that onset word-initially: before most vowels `ㄹ` → `ㄴ` (勞 로→노), and before /i/ or a /j/-glide `ㄹ` → `∅` with the syllable simply losing its onset (理 리→이, 良 량→양). The North keeps the etymological `ㄹ` written and prescriptively pronounced as [ɾ]. The rule is positional, not lexical: even in the South the same morpheme keeps `ㄹ` word-medially (勞動 → 노동 but 過勞 → 과로 'overwork'; 歷史 → 역사 but 經歷 → 경력 'career'), and the surname 李 is southern 이 but northern 리. This single rule produces the most frequent and most recognizable South↔North spelling/pronunciation splits in running text. |
| 두음법칙 — 초성 `ㄴ` → `∅` before /i, j/ (initial-sound rule on `ㄴ`) | word-initial `ㄴ` deletes before /i/ or a /j/-glide in Sino-Korean roots — 여자 /jʌ.tɕa/, 익명 /iŋ.mjʌŋ/, 요소 /jo.so/ | word-initial `ㄴ` retained before /i, j/ — 녀자 /njʌ.tɕa/, 닉명 /niŋ.mjʌŋ/, 뇨소 /njo.so/ | 女子 'woman': South 여자 (yeoja) /jʌ.tɕa/ — North 녀자 (nyeoja) /njʌ.tɕa/; 匿名 'anonymity': South 익명 (ingmyeong) /iŋ.mjʌŋ/ — North 닉명 (ningmyeong) /niŋ.mjʌŋ/; 尿素 'urea': South 요소 (yoso) /jo.so/ — North 뇨소 (nyoso) /njo.so/; 女性 'female (sex)': South 여성 (yeoseong) /jʌ.sʌŋ/ — North 녀성 (nyeoseong) /njʌ.sʌŋ/ | The second branch of 두음법칙: in the South, an etymological word-initial `ㄴ` /n/ is also deleted when it precedes /i/ or a /j/-on-glide, so 女 (etymological 녀) surfaces as 여 and 尿 (뇨) as 요. The North retains the `ㄴ`, giving 녀자, 뇨소. As with the `ㄹ` branch, the rule is strictly word-initial: 男女 'men and women' is 남녀 (namnyeo) in BOTH standards because the 女 morpheme is non-initial there. This is why 'woman' alone is southern 여자 but the compound keeps 녀 in 남녀 even in Seoul. |
| Surname and proper-noun reflexes of 두음법칙 | personal/clan names follow the South initial-sound rule — 이 (Lee) /i/, 임 (Lim) /im/, 유 (Yu/Ryu) /ju/, 나 (Na) /na/ | names keep etymological `ㄹ`/`ㄴ` — 리 (Ri) /ɾi/, 림 (Rim) /ɾim/, 류 (Ryu) /ɾju/, 라 (Ra) /ɾa/ | surname 李: South 이 (I, romanized 'Lee'/'Yi') /i/ — North 리 (Ri) /ɾi/; surname 林: South 임 (Im) /im/ — North 림 (Rim) /ɾim/; surname 柳/劉: South 유 (Yu) /ju/ — North 류 (Ryu) /ɾju/; surname 羅: South 나 (Na) /na/ — North 라 (Ra) /ɾa/ | The most socially visible application of the rule is in names. The hugely common surname 李 is 이 (officially romanized 'Lee' or 'Yi' though pronounced /i/) in the South but 리 (Ri) in the North — Korean-diaspora spellings 'Rhee/Yi/Lee' all trace to the same 李. Note a fine print: South Korean naming law permits a person to register the etymological `ㄹ` form (e.g. 류 Ryu rather than 유 Yu) as a personal preference, so some Southern surnames retain `ㄹ` by individual choice even though the default rule would delete it. North Korean orthography applies the etymological form uniformly. |
| Lexical divergence — purism vs borrowing (다듬은 말 vs 외래어) | many international loanwords (mostly via English), written in Hangul — 주스 /tɕu.sɯ/ 'juice', 노크 /no.kʰɯ/ 'knock', 아이스크림 /a.i.sɯ.kʰɯ.ɾim/ | native/refined coinages (다듬은 말); Western loans fewer, often Russian-routed — 단물 /tan.mul/ 'sweet water = juice', 손기척 /son.ki.tɕʌk̚/ 'hand-signal = knock', 얼음보숭이 /ʌ.ɾɯm.po.suŋ.i/ | 'juice': South 주스 (juseu) /tɕu.sɯ/ — North 단물 (danmul) /tan.mul/; 'ice cream': South 아이스크림 (aiseukeurim) — North 얼음보숭이 (eoreumbosung-i) /ʌ.ɾɯm.po.suŋ.i/; 'knock (on a door)': South 노크 (nokeu) /no.kʰɯ/ — North 손기척 (songicheok) /son.ki.tɕʌk̚/; 'tractor': South 트랙터 (teuraekteo, from English) — North 뜨락또르 (tteurakttoreu, from Russian тра́ктор) | Beyond phonology, the standards diverge sharply in vocabulary policy. South Korean freely borrows international vocabulary (overwhelmingly from English) and writes it in Hangul under the 외래어 표기법. North Korean language planning has pursued 말다듬기 ('word-refining'), replacing many Sino-Korean and Western loans with transparent native compounds — 단물 'sweet-water' for juice, 얼음보숭이 for ice cream. Where the North does keep a Western loan, its source and shape often differ: 뜨락또르 (from Russian тра́ктор) vs Southern 트랙터 (from English 'tractor'). These are lexical rather than phonological differences, but they change the surface IPA of everyday words wholesale and are a constant cue to which standard a text follows. |
| Orthographic spacing and morphophonemic spelling norms | looser spacing; bound nouns/auxiliaries often spaced; sai-siot `ㅅ` written — 나뭇잎 /na.mun.nip̚/ 'tree leaf' (with sai-siot), 할 수 있다 spaced | tighter compounding; sai-siot generally NOT written; more words joined — 나무잎 /na.mu.ip̚/ (no sai-siot in spelling), 할수 있다 joined | 'tree leaf': South 나뭇잎 (namunnip) — North 나무잎 (namuip), differing on the 사이시옷 (sai-siot); 'can do / be able to': South 할 수 있다 (spaced) — North 할수 있다 (tighter); 'rain water': South 빗물 (binmul, sai-siot) — North 비물 (bimul) | The two orthographies differ in spacing (띄어쓰기) and in the 사이시옷 (sai-siot) convention. South Korean writes an interfix `ㅅ` between the elements of many native compounds to mark the tensing/nasal-insertion at the boundary (나무 + 잎 → 나뭇잎, pronounced /na.mun.nip̚/), and spaces bound nouns such as 수 'ability' and 것 'thing'. North Korean orthography largely does NOT write the sai-siot (나무잎, 비물) and compounds/spaces more tightly. The underlying boundary phonology (n-insertion, tensing) can still occur in speech, but the spellings — and therefore the romanized readback — diverge. These are prescriptive orthographic choices rather than deep sound changes. |
| Vowel realization — `ㅓ` /ʌ/ and the 애/에 merger | Seoul `ㅓ` is mid-low unrounded [ʌ̹]~[ɔ̜]; `ㅐ`/`ㅔ` merged to [e̞] for younger speakers — 어머니 [ʌ.mʌ.ni], 개 [kɛ]=게 [ke] → both [ke̞] | Pyongyang `ㅓ` noticeably rounder/backer, often [ɔ]; `ㅐ`/`ㅔ` contrast more often kept — 어머니 [ɔ.mɔ.ni], 개 [kɛ] vs 게 [ke] kept distinct | 어머니 'mother': South [ʌ.mʌ.ni] — North [ɔ.mɔ.ni] (rounder `ㅓ`); 거름 'manure' / 걸음 'a step': South both ~[kʌ.ɾɯm] — North 거름 [kɔ.ɾɯm] with rounder `ㅓ`; 개 'dog' / 게 'crab': South younger [ke̞] = [ke̞] (merged) — North [kɛ] vs [ke] (kept) | Realization of the vowels differs subtly. The Seoul `ㅓ` /ʌ/ is a fairly open, unrounded back-central [ʌ̹]; the Pyongyang `ㅓ` is described as backer and distinctly rounder, edging toward [ɔ], a stereotyped marker of Northern speech. The South leads the 애/에 merger, with most younger Seoul speakers collapsing `ㅐ` /ɛ/ and `ㅔ` /e/ to a single mid [e̞], so 개 'dog' and 게 'crab' are homophones; the North (and conservative Southern speakers) more often keep the two apart. Both standards share the same eight-vowel inventory on paper; the divergence is in phonetic realization and in how far the merger has spread. |
| Consonant realization — onset lenis voicing and overall 'tension' | lax stops voice intervocalically [ɡ d b dʑ]; emerging tonogenesis (onset cues pitch) — 고기 [ko.ɡi] 'meat', 바다 [pa.da] 'sea' | intervocalic voicing weaker/more conservative; delivery often perceived as firmer/more tensed — 고기 [ko.ɡi]~[ko.ki] 'meat', 바다 [pa.da]~[pa.ta] 'sea' | 고기 'meat': South [ko.ɡi] (clear voiced [ɡ]) — North [ko.ɡi]~[ko.ki] (weaker voicing); 어디 'where': South [ʌ.di] — North [ɔ.di]~[ɔ.ti]; 부모 'parents': South [pu.mo] — North [pu.mo] (more uniform tension reported) | Both standards share the signature three-way laryngeal contrast (lenis `ㄱㄷㅂㅈ`, tense `ㄲㄸㅃㅉㅆ`, aspirated `ㅋㅌㅍㅊ`) with no phonemic voicing. The divergence is allophonic and gradient: Seoul lenis stops voice robustly between voiced segments ([ko.ɡi], [pa.da]), and Seoul is undergoing a tonogenetic restructuring in which the onset's laryngeal class (lenis vs aspirate/tense), rather than VOT alone, increasingly cues the pitch of the following vowel. Northern speech is reported as more conservative in intervocalic voicing and is often perceived as firmer or more strongly articulated. None of this is phonemic: it is realization and prosodic implementation, not a difference in the inventory. |
| `ㄹ` in loanwords and Sino-Korean medials | follows 외래어 표기법; medial `ㄹ` patterns per Seoul norms — 라디오 /ɾa.ti.o/ 'radio', 텔레비전 /tʰel.le.pi.tɕʌn/ 'television' | loan `ㄹ` kept initially too (no 두음법칙 even in loans); different loan shapes — 라지오 /ɾa.tɕi.o/ 'radio', 텔레비죤 /tʰel.le.pi.tɕjon/ | 'radio': South 라디오 (radio) /ɾa.ti.o/ — North 라지오 (rajio) /ɾa.tɕi.o/; 'television': South 텔레비전 (tellebijeon) /tʰel.le.pi.tɕʌn/ — North 텔레비죤 (tellebijyon) /tʰel.le.pi.tɕjon/; 'Russia': South 러시아 (Reosia) /ɾʌ.ɕi.a/ — North 로씨야 (Rossiya) /ɾo.s͈i.ja/ | Because the North does not apply 두음법칙, loanwords that begin with an [r]/[l] sound keep a written word-initial `ㄹ` in both standards (Western loans are exempt from the rule even in the South: 라디오, 러시아), but the two diverge in the precise Hangul shaping of the loan: South 라디오 vs North 라지오, South 텔레비전 vs North 텔레비죤 (the North preserving the `ㅈ` + glide spelling 죤), and country names routed differently (South 러시아 from English 'Russia' vs North 로씨야 from Russian Росси́я, with a tense `ㅆ`). The phoneme /l~ɾ/ behaves identically inside words in both standards ([ɾ] as an intervocalic onset, [l] in coda and in geminate `ㄹㄹ`); the differences are in loan adaptation policy and orthography, not in the liquid's phonology. |

Standard South Korean (표준어, Seoul) and North Korean (문화어, Pyongyang) differ most consequentially in (1) the 두음법칙 (initial-sound rule), the South changing word-initial `ㄹ` → `ㄴ` → `∅` and `ㄴ` → `∅` before /i, j/ in Sino-Korean roots (勞動 노동 vs 로동, 女子 여자 vs 녀자, 李氏 이씨 vs 리씨) while the North keeps the etymological `ㄹ`/`ㄴ` — by far the most frequent and recognizable split, surfacing especially in names (Lee 이 vs Ri 리); (2) lexicon and orthography, where North purism replaces loans with native 다듬은 말 (단물 for 주스, 얼음보숭이 for 아이스크림) and routes the loans it keeps differently (뜨락또르 from Russian vs 트랙터 from English; 로씨야 vs 러시아), alongside spacing and 사이시옷 spelling norms (나뭇잎 vs 나무잎); and (3) phonetic realization — the rounder, backer Pyongyang `ㅓ` ([ɔ] vs Seoul [ʌ]), the South-led 애/에 merger (개=게 [ke̞]), and gradient differences in lenis voicing and perceived tension. Crucially, BOTH reference standards are toneless and stressless: there is no pitch contrast between them. Lexical pitch (성조) lives only in the regional ASIDES — Gyeongsang (동남) and Hamgyŏng (북동) are true pitch-accent dialects — while Jeolla and Chungcheong differ mainly in morphology and intonation, and Jeju (제주어) stands apart as a critically endangered, often separately classified Koreanic variety that even preserves the lost arae-a vowel `ㆍ` /ɒ/.

### Asides: regional varieties (방언, bang-eon)

CLEARLY SECONDARY. The items below are regional varieties (방언, bang-eon) and a divergent sister variety, NOT part of the two reference standards above. They are documented as asides because the shipped Korean guide transcribes the two standards (표준어 and 문화어); regional dialects are mentioned for orientation only and are not the target of the four reader tiers.

#### Regional dialects

| Dialect | Key feature | IPA illustration | Explanation |
|---|---|---|---|
| 동남 방언 — Gyeongsang (Southeastern: Busan, Daegu, Ulsan) | LEXICAL PITCH-ACCENT (성조, seongjo) — the most salient aside | minimal sets distinguished only by pitch, e.g. 가가가 (variously 'is that person Ga?', 'take that thing', etc.) disambiguated by high/low patterns; 손 'hand' (H) vs 손 'guest' (L) | Unlike both Standard standards, which have NO lexical tone, Gyeongsang Korean is a genuine pitch-accent dialect: each word carries a lexically specified high/low melody, and minimal pairs differ in pitch alone. It is the textbook example of a tone-bearing Koreanic variety. Gyeongsang also tends to merge `ㅡ` /ɯ/ and `ㅓ` /ʌ/, and to simplify some onset glides. Pitch here is genuinely phonemic, the opposite of the toneless reference standards. |
| 서남 방언 — Jeolla (Southwestern: Gwangju, Jeonju) | distinctive sentence-final endings and vowel quality; NOT pitch-accent | characteristic endings such as -잉 [-iŋ], -으라우, and a generally lowered/centralized vowel set; 거시기 [kʌ.ɕi.ɡi] as an all-purpose placeholder | Jeolla is an intonation (non-tonal) dialect best known for its sentence-final particles and its warm, drawled prosody rather than for lexical pitch. Some vowel mergers and consonant lenition occur, but the system is structurally close to the Seoul standard apart from morphology and intonation. |
| 중부 방언 (충청) — Chungcheong (Central: Daejeon, Cheongju) | slow, drawled tempo and lengthened/glided vowels; closest to the Seoul standard | vowel lengthening and gentle diphthongization, e.g. 그래유 [kɯ.ɾɛː.ju] for standard 그래요 'that's right', with the characteristic -유 [-ju] ending | Chungcheong is part of the central dialect zone and is the regional variety closest to 표준어. Its hallmarks are a markedly unhurried tempo, vowel lengthening, and the soft sentence-final -유 in place of standard -요. There is no lexical tone; the differences are prosodic and morphological. |
| 북동 방언 — Hamgyŏng (Northeastern North Korea, and Korean-Chinese 조선족 areas) | LEXICAL PITCH-ACCENT — the northern counterpart to Gyeongsang | high/low lexical melodies on words paralleling the Gyeongsang system; conservative retention of some older vowel distinctions | Hamgyŏng is the second major pitch-accent zone of Koreanic, the northeastern mirror of Gyeongsang and likewise outside both toneless reference standards. It preserves lexical pitch and several conservative phonological features and underlies much of the Koryo-saram (Central Asian) and Yanbian Korean-Chinese speech. Like Gyeongsang, its pitch is phonemic — a sharp contrast with 문화어, the Pyongyang standard, which is toneless. |

#### 제주어 / 제주말 — Jeju (Jejueo)

- **Status:** Deeply divergent variety, often classified as a SEPARATE KOREANIC LANGUAGE; UNESCO-listed as critically endangered (2010).
- **Key feature:** low mutual intelligibility with mainland Korean; conservative phonology + heavy morphological divergence.
- **IPA illustration:** retains the historic 'arae-a' vowel `ㆍ` /ɒ/ (lost on the mainland), giving a ninth monophthong; distinctive verb endings and aspect markers; example: 혼저옵서예 [hon.dʑʌ.op̚.s͈ʌ.je] 'welcome / please come in', opaque to most mainland speakers.

Jeju is the most divergent Koreanic variety by far. It preserves the medieval vowel `ㆍ` (아래아, arae-a) /ɒ/ that merged away on the mainland centuries ago, keeps several archaic consonant and grammatical features, and has its own tense/aspect and sentence-ender morphology, yielding low mutual intelligibility with Seoul Korean — strong enough that many linguists treat it as a sister LANGUAGE within Koreanic rather than a dialect of Korean. It is critically endangered, with fluent speech now mostly among the elderly. It is well outside the scope of the two reference standards and is included here purely for orientation.

## Orthography: Hangul & Grapheme–Phoneme Correspondences

Korean is written in 한글 (Hangul), a **featural alphabet** created in 1443 (promulgated 1446 in the 훈민정음 Hunminjeongeum) — a unique writing system in which letter **shapes** iconically encode phonetic features rather than being arbitrary signs. Two facts make Hangul's grapheme-to-phoneme relationship unlike either deep English/French or shallow Spanish. **(1) Featural iconicity:** consonant letters depict the articulatory organ used to make the sound, and sounds that share a place/manner of articulation share a base shape, with extra strokes or doubling marking added features (aspiration, tenseness); vowel letters are composed from three cosmological strokes — heaven (`ㆍ`, a dot), earth (`ㅡ`, a horizontal line) and human (`ㅣ`, a vertical line). **(2) Morphophonemic spelling:** written forms preserve the underlying shape of each morpheme (the dictionary stem) rather than the surface pronunciation, so the reader must apply the language's phonological rules (연음 liaison, 음절의 끝소리 규칙 coda neutralization, 비음화 nasalization, 경음화 tensification, 격음화 aspiration, 구개음화 palatalization, etc.) to get from the spelled form to the spoken form. Thus the **spelling** direction (sound → written morpheme) is fairly determinate, but the **reading** direction (written form → surface phonemes) requires running the rule set — e.g. 꽃이 is read [꼬치] kkochi, 꽃 alone is read [꼳] kkot, and 꽃나무 is read [꼰나무] kkonnamu: one morpheme 꽃 /kkoch/ with three surface realizations.

Letters (자모 jamo) are not written in a linear string but are **packed into square syllable blocks** of the canonical shape (C)(G)V(C): an onset 초성 (choseong), a medial 중성 (jungseong = vowel ± glide) and an optional coda 종성 (jongseong = 받침 batchim). These blocks have precomposed Unicode codepoints generated by a fixed arithmetic formula. Two written standards are documented in parallel as the GA/RP analog: **Standard South Korean** (표준어, educated Seoul) and **North Korean** (문화어, Pyongyang); they share the same Hangul script and composition rules, diverging mainly in the 두음법칙 (initial-sound rule), a few spelling/spacing norms, and dictionary letter order.

### Reference Standards

| Label | Standard |
|---|---|
| South | 표준어 (pyojun-eo) — Standard South Korean, educated Seoul speech. Applies the 두음법칙 (initial-sound rule) in spelling AND pronunciation: word-initial `ㄹ` → `ㄴ` → ∅ and `ㄴ` → ∅ before i/j (女子 → 여자 yeoja, 勞動 → 노동 nodong, 理由 → 이유 iyu). Spelling is governed by 한글 맞춤법 (Hangul Orthography, 1988). The Peshitta Romanized tier uses Revised Romanization (RR, 2000), the official South Korean system. |
| North | 문화어 (munhwaeo) — North Korean standard, Pyongyang-based. Does NOT apply the 두음법칙: word-initial `ㄹ`/`ㄴ` are RETAINED in both spelling and speech (女子 → 녀자 nyeoja, 勞動 → 로동 rodong, 理由 → 리유 riyu). Slightly more conservative norms; uses McCune–Reischauer-style romanization conventions in some contexts and a different dictionary collation order for the jamo (the silent initial `ㅇ` placed last, and the tense consonants `ㄲ ㄸ ㅃ ㅆ ㅉ` ordered after the plain series rather than adjacent to their plain counterparts). Both standards use the identical Hangul alphabet and the same syllable-block arithmetic. |

### General Principles

Six organising principles govern how Hangul letters map to sounds.

- **Featural iconicity:** Hangul is the world's premier featural alphabet — letter shapes are not arbitrary but depict the articulator and encode phonetic features. The five basic consonant shapes are pictograms of the speech organs — `ㄱ` (back of tongue raised to the soft palate, velar), `ㄴ` (tongue tip at the alveolar ridge), `ㅁ` (the closed mouth/lips), `ㅅ` (the incisor teeth), `ㅇ` (the throat) — and additional strokes ADD features in a phonetically motivated way.
  - `ㄱ` /k/ + stroke → `ㅋ` /kʰ/ (aspiration added); doubled → `ㄲ` /k͈/ (tenseness added)
  - `ㄴ` /n/ + stroke → `ㄷ` /t/ (stop) + stroke → `ㅌ` /tʰ/ (aspirated); doubled `ㄸ` /t͈/ (tense)
  - `ㅁ` /m/ + strokes → `ㅂ` /p/ + stroke → `ㅍ` /pʰ/; doubled `ㅃ` /p͈/
  - `ㅅ` /s/ → `ㅈ` /tɕ/ → `ㅊ` /tɕʰ/; doubled `ㅆ` /s͈/, `ㅉ` /tɕ͈/ (sibilant family)
  - `ㅇ` (throat/null) related to `ㅎ` /h/ (with strokes) — laryngeal/glottal family
- **Vowel composition from three strokes:** Vowel letters are built from three cosmological primitives — heaven 하늘 = `ㆍ` (arae-a, a dot, now obsolete as an independent letter), earth 땅 = `ㅡ` (a horizontal line) and human 사람 = `ㅣ` (a vertical line). The dot attaches to the `ㅡ`/`ㅣ` axis to make the basic vowels, a second dot makes the y-glide (iotized) vowels, and `ㅗ`/`ㅜ`/`ㅏ`/`ㅓ` combine with `ㅣ` or with each other to form w-glide and complex vowels. The dot `ㆍ` has merged into `ㅏ`/`ㅡ` in modern Korean but its compositional logic still explains the shapes.
  - `ㅣ` (human) + dot to the right = `ㅏ` /a/; + dot to the left = `ㅓ` /ʌ/
  - `ㅡ` (earth) + dot above = `ㅗ` /o/; + dot below = `ㅜ` /u/
  - second dot (iotation) → `ㅑ` /ja/, `ㅕ` /jʌ/, `ㅛ` /jo/, `ㅠ` /ju/ (the y-series)
  - `ㅗ` + `ㅏ` = `ㅘ` /wa/; `ㅜ` + `ㅓ` = `ㅝ` /wʌ/; `ㅡ` + `ㅣ` = `ㅢ` /ɰi/ (w/ɰ-glide composites)
  - `ㅏ` + `ㅣ` = `ㅐ` /ɛ/; `ㅓ` + `ㅣ` = `ㅔ` /e/; `ㅗ` + `ㅣ` = `ㅚ` /ø/; `ㅜ` + `ㅣ` = `ㅟ` /y/
- **Morphophonemic spelling:** Korean orthography (한글 맞춤법) is morphophonemic, not phonetic — it spells each morpheme with a fixed, recoverable shape (the underlying form) so that the visual identity of stems and affixes is preserved across the alternations caused by phonology. The reader must apply the rule set to recover the surface pronunciation. This is the single biggest source of read-direction non-determinism — the opposite of Spanish's shallow read-off.
  - 꽃 'flower' is spelled with stem-final `ㅊ` in every form, but surfaces differently: 꽃이 [꼬치] kkochi (liaison, `ㅊ` keeps its value before a vowel), 꽃 [꼳] kkot (coda neutralization to [t]), 꽃나무 [꼰나무] kkonnamu (neutralized [t] then nasalized to [n] before `ㄴ`)
  - 값 'price' (stem-final cluster `ㅄ`): 값이 [갑씨] gapsi (liaison + tensification, but RR does not separately mark rule-derived tensification, so the readback stays single-s), 값 [갑] gap (cluster simplifies to [p]), 값도 [갑또] gapdo (tensification)
  - 먹다 'to eat' stem 먹-: 먹어 [머거] meogeo (liaison), 먹는 [멍는] meongneun (nasalization), 먹고 [먹꼬] meokkko (tensification) — one written stem, three surface onsets/codas
  - 같이 'together' spelled with `ㅌ` + 이 but read [가치] gachi (구개음화 palatalization `ㅌ` + i → [tɕʰ])
- **Syllable-block packing:** Unlike linearly written alphabets, Hangul packs jamo into square syllable blocks, the canonical unit (C)(G)V(C). Each block has one onset (초성 choseong), one medial (중성 jungseong, a vowel possibly with a glide), and an optional coda (종성 jongseong / 받침 batchim). The arrangement inside the block depends on whether the vowel is vertical (onset left, vowel right: 가), horizontal (onset top, vowel bottom: 구), or mixed (와), with the coda always on the bottom. There are NO onset clusters and at most one written coda slot (which may itself hold a two-jamo cluster).
  - 한 = `ㅎ` (onset) + `ㅏ` (medial) + `ㄴ` (coda), packed onset-left/vowel-right/coda-bottom
  - 국 = `ㄱ` + `ㅜ` + `ㄱ`, packed onset-top/vowel-middle/coda-bottom (horizontal vowel)
  - 글 = `ㄱ` + `ㅡ` + `ㄹ`; 와 = `ㅇ`(null) + `ㅘ`; 닭 = `ㄷ` + `ㅏ` + `ㄺ` (cluster coda)
  - A vowel-initial syllable still fills the onset slot with the silent placeholder `ㅇ`: 아 = `ㅇ` + `ㅏ`, 이 = `ㅇ` + `ㅣ`
- **Coda neutralization and cluster simplification:** Although 27 different jongseong (single and cluster) can be written, the spoken coda neutralizes to only **seven** sounds [k t p l m n ŋ] (음절의 끝소리 규칙), and two-jamo cluster codas simplify so that only one consonant is pronounced when no vowel follows. This is a read-direction rule with no spelling counterpart: the written coda preserves the morpheme; the spoken coda is one of seven.
  - `ㄷ ㅅ ㅆ ㅈ ㅊ ㅌ ㅎ` all neutralize to [t] in coda: 낫/낮/낯/낟 all = [낟] nat; 옷 [옫] ot
  - `ㄱ ㄲ ㅋ` → [k] (부엌 [부억] bueok); `ㅂ ㅍ` → [p] (앞 [압] ap)
  - `ㄺ` → [k] (닭 [닥] dak); `ㄼ` → [l] (여덟 [여덜] yeodeol); `ㄻ` → [m] (삶 [삼] sam); `ㄳ` → [k]; `ㄵ` → [n]; `ㅄ` → [p]
  - but the dropped jamo REAPPEARS before a vowel via liaison: 닭이 [달기] dalgi, 값을 [갑쓸] gapseul
- **No lexical tone/stress in script:** Hangul marks NO suprasegmentals — there is no lexical tone or stress sign in modern orthography (Standard Korean has neither). Pitch and phrasing are organized at the accentual-phrase level and are not written. (The 15th-century 훈민정음 used left-margin dots 방점 to mark Middle Korean tone, but these were abandoned by the 16th–17th centuries.)
  - 눈 can be 'eye' or 'snow' (a vowel-length minimal pair in conservative speech) — spelling is identical, no diacritic distinguishes them
  - Spacing (띄어쓰기) marks word/phrase boundaries but not prosody
  - No accent mark ever changes a vowel's quality (contrast the Spanish acute or French accents)

### Jamo Inventory

The 자모 (jamo) are the atomic letters of Hangul, classified by the slot they fill in a syllable block: 초성 choseong (onset consonants), 중성 jungseong (medial vowels / glide + vowel) and 종성 jongseong (coda consonants, 받침). Modern Hangul uses **19 onset consonants, 21 medials and 27 codas** (plus the empty coda). The same shape may serve in more than one slot (e.g. `ㄱ` is both an onset and a coda), but Unicode treats onset and coda jamo as distinct conjoining characters. Standalone teaching/keyboard letters live in the Hangul Compatibility Jamo block (`U+3130–U+318F`); the conjoining forms used inside blocks live in `U+1100–U+11FF`.

#### Basic Consonant Letters (plain / lax series)

| Jamo | Name (South) | Name (North) | IPA | Feature | As coda |
|---|---|---|---|---|---|
| `ㄱ` | 기역 | 기윽 | /k/ (onset, voiced [ɡ] intervocalically) | plain/lax velar stop; base shape of the velar family | [k] |
| `ㄴ` | 니은 | 니은 | /n/ | alveolar nasal; base shape of the alveolar family | [n] |
| `ㄷ` | 디귿 | 디읃 | /t/ (voiced [d] intervocalically) | plain/lax alveolar stop (`ㄴ` + stroke) | [t] |
| `ㄹ` | 리을 | 리을 | /l ~ ɾ/ | liquid: tap [ɾ] as intervocalic onset, lateral [l] in coda and geminate `ㄹㄹ` | [l] |
| `ㅁ` | 미음 | 미음 | /m/ | bilabial nasal; base shape of the labial family (the closed mouth) | [m] |
| `ㅂ` | 비읍 | 비읍 | /p/ (voiced [b] intervocalically) | plain/lax bilabial stop (`ㅁ` + strokes) | [p] |
| `ㅅ` | 시옷 | 시읏 | /s/ (→ [ɕ] before /i/ or /j/) | alveolar fricative; base shape of the sibilant family (the teeth) | [t] |
| `ㅇ` | 이응 | 이응 | onset: silent placeholder ∅ ; coda: /ŋ/ | throat/null; carries a vowel-initial syllable as a placeholder, and is the velar nasal only as a coda | [ŋ] |
| `ㅈ` | 지읒 | 지읒 | /tɕ/ (voiced [dʑ] intervocalically) | plain/lax alveolo-palatal affricate (sibilant family, `ㅅ`-based) | [t] |
| `ㅊ` | 치읓 | 치읓 | /tɕʰ/ | aspirated affricate (`ㅈ` + stroke) | [t] |
| `ㅋ` | 키읔 | 키읔 | /kʰ/ | aspirated velar stop (`ㄱ` + stroke) | [k] |
| `ㅌ` | 티읕 | 티읕 | /tʰ/ | aspirated alveolar stop (`ㄷ` + stroke) | [t] |
| `ㅍ` | 피읖 | 피읖 | /pʰ/ | aspirated bilabial stop (`ㅂ` + strokes) | [p] |
| `ㅎ` | 히읗 | 히읗 | /h/ | glottal fricative; laryngeal family (`ㅇ` + strokes) | [t] (neutralized) / triggers 격음화 aspiration on an adjacent stop |

#### Tense (Fortis) Consonant Letters

| Jamo | Name (South) | Name (North) | IPA | Feature | As coda |
|---|---|---|---|---|---|
| `ㄲ` | 쌍기역 | 된기윽 | /k͈/ | tense (fortis) velar stop — doubled `ㄱ`; tense marker = `U+0348` combining double vertical line below | [k] |
| `ㄸ` | 쌍디귿 | 된디읃 | /t͈/ | tense alveolar stop — doubled `ㄷ`; onset only (never a coda) | n/a |
| `ㅃ` | 쌍비읍 | 된비읍 | /p͈/ | tense bilabial stop — doubled `ㅂ`; onset only | n/a |
| `ㅆ` | 쌍시옷 | 된시읏 | /s͈/ | tense alveolar fricative — doubled `ㅅ` | [t] |
| `ㅉ` | 쌍지읒 | 된지읒 | /tɕ͈/ | tense affricate — doubled `ㅈ`; onset only | n/a |

#### Basic Vowel Letters

| Jamo | IPA | Composition | Type |
|---|---|---|---|
| `ㅏ` | /a/ | `ㅣ` (human) + dot right | monophthong |
| `ㅓ` | /ʌ/ | `ㅣ` (human) + dot left | monophthong |
| `ㅗ` | /o/ | `ㅡ` (earth) + dot above | monophthong |
| `ㅜ` | /u/ | `ㅡ` (earth) + dot below | monophthong |
| `ㅡ` | /ɯ/ | earth (the horizontal line itself) | monophthong |
| `ㅣ` | /i/ | human (the vertical line itself) | monophthong |
| `ㅐ` | /ɛ/ (merged to [e̞] for most young Seoul speakers — the 애/에 merger) | `ㅏ` + `ㅣ` | monophthong |
| `ㅔ` | /e/ (merged to [e̞] for most young Seoul speakers) | `ㅓ` + `ㅣ` | monophthong |
| `ㅚ` | /ø/ (conservative); usually diphthongized to [we] | `ㅗ` + `ㅣ` | front rounded monophthong / diphthong |
| `ㅟ` | /y/ (conservative); usually diphthongized to [wi] | `ㅜ` + `ㅣ` | front rounded monophthong / diphthong |

#### Glide Vowel Letters (y- and w-series)

| Jamo | IPA | Composition | Glide |
|---|---|---|---|
| `ㅑ` | /ja/ | `ㅏ` + second dot (iotation) | j |
| `ㅒ` | /jɛ/ | `ㅐ` + iotation | j |
| `ㅕ` | /jʌ/ | `ㅓ` + iotation | j |
| `ㅖ` | /je/ | `ㅔ` + iotation | j |
| `ㅛ` | /jo/ | `ㅗ` + iotation | j |
| `ㅠ` | /ju/ | `ㅜ` + iotation | j |
| `ㅘ` | /wa/ | `ㅗ` + `ㅏ` | w |
| `ㅙ` | /wɛ/ | `ㅗ` + `ㅐ` | w |
| `ㅝ` | /wʌ/ | `ㅜ` + `ㅓ` | w |
| `ㅞ` | /we/ | `ㅜ` + `ㅔ` | w |
| `ㅢ` | /ɰi/ | `ㅡ` + `ㅣ` | ɰ |

*Note on `ㅢ`: realized [ɰi] word-initially, often [i] non-initially, and [e] in the genitive particle 의 [e].*

#### Coda (종성 / 받침) Inventory

The 종성 (jongseong / 받침) slot. **27 codas can be written** — 16 single jamo and 11 two-jamo clusters — but all neutralize to one of the seven coda sounds [k t p l m n ŋ] when no vowel follows. The cluster codas (`ㄳ ㄵ ㄶ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅄ`) drop one member in pronunciation but restore it via 연음 (liaison) before a vowel. `ㄸ`, `ㅃ`, `ㅉ` never occur as codas.

**Single codas (16):**

| Coda | Sound | Coda | Sound | Coda | Sound | Coda | Sound |
|---|---|---|---|---|---|---|---|
| `ㄱ` | [k] | `ㄲ` | [k] | `ㄴ` | [n] | `ㄷ` | [t] |
| `ㄹ` | [l] | `ㅁ` | [m] | `ㅂ` | [p] | `ㅅ` | [t] |
| `ㅆ` | [t] | `ㅇ` | [ŋ] | `ㅈ` | [t] | `ㅊ` | [t] |
| `ㅋ` | [k] | `ㅌ` | [t] | `ㅍ` | [p] | `ㅎ` | [t] |

**Cluster codas (11):**

| Cluster | Pronounced | Example |
|---|---|---|
| `ㄳ` | [k] | 몫 [목] mok |
| `ㄵ` | [n] | 앉다 [안따] antta |
| `ㄶ` | [n] | 많다 [만타] manta (`ㅎ` + `ㄷ` → aspirated `ㅌ`) |
| `ㄺ` | [k] | 닭 [닥] dak; before `ㄱ` → [l]: 읽고 [일꼬] ilkko |
| `ㄻ` | [m] | 삶 [삼] sam |
| `ㄼ` | [l] | 여덟 [여덜] yeodeol; but 밟다 [밥따] baptta is an exception ([p]) |
| `ㄽ` | [l] | 곬 [골] gol |
| `ㄾ` | [l] | 핥다 [할따] haltta |
| `ㄿ` | [p] | 읊다 [읍따] euptta |
| `ㅀ` | [l] | 싫다 [실타] silta (`ㅎ` + `ㄷ` → aspirated `ㅌ`) |
| `ㅄ` | [p] | 값 [갑] gap |

### Syllable-Block Composition

Hangul jamo compose into precomposed **syllable blocks** occupying the Unicode range `U+AC00–U+D7A3` (11,172 blocks = 19 onsets × 21 medials × 28 coda-slots, where coda-slot 0 = no coda). Each block is a single codepoint computed by a fixed arithmetic formula from the indices of its three jamo. The Hangul Jamo block `U+1100–U+11FF` holds the conjoining jamo used by the algorithm; the Hangul Compatibility Jamo block `U+3130–U+318F` holds standalone forms used for teaching and keyboard labels.

**Formula:**

```
syllable_codepoint = 0xAC00 + (choseong_index × 588) + (jungseong_index × 28) + jongseong_index
```

**Constants:**

| Constant | Value |
|---|---|
| S_base | `0xAC00` (44032) — first syllable 가 |
| choseong_count | 19 |
| jungseong_count | 21 |
| jongseong_count | 28 |
| choseong_stride | 588 |
| jungseong_stride | 28 |

*Note: 588 = 21 × 28 (medials × coda-slots); coda-slot index 0 means no coda.*

#### Index Orders

Choseong indices 0–18, jungseong indices 0–20, jongseong indices 0–27. The choseong/jongseong orders differ: choseong has no empty slot and excludes the cluster codas; jongseong begins with `(none)` and includes the 11 clusters but excludes `ㄸ ㅃ ㅉ`.

**Choseong (onset) order — indices 0–18:**

| Idx | Jamo | Idx | Jamo | Idx | Jamo | Idx | Jamo |
|---|---|---|---|---|---|---|---|
| 0 | `ㄱ` | 5 | `ㄹ` | 10 | `ㅆ` | 15 | `ㅋ` |
| 1 | `ㄲ` | 6 | `ㅁ` | 11 | `ㅇ` | 16 | `ㅌ` |
| 2 | `ㄴ` | 7 | `ㅂ` | 12 | `ㅈ` | 17 | `ㅍ` |
| 3 | `ㄷ` | 8 | `ㅃ` | 13 | `ㅉ` | 18 | `ㅎ` |
| 4 | `ㄸ` | 9 | `ㅅ` | 14 | `ㅊ` |  |  |

**Jungseong (medial) order — indices 0–20:**

| Idx | Jamo | Idx | Jamo | Idx | Jamo |
|---|---|---|---|---|---|
| 0 | `ㅏ` | 7 | `ㅖ` | 14 | `ㅝ` |
| 1 | `ㅐ` | 8 | `ㅗ` | 15 | `ㅞ` |
| 2 | `ㅑ` | 9 | `ㅘ` | 16 | `ㅟ` |
| 3 | `ㅒ` | 10 | `ㅙ` | 17 | `ㅠ` |
| 4 | `ㅓ` | 11 | `ㅚ` | 18 | `ㅡ` |
| 5 | `ㅔ` | 12 | `ㅛ` | 19 | `ㅢ` |
| 6 | `ㅕ` | 13 | `ㅜ` | 20 | `ㅣ` |

**Jongseong (coda) order — indices 0–27:**

| Idx | Jamo | Idx | Jamo | Idx | Jamo | Idx | Jamo |
|---|---|---|---|---|---|---|---|
| 0 | (none) | 7 | `ㄷ` | 14 | `ㄿ` | 21 | `ㅇ` |
| 1 | `ㄱ` | 8 | `ㄹ` | 15 | `ㅀ` | 22 | `ㅈ` |
| 2 | `ㄲ` | 9 | `ㄺ` | 16 | `ㅁ` | 23 | `ㅊ` |
| 3 | `ㄳ` | 10 | `ㄻ` | 17 | `ㅂ` | 24 | `ㅋ` |
| 4 | `ㄴ` | 11 | `ㄼ` | 18 | `ㅄ` | 25 | `ㅌ` |
| 5 | `ㄵ` | 12 | `ㄽ` | 19 | `ㅅ` | 26 | `ㅍ` |
| 6 | `ㄶ` | 13 | `ㄾ` | 20 | `ㅆ` | 27 | `ㅎ` |

#### Worked Examples

| Block | Decomposition | Calculation | Reading |
|---|---|---|---|
| 가 | `ㄱ`(0) + `ㅏ`(0) + ∅(0) | `0xAC00 + 0×588 + 0×28 + 0 = 0xAC00` (44032) | ga |
| 한 | `ㅎ`(18) + `ㅏ`(0) + `ㄴ`(4) | `44032 + 18×588 + 0×28 + 4 = 54620 = U+D55C` | han |
| 글 | `ㄱ`(0) + `ㅡ`(18) + `ㄹ`(8) | `44032 + 0×588 + 18×28 + 8 = 44544 = U+AE00` | geul |
| 닭 | `ㄷ`(3) + `ㅏ`(0) + `ㄺ`(9) | `44032 + 3×588 + 0×28 + 9 = 45805 = U+B2ED` | dak (cluster coda `ㄺ`) |
| 꽃 | `ㄲ`(1) + `ㅗ`(8) + `ㅊ`(23) | `44032 + 1×588 + 8×28 + 23 = 44867 = U+AF43` | kkot (spelled with `ㅊ` coda) |

#### Inverse Decomposition

To split a precomposed block `S` back into jamo indices:

```
offset           = S − 0xAC00
jongseong_index  = offset mod 28
jungseong_index  = (offset ÷ 28) mod 21
choseong_index   = offset ÷ 588        (integer division)
```

### Morphophonemic Spelling

The governing principle of Korean orthography: **spell the morpheme, not the sound.** A stem or affix keeps one constant written shape so its identity is visible across all the surface alternations triggered by phonology. Reading aloud therefore means restoring the underlying form and then applying the phonological rules (named in Hangul + English) to compute the surface phones. The worked sets below show one written morpheme yielding several pronunciations.

#### 꽃 'flower' — underlying /kkoch/, stem-final `ㅊ`

| Written | Surface | RR | Rules applied |
|---|---|---|---|
| 꽃이 | [꼬치] | kkochi | 연음 liaison — `ㅊ` moves to the onset of 이 and keeps its /tɕʰ/ value |
| 꽃 | [꼳] | kkot | 음절의 끝소리 규칙 coda neutralization — `ㅊ` → [t] in coda |
| 꽃나무 | [꼰나무] | kkonnamu | neutralization `ㅊ`→[t] then 비음화 nasalization [t]→[n] before `ㄴ` |
| 꽃밭 | [꼳빧] | kkotbat | neutralization ([t]) + 경음화 tensification (`ㅂ`→[p͈]) + neutralization of final `ㅌ`→[t] |

#### 값 'price' — underlying /kaps/, cluster coda `ㅄ`

| Written | Surface | RR | Rules applied |
|---|---|---|---|
| 값이 | [갑씨] | gapsi | 연음 liaison of `ㅅ` + 경음화 tensification (`ㅅ`→[s͈] after [p]); the surface is [갑씨], but RR does not separately mark rule-derived tensification (cf. siblings 값도 gapdo, 값을 gapseul, 꽃밭 kkotbat), so the RR readback is single-s gapsi |
| 값 | [갑] | gap | cluster simplification `ㅄ` → [p] |
| 값도 | [갑또] | gapdo | simplification ([p]) + 경음화 (`ㄷ`→[t͈]) |

#### 먹- 'eat' — underlying /mʌk/

| Written | Surface | RR | Rules applied |
|---|---|---|---|
| 먹어 | [머거] | meogeo | 연음 liaison; intervocalic `ㄱ` voices to [ɡ] |
| 먹는 | [멍는] | meongneun | 비음화 nasalization — [k]→[ŋ] before `ㄴ` |
| 먹고 | [먹꼬] | meokkko | 경음화 tensification — `ㄱ`→[k͈] after the obstruent coda [k] |

#### 같- 'be same' / 굳- 'harden' — stem-final `ㅌ` / `ㄷ` before i

| Written | Surface | RR | Rules applied |
|---|---|---|---|
| 같이 | [가치] | gachi | 구개음화 palatalization — `ㅌ` + 이 → [tɕʰ] |
| 굳이 | [구지] | guji | 구개음화 palatalization — `ㄷ` + 이 → [tɕ] |
| 해돋이 | [해도지] | haedoji | 구개음화 across a morpheme boundary (해돋- + -이) |

**Contrast note:** Because the spelling fixes the morpheme, Korean is fairly determinate in the **write** direction (a known morpheme has one spelling) but non-deterministic in the naive **read** direction (the same written block can surface differently depending on what follows). This is the inverse profile of shallow Spanish, where reading is deterministic but a few sounds have alternative spellings.

### Romanization (RR vs MR)

Korean is romanized in this guide by two reference systems documented in parallel: **Revised Romanization** (RR / 국어의 로마자 표기법), the official South Korean standard adopted in 2000, and **McCune–Reischauer** (MR), the older academic standard (1937, still common in libraries, North Korea variants, and pre-2000 scholarship). RR uses only plain ASCII letters; MR uses the breve diacritics ŏ ŭ and apostrophes to mark aspiration. The Korean Peshitta's Revised Romanization tier is a phonetic **readback** of the composed Hangul using RR rules, so it reflects the **surface** pronunciation (after the phonological rules apply), not the morphophonemic spelling.

#### Comparison Table

| Jamo | IPA | RR | MR | Note |
|---|---|---|---|---|
| `ㅓ` | /ʌ/ | eo | ŏ | RR digraph eo vs MR o-breve. e.g. 서울 RR Seoul, MR Sŏul |
| `ㅡ` | /ɯ/ | eu | ŭ | RR digraph eu vs MR u-breve. e.g. 음식 RR eumsik, MR ŭmsik |
| `ㅜ` | /u/ | u | u | Identical. |
| `ㅗ` | /o/ | o | o | Identical. |
| `ㅢ` | /ɰi/ | ui | ŭi | RR ui vs MR ŭi. |
| `ㅐ` | /ɛ/ | ae | ae | Identical. |
| `ㅔ` | /e/ | e | e | Identical; RR distinguishes 에 e from 애 ae. |
| `ㅚ` | /ø/~[we] | oe | oe | Identical. |
| `ㅟ` | /y/~[wi] | wi | wi | Identical. |
| `ㄱ` | /k/ ([ɡ] intervocalic) | g / k | k / g | RR: g initially/voiced, k in coda before consonant or word-final (강 gang, 국 guk). MR: k initially, g when voiced intervocalically (the inverse default). e.g. 부산 RR Busan, MR Pusan |
| `ㄷ` | /t/ ([d] intervocalic) | d / t | t / d | RR d initially/voiced, t in coda; MR t / voiced d. Parallels `ㄱ`. |
| `ㅂ` | /p/ ([b] intervocalic) | b / p | p / b | RR b initially/voiced, p in coda; MR p / voiced b. Parallels `ㄱ`. |
| `ㅈ` | /tɕ/ ([dʑ] intervocalic) | j | ch / j | RR always j; MR ch initially, j when voiced. e.g. 제주 RR Jeju, MR Cheju |
| `ㅊ` | /tɕʰ/ | ch | ch' | MR marks aspiration with an apostrophe; RR has no apostrophe (ch vs MR ch'). |
| `ㅋ` | /kʰ/ | k | k' | RR k vs MR k' — RR's coda `ㄱ` and onset `ㅋ` can both surface as k, MR keeps them distinct via the apostrophe. |
| `ㅌ` | /tʰ/ | t | t' | RR t vs MR t' (apostrophe = aspiration). |
| `ㅍ` | /pʰ/ | p | p' | RR p vs MR p'. |
| `ㄲ` | /k͈/ | kk | kk | Tense = doubled letter in both. |
| `ㄸ` | /t͈/ | tt | tt | Doubled. |
| `ㅃ` | /p͈/ | pp | pp | Doubled. |
| `ㅆ` | /s͈/ | ss | ss | Doubled. |
| `ㅉ` | /tɕ͈/ | jj | tch | RR jj vs MR tch. |
| `ㄹ` | /l ~ ɾ/ | r / l | r / l | Both: r as intervocalic onset (사랑 sarang), l in coda or geminate (서울 Seoul, 빨리 ppalli). |
| `ㅅ` | /s/ ([ɕ] before i/j) | s | s / sh | RR always s (시 si); MR may write sh before i (shi) in older practice. |
| `ㅎ` | /h/ | h | h | Identical. |
| `ㅇ` | onset ∅ / coda /ŋ/ | (silent) / ng | (silent) / ng | Onset placeholder is not romanized; coda = ng (강 gang). |

#### RR Rules Used for the Peshitta Tier

The Peshitta Romanized tier applies the official RR (2000) rules to the **composed Hangul**, reading off surface pronunciation. Key rules:

- Plain stops `ㄱ`/`ㄷ`/`ㅂ`/`ㅈ` = g/d/b/j before a vowel (and when voiced), but k/t/p in coda position before a consonant or at word-end: 한국 Hanguk, 받침 batchim, 밥 bap.
- Romanize the SOUND, so phonological changes ARE shown: assimilations are written. 신라 → [실라] → Silla (유음화 lateralization); 종로 → [종노] → Jongno (비음화); 좋고 → [조코] → joko (격음화 aspiration); 같이 → [가치] → gachi (구개음화).
- Tense consonants are doubled: `ㄲ` kk, `ㄸ` tt, `ㅃ` pp, `ㅆ` ss, `ㅉ` jj. (RR does NOT separately mark tensification that arises only from the rules unless it is lexicalized.)
- `ㄹㄹ` = ll (geminate lateral): 빨리 ppalli; intervocalic single `ㄹ` = r: 노래 norae.
- The vowels `ㅓ` = eo, `ㅡ` = eu, `ㅢ` = ui, `ㅐ` = ae, `ㅚ` = oe, `ㅟ` = wi; y-glides ya/yeo/yo/yu/yae/ye; w-glides wa/wae/wo/we.
- No apostrophes and no breves are used (the ASCII-only design); a hyphen may be inserted to avoid ambiguity (e.g. 중앙 jung-ang vs jun-gang).
- Proper-noun capitalization and given-name conventions follow RR; the Peshitta tier prioritizes consistent surface readback over name-style overrides.
- 두음법칙 (South) is reflected because the tier romanizes Standard South Korean surface forms: 이유 iyu, 여자 yeoja, 노동 nodong (a North-standard readback would give riyu, nyeoja, rodong).

### Reader Tiers

The Korean Peshitta ships **four** companion reader tiers; this orthography section underpins the two Korean-script-derived tiers.

| Tier | Description |
|---|---|
| Scholarly | language-neutral Latin transliteration |
| Pretty | simplified language-neutral Latin |
| Hangul | 한글 composed syllable blocks — the output of the composition formula in this section |
| Revised Romanization | RR readback of the Hangul — the output of the romanization rules in this section |

**Companion files:** `Korean/korean_pronunciation_guide.md`, `Korean/Peshita_Korean/Hangul/`, `Korean/Peshita_Korean/Romanized/`.

### Summary Notes

- Hangul is a **featural alphabet** — letter shapes encode articulatory features. Memorizing the five base consonant shapes (`ㄱ` velar, `ㄴ` alveolar, `ㅁ` labial, `ㅅ` sibilant, `ㅇ` laryngeal/null) plus the stroke-adding and doubling conventions yields the whole 19-consonant inventory; vowels follow from heaven (`ㆍ`), earth (`ㅡ`) and human (`ㅣ`) strokes.
- Korean spelling is **morphophonemic**: it preserves the dictionary shape of each morpheme rather than its surface sound, so reading aloud requires applying the phonological rules (연음, 음절의 끝소리 규칙, 비음화, 유음화, 경음화, 격음화, 구개음화, `ㄴ`-첨가). 꽃 alone is [꼳] but 꽃이 is [꼬치] and 꽃나무 is [꼰나무] — one spelling, three surface forms.
- Jamo pack into square **syllable blocks** of shape (C)(G)V(C): onset 초성, medial 중성, optional coda 종성/받침. There are no onset clusters; a vowel-initial syllable still fills the onset slot with the silent placeholder `ㅇ` (아, 이).
- Although 27 codas can be written, the spoken coda neutralizes to just **seven** sounds [k t p l m n ŋ], and two-jamo cluster codas drop one member — but the dropped jamo returns via 연음 (liaison) before a vowel (닭 [닥] but 닭이 [달기]).
- Precomposed syllable blocks live in Unicode `U+AC00–U+D7A3` (11,172 blocks) and are generated by `codepoint = 0xAC00 + (choseong×588) + (jungseong×28) + jongseong`, with choseong 0–18, jungseong 0–20, jongseong 0–27. Conjoining jamo are `U+1100–U+11FF`; standalone compatibility jamo are `U+3130–U+318F`.
- Two romanizations are documented: RR (official South Korea, 2000, ASCII-only: `ㅓ` eo, `ㅡ` eu, `ㅈ` j, no apostrophes) and MR (academic, with breves ŏ ŭ and aspiration apostrophes ch' k' t' p'). The Peshitta Romanized tier uses RR applied to the composed Hangul, reflecting surface pronunciation (신라 → Silla, 종로 → Jongno).
- The two written standards (South 표준어, North 문화어) share the identical Hangul script and syllable-block arithmetic; they diverge mainly in the 두음법칙 (initial-sound rule, applied in South spelling/speech but NOT in North — 여자/녀자, 노동/로동, 이유/리유), a few jamo names (기역/기윽), spacing/spelling norms, and dictionary collation order.
- Hangul marks **no suprasegmentals**: there is no lexical tone or stress, and no accent mark ever changes a vowel's quality. Prosody is organized at the accentual-phrase level and is not written. (Middle Korean tone dots 방점 were dropped by the 16th–17th centuries.)

---

*Korean Pronunciation Guide — Orthography section. Compiled by Shin.*

## Connected Speech & Sandhi

The segmental processes of connected (running) speech in Standard Korean, organised around its signature mechanism: pervasive, largely **obligatory across-boundary sandhi** (연접, *yeonjeop*). This is the Korean analog of the English guide's "Weak Forms & Connected Speech" slot and the Spanish guide's "Connected Speech & Sinalefa" slot, but the central mechanism is fundamentally different from English. English reshapes word boundaries by **reducing** unstressed function words to a schwa-centred "weak form"; Korean has **no weak forms, no vowel reduction, and no schwa** — every vowel keeps its full quality in every position (한국어에는 약형이 없다). Instead, Korean smooths the utterance by applying its rich battery of phonological rules **straight across morpheme, word, and phrase boundaries** as if the string were a single phonological word: liaison/resyllabification (연음), coda neutralisation (음절의 끝소리 규칙), nasalisation (비음화), lateralisation (유음화), tensification (경음화), aspiration/ㅎ-coalescence (격음화), palatalisation (구개음화), and ㄴ-insertion (ㄴ 첨가). Because Korean orthography is **morphophonemic** (it preserves underlying morpheme shape, not surface phonetics), the gap between the written 한글 string and the spoken IPA is large and is bridged almost entirely by these boundary sandhi rules. On top of the obligatory phrase-internal processes there is a separate, register-sensitive layer of **optional casual-speech contractions and clitic fusions** (거 < 것, 뭐 < 무엇, 게 < 것이) that behaves more like the gradient English processes.

**Applies to:** Spontaneous and fluent connected speech in both reference standards. The core grammatical sandhi rules (연음, 음절의 끝소리 규칙, 비음화, 유음화, 경음화, 격음화, 구개음화) are **not** optional reductions and **not** confined to fast casual speech: they are part of the prescriptive standard pronunciation (표준 발음법 / North 문화어 발음법) and apply already at careful, formal, read-aloud, and even citation tempos within a word, and across word boundaries inside an accentual/intonational phrase. They are suspended only across a genuine prosodic pause (the start of a new accentual phrase after a breath group, in dictation, or in deliberately syllable-by-syllable hyper-articulation). The **optional** layer — casual contractions (거, 뭐, 게), particle/ending cliticisation beyond the standard, and tempo-driven vowel/glide deletions — is gradient and register-dependent in the English manner: it increases with speed and informality and disappears in careful or honorific-formal delivery. Crucially, even at the fastest rate, no Korean vowel reduces to schwa or loses its quality the way an English weak-form vowel does.

### Reference Standards

| Standard | Description |
|---|---|
| **South (표준어, *pyojun-eo*)** | Educated Seoul speech, codified in 표준 발음법 (Standard Pronunciation Rules). Applies 두음법칙 (initial-sound rule) word-initially. Full obligatory sandhi set as described below. |
| **North (문화어, *munhwaeo*)** | Pyongyang-based standard, codified in 문화어 발음법. Does **not** apply 두음법칙 (retains word-initial `ㄹ`/`ㄴ`: 로동/녀자), is slightly more conservative in a few tensification and ㄴ-insertion environments, but shares the same general sandhi machinery (연음, 비음화, 유음화, 격음화, 구개음화). |

**No-reduction note:** There is **no schwa and no vowel reduction** in Korean. The monophthongs /a ʌ o u ɯ i e (ɛ)/ keep their full quality whether they fall in a prosodically prominent syllable or not, in citation and in the fastest connected speech alike. This is the single largest contrast with English connected speech: English collapses unstressed function words onto schwa /ə/, syllabic consonants, or zero, whereas Korean has no lexical stress to drive such reduction (Korean has **no lexical stress and no lexical tone**; prosody is organised in accentual phrases with a phrase tune, commonly LHLH). Korean grammatical function morphemes — case/topic particles (이/가, 을/를, 은/는, 에, 에서, 도, 만, 의), verbal endings (-고, -서, -니까, -습니다), and copula 이다 — are bound suffixes written attached to their host and pronounced with their **full vowels**; what changes across the seam between a stem and its particle/ending, or between two words inside a phrase, is the **consonants** (via the sandhi rules below) and **syllabification** (via 연음), never the vowel quality. The nearest Korean counterpart to the English strong-vs-weak alternation is the optional full-form↔contracted-form choice (것 vs 거, 무엇 vs 뭐), which is about morpheme shape and syllable count, not vowel reduction.

### Boundary Phenomena

The obligatory grammatical sandhi processes, each computed across morpheme, word, and phrase boundaries within an accentual phrase.

#### 연음 (liaison / resyllabification across a boundary)

**Category:** linking

When a syllable carrying a written coda (받침) is followed within the same phrase by a syllable beginning with the onset placeholder `ㅇ` (i.e. a vowel-initial syllable), the coda consonant moves to fill that empty onset, so the syllable boundary shifts **inside** the second syllable and the consonant is heard as belonging to it. This is the most pervasive Korean boundary process; combined with the morphophonemic spelling, it is the chief reason the spoken IPA diverges from the written 한글. It operates across stem→particle, stem→ending, and word→word seams alike.

- **Rules:** Coda C + onset `ㅇ`(∅) within a phrase → C re-syllabified as the next onset: C.∅V → .CV. Because the coda is **not** phrase-final and **not** followed by a consonant, it **escapes** coda neutralisation and surfaces with its full underlying value, including its lenis voicing intervocalically (`ㄱㄷㅂㅈ` → [ɡ d b dʑ]) and `ㄹ` → intervocalic flap [ɾ]. A double/cluster coda (겹받침) splits: the **first** consonant stays as the coda of syllable 1 and the **second** moves to onset syllable 2 (읽어 → [il.ɡʌ], 앉아 → [an.dʑa]). A coda `ㅇ` /ŋ/ does **not** move (it is a nasal, not a placeholder onset) — the following vowel keeps a zero onset. Coda `ㅎ` is deleted before a vowel (낳아 → [na.a]).
- **Notation:** `...C.∅V... → ...CV...` (coda C becomes the onset of the next syllable; `ㄱㄷㅂㅈ`→[ɡ d b dʑ], `ㄹ`→[ɾ] intervocalically; `ㅇ` does not move; `ㅎ`→∅)

| Hangul | RR | IPA | Note |
|---|---|---|---|
| 옷이 | osi | [o.ɕi] | stem 옷 (clothes) + subject particle 이; coda `ㅅ` /s/ re-syllabifies and, before /i/, surfaces as [ɕ]; it is **not** neutralised to [t] because it is not phrase-final |
| 꽃을 | kkocheul | [k͈o.tɕʰɯl] | 꽃 (flower) + object particle 을; underlying coda `ㅊ` /tɕʰ/ re-syllabifies fully as the onset [tɕʰ]; in isolation 꽃 alone is neutralised to [k͈ot̚] |
| 집에 | jibe | [tɕi.be] | 집 (house) + locative particle 에; lenis `ㅂ` /p/ re-syllabified intervocalically voices to [b] |
| 읽어요 | ilgeoyo | [il.ɡʌ.jo] | 겹받침 `ㄺ` splits: `ㄹ` stays as coda [l], `ㄱ` moves to the onset and voices to [ɡ] intervocalically |
| 밥을 먹어요 | babeul meogeoyo | [pa.bɯl mʌ.ɡʌ.jo] | across the stem→particle seam (밥+을) **and** the verb stem→ending seam (먹+어요); both lenis codas voice and re-syllabify; word-initial 밥 keeps voiceless [p] |

#### 음절의 끝소리 규칙 (coda neutralisation at a boundary)

**Category:** neutralisation

Any coda that is **not** re-syllabified onto a following vowel — i.e. one that stands before a consonant or before a prosodic pause/phrase edge — neutralises to one of just seven unreleased sounds [k̚ t̚ p̚ l m n ŋ]. At a word/phrase boundary this means a word-final coda is computed against whatever begins the next word, so the **same** word can show different surface codas depending on its neighbour. Cluster codas additionally simplify so that only one consonant is pronounced.

- **Rules:** Before a consonant or at a phrase edge: `ㄱㄲㅋ`(`ㄳㄺ`) → [k̚]; `ㄷㅌㅅㅆㅈㅊㅎ` → [t̚]; `ㅂㅍ`(`ㅄㄿ`) → [p̚]; `ㄴ`→[n], `ㅁ`→[m], `ㅇ`→[ŋ], `ㄹ`→[l]. Cluster codas drop one member by fixed rule (`ㄳ`→[k̚], `ㄵ`→[n], `ㄼ`→[l] but 밟다→[p̚], `ㄺ`→[k̚] by default but the `ㄹ` surfaces (→[l]) before a `ㄱ`-initial suffix in verb stems: 읽고→[il.k͈o], `ㄻ`→[m], `ㄿ`→[p̚], `ㅀ`→[l], `ㅄ`→[p̚]). This is the **feeding** input to nasalisation, lateralisation and tensification at the boundary: the obstruent is first neutralised, then triggers/undergoes the next rule.
- **Notation:** `coda /…/ → {[k̚ t̚ p̚] obstruents | [l m n ŋ] sonorants} / _ {C, ##}`

| Hangul | RR | IPA | Note |
|---|---|---|---|
| 옷 사세요 | ot saseyo | [ot̚ s͈a.se.jo] | 옷 (clothes) before a consonant-initial word: coda `ㅅ` /s/ neutralises to unreleased [t̚] (and triggers tensification of the following `ㅅ` → [s͈]) |
| 꽃 한 송이 | kkot han songi | [k͈o.tʰan soŋ.i] | 꽃 (flower) before `ㅎ`-initial 한: coda neutralises toward [t̚], then 격음화 with following `ㅎ` → [tʰ]; shows neutralisation feeding aspiration across the word boundary |
| 값 비싸요 | gap bissayo | [kap̚ p͈i.s͈a.jo] | cluster coda `ㅄ` simplifies to [p̚] before a consonant; the lenis `ㅂ` of 비 then tensifies → [p͈] |

#### 비음화 (nasalisation across a boundary)

**Category:** assimilation

A neutralised obstruent coda assimilates to a following nasal onset and itself becomes the homorganic nasal; additionally a following `ㄹ` becomes [n] after most obstruents and nasals. This is regressive (anticipatory) place/manner assimilation and applies straight across word and phrase boundaries inside an accentual phrase, not merely word-internally.

- **Rules:** (1) Obstruent → nasal before a nasal: [k̚]→[ŋ], [t̚]→[n], [p̚]→[m] / _ {`ㄴ` `ㅁ`}. (2) `ㄹ`-nasalisation: word-/morpheme-initial `ㄹ` → [n] after a coda that is an obstruent or nasal; if that coda is itself an obstruent it **also** nasalises, giving e.g. [k]+[l] → [ŋ]+[n] (백리 → [pɛŋ.ni]). Computed over the boundary, so the same final obstruent surfaces as a nasal only when the next word starts with a nasal.
- **Notation:** `[k̚ t̚ p̚] → [ŋ n m] / _ {ㄴ ㅁ}` ; `ㄹ → [n] / {obstruent, nasal}_` ; `obstruent+ㄹ → nasal+[n]`

| Hangul | RR | IPA | Note |
|---|---|---|---|
| 밥 먹어 | bap meogeo | [pam mʌ.ɡʌ] | across the word boundary: coda `ㅂ` → [p̚] → nasal [m] before `ㅁ` of 먹 |
| 한국 사람 | hanguk saram | [han.ɡuk̚ s͈a.ɾam] | no nasal trigger here (`ㅅ` follows), so the `ㄱ` does **not** nasalise — included to show nasalisation is conditioned by the following onset across the boundary |
| 몇 명 | myeot myeong | [mjʌn mjʌŋ] | 몇 (how many) coda `ㅊ` → [t̚] → [n] before `ㅁ`; classic counting phrase pronounced across the boundary |
| 십 리 | sip ri | [ɕim ni] | `ㄹ`-nasalisation feeding obstruent nasalisation: `ㅂ`+`ㄹ` → [m]+[n]; '10 li' |

#### 유음화 (lateralisation across a boundary)

**Category:** assimilation

An `ㄴ` that is adjacent to an `ㄹ` assimilates fully to [l], producing a geminate [ll] across the seam. It applies both progressively (`ㄹ`+`ㄴ`) and regressively (`ㄴ`+`ㄹ`) and reaches across word/morpheme boundaries within a phrase.

- **Rules:** `ㄴ` → [l] / `ㄹ`_ (progressive) and / _`ㄹ` (regressive); surface is geminate [l.l]. Note the lexical/structural exception class (e.g. 의견란, 생산량) where the `ㄴ`+`ㄹ` string instead undergoes `ㄹ`-nasalisation (→ [n.n]) — a Sino-Korean boundary effect — but the default at a native/phrasal boundary is lateralisation.
- **Notation:** `ㄴ → [l] / {ㄹ_ , _ㄹ}  →  surface [l.l]`

| Hangul | RR | IPA | Note |
|---|---|---|---|
| 신라 | silla | [ɕil.la] | regressive: `ㄴ`+`ㄹ` → [l.l]; the classic textbook case (Silla dynasty), boundary between two Sino-Korean morphemes |
| 한 리터 | han riteo | [hal li.tʰʌ] | across a word boundary: numeral 한 (one) + 리터 (litre); `ㄴ` → [l] before `ㄹ` → geminate [ll] |
| 줄넘기 | julleomgi | [tɕul.lʌm.ɡi] | progressive: `ㄹ`+`ㄴ` → [l.l] at the compound seam 줄(rope)+넘기(jumping) |

#### 경음화 (tensification / fortis at a boundary)

**Category:** assimilation

A lenis (plain) obstruent `ㄱㄷㅂㅅㅈ` becomes its tense (fortis) counterpart `ㄲㄸㅃㅆㅉ` after a neutralised obstruent coda, and in several morphologically defined environments. Across boundaries this makes the onset of a following word/morpheme fortis when the preceding word ends in an obstruent coda — a process with no surface trace in the morphophonemic spelling.

- **Rules:** (1) After an obstruent coda [k̚ t̚ p̚]: lenis `ㄱㄷㅂㅅㅈ` → tense `ㄲㄸㅃㅆㅉ` (obligatory, automatic). (2) After a sonorant coda `ㄴ`/`ㅁ` of certain **verb stems**: stem-final nasal + lenis suffix obstruent tensifies (안고 → [an.k͈o]). (3) After the prospective/adnominal ending -(으)ㄹ: following lenis obstruent tensifies (할 것 → [hal k͈ʌt̚]). (4) In many Sino-Korean and compound boundaries (사이시옷 environments). Tensification regularly **feeds off** coda neutralisation across the word seam.
- **Notation:** `lenis {ㄱㄷㅂㅅㅈ} → tense {ㄲㄸㅃㅆㅉ}([k͈ t͈ p͈ s͈ tɕ͈]) / {[k̚ t̚ p̚], certain nasal stems, -ㄹ}_`

| Hangul | RR | IPA | Note |
|---|---|---|---|
| 학교 | hakgyo | [hak̚.k͈jo] | obstruent coda [k̚] + lenis `ㄱ` → tense [k͈] at the morpheme seam 학(study)+교(school) |
| 옷 가게 | ot gage | [ot̚ k͈a.ɡe] | across a **word** boundary: 옷 (clothes) coda → [t̚], then 가게 (shop) onset `ㄱ` → tense [k͈]; the second `ㄱ` (intervocalic) stays lenis [ɡ] |
| 할 수 있다 | hal su itda | [hal s͈u it̚.t͈a] | post-(으)ㄹ tensification across the boundary: 할 (adnominal) + 수 → [s͈u]; inside 있다 coda [t̚]+`ㄷ` → [t͈] |
| 갈 데 | gal de | [kal t͈e] | the -ㄹ ending tensifies the following lenis `ㄷ` of the bound noun 데 (place) across the seam → [t͈] |

#### 격음화 (aspiration / ㅎ-coalescence across a boundary)

**Category:** coalescence

`ㅎ` and a plain stop **coalesce** into a single aspirated stop, whether the `ㅎ` precedes or follows the stop. Both segments are replaced by the one aspirated output (mutual coalescence, like English yod-coalescence in mechanism). Applies across morpheme and word boundaries; `ㅎ` is also weakened or deleted intervocalically and after sonorants.

- **Rules:** (1) `ㅎ` + {`ㄱㄷㅂㅈ`} → [kʰ tʰ pʰ tɕʰ] (progressive, `ㅎ` first): 좋고 → [tɕo.kʰo]. (2) {coda `ㄱㄷㅂㅈ` → neutralised obstruent} + `ㅎ` → [kʰ tʰ pʰ tɕʰ] (regressive, `ㅎ` second): 백화점 → [pɛ.kʰwa.dʑʌm], 못 하다 → [mo.tʰa.da]. (3) `ㅎ`-weakening/deletion: coda `ㅎ` deletes before a vowel (좋아 → [tɕo.a]) and intervocalic `ㅎ` is often weakened/dropped in fast speech.
- **Notation:** `ㅎ + {ㄱㄷㅂㅈ} ↔ {ㄱㄷㅂㅈ} + ㅎ → [kʰ tʰ pʰ tɕʰ]` ; `ㅎ → ∅ / V_V and / _V(coda)`

| Hangul | RR | IPA | Note |
|---|---|---|---|
| 못 해 | mot hae | [mo.tʰɛ] | across a word boundary: 못 (cannot) coda → [t̚] + `ㅎ` of 해 → coalesced aspirate [tʰ]; '(I) can't do (it)' |
| 좋고 | joko | [tɕo.kʰo] | stem-final `ㅎ` + ending `ㄱ` → [kʰ] (`ㅎ`-first coalescence) |
| 축하 | chuka | [tɕu.kʰa] | coda `ㄱ` + `ㅎ` → [kʰ] at the morpheme seam 축(celebrate)+하; 'congratulations' |
| 좋아요 | joayo | [tɕo.a.jo] | `ㅎ`-deletion: coda `ㅎ` deletes before the vowel of the ending → no aspiration; 'good / I like it' |

#### 구개음화 (palatalisation across a stem→suffix boundary)

**Category:** assimilation

A coda `ㄷ` or `ㅌ` becomes the palato-alveolar affricate [tɕ] or [tɕʰ] when the following morpheme begins with the vowel /i/ or the glide /j/ — almost always at the seam between a stem ending in `ㄷ`/`ㅌ` and a particle/suffix beginning 이/히/여. The coda does not merely re-syllabify; it changes place to palatal.

- **Rules:** `ㄷ` + 이 → [dʑi]~[tɕi] ; `ㅌ` + 이 → [tɕʰi] ; `ㄷ` + 히 → [tɕʰi] (`ㄷ`+`ㅎ`→`ㅌ` then palatalises). Triggered only by /i j/ across a **morpheme** boundary (it does not apply morpheme-internally, e.g. 잔디 stays [tɕan.di]). A boundary effect par excellence: the same stem-final `ㄷ`/`ㅌ` palatalises before 이 but re-syllabifies plainly before other vowels.
- **Notation:** `ㄷ → [dʑ/tɕ], ㅌ → [tɕʰ] / _ {이, 히, 여}` (at a stem→suffix boundary)

| Hangul | RR | IPA | Note |
|---|---|---|---|
| 굳이 | guji | [ku.dʑi] | stem 굳- + 이; coda `ㄷ` palatalises to [dʑ] before /i/ → 'firmly / insistently' |
| 같이 | gachi | [ka.tɕʰi] | stem 같- (coda `ㅌ`) + 이; `ㅌ` palatalises to [tɕʰ] before /i/ → 'together'; contrast plain re-syllabification in 같아 [ka.tʰa] |
| 굳히다 | guchida | [ku.tɕʰi.da] | `ㄷ` + 히: `ㄷ`+`ㅎ` coalesce to `ㅌ` which then palatalises before /i/ → [tɕʰi]; 'to harden' |

#### ㄴ 첨가 (n-insertion at a compound / phrase boundary)

**Category:** insertion

An [n] is inserted at a compound or phrase boundary when the **first** element ends in a consonant and the **second** element begins with the vowel /i/ or a /j/-glide (이 야 여 요 유 etc.). The inserted [n] then feeds further sandhi (it can nasalise a preceding obstruent or lateralise after `ㄹ`). This is the prototypical boundary-only process: it appears precisely **because** there is a morphological/word seam there.

- **Rules:** ∅ → [n] / C# _ {이, 야, 여, 요, 유, 얘, 예} at a compound or close phrase boundary, when the second element is an independent morpheme. The inserted [n] then triggers: (a) nasalisation of a preceding obstruent coda ([k̚]→[ŋ], [p̚]→[m]); (b) lateralisation if the preceding coda is `ㄹ` (`ㄹ` + inserted `ㄴ` → [l.l]). It is somewhat lexically variable and is one area where North/South and individual speakers differ; it does **not** apply at a stem→particle seam where plain 연음 is expected.
- **Notation:** `∅ → [n] / C# _ {이/j-vowel}` ; then `[k̚ p̚]→[ŋ m] / _[n]` ; `ㄹ#_[n] → [l.l]`

| Hangul | RR | IPA | Note |
|---|---|---|---|
| 한 일 | han il | [han nil] | the brief's headline case: 한 (one) + 일 (work/thing); [n] inserted before /i/ at the phrase boundary, giving geminate-feeling [han.nil] (contrast 연음-only 하닐 if no insertion) |
| 꽃잎 | kkonnip | [k͈on.nip̚] | compound 꽃(flower)+잎(leaf): [n] inserted before /i/, then coda `ㅊ`→[t̚]→nasalised [n] before the inserted [n] → [k͈on.nip̚]; 'petal' |
| 서울역 | seoullyeok | [sʌ.ul.ljʌk̚] | compound 서울+역(station): [n] inserted before /j/ then lateralised after `ㄹ` → [l.l]; 'Seoul Station' |
| 무슨 일 | museun il | [mu.sɯn nil] | across a phrase boundary 무슨 (what) + 일 (matter); the inserted [n] is variable here: in the `ㄴ`-inserting reading [mu.sɯn.nil], otherwise plain 연음 [mu.sɯ.nil]; 'what's the matter' (RR given spelling-based as *museun il*) |

#### 조사·어미 접어화 (particle / ending cliticisation)

**Category:** cliticisation

Korean grammatical particles (case, topic, and delimiter markers) and verbal endings are bound clitics written attached to their host word and pronounced as part of the same phonological word. They never carry independent prominence and they feed all the segmental sandhi above (연음, 경음화, etc.) across the host→clitic seam. Unlike English clitic auxiliaries (it's, they've), the Korean vowel is never reduced — only re-syllabification and consonant sandhi apply.

- **Rules:** Particles alternate their form by the host's final segment (allomorphy), not by reduction: subject 이/가, object 을/를, topic 은/는, instrumental 으로/로 select the consonant-vowel vs vowel-initial allomorph after a coda vs a vowel. The chosen allomorph then re-syllabifies (책+을 → [tɕʰɛ.ɡɯl]) or, if vowel-initial after a coda, pulls the coda onto itself. Endings behave likewise (먹+습니다 → nasalisation → [mʌk̚.s͈ɯm.ni.da]). The clitic is phonologically inseparable from the host within the accentual phrase.
- **Notation:** `host#clitic → single phonological word; allomorph selection by host-final segment; then 연음 / 경음화 / 비음화 apply across the seam`

| Hangul | RR | IPA | Note |
|---|---|---|---|
| 책을 | chaegeul | [tɕʰɛ.ɡɯl] | 책 (book) + object 을; lenis coda `ㄱ` re-syllabifies and voices to [ɡ]; full vowel /ɯ/ kept, no reduction |
| 꽃이 | kkochi | [k͈o.tɕʰi] | 꽃 + subject 이; the underlying `ㅊ` surfaces fully on the clitic onset, **not** the neutralised [t̚] of bare 꽃 |
| 먹습니다 | meokseumnida | [mʌk̚.s͈ɯm.ni.da] | stem 먹- + formal ending -습니다: tensification (`ㄱ`+`ㅅ`→[s͈]) and nasalisation (`ㅂ`→[m] before `ㄴ`) cascade across the stem→ending clitic seam; 'eats (formal)' |
| 집으로 | jibeuro | [tɕi.bɯ.ɾo] | 집 + directional 으로 (post-coda allomorph); coda `ㅂ` voices and re-syllabifies → [b]; `ㄹ` intervocalic flap [ɾ] |

#### 경어·어미 융합 (honorific / ending fusion and copula contraction)

**Category:** fusion

At the stem→ending seam, vowel-final stems and vowel-initial endings (and the honorific infix -(으)시-) **fuse**: identical or compatible vowels coalesce, and a stem-final high vowel/glide may merge with the ending into a diphthong or a single syllable. This is regular standard morphophonology, not casual slang, though some outputs have casual variants.

- **Rules:** (1) Identical-vowel coalescence: stem `ㅏ`/`ㅓ` + ending 아/어 → single long-ish vowel (가 + 아 → 가 [ka], 서 + 어 → 서 [sʌ]). (2) Glide fusion: stem `ㅗ`/`ㅜ` + 아/어 → `ㅘ`/`ㅝ` (오 + 아 → 와 [wa], 주 + 어 → 줘 [tɕwʌ]); stem `ㅣ` + 어 → `ㅕ` [jʌ] (기 + 어 → 겨). (3) Honorific -(으)시- + polite -어요 → -세요 [se.jo] (가시어요 → 가세요). (4) Copula 이다: vowel-final noun + 이에요 often → -예요 (친구이에요 → 친구예요 [tɕʰin.ɡu.je.jo]).
- **Notation:** `Vstem + Vending → coalesced V / glide+V` ; `-시-+-어요 → -세요` ; `N(V)+이에요 → -예요`

| Hangul | RR | IPA | Note |
|---|---|---|---|
| 봐요 | bwayo | [pwa.jo] | 보(see) + 아요 → 보+아 fuse to 와 [wa]; glide-fusion of stem `ㅗ` with ending `ㅏ`; 'look / see (polite)' |
| 가세요 | gaseyo | [ka.se.jo] | honorific fusion: 가 + -시- + -어요 → 가세요; '(please) go' |
| 줘 | jwo | [tɕwʌ] | 주(give) + 어 → 줘; stem `ㅜ` glides to [w] before the ending vowel `ㅓ` → single syllable [tɕwʌ] |
| 친구예요 | chinguyeyo | [tɕʰin.ɡu.je.jo] | copula contraction: 친구(friend) + 이에요 → 친구예요; '(it) is a friend' |

#### 구어 축약 (casual-speech contractions)

**Category:** contraction

The one Korean layer that behaves like the gradient, register-sensitive English processes: in casual/colloquial speech full forms contract to shorter forms by deleting or fusing segments and syllables. These are **optional**, scale with informality and speed, and are avoided in careful or honorific-formal registers — directly analogous to English weak/contracted forms (it's, gonna), though again driven by syllable/segment loss rather than vowel-quality reduction.

- **Rules:** Common patterns: (1) 것 → 거 (bound noun 'thing/fact'), and its case-marked fusions 것이 → 게, 것을 → 걸, 것은 → 건; (2) 무엇 → 뭐 → (further) 머; (3) 이것/그것/저것 → 이거/그거/저거; (4) topic/subject clitic + preceding vowel fusion (나는 → 난, 너는 → 넌, 나를 → 날); (5) 하- contractions (하여 → 해, -하지 않- → -찮-, 그렇지 → 그치); (6) ending fusions (-고 있어 → -고있어 → 'casual' -고써 in fast speech regionally). Reversible to the full form in careful speech.
- **Notation:** `것 → 거 [kʌ]` ; `것이 → 게 [ke]` ; `것을 → 걸 [kʌl]` ; `무엇 → 뭐 [mwʌ]` ; `나는 → 난 [nan]`

| Hangul | RR | IPA | Note |
|---|---|---|---|
| 이거 | igeo | [i.ɡʌ] | casual contraction of 이것 (this thing); full form 이것 [i.ɡʌt̚] in careful speech |
| 뭐 | mwo | [mwʌ] | casual contraction of 무엇 (what); 무엇 [mu.ʌt̚] → 뭐 [mwʌ], with further fast-speech [mʌ] |
| 갈 게 | gal ge | [kal k͈e] | 것이 → 게; '(I)'ll go'; the -ㄹ ending also tensifies the contracted 게 onset → [k͈e], showing casual contraction still feeds obligatory sandhi |
| 난 | nan | [nan] | 나는 (as-for-me) contracts to 난; clitic 는 fuses onto the pronoun without any vowel reduction of 나 |

### Interaction, Register & Dialect

**Process-ordering note:** These boundary processes feed one another in a cascade across a single accentual phrase. The usual ordering: (1) compute the underlying string with all particles/endings cliticised onto their hosts; (2) apply 연음 (resyllabification) wherever a coda meets a following vowel onset, which lets that coda **escape** neutralisation and surface fully (often voiced/flapped intervocalically); (3) on every coda that did **not** re-syllabify, apply 음절의 끝소리 규칙 (neutralisation to [k̚ t̚ p̚ l m n ŋ]) and cluster simplification; (4) on that neutralised string apply the assimilation/coalescence rules — 비음화, 유음화, 격음화, 경음화, 구개음화 — and any ㄴ 첨가, each computed over the **new** post-neutralisation context. This is why one word changes shape with its neighbour: 옷 is [ot̚] in isolation, [o.ɕi] before 이 (연음), [on] before a nasal (비음화), [ot̚ k͈…] before a lenis stop (neutralisation + 경음화). A single short phrase can show several at once: 못 잊어, in the `ㄴ`-inserting reading common in connected speech, → ㄴ-insertion (못_잊 → 못 닞) feeding obstruent neutralisation and nasalisation → [mon.ni.dʑʌ] (the more careful liaison reading [mo.di.dʑʌ]~[mo.t͈i.dʑʌ] also occurs); 같이 가요 → 구개음화 in 같이 [ka.tɕʰi] then 연음 across the boundary.

**Rate and register note:** Unlike English weak forms, the core Korean grammatical sandhi (연음, 음절의 끝소리 규칙, 비음화, 유음화, 경음화, 격음화, 구개음화) is **obligatory and prescriptive**: it operates already at careful, formal, read-aloud and even slow tempos and is required by Standard Pronunciation (표준 발음법 / 문화어 발음법) — failing to apply it sounds unnatural or like spelling-pronunciation, not merely 'careful'. What slow or hyper-articulate delivery removes is mainly the **optional** top layer: casual contractions (것→거, 무엇→뭐), extra fast-speech `ㅎ`-deletion and glide/vowel coalescence, and beyond-standard clusterings — these scale with speed and informality exactly like English connected-speech processes and disappear in formal/honorific registers. Citation/dictionary 한글 gives the morphophonemic underlying form; the IPA of running Korean requires the obligatory sandhi to be applied to sound native, and adds the optional contractions only in casual register. No amount of fast speech introduces schwa or vowel reduction.

**Dialect-variation note:** Standard South (표준어/Seoul) vs North (문화어/Pyongyang) divergences relevant to the boundary: (1) **두음법칙** (initial-sound rule) — South changes word-initial `ㄹ`→`ㄴ`→∅ and `ㄴ`→∅ before i/j (여자, 노동), which reshapes how an initial liquid behaves across a preceding boundary, whereas North **retains** initial `ㄹ`/`ㄴ` (녀자, 로동) so 유음화/비음화 across that seam differ; (2) **ㄴ 첨가** is somewhat more restricted and more lexically variable in the North standard and across individual speakers; (3) a few **경음화** environments (some Sino-Korean and compound 사이시옷 cases) are realised more conservatively in the North; (4) realisation details — the `ㅐ`/`ㅔ` merger and `ㅚ`/`ㅟ` diphthongisation are Seoul-progressive and feed glide-fusion outputs (와/워/예) slightly differently. Pitch-accent dialects (Gyeongsang 동남, Hamgyŏng 북동) keep lexical pitch and have their own phrase-tone realisations, but their segmental boundary sandhi is broadly the same as the standard; these are asides only — the obligatory sandhi set itself is shared nationwide.

**Contrast with English:** The defining contrast with the English "Weak Forms & Connected Speech" section: English connected speech is driven by **vowel reduction** — unstressed function words collapse onto schwa /ə/, syllabic consonants, or zero, and rhythm is stress-timed with strong↔weak form alternation. Korean has **no weak forms, no schwa, no vowel reduction, and no lexical stress** to motivate any; its function morphemes are bound clitics with full vowels. Where English bridges word boundaries by reducing vowels and inserting linking/intrusive-r and glides, Korean bridges them by applying a large set of **obligatory consonant-and-syllabification rules** across the seam (연음, 비음화, 유음화, 경음화, 격음화, 구개음화, ㄴ 첨가) on top of a morphophonemic orthography. The English strong-vs-weak distinction has essentially no Korean counterpart; its nearest analog is the **optional casual-contraction layer** (것→거, 무엇→뭐, 나는→난), which is about syllable/segment loss in informal register, not vowel quality. Net: English connected speech is a vowel-reduction system; Korean connected speech is a consonant-sandhi system.

**Cross-reference:** This section is the Korean counterpart to the English guide's "Weak Forms & Connected Speech" and the Spanish guide's "Connected Speech & Sinalefa." Unlike the English weak forms — which are gradient, optional, fast-speech vowel reductions — most of the Korean processes here are **obligatory**, phrase-internal grammatical sandhi prescribed by the Standard Pronunciation rules; only the final 구어 축약 (casual-speech contractions) layer is gradient and register-bound in the English manner. Read this section together with the Korean guide's *Phonological Rules* section (the same rule set documented word-internally), the *Syllable Structure & Batchim* section (the 7-sound coda neutralisation that feeds these boundary rules), the *Consonants* section (the 3-way lenis/tense/aspirated contrast and lenis intervocalic voicing that surface via 연음), and the *Vowels*/*Diphthongs* sections (full-quality vowels with no reduction; glide-fusion mechanism behind honorific/ending fusion). Where the English guide opposes GA vs RP (chiefly rhoticity) and the Spanish guide opposes Castilian vs Latin American (distinción/seseo), the Korean guide opposes South 표준어 vs North 문화어 (chiefly 두음법칙 and a few tensification/ㄴ-insertion environments). Companion materials: the four Korean Peshitta tiers (`Korean/Peshita_Korean/Scholarly/`, `Korean/Peshita_Korean/Pretty/`, `Korean/Peshita_Korean/Hangul/`, `Korean/Peshita_Korean/Romanized/`) and the prose guide `Korean/korean_pronunciation_guide.md` — the Hangul tier shows the morphophonemic spelling and the Romanized (RR) tier reads back the surface result of these sandhi rules.

---

*— Shin*

## Sample Words in IPA

32 illustrative Korean words transcribed in IPA for two reference standards — Standard South Korean (표준어 *pyojun-eo*, educated Seoul speech) and North Korean (문화어 *munhwaeo*, Pyongyang-based standard) — modeled on the English guide's parallel GA/RP columns, the Spanish guide's Castilian/Latin-American columns, and the Peshitta guide's parallel Eastern/Western tradition columns. The words are chosen to exercise the full segmental system: the complete 19-consonant inventory including the signature THREE-WAY laryngeal contrast (plain ~ tense ~ aspirated) in minimal sets, all 8 modern Seoul monophthongs plus the conservative front-rounded ㅚ/ㅟ, the principal /j/- and /w/-glide diphthongs and ㅢ /ɰi/, the 7-sound batchim (받침 coda) neutralization, cluster-coda simplification, and EVERY major phonological rule of Korean — 연음 liaison, 음절의 끝소리 규칙 coda neutralization, 비음화 nasalization, 유음화 lateralization, 경음화 tensification, 격음화 aspiration, 구개음화 palatalization, ㄴ-첨가 n-insertion, and the South-only 두음법칙 initial-sound rule. Each entry gives the word in Hangul (한글) with Revised Romanization (rr) and McCune–Reischauer (mr) readbacks, parallel South and North IPA, a gloss, the phonemes it illustrates, and the rules it illustrates, so the array as a whole forms a verifiable coverage matrix for the Korean phonological system. These map onto the four shipped reader tiers (Scholarly + Pretty Latin, 한글 Hangul blocks, and RR readback).

*Words were selected illustratively (not corpus-sliced) to guarantee complete coverage: collectively they realize all 19 consonant phonemes, instantiate the three-way laryngeal minimal sets (불 /pul/ ~ 뿔 /p͈ul/ ~ 풀 /pʰul/ for the bilabials; 달 /tal/ ~ 딸 /t͈al/ ~ 탈 /tʰal/ for the alveolars), supply each modern monophthong (ㅏㅓㅗㅜㅡㅣㅐㅔ) plus conservative ㅚ/ㅟ, demonstrate the main diphthongs and the unique ㅢ /ɰi/, exhibit the seven-way batchim neutralization and cluster-coda simplification (값 /kap̚/, 닭 /tak̚/, 앉다 /ant͈a/), and exemplify every named phonological rule with at least one keyword. South Korean and North Korean transcriptions are given in parallel; where the two standards diverge (overwhelmingly the 두음법칙 initial-sound rule, e.g. 여자/녀자, 노동/로동, 이름/리름, plus minor vowel realizations) both values are shown and the divergence is noted in the per-word gloss. The South/North 두음법칙 pairs (여자, 노동, 이발) are the explicit cross-standard contrast set.*

*The hallmark of Korean consonantism is a THREE-WAY laryngeal contrast among the stops and affricate — plain/lax (lenis) ㄱㄷㅂㅈ /k t p tɕ/, tense/fortis ㄲㄸㅃㅉ /k͈ t͈ p͈ tɕ͈/ (the tense diacritic is `U+0348` COMBINING DOUBLE VERTICAL LINE BELOW), and aspirated ㅋㅌㅍㅊ /kʰ tʰ pʰ tɕʰ/ — with NO phonemic voicing contrast. Voicing is purely ALLOPHONIC: a plain stop voices intervocalically, so ㄱ /k/ → [ɡ], ㄷ /t/ → [d], ㅂ /p/ → [b], ㅈ /tɕ/ → [dʑ] between voiced sounds, but is voiceless word-initially. Entries such as 바보 /pabo/ [pa.bo] ('fool', initial voiceless /p/, medial voiced [b]) and 고기 /kogi/ [ko.ɡi] ('meat') make this lenition explicit by transcribing the voiced allophones phonetically in [brackets] beside the phonemic /slashes/. This is the direct analog of Spanish spirantization or English aspiration as the language's signature allophonic process, and it is identical in both the South and North standards.*

**Total sample words:** 32

| Word | RR | MR | South 표준어 | North 문화어 | Gloss | Phonemes | Rules illustrated |
|---|---|---|---|---|---|---|---|
| 불 | `bul` | `pul` | `/pul/` | `/pul/` | 'fire' | /p/, /u/, /l/ | 삼지적 상관속 (three-way laryngeal contrast: plain member) |
| 뿔 | `ppul` | `ppul` | `/p͈ul/` | `/p͈ul/` | 'horn' | /p͈/, /u/, /l/ | 삼지적 상관속 (three-way laryngeal contrast: tense member) |
| 풀 | `pul` | `p'ul` | `/pʰul/` | `/pʰul/` | 'grass' | /pʰ/, /u/, /l/ | 삼지적 상관속 (three-way laryngeal contrast: aspirated member) |
| 달 | `dal` | `tal` | `/tal/` | `/tal/` | 'moon' | /t/, /a/, /l/ | 삼지적 상관속 (three-way laryngeal contrast: plain member) |
| 딸 | `ttal` | `ttal` | `/t͈al/` | `/t͈al/` | 'daughter' | /t͈/, /a/, /l/ | 삼지적 상관속 (three-way laryngeal contrast: tense member) |
| 탈 | `tal` | `t'al` | `/tʰal/` | `/tʰal/` | 'mask' | /tʰ/, /a/, /l/ | 삼지적 상관속 (three-way laryngeal contrast: aspirated member) |
| 감자 | `gamja` | `kamja` | `/kamtɕa/` | `/kamtɕa/` | 'potato' | /k/, /a/, /m/, /tɕ/ | 유성음화 (intervocalic voicing of plain obstruents) |
| 고기 | `gogi` | `kogi` | `/kogi/ [ko.ɡi]` | `/kogi/ [ko.ɡi]` | 'meat' | /k/, /o/, /i/ | 유성음화 (intervocalic voicing: ㄱ /k/ → [ɡ]) |
| 바보 | `babo` | `pabo` | `/pabo/ [pa.bo]` | `/pabo/ [pa.bo]` | 'fool' | /p/, /a/, /o/, [b] | 유성음화 (intervocalic voicing: ㅂ /p/ → [b]) |
| 아버지 | `abeoji` | `abŏji` | `/abʌtɕi/ [a.bʌ.dʑi]` | `/abʌtɕi/ [a.bʌ.dʑi]` | 'father' | /a/, [b], /ʌ/, /tɕ/, /i/ | 유성음화 (intervocalic voicing: ㅂ → [b], ㅈ /tɕ/ → [dʑ]) |
| 사람 | `saram` | `saram` | `/saɾam/` | `/saɾam/` | 'person' | /s/, /a/, /ɾ/, /m/ | ㄹ의 이음 (ㄹ realized as intervocalic tap [ɾ]) |
| 시간 | `sigan` | `sigan` | `/sigan/ [ɕi.ɡan]` | `/sigan/ [ɕi.ɡan]` | 'time, hour' | /s/, /i/, [ɡ], /a/, /n/ | ㅅ 구개음화 (ㅅ /s/ → [ɕ] before /i/, /j/); 유성음화 (ㄱ → [ɡ]) |
| 한국 | `hanguk` | `han'guk` | `/hanɡuk̚/` | `/hanɡuk̚/` | 'Korea (South Korean name, 韓國)' | /h/, /a/, /n/, [ɡ], /u/, /k/ | 음절의 끝소리 규칙 (coda neutralization: final ㄱ as unreleased [k̚]) |
| 꽃 | `kkot` | `kkot` | `/k͈ot̚/` | `/k͈ot̚/` | 'flower' | /k͈/, /o/, /t/ | 음절의 끝소리 규칙 (coda neutralization: ㅊ → [t̚]) |
| 부엌 | `bueok` | `puŏk` | `/puʌk̚/` | `/puʌk̚/` | 'kitchen' | /p/, /u/, /ʌ/, /k/ | 음절의 끝소리 규칙 (coda neutralization: ㅋ → [k̚]) |
| 값 | `gap` | `kap` | `/kap̚/` | `/kap̚/` | 'price, value' | /k/, /a/, /p/ | 자음군 단순화 (cluster-coda simplification: ㅄ → [p̚]); 음절의 끝소리 규칙 (coda neutralization) |
| 닭 | `dak` | `tak` | `/tak̚/` | `/tak̚/` | 'chicken' | /t/, /a/, /k/ | 자음군 단순화 (cluster-coda simplification: ㄺ → [k̚]) |
| 앉다 | `anda` | `antta` | `/ant͈a/ [an.t͈a]` | `/ant͈a/ [an.t͈a]` | 'to sit' (dictionary form) | /a/, /n/, /t͈/ | 자음군 단순화 (cluster-coda simplification: ㄵ → [n]); 경음화 (post-obstruent tensification: ㄷ → ㄸ) |
| 국물 | `gungmul` | `kungmul` | `/kuŋmul/` | `/kuŋmul/` | 'broth, soup' | /k/, /u/, /ŋ/, /m/, /l/ | 비음화 (nasalization: ㄱ /k/ → [ŋ] before nasal ㅁ) |
| 신라 | `Silla` | `Silla` | `/silla/` | `/silla/` | 'Silla' (ancient Korean kingdom, 新羅) | /s/, /i/, /l/ | 유음화 (lateralization: ㄴ + ㄹ → [ll]) |
| 좋다 | `jota` | `chot'a` | `/tɕotʰa/` | `/tɕotʰa/` | 'to be good' (dictionary form) | /tɕ/, /o/, /tʰ/, /a/ | 격음화 (aspiration: coda ㅎ + ㄷ → [tʰ]) |
| 축하 | `chukha` | `ch'ukha` | `/tɕʰukʰa/` | `/tɕʰukʰa/` | 'congratulation' | /tɕʰ/, /u/, /kʰ/, /a/ | 격음화 (aspiration: coda ㄱ + ㅎ → [kʰ]) |
| 같이 | `gachi` | `kach'i` | `/katɕʰi/` | `/katɕʰi/` | 'together' | /k/, /a/, /tɕʰ/, /i/ | 구개음화 (palatalization: ㅌ + i → [tɕʰ]); 연음 (liaison feeds the change) |
| 꽃잎 | `kkonnip` | `kkonnip` | `/k͈onnip̚/` | `/k͈onnip̚/` | 'flower petal' | /k͈/, /o/, /n/, /i/, /p/ | ㄴ-첨가 (n-insertion at compound boundary before i/j); 비음화 (ㅊ-coda → [n] before the inserted ㄴ); 음절의 끝소리 규칙 |
| 여자 | `yeoja` | `yŏja` | `/jʌdʑa/` | `/njʌdʑa/` | 'woman' (女子) | /j/, /ʌ/, /tɕ/, /a/ | 두음법칙 (initial-sound rule — South applies, North does not); 유성음화 (ㅈ → [dʑ]) |
| 노동 | `nodong` | `nodong` | `/nodoŋ/ [no.doŋ]` | `/lodoŋ/ [ɾo.doŋ]` | 'labor, work' (勞動) | /n/, /o/, [d], /ŋ/, /ɾ/ | 두음법칙 (initial-sound rule: South ㄹ→ㄴ; North keeps ㄹ); 유성음화 (ㄷ → [d]) |
| 이발 | `ibal` | `ibal` | `/ibal/ [i.bal]` | `/libal/ [ɾi.bal]` | 'haircut' (理髮) | /i/, [b], /a/, /l/ | 두음법칙 (initial-sound rule: South ㄹ→∅ before i; North keeps ㄹ) |
| 그릇 | `geureut` | `kŭrŭt` | `/kɯɾɯt̚/` | `/kɯɾɯt̚/` | 'bowl, dish' | /k/, /ɯ/, /ɾ/, /t/ | ㅡ 단모음 (bare monophthong ㅡ /ɯ/); 음절의 끝소리 규칙 (coda neutralization: ㅅ → [t̚]) |
| 의사 | `uisa` | `ŭisa` | `/ɰisa/` | `/ɰisa/` | 'doctor' (醫師) | /ɰ/, /i/, /s/, /a/ | ㅢ 실현 (realization of the diphthong ㅢ /ɰi/) |
| 회사 | `hoesa` | `hoesa` | `/høsa/ [hwe.sa]` | `/høsa/ [hø.sa]` | 'company, firm' (會社) | /h/, /ø/, /s/, /a/ | ㅚ 실현 (ㅚ /ø/ monophthong vs diphthongized [we]) |
| 위 | `wi` | `wi` | `/y/ [wi]` | `/y/ [wi]` | 'top, above' | /y/, /w/, /i/ | ㅟ 실현 (ㅟ /y/ monophthong vs diphthongized [wi]) |
| 왜 | `wae` | `wae` | `/wɛ/` | `/wɛ/` | 'why' | /w/, /ɛ/ | w-계 이중모음 (w-glide diphthong ㅙ /wɛ/); 애/에 합류 (ㅐ/ㅔ merger) |

### Per-Word Notes

- **불** `/pul/` — Identical in both standards. The PLAIN (lenis) bilabial member of the bilabial three-way minimal set 불 /pul/ ('fire') ~ 뿔 /p͈ul/ ('horn') ~ 풀 /pʰul/ ('grass'). Word-initial plain /p/ is voiceless [p] (it would voice to [b] only between voiced sounds). High back rounded vowel ㅜ /u/; coda ㄹ as [l].
- **뿔** `/p͈ul/` — Identical in both standards. The TENSE (fortis) member of the bilabial minimal set, contrasting with 불 /pul/ and 풀 /pʰul/. Tense ㅃ /p͈/ is articulated with a tensed glottis and no aspiration; the diacritic is `U+0348`. Confirms the lenis~fortis opposition that English and Spanish lack.
- **풀** `/pʰul/` — Identical in both standards. The ASPIRATED member of the bilabial minimal set. Note that rr collapses 불 and 풀 both to 'bul/pul'-shaped forms; mr distinguishes them with the apostrophe (p'ul) — a place where McCune–Reischauer encodes aspiration that Revised Romanization does not. Strong [pʰ] release.
- **달** `/tal/` — Identical in both standards. The PLAIN alveolar member of the alveolar three-way minimal set 달 /tal/ ('moon') ~ 딸 /t͈al/ ('daughter') ~ 탈 /tʰal/ ('mask'). Word-initial /t/ is voiceless [t]. Low vowel ㅏ /a/; coda ㄹ [l].
- **딸** `/t͈al/` — Identical in both standards. The TENSE alveolar member of the minimal set, contrasting with 달 /tal/ and 탈 /tʰal/. Tense ㄸ /t͈/ (diacritic `U+0348`).
- **탈** `/tʰal/` — Identical in both standards. The ASPIRATED alveolar member of the minimal set. Like the 불~풀 pair, mr (t'al) marks the aspiration that rr (tal) leaves ambiguous against 달.
- **감자** `/kamtɕa/` — Identical in both standards. Word-initial plain ㄱ /k/ is voiceless [k]; the plain affricate ㅈ /tɕ/ is here post-nasal. Demonstrates onset /k/ and the affricate /tɕ/; coda ㅁ /m/. Contrast with 고기 below for the intervocalic-voicing allophony of the plain series.
- **고기** `/kogi/ [ko.ɡi]` — Identical in both standards. The clearest minimal demonstration of plain-stop VOICING: the first ㄱ is word-initial voiceless [k], the second ㄱ is intervocalic voiced [ɡ] — [ko.ɡi], not *[ko.ki]. Same phoneme /k/, two allophones. Mid back rounded ㅗ /o/ and high front ㅣ /i/.
- **바보** `/pabo/ [pa.bo]` — Identical in both standards. Voicing on the bilabial: initial ㅂ is voiceless [p], intervocalic ㅂ is voiced [b] → [pa.bo]. The voiced allophone [b] is phonetic, not a separate phoneme. Pairs with 고기 (/k/→[ɡ]) and 아버지 (/tɕ/) to show the allophonic [b d ɡ dʑ] set.
- **아버지** `/abʌtɕi/ [a.bʌ.dʑi]` — Identical in both standards. A double voicing showcase: intervocalic ㅂ → [b] and intervocalic ㅈ → [dʑ], giving [a.bʌ.dʑi]. Demonstrates the mid back unrounded vowel ㅓ /ʌ/ (note mr writes it ŏ with a breve; rr writes it 'eo'). High front ㅣ /i/.
- **사람** `/saɾam/` — Identical in both standards. Plain fricative ㅅ /s/ before /a/ stays [s] (it would become [ɕ] only before /i/ or /j/, see 시간). Intervocalic ㄹ is the TAP [ɾ] — sa-[ɾ]-am — whereas coda ㄹ would be the lateral [l]. Coda ㅁ /m/. The two ㄹ realizations [ɾ]~[l] are positional allophones, not a phonemic contrast.
- **시간** `/sigan/ [ɕi.ɡan]` — Identical in both standards. Demonstrates that ㅅ /s/ palatalizes to [ɕ] before /i/: [ɕi], not *[si]. The intervocalic ㄱ also voices to [ɡ] → [ɕi.ɡan]. Coda ㄴ /n/. (Distinct from the morphophonemic 구개음화 of ㄷㅌ; this is the lower-level /s/ allophony.)
- **한국** `/hanɡuk̚/` — Identical phonetically; the names differ politically (South: 한국; North uses 조선 for the country). Onset ㅎ /h/; the medial ㄱ after nasal ㄴ; the final ㄱ is an UNRELEASED coda stop [k̚] (batchim). Note mr inserts an apostrophe (han'guk) to keep ㄴ+ㄱ from being misread as the digraph for ㅇ /ŋ/.
- **꽃** `/k͈ot̚/` — Identical in both standards. Tense onset ㄲ /k͈/. The crucial point is the CODA: written ㅊ (/tɕʰ/) neutralizes to the unreleased alveolar stop [t̚] in coda position → /k͈ot̚/. One of the classic seven-batchim demonstrations: all of ㅅㅆㅈㅊㅌㅎ-codas surface as [t̚]. Under 연음 the underlying ㅊ resurfaces, e.g. 꽃이 [k͈o.tɕʰi].
- **부엌** `/puʌk̚/` — Identical in both standards. Written coda ㅋ (/kʰ/) neutralizes to unreleased [k̚]: /puʌk̚/, aspiration lost in coda. The hiatus ㅜ+ㅓ = /uʌ/. Under 연음 the ㅋ resurfaces as an onset, e.g. 부엌에 [pu.ʌ.kʰe].
- **값** `/kap̚/` — Identical in both standards. CLUSTER-CODA simplification: the written double-coda ㅄ (ㅂ+ㅅ) drops the ㅅ and the ㅂ surfaces as unreleased [p̚] → /kap̚/. When followed by a vowel the whole cluster is preserved via 연음 + 경음화, e.g. 값이 [kap.s͈i]. Demonstrates that Korean has NO pronounced coda clusters.
- **닭** `/tak̚/` — Identical in both standards. CLUSTER-CODA simplification of ㄺ (ㄹ+ㄱ): the ㄹ is dropped and the ㄱ surfaces as unreleased [k̚] → /tak̚/. (Which member survives is lexically/dialectally variable; standard Seoul keeps the ㄱ here.) Under 연음, 닭이 → [tal.ɡi].
- **앉다** `/ant͈a/ [an.t͈a]` — Identical in both standards. The double-coda ㄵ (ㄴ+ㅈ) simplifies so only ㄴ is pronounced, BUT the dropped ㅈ triggers 경음화: the following ㄷ of the ending -다 tenses to ㄸ → [an.t͈a]. A combined cluster-simplification + tensification showcase.
- **국물** `/kuŋmul/` — Identical in both standards. NASALIZATION: the coda ㄱ /k/ assimilates to the velar nasal [ŋ] before the nasal onset ㅁ → 국물 written guk-mul but pronounced /kuŋmul/. Spelling stays morphophonemic (국 'soup' + 물 'water'); rr 'gungmul' reflects the surface. Coda ㄹ [l] finally; the ㅇ here is /ŋ/.
- **신라** `/silla/` — Identical in both standards. LATERALIZATION: the sequence ㄴ+ㄹ (sin+ra) assimilates to a geminate lateral [ll] → /silla/, NOT *[sinɾa]. The geminate ㄹㄹ is realized as [l.l] (not the tap). Both rr and mr write the surface 'Silla'. ㅅ palatalizes to [ɕ] before /i/: [ɕil.la].
- **좋다** `/tɕotʰa/` — Identical in both standards. ASPIRATION/ㅎ-merger: the coda ㅎ of 좋 fuses with the following plain ㄷ of -다 to yield the aspirate [tʰ] → /tɕotʰa/, not *[tɕot.ta]. rr writes 'jota' (showing the aspirate as plain t), mr 'chot'a' (apostrophe marks the aspiration). Plain affricate ㅈ /tɕ/ onset.
- **축하** `/tɕʰukʰa/` — Identical in both standards. The reverse-order ASPIRATION: coda ㄱ + onset ㅎ → [kʰ], so 축하 (chuk+ha) → /tɕʰukʰa/, not *[tɕʰuk.ha]. Demonstrates the aspirated affricate ㅊ /tɕʰ/ onset together with the ㄱ+ㅎ → ㅋ merger. A textbook 격음화 environment.
- **같이** `/katɕʰi/` — Identical in both standards. PALATALIZATION: the coda ㅌ /tʰ/ before the suffix vowel ㅣ /i/ becomes the aspirated affricate [tɕʰ] → 같이 /katɕʰi/, never *[ka.tʰi]. (Parallel ㄷ+i → [tɕ], e.g. 굳이 → [ku.dʑi].) rr renders it 'gachi', mr 'kach'i'. A signature Korean morphophonemic rule.
- **꽃잎** `/k͈onnip̚/` — Identical in both standards. A multi-rule showcase: at the compound boundary 꽃 + 잎, an [n] is INSERTED before the /i/ (ㄴ-첨가), then the coda of 꽃 (underlying ㅊ → [t̚]) NASALIZES to [n] before that inserted ㄴ, and the final ㅍ neutralizes to [p̚] → /k͈onnip̚/, rr 'kkonnip'. Tense ㄲ onset, vowel ㅗ /o/.
- **여자** `South /jʌdʑa/ ~ North /njʌdʑa/` — SOUTH/NORTH 두음법칙 PAIR. From Sino-Korean 女子: the South drops word-initial ㄴ before /j/ → 여자 /jʌdʑa/; the North RETAINS the ㄴ → 녀자 /njʌdʑa/. On-glide diphthong ㅕ /jʌ/; intervocalic ㅈ voices to [dʑ]. The clearest standard-divergence entry.
- **노동** `South /nodoŋ/ [no.doŋ] ~ North /lodoŋ/ [ɾo.doŋ]` — SOUTH/NORTH 두음법칙 PAIR. From Sino-Korean 勞動: the South changes word-initial ㄹ to ㄴ → 노동 /nodoŋ/; the North KEEPS ㄹ → 로동 /lodoŋ/ (the liquid phoneme ㄹ /l/, realized word-initially as the tap [ɾo]; some analyses prefer [r]). Intervocalic ㄷ voices to [d]; final ㅇ is /ŋ/. (Cf. the North party paper 로동신문 vs South 노동.)
- **이발** `South /ibal/ [i.bal] ~ North /libal/ [ɾi.bal]` — SOUTH/NORTH 두음법칙 PAIR. From Sino-Korean 理髮: before /i/ the South DELETES initial ㄹ entirely → 이발 /ibal/; the North KEEPS it → 리발 /libal/ (the phoneme ㄹ /l/, surfacing word-initially as the tap [ɾi]). Completes the three 두음법칙 outcomes — ㄹ→ㄴ (노동), ㄴ→∅ before j (여자), ㄹ→∅ before i (이발). Intervocalic ㅂ → [b]; coda ㄹ [l].
- **그릇** `/kɯɾɯt̚/` — Identical in both standards. The bare high back UNROUNDED vowel ㅡ /ɯ/ appears twice (rr 'eu', mr 'ŭ' with a breve) — the vowel with no close analog in English or Spanish. Intervocalic ㄹ is the tap [ɾ]; the final coda ㅅ neutralizes to unreleased [t̚] (음절의 끝소리 규칙). Under 연음, 그릇이 → [kɯ.ɾɯ.ɕi].
- **의사** `/ɰisa/` — Identical in both standards. The UNIQUE diphthong ㅢ /ɰi/ (velar approximant on-glide + /i/), found only in this letter. Word-initially it is the full [ɰi]; non-initially or in possessive 의 it is widely reduced to [i] or [e]. ㅅ stays [s] before /a/. Demonstrates ㅡ /ɯ/'s glide partner.
- **회사** `South /høsa/ [hwe.sa] ~ North /høsa/ [hø.sa]` — The conservative front rounded monophthong ㅚ /ø/. Most younger SEOUL speakers diphthongize it to [we] → [hwe.sa]; the more conservative NORTH standard better preserves the monophthong [hø.sa]. rr/mr both write 'hoe'. Pairs with 위 (ㅟ /y/) for the front-rounded set.
- **위** `/y/ [wi]` — Identical in both standards. The conservative front rounded high monophthong ㅟ /y/, in modern Seoul almost universally diphthongized to [wi]. Together with 회사 (ㅚ) it documents the two front-rounded vowels of conservative Korean. The onset ㅇ is the silent placeholder (no /ŋ/ in onset).
- **왜** `/wɛ/` — Identical in both standards. The w-on-glide diphthong ㅙ /wɛ/. The nucleus ㅐ /ɛ/ illustrates the front mid vowels; for most younger Seoul speakers ㅐ/ㅔ have MERGED to [e̞] (the 애/에 merger), so ㅙ /wɛ/, ㅞ /we/, and (diphthongized) ㅚ all converge on [we] — making 왜/외/웨 near-homophones. Silent onset ㅇ.

### Coverage Matrix

#### Consonant Inventory Checklist

All 19 consonant phonemes are accounted for (`consonants_all_19_covered: true`). Each row lists the keyword(s) in the array that realize the phoneme.

| Phoneme | Keywords |
|---|---|
| ㄱ /k/ | 감자, 고기, 한국, 국물, 축하, 같이 |
| ㄲ /k͈/ | 꽃, 꽃잎 |
| ㄴ /n/ | 시간, 한국, 신라, 노동, 꽃잎 |
| ㄷ /t/ | 달, 닭, 노동, 좋다 (ending -다) |
| ㄸ /t͈/ | 딸, 앉다 (tensed ending) |
| ㄹ /l ~ ɾ/ | 불 [l], 사람 [ɾ], 신라 [ll], 이발 [l], 노동 (North [ɾ]) |
| ㅁ /m/ | 감자, 사람, 국물 |
| ㅂ /p/ | 불, 바보, 아버지, 값, 이발, 부엌 (onset) |
| ㅃ /p͈/ | 뿔 |
| ㅅ /s ~ ɕ/ | 사람 [s], 시간 [ɕ], 신라 [ɕ], 의사 [s], 회사 [s] |
| ㅆ /s͈/ | not given a dedicated single-syllable keyword; supplied by e.g. 쌀 /s͈al/ ('rice'), 싸다 /s͈ada/ ('cheap') — the tense fricative /s͈/; also surfaces via 경음화 in 값이 [kap.s͈i] |
| ㅇ /ŋ/ (coda) | 국물 [ŋ], 노동 [ŋ], 한국 (medial ㄴ; ㅇ as onset placeholder in 위/왜/여자) |
| ㅈ /tɕ/ | 감자, 아버지, 좋다, 여자 |
| ㅉ /tɕ͈/ | not given a dedicated keyword; supplied by e.g. 짜다 /tɕ͈ada/ ('salty'), 찌개 /tɕ͈igɛ/ ('stew') — the tense affricate /tɕ͈/ |
| ㅊ /tɕʰ/ | 축하, 꽃 (coda → [t̚]), 꽃잎 (coda) |
| ㅋ /kʰ/ | 축하, 부엌 (coda → [k̚]) |
| ㅌ /tʰ/ | 탈, 같이 (→ [tɕʰ] by palatalization), 좋다 (→ [tʰ] by aspiration) |
| ㅍ /pʰ/ | 풀, 꽃잎 (coda → [p̚]) |
| ㅎ /h/ | 한국, 축하, 회사, 좋다 (coda ㅎ feeds 격음화) |

*Consonant gaps note:* 18 of the 19 consonant phonemes are realized by at least one dedicated array keyword, including the full three-way laryngeal sets for the bilabials (불/뿔/풀) and alveolars (달/딸/탈). The two phonemes not given a dedicated single-syllable keyword are the tense fricative ㅆ /s͈/ and the tense affricate ㅉ /tɕ͈/; both are flagged in the checklist with standard exemplars (쌀/싸다 and 짜다/찌개) and ㅆ additionally surfaces inside the array via 경음화 (값이 [kap.s͈i]). ㅇ as an onset is the silent placeholder (위, 왜, 여자, 의사); it is a true /ŋ/ only as a coda (국물, 노동).

#### Laryngeal Three-Way Minimal Sets

| Series | Plain | Tense | Aspirated |
|---|---|---|---|
| Bilabial | 불 /pul/ | 뿔 /p͈ul/ | 풀 /pʰul/ |
| Alveolar | 달 /tal/ | 딸 /t͈al/ | 탈 /tʰal/ |

*Note:* the velar (가/까/카) and affricate (자/짜/차) sets follow the same pattern; the bilabial and alveolar sets are given as full array entries.

#### Vowels — Monophthongs

All monophthongs are covered (`vowels_monophthongs_covered: true`).

| Vowel | Keywords |
|---|---|
| ㅏ /a/ | 달, 탈, 감자, 사람, 같이, 의사, 회사 |
| ㅓ /ʌ/ | 아버지 (ㅓ = mr ŏ), 부엌, 여자 (in ㅕ /jʌ/) |
| ㅗ /o/ | 고기, 바보, 꽃, 노동, 좋다, 꽃잎 |
| ㅜ /u/ | 불, 뿔, 풀, 국물, 축하, 부엌 (in /uʌ/) |
| ㅡ /ɯ/ | 그릇 /kɯɾɯt̚/ (bare monophthong /ɯ/ twice), also via its glide ㅢ /ɰi/ in 의사 |
| ㅣ /i/ | 고기, 시간, 신라, 같이, 의사, 위, 이발 |
| ㅐ /ɛ/ | 왜 (ㅙ /wɛ/); merges with ㅔ /e/ to [e̞] for most young Seoul speakers (애/에 merger) |
| ㅔ /e/ | represented via the ㅐ/ㅔ merger note on 왜 and the [we] realizations of ㅚ/ㅞ; bare /e/ via e.g. 네 /ne/ ('yes') |

#### Conservative Front-Rounded Vowels

| Vowel | Realization |
|---|---|
| ㅚ /ø/ | 회사 /høsa/ — monophthong [ø] (conservative/North) vs diphthongized [we] (young Seoul) |
| ㅟ /y/ | 위 /y/ — monophthong [y] (conservative) vs diphthongized [wi] (modern Seoul) |

#### Diphthongs and Glides

| Glide / Diphthong | Keyword |
|---|---|
| /j/-glide /jʌ/ | 여자 /jʌdʑa/ (ㅕ /jʌ/, on-glide /j/ + ㅓ) |
| /w/-glide /wɛ/ | 왜 /wɛ/ (ㅙ /wɛ/, on-glide /w/ + ㅐ) |
| /w/-glide /we/, /wi/ | 회사 [hwe.sa] and 위 [wi] when ㅚ/ㅟ are diphthongized (ㅞ /we/ ~ [we], ㅟ → [wi]) |
| /ɰ/-glide /ɰi/ | 의사 /ɰisa/ — the unique ㅢ /ɰi/ with the velar approximant on-glide /ɰ/ |

*Note:* the remaining /j/-series (ㅑㅛㅠㅒㅖ) and /w/-series (ㅘㅝ) follow the same on-glide + vowel pattern as 여자 and 왜; representative members are given as array entries.

#### Phonological Rules Checklist

| Rule | Keyword(s) |
|---|---|
| 연음 (liaison / resyllabification) | 같이 (feeds palatalization); noted under 꽃 (꽃이 [k͈o.tɕʰi]); 부엌 (부엌에 [pu.ʌ.kʰe]); 값 (값이 [kap.s͈i]); 닭 (닭이 [tal.ɡi]) |
| 음절의 끝소리 규칙 (coda neutralization, 7 sounds) | 한국 [k̚], 꽃 [t̚], 부엌 [k̚], 값 [p̚], 닭 [k̚], 꽃잎 [p̚] |
| 자음군 단순화 (cluster-coda simplification) | 값 (ㅄ → [p̚]), 닭 (ㄺ → [k̚]), 앉다 (ㄵ → [n]) |
| 비음화 (nasalization) | 국물 (ㄱ → [ŋ] / _ㅁ), 꽃잎 (ㅊ-coda → [n] / _inserted ㄴ) |
| 유음화 (lateralization) | 신라 (ㄴ+ㄹ → [ll]) |
| 경음화 (tensification / fortis) | 앉다 (dropped ㅈ tenses ㄷ → [t͈]); noted under 값 (값이 [kap.s͈i]) |
| 격음화 (aspiration / ㅎ-merger) | 좋다 (ㅎ+ㄷ → [tʰ]), 축하 (ㄱ+ㅎ → [kʰ]) |
| 구개음화 (palatalization) | 같이 (ㅌ+i → [tɕʰ]); noted: ㄷ+i → [tɕ] e.g. 굳이 [ku.dʑi] |
| ㄴ-첨가 (n-insertion) | 꽃잎 (compound boundary, [n] before /i/) |
| ㅅ 구개음화 (s-allophony) | 시간 [ɕi], 신라 [ɕil], (ㅅ /s/ → [ɕ] before /i/, /j/) |
| 유성음화 (intervocalic voicing of plain obstruents) | 고기 (ㄱ→[ɡ]), 바보 (ㅂ→[b]), 아버지 (ㅂ→[b], ㅈ→[dʑ]), 시간 (ㄱ→[ɡ]), 노동 (ㄷ→[d]) |
| 두음법칙 (initial-sound rule, South only) | 여자/녀자 (ㄴ→∅ before j), 노동/로동 (ㄹ→ㄴ), 이발/리발 (ㄹ→∅ before i) |

#### Batchim (받침) Neutralization Demonstrations

- The 7 surface codas are [k t p l m n ŋ]: [k̚] 한국·부엌·닭, [t̚] 꽃, [p̚] 값·꽃잎, [l] 불·사람(coda)·이발, [m] 감자·사람·국물, [n] 시간·신라·앉다·꽃잎, [ŋ] 국물·노동.
- All written coda jamo reduce to these 7: 부엌 ㅋ→[k̚], 꽃 ㅊ→[t̚], 꽃잎 ㅍ→[p̚].

#### Cluster-Coda Simplification Demonstrations

| Cluster | Result | Keyword |
|---|---|---|
| ㅄ | → [p̚] | 값 /kap̚/ (drops ㅅ) |
| ㄺ | → [k̚] | 닭 /tak̚/ (drops ㄹ) |
| ㄵ | → [n] (+경음화) | 앉다 [an.t͈a] (drops ㅈ, which tenses the next stop) |

#### Intervocalic Voicing Demonstrations

| Phoneme | Allophone | Keywords |
|---|---|---|
| ㄱ /k/ | → [ɡ] | 고기 [ko.ɡi], 시간 [ɕi.ɡan] |
| ㄷ /t/ | → [d] | 노동 [no.doŋ], 아버지 (cf.) |
| ㅂ /p/ | → [b] | 바보 [pa.bo], 아버지 [a.bʌ.dʑi], 이발 [i.bal] |
| ㅈ /tɕ/ | → [dʑ] | 아버지 [a.bʌ.dʑi], 여자 [jʌ.dʑa] |

#### South / North Divergence Types Illustrated

- **두음법칙 (initial-sound rule):** the central South↔North contrast — 여자 vs 녀자 (ㄴ→∅ / kept), 노동 vs 로동 (ㄹ→ㄴ / kept as [ɾ]), 이발 vs 리발 (ㄹ→∅ / kept).
- **Vowel realization conservatism:** North better preserves the ㅚ /ø/ monophthong ([hø.sa]) where young Seoul diphthongizes to [hwe.sa].
- **Shared (standard-invariant) processes** — three-way laryngeal contrast, intervocalic voicing, coda neutralization, cluster simplification, 비음화/유음화/경음화/격음화/구개음화, ㄴ-첨가 — are illustrated identically in both columns by the remaining 26 entries.
- **Country naming aside:** South 한국 vs North 조선 for the nation (the segmental pronunciation of 한국 itself is identical).

---

*Section maintained by Shin.*

## Unicode Reference

Unicode codepoint reference for every IPA symbol, diacritic, suprasegmental mark, and Hangul (한글) character used throughout this Korean pronunciation guide. Each entry gives the symbol, its Unicode codepoint (U+XXXX), decimal value, official Unicode character name, and its phonetic role in Korean, documenting in parallel the two reference standards used throughout the guide: STANDARD SOUTH KOREAN (표준어 *pyojun-eo*, educated Seoul speech) and NORTH KOREAN (문화어 *munhwaeo*, Pyongyang standard). All IPA codepoints follow the IPA 2015 revision conventions. The most distinctive Korean entries are the three-way laryngeal contrast — note especially the TENSE/FORTIS diacritic `U+0348` COMBINING DOUBLE VERTICAL LINE BELOW used for ㄲ ㄸ ㅃ ㅉ ㅆ — and the alveolo-palatal affricate base ɕ/ʑ. Most plain IPA consonants and several vowels reuse Basic Latin letters, while the specialized symbols live in the IPA Extensions, Spacing Modifier Letters, and Combining Diacritical Marks blocks. The Hangul characters themselves are catalogued separately under **Hangul Jamo** and **Hangul Unicode Blocks**, including the composition formula for the 11,172 precomposed syllable blocks. This guide ships four reader tiers — Scholarly and Pretty (language-neutral Latin), Hangul (한글 composed blocks), and Revised Romanization (RR readback) — and these codepoints underpin all of them.

### IPA Consonant Symbols

The 19 Korean consonant phonemes plus key allophonic symbols, organized around the signature THREE-WAY LARYNGEAL CONTRAST of the obstruents: plain/lax (lenis), tense/fortis, and aspirated. Korean has NO phonemic voicing contrast: the lax stops /k t p tɕ/ voice intervocalically to [ɡ d b dʑ], shown as separate allophone entries. The affricates tɕ tɕʰ tɕ͈ dʑ are digraphs built on the alveolo-palatal base ɕ/ʑ (no single codepoint). The TENSE consonants are written with the base symbol plus `U+0348` COMBINING DOUBLE VERTICAL LINE BELOW (k͈ t͈ p͈ tɕ͈ s͈). Aspiration uses the modifier letter ʰ `U+02B0`. The plain stops /k t p/, fricatives /s h/, nasals /m n/, and the liquid /l/ reuse Basic Latin letters; ɡ is the single-story script g, ŋ the eng, ɾ the fishhook r, and ɕ ʑ come from IPA Extensions. Korean LACKS /f v θ ð z ʃ ʒ/ entirely — a major gap relative to Aramaic.

| Symbol | Codepoint | Decimal | Name | Jamo | IPA Role |
|---|---|---|---|---|---|
| k | `U+006B` | 107 | LATIN SMALL LETTER K | `ㄱ` | plain/lax (lenis) velar plosive `/k/` (가 ga, 기 gi); voices to `[ɡ]` intervocalically; realized as unreleased `[k̚]` in coda; aspirated lightly word-initially — the unmarked member of the velar three-way contrast |
| t | `U+0074` | 116 | LATIN SMALL LETTER T | `ㄷ` | plain/lax (lenis) alveolar plosive `/t/` (다 da, 도 do); voices to `[d]` intervocalically; unreleased `[t̚]` in coda; the unmarked member of the alveolar three-way contrast |
| p | `U+0070` | 112 | LATIN SMALL LETTER P | `ㅂ` | plain/lax (lenis) bilabial plosive `/p/` (바 ba, 보 bo); voices to `[b]` intervocalically; unreleased `[p̚]` in coda; the unmarked member of the bilabial three-way contrast |
| tɕ | — (digraph) | — | LATIN SMALL LETTER T (`U+0074`) + LATIN SMALL LETTER C WITH CURL (`U+0255`) | `ㅈ` | plain/lax (lenis) alveolo-palatal affricate `/tɕ/` (자 ja, 지 ji); voices to `[dʑ]` intervocalically; the unmarked member of the affricate three-way contrast; the IPA tie-bar ligature t͡ɕ may also be written |
| k͈ | — (base + combining) | — | LATIN SMALL LETTER K (`U+006B`) + COMBINING DOUBLE VERTICAL LINE BELOW (`U+0348`) | `ㄲ` | TENSE/FORTIS velar plosive `/k͈/` (까 kka); the tense marker is `U+0348` placed below the base k; produced with a constricted, tensed glottis and no aspiration; contrasts minimally with plain `/k/` and aspirated `/kʰ/` |
| t͈ | — (base + combining) | — | LATIN SMALL LETTER T (`U+0074`) + COMBINING DOUBLE VERTICAL LINE BELOW (`U+0348`) | `ㄸ` | TENSE/FORTIS alveolar plosive `/t͈/` (따 tta); tensed-glottis, unaspirated; the tense marker is `U+0348` below the base t |
| p͈ | — (base + combining) | — | LATIN SMALL LETTER P (`U+0070`) + COMBINING DOUBLE VERTICAL LINE BELOW (`U+0348`) | `ㅃ` | TENSE/FORTIS bilabial plosive `/p͈/` (빠 ppa); tensed-glottis, unaspirated; the tense marker is `U+0348` below the base p |
| tɕ͈ | — (digraph + combining) | — | LATIN SMALL LETTER T (`U+0074`) + LATIN SMALL LETTER C WITH CURL (`U+0255`) + COMBINING DOUBLE VERTICAL LINE BELOW (`U+0348`) | `ㅉ` | TENSE/FORTIS alveolo-palatal affricate `/tɕ͈/` (짜 jja); tensed-glottis, unaspirated; the tense marker `U+0348` attaches under the ɕ element |
| s͈ | — (base + combining) | — | LATIN SMALL LETTER S (`U+0073`) + COMBINING DOUBLE VERTICAL LINE BELOW (`U+0348`) | `ㅆ` | TENSE/FORTIS alveolar fricative `/s͈/` (싸 ssa); the only tense fricative; tensed, longer, more forceful frication than plain `/s/`; becomes `[ɕ͈]` before `/i/` or `/j/`; the tense marker is `U+0348` below the base s |
| kʰ | — (base + modifier) | — | LATIN SMALL LETTER K (`U+006B`) + MODIFIER LETTER SMALL H (`U+02B0`) | `ㅋ` | ASPIRATED velar plosive `/kʰ/` (카 ka); strong breathy release; the aspirated member of the velar three-way contrast; ʰ is the spacing modifier letter, not a superscript h glyph |
| tʰ | — (base + modifier) | — | LATIN SMALL LETTER T (`U+0074`) + MODIFIER LETTER SMALL H (`U+02B0`) | `ㅌ` | ASPIRATED alveolar plosive `/tʰ/` (타 ta); strong breathy release; the aspirated member of the alveolar three-way contrast |
| pʰ | — (base + modifier) | — | LATIN SMALL LETTER P (`U+0070`) + MODIFIER LETTER SMALL H (`U+02B0`) | `ㅍ` | ASPIRATED bilabial plosive `/pʰ/` (파 pa); strong breathy release; the aspirated member of the bilabial three-way contrast |
| tɕʰ | — (digraph + modifier) | — | LATIN SMALL LETTER T (`U+0074`) + LATIN SMALL LETTER C WITH CURL (`U+0255`) + MODIFIER LETTER SMALL H (`U+02B0`) | `ㅊ` | ASPIRATED alveolo-palatal affricate `/tɕʰ/` (차 cha); strong breathy release; the aspirated member of the affricate three-way contrast |
| s | `U+0073` | 115 | LATIN SMALL LETTER S | `ㅅ` | plain alveolar fricative `/s/` (사 sa, 소 so); NOT part of the three-way stop contrast but pairs with tense `/s͈/`; palatalizes to alveolo-palatal `[ɕ]` before `/i/` or `/j/` (시 `[ɕi]` si, 셔 `[ɕʌ]` syeo) |
| h | `U+0068` | 104 | LATIN SMALL LETTER H | `ㅎ` | voiceless glottal fricative `/h/` (하 ha); weakens or deletes intervocalically and after a sonorant (좋아 → `[tɕoa]`); fuses with an adjacent plain stop to yield aspiration (격음화), e.g. ㅎ+ㄱ → `[kʰ]` |
| m | `U+006D` | 109 | LATIN SMALL LETTER M | `ㅁ` | voiced bilabial nasal `/m/` (마 ma); occurs as both onset and coda; one of the seven permitted coda sounds; the target of bilabial nasalization (`/p/` → `[m]` before a nasal) |
| n | `U+006E` | 110 | LATIN SMALL LETTER N | `ㄴ` | voiced alveolar nasal `/n/` (나 na); onset and coda; one of the seven permitted coda sounds; target of alveolar nasalization (`/t/` → `[n]` before a nasal); becomes `[l]` next to ㄹ (유음화) |
| ŋ | `U+014B` | 331 | LATIN SMALL LETTER ENG | `ㅇ` | voiced velar nasal `/ŋ/` — occurs ONLY as a coda (강 `[kaŋ]` gang); the letter ㅇ as a SYLLABLE ONSET is a SILENT placeholder (zero consonant), carrying no sound; target of velar nasalization (`/k/` → `[ŋ]` before a nasal) |
| l | `U+006C` | 108 | LATIN SMALL LETTER L | `ㄹ` | lateral approximant realization of the liquid `/l ~ ɾ/` (ㄹ); appears as `[l]` in coda position (달 `[tal]` dal) and in the geminate ㄹㄹ (`[ll]`, e.g. 빨리 `[p͈alli]`); one of the seven permitted coda sounds |
| ɾ | `U+027E` | 638 | LATIN SMALL LETTER R WITH FISHHOOK | `ㄹ` | alveolar TAP/flap realization of the liquid `/l ~ ɾ/` (ㄹ); appears as `[ɾ]` as an intervocalic ONSET (다리 `[taɾi]` dari); complementary with the coda/geminate `[l]` allophone |
| ɡ | `U+0261` | 609 | LATIN SMALL LETTER SCRIPT G | `ㄱ` | voiced velar plosive `[ɡ]` — the INTERVOCALIC ALLOPHONE of plain `/k/` (아기 `[aɡi]` agi); the single-story script g, distinct from Latin small letter g `U+0067`; not a separate phoneme — Korean has no voicing contrast |
| d | `U+0064` | 100 | LATIN SMALL LETTER D | `ㄷ` | voiced alveolar plosive `[d]` — the INTERVOCALIC ALLOPHONE of plain `/t/` (어디 `[ʌdi]` eodi); not a separate phoneme |
| b | `U+0062` | 98 | LATIN SMALL LETTER B | `ㅂ` | voiced bilabial plosive `[b]` — the INTERVOCALIC ALLOPHONE of plain `/p/` (아버지 `[abʌdʑi]` abeoji); not a separate phoneme |
| dʑ | — (digraph) | — | LATIN SMALL LETTER D (`U+0064`) + LATIN SMALL LETTER Z WITH CURL (`U+0291`) | `ㅈ` | voiced alveolo-palatal affricate `[dʑ]` — the INTERVOCALIC ALLOPHONE of plain `/tɕ/` (아버지 `[abʌdʑi]` abeoji); not a separate phoneme; the IPA tie-bar ligature d͡ʑ may also be written |
| ɕ | `U+0255` | 597 | LATIN SMALL LETTER C WITH CURL | `ㅅ / ㅈ ㅊ` | voiceless alveolo-palatal fricative `[ɕ]` — the ALLOPHONE of `/s/` before `/i/` or `/j/` (시 `[ɕi]` si); also the fricative element of all the affricates tɕ tɕʰ tɕ͈ dʑ; from IPA Extensions, NOT the postalveolar ʃ |
| ʑ | `U+0291` | 657 | LATIN SMALL LETTER Z WITH CURL | `ㅈ` | voiced alveolo-palatal fricative — the voiced fricative element of the intervocalic affricate allophone `[dʑ]`; not an independent Korean phoneme; the voiced counterpart of ɕ |

### IPA Vowel Symbols

Korean's monophthong inventory (modern Seoul ~7–8; conservative up to 10). The core eight monophthongs are /a ʌ o u ɯ i ɛ e/; ㅐ /ɛ/ and ㅔ /e/ are merged to a single mid front [e̞] for most younger Seoul speakers (the 애/에 merger). The front rounded ㅚ /ø/ and ㅟ /y/ are monophthongs only in conservative speech, usually diphthongized to [we] and [wi]. The on-glides /j/, /w/ and the unique /ɰ/ (only in ㅢ /ɰi/) build the rising diphthongs. Several qualities reuse Basic Latin letters (a o u i e y); ʌ ɯ ɛ ø ɰ come from IPA Extensions and Latin-1 Supplement. Korean has NO phonemic vowel length in the modern standard (older Seoul and the North preserve some length distinctions) and NO schwa /ə/.

| Symbol | Codepoint | Decimal | Name | Jamo | IPA Role |
|---|---|---|---|---|---|
| a | `U+0061` | 97 | LATIN SMALL LETTER A | `ㅏ` | open central/front unrounded vowel `/a/` (아 a, 가 ga); roughly cardinal `[a]`; full quality in all positions — no reduction |
| ʌ | `U+028C` | 652 | LATIN SMALL LETTER TURNED V | `ㅓ` | open-mid back unrounded vowel `/ʌ/` (어 eo, 거 geo); RR 'eo', MR 'ŏ'; in much of modern Seoul realized more centrally/raised toward `[ɔ̜]`~`[ə]`-like; the North keeps a more clearly back `[ʌ]` |
| o | `U+006F` | 111 | LATIN SMALL LETTER O | `ㅗ` | close-mid back rounded vowel `/o/` (오 o, 고 go); roughly cardinal `[o]`; in younger Seoul speech often raised, narrowing the contrast with `/u/` |
| u | `U+0075` | 117 | LATIN SMALL LETTER U | `ㅜ` | close back rounded vowel `/u/` (우 u, 구 gu); cardinal `[u]`, sometimes slightly centralized `[ʉ]` in Seoul |
| ɯ | `U+026F` | 623 | LATIN SMALL LETTER TURNED M | `ㅡ` | close back UNROUNDED vowel `/ɯ/` (으 eu, 그 geu); RR 'eu', MR 'ŭ'; the characteristic Korean high back unrounded vowel, absent from Aramaic and English; the default epenthetic vowel in loanword adaptation |
| i | `U+0069` | 105 | LATIN SMALL LETTER I | `ㅣ` | close front unrounded vowel `/i/` (이 i, 기 gi); cardinal `[i]`; triggers palatalization of `/s/`→`[ɕ]`, ㄷㅌ→`[tɕ tɕʰ]`, and the 두음법칙 initial-sound changes in the South |
| ɛ | `U+025B` | 603 | LATIN SMALL LETTER OPEN E | `ㅐ` | open-mid front unrounded vowel `/ɛ/` (애 ae); RR 'ae'; MERGED with `/e/` (ㅔ) to a single mid front `[e̞]` for most younger Seoul speakers (the 애/에 merger); kept distinct in careful and conservative speech |
| e | `U+0065` | 101 | LATIN SMALL LETTER E | `ㅔ` | close-mid front unrounded vowel `/e/` (에 e); RR 'e'; merged with `/ɛ/` (ㅐ) to `[e̞]` for most younger Seoul speakers; also the vowel of the diphthongs ㅖ `/je/`, ㅞ `/we/` and the usual diphthongized realization of ㅚ → `[we]` |
| ø | `U+00F8` | 248 | LATIN SMALL LETTER O WITH STROKE | `ㅚ` | close-mid front ROUNDED vowel `/ø/` (외 oe) — a monophthong only in CONSERVATIVE speech; for most modern speakers ㅚ is diphthongized to `[we]`; RR 'oe'; from Latin-1 Supplement |
| y | `U+0079` | 121 | LATIN SMALL LETTER Y | `ㅟ` | close front ROUNDED vowel `/y/` (위 wi) — a monophthong only in CONSERVATIVE speech; for most modern speakers ㅟ is diphthongized to `[wi]`; RR 'wi'; here the IPA value, NOT the glide `/j/` |
| j | `U+006A` | 106 | LATIN SMALL LETTER J | `ㅑㅕㅛㅠㅒㅖ` | palatal ON-GLIDE `/j/` of the rising y-diphthongs: ㅑ `/ja/`, ㅕ `/jʌ/`, ㅛ `/jo/`, ㅠ `/ju/`, ㅒ `/jɛ/`, ㅖ `/je/`; NOT the affricate value of Latin 'j' |
| w | `U+0077` | 119 | LATIN SMALL LETTER W | `ㅘㅙㅝㅞㅚㅟ` | labial-velar ON-GLIDE `/w/` of the rising w-diphthongs: ㅘ `/wa/`, ㅙ `/wɛ/`, ㅝ `/wʌ/`, ㅞ `/we/`, plus ㅚ→`[we]` and ㅟ→`[wi]` when diphthongized |
| ɰ | `U+0270` | 624 | LATIN SMALL LETTER TURNED M WITH LONG LEG | `ㅢ` | velar/unrounded ON-GLIDE `/ɰ/` — occurs ONLY in the diphthong ㅢ `/ɰi/` (의 ui); realized as `[i]` in non-initial syllables and as `[e]` in the possessive particle 의; a glide unique to Korean among the guide's languages |

### Diacritics & Suprasegmentals

Marks for the laryngeal contrast, articulator detail, and prosody. The single most important diacritic here is `U+0348` COMBINING DOUBLE VERTICAL LINE BELOW, the TENSE/FORTIS marker on ㄲ ㄸ ㅃ ㅉ ㅆ (k͈ t͈ p͈ tɕ͈ s͈). Aspiration uses the spacing modifier ʰ `U+02B0`. Korean has NO LEXICAL STRESS and NO LEXICAL TONE in the standard language, so the primary/secondary stress marks (ˈ ˌ) are used only to indicate accentual-phrase prominence where the guide marks prosody; the length mark ː appears only for the conservative/Northern long-vowel distinctions. The tie bar joins affricate elements. Combining marks live in Combining Diacritical Marks (`U+0300–U+036F`) and attach to the preceding base; the stress/length marks are spacing modifier letters.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| ◌͈ | `U+0348` | 840 | COMBINING DOUBLE VERTICAL LINE BELOW | TENSE/FORTIS diacritic — the defining Korean laryngeal mark; written below the base symbol to denote the tense obstruents ㄲ `/k͈/`, ㄸ `/t͈/`, ㅃ `/p͈/`, ㅉ `/tɕ͈/`, ㅆ `/s͈/`; signals a tensed, constricted glottis with no aspiration; combines below the base letter |
| ʰ | `U+02B0` | 688 | MODIFIER LETTER SMALL H | ASPIRATION mark — forms the aspirated obstruents ㅋ `/kʰ/`, ㅌ `/tʰ/`, ㅍ `/pʰ/`, ㅊ `/tɕʰ/`, and the surface aspiration produced by 격음화 (ㅎ + plain stop); a spacing modifier letter, NOT a superscript-h glyph |
| ◌̚ | `U+031A` | 794 | COMBINING LEFT ANGLE ABOVE | NO AUDIBLE RELEASE (unreleased) diacritic — marks the unreleased coda stops `[k̚ t̚ p̚]` that result from coda neutralization (음절의 끝소리 규칙), e.g. 밥 `[pap̚]`; combines above the base letter |
| ◌̟ | `U+031F` | 799 | COMBINING PLUS SIGN BELOW | ADVANCED (fronted) diacritic — a backness adjustment used for fine vowel-quality notation, e.g. a fronted/advanced back-vowel realization `[ʌ̟]` of ㅓ in much of modern Seoul; combines below the base letter (the LOWERED `[e̞]` target of the ㅐ/ㅔ merger is written with `U+031E`, not this mark) |
| ◌̞ | `U+031E` | 798 | COMBINING DOWN TACK BELOW | LOWERED diacritic — used to write the mid `[e̞]` target of the merged ㅐ/ㅔ vowels and other lowered qualities; combines below the base letter |
| ◌̃ | `U+0303` | 771 | COMBINING TILDE | NASALIZATION diacritic — marks contextual vowel nasalization adjacent to nasal consonants in connected speech; combines above the base vowel |
| ◌̯ | `U+032F` | 815 | COMBINING INVERTED BREVE BELOW | NON-SYLLABIC diacritic — marks a glide/off-glide element written under a vowel base where a diphthong is transcribed with vowel symbols rather than glide letters; combines below the base letter |
| ◌͡◌ | `U+0361` | 865 | COMBINING DOUBLE INVERTED BREVE | TIE BAR (affricate ligature) — joins the two elements of the affricates into single units t͡ɕ, t͡ɕʰ, t͡ɕ͈, d͡ʑ (자 `[t͡ɕa]`); spans the two base letters, written above; the below-base equivalent is the double breve below `U+035C` |
| ˈ | `U+02C8` | 712 | MODIFIER LETTER VERTICAL LINE | PRIMARY prominence mark — placed before a syllable; Korean has NO lexical stress, so this is used only to indicate accentual-phrase / intonational prominence where the guide notates prosody (and lexical pitch in the Gyeongsang and Hamgyŏng pitch-accent dialects); a spacing modifier letter, NOT the apostrophe `U+0027` |
| ˌ | `U+02CC` | 716 | MODIFIER LETTER LOW VERTICAL LINE | SECONDARY prominence mark — likewise used only for phrase-level prosodic notation, not lexical stress (which Korean lacks); a spacing modifier letter |
| ː | `U+02D0` | 720 | MODIFIER LETTER TRIANGULAR COLON | LENGTH mark — modern Standard South Korean has effectively LOST phonemic vowel length, so this appears only where the guide records the conservative older-Seoul and Northern (문화어) long-vowel distinctions (눈 `[nun]` 'eye' vs `[nuːn]` 'snow'); a spacing modifier letter, NOT two colons |

### Hangul Jamo

The HANGUL COMPATIBILITY JAMO (`U+3130–U+318F`) — the standalone, non-conjoining forms used to NAME and DISPLAY individual letters (자모 *jamo*) in isolation, as in a chart or when citing a letter abstractly. These are distinct from the conjoining Hangul Jamo (`U+1100–U+11FF`) that actually compose into syllable blocks, and from the precomposed Hangul Syllables (`U+AC00–U+D7A3`). Each jamo is classified by its role in the square syllable block: 초성 (*choseong*, onset), 중성 (*jungseong*, medial vowel/glide), 종성 (*jongseong*, coda). The official Unicode names romanize the letters in a McCune–Reischauer-like scheme (KIYEOK = ㄱ, SSANG- = tense/doubled, etc.). All 19 consonant letters, all 21 vowel letters, and the cluster-coda (겹받침) jamo used in this guide are listed.

#### Consonant Letters

| Jamo | Codepoint | Decimal | Name | Korean Name | Role |
|---|---|---|---|---|---|
| `ㄱ` | `U+3131` | 12593 | HANGUL LETTER KIYEOK | 기역 | plain velar; onset or coda; IPA `/k/` (→`[ɡ]` intervocalic, `[k̚]` coda) |
| `ㄲ` | `U+3132` | 12594 | HANGUL LETTER SSANGKIYEOK | 쌍기역 | tense velar; IPA `/k͈/` |
| `ㄴ` | `U+3134` | 12596 | HANGUL LETTER NIEUN | 니은 | alveolar nasal; onset or coda; IPA `/n/` |
| `ㄷ` | `U+3137` | 12599 | HANGUL LETTER TIKEUT | 디귿 | plain alveolar stop; IPA `/t/` (→`[d]` intervocalic) |
| `ㄸ` | `U+3138` | 12600 | HANGUL LETTER SSANGTIKEUT | 쌍디귿 | tense alveolar stop; onset only; IPA `/t͈/` |
| `ㄹ` | `U+3139` | 12601 | HANGUL LETTER RIEUL | 리을 | liquid; onset `[ɾ]` / coda & geminate `[l]`; IPA `/l ~ ɾ/` |
| `ㅁ` | `U+3141` | 12609 | HANGUL LETTER MIEUM | 미음 | bilabial nasal; onset or coda; IPA `/m/` |
| `ㅂ` | `U+3142` | 12610 | HANGUL LETTER PIEUP | 비읍 | plain bilabial stop; IPA `/p/` (→`[b]` intervocalic) |
| `ㅃ` | `U+3143` | 12611 | HANGUL LETTER SSANGPIEUP | 쌍비읍 | tense bilabial stop; onset only; IPA `/p͈/` |
| `ㅅ` | `U+3145` | 12613 | HANGUL LETTER SIOS | 시옷 | plain alveolar fricative; IPA `/s/` (→`[ɕ]` before i/j) |
| `ㅆ` | `U+3146` | 12614 | HANGUL LETTER SSANGSIOS | 쌍시옷 | tense alveolar fricative; IPA `/s͈/` |
| `ㅇ` | `U+3147` | 12615 | HANGUL LETTER IEUNG | 이응 | SILENT zero-onset placeholder; as a CODA = velar nasal IPA `/ŋ/` |
| `ㅈ` | `U+3148` | 12616 | HANGUL LETTER CIEUC | 지읒 | plain affricate; IPA `/tɕ/` (→`[dʑ]` intervocalic) |
| `ㅉ` | `U+3149` | 12617 | HANGUL LETTER SSANGCIEUC | 쌍지읒 | tense affricate; onset only; IPA `/tɕ͈/` |
| `ㅊ` | `U+314A` | 12618 | HANGUL LETTER CHIEUCH | 치읓 | aspirated affricate; IPA `/tɕʰ/` |
| `ㅋ` | `U+314B` | 12619 | HANGUL LETTER KHIEUKH | 키읔 | aspirated velar stop; IPA `/kʰ/` |
| `ㅌ` | `U+314C` | 12620 | HANGUL LETTER THIEUTH | 티읕 | aspirated alveolar stop; IPA `/tʰ/` |
| `ㅍ` | `U+314D` | 12621 | HANGUL LETTER PHIEUPH | 피읖 | aspirated bilabial stop; IPA `/pʰ/` |
| `ㅎ` | `U+314E` | 12622 | HANGUL LETTER HIEUH | 히읗 | glottal fricative; IPA `/h/`; triggers 격음화 aspiration |

#### Vowel Letters

| Jamo | Codepoint | Decimal | Name | RR | IPA |
|---|---|---|---|---|---|
| `ㅏ` | `U+314F` | 12623 | HANGUL LETTER A | a | `/a/` |
| `ㅐ` | `U+3150` | 12624 | HANGUL LETTER AE | ae | `/ɛ/` (merged → `[e̞]`) |
| `ㅑ` | `U+3151` | 12625 | HANGUL LETTER YA | ya | `/ja/` |
| `ㅒ` | `U+3152` | 12626 | HANGUL LETTER YAE | yae | `/jɛ/` |
| `ㅓ` | `U+3153` | 12627 | HANGUL LETTER EO | eo | `/ʌ/` |
| `ㅔ` | `U+3154` | 12628 | HANGUL LETTER E | e | `/e/` (merged → `[e̞]`) |
| `ㅕ` | `U+3155` | 12629 | HANGUL LETTER YEO | yeo | `/jʌ/` |
| `ㅖ` | `U+3156` | 12630 | HANGUL LETTER YE | ye | `/je/` |
| `ㅗ` | `U+3157` | 12631 | HANGUL LETTER O | o | `/o/` |
| `ㅘ` | `U+3158` | 12632 | HANGUL LETTER WA | wa | `/wa/` |
| `ㅙ` | `U+3159` | 12633 | HANGUL LETTER WAE | wae | `/wɛ/` |
| `ㅚ` | `U+315A` | 12634 | HANGUL LETTER OE | oe | `/ø/` (usually → `[we]`) |
| `ㅛ` | `U+315B` | 12635 | HANGUL LETTER YO | yo | `/jo/` |
| `ㅜ` | `U+315C` | 12636 | HANGUL LETTER U | u | `/u/` |
| `ㅝ` | `U+315D` | 12637 | HANGUL LETTER WEO | wo | `/wʌ/` |
| `ㅞ` | `U+315E` | 12638 | HANGUL LETTER WE | we | `/we/` |
| `ㅟ` | `U+315F` | 12639 | HANGUL LETTER WI | wi | `/y/` (usually → `[wi]`) |
| `ㅠ` | `U+3160` | 12640 | HANGUL LETTER YU | yu | `/ju/` |
| `ㅡ` | `U+3161` | 12641 | HANGUL LETTER EU | eu | `/ɯ/` |
| `ㅢ` | `U+3162` | 12642 | HANGUL LETTER YI | ui | `/ɰi/` |
| `ㅣ` | `U+3163` | 12643 | HANGUL LETTER I | i | `/i/` |

#### Cluster-Coda Letters (겹받침)

The 겹받침 (double-coda) compatibility jamo. In writing, two consonants stack in the coda slot; in pronunciation, coda neutralization (음절의 끝소리 규칙) reduces each cluster so only ONE of the two consonants is sounded (often the left, sometimes the right, depending on the cluster), e.g. 닭 `[tak̚]` (only ㄱ of ㄺ), 값 `[kap̚]` (only ㅂ of ㅄ).

| Jamo | Codepoint | Decimal | Name | Coda Realization |
|---|---|---|---|---|
| `ㄳ` | `U+3133` | 12595 | HANGUL LETTER KIYEOK-SIOS | → `[k̚]` |
| `ㄵ` | `U+3135` | 12597 | HANGUL LETTER NIEUN-CIEUC | → `[n]` |
| `ㄶ` | `U+3136` | 12598 | HANGUL LETTER NIEUN-HIEUH | → `[n]` (ㅎ triggers aspiration on a following stop) |
| `ㄺ` | `U+313A` | 12602 | HANGUL LETTER RIEUL-KIYEOK | → `[k̚]` (e.g. 닭) |
| `ㄻ` | `U+313B` | 12603 | HANGUL LETTER RIEUL-MIEUM | → `[m]` (e.g. 삶) |
| `ㄼ` | `U+313C` | 12604 | HANGUL LETTER RIEUL-PIEUP | → `[l]` generally (넓다 `[nʌlt͈a]`); prescriptively `[p̚]` in 밟- (밟다 `[pap̚t͈a]`) and in the 넓적-/넓죽- compounds (넓- → [넙]) |
| `ㄽ` | `U+313D` | 12605 | HANGUL LETTER RIEUL-SIOS | → `[l]` |
| `ㄾ` | `U+313E` | 12606 | HANGUL LETTER RIEUL-THIEUTH | → `[l]` |
| `ㄿ` | `U+313F` | 12607 | HANGUL LETTER RIEUL-PHIEUPH | → `[p̚]` |
| `ㅀ` | `U+3140` | 12608 | HANGUL LETTER RIEUL-HIEUH | → `[l]` (ㅎ triggers aspiration on a following stop) |
| `ㅄ` | `U+3144` | 12612 | HANGUL LETTER PIEUP-SIOS | → `[p̚]` (e.g. 값) |

### Hangul Unicode Blocks

Hangul (한글) characters occupy three principal Unicode blocks, plus extension blocks not used by this guide. This guide's Hangul tier and Revised-Romanization readback are built on the PRECOMPOSED Hangul Syllables block; the standalone HANGUL COMPATIBILITY JAMO block supplies the isolated letter forms used in charts and citations; the CONJOINING Hangul Jamo block is the algorithmic substrate for composition/decomposition. Every Korean syllable block is also algorithmically derivable from a choseong + jungseong + jongseong triple via the composition formula below.

| Block | Range | Count | Usage / Description |
|---|---|---|---|
| Hangul Syllables | `U+AC00–U+D7A3` | 11172 | The 11,172 PRECOMPOSED modern Korean syllable blocks — one codepoint per square block of (C)(G)V(C). This is the canonical block for normal Korean text and is what this guide's Hangul reader tier renders (한글 composed blocks). Each block is NFC-normalized to a single codepoint. First: 가 `U+AC00` (HANGUL SYLLABLE GA). Last: 힣 `U+D7A3` (HANGUL SYLLABLE HIH). |
| Hangul Jamo | `U+1100–U+11FF` | 256 | The CONJOINING jamo: choseong (onsets) `U+1100–U+115F`, jungseong (medials) `U+1160–U+11A7`, jongseong (codas) `U+11A8–U+11FF`, plus the choseong filler `U+115F` and jungseong filler `U+1160`. These combine dynamically into syllable blocks (NFD form) and are the algorithmic basis of the composition formula; they are visually distinct from the standalone compatibility jamo. First: ᄀ `U+1100` (HANGUL CHOSEONG KIYEOK). Last: ᇿ `U+11FF` (HANGUL JONGSEONG SSANGNIEUN). (Count note: full 256-codepoint block span — the block is fully assigned, so assigned codepoints = span = 256.) |
| Hangul Compatibility Jamo | `U+3130–U+318F` | 94 | STANDALONE, non-conjoining letter forms used to display or name a jamo in isolation (charts, citations, this guide's Hangul Jamo section). `U+3130` and `U+318F` are unassigned; `U+3164` is the HANGUL FILLER. These do NOT combine into syllable blocks — for that, the conjoining Hangul Jamo block is required. First: ㄱ `U+3131` (HANGUL LETTER KIYEOK). Last: ㆎ `U+318E` (HANGUL LETTER ARAEAE). (Count note: 94 ASSIGNED codepoints within a 96-codepoint block span — `U+3130` and `U+318F` are unassigned.) |
| Basic Latin | `U+0000–U+007F` | — | Source of the IPA plain consonants `/k t p s h m n l/`, the vowels `/a o u i e y/`, the glides `/j w/`, and the bases of all affricate/aspirate digraphs (t d s h plus ʰ). Also supplies the ASCII letters of the Revised Romanization and McCune–Reischauer reader tiers. |
| Latin-1 Supplement | `U+0080–U+00FF` | — | Source of ø `U+00F8` (IPA `/ø/` for ㅚ). MR breve-bearing vowels (ŏ ŭ) and the apostrophe-marked aspirates are composed/displayed using related Latin blocks. |
| Latin Extended-A | `U+0100–U+017F` | — | Source of ŋ `U+014B` (LATIN SMALL LETTER ENG) for the coda velar nasal `/ŋ/` (ㅇ as coda). McCune–Reischauer ŏ `U+014F` / ŭ `U+016D` (o/u with breve) also live here. |
| IPA Extensions | `U+0250–U+02AF` | — | Source of the specialized IPA symbols: ɕ `U+0255`, ɡ `U+0261`, ɯ `U+026F`, ɰ `U+0270`, ɾ `U+027E`, ʌ `U+028C`, ʑ `U+0291`, ɛ `U+025B`. |
| Spacing Modifier Letters | `U+02B0–U+02FF` | — | Source of ʰ `U+02B0` (aspiration), ˈ `U+02C8` (primary prominence), ˌ `U+02CC` (secondary prominence), ː `U+02D0` (length, used only for conservative/Northern long vowels). |
| Combining Diacritical Marks | `U+0300–U+036F` | — | Source of the laryngeal and articulatory marks: ◌͈ `U+0348` (TENSE/FORTIS — the signature Korean diacritic), ◌̚ `U+031A` (no audible release, coda stops), ◌̞ `U+031E` (lowered), ◌̟ `U+031F` (advanced), ◌̃ `U+0303` (nasalized), ◌̯ `U+032F` (non-syllabic), ◌͡◌ `U+0361` (affricate tie bar). |

#### Composition Formula

Any modern Hangul syllable block in `U+AC00–U+D7A3` is algorithmically composed from a *choseong* (onset) index, a *jungseong* (medial) index, and a *jongseong* (coda) index. This is how the guide's tooling converts a jamo triple to a single composed block and back (decomposition).

> **Formula:** `syllable_codepoint = 0xAC00 + (choseong_index × 588) + (jungseong_index × 28) + jongseong_index`

**Indices**

| Element | Count | Order (index range) |
|---|---|---|
| 초성 choseong (onset) | 19 | `ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ` (indices 0–18) |
| 중성 jungseong (medial) | 21 | `ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ` (indices 0–20) |
| 종성 jongseong (coda) | 28 | `(none) ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄹ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅄ ㅅ ㅆ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ` (indices 0–27; index 0 = no coda) |

- **Block constant 588** = 21 (jungseong) × 28 (jongseong) — the span of one choseong.
- **Block constant 28** = number of jongseong slots including the no-coda case.

**Worked Examples**

| Syllable | Jamo | Calculation | Codepoint | RR |
|---|---|---|---|---|
| 가 | ㄱ + ㅏ + (none) | `0xAC00 + (0 × 588) + (0 × 28) + 0 = 0xAC00` | `U+AC00` | ga |
| 한 | ㅎ + ㅏ + ㄴ | `0xAC00 + (18 × 588) + (0 × 28) + 4 = 0xD55C` | `U+D55C` | han |
| 글 | ㄱ + ㅡ + ㄹ | `0xAC00 + (0 × 588) + (18 × 28) + 8 = 0xAE00` | `U+AE00` | geul |
| 닭 | ㄷ + ㅏ + ㄺ | `0xAC00 + (3 × 588) + (0 × 28) + 9 = 0xB2ED` | `U+B2ED` | dak (cluster coda ㄺ → `[k̚]`) |

**Decomposition Formula**

The inverse: given a syllable codepoint S in `U+AC00–U+D7A3`, recover the jamo indices.

1. `offset = S − 0xAC00`
2. `jongseong_index = offset mod 28`
3. `jungseong_index = (offset ÷ 28) mod 21`   (integer division)
4. `choseong_index = offset ÷ 588`   (integer division)

---

*Compiled by Shin.*

## Cross-Reference to the Companion Guides

Cross-reference relating this Korean (한국어) IPA pronunciation guide to its six companion guides: the three Indo-European guides — English, French, and Spanish — and the three Afroasiatic Semitic guides — Classical Syriac (Peshitta), Biblical Aramaic, and Biblical Hebrew. Korean is the FIRST member of this guide family that is neither Indo-European nor Semitic: it is Koreanic, almost universally described as a language ISOLATE (no securely demonstrated relatives), and it is simultaneously the FIRST East Asian / CJK-region guide and the FIRST guide written in a FEATURAL script (Hangul 한글). Where the Semitic guides cross-reference one another within a single family, and the Indo-European guides cross-reference one another as branches of one stock, this section is TRIPLY contrastive: it documents the wide typological gap between Korean and BOTH the Indo-European and the Semitic blocks, while noting the shared descriptive apparatus (IPA 2015, phonemic vs phonetic notation, articulatory place/manner classification) that lets all seven guides be read against one another. It is a contrastive bridge, NOT a claim of genetic relationship: Korean is related to none of the other six; only the IPA framework is fully shared. Korean is documented here in TWO parallel reference standards — STANDARD SOUTH KOREAN (표준어 *pyojun-eo*, educated Seoul speech) and NORTH KOREAN (문화어 *munhwaeo*, Pyongyang standard) — the Korean analogue of the English guide's GA/RP pairing and the Spanish guide's Castilian/Latin-American pairing.

### Shared Framework

All seven guides (Korean, English, French, Spanish, Peshitta, Biblical Aramaic, Biblical Hebrew) are built on the same descriptive linguistic apparatus, which makes their pronunciation data directly comparable even though Korean is unrelated to every one of the other six.

- Primary and sole pronunciation system is the International Phonetic Alphabet (IPA), 2015 revision; orthography (here Hangul) is never the authoritative phonetic record, and Korean spelling is in any case MORPHOPHONEMIC — it preserves morpheme shape rather than surface sound, so IPA is indispensable.
- Phonemic transcriptions are written between /slashes/; narrow phonetic transcriptions are written between [brackets].
- Consonants are classified by place of articulation, manner of articulation, and a laryngeal/voicing dimension (the IPA pulmonic consonant chart); Korean replaces the voiced~voiceless contrast of the other six with a THREE-WAY laryngeal contrast (lax/plain vs tense/fortis vs aspirated).
- Vowels are classified by height, backness, and roundedness (the IPA vowel chart); Korean, like Spanish and unlike English/French and the Semitic guides, has NO phonemic length in the standard modern system and minimal vowel reduction.
- Suprasegmental marks are shared where relevant: `ʰ` aspiration, the combining tense diacritic `◌͈` (U+0348, combining double vertical line below) for the fortis series, the tie bar `◌͡◌` for affricates and on-glides, and the under-arch `◌̯` for non-syllabic glides. Korean uses NO stress mark (`ˈ`) and NO tone mark in the standard, because Standard Korean has neither lexical stress nor lexical tone.
- Each guide documents two parallel reference traditions of one language: Korean uses Standard South Korean (표준어, Seoul) and North Korean (문화어, Pyongyang); English uses General American (GA) and Received Pronunciation (RP/SSBE); Spanish uses Castilian and Latin American; French uses standard reference (Parisian-based) pronunciation; the Semitic guides use Eastern/Western (Peshitta) or reconstructed reading traditions (e.g. Tiberian for Hebrew and Biblical Aramaic).

Because the framework is identical, an IPA symbol means the same articulatory target in every guide. `/m/`, `/n/`, `/s/`, `/k/` denote the same sounds in Korean as in English, French, Spanish, Syriac, Aramaic, or Hebrew; only the phoneme inventories, the laryngeal organization, the distributions, the allophonic rules (Korean's rich coda neutralization, liaison, nasalization, etc.), and the suprasegmental systems differ. Korean's most distinctive contribution to the set — the tense/fortis series transcribed with `◌͈` — has no phonemic counterpart in any other guide.

### Typological Contrasts

| Feature | Korean | Indo-European (English, French, Spanish) | Semitic (Syriac, Biblical Aramaic, Biblical Hebrew) |
|---|---|---|---|
| Language family | Koreanic; Korean is almost universally treated as a language ISOLATE — it has no securely demonstrated genetic relatives (the historical 'Altaic' grouping with Turkic/Mongolic/Tungusic, and proposals linking it to Japonic, are not established). This makes Korean the only guide in the set with no living or attested family ties to any companion. | English is Indo-European > Germanic > West Germanic; French is Indo-European > Italic > Romance > Gallo-Romance; Spanish is Indo-European > Italic > Romance > Ibero-Romance. The three IE guides are related to one another (French and Spanish closely, as Romance siblings) but NOT to Korean. | Syriac and Biblical Aramaic are Afroasiatic > Semitic > Northwest Semitic (Aramaic branch); Biblical Hebrew is Northwest Semitic (Canaanite branch). The Semitic three are closely related to one another but unrelated to Korean and to the Indo-European guides. |
| Position in the guide family (firsts) | Korean is the FIRST non-Indo-European AND non-Semitic guide, the FIRST East Asian / CJK-region language documented, the FIRST language isolate, the FIRST agglutinative language, the FIRST guide with a featural alphabet (Hangul), and the FIRST guide whose core consonant system is organized by a three-way LARYNGEAL contrast rather than by voicing. It is the maximal typological outlier of the set. | English, French, and Spanish are all fusional Indo-European languages written in the Latin alphabet — the established 'core' against which Korean's novelty is measured. | Peshitta, Biblical Aramaic, and Biblical Hebrew are root-and-pattern Afroasiatic languages written in right-to-left abjads — themselves a strong contrast to the IE guides, but still sharing a voicing-based laryngeal system that Korean does not. |
| Morphological type | AGGLUTINATIVE: grammar is built by stringing transparent, largely invariant suffixes onto a stem in fixed order — case particles, tense/aspect, honorific and speech-level markers — e.g. 가다 'go' → 가시었습니다 (morpheme segmentation, not strict RR: *ga-si-eoss-seumnida* = go + HONORIFIC + PAST + DEFERENTIAL-DECLARATIVE; strict RR of the spelled form is *gasieotseumnida*, surface pronunciation [kaɕiʌt̚s͈ɯmnida]). Each morpheme keeps a stable shape and one meaning; there is essentially no fusion or templatic interleaving. | English is predominantly concatenative/fusional with strong analytic tendencies (function words + word order); French and Spanish are more richly fusional, packing several grammatical categories into single inflectional endings (Spanish *hablábamos* = stem + tense/aspect + person/number fused). None is agglutinative in the clean, one-suffix-one-meaning Korean sense. | Root-and-pattern (templatic, nonconcatenative): meaning is built from a discontinuous (usually triconsonantal) root interleaved with vowel/consonant templates (k-t-b → *katab*, *ktib*, *maktub*). This interdigitation is the structural opposite of Korean's linear suffixing — Korean and Semitic morphology lie at opposite ends of the typological space. |
| Basic word order | Rigidly HEAD-FINAL SOV (Subject–Object–Verb): the verb closes the clause, modifiers precede heads, the language uses POSTpositions (particles) rather than prepositions, and relative clauses precede their noun. Word order within the clause is otherwise relatively free because case particles mark grammatical roles. | English, French, and Spanish are basically SVO (Subject–Verb–Object) and use PREpositions; Romance allows freer subject placement than English but all three keep the verb medial, not final. | Classical Syriac, Biblical Aramaic, and Biblical Hebrew tend toward VSO (verb-initial), especially in narrative (Hebrew *wayyiqtol* chains), though SVO also occurs. Korean's strict verb-FINAL order is thus opposite to the Semitic verb-INITIAL tendency and distinct from the verb-MEDIAL Indo-European pattern. |
| Writing system, structure, and direction | Hangul (한글), written LEFT-to-RIGHT, is a FEATURAL alphabet: consonant letter SHAPES iconically depict the articulator, and sounds that share a feature share a base shape (`ㄱ`→`ㅋ`→`ㄲ`; `ㄴ`→`ㄷ`→`ㅌ`→`ㄸ`; `ㅁ`→`ㅂ`→`ㅍ`→`ㅃ`; `ㅅ`→`ㅈ`→`ㅊ`). Individual letters (자모 *jamo*) are then composed into square SYLLABLE BLOCKS (초성 onset / 중성 medial / 종성 coda). No other guide uses a featural script or syllable-block composition. | English, French, and Spanish use the Latin (Roman) alphabet, a segmental alphabet written left-to-right with separate consonant and vowel letters laid out linearly; letter shapes are arbitrary, not featural. | Syriac uses the Syriac abjad; Biblical Aramaic and Biblical Hebrew use the Hebrew square abjad — both written RIGHT-to-LEFT, encoding consonants as letters and marking vowels only optionally via later pointing (Syriac dots; Tiberian niqqud). Korean differs on every axis: direction, featural design, full vowel representation, and square-block layout. |
| Core laryngeal organization of stops/affricates | A THREE-WAY laryngeal contrast among the obstruents with NO phonemic voicing: LAX/plain `ㄱㄷㅂㅈ` /k t p tɕ/ (voiced [ɡ d b dʑ] only allophonically between voiced sounds), TENSE/fortis `ㄲㄸㅃㅉㅆ` /k͈ t͈ p͈ tɕ͈ s͈/ (transcribed with `◌͈`), and ASPIRATED `ㅋㅌㅍㅊ` /kʰ tʰ pʰ tɕʰ/. Voicing is never contrastive in Korean. | English, French, and Spanish all use a TWO-WAY VOICING contrast (/p/ vs /b/, /t/ vs /d/, /k/ vs /ɡ/). English aspirates voiceless stops in stressed onset ([pʰ tʰ kʰ]) but only allophonically; French and Spanish keep them unaspirated. None has a tense/fortis series. | The Semitic guides also lack the Korean tense series; their distinctive obstruent dimension is the EMPHATIC (pharyngealized) set (Teth /tˤ/, Tsade /sˤ/) plus a voicing contrast, alongside Begadkephat hard~soft spirantization. Korean's three-way lax/tense/aspirated split is unique in the set; the closest superficial parallel — Korean aspiration — is allophonic in English but PHONEMIC in Korean. |
| Consonant inventory — guttural and emphatic region | Korean has only ONE back/glottal consonant, /h/ (`ㅎ`), which lenites and often deletes intervocalically. It has NO pharyngeals, NO emphatics, NO uvulars, and NO phonemic glottal stop. It also lacks /f v θ ð z ʃ ʒ/ entirely. Its rhotic is a single /l ~ ɾ/ phoneme: tap [ɾ] as an intervocalic onset, lateral [l] in coda and in geminate `ㄹㄹ`. | English adds /f v θ ð s z ʃ ʒ/ and an approximant rhotic [ɹ]; French and Spanish add /f/ (and French /v z ʃ ʒ/, uvular /ʁ/; Spanish velar /x/, trill/tap /r ɾ/). All have richer fricative inventories than Korean. | The Semitic guides add the full guttural/emphatic apparatus — pharyngeals /ħ/ (Heth) and /ʕ/ (Ayin), glottals /ʔ/ (Aleph) and /h/, emphatics /tˤ sˤ/, uvular /q/ (Qoph), and /v z/ etc. from spirantization. Korean shares with them only the plain /h/; everything else in their guttural/emphatic zone is foreign to Korean, and conversely Korean's tense series is foreign to them. |
| Vowel inventory | A moderate monophthong system: modern Seoul ~7–8 (/a ʌ o u ɯ i e/, with `ㅐ`/`ㅔ` largely merged to [e̞] — the 애/에 merger), conservatively up to 10 (adding front rounded /ø/ `ㅚ` and /y/ `ㅟ`, usually diphthongized to [we]/[wi]). On-glide diphthongs are built with /j/, /w/, and /ɰ/ (the last only in `ㅢ` /ɰi/). There is no phonemic length in the standard and essentially no reduction. | English has a large system (~11–12 monophthongs plus phonemic diphthongs FACE/PRICE/CHOICE/MOUTH/GOAT) with pervasive schwa reduction; French has ~11–13 oral vowels PLUS nasal vowels /ɛ̃ ɑ̃ ɔ̃/ and front rounded /y ø œ/; Spanish has a clean 5-vowel system /a e i o u/ with no reduction. Korean's /ɯ/ (close back UNROUNDED) and its conservative front rounded /ø y/ set it apart; it shares Spanish's no-length, no-reduction profile but is larger than Spanish. | Smaller systems (Peshitta Eastern 7, Western 5; Tiberian 7) that, unlike Korean, include a reduced vowel (shewa) and lack Korean's /ɯ/ and front rounded vowels. Korean's glide-based diphthong set is also larger than the marginal Semitic glide sequences. |
| Syllable structure and coda behavior | Strict (C)(G)V(C): at most one onset consonant, an optional on-glide G (/j w/), a vowel, and at most one coda. There are NO onset clusters. The coda (받침 *batchim*) NEUTRALIZES to just 7 sounds [k t p l m n ŋ]; every written single or cluster coda reduces to one of these when pronounced, and cluster-jamo codas (`ㄳ ㄵ ㄺ ㄻ ㄼ` …) simplify to a single pronounced consonant. Across word/morpheme boundaries a coda re-syllabifies onto a following vowel (연음 liaison). | English permits heavy clusters at both edges (*strengths* /strɛŋkθs/); French and Spanish allow some onset clusters (with /l r/) and codas, far richer than Korean's. None neutralizes codas to a fixed 7-sound set. | Semitic syllables center on the consonantal root and tolerate clusters that Korean's (C)(G)V(C) frame forbids. Korean's rigorously simple syllable canon and its 7-way coda neutralization are unique in the set. |
| Signature phonological rules | Korean's grammar of pronunciation is unusually rich and is the heart of this guide: 연음 (liaison/resyllabification), 음절의 끝소리 규칙 (7-sound coda neutralization), 비음화 (nasalization: obstruent → nasal before a nasal), 유음화 (lateralization: `ㄴ`→[l] next to `ㄹ`), 경음화 (tensification: plain obstruent → tense after an obstruent coda), 격음화 (aspiration: `ㅎ` + plain stop → aspirated), 구개음화 (palatalization: `ㄷ`/`ㅌ` + i/j → [tɕ]/[tɕʰ]), and ㄴ-첨가 (n-insertion at compound boundaries before i/j). Crucially, the 두음법칙 (initial-sound rule) is a SOUTH↔NORTH divergence: South changes word-initial `ㄹ`/`ㄴ` (여자, 노동) while North RETAINS them (녀자, 로동). | English has assimilation, flapping, and reduction; French has liaison/enchaînement and elision; Spanish has /b d ɡ/ spirantization and /s/-voicing. These are real but fewer and less pervasive than Korean's interlocking sandhi rules. | Begadkephat spirantization and gemination are the headline Semitic processes. None of the other six has anything matching the density of Korean's obligatory cross-boundary sandhi (nasalization, lateralization, tensification, neutralization) all operating together. |
| Suprasegmentals: stress, tone, and prosody | Standard Korean has NO lexical stress and NO lexical tone. Prosody is organized into ACCENTUAL PHRASES (AP) carrying a phrase-level tune (commonly LHLH); Seoul Korean is undergoing a tonogenetic shift in which the onset's laryngeal class conditions the following pitch. (Pitch-ACCENT dialects that DO keep lexical pitch — Gyeongsang in the South-East, Hamgyŏng in the North-East — are noted only as asides.) | English has lexical, contrastive STRESS (ˈrecord vs reˈcord) and is stress-timed; Spanish also has lexical contrastive stress (*término*/*termino*/*terminó*) and is syllable-timed; French has FIXED phrase-final stress, not lexical, and is syllable-timed. All three foreground stress, which Korean lacks entirely. | Stress in the Semitic guides is largely predictable from word structure (typically final or penultimate). Korean is the only guide of the seven with NO word-level stress AND NO lexical tone, relying instead on phrase-level intonation — a prosodic profile unlike any companion. |
| Honorifics and speech levels | Korean has a grammatically PERVASIVE honorific and speech-level system: subject honorification (the suffix -시- -si-), addressee-oriented speech levels (합니다체 deferential, 해요체 polite, 해체 casual, etc.), and an extensive honorific/humble vocabulary. Social relationship is encoded morphologically in nearly every sentence. | English has only lexical politeness and no grammatical honorific system; French and Spanish have a single T/V pronoun distinction (*tu*/*vous*, *tú*/*usted*) but nothing approaching Korean's multi-tiered, suffix-driven system. | The Semitic guides have no comparable grammaticalized speech-level system. Korean's honorific morphology is a typological feature with no real analogue anywhere else in the set, and it directly shapes pronunciation by selecting different (often longer, suffix-laden) surface forms. |

### Companion Guides

**Indo-European guides**

- **English** — `english_pronunciation_guide.json`. Modern English (Indo-European > Germanic), documented in General American (GA) and Received Pronunciation (RP/SSBE). Shares with Korean only the GA/RP-style two-standard format and a few plain consonants; differs sharply in family, SVO word order, voicing-based stops, a large reducing vowel system, lexical stress, and the Latin alphabet. English aspiration ([pʰ tʰ kʰ]) is allophonic, whereas Korean aspiration is phonemic — an instructive near-miss for learners crossing between the two.
- **French** — `french_pronunciation_guide.json`. Modern Standard French (Indo-European > Italic > Romance), Parisian-based reference pronunciation. Like Korean it is syllable-timed in feel and has front rounded vowels (/y ø œ/) that resonate with conservative Korean `ㅟ` /y/ and `ㅚ` /ø/ — the single closest VOWEL parallel to Korean in the set — but it diverges on family, fixed phrase-final stress, nasal vowels (absent in Korean), uvular /ʁ/, and the Latin script.
- **Spanish** — `spanish_pronunciation_guide.json`. Modern Spanish (Indo-European > Italic > Romance), documented in Castilian (distinción) and Latin American (seseo). The closest companion to Korean in two respects: a no-phonemic-length, low-reduction vowel system, and a tap [ɾ] that matches Korean's intervocalic `ㄹ` allophone. It diverges on family, fusional morphology, SVO order, voicing-based stops, lexical stress, and the trill/tap phonemic contrast (Korean has no trill and no rhotic phoneme contrast). The most useful single comparison for Korean's vowels and its tap rhotic.

**Semitic guides**

- **Peshitta** — `peshitta_pronunciation_guide.json`. Classical Syriac (Aramaic), the Peshitta reading tradition. Documents Eastern (Madnhaya) and Western (Serto) traditions in parallel, the Begadkephat spirantization rule, guttural and emphatic consonants, and the Syriac abjad (`U+0700`–`U+074F`). Unrelated to Korean (Afroasiatic vs Koreanic isolate) and maximally distant in morphology (root-and-pattern vs agglutinative) and script (right-to-left abjad vs featural Hangul); it shares with Korean only a handful of plain IPA consonants (/m n s k t p h/ and similar).
- **Biblical Aramaic** — `biblical_aramaic_pronunciation_guide.json`. Biblical Aramaic / Jewish Literary Aramaic, as preserved in the Tiberian pointing of the Aramaic portions of the Hebrew Bible (Daniel, Ezra). Northwest Semitic (Aramaic branch); uses the Hebrew square abjad with Tiberian niqqud. Shares emphatic/guttural consonants and triconsonantal root morphology with Syriac and Hebrew; unrelated to Korean and contrasting with it on every major typological axis.
- **Biblical Hebrew** — `biblical_hebrew_pronunciation_guide.json`. Biblical (Classical) Hebrew in the Tiberian reading tradition. Northwest Semitic (Canaanite branch); uses the Hebrew square abjad with Tiberian niqqud. Notable for the prefixed definite article /ha-/ with following gemination, the Tiberian uvular Resh /ʁ/, and a 7-vowel system with shewa; unrelated to Korean. Useful to Korean readers mainly as a study in how a voicing-plus-emphatic obstruent system differs from Korean's lax/tense/aspirated three-way contrast.

### Shared IPA Symbols

IPA symbols organized by how they relate Korean to its six companions. Korean's three-way laryngeal obstruent system means the overlap is narrower than between, say, English and Spanish: Korean shares the NASALS, plain /h/, /s/, the glides, and the bare place values of its lax stops, but its tense series is Korean-only and the Semitic gutturals/emphatics (and many IE fricatives) are absent from Korean. The symbol denotes the same articulatory target in every guide; the languages differ in how these phonemes pattern, not in what the symbols mean.

#### Symbols Shared with the Companions

| IPA | Name | Korean | Other guides |
|---|---|---|---|
| `m` | voiced bilabial nasal | /m/ (`ㅁ`) — onset and coda (마음 *ma-eum*; 밤 *bam*); one of the 7 neutralized coda sounds | English/French/Spanish /m/; Mem / Mim in all three Semitic guides — the same sound everywhere |
| `n` | voiced alveolar nasal | /n/ (`ㄴ`) — onset and coda (나 *na*; 산 *san*); a coda target and the output of 비음화 nasalization | English/French/Spanish /n/; Nun in all three Semitic guides |
| `ŋ` | voiced velar nasal | /ŋ/ — the value of `ㅇ` ONLY in coda position (강 *gang*); as an ONSET, `ㅇ` is a silent placeholder, not /ŋ/ | English /ŋ/ (sing) — a phoneme; in French/Spanish only an allophone of /n/ before velars; not a primary Semitic phoneme. Korean uses it as a full coda phoneme. |
| `h` | voiceless glottal fricative | /h/ (`ㅎ`); lenites and often DELETES between voiced sounds, and combines with a following plain stop to aspirate it (격음화) | English /h/; absent (or marginal) in French; Spanish has [h] only as a regional realization of /s/ or /x/; Semitic He /h/ (distinct from pharyngeal Heth /ħ/). Korean shares the plain /h/ but adds its distinctive aspiration-merger behavior. |
| `s` | voiceless alveolar fricative | /s/ (`ㅅ`); palatalizes to [ɕ] before /i/ or /j/ (시 [ɕi]); note Korean ALSO has a TENSE counterpart /s͈/ (`ㅆ`) — see Korean-only below | English/French/Spanish /s/; Semkath / Samekh / Sin in the Semitic guides (distinct from emphatic Tsade /sˤ/). The plain symbol matches; Korean's tense /s͈/ has no companion. |
| `k` | voiceless velar plosive | /k/ — the LAX stop `ㄱ`; voices to [ɡ] between voiced sounds (아기 [aɡi]); also one of the 7 coda sounds [k] | English /k/ (aspirated [kʰ] in stressed onset); French/Spanish unaspirated /k/; Kaph in the Semitic guides. The bare place/manner value matches; Korean adds tense `ㄲ` /k͈/ and aspirated `ㅋ` /kʰ/ alongside it. |
| `t` | voiceless alveolar/dental plosive | /t/ — the LAX stop `ㄷ`; voices to [d] intervocalically; also a coda sound [t] (the neutralization target of `ㅅ ㅆ ㅈ ㅊ ㅌ ㅎ` in coda) | English /t/ (aspirated [tʰ]; GA flap [ɾ]); French/Spanish dental unaspirated /t/; Taw in the Semitic guides. Korean adds tense `ㄸ` /t͈/ and aspirated `ㅌ` /tʰ/. |
| `p` | voiceless bilabial plosive | /p/ — the LAX stop `ㅂ`; voices to [b] intervocalically; also a coda sound [p] | English /p/ (aspirated [pʰ]); French/Spanish unaspirated /p/; Pe (hard allophone) in the Semitic guides. Korean adds tense `ㅃ` /p͈/ and aspirated `ㅍ` /pʰ/. |
| `tɕ` | voiceless alveolo-palatal affricate | /tɕ/ — the LAX affricate `ㅈ`; voices to [dʑ] intervocalically (the only affricate place in Korean) | Nearest companion is the postalveolar /tʃ/ (English CHurch; Spanish ch *mucho*) — a similar but NOT identical place of articulation (alveolo-palatal vs postalveolar). French has /tʃ/ only in loans; not a primary Semitic phoneme. Korean adds tense `ㅉ` /tɕ͈/ and aspirated `ㅊ` /tɕʰ/. |
| `j` | voiced palatal approximant (glide) | /j/ — the on-glide in `ㅑ ㅕ ㅛ ㅠ ㅒ ㅖ` (야 *ja*, 여 *jʌ*) | English /j/ (yes); French /j/ (yeux); Spanish /j/ (tiene); Yodh / Yud in the Semitic guides |
| `w` | voiced labial-velar approximant (glide) | /w/ — the on-glide in `ㅘ ㅙ ㅝ ㅞ` (and in the usual diphthongal realizations of `ㅚ ㅟ`): 와 *wa*, 워 *wʌ* | English /w/ (we); French /w/ (oui); Spanish /w/ (cuota); Waw / Vav (consonantal) in the Semitic guides |
| `ɾ` | voiced alveolar tap | /l ~ ɾ/ — the SINGLE Korean liquid `ㄹ`, realized as the tap [ɾ] when it is an intervocalic onset (나라 [naɾa]) | Spanish /ɾ/ is a full phoneme contrasting with the trill /r/ (*pero*/*perro*); English [ɾ] is only the GA allophone of /t d/ (water); not a distinct phoneme in French or the Semitic guides. Korean's [ɾ] is an ALLOPHONE of /l/, not a phoneme — closest in sound to Spanish but not in status. |
| `l` | voiced alveolar lateral approximant | /l ~ ɾ/ — the same liquid `ㄹ`, realized as lateral [l] in CODA and in geminate `ㄹㄹ` (말 [mal], 빨리 [p͈alli]) | English /l/ (clear [l] and dark [ɫ]); French/Spanish clear /l/; Lamadh / Lamed in the Semitic guides. Korean has no dark [ɫ]; its [l]~[ɾ] are one phoneme split by position. |

#### Korean-Only Symbols

Korean phonemes with NO counterpart anywhere else in the seven-guide set — chiefly the entire TENSE/fortis series (transcribed with the combining double vertical line below, `U+0348`) and a few vowels. These are the articulatory targets a reader of any companion guide must learn entirely anew for Korean.

| IPA | Jamo | Description |
|---|---|---|
| `k͈` | `ㄲ` | Tense velar stop; phonemic, contrasting with lax /k/ and aspirated /kʰ/ (e.g. 까 vs 가 vs 카). No voicing- or emphatic-based system in the other guides has a fortis stop like this. |
| `t͈` | `ㄸ` | Tense alveolar stop (따/다/타). Korean-only. |
| `p͈` | `ㅃ` | Tense bilabial stop (빠/바/파). Korean-only. |
| `tɕ͈` | `ㅉ` | Tense alveolo-palatal affricate (짜/자/차). Korean-only. |
| `s͈` | `ㅆ` | Tense alveolar fricative (쌀 'rice' vs 살 'flesh'). The only tense FRICATIVE; no companion has it. |
| `ɯ` | `ㅡ` | Close back UNROUNDED vowel. Absent from English, French, Spanish, and the Semitic guides; a hallmark Korean vowel. |
| `ɰ` | `ㅢ` (on-glide) | The on-glide of `ㅢ` /ɰi/ — a velar/unrounded approximant glide. Occurs in no companion guide. |
| `ø`, `y` | `ㅚ`, `ㅟ` | As MONOPHTHONGS (conservative Korean): front rounded vowels that COINCIDE with French /ø/ and /y/ in symbol/value — the one place Korean's vowels overlap a companion — but in most modern Korean they diphthongize to [we]/[wi], so they are listed here as Korean's (semi-)distinctive set rather than as fully shared. |

#### Symbols Absent in Korean

Phonemes prominent in the companion guides that Korean lacks. Korean has NO phonemic voicing contrast (voiced obstruents appear only as intervocalic allophones), no labiodentals, no dental fricatives, no postalveolar sibilants as phonemes, and none of the Semitic gutturals/emphatics. These are the principal targets a Korean speaker must acquire to read the other six guides.

| IPA | Found in | Note on absence in Korean |
|---|---|---|
| `b d ɡ dʑ` | English/French/Spanish phonemes; Semitic hard allophones | Voiced obstruents — phonemes elsewhere; in Korean they exist ONLY as intervocalic allophones of lax /p t k tɕ/, never contrastively |
| `f v` | English/French/Spanish /f/; English/French /v/; Semitic spirantized Pe/Beth | Labiodental fricatives — Korean has neither and substitutes /p~pʰ/ or /b/ in loans |
| `θ ð` | English /θ ð/; Castilian /θ/; Semitic spirantized Taw/Daleth | Dental fricatives — absent in Korean |
| `z` | English/French/Spanish and Semitic Zayin | Voiced alveolar fricative — absent in Korean, which has no [z] even allophonically |
| `ʃ ʒ` | English/French phonemes | Postalveolar sibilants — Korean has [ɕ] only as an allophone of /s/ before /i j/, and no /ʒ/ at all |
| `ʁ` | French and Tiberian-Hebrew Resh | Uvular rhotic — absent in Korean |
| `r` | Spanish and Syriac/Aramaic Resh | Alveolar TRILL — Korean has only the tap/lateral allophones of `ㄹ`, never a trill |
| `ħ ʕ` | Semitic Heth/Ayin | Pharyngeal fricatives — absent in Korean |
| `ʔ` | Semitic Aleph/Alaph | Glottal stop — not phonemic in Korean |
| `q` | Semitic Qoph | Voiceless uvular plosive — absent in Korean |
| `tˤ sˤ` | Semitic Teth/Tsade | Emphatic/pharyngealized obstruents — absent in Korean |
| `x` | Spanish jota and Semitic spirantized Kaph | Voiceless velar fricative — absent in Korean as a phoneme |
| `ɛ̃ ɑ̃ ɔ̃` | French nasal VOWELS | Korean has no nasal vowels |

### Reader Tiers

Unlike the single Latin-text companions, the Korean Peshitta ships FOUR reader tiers, because Korean uses a non-Latin native script. These are companion materials referenced throughout this guide and should be read alongside the IPA.

| Tier | Description |
|---|---|
| Scholarly | Language-neutral Latin transcription, the precise scholarly readback. |
| Pretty | Language-neutral Latin transcription, smoothed for readability. |
| Hangul (한글) | The native composed syllable blocks (the authoritative Korean-script form). |
| Revised Romanization (RR) | The official South Korean (2000) romanized readback of the Hangul. |

**Companion directories** (repo-relative):

- `Korean/Peshita_Korean/Scholarly/`
- `Korean/Peshita_Korean/Pretty/`
- `Korean/Peshita_Korean/Hangul/`
- `Korean/Peshita_Korean/Romanized/`
- `Korean/korean_pronunciation_guide.md`

> **Note:** Hangul is the primary native-script tier; RR (Revised Romanization) and the older McCune–Reischauer (MR, with breves ŏ ŭ and apostrophes) are the two romanization systems a reader may meet — RR is the one used for the readback tier here.

> **Note:** Unlike the Semitic guides' cross_reference sections, which trace correspondences WITHIN one family, and the Indo-European guides', which trace correspondences across branches of ONE stock, this section is TRIPLY contrastive: Korean shares the IPA description framework with all six companions yet is genetically unrelated to every one of them — it is a Koreanic ISOLATE and the FIRST non-Indo-European, non-Semitic, East Asian (CJK-region), agglutinative, featural-script guide in the family. Its distinctive profile across the set is the THREE-WAY laryngeal contrast (lax `ㄱㄷㅂㅈ` vs tense `ㄲㄸㅃㅉㅆ` /◌͈/ vs aspirated `ㅋㅌㅍㅊ`) with NO phonemic voicing; a moderate vowel system including close-back-unrounded /ɯ/ and conservative front rounded /ø y/, with no length and little reduction; a rigid (C)(G)V(C) syllable with 7-sound coda neutralization; an exceptionally dense set of obligatory sandhi rules (연음, 비음화, 유음화, 경음화, 격음화, 구개음화, ㄴ-첨가); rigid head-final SOV order with postpositions; a pervasive grammatical honorific system; and NO lexical stress or tone, organized instead into accentual phrases. Throughout, Standard South Korean (표준어, Seoul) and North Korean (문화어, Pyongyang) are documented in parallel — most visibly in the 두음법칙 initial-sound rule (South 여자/노동 vs North 녀자/로동) — as the two reference standards of the language, the Korean analogue of the GA/RP and Castilian/Latin-American pairings elsewhere in the set.
