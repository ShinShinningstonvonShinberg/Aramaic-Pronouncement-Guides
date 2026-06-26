# Arabic IPA Pronunciation Guide

**Version:** 1.0.0
**Date:** 2026-06-26
**Language:** Arabic (العربية) (ISO 639-3: `arb`)  
**Encoding:** UTF-8  
**IPA Standard:** IPA (International Phonetic Alphabet, 2015 revision)  
**Reference Standards:** Modern Standard Arabic (الفصحى) and Classical/Quranic Arabic  

Machine-readable IPA-based pronunciation guide for Arabic (العربية *al-ʿarabiyya*), covering Modern Standard Arabic (MSA, الفصحى *al-fuṣḥā*) and Classical/Quranic Arabic (the *tajwīd* careful-recitation register) in parallel. All pronunciation data is encoded in the International Phonetic Alphabet (IPA, 2015 revision) as the primary and only system. Designed for AI-assisted pronunciation, text-to-speech reference, second-language teaching, scriptural recitation support, and language documentation. As the FIRST target language documented in the same Central Semitic family as the project's Syriac/Aramaic source, this guide is framed throughout as a sibling-language map: Arabic is a Semitic SIBLING of the source and natively hosts the pharyngeals, emphatics, interdentals, and uvulars that make it the most faithful phonological match in the project for the source inventory.

### Varieties Covered

- **Modern Standard Arabic (MSA)** — اللغة العربية الفصحى (*al-luġa al-ʿarabiyya al-fuṣḥā*). The contemporary pan-Arab literary and formal standard used across the Arabic-speaking world in news media, education, official writing, formal speech, and modern literature — the direct descendant and modernization of Classical Arabic, sharing its grammar and phonology while expanding the lexicon. Formal/literary register with no native speakers but universally taught as the prestige written and broadcast standard. It preserves the full 28-consonant inventory including the pharyngeals ح /ħ/ and ع /ʕ/, the emphatics ط /tˤ/ ص /sˤ/ ض /dˤ/ ظ /ðˤ/, the interdentals ث /θ/ ذ /ð/ ظ /ðˤ/, and the uvular ق /q/; three short vowels /a i u/ and three long /aː iː uː/ with diphthongs /aj aw/; rule-based, weight-sensitive, non-phonemic stress with phonemic gemination (shadda); and fully operative definite-article assimilation (sun vs moon letters) and emphasis spread (*tafkhīm*). Reference realizations: ج (jīm) = [dʒ]; ق (qāf) = [q]; interdentals retained as [θ ð ðˤ]. It plays the role of one of two co-equal documented standards (compare General American in the English guide and the Eastern/Madnhaya tradition in the Peshitta guide).
- **Classical / Quranic Arabic (CA)** — العربية الكلاسيكية / لغة القرآن (*al-ʿarabiyya al-kilāsīkiyya / luġat al-Qurʾān*). The older codified form of the language, standardized by the early Arab grammarians and definitively represented by the language of the Qurʾān and classical literature, read in the careful-recitation register governed by the rules of *tajwīd* (تجويد). Liturgical/scriptural and classical-literary register — the genre-appropriate standard for scripture and the historical model from which MSA derives. It preserves every MSA contrast and adds finer phonetic detail codified in *tajwīd*: full desinential inflection (*iʿrāb*) in continuous careful recitation with pausal (*waqf*) forms dropping final short vowels and tanwīn utterance-finally; the *tajwīd* articulation rules *idghām*, *ikhfāʾ*, *iqlāb*, *madd*, and *qalqala* over precise *makhārij* (articulation points); and emphasis (*tafkhīm*) vs thinning (*tarqīq*), notably on ر /r/ and the lām of the divine name الله. Reference realizations: ج (jīm) classically palatal [ɟ] (recitation commonly [dʒ], historically conservative [ɡ]); ق (qāf) = [q] as a back/emphasis-triggering consonant; ض (ḍād) = pharyngealized [dˤ] (the "language of the ḍād", لغة الضاد); interdentals fully retained as [θ ð ðˤ]. It is the conservative, contrast-maximal standard (compare Received Pronunciation in the English guide and the Western/Serto tradition in the Peshitta guide).

### Companion Files

- `Arabic/arabic_pronunciation_guide.md`
- `Arabic/Peshita_Arabic/Scholarly/`
- `Arabic/Peshita_Arabic/Pretty/`
- `Arabic/Peshita_Arabic/Vocalized/`
- `Arabic/Peshita_Arabic/Unvocalized/`
- `peshitta_pronunciation_guide.json`
- `biblical_aramaic_pronunciation_guide.json`
- `biblical_hebrew_pronunciation_guide.json`
- `English/english_pronunciation_guide.json`
- `Spanish/spanish_pronunciation_guide.json`

### Notes

- Arabic is written right-to-left in the Arabic abjad, like its Semitic companion guides (Syriac/Aramaic and Hebrew) and unlike the left-to-right Latin of the English guide.
- The abjad records consonants and long vowels; short vowels (harakat) are normally unwritten, so the same consonantal skeleton can spell several words — this is why the Vocalized vs Unvocalized reader split matters and why IPA (not spelling) is the authoritative pronunciation record here.
- Arabic is a SIBLING of the Syriac/Aramaic source within Central Semitic: it natively hosts ~25 of the source's 34 symbols 1:1, including the pharyngeals ح /ħ/ and ع /ʕ/, the emphatics ط /tˤ/ ص /sˤ/, the interdentals ث /θ/ ذ /ð/, and the back consonants خ /x/ غ /ɣ/ ق /q/ ش /ʃ/ ء /ʔ/. This makes the Arabic Peshitta reader tiers the most faithful in the whole project.
- Only a few source contrasts are not native: Arabic adds the emphatics ض /dˤ/ and ظ /ðˤ/ (absent from the source) and lacks /v p ɡ/ (resolved in the reader tier as v→ف, p→ب, ɡ→ج), plus the source /e o/ collapse to /i u/ matching attested Western Syriac vocalism — these are the only systematic gaps.
- Two reference standards are documented in parallel: Modern Standard Arabic (MSA, الفصحى) — the contemporary pan-Arab literary standard — and Classical/Quranic Arabic (the *tajwīd* careful-recitation register), which preserves every MSA contrast plus finer codified detail and is the genre-appropriate standard for scripture.
- Levantine and other spoken dialects are documented-only asides and are NOT shipped standards: urban Levantine collapses qāf ق → [ʔ] and the interdentals ث/ذ → stops, destroying the very contrasts that make Arabic a faithful match for the Semitic source.
- Emphatic (pharyngealized) consonants ط /tˤ/ ص /sˤ/ ض /dˤ/ ظ /ðˤ/ — joined functionally by ق /q/ — trigger EMPHASIS SPREAD (*tafkhīm*): adjacent vowels back and lower (e.g. /a/ → [ɑ]), reshaping local vowel quality. This pharyngealization and the true pharyngeals ح /ħ/ ع /ʕ/ are absent from English but shared with the Semitic source.
- Arabic morphology is root-and-pattern (templatic): meaning lives in a consonantal root (typically triconsonantal) interleaved with vocalic patterns, so vocalization is morphologically load-bearing and the IPA reflects the fully-realized pattern.
- The definite article الـ *al-* assimilates to following SUN LETTERS (الشَّمْس *aš-šams* 'the sun', lām assimilated) but stays before MOON LETTERS (القَمَر *al-qamar* 'the moon'); hamzat al-waṣl (the connecting hamza) elides in connected speech.
- Phonemic transcriptions use / / slashes; phonetic transcriptions use [ ] brackets. Suprasegmentals: /ː/ marks vowel length; /ˈ/ marks primary stress; /ˤ/ marks pharyngealization (emphasis); shadda gemination is shown by doubling or /ː/ on the consonant.
- Stress in Arabic is rule-based and predictable (weight-sensitive, falling on a heavy penult/antepenult), NOT phonemic — unlike English, where stress can distinguish lexemes. Gemination (shadda), however, IS contrastive.
- Case and mood endings (*iʿrāb*) are described for completeness but are NOT emitted in the source-aligned IPA: the Syriac source is caseless, and pausal (*waqf*) forms drop final short vowels and tanwīn utterance-finally.
- The realization of ج (jīm) varies by standard and region: [dʒ] in MSA, [ɡ] in Egyptian/conservative Classical, [ʒ] in Levantine — the guide uses [dʒ] as the MSA reference value.
- RTL Arabic-script values appear directly as real Unicode in this guide (e.g. العربية, كَتَبَ, الشَّمْس) rather than escaped; examples are given VOCALIZED (with harakat) for unambiguous pronunciation, and verse bodies in the reader tiers are wrapped in RLI…PDI bidi isolates.
- All IPA transcriptions use the standard 2015 IPA chart notation; romanization in scholarly prose follows DIN 31635 / ALA-LC, with Buckwalter referenced for ASCII/NLP interchange.
- Authorship: Shin.

## Table of Contents

- [How to Read This Guide](#how-to-read-this-guide)
  - [Phonemic vs phonetic notation](#phonemic-vs-phonetic-notation)
  - [Reading the IPA](#reading-the-ipa)
  - [Emphatic, pharyngeal, and interdental notation](#emphatic-pharyngeal-and-interdental-notation)
  - [The Arabic abjad, harakat, and romanization](#the-arabic-abjad-harakat-and-romanization)
  - [Right-to-left (RTL)](#right-to-left-rtl)
  - [The two parallel reference standards](#the-two-parallel-reference-standards)
- [Phonological Inventory](#phonological-inventory)
  - [Consonant Phonemes](#consonant-phonemes)
  - [Vowel Phonemes](#vowel-phonemes)
- [Consonants (الحروف الساكنة)](#consonants-الحروف-الساكنة)
  - [Reference Standards](#reference-standards)
  - [Consonant Inventory](#consonant-inventory)
  - [Unicode Codepoints](#unicode-codepoints)
  - [Natural Classes](#natural-classes)
  - [Source Inventory Mapping](#source-inventory-mapping)
- [Vowels & Harakat](#vowels--harakat)
  - [Overview](#overview)
  - [Reference Registers](#reference-registers)
  - [Vowel Inventory](#vowel-inventory)
  - [Diphthongs (Summary)](#diphthongs-summary)
  - [Allophony](#allophony)
  - [Ḥarakāt — The Vocalization Diacritics (تَشْكِيل)](#ḥarakāt--the-vocalization-diacritics-تشكيل)
  - [Classical vs MSA Vowels](#classical-vs-msa-vowels)
  - [Cross-Reference](#cross-reference)
- [Diphthongs & Long Vowels](#diphthongs--long-vowels)
  - [The Two Diphthongs](#the-two-diphthongs)
  - [Long Vowels — The Matres Lectionis (حروف المد)](#long-vowels--the-matres-lectionis-حروف-المد)
  - [Writing Length & Diphthongs in the Abjad](#writing-length--diphthongs-in-the-abjad)
  - [Monophthongization](#monophthongization)
  - [Cross-Reference to the Semitic Siblings](#cross-reference-to-the-semitic-siblings)
  - [Unicode Reference](#unicode-reference)
- [Consonant–Vowel IPA Matrix](#consonantvowel-ipa-matrix)
  - [Selection Principle](#selection-principle)
  - [Reference Vowels](#reference-vowels)
  - [Backing Legend (tafkhīm)](#backing-legend-tafkhīm)
  - [CV Matrix](#cv-matrix)
  - [Phonetic Notes](#phonetic-notes)
  - [Accent Notes](#accent-notes)
  - [Cross-References](#cross-references)
- [Suprasegmentals](#suprasegmentals)
  - [Tone](#tone)
  - [Stress](#stress)
  - [Gemination](#gemination)
  - [Vowel Length](#vowel-length)
  - [Emphasis Spread](#emphasis-spread)
  - [Tanwīn and Iʿrāb Prosody](#tanwīn-and-iʿrāb-prosody)
  - [Pausal Forms](#pausal-forms)
  - [Madd Lengthening](#madd-lengthening)
  - [Idghām and Assimilation](#idghām-and-assimilation)
  - [Hamzat al-Waṣl](#hamzat-al-waṣl)
  - [Intonation](#intonation)
  - [Summary Table](#summary-table)
  - [Cross-Reference](#cross-reference-1)
- [Syllable Structure](#syllable-structure)
  - [Obligatory Onset](#obligatory-onset)
  - [Onset](#onset)
  - [Nucleus](#nucleus)
  - [Coda](#coda)
  - [Syllable Weight](#syllable-weight)
  - [Syllable Types](#syllable-types)
  - [Non-occurring Types](#non-occurring-types)
  - [Hamzat al-Waṣl](#hamzat-al-waṣl-1)
  - [The Definite Article and Waṣl](#the-definite-article-and-waṣl)
  - [Syllabification](#syllabification)
  - [Constraints](#constraints)
  - [Cross-references](#cross-references-1)
- [Phonological Rules](#phonological-rules)
  - [Ordering of the Rules](#ordering-of-the-rules)
  - [Rules at a Glance](#rules-at-a-glance)
  - [Rule 1: التشديد / الشدة (*at-tashdīd / aš-šadda*) — Gemination (consonant doubling)](#rule-1-التشديد--الشدة-at-tashdīd--aš-šadda--gemination-consonant-doubling)
  - [Rule 2: التفخيم وانتشار الإطباق (*at-tafkhīm wa-intišār al-iṭbāq*) — Emphasis (pharyngealization) spread](#rule-2-التفخيم-وانتشار-الإطباق-at-tafkhīm-wa-intišār-al-iṭbāq--emphasis-pharyngealization-spread)
  - [Rule 3: الإمالة (*al-imāla*) — Imāla (raising/fronting of ā toward [eː]/[iː])](#rule-3-الإمالة-al-imāla--imāla-raisingfronting-of-ā-toward-eːiː)
  - [Rule 4: تقصير الصائت في المقطع المغلق (*taqṣīr aṣ-ṣāʾit fī l-maqṭaʿ al-mughlaq*) — Vowel shortening in closed syllables / unstressed reduction](#rule-4-تقصير-الصائت-في-المقطع-المغلق-taqṣīr-aṣ-ṣāʾit-fī-l-maqṭaʿ-al-mughlaq--vowel-shortening-in-closed-syllables--unstressed-reduction)
  - [Rule 5: لام التعريف: الحروف الشمسية والقمرية (*lām at-taʿrīf: al-ḥurūf aš-šamsiyya wa-l-qamariyya*) — Definite-article assimilation: sun vs moon letters](#rule-5-لام-التعريف-الحروف-الشمسية-والقمرية-lām-at-taʿrīf-al-ḥurūf-aš-šamsiyya-wa-l-qamariyya--definite-article-assimilation-sun-vs-moon-letters)
  - [Rule 6: همزة الوصل (*hamzat al-waṣl*) — Elidable (connecting) hamza](#rule-6-همزة-الوصل-hamzat-al-waṣl--elidable-connecting-hamza)
  - [Rule 7: أحكام النون الساكنة والتنوين والإدغام (*aḥkām an-nūn as-sākina wa-t-tanwīn wa-l-idghām*) — Rules of *nūn sākina* / *tanwīn* and general assimilation (*tajwīd*)](#rule-7-أحكام-النون-الساكنة-والتنوين-والإدغام-aḥkām-an-nūn-as-sākina-wa-t-tanwīn-wa-l-idghām--rules-of-nūn-sākina--tanwīn-and-general-assimilation-tajwīd)
  - [Rule 8: الإعراب: حركات الإعراب (*al-iʿrāb: ḥarakāt al-iʿrāb*) — Desinential case/mood inflection (descriptive only)](#rule-8-الإعراب-حركات-الإعراب-al-iʿrāb-ḥarakāt-al-iʿrāb--desinential-casemood-inflection-descriptive-only)
  - [Rule 9: الوقف: الصيغ الوقفية (*al-waqf: aṣ-ṣiyagh al-waqfiyya*) — Pausal forms (utterance-final waqf)](#rule-9-الوقف-الصيغ-الوقفية-al-waqf-aṣ-ṣiyagh-al-waqfiyya--pausal-forms-utterance-final-waqf)
- [MSA vs. Classical/Quranic (Register & Dialect)](#msa-vs-classicalquranic-register--dialect)
  - [Reference standards](#reference-standards-1)
  - [Differences](#differences)
  - [Spoken dialect asides (العامِّيَّة / اللَّهَجات)](#spoken-dialect-asides-العامية--اللهجات)
  - [Summary](#summary)
- [Orthography: The Arabic Abjad](#orthography-the-arabic-abjad)
  - [The Two Letter Orders](#the-two-letter-orders)
  - [Contextual (Positional) Forms](#contextual-positional-forms)
  - [Consonant Graphemes](#consonant-graphemes)
  - [Vowel Orthography](#vowel-orthography)
  - [Hamza and Its Seats](#hamza-and-its-seats)
  - [Special Letters and Devices](#special-letters-and-devices)
  - [Eastern Arabic Numerals](#eastern-arabic-numerals)
  - [Abjad Numerals (ḥisāb al-jummal)](#abjad-numerals-ḥisāb-al-jummal)
  - [Romanization Schemes](#romanization-schemes)
  - [Cognate Abjad Order (Arabic · Hebrew · Syriac)](#cognate-abjad-order-arabic--hebrew--syriac)
  - [Grapheme → Phoneme Summary](#grapheme--phoneme-summary)
  - [Unicode Blocks](#unicode-blocks)
  - [Reader-Tier Cross-Reference](#reader-tier-cross-reference)
  - [Key Points](#key-points)
- [Connected Speech & Liaison](#connected-speech--liaison)
  - [Reference Standards](#reference-standards-2)
  - [Contrast with English](#contrast-with-english)
  - [Boundary Phenomena](#boundary-phenomena)
  - [General Rules](#general-rules)
  - [Interaction of Boundary Processes](#interaction-of-boundary-processes)
  - [Register Note](#register-note)
  - [Cross-Reference](#cross-reference-2)
- [Sample Words in IPA](#sample-words-in-ipa)
  - [Coverage Matrix](#coverage-matrix)
- [Unicode Reference](#unicode-reference-1)
  - [IPA Consonant Symbols](#ipa-consonant-symbols)
  - [IPA Vowel Symbols](#ipa-vowel-symbols)
  - [Diacritics & Suprasegmentals](#diacritics--suprasegmentals)
  - [Arabic Letters](#arabic-letters)
  - [Arabic Harakat (Tashkīl)](#arabic-harakat-tashkīl)
  - [Unicode Blocks Used](#unicode-blocks-used)
  - [Cross-Reference to Sister Scripts](#cross-reference-to-sister-scripts)
- [Cross-Reference to the Semitic & Companion Guides](#cross-reference-to-the-semitic--companion-guides)
  - [Shared Framework](#shared-framework)
  - [The Semitic Family](#the-semitic-family)
  - [Typological Contrasts](#typological-contrasts)
  - [Companion Guides](#companion-guides)
  - [Shared IPA Symbols](#shared-ipa-symbols)

## How to Read This Guide

This guide records pronunciation in the International Phonetic Alphabet (IPA, 2015 revision) as the primary and only pronunciation system; Arabic-script values appear as real Unicode (RTL) and Latin transliteration is a secondary aid. A few conventions are used throughout.

### Phonemic vs phonetic notation

- **Phonemic transcription** is written between forward slashes: `/ /`. It records the contrastive sound categories (phonemes) of the language, abstracting away from predictable detail — e.g. كَتَبَ *kataba* 'he wrote' is `/ˈka.ta.ba/`.
- **Phonetic transcription** is written between square brackets: `[ ]`. It records the actual realized sounds, including allophonic detail — e.g. emphasis spread backing /a/ to `[ɑ]` next to an emphatic, as in صَلَاة *ṣalāh* 'prayer' `[sˤɑˈlaːh]`.

### Reading the IPA

- Every entry's authoritative pronunciation is its IPA. Where the Arabic spelling is ambiguous (because short vowels are normally unwritten), the IPA — not the abjad skeleton — is the record of record.
- Suprasegmentals used in this guide:

| Mark | Name | Meaning |
| --- | --- | --- |
| `ː` | length | a long vowel or geminate consonant — e.g. كِتَاب *kitāb* `/kiˈtaːb/`; gemination (shadda) may also be shown by doubling |
| `ˈ` | primary stress | precedes the syllable carrying main stress (rule-based, not phonemic) — e.g. `/ˈka.ta.ba/` |
| `ˤ` | pharyngealization | marks an emphatic (pharyngealized) consonant — e.g. ط `/tˤ/`, ص `/sˤ/` |

- Stress in Arabic is **predictable** (weight-sensitive, falling on a heavy penult/antepenult), so `ˈ` records position rather than a contrast. **Gemination** (shadda), by contrast, IS contrastive, so the length mark / doubled consonant is load-bearing.

### Emphatic, pharyngeal, and interdental notation

These three natural classes are the heart of what makes Arabic a faithful Semitic match for the source, and English has none of them. Watch for:

| Class | Letters | IPA | Notation note |
| --- | --- | --- | --- |
| Emphatic (pharyngealized) | ط ص ض ظ | `/tˤ sˤ dˤ ðˤ/` | the superscript `ˤ` marks pharyngealization; functionally joined by ق `/q/`. They trigger EMPHASIS SPREAD (*tafkhīm*): adjacent vowels back and lower, e.g. /a/ → `[ɑ]` |
| Pharyngeal | ح ع | `/ħ ʕ/` | true pharyngeal fricatives — ح voiceless, ع voiced; shared with the source, absent from English |
| Interdental | ث ذ ظ | `/θ ð ðˤ/` | true interdental fricatives, retained in the MSA/Classical reference (many spoken dialects shift these to stops or sibilants) |
| Uvular | ق | `/q/` | voiceless uvular plosive; a back consonant that participates in vowel backing |

### The Arabic abjad, harakat, and romanization

- **Abjad.** Arabic is written in a 28-letter consonantal abjad, right-to-left, in cursive script where most letters take up to four contextual shapes (initial, medial, final, isolated); the six non-connecting letters ا د ذ ر ز و join only on their right.
- **Harakat (تشكيل).** Short vowels are optional diacritics: fatḥa ـَ `/a/`, kasra ـِ `/i/`, ḍamma ـُ `/u/`; plus sukūn ـْ (vowellessness), shadda ـّ (gemination), and tanwīn ـً ـٍ ـٌ (indefinite case endings *-an -in -un*). Long vowels use the matres lectionis ا `/aː/`, و `/uː/`, ي `/iː/` (و and ي also carry the diphthongs `/aw/` and `/aj/`). Everyday text is unvocalized; fully vocalized text is standard for the Qurʾān, children's books, poetry, and pedagogy.
- **Vocalized examples.** Throughout this guide, Arabic examples are shown VOCALIZED (with harakat) for unambiguous pronunciation — e.g. الشَّمْس *aš-šams*, القَمَر *al-qamar*, مَكْتُوب *maktūb* — even though running Arabic text normally omits them.
- **Hamza.** The glottal stop ء `/ʔ/` is written standalone or on a seat (أ إ ؤ ئ); the connecting hamza (hamzat al-waṣl) on initial alif elides in connected speech.
- **Romanization.** Latin transliteration is secondary to the IPA. Scholarly prose follows **DIN 31635 / ALA-LC** (ṯ ḏ ḥ ḫ ḍ ṣ ṭ ẓ ʿ ġ q; long vowels ā ī ū), with **Buckwalter** (a strictly ASCII, reversible NLP scheme: v=ث, \*=ذ, H=ح, x=خ, S=ص, D=ض, T=ط, Z=ظ, E=ع, g=غ, q=ق, ' = hamza) referenced for ASCII/NLP interchange.

### Right-to-left (RTL)

Arabic is written and stored right-to-left, in LOGICAL order. RTL Arabic-script values appear directly as real Unicode in this guide (e.g. العربية, كَتَبَ) — the Markdown renderer handles bidi within tables and prose. In the Peshitta reader tiers, RTL verse bodies are wrapped in Unicode bidi isolates RLI (U+2067) … PDI (U+2069) so embedded Latin tokens, digits, and punctuation render correctly.

### The two parallel reference standards

Two co-equal reference standards are documented in parallel, and where they differ both transcriptions are given side by side:

- **Modern Standard Arabic (MSA, الفصحى)** — the contemporary pan-Arab literary standard. Reference values: ج = [dʒ], ق = [q], interdentals retained as [θ ð ðˤ].
- **Classical / Quranic Arabic (CA)** — the *tajwīd* careful-recitation register. Preserves every MSA contrast and adds finer codified detail (idghām, ikhfāʾ, iqlāb, madd, qalqala, makhārij; *tafkhīm* vs *tarqīq*); pausal (*waqf*) forms drop final short vowels and tanwīn utterance-finally.

The central relationship is conservation: Classical/Quranic is the contrast-maximal historical model, and MSA is its modern descendant sharing the same phonology. Spoken dialects (e.g. Levantine) are documented-only asides and are NOT shipped standards, because they collapse exactly the contrasts (qāf, interdentals) that make Arabic faithful to the source. Because Arabic is a Semitic sibling that natively hosts almost the entire source inventory, the **Arabic Peshitta reader tiers are the most faithful, near-reversible reader set in the whole project.**

## Phonological Inventory

The complete phonemic inventory of Arabic (العربية), documented in parallel for two reference standards: Modern Standard Arabic (MSA, الفُصْحى *al-fuṣḥā*) and Classical/Quranic Arabic (لُغة القُرْآن, the *tajwīd* careful-recitation register). The consonant system is shared between the two standards; Classical recitation simply realizes the same 28 contrasts with finer detail. Arabic is a Central Semitic **sister** of the source language (Syriac/Aramaic) and of Hebrew, so its signature contrasts — the pharyngeals ح ع, the pharyngealized "emphatic" series ط ص ض ظ, the interdentals ث ذ ظ, and the uvular ق — line up almost one-to-one with the source's, making it the most faithful match in the project. This section is a **summary**; the consonant series, harakāt, diphthongs, syllable structure and phonological rules are each elaborated in their own dedicated sections.

### Consonant Phonemes

All 28 consonant phonemes of Arabic arranged by place and manner of articulation (IPA standard layout). The consonant inventory is identical between Modern Standard and Classical/Quranic Arabic; only the realization of ج (*jīm*) varies by register/region (see notes).

**Total consonant phonemes:** 28  
28 consonant letters yield 28 consonant phonemes (Arabic has no *begadkephat*-style allophonic stop/fricative split, unlike Syriac and Hebrew). Inventory by manner: 8 plosives `/b t d tˤ dˤ k q ʔ/` + 1 affricate `/dʒ/` (ج, MSA) + 13 fricatives `/f θ ð s z sˤ ðˤ ʃ x ɣ ħ ʕ h/` + 2 nasals `/m n/` + 1 trill `/r/` + 1 lateral approximant `/l/` + 2 approximants/glides `/j w/` = 28. The marked Semitic series: **pharyngeals** ح `/ħ/` and ع `/ʕ/`; the four pharyngealized ("emphatic"/*mufakhkham*) consonants ط `/tˤ/`, ص `/sˤ/`, ض `/dˤ/`, ظ `/ðˤ/` (with uvular ق `/q/` often grouped as a back/emphatic consonant); the **interdentals** ث `/θ/`, ذ `/ð/`, ظ `/ðˤ/`. Arabic has **no** native `/v/`, `/p/`, or `/ɡ/`. Relation to the **source** 34-symbol Syriac inventory: Arabic natively hosts ~25 of the source consonants 1:1; the source has `/tˤ/` and `/sˤ/` but lacks Arabic's `/dˤ/` and `/ðˤ/`, while the source's `/v p ɡ/` are absent from Arabic (resolved in the Peshitta reader tier as v→ف, p→ب, ɡ→ج).

#### IPA Consonant Chart

IPA consonant chart for Arabic (rows = manner, columns = place). The four pharyngealized "emphatic" consonants `/tˤ sˤ dˤ ðˤ/` are shown in their primary place columns (alveolar / interdental) and flagged as emphatic by the superscript ˤ; voiceless precedes voiced within each cell.

| Manner | Bilabial | Labiodental | Interdental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|---|---|---|---|---|---|---|---|---|---|---|
| Plosive | b |  |  | t d tˤ dˤ |  |  | k | q |  | ʔ |
| Affricate |  |  |  |  | dʒ |  |  |  |  |  |
| Nasal | m |  |  | n |  |  |  |  |  |  |
| Trill |  |  |  | r |  |  |  |  |  |  |
| Fricative |  | f | θ ð ðˤ | s z sˤ | ʃ |  | x ɣ |  | ħ ʕ | h |
| Approximant |  |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |  |  |

*`/w/` و is a labial-velar approximant and is not assignable to a single column in this simplified chart (it patterns as both bilabial and velar). The four **emphatic** (pharyngealized) consonants are placed in their primary articulation columns — `/tˤ dˤ sˤ/` in the alveolar column, `/ðˤ/` in the interdental column — and are identified by the superscript ˤ; ق `/q/` patterns with the emphatics phonologically but is charted at its uvular place. ج `/dʒ/` is charted as a postalveolar affricate (MSA); its `[ɡ]` (Classical/Egyptian) and `[ʒ]` (Levantine) realizations are documented in the notes. All 28 phonemes are accounted for: b t d tˤ dˤ k q ʔ (8 plosives) + dʒ (1 affricate) + f θ ð ðˤ s z sˤ ʃ x ɣ ħ ʕ h (13 fricatives) + m n (2 nasals) + r (1 trill) + l (1 lateral) + j w (2 approximants) = 28.*

#### Notes by Place of Articulation

- **Bilabial:** `/b m/` (plus the bilabial component of the glide `/w/`). `/b/` ب is the only bilabial plosive; Arabic has no voiceless `/p/` (loanword `[p]` is written ب, e.g. باكِستان *bākistān*). `/m/` م is the bilabial nasal. The glide `/w/` و has a bilabial component but is listed under labial-velar. Examples: بَيْت *bayt* 'house' `/bajt/`, مَاء *māʾ* 'water' `/maːʔ/`.
- **Labiodental:** `/f/`. `/f/` ف is the sole labiodental. Arabic has no native voiced `/v/`; loanword `[v]` is rendered with ف (or the non-standard ڤ), e.g. فيروس *fayrūs* 'virus'. In the Peshitta reader tier the source `/v/` merges to ف. Example: فَجْر *fajr* 'dawn' `/fadʒr/`.
- **Interdental:** `/θ ð ðˤ/`. The interdental series: ث `/θ/` (voiceless, as in ثَلاثة *θalāθa* 'three'), ذ `/ð/` (voiced, as in ذَهَب *ðahab* 'gold'), and the pharyngealized ظ `/ðˤ/` (emphatic interdental, as in ظِلّ *ðˤill* 'shade'). These three are a hallmark Semitic feature preserved in MSA and Classical/Quranic Arabic and shared with the source; urban Levantine collapses ث/ذ→stops, which is why it is documented-only, not shipped.
- **Alveolar:** `/t d tˤ dˤ s z sˤ n r l/`. Plain coronals: ت `/t/`, د `/d/`, س `/s/`, ز `/z/`, ن `/n/`, ل `/l/`, ر `/r/`. The pharyngealized ("emphatic") coronals: ط `/tˤ/` (طَالِب *ṭālib* 'student'), ض `/dˤ/` (the *ḍād*, ضَوْء *ḍawʾ* 'light' — so iconic that Arabic is called لُغة الضَّاد *lughat al-ḍād*, 'the language of the *ḍād*'), and ص `/sˤ/` (صَبْر *ṣabr* 'patience'). Emphatics trigger backing of adjacent vowels (a→`[ɑ]`) and emphasis spread (*tafkhīm*). ر `/r/` is an alveolar trill (often a tap `[ɾ]`) and is itself emphatic `[rˤ]` adjacent to back vowels. ل `/l/` is clear `[l]` except the emphatic `[ɫ]` in اللّٰه *Allāh* `/ʔaɫːaːh/`. The source has `/tˤ/` and `/sˤ/` but lacks the Arabic-only `/dˤ/` and `/ðˤ/`.
- **Postalveolar:** `/dʒ ʃ/`. ج (*jīm*) and ش `/ʃ/` (شَمْس *šams* 'sun'). ج is the most variable Arabic consonant: voiced postalveolar affricate `[dʒ]` in MSA (and Levantine/Hejazi), voiced velar plosive `[ɡ]` in Egyptian and in many Classical/*tajwīd* descriptions, and voiced postalveolar fricative `[ʒ]` in much of Levantine/North African speech. The `[ɡ]` realization is why ج resolves the source `/ɡ/` in the Peshitta reader tier (ɡ→ج).
- **Palatal:** `/j/`. `/j/` ي (*yāʾ*) is the palatal glide (consonantal), as in يَد *yad* 'hand' `/jad/`. As a *mater lectionis* ي also writes long `/iː/`, and it forms the diphthong `/aj/` (e.g. بَيْت *bayt*).
- **Velar:** `/k x ɣ/`. ك `/k/` (كِتاب *kitāb* 'book'), and the velar/post-velar fricative pair خ `/x/` (voiceless, خُبْز *xubz* 'bread') and غ `/ɣ/` (voiced, غُرفة *ɣurfa* 'room'). Arabic has no native voiced velar plosive `/ɡ/`; the `[ɡ]` realization belongs to ج (and to dialectal ق). The pair `/x ɣ/` aligns directly with the source's soft Gamal/Kaph fricatives.
- **Uvular:** `/q/`. ق `/q/` (*qāf*) is the voiceless uvular plosive, as in قَلَم *qalam* 'pen' and القُرْآن *al-qurʾān*. It is a back/emphatic-patterning consonant that backs adjacent vowels. In MSA and Classical/Quranic Arabic it is firmly `[q]`; urban Levantine collapses it to `[ʔ]` (glottal stop) and Bedouin/Gulf to `[ɡ]` — both documented-only, since the `[q]`↔source-`/q/` (Qoph) match is a key reason Arabic is faithful to the source.
- **Pharyngeal:** `/ħ ʕ/`. The pharyngeals: ح `/ħ/` (voiceless, as in حُبّ *ḥubb* 'love') and ع `/ʕ/` (voiced, as in عَيْن *ʿayn* 'eye/spring'). Produced by constriction of the pharynx (epiglotto-pharyngeal). This pair maps 1:1 onto the source's Kheth `/ħ/` and Ayin `/ʕ/` and is a defining shared Semitic feature; ع in particular is famously difficult for non-Semitic speakers and central to the faithful rendering of the source.
- **Glottal:** `/ʔ h/`. `/ʔ/` ء (*hamza*, written with seat variants أ إ ؤ ئ or bare ء) is the glottal stop, fully phonemic in Arabic (سَأَل *saʾala* 'he asked'); contrast *hamzat al-qaṭʿ* (stable) with *hamzat al-waṣl* (elidable). `/h/` ه (*he*) is the voiceless glottal fricative (هُوَ *huwa* 'he'). Both map directly onto the source's Alaph `/ʔ/` and He `/h/`.
- **Labial-velar:** `/w/`. `/w/` و (*wāw*) is the voiced labial-velar (rounded) approximant, as in وَلَد *walad* 'boy' `/walad/`. As a *mater lectionis* و also writes long `/uː/`, and it forms the diphthong `/aw/` (e.g. يَوْم *yawm* 'day' `/jawm/`).

### Vowel Phonemes

The vowel system of Arabic: three vowel qualities `/a i u/`, each occurring **short** and **long**, plus two diphthongs `/aj/` (ay) and `/aw/` (aw). This compact triangular system is shared by Modern Standard and Classical/Quranic Arabic. The short vowels are written with the harakāt (vocalization diacritics) *fatḥa*, *kasra*, *ḍamma*; the long vowels are written with the *matres lectionis* ا و ي. Full per-sign detail and allophony are elaborated in the dedicated harakāt / vowel section; diphthongs have their own section.

**Short vowel count:** 3 | **Long vowel count:** 3 | **Diphthong count:** 2  
**Three** vowel qualities (`/a/`, `/i/`, `/u/`) × **two** lengths (short `/a i u/`, long `/aː iː uː/`) = 6 monophthong phonemes, plus 2 diphthongs `/aj aw/`. Length is contrastive and phonemic (e.g. كَتَبَ *kataba* 'he wrote' vs كاتَبَ *kātaba* 'he corresponded'; جَمَل *jamal* 'camel' vs جَميل *jamīl* 'beautiful'). Allophony: near the emphatics `/tˤ sˤ dˤ ðˤ/` and the back consonants `/q x ɣ/`, `/a aː/` back to `[ɑ ɑː]` (*tafkhīm*); in some Classical/dialectal contexts `/aː/` raises toward `[eː]`/`[iː]` (*imāla*). The Peshitta reader tier collapses source `/e/`→kasra/ī and `/o/`→ḍamma/ū to fit this three-quality system, matching attested Western Syriac vocalism, while preserving vowel length via the matres.

#### IPA Vowel Chart

IPA vowel quadrilateral for Arabic (three qualities; each occurs short and long). Backed allophones `[ɑ ɑː]` appear adjacent to emphatic/back consonants.

| Height | Front (unrounded) | Central | Back (rounded) |
|---|---|---|---|
| close | i  iː |  | u  uː |
| open |  | a  aː | (ɑ  ɑː) allophonic |

*Arabic is a classic triangular three-vowel system: high front `/i iː/`, high back rounded `/u uː/`, and low central `/a aː/`. The back open allophones `[ɑ ɑː]` are **not** separate phonemes — they arise from emphasis/backing (*tafkhīm*) near `/tˤ sˤ dˤ ðˤ q x ɣ/` and in اللّٰه. Compare the source: Eastern Syriac maintains 7 vowel qualities and Hebrew 7, where Arabic has the most economical 3 — hence the reader-tier collapses e→i and o→u.*

#### Short Vowels (Harakāt)

The harakāt (الحَرَكات, vocalization diacritics) for the short vowels. Normally unwritten in everyday text; supplied in full (تَشكيل *tashkīl*) for scripture, pedagogy and the **vocalized** Peshitta reader tier.

| IPA | Sign | Unicode | Description |
|---|---|---|---|
| `/a/` | فَتْحة *fatḥa* (ـَ) | `U+064E` | Short open vowel; small diagonal stroke above the consonant. Backs to `[ɑ]` near emphatics/back consonants. Example: مَنْ *man* 'who'. |
| `/i/` | كَسْرة *kasra* (ـِ) | `U+0650` | Short close front vowel; small diagonal stroke below the consonant. Example: مِنْ *min* 'from'. |
| `/u/` | ضَمّة *ḍamma* (ـُ) | `U+064F` | Short close back rounded vowel; small *wāw*-shaped mark above the consonant. Example: كُلّ *kull* 'all/every'. |

#### Long Vowels (Matres Lectionis)

The long vowels are written as a haraka followed by a *mater lectionis* (ا و ي).

| IPA | Sign | Mater | Description |
|---|---|---|---|
| `/aː/` | *fatḥa* + *alif* (ـَا) | ا *alif* (`U+0627`) | Long open vowel; *fatḥa* followed by the mater *alif*. Backs to `[ɑː]` near emphatics. Example: باب *bāb* 'door' `/baːb/`. |
| `/iː/` | *kasra* + *yāʾ* (ـِي) | ي *yāʾ* (`U+064A`) | Long close front vowel; *kasra* followed by the mater *yāʾ*. Example: فيل *fīl* 'elephant' `/fiːl/`. |
| `/uː/` | *ḍamma* + *wāw* (ـُو) | و *wāw* (`U+0648`) | Long close back rounded vowel; *ḍamma* followed by the mater *wāw*. Example: نور *nūr* 'light' `/nuːr/`. |

#### Diphthongs

The two closing diphthongs; elaborated in the dedicated diphthongs section.

| IPA | Spelling | Description |
|---|---|---|
| `/aj/` | *fatḥa* + sukūn-bearing *yāʾ* (ـَيْ) | Closing diphthong 'ay'; *fatḥa* followed by a non-syllabic *yāʾ*. Example: بَيْت *bayt* 'house' `/bajt/`, خَيْر *xayr* 'good'. |
| `/aw/` | *fatḥa* + sukūn-bearing *wāw* (ـَوْ) | Closing diphthong 'aw'; *fatḥa* followed by a non-syllabic *wāw*. Example: يَوْم *yawm* 'day' `/jawm/`, لَوْن *lawn* 'colour'. |

#### Auxiliary Marks

Non-vowel diacritics that complete the *tashkīl* system.

| Sign | Unicode | Description |
|---|---|---|
| سُكون *sukūn* (ـْ) | `U+0652` | Absence of a vowel; marks a consonant closing a syllable (no following vowel). |
| شَدّة *shadda* (ـّ) | `U+0651` | Gemination/doubling of the consonant; phonemic and contrastive (e.g. دَرَسَ *darasa* 'he studied' vs دَرَّسَ *darrasa* 'he taught'). |
| تَنْوين *tanwīn* / nunation (ـً ـٍ ـٌ) | `U+064B` *fatḥatān*, `U+064D` *kasratān*, `U+064C` *ḍammatān* | Final indefinite nunation: `/an/` (ـً), `/in/` (ـٍ), `/un/` (ـٌ). Case-marking desinential vowels; dropped in pausal (*waqf*) forms and not emitted in the caseless source-aligned IPA. |

---

*Signed: Shin*

## Consonants (الحروف الساكنة)

The 28 consonant phonemes of Arabic (العربية), documented in parallel for two reference standards: Modern Standard Arabic (MSA, الفصحى *al-fuṣḥā*) and Classical/Quranic Arabic (the *tajwīd* careful-recitation register). Unlike the vowels, the Arabic consonant inventory is essentially identical across both standards, so each phoneme carries one set of IPA, place, manner and voicing values; register-specific and dialectal surface realisations are recorded in the allophony notes. Phonemic values are given in /slashes/ and phonetic realisations in [brackets], following the IPA (2015 revision). Arabic is the FIRST target language in the same family as the source: as a Central Semitic SISTER of Syriac/Aramaic and Hebrew, it natively hosts the pharyngeals (`ħ` ح, `ʕ` ع), the emphatic/pharyngealised series (`tˤ` ط, `sˤ` ص, `dˤ` ض, `ðˤ` ظ), the interdentals (`θ` ث, `ð` ذ, `ðˤ` ظ), and the uvular `q` ق — the very contrasts that make it the most faithful match for the source 34-symbol Syriac inventory. The abjad order here follows the modern *hijāʾī* sequence ا ب ت ث …; the **abjad value** field records the traditional أبجد numeral. Note the gaps: Arabic has NO native `/v/`, `/p/` or `/ɡ/` — in the Peshitta reader tier the source maps v→ف, p→ب (merges) and ɡ→ج (realization).

**Consonant phonemes:** 28 | **Effective phonemes:** 28  
28 abjad consonant letters map essentially 1:1 to 28 phonemes; Arabic has no *begadkephat*-style hard/soft alternation, so the letter-to-phoneme ratio is clean. The Syriac source is counted differently elsewhere in this guide: its ABJAD has 22 base letters, but the full phonemic inventory the project documents is the 34-symbol figure (the 22 letters plus the *begadkephat* spirantized allophone pairs and the *matres*/vowel signs), which is why the overlap is framed as "~25 of 34" rather than against 22. The only major surface alternation in Arabic is positional/dialectal allophony, not phonemic spirantisation. `ج` (*jīm*) is a single phoneme whose canonical realisation [dʒ] varies regionally to [ɡ] (Egyptian/older Classical) or [ʒ] (Levantine). Gemination via *shadda* (ـّ) is contrastive but doubles existing phonemes rather than adding new ones. Hamza `ء` (`/ʔ/`) and the hamza seat-letters (أ إ ؤ ئ) all encode the same glottal-stop phoneme.

### Reference Standards

The two shipped standards documented in parallel, plus the dialectal aside that is described but NOT shipped.

| Standard | Description |
|---|---|
| **MSA** | Modern Standard Arabic (الفصحى *al-fuṣḥā*) — the contemporary pan-Arab literary/formal standard; preserves all 28 consonant contrasts. |
| **Classical** | Classical / Quranic Arabic (لغة القرآن) — the older codified form read in the *tajwīd* careful-recitation register; preserves every MSA contrast plus finer *tajwīd* detail (*idghām*, *qalqala*, *tafkhīm*/*tarqīq*, etc.). Genre-appropriate for scripture. |
| *Dialectal aside* | Urban Levantine and Egyptian realisations are documented descriptively in the allophony notes only; they collapse key contrasts (qāf→[ʔ]; interdentals ث/ذ/ظ→stops or sibilants) and are **NOT** shipped standards. |

### Consonant Inventory

The 28 consonant phonemes with their IPA value, Arabic letter (vocalized and isolated), letter name (Arabic and transliterated), abjad numeral value, Unicode codepoint, place, manner, voicing, source-symbol match, example words (with IPA), and allophony notes.

| # | IPA | Letter | Isolated | Name (Arabic) | Name (translit.) | Abjad | Unicode | Place | Manner | Voicing |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `/ʔ/` | ء (أَ، إِ، ؤ، ئ) | `ء` | همزة | *hamza* | 1 | `U+0621` | glottal | plosive | voiceless |
| 2 | `/b/` | بَ | `ب` | باء | *bāʾ* | 2 | `U+0628` | bilabial | plosive | voiced |
| 3 | `/t/` | تَ | `ت` | تاء | *tāʾ* | 400 | `U+062A` | alveolar | plosive | voiceless |
| 4 | `/θ/` | ثَ | `ث` | ثاء | *thāʾ* | 500 | `U+062B` | interdental (dental) | fricative | voiceless |
| 5 | `/dʒ/` | جَ | `ج` | جيم | *jīm* | 3 | `U+062C` | postalveolar (palato-alveolar) | affricate | voiced |
| 6 | `/ħ/` | حَ | `ح` | حاء | *ḥāʾ* | 8 | `U+062D` | pharyngeal | fricative | voiceless |
| 7 | `/x/` | خَ | `خ` | خاء | *khāʾ* | 600 | `U+062E` | velar / uvular | fricative | voiceless |
| 8 | `/d/` | دَ | `د` | دال | *dāl* | 4 | `U+062F` | alveolar (dental) | plosive | voiced |
| 9 | `/ð/` | ذَ | `ذ` | ذال | *dhāl* | 700 | `U+0630` | interdental (dental) | fricative | voiced |
| 10 | `/r/` | رَ | `ر` | راء | *rāʾ* | 200 | `U+0631` | alveolar | trill | voiced |
| 11 | `/z/` | زَ | `ز` | زاي | *zāy (zayn)* | 7 | `U+0632` | alveolar | fricative | voiced |
| 12 | `/s/` | سَ | `س` | سين | *sīn* | 60 | `U+0633` | alveolar | fricative | voiceless |
| 13 | `/ʃ/` | شَ | `ش` | شين | *shīn* | 300 | `U+0634` | postalveolar (palato-alveolar) | fricative | voiceless |
| 14 | `/sˤ/` | صَ | `ص` | صاد | *ṣād* | 90 | `U+0635` | alveolar | fricative | voiceless |
| 15 | `/dˤ/` | ضَ | `ض` | ضاد | *ḍād* | 800 | `U+0636` | alveolar | plosive | voiced |
| 16 | `/tˤ/` | طَ | `ط` | طاء | *ṭāʾ* | 9 | `U+0637` | alveolar | plosive | voiceless |
| 17 | `/ðˤ/` | ظَ | `ظ` | ظاء | *ẓāʾ* | 900 | `U+0638` | interdental (dental) | fricative | voiced |
| 18 | `/ʕ/` | عَ | `ع` | عين | *ʿayn* | 70 | `U+0639` | pharyngeal | fricative (approximant) | voiced |
| 19 | `/ɣ/` | غَ | `غ` | غين | *ghayn* | 1000 | `U+063A` | velar / uvular | fricative | voiced |
| 20 | `/f/` | فَ | `ف` | فاء | *fāʾ* | 80 | `U+0641` | labiodental | fricative | voiceless |
| 21 | `/q/` | قَ | `ق` | قاف | *qāf* | 100 | `U+0642` | uvular | plosive | voiceless |
| 22 | `/k/` | كَ | `ك` | كاف | *kāf* | 20 | `U+0643` | velar | plosive | voiceless |
| 23 | `/l/` | لَ | `ل` | لام | *lām* | 30 | `U+0644` | alveolar | lateral approximant | voiced |
| 24 | `/m/` | مَ | `م` | ميم | *mīm* | 40 | `U+0645` | bilabial | nasal | voiced |
| 25 | `/n/` | نَ | `ن` | نون | *nūn* | 50 | `U+0646` | alveolar | nasal | voiced |
| 26 | `/h/` | هَ | `ه` | هاء | *hāʾ* | 5 | `U+0647` | glottal | fricative | voiceless |
| 27 | `/w/` | وَ | `و` | واو | *wāw* | 6 | `U+0648` | labial-velar | approximant | voiced |
| 28 | `/j/` | يَ | `ي` | ياء | *yāʾ* | 10 | `U+064A` | palatal | approximant | voiced |

#### Feature Flags and Source Match

Per-phoneme phonological feature flags (emphatic, pharyngeal, interdental, guttural, sun letter, obstruent, sonorant) plus the matching symbol in the Syriac/Hebrew source inventory.

| # | IPA | Letter | Emphatic | Pharyngeal | Interdental | Guttural | Sun letter | Obstruent | Sonorant | Source-symbol match |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `/ʔ/` | `ء` | no | no | no | yes | no | yes | no | `ʔ` (Syriac ʾAlaph ܐ / Hebrew ʾAlef א) |
| 2 | `/b/` | `ب` | no | no | no | no | no | yes | no | `b` (Syriac Beth ܒ / Hebrew Bet ב); also the Peshitta reader target for source `/p/` (p→ب merge) |
| 3 | `/t/` | `ت` | no | no | no | no | yes | yes | no | `t` (Syriac Taw ܬ / Hebrew Tav ת) |
| 4 | `/θ/` | `ث` | no | no | yes | no | yes | yes | no | `θ` (Syriac soft Taw [θ] / Hebrew soft Tav [θ]); a 1:1 interdental match with the source |
| 5 | `/dʒ/` | `ج` | no | no | no | no | no | yes | no | `ɡ` (Syriac Gamal ܓ / Hebrew Gimel ג): the Peshitta reader maps source `/ɡ/` → ج, since ج realises as [ɡ] in Egyptian/older Classical Arabic |
| 6 | `/ħ/` | `ح` | no | yes | no | yes | no | yes | no | `ħ` (Syriac Kheth ܚ / Hebrew Chet ח): a 1:1 pharyngeal match — a hallmark Semitic contrast |
| 7 | `/x/` | `خ` | no | no | no | yes | no | yes | no | `x` (Syriac soft Kaph [x] / Hebrew soft Kaf [x]): a 1:1 match |
| 8 | `/d/` | `د` | no | no | no | no | yes | yes | no | `d` (Syriac Dalath ܕ / Hebrew Dalet ד) |
| 9 | `/ð/` | `ذ` | no | no | yes | no | yes | yes | no | `ð` (Syriac soft Dalath [ð] / Hebrew soft Dalet [ð]): a 1:1 interdental match |
| 10 | `/r/` | `ر` | no | no | no | no | yes | no | yes | `r` (Syriac Resh ܪ / Hebrew Resh ר); note the source/Tiberian Hebrew resh is often uvular [ʁ], whereas Arabic *rāʾ* is a coronal trill |
| 11 | `/z/` | `ز` | no | no | no | no | yes | yes | no | `z` (Syriac Zayn ܙ / Hebrew Zayin ז) |
| 12 | `/s/` | `س` | no | no | no | no | yes | yes | no | `s` (Syriac Semkath ܣ / Hebrew Samekh ס, and Hebrew Sin שׂ [s]) |
| 13 | `/ʃ/` | `ش` | no | no | no | no | yes | yes | no | `ʃ` (Syriac Shin ܫ / Hebrew Shin שׁ [ʃ]) |
| 14 | `/sˤ/` | `ص` | **yes** | no | no | no | yes | yes | no | `sˤ` (Syriac Tsade ܨ / Hebrew Tsadi צ): the source HAS this emphatic, a 1:1 match |
| 15 | `/dˤ/` | `ض` | **yes** | no | no | no | yes | yes | no | **NONE** — the source 34-symbol inventory has `tˤ` and `sˤ` but NO voiced emphatic `dˤ`; this is an Arabic-only phoneme |
| 16 | `/tˤ/` | `ط` | **yes** | no | no | no | yes | yes | no | `tˤ` (Syriac Teth ܛ / Hebrew Tet ט): the source HAS this emphatic, a 1:1 match |
| 17 | `/ðˤ/` | `ظ` | **yes** | no | yes | no | yes | yes | no | **NONE** — the source lacks the voiced emphatic interdental; an Arabic-only phoneme (it is, however, the emphatic partner of source-shared ð/θ) |
| 18 | `/ʕ/` | `ع` | no | yes | no | yes | no | yes | no | `ʕ` (Syriac Ayin ܥ / Hebrew Ayin ע): a 1:1 pharyngeal match — a hallmark Semitic contrast |
| 19 | `/ɣ/` | `غ` | no | no | no | yes | no | yes | no | `ɣ` (Syriac soft Gamal [ɣ] / Hebrew soft Gimel [ɣ]): a 1:1 match |
| 20 | `/f/` | `ف` | no | no | no | no | no | yes | no | `f` (Syriac soft Pe [f] / Hebrew soft Pe [f]); also the Peshitta reader target for source `/v/` (v→ف merge) |
| 21 | `/q/` | `ق` | no¹ | no | no | no | no | yes | no | `q` (Syriac Qaph ܩ / Hebrew Qof ק): a 1:1 uvular match |
| 22 | `/k/` | `ك` | no | no | no | no | no | yes | no | `k` (Syriac Kaph ܟ / Hebrew Kaf כ) |
| 23 | `/l/` | `ل` | no | no | no | no | yes | no | yes | `l` (Syriac Lamadh ܠ / Hebrew Lamed ל) |
| 24 | `/m/` | `م` | no | no | no | no | no | no | yes | `m` (Syriac Mim ܡ / Hebrew Mem מ) |
| 25 | `/n/` | `ن` | no | no | no | no | yes | no | yes | `n` (Syriac Nun ܢ / Hebrew Nun נ) |
| 26 | `/h/` | `ه` | no | no | no | yes | no | yes | no | `h` (Syriac He ܗ / Hebrew He ה) |
| 27 | `/w/` | `و` | no | no | no | no | no | no | yes | `w` (Syriac Waw ܘ / Hebrew Vav ו) |
| 28 | `/j/` | `ي` | no | no | no | no | no | no | yes | `j` (Syriac Yudh ܝ / Hebrew Yod י) |

¹ `/q/` is **not** pharyngealised, but it is conventionally grouped *with* the emphatics for emphasis-spread purposes (`emphasis_grouped_with_emphatics: true`); see the natural-classes notes below. Letters `د` *dāl*, `ذ` *dhāl*, `ر` *rāʾ*, `ز` *zāy*, `و` *wāw* are **non-connecting** (they join only on their right). `و` *wāw* and `ي` *yāʾ* are also **glides** that double as ***matres lectionis*** (vowel-letters).

#### Example Words

Three vocalized example words per phoneme (Arabic shown with harakat), with romanization, phonemic IPA, and gloss.

| # | IPA | Examples (vocalized Arabic — romanization — IPA — gloss) |
|---|---|---|
| 1 | `/ʔ/` | أَكَلَ — *ʔakala* — `/ʔa.ka.la/` — "he ate"; سَأَلَ — *saʔala* — `/sa.ʔa.la/` — "he asked"; جَاءَ — *jāʔa* — `/dʒaː.ʔa/` — "he came" |
| 2 | `/b/` | بَابٌ — *bāb* — `/baːb/` — "door"; كِتَابٌ — *kitāb* — `/ki.taːb/` — "book"; حُبٌّ — *ḥubb* — `/ħubb/` — "love" |
| 3 | `/t/` | تَمْرٌ — *tamr* — `/tamr/` — "dates (fruit)"; بِنْتٌ — *bint* — `/bint/` — "girl, daughter"; كَتَبَ — *kataba* — `/ka.ta.ba/` — "he wrote" |
| 4 | `/θ/` | ثَلَاثَةٌ — *thalātha* — `/θa.laː.θa/` — "three"; ثَوْرٌ — *thawr* — `/θawr/` — "bull, ox"; حَدِيثٌ — *ḥadīth* — `/ħa.diːθ/` — "speech; hadith" |
| 5 | `/dʒ/` | جَمَلٌ — *jamal* — `/dʒa.mal/` — "camel"; رَجُلٌ — *rajul* — `/ra.dʒul/` — "man"; مَسْجِدٌ — *masjid* — `/mas.dʒid/` — "mosque" |
| 6 | `/ħ/` | حُبٌّ — *ḥubb* — `/ħubb/` — "love"; مِفْتَاحٌ — *miftāḥ* — `/mif.taːħ/` — "key"; صَحْرَاءُ — *ṣaḥrāʾ* — `/sˤaħ.raːʔ/` — "desert" |
| 7 | `/x/` | خُبْزٌ — *khubz* — `/xubz/` — "bread"; أَخٌ — *ʾakh* — `/ʔax/` — "brother"; تَارِيخٌ — *tārīkh* — `/taː.riːx/` — "history; date" |
| 8 | `/d/` | دَارٌ — *dār* — `/daːr/` — "house, abode"; وَلَدٌ — *walad* — `/wa.lad/` — "boy, child"; يَدٌ — *yad* — `/jad/` — "hand" |
| 9 | `/ð/` | هَذَا — *hādhā* — `/haː.ðaː/` — "this (masc.)"; ذَهَبٌ — *dhahab* — `/ða.hab/` — "gold"; أُسْتَاذٌ — *ʾustādh* — `/ʔus.taːð/` — "teacher, professor" |
| 10 | `/r/` | رَأْسٌ — *raʾs* — `/raʔs/` — "head"; نَهْرٌ — *nahr* — `/nahr/` — "river"; بَحْرٌ — *baḥr* — `/baħr/` — "sea" |
| 11 | `/z/` | زَيْتٌ — *zayt* — `/zajt/` — "oil"; مَوْزٌ — *mawz* — `/mawz/` — "bananas"; زَوْجٌ — *zawj* — `/zawdʒ/` — "husband, pair" |
| 12 | `/s/` | سَلَامٌ — *salām* — `/sa.laːm/` — "peace"; شَمْسٌ — *shams* — `/ʃams/` — "sun"; دَرْسٌ — *dars* — `/dars/` — "lesson" |
| 13 | `/ʃ/` | شَمْسٌ — *shams* — `/ʃams/` — "sun"; شَجَرَةٌ — *shajara* — `/ʃa.dʒa.ra/` — "tree"; عَيْشٌ — *ʿaysh* — `/ʕajʃ/` — "living; bread (dial.)" |
| 14 | `/sˤ/` | صَيْفٌ — *ṣayf* — `/sˤajf/` — "summer"; صَلَاةٌ — *ṣalāh* — `/sˤa.laː/` — "prayer"; خَاصٌّ — *khāṣṣ* — `/xaːsˤsˤ/` — "special, private" |
| 15 | `/dˤ/` | ضَوْءٌ — *ḍawʾ* — `/dˤawʔ/` — "light"; أَرْضٌ — *ʾarḍ* — `/ʔardˤ/` — "earth, land"; رَمَضَانُ — *ramaḍān* — `/ra.ma.dˤaːn/` — "Ramadan" |
| 16 | `/tˤ/` | طَيْرٌ — *ṭayr* — `/tˤajr/` — "bird(s)"; طَرِيقٌ — *ṭarīq* — `/tˤa.riːq/` — "road, way"; بَطْنٌ — *baṭn* — `/batˤn/` — "belly, abdomen" |
| 17 | `/ðˤ/` | ظِلٌّ — *ẓill* — `/ðˤill/` — "shade, shadow"; عَظِيمٌ — *ʿaẓīm* — `/ʕa.ðˤiːm/` — "great, mighty"; حِفْظٌ — *ḥifẓ* — `/ħifðˤ/` — "preservation; memorisation" |
| 18 | `/ʕ/` | عَيْنٌ — *ʿayn* — `/ʕajn/` — "eye; spring"; عَرَبِيٌّ — *ʿarabiyy* — `/ʕa.ra.bijj/` — "Arabic, Arab"; سَمِعَ — *samiʿa* — `/sa.mi.ʕa/` — "he heard" |
| 19 | `/ɣ/` | غَيْمٌ — *ghaym* — `/ɣajm/` — "cloud"; لُغَةٌ — *lugha* — `/lu.ɣa/` — "language"; بَلَّغَ — *ballagha* — `/bal.la.ɣa/` — "he conveyed/announced" |
| 20 | `/f/` | فَمٌ — *fam* — `/fam/` — "mouth"; سَفَرٌ — *safar* — `/sa.far/` — "travel, journey"; خَوْفٌ — *khawf* — `/xawf/` — "fear" |
| 21 | `/q/` | قَلْبٌ — *qalb* — `/qalb/` — "heart"; قُرْآنٌ — *qurʾān* — `/qur.ʔaːn/` — "Quran"; صَدِيقٌ — *ṣadīq* — `/sˤa.diːq/` — "friend" |
| 22 | `/k/` | كَلْبٌ — *kalb* — `/kalb/` — "dog"; كِتَابٌ — *kitāb* — `/ki.taːb/` — "book"; مَلِكٌ — *malik* — `/ma.lik/` — "king" |
| 23 | `/l/` | لَيْلٌ — *layl* — `/lajl/` — "night"; قَلَمٌ — *qalam* — `/qa.lam/` — "pen"; اَللّٰهُ — *Allāh* — `/ʔalˤ.lˤaːh/` — "God, Allah" |
| 24 | `/m/` | مَاءٌ — *māʾ* — `/maːʔ/` — "water"; قَمَرٌ — *qamar* — `/qa.mar/` — "moon"; اِسْمٌ — *ism* — `/ʔism/` — "name" |
| 25 | `/n/` | نُورٌ — *nūr* — `/nuːr/` — "light"; بِنْتٌ — *bint* — `/bint/` — "girl, daughter"; عَيْنٌ — *ʿayn* — `/ʕajn/` — "eye; spring" |
| 26 | `/h/` | هَوَاءٌ — *hawāʾ* — `/ha.waːʔ/` — "air"; نَهْرٌ — *nahr* — `/nahr/` — "river"; وَجْهٌ — *wajh* — `/wadʒh/` — "face" |
| 27 | `/w/` | وَلَدٌ — *walad* — `/wa.lad/` — "boy, child"; يَوْمٌ — *yawm* — `/jawm/` — "day"; نُورٌ — *nūr* — `/nuːr/` — "light" |
| 28 | `/j/` | يَدٌ — *yad* — `/jad/` — "hand"; بَيْتٌ — *bayt* — `/bajt/` — "house"; كَبِيرٌ — *kabīr* — `/ka.biːr/` — "big, great" |

#### Allophony Notes (per phoneme)

- **1 `/ʔ/` `ء` همزة *hamza* — U+0621** (seat variants: `U+0623` أ, `U+0625` إ, `U+0624` ؤ, `U+0626` ئ; abjad note: the numeral 1, أ *alif*, is the abjad value of the *alif* seat — hamza ء itself is a diacritic-like sign that rides on *alif*/*wāw*/*yāʾ* seats). Phonemic glottal stop. Written with hamza ء on a seat (أ إ ؤ ئ) or stand-alone; the seat is chosen by surrounding vowels, not by phonemic value. Distinguish phonemic *hamzat al-qaṭʿ* (always pronounced) from *hamzat al-waṣl* (the elidable connecting hamza of ال and of certain verb/noun stems, written ٱ `U+0671`), which is realised only utterance-initially and drops in connected speech (e.g. بِسْمِ ٱللّٰه → *bismi-llāh*). Urban Levantine and Egyptian merge etymological `/q/` into [ʔ], greatly raising hamza's functional load there (documented aside only).
- **2 `/b/` `ب` باء *bāʾ* — U+0628.** Fully voiced [b] in all positions. Devoices partially to [b̥] in coda before a voiceless obstruent (e.g. اِبْتَدَأَ *ibtadaʾa*, where b precedes t). Arabic lacks a `/p/`, so loanword [p] is normally nativised to [b] (and ب also carries source `/p/` in the Peshitta reader tier); modern writing may use a three-dot پ (`U+067E`) for foreign [p], but that letter is not part of the 28-consonant Arabic inventory.
- **3 `/t/` `ت` تاء *tāʾ* — U+062A.** Plain (non-emphatic) voiceless alveolar stop, unaspirated or only lightly aspirated — contrasts sharply with emphatic ط `/tˤ/`, which backs adjacent vowels (تِين *tīn* "fig" [tiːn] vs طِين *ṭīn* "clay/mud" [tˤɑ…] with backed vowel). A sun letter: the article *lām* assimilates before it (الـتَّمْر → *at-tamr*). Note the related grapheme *tāʾ marbūṭa* ة (`U+0629`), a feminine-ending letter read as [t] in construct/with case but as [h] or zero in pausal forms — it is an orthographic variant of ت/ه, not a separate phoneme. In *tajwīd*, coda `/t/` before certain consonants may undergo *idghām*.
- **4 `/θ/` `ث` ثاء *thāʾ* — U+062B.** Voiceless interdental fricative, like English "think." A sun letter (الـثَّوْب → *ath-thawb*). Carefully preserved in MSA and Classical/Quranic recitation, where merging it would destroy a contrast Arabic shares with the source. Many urban dialects (Levantine, Egyptian) shift ث → [t] (or [s] in learned/loan vocabulary), but that merger is explicitly NOT part of the shipped standards.
- **5 `/dʒ/` `ج` جيم *jīm* — U+062C.** The single most variable Arabic consonant. Canonical MSA value is the voiced postalveolar affricate [dʒ]. Major regional realisations: [ɡ] (voiced velar plosive) in Egyptian Arabic and reconstructed for older Classical/Quranic recitation (the historically original value, < Proto-Semitic \*g); [ʒ] (voiced postalveolar fricative) in Levantine and much of the Maghreb; [ʝ]/[j]-like in parts of the Gulf. Because Arabic has no separate `/ɡ/` phoneme, ج is precisely the grapheme used to render the source `/ɡ/` in the Peshitta reader tier. A moon letter (الـجَمَل → *al-jamal*).
- **6 `/ħ/` `ح` حاء *ḥāʾ* — U+062D.** Voiceless pharyngeal fricative — a strong constriction of the pharynx, sharply distinct from glottal `/h/` and from velar/uvular `/x/`. One of the true pharyngeals (with ع `/ʕ/`) that make Arabic a faithful match for the source's ħ. Stable across MSA, Classical/Quranic and virtually all dialects (rarely lost). In *tajwīd* it is one of the *ḥurūf al-ḥalq* (throat letters) and blocks *idghām*/*iqlāb* assimilations involving the *nūn sākina*.
- **7 `/x/` `خ` خاء *khāʾ* — U+062E.** Voiceless dorsal fricative, articulated at the velar–uvular region (often transcribed [x] but frequently nearer uvular [χ]). Pairs with voiced غ `/ɣ/`. A guttural/throat-region letter; stable across MSA, Classical/Quranic and the dialects. Distinct from pharyngeal ح `/ħ/` (which is further back, in the pharynx with no dorsal raising).
- **8 `/d/` `د` دال *dāl* — U+062F (non-connecting).** Plain voiced (dental-to-alveolar) stop, the non-emphatic counterpart of ض `/dˤ/`. A non-connecting letter (joins only on its right). A sun letter (الـدَّار → *ad-dār*). Fully voiced intervocalically; may devoice slightly word-finally in pausal position. Contrast with emphatic ض is carried by vowel backing/colour, not by place alone.
- **9 `/ð/` `ذ` ذال *dhāl* — U+0630 (non-connecting).** Voiced interdental fricative, like English "this." A non-connecting sun letter (الـذَّهَب → *adh-dhahab*). Carefully preserved in MSA and Classical/Quranic recitation. Urban Levantine and Egyptian commonly merge ذ → [d] (or [z] in learned/loan items), but this merger is excluded from the shipped standards because it would collapse a contrast Arabic shares directly with the source.
- **10 `/r/` `ر` راء *rāʾ* — U+0631 (non-connecting).** Voiced alveolar trill [r], reducing to a tap [ɾ] intervocalically and in fast speech. A non-connecting sun letter (الـرَّأْس → *ar-raʾs*). Subject to *tafkhīm*/*tarqīq* (heavy vs light) in *tajwīd*: *rāʾ* velarises to an emphatic, backed [rˤ] adjacent to back/low vowels and emphatic consonants (e.g. with *fatḥa*/*ḍamma* or near ص ط ق), and stays light/plain [r] adjacent to *kasra* `/i/` — exactly the kind of emphatic-trill allophony also seen in Tiberian Hebrew resh.
- **11 `/z/` `ز` زاي *zāy (zayn)* — U+0632 (non-connecting).** Voiced alveolar sibilant fricative, the voiced counterpart of س `/s/`. A non-connecting sun letter (الـزَّيْت → *az-zayt*). Stable across registers. Distinct from the emphatic/interdental ظ `/ðˤ/`, which some dialects merge toward [zˤ].
- **12 `/s/` `س` سين *sīn* — U+0633.** Plain voiceless alveolar sibilant, the non-emphatic counterpart of ص `/sˤ/` — the س/ص contrast (and the emphasis spread it triggers) is one of Arabic's signature minimal pairs (سَيْف *sayf* "sword" vs صَيْف *ṣayf* "summer"). A sun letter (الـسَّلَام → *as-salām*). Stable across MSA, Classical/Quranic and the dialects.
- **13 `/ʃ/` `ش` شين *shīn* — U+0634.** Voiceless postalveolar sibilant, like English "sh." A sun letter (and the textbook example of sun-letter assimilation: الشمس → *aš-šams*, *lām* fully assimilated into a geminate `/ʃ/`). Stable across registers. Some Yemeni/older descriptions note a less palatalised value, but MSA/Classical [ʃ] is uniform.
- **14 `/sˤ/` `ص` صاد *ṣād* — U+0635 (emphatic).** Emphatic (pharyngealised/velarised) voiceless alveolar sibilant — the emphatic counterpart of س `/s/`. Triggers *tafkhīm*: adjacent `/a/` backs to [ɑ] and neighbouring consonants take on a "dark" colouring (emphasis spread, which can propagate across the whole syllable or word). A sun letter (الـصَّيْف → *aṣ-ṣayf*). Contrasts minimally with س (سَيْف vs صَيْف). Matches the source's emphatic sˤ directly.
- **15 `/dˤ/` `ض` ضاد *ḍād* — U+0636 (emphatic; Arabic-only).** Emphatic (pharyngealised) voiced alveolar stop — Arabic's most famous sound, so iconic that Arabic is called لغة الضاد *lughat al-ḍād*, "the language of the *ḍād*." In Classical/old Arabic it was a pharyngealised lateral or lateralised fricative (a unique sound now lost); the modern MSA value is a plain emphatic stop [dˤ]. The source language has no equivalent (it lacks both dˤ and ðˤ), so ض represents an Arabic surplus over the source inventory. A sun letter; triggers strong emphasis spread. Many dialects merge ض and ظ toward a single emphatic value.
- **16 `/tˤ/` `ط` طاء *ṭāʾ* — U+0637 (emphatic).** Emphatic (pharyngealised) voiceless alveolar stop — the emphatic counterpart of ت `/t/`. Strong *tafkhīm*: backs adjacent `/a/` to [ɑ] and darkens the syllable. A sun letter (الـطَّرِيق → *aṭ-ṭarīq*). Classically described as voiceless, though in some reconstructions the old *ṭāʾ* was the voiced member of an emphatic pair; modern MSA is firmly voiceless [tˤ]. In *tajwīd*, ط exhibits *qalqala* (a slight echo/bounce) when *sākin*. Matches the source emphatic tˤ directly.
- **17 `/ðˤ/` `ظ` ظاء *ẓāʾ* — U+0638 (emphatic, interdental; Arabic-only).** Emphatic (pharyngealised) voiced interdental fricative — the emphatic counterpart of ذ `/ð/`, classed both as an interdental and as an emphatic. The source inventory has no voiced emphatic, so ظ is Arabic-specific. A sun letter; triggers emphasis spread. The most dialect-variable emphatic: urban Levantine/Egyptian commonly realise it as emphatic [zˤ] (merging with ض in many dialects), and it is frequently confused with ض in spelling — but MSA and Classical/Quranic recitation keep [ðˤ] distinct.
- **18 `/ʕ/` `ع` عين *ʿayn* — U+0639 (pharyngeal).** Voiced pharyngeal — a constriction of the pharynx, often more an approximant [ʕ̞] than a true fricative, and sometimes with creaky/epiglottal colouring. The voiced partner of ح `/ħ/`. One of the defining Semitic sounds, preserved across MSA, Classical/Quranic recitation and virtually all dialects; its faithful retention is a key reason Arabic matches the source so well. A moon letter and a *ḥurūf al-ḥalq* (throat letter) in *tajwīd*. Notoriously hard for non-Semitic speakers, who tend to substitute [ʔ] or zero.
- **19 `/ɣ/` `غ` غين *ghayn* — U+063A.** Voiced dorsal fricative at the velar–uvular region (often nearer uvular [ʁ]), the voiced counterpart of خ `/x/`. A guttural/throat-region letter; stable across MSA, Classical/Quranic and the dialects. Used to render foreign [ɡ] in some loanwords/transcriptions, though ج and (non-standard) گ are also used. A moon letter (الـغَيْم → *al-ghaym*).
- **20 `/f/` `ف` فاء *fāʾ* — U+0641.** Voiceless labiodental fricative. Arabic has no voiced `/v/`, so loan [v] is nativised to [f] (and ف also carries the source `/v/` in the Peshitta reader tier); a three-dot ڤ (`U+06A4`) is sometimes used for foreign [v] but is outside the 28-consonant inventory. A moon letter (الـفَم → *al-fam*). Stable across all registers. Some Maghrebi traditions write *fāʾ* with the dot below.
- **21 `/q/` `ق` قاف *qāf* — U+0642 (grouped with emphatics).** Voiceless uvular plosive — articulated further back than velar `/k/`. Though not pharyngealised, it patterns with the emphatics: it resists *imāla* and tends to back adjacent `/a/` to [ɑ], so it is conventionally grouped with the emphatic/*tafkhīm* set. Major dialectal realisations: [q] retained in MSA/Classical and many rural/Bedouin and Maghrebi varieties; [ʔ] in urban Levantine, Cairene and Maltese (qāf→hamza); [ɡ] in Gulf, Bedouin, Upper Egyptian and Sudanese; [k] in some Palestinian rural speech. The shipped standards keep [q]; collapsing it to [ʔ] would destroy the q/ʔ contrast that mirrors the source. A moon letter (الـقَلْب → *al-qalb*).
- **22 `/k/` `ك` كاف *kāf* — U+0643.** Voiceless velar plosive — the plain (non-uvular) dorsal stop, contrasting with uvular ق `/q/` (كَلْب *kalb* "dog" vs قَلْب *qalb* "heart"). Lightly aspirated in onsets; fronted toward palatal [k̟] before front vowels and backed before back vowels. Unlike the source's *begadkephat kāf*, Arabic ك does NOT spirantise to [x] — that is one of the points where Arabic diverges from Syriac/Hebrew (Arabic has no hard/soft alternation). A moon letter (الـكَلْب → *al-kalb*).
- **23 `/l/` `ل` لام *lām* — U+0644.** Voiced alveolar lateral, normally "clear/light" [l] in all positions (unlike English, which darkens coda `/l/`). The signature exception is the name الله *Allāh*: after `/a/` or `/u/` the *lām* is pronounced emphatic/velarised "dark" [lˤ] ([ʔalˤˈlˤɑːh]), but stays light after `/i/` (بِسْمِ ٱللّٰه *bismi-llāh*, light [l]). *Lām* is the consonant of the definite article ال: it assimilates entirely into the following sun letter (الشمس *aš-šams*) and remains [l] before moon letters (القمر *al-qamar*). The *lām-alif* ligature لا (`U+FEFB`) is a required orthographic ligature.
- **24 `/m/` `م` ميم *mīm* — U+0645.** Voiced bilabial nasal, stable in all positions and registers. A moon letter (الـمَاء → *al-māʾ*). In *tajwīd*, a *mīm sākina* before ب assimilates with *ghunna* (nasalisation) — *ikhfāʾ shafawī* — and geminate مّ carries an obligatory two-beat *ghunna*.
- **25 `/n/` `ن` نون *nūn* — U+0646.** Voiced alveolar nasal. A sun letter (الـنُّور → *an-nūr*). Highly active in *tajwīd* as the *nūn sākina* / *tanwīn*, with four classic behaviours before different following letters: *iẓhār* (clear, before throat letters ء ه ع ح غ خ), *idghām* (assimilation, with/without *ghunna* into ي ر م ل و ن), *iqlāb* (→ [m] before ب), and *ikhfāʾ* (partial nasal hiding before the remaining letters). Assimilates in place to a following velar/uvular as [ŋ] (e.g. before ك/ق). *Tanwīn* (nunation ـً ـٍ ـٌ) is phonetic `/-n/` written as doubled vowel diacritics and dropped in pausal forms.
- **26 `/h/` `ه` هاء *hāʾ* — U+0647.** Voiceless glottal fricative, distinct from pharyngeal ح `/ħ/` (هاء is a simple breath, حاء a pharyngeal constriction). A guttural/throat letter and moon letter (الـهَوَاء → *al-hawāʾ*). The 3rd-masc-sg suffix ـه (-hu/-hi) often realises a long vowel in connected recitation (*madd al-ṣila* in *tajwīd*). Note the related grapheme *tāʾ marbūṭa* ة, written like ه with two dots, read [t] in liaison but [h]/zero in pause.
- **27 `/w/` `و` واو *wāw* — U+0648 (non-connecting; glide; *mater lectionis*).** Voiced labial-velar glide [w] as a consonant (وَلَد *walad*). The same letter و doubles as a *mater lectionis*: it writes the long vowel `/uː/` (نُور *nūr*) and is the second element of the diphthong `/aw/` (يَوْم *yawm*). A non-connecting moon letter (الـوَلَد → *al-walad*). Glide and vowel uses are disambiguated by the harakat and syllable structure, not by the letter shape.
- **28 `/j/` `ي` ياء *yāʾ* — U+064A (glide; *mater lectionis*).** Voiced palatal glide [j] as a consonant (يَد *yad* "hand"). The same letter ي doubles as a *mater lectionis*: it writes the long vowel `/iː/` (كَبِير *kabīr*) and is the second element of the diphthong `/aj/` (بَيْت *bayt*). A moon letter (الـيَد *al-yad*). In final position it may be written dotless as *alif maqṣūra* ى (`U+0649`), realised as `/aː/` rather than `/j/` or `/iː/` — an orthographic, not phonemic, distinction.

### Unicode Codepoints

Quick-reference table of the 28 base consonant letters and the additional/related codepoints cited above.

| IPA | Letter | Codepoint |
|---|---|---|
| `/ʔ/` | `ء` *hamza* | `U+0621` |
| (seat) | `أ` hamza-on-alif above | `U+0623` |
| (seat) | `إ` hamza-on-alif below | `U+0625` |
| (seat) | `ؤ` hamza-on-wāw | `U+0624` |
| (seat) | `ئ` hamza-on-yāʾ | `U+0626` |
| `/b/` | `ب` *bāʾ* | `U+0628` |
| `/t/` | `ت` *tāʾ* | `U+062A` |
| `/θ/` | `ث` *thāʾ* | `U+062B` |
| `/dʒ/` | `ج` *jīm* | `U+062C` |
| `/ħ/` | `ح` *ḥāʾ* | `U+062D` |
| `/x/` | `خ` *khāʾ* | `U+062E` |
| `/d/` | `د` *dāl* | `U+062F` |
| `/ð/` | `ذ` *dhāl* | `U+0630` |
| `/r/` | `ر` *rāʾ* | `U+0631` |
| `/z/` | `ز` *zāy* | `U+0632` |
| `/s/` | `س` *sīn* | `U+0633` |
| `/ʃ/` | `ش` *shīn* | `U+0634` |
| `/sˤ/` | `ص` *ṣād* | `U+0635` |
| `/dˤ/` | `ض` *ḍād* | `U+0636` |
| `/tˤ/` | `ط` *ṭāʾ* | `U+0637` |
| `/ðˤ/` | `ظ` *ẓāʾ* | `U+0638` |
| `/ʕ/` | `ع` *ʿayn* | `U+0639` |
| `/ɣ/` | `غ` *ghayn* | `U+063A` |
| `/f/` | `ف` *fāʾ* | `U+0641` |
| `/q/` | `ق` *qāf* | `U+0642` |
| `/k/` | `ك` *kāf* | `U+0643` |
| `/l/` | `ل` *lām* | `U+0644` |
| `/m/` | `م` *mīm* | `U+0645` |
| `/n/` | `ن` *nūn* | `U+0646` |
| `/h/` | `ه` *hāʾ* | `U+0647` |
| `/w/` | `و` *wāw* | `U+0648` |
| `/j/` | `ي` *yāʾ* | `U+064A` |
| — | `ٱ` *hamzat al-waṣl* (alif waṣla) | `U+0671` |
| — | `ة` *tāʾ marbūṭa* | `U+0629` |
| — | `ى` *alif maqṣūra* | `U+0649` |
| — | `لا` *lām-alif* ligature | `U+FEFB` |
| — | `پ` *pe* (foreign [p], non-inventory) | `U+067E` |
| — | `ڤ` *ve* (foreign [v], non-inventory) | `U+06A4` |

### Natural Classes

Groupings of the consonant phonemes by shared phonological features, drawn from the source data.

| Class | Members |
|---|---|
| Plosives | `/ʔ/`, `/b/`, `/t/`, `/d/`, `/tˤ/`, `/dˤ/`, `/k/`, `/q/` |
| Affricates | `/dʒ/` |
| Fricatives | `/f/`, `/θ/`, `/ð/`, `/s/`, `/z/`, `/sˤ/`, `/ðˤ/`, `/ʃ/`, `/x/`, `/ɣ/`, `/ħ/`, `/ʕ/`, `/h/` |
| Nasals | `/m/`, `/n/` |
| Approximants | `/l/`, `/j/`, `/w/` |
| Trill | `/r/` |
| Emphatics (pharyngealized) | `/tˤ/`, `/sˤ/`, `/dˤ/`, `/ðˤ/` |
| Uvular | `/q/`, `/x/`, `/ɣ/` |
| Pharyngeals | `/ħ/`, `/ʕ/` |
| Interdentals | `/θ/`, `/ð/`, `/ðˤ/` |
| Gutturals + emphatics (grouped) | `/tˤ/`, `/sˤ/`, `/dˤ/`, `/ðˤ/`, `/q/`, `/x/`, `/ɣ/`, `/ħ/`, `/ʕ/`, `/h/`, `/ʔ/` |
| Sibilants | `/s/`, `/z/`, `/sˤ/`, `/ʃ/`, `/dʒ/` |
| Obstruents | `/ʔ/`, `/b/`, `/t/`, `/d/`, `/tˤ/`, `/dˤ/`, `/k/`, `/q/`, `/dʒ/`, `/f/`, `/θ/`, `/ð/`, `/s/`, `/z/`, `/sˤ/`, `/ðˤ/`, `/ʃ/`, `/x/`, `/ɣ/`, `/ħ/`, `/ʕ/`, `/h/` |
| Sonorants | `/m/`, `/n/`, `/l/`, `/r/`, `/j/`, `/w/` |
| Voiceless | `/ʔ/`, `/t/`, `/tˤ/`, `/k/`, `/q/`, `/f/`, `/θ/`, `/s/`, `/sˤ/`, `/ʃ/`, `/x/`, `/ħ/`, `/h/` |
| Voiced | `/b/`, `/d/`, `/dˤ/`, `/dʒ/`, `/ð/`, `/z/`, `/ðˤ/`, `/ɣ/`, `/ʕ/`, `/m/`, `/n/`, `/l/`, `/r/`, `/j/`, `/w/` |
| Sun letters (الحروف الشمسية *shamsiyya*) | `/t/`, `/θ/`, `/d/`, `/ð/`, `/r/`, `/z/`, `/s/`, `/ʃ/`, `/sˤ/`, `/dˤ/`, `/tˤ/`, `/ðˤ/`, `/l/`, `/n/` |
| Moon letters (الحروف القمرية *qamariyya*) | `/ʔ/`, `/b/`, `/dʒ/`, `/ħ/`, `/x/`, `/ʕ/`, `/ɣ/`, `/f/`, `/q/`, `/k/`, `/m/`, `/h/`, `/w/`, `/j/` |

**Natural-classes notes.** The sun-letter (الحروف الشمسية) vs moon-letter (الحروف القمرية) split is a phonologically defined class governing definite-article ال assimilation: before a SUN letter (all coronals) the *lām* of ال assimilates into a geminate of the following consonant (الشمس → *aš-šams*, not *al-šams*); before a MOON letter the *lām* stays [l] (القمر → *al-qamar*). The 14 sun letters are exactly the coronal obstruents and coronal sonorants l, n; the 14 moon letters are the labials, dorsals, gutturals and glides. The emphatic series tˤ sˤ dˤ ðˤ (often joined by q in emphasis-spread discussion) triggers *tafkhīm* (velarisation/pharyngealisation) of adjacent vowels and consonants. ح ħ and ع ʕ are the true pharyngeals; together with ء ʔ, ه h, خ x and غ ɣ they form the broader "guttural" (حلقية *ḥalqiyya*) grouping relevant to *tajwīd* and to root-cooccurrence constraints.

### Source Inventory Mapping

How the Arabic consonant inventory maps onto the source's 34-symbol Syriac/Aramaic inventory.

**Summary.** Arabic natively hosts ~25 of the source's 34 Syriac symbols 1:1, the highest overlap of any target language in the project (a Semitic-sibling effect).

#### Hosted 1:1 (source symbol → Arabic letter)

| Source symbol | Arabic letter |
|---|---|
| `ʔ` | ء |
| `b` | ب |
| `d` | د |
| `h` | ه |
| `w` | و |
| `z` | ز |
| `ħ` | ح |
| `tˤ` | ط |
| `j` | ي |
| `k` | ك |
| `l` | ل |
| `m` | م |
| `n` | ن |
| `s` | س |
| `ʕ` | ع |
| `f` | ف |
| `sˤ` | ص |
| `q` | ق |
| `r` | ر |
| `ʃ` | ش |
| `t` | ت |
| `θ` | ث |
| `ð` | ذ |
| `x` | خ |
| `ɣ` | غ |

#### Arabic-only (not in the source)

| Arabic phoneme | Note |
|---|---|
| `dˤ` (ض) | voiced emphatic; the source has tˤ and sˤ but NOT dˤ or ðˤ |
| `ðˤ` (ظ) | voiced emphatic interdental; source-absent |

#### Source-only gaps in Arabic (Peshitta reader mappings)

| Source symbol | Gap & Peshitta reader mapping |
|---|---|
| `v` | no native `/v/` → Peshitta reader maps v→ف (merge into f) |
| `p` | no native `/p/` → Peshitta reader maps p→ب (merge into b) |
| `ɡ` | no native plosive `/ɡ/` → Peshitta reader maps ɡ→ج (realization; ج is canonically [dʒ] in MSA but [ɡ] in Egyptian/older Classical, so the grapheme covers the source velar stop) |

---

*Section authored for the Arabic Pronunciation Guide. — Shin*

## Vowels & Harakat

The Arabic vowel system: a compact, symmetrical THREE-QUALITY × TWO-LENGTH inventory — short /a i u/ and long /aː iː uː/ — plus the two diphthongs /aj/ and /aw/ (treated more fully in the diphthongs section). This is far smaller than the source's six-quality Syriac/Aramaic vowel set (e/i and o/u distinguished), and the mapping is therefore a MERGE: Syriac /e/ and /i/ both surface as Arabic kasra /i ~ iː/, and Syriac /o/ and /u/ both surface as Arabic ḍamma /u ~ uː/ (matching attested Western Syriac vocalism). What Arabic loses in vowel quality it regains in precision elsewhere: vowel LENGTH is phonemic and reliably written (via the matres lectionis), and the consonant inventory is a near-1:1 sibling of the source. Two reference registers are documented in parallel throughout this guide, mirroring the Eastern/Western traditions of the Peshitta guide and the GA/RP pairing of the English guide: MSA = Modern Standard Arabic (الفصحى al-fuṣḥā), and CLASSICAL/QURANIC = the tajwīd careful-recitation register (لغة القرآن). IPA conventions: /slashes/ = phonemic, [brackets] = phonetic detail; length marked /ː/; vowels written in Arabic are normally UNWRITTEN — they appear only as optional ḥarakāt (تشكيل tashkīl) diacritics, shown vocalized in all examples below.

### Overview

Three vowel qualities — open /a/, close-front /i/, close-back-rounded /u/ — each with a phonemic short~long contrast; plus two diphthongs /aj/, /aw/.

| Property | Value |
|---|---|
| Short vowels | `/a/` `/i/` `/u/` |
| Long vowels | `/aː/` `/iː/` `/uː/` |
| Diphthongs | `/aj/` `/aw/` |
| Phonemic length | Yes — contrastive |

**Phonemic length.** Length is contrastive and lexically/grammatically meaningful: e.g. كَتَبَ *kataba* 'he wrote' vs كَاتَبَ *kātaba* 'he corresponded'; عَلِمَ *ʕalima* 'he knew' vs عَالِم *ʕālim* 'scholar'. Short vowels are written only with ḥarakāt diacritics; long vowels are written with the matres lectionis ا (alif) ي (yāʾ) و (wāw), so long vowels survive even in unvocalized text while short vowels do not.

**No reduced vowel.** Arabic has NO schwa /ə/ and NO reduced/ḥaṭaf vowels. Every written vowel is fully realized; absence of a vowel is marked by sukūn ـْ. (Epenthetic/anaptyctic [ə]-like transitions can appear in fast speech to break up clusters, but they are non-phonemic and never written.)

**Comparison to the source (Syriac/Aramaic).** The Syriac/Aramaic source distinguishes SIX vowel qualities (a, ɑ/ɔ, e/ɛ, i, o, u). Arabic has only THREE. The reader-tier collapse is: source e/ɛ → kasra /i ~ iː/ (length from a following bare Yudh → matching ī); source o → ḍamma /u ~ uː/ (length from a following bare Waw → matching ū). The Syriac qualitative a/ɑ(/ɔ) distinction is realized in Arabic ALLOPHONICALLY (plain [a]~[æ] vs backed [ɑ] near emphatics/pharyngeals), not phonemically. The full six-way Syriac-name mapping is tabulated under Cross-Reference below; the only lossy quality merges are e/i and o/u.

**Comparison to Hebrew.** Tiberian Biblical Hebrew has a richer 7-quality niqqud system (Patach /a/, Qamats /ɔ/, Segol /ɛ/, Tsere /e/, Hiriq /i/, Holam /o/, Qubuts/Shuruq /u/), plus reduced shva/ḥaṭaf vowels. Arabic, by contrast, has no phonemic reduced/ultra-short vowel: sukūn marks the ABSENCE of a vowel, not a schwa. Where Hebrew points qamats /ɔ/ vs patach /a/, Arabic has only fatḥa /a/ (with allophonic backing to [ɑ]).

### Reference Registers

Two register-standards are documented in parallel, the Arabic analog of the guide's GA/RP and Eastern/Western pairs.

| Register | Name | Note |
|---|---|---|
| MSA | Modern Standard Arabic (الفصحى *al-fuṣḥā*) | The contemporary pan-Arab literary/formal standard. Short vowels are somewhat more peripheral and length is often less sharply maintained in casual delivery; final short case vowels (iʿrāb) are frequently dropped (pausal/colloquializing tendency). /a/ is commonly fronted to [æ] away from emphatics. |
| Classical / Quranic | Classical / Quranic Arabic (لغة القرآن, tajwīd register) | The older codified form preserved in careful Quranic recitation (tajwīd). Vowel LENGTH is strictly observed and even further specified by madd (prolongation) rules — natural madd ≈ 2 morae, while obligatory/permissible madd can reach 4–6 morae. Backing (tafkhīm) and imāla are systematically governed. Genre-appropriate for scripture; preserves every MSA contrast plus finer durational detail. |

### Vowel Inventory

The six monophthongs (three qualities × two lengths), with their ḥaraka spelling, codepoints, articulatory description, and vocalized examples. Long vowels are spelled as a short ḥaraka plus a mater lectionis.

| IPA | Name | Arabic name | Ḥaraka | Mater | Length | Height | Backness | Rounding | Default realization |
|---|---|---|---|---|---|---|---|---|---|
| `/a/` | fatḥa (short a) | فَتْحَة | `ـَ` | — | short | open | front-to-central | unrounded | [a] (often fronted to [æ] in MSA away from emphatics) |
| `/aː/` | fatḥa + alif (long ā) | فَتْحَة وَأَلِف | `ـَا` | `ا` (alif, `U+0627`) | long | open | front-to-central (backs near emphatics) | unrounded | [aː] ~ [æː] (plain); [ɑː] (backed, near emphatics/pharyngeals) |
| `/i/` | kasra (short i) | كَسْرَة | `ـِ` | — | short | close (lowered to [ɪ] near emphatics) | front | unrounded | [i] (plain); [ɪ] (lowered/backed near emphatics & pharyngeals) |
| `/iː/` | kasra + yāʾ (long ī) | كَسْرَة وَيَاء | `ـِي` | `ي` (yāʾ, `U+064A`) | long | close | front | unrounded | [iː] (plain); [ɪː] (near emphatics) |
| `/u/` | ḍamma (short u) | ضَمَّة | `ـُ` | — | short | close (lowered to [ʊ] near emphatics) | back | rounded | [u] (plain); [ʊ]~[o] (lowered/backed near emphatics & pharyngeals) |
| `/uː/` | ḍamma + wāw (long ū) | ضَمَّة وَوَاو | `ـُو` | `و` (wāw, `U+0648`) | long | close | back | rounded | [uː] (plain); [ʊː]~[oː] (near emphatics) |

#### Codepoint Reference

The Unicode points making up each vowel's vocalized spelling (ḥaraka, plus mater where long).

| IPA | Ḥaraka | Codepoint(s) | Unicode name(s) |
|---|---|---|---|
| `/a/` | `ـَ` | `U+064E` | ARABIC FATHA |
| `/aː/` | `ـَا` | `U+064E U+0627` | ARABIC FATHA + ALIF |
| `/i/` | `ـِ` | `U+0650` | ARABIC KASRA |
| `/iː/` | `ـِي` | `U+0650 U+064A` | ARABIC KASRA + YEH |
| `/u/` | `ـُ` | `U+064F` | ARABIC DAMMA |
| `/uː/` | `ـُو` | `U+064F U+0648` | ARABIC DAMMA + WAW |

#### Sample Words

Vocalized examples for each vowel, with romanization, phonemic transcription, and gloss.

| Vowel | Arabic (vocalized) | Romanization | IPA | Gloss |
|---|---|---|---|---|
| `/a/` | مَنْ | man | `/man/` | who |
| `/a/` | كَتَبَ | kataba | `/ka.ta.ba/` | he wrote |
| `/a/` | بَحْر | baḥr | `/baħr/` | sea |
| `/aː/` | بَاب | bāb | `/baːb/` | door |
| `/aː/` | كَاتِب | kātib | `/kaː.tib/` | writer |
| `/aː/` | صَامَ | ṣāma | `/sˤɑːma/` | he fasted (backed ā) |
| `/i/` | مِنْ | min | `/min/` | from |
| `/i/` | بِنْت | bint | `/bint/` | girl |
| `/i/` | عِلْم | ʕilm | `/ʕilm/` | knowledge |
| `/iː/` | كَبِير | kabīr | `/ka.biːr/` | big |
| `/iː/` | فِيل | fīl | `/fiːl/` | elephant |
| `/iː/` | دِين | dīn | `/diːn/` | religion |
| `/u/` | كُلّ | kull | `/kull/` | all/every |
| `/u/` | أُمّ | ʾumm | `/ʔumm/` | mother |
| `/u/` | قُل | qul | `/qul/` | say! (backed → [qʊl]) |
| `/uː/` | نُور | nūr | `/nuːr/` | light |
| `/uː/` | يَقُولُ | yaqūlu | `/ja.quː.lu/` | he says |
| `/uː/` | مَكْتُوب | maktūb | `/mak.tuːb/` | written |

#### Allophony Notes by Vowel

- **`/a/` fatḥa** — Plain fatḥa is front-central [a], commonly raised toward [æ] in MSA. It BACKS to [ɑ] adjacent to the emphatics ط tˤ, ص sˤ, ض dˤ, ظ ðˤ (and frequently ق q, ر r, sometimes خ x, غ ɣ) and to the pharyngeals ح ħ, ع ʕ — this is emphasis spread (tafkhīm). In some Classical and dialectal contexts fatḥa undergoes IMĀLA, raising toward [e] or [i] (see Allophony section). Realized long as fatḥa + alif.
- **`/aː/` fatḥa + alif** — Long /aː/ is the most allophonically variable Arabic vowel: front [æː] in plain/coronal environments (e.g. كَاتِب *kātib* [kæːtib]), but firmly back [ɑː] under emphasis (e.g. صَام *ṣāma* [sˤɑːmæ]→[sˤɑːm]). This [æː]~[ɑː] split is the chief phonetic correlate of emphasis in Arabic and the nearest Arabic analog to the source's a/ɑ qualitative distinction — but it is ALLOPHONIC (predictable from environment), not phonemic. The carrier alif ا is a non-connecting letter and a pure mater lectionis here (it bears no vowel of its own). In Quranic recitation /aː/ is the locus of madd prolongation.
- **`/i/` kasra** — Close front [i]; lowers and slightly retracts toward [ɪ]~[e] adjacent to emphatics and pharyngeals (emphasis spread also affects high vowels, not only /a/). Source Syriac /e/ AND /i/ both map onto Arabic kasra (the e/i merge). Realized long as kasra + yāʾ.
- **`/iː/` kasra + yāʾ** — Long close front [iː]; the carrier yāʾ ي functions as a pure mater lectionis (it would be the consonant /j/ if it bore its own vowel). Backs/lowers to [ɪː] under emphasis. The source's long /eː/ and /iː/ both surface here (length is preserved via the mater). Subject to madd prolongation in tajwīd.
- **`/u/` ḍamma** — Close back rounded [u]; lowers toward [ʊ]~[o] near emphatics/pharyngeals and /q/ (e.g. قُل *qul* [qʊl]). Source Syriac /o/ AND /u/ both map onto Arabic ḍamma (the o/u merge, matching Western Syriac vocalism). Realized long as ḍamma + wāw.
- **`/uː/` ḍamma + wāw** — Long close back rounded [uː]; carrier wāw و is a pure mater lectionis here (it would be the consonant /w/ if it bore its own vowel). Lowers to [ʊː]~[oː] under emphasis. The source's long /oː/ and /uː/ both surface here. Subject to madd prolongation in tajwīd.

### Diphthongs (Summary)

Arabic has two phonemic diphthongs, both with a fatḥa nucleus plus a glide written as bare (sukūn-bearing) yāʾ or wāw. Treated in full in the diphthongs section; summarized here for completeness of the vowel inventory.

| IPA | Name | Spelling | Codepoints | Register note |
|---|---|---|---|---|
| `/aj/` | ay | `ـَيْ` (fatḥa + yāʾ with sukūn) | `U+064E U+064A U+0652` | MSA [aj]~[aɪ]; many dialects monophthongize to [eː]. Classical keeps the diphthong crisp. |
| `/aw/` | aw | `ـَوْ` (fatḥa + wāw with sukūn) | `U+064E U+0648 U+0652` | MSA [aw]~[aʊ]; many dialects monophthongize to [oː]. Classical keeps the diphthong crisp. |

**Diphthong examples.**

| Diphthong | Arabic (vocalized) | Romanization | IPA | Gloss |
|---|---|---|---|---|
| `/aj/` | بَيْت | bayt | `/bajt/` | house |
| `/aj/` | كَيْفَ | kayfa | `/kaj.fa/` | how |
| `/aw/` | يَوْم | yawm | `/jawm/` | day |
| `/aw/` | نَوْم | nawm | `/nawm/` | sleep |

### Allophony

Arabic vowel quality is highly context-dependent. The three signature processes are emphatic/pharyngeal BACKING, IMĀLA (fronting/raising of /a/), and predictable length adjustments.

#### Tafkhīm — Emphasis Spread (تَفْخِيم)

Adjacency to an emphatic (pharyngealized) or pharyngeal consonant retracts and lowers neighboring vowels.

**Triggers:** ط tˤ, ص sˤ, ض dˤ, ظ ðˤ, ق q (often), ر r (often, when 'heavy'), ح ħ, ع ʕ, خ x / غ ɣ (variably).

| Vowel | Plain | Backed | Example | Romanization | Phonetic | Gloss |
|---|---|---|---|---|---|---|
| `/a/`, `/aː/` | [a]~[æ(ː)] | [ɑ(ː)] | طَاب | ṭāba | [tˤɑːb] | it was good |
| `/i/`, `/iː/` | [i(ː)] | [ɪ(ː)] | صِين | ṣīn | [sˤɪːn] | China |
| `/u/`, `/uː/` | [u(ː)] | [ʊ(ː)]~[o(ː)] | قُلْت | qultu | [qʊltu] | I said |

- **Spread:** Emphasis spreads bidirectionally across the syllable/word from the emphatic consonant, affecting all vowels (and some consonants) in its domain; the [æ(ː)]~[ɑ(ː)] contrast on /a(ː)/ is its most audible exponent and the closest Arabic analog to the source's phonemic a/ɑ split.
- **Note:** This backing is the principal reason urban-Levantine (which loses the emphatics ث/ذ/ظ and qāf) is documented-only and NOT shipped: collapsing the emphatics destroys the very vowel-backing contrasts that make Arabic a faithful match for the Semitic source.

#### Imāla (إِمَالَة, 'inclination')

Raising/fronting of /a/ and especially /aː/ toward [e] or [i], typically in the neighborhood of front/high segments (an original kasra or a yāʾ) and away from emphatics/back consonants.

- **Registers:** A regular, codified feature of several Quranic recitation traditions (notably the reading of Ḥamza/al-Kisāʾī and Warš in specific words) and pervasive in many modern dialects (e.g. final feminine -ة realized [-e]). In default MSA it is largely suppressed/leveled to [a(ː)].
- **Note:** Imāla is qualitatively parallel to the source's having distinct front-mid /e/ — Arabic recovers an [e]-like quality contextually even though /e/ is not phonemic. It is the mirror-image process to emphatic backing.

| Arabic (vocalized) | Romanization | Phonetic | Gloss |
|---|---|---|---|
| النَّاس | an-nās → an-nēs (imāla) | [anneːs] | the people (with imāla) |
| مَجْرَاهَا | majrāhā → majrēhā | [madʒreːhaː] | its course (Quranic imāla, Hūd 11:41) |

#### Short /a/ vs Long /aː/ Realization

Short /a/ and long /aː/ share a phoneme quality but differ in duration AND, often, in peripherality. Short /a/ is centralized and short; long /aː/ is more peripheral and ~1.5–2× the duration. In plain contexts both front toward [æ]/[æː] in MSA; both back to [ɑ]/[ɑː] under emphasis. In careful Quranic delivery /aː/ may be prolonged well beyond 2 morae under madd rules while short /a/ never lengthens. Final short /a/ (and other short vowels) is dropped utterance-finally in PAUSAL form (waqf).

#### High-Vowel Lowering

In closed and/or unstressed syllables and near gutturals, short /i/ and /u/ commonly lower to [ɪ] and [ʊ].

| Arabic (vocalized) | Romanization | Phonetic | Gloss |
|---|---|---|---|
| بِنْت | bint | [bɪnt] | girl |
| كُلّ | kull | [kʊll] | all |

### Ḥarakāt — The Vocalization Diacritics (تَشْكِيل)

The ḥarakāt (حَرَكَات, 'movements') are the optional vocalization diacritics (تَشْكِيل *tashkīl*) that mark short vowels, vowel-absence, gemination, and nunation on the consonantal abjad. Texts are normally written WITHOUT them; full vocalization (مُشَكَّل *mushakkal*) is used for the Quran, children's/learners' material, poetry, and disambiguation. They are written in logical order AFTER their host consonant in the code stream even though rendered above/below it. The Arabic Peshitta's Vocalized reader tier supplies the full ḥarakāt; the Unvocalized tier strips them.

#### Short-Vowel Marks

| Name | Arabic name | Character | Codepoint | Unicode name | Position | IPA | Function |
|---|---|---|---|---|---|---|---|
| fatḥa | فَتْحَة | `ـَ` | `U+064E` | ARABIC FATHA | above | `/a/` | marks short /a/ on the preceding consonant |
| kasra | كَسْرَة | `ـِ` | `U+0650` | ARABIC KASRA | below | `/i/` | marks short /i/ on the preceding consonant |
| ḍamma | ضَمَّة | `ـُ` | `U+064F` | ARABIC DAMMA | above | `/u/` | marks short /u/ on the preceding consonant |

- **fatḥa** — With a following alif ا it spells long /aː/; with a following bare yāʾ/wāw + sukūn it forms the diphthongs /aj/, /aw/. A superscript-alif variant (dagger alif, ـٰ `U+0670`) marks an unwritten long /aː/ in some Classical spellings (e.g. هَٰذَا *hādhā* 'this', الله *allāh*).
- **kasra** — With a following yāʾ ي it spells long /iː/. The only ḥaraka written below the line (with kasratān).
- **ḍamma** — Shaped like a miniature wāw و. With a following wāw و it spells long /uː/.

#### Sukūn — Vowel Absence

| Name | Arabic name | Character | Codepoint | Unicode name | Position | IPA | Function |
|---|---|---|---|---|---|---|---|
| sukūn | سُكُون | `ـْ` | `U+0652` | ARABIC SUKUN | above | ∅ (no vowel) | marks that the consonant has NO following vowel (closes a syllable / forms a consonant cluster) |

**Note:** Arabic's sukūn is the absence of a vowel, NOT a schwa — contrast Hebrew/Aramaic mobile shva [ə]. A consonant under sukūn is the coda of CVC/CVːC or the second member of a final CVCC cluster. Sometimes drawn as a small circle ـْ or a head-of-jīm shape (ۡ `U+06E1`, 'small high dotless head of khāh') in Quranic typography.

#### Shadda — Gemination

| Name | Arabic name | Character | Codepoint | Unicode name | Position | IPA | Function |
|---|---|---|---|---|---|---|---|
| shadda | شَدَّة | `ـّ` | `U+0651` | ARABIC SHADDA | above | Cː (geminate / doubled consonant) | marks gemination of the host consonant; CONTRASTIVE |

**Note:** Shadda doubles (lengthens) the consonant: contrastive — دَرَسَ *darasa* 'he studied' vs دَرَّسَ *darrasa* 'he taught'. It STACKS with a vowel mark: a following fatḥa/ḍamma sits above the shadda, a following kasra below it (or, in some traditions, just under the shadda). The lām of an assimilated definite article over a sun letter is written with shadda (e.g. الشَّمْس *aš-šams*). Gemination is phonemic and weight-bearing for stress.

**Stacking examples.**

| Arabic (vocalized) | Romanization | IPA | Gloss |
|---|---|---|---|
| مُدَرِّس | mudarris | `/mu.dar.ris/` | teacher (shadda + kasra on rāʾ) |
| حَجّ | ḥajj | `/ħadʒː/` | pilgrimage (geminate jīm) |

#### Tanwīn — Nunation

Doubled ḥarakāt marking indefinite case endings, pronounced as the vowel + a final /n/. They appear utterance-medially; in PAUSAL form (waqf) the /n/ is dropped (and fatḥatān typically surfaces as a long [aː]). The source IPA is caseless, so tanwīn/iʿrāb endings are descriptive only and are NOT emitted in the Peshitta reader tier.

| Name | Arabic name | Character | Codepoint | Unicode name | Position | IPA | Note |
|---|---|---|---|---|---|---|---|
| fatḥatān (tanwīn fatḥ) | فَتْحَتَان | `ـً` | `U+064B` | ARABIC FATHATAN | above | `/an/` | Usually written on a carrier alif (ـًا) except after tāʾ marbūṭa ة or hamza on alif; e.g. شُكْرًا *shukran* 'thanks' `/ʃuk.ran/` → pausal [ʃukraː]. |
| ḍammatān (tanwīn ḍamm) | ضَمَّتَان | `ـٌ` | `U+064C` | ARABIC DAMMATAN | above | `/un/` | Indefinite nominative; e.g. كِتَابٌ *kitābun* 'a book' `/ki.taː.bun/`. |
| kasratān (tanwīn kasr) | كَسْرَتَان | `ـٍ` | `U+064D` | ARABIC KASRATAN | below | `/in/` | Indefinite genitive; e.g. كِتَابٍ *kitābin* `/ki.taː.bin/`. |

#### Auxiliary Marks

Vowel-related marks beyond the core ḥarakāt (short-vowel marks, sukūn, shadda, tanwīn), used in fully-pointed (especially Quranic) text.

| Name | Arabic name | Character | Codepoint | Unicode name | IPA | Note |
|---|---|---|---|---|---|---|
| dagger alif (alif khanjariyya) | أَلِف خَنْجَرِيَّة | `ـٰ` | `U+0670` | ARABIC LETTER SUPERSCRIPT ALEF | `/aː/` | A superscript stroke marking a long /aː/ that is not written with a full alif, e.g. هَٰذَا *hādhā* 'this', رَحْمَٰن *raḥmān*, لَٰكِن *lākin*, اللّٰه *allāh*. |
| hamzat waṣl | هَمْزَة وَصْل | `ٱ` | `U+0671` | ARABIC LETTER ALEF WASLA | ∅ medially / prosthetic vowel initially | An elidable connecting hamza on an initial alif. Utterance-initially it carries a prosthetic short vowel (usually /i/, e.g. اِسْم *ism*); after a preceding vowel it ELIDES, e.g. فِي ٱلْبَيْت *fi l-bayt* 'in the house'. Resolves Arabic's ban on word-initial consonant clusters; relevant to vowel realization at word boundaries. |
| maddah | مَدَّة | `ـٓ` | `U+0653` | ARABIC MADDAH ABOVE | `/ʔaː/` | Written over alif (آ `U+0622`) to mark hamza + long /aː/ (i.e. /ʔaː/), e.g. آدَم *ʾādam*, قُرْآن *qurʾān*. Distinct from (though related to) the tajwīd madd prolongation rules on long vowels. |

### Classical vs MSA Vowels

How the two reference registers differ specifically in vowels.

| Dimension | Difference |
|---|---|
| Length precision | Classical/Quranic strictly maintains and even sub-specifies long-vowel duration (madd, 2–6 morae); MSA tends toward less sharply graded length and shortens long vowels in some closed/unstressed contexts. |
| Imāla | Codified and tradition-specific in Quranic recitation (e.g. Ḥamza, al-Kisāʾī, Warš); largely suppressed/leveled in default MSA. |
| Final short vowels (iʿrāb) | Classical realizes full desinential case/mood vowels (-u/-a/-i, -na etc.); MSA frequently drops final short vowels in pausa and in less formal delivery (the source IPA is caseless, so these are NOT emitted in the reader tier either way). |
| Tafkhīm/backing detail | Both register systems back vowels near emphatics, but tajwīd specifies the precise domain and degree (e.g. the heavy vs light lām of allāh, the heavy rāʾ rules) far more finely than MSA description. |
| Quality stability | The three-quality core /a i u/ is identical across both registers; the divergences are durational and allophonic, never a change in the phonemic vowel inventory. |

### Cross-Reference

#### To the Source (Syriac/Aramaic)

The Peshitta source's SIX vowel qualities collapse into Arabic's THREE. Vowel LENGTH, lost as a contrast in the Syriac diacritics-vs-mater system, is RECOVERED and made explicit in Arabic via the matres lectionis (ا ي و). This is why the Arabic Peshitta is the most faithful / near-reversible reader tier in the project: the consonants map ~1:1 and length is preserved, with only the e/i and o/u quality merges as lossy steps (matching attested Western Syriac vocalism).

| Syriac vowel | Syriac IPA | → Arabic | Arabic IPA | Merge type |
|---|---|---|---|---|
| Pthakha | /a/ | fatḥa | `/a/` | direct |
| Zqapha | /ɑ~ɔ/ | fatḥa (backed allophone [ɑ], or long `/aː/`) | `/a/`, `/aː/` | allophonic / length |
| Rbasa | /e~ɛ/ | kasra | `/i ~ iː/` | **lossy** (e→i) |
| Khwasa | /i/ | kasra | `/i ~ iː/` | direct |
| ʿEsasa | /u/ | ḍamma | `/u ~ uː/` | direct |
| Rwakha | /o/ | ḍamma | `/u ~ uː/` | **lossy** (o→u) |

#### To Hebrew

Tiberian Hebrew distinguishes 7 vowel qualities plus reduced shva/ḥaṭaf vowels; Arabic has 3 and no reduced vowel (sukūn = zero, not schwa). Where Hebrew separates qamats /ɔ/ from patach /a/ and tsere /e/ from segol /ɛ/ and hiriq /i/, Arabic merges each pair into fatḥa /a/ or kasra /i/ respectively. Arabic compensates with a robust, written long~short contrast that Tiberian Hebrew encodes only indirectly (via mater lectionis and qamats gadol/qatan rules).

#### To the English Template

The English guide organizes monophthongs by Wells lexical sets across GA/RP; this section organizes Arabic's far smaller inventory by the three qualities × length across MSA/Classical-Quranic. The English schwa /ə/ and the rich checked/free/weak distribution have no Arabic counterpart — Arabic has no reduced vowel and no vowel-reduction in unstressed syllables; every Arabic vowel is fully realized and length is the primary suprasegmental contrast.

---

*Section authored by Shin.*

## Diphthongs & Long Vowels

Diphthongs and long vowels in Arabic (العربية) are treated together because both are built on the same orthographic machinery — a short vowel (haraka) followed by a glide letter (`و` wāw or `ي` yāʾ). Standard Arabic has exactly TWO phonemic diphthongs, `/aj/` (`ـَيْ`) and `/aw/` (`ـَوْ`), each a sequence of fatḥa `/a/` + a glide carried by yāʾ or wāw bearing sukūn. They contrast with the three LONG VOWELS `/aː iː uː/`, which are written with the very same three carrier letters (`ا و ي`) functioning as *matres lectionis* (حروف المد *ḥurūf al-madd*, 'letters of prolongation') — i.e. `ا و ي` do double duty as both true consonants/glides and as length-markers.

The crucial difference is the vowel on the carrier: when `و`/`ي` carry sukūn after a fatḥa they form the diphthongs `/aw/` `/aj/`, but when they are 'silent' length-carriers homorganic with the preceding haraka (ḍamma + `و`, kasra + `ي`, fatḥa + `ا`) they yield the long monophthongs `/uː iː aː/`. In Classical / Quranic Arabic and careful MSA the diphthongs are preserved as true diphthongs [aj]~[aw]; across most modern spoken dialects they have MONOPHTHONGIZED to mid long vowels [eː] and [oː] (بَيْت *bayt* → [beːt], يَوْم *yawm* → [joːm]) — the same `/aj/`→`/eː/`, `/aw/`→`/oː/` collapse seen historically in the Semitic siblings (Syriac, Hebrew). Length is phonemic throughout: vowel quantity distinguishes lexemes (e.g. كَتَبَ *kataba* 'he wrote' vs كَاتَبَ *kātaba* 'he corresponded'), so the matres are structurally load-bearing, not decorative.

**Phonemic status.** Arabic distinguishes three short vowel qualities `/a i u/` (the harakāt fatḥa/kasra/ḍamma), three long vowels `/aː iː uː/` (the matres `ا`/`و`/`ي`), and two diphthongs `/aj/` `/aw/`. Diphthongs are analyzed phonologically as fatḥa + a tautosyllabic glide `/j/` or `/w/` (i.e. CVG), not as unitary vowel phonemes; this differs from the English template, where the diphthong is a single phonemic unit. Vowel LENGTH (*kammiyya*) is contrastive at every quality, and gemination of the glides (`yy` `/jj/`, `ww` `/ww/`) is separately contrastive via shadda.

### The Two Diphthongs

| Diphthong | Translit. | Vocalized | Components | Type | Description |
|---|---|---|---|---|---|
| `/aj/` | ay | `ـَيْ` | fatḥa `ـَ` `/a/` + yāʾ `ي` with sukūn `ـْ` (glide [j]) | closing (front) | Open-to-palatal closing diphthong: starts at fatḥa [a] and glides up toward the palatal glide [j]. Phonologically `/a/` + tautosyllabic `/j/`. |
| `/aw/` | aw | `ـَوْ` | fatḥa `ـَ` `/a/` + wāw `و` with sukūn `ـْ` (glide [w]) | closing (back) | Open-to-labiovelar closing diphthong: starts at fatḥa [a] and glides up and back toward the rounded labial-velar glide [w]. Phonologically `/a/` + tautosyllabic `/w/`. |

#### `/aj/` — fatḥa + yāʾ·sukūn (`ـَيْ`)

| Word | Translit. | Gloss | Classical | Dialectal |
|---|---|---|---|---|
| بَيْت | bayt | house | `/bajt/` | [beːt] |
| خَيْر | khayr | good, goodness | `/xajr/` | [xeːr] |
| كَيْف | kayf | how | `/kajf/` | [keːf] |
| عَيْن | ʿayn | eye / spring (also the letter `ع`) | `/ʕajn/` | [ʕeːn] |

*Notes.* Spelled fatḥa over the preceding consonant followed by a sukūn-bearing yāʾ. Preserved as a true diphthong [aj] in Classical/Quranic recitation (tajwīd) and in careful MSA reading. In most modern urban dialects (Levantine, much of the Maghreb, urban Egyptian) it monophthongizes to a long close-mid front [eː]; some dialects keep a fronted [ej]. Near emphatic/pharyngeal consonants the onset backs toward [ɑ] (e.g. صَيْف *ṣayf* 'summer' → [sˤɑjf] / dialectal [sˤeːf]). Distinguish the DIPHTHONG `ـَيْ` `/aj/` (yāʾ with sukūn after fatḥa) from the LONG VOWEL `ـِي` `/iː/` (yāʾ as mater after kasra): بَيْت *bayt* `/bajt/` vs بِيت *bīt* `/biːt/`.

#### `/aw/` — fatḥa + wāw·sukūn (`ـَوْ`)

| Word | Translit. | Gloss | Classical | Dialectal |
|---|---|---|---|---|
| يَوْم | yawm | day | `/jawm/` | [joːm] |
| لَوْن | lawn | colour | `/lawn/` | [loːn] |
| صَوْت | ṣawt | voice, sound | `/sˤawt/` | [sˤoːt] |
| نَوْم | nawm | sleep | `/nawm/` | [noːm] |

*Notes.* Spelled fatḥa over the preceding consonant followed by a sukūn-bearing wāw. Preserved as [aw] in Classical/Quranic recitation and careful MSA; monophthongizes to a long close-mid back rounded [oː] in most modern dialects. As with `/aj/`, emphasis spread backs the onset near emphatics/pharyngeals. Distinguish the DIPHTHONG `ـَوْ` `/aw/` (wāw with sukūn after fatḥa) from the LONG VOWEL `ـُو` `/uː/` (wāw as mater after ḍamma): لَوْن *lawn* `/lawn/` vs نُور *nūr* `/nuːr/`.

### Long Vowels — The Matres Lectionis (حروف المد)

The three long vowels of Arabic are written with the *matres lectionis* — the 'letters of prolongation' (حروف المد *ḥurūf al-madd*) `ا` (alif), `و` (wāw) and `ي` (yāʾ). Each carrier must be HOMORGANIC with the preceding short vowel (haraka): alif prolongs fatḥa → `/aː/`, wāw prolongs ḍamma → `/uː/`, yāʾ prolongs kasra → `/iː/`. When the carrier instead bears its own sukūn after a fatḥa, the result is a diphthong, not a long vowel — this is the single contrast that separates the two systems. Long vowels are the structural carriers of phonemic vowel length and are normally written even in unvocalized text, whereas short vowels (harakāt) are usually left unwritten.

| Long Vowel | Translit. | Mater | Vocalized | Formation |
|---|---|---|---|---|
| `/aː/` | ā | `ا` (alif) | `ـَا` | fatḥa `ـَ` `/a/` prolonged by a following bare alif `ا` |
| `/iː/` | ī | `ي` (yāʾ) | `ـِي` | kasra `ـِ` `/i/` prolonged by a following yāʾ `ي` (bearing no vowel of its own) |
| `/uː/` | ū | `و` (wāw) | `ـُو` | ḍamma `ـُ` `/u/` prolonged by a following wāw `و` (bearing no vowel of its own) |

#### `/aː/` — fatḥa + alif (`ـَا`)

| Word | Translit. | Gloss | IPA |
|---|---|---|---|
| كِتَاب | kitāb | book | `/kiˈtaːb/` |
| بَاب | bāb | door | `/baːb/` |
| قَالَ | qāla | he said | `/ˈqaːla/` |

*Notes.* Realized [aː] but BACKED to [ɑː] adjacent to emphatics/pharyngeals/qāf (طَالِب *ṭālib* → [tˤɑːlib]) and RAISED toward [eː]/[æː] by imāla in some Classical/dialectal registers. Word-finally `/aː/` may be written with dotless yāʾ `ى` (alif maqṣūra), e.g. هُدَى *hudā* `/huˈdaː/` 'guidance', or with bare alif. The standalone long-ā at word start is written `آ` (alif madda, U+0622), e.g. آمَنَ *āmana* `/ˈʔaːmana/` 'he believed'. Quranic tajwīd recognises a graded system of *madd* (prolongation) lengths (*madd ṭabīʿī* ~2 morae up to *madd lāzim* ~6 morae) layered on top of this base `/aː/`.

#### `/iː/` — kasra + yāʾ (`ـِي`)

| Word | Translit. | Gloss | IPA |
|---|---|---|---|
| كَبِير | kabīr | big, great | `/kaˈbiːr/` |
| فِيل | fīl | elephant | `/fiːl/` |
| بِنْت | bint | girl, daughter (contrast: short `/i/`, no mater) | `/bint/` |

*Notes.* The yāʾ here is a length-marker, NOT the glide of a diphthong: the preceding haraka must be kasra (homorganic), giving `/iː/`. Contrast with `/aj/`, where the preceding haraka is fatḥa and the yāʾ carries sukūn (بِيت *bīt* `/biːt/` vs بَيْت *bayt* `/bajt/`). Shortened to [i] in unstressed closed syllables in some registers; quality stable [iː] elsewhere.

#### `/uː/` — ḍamma + wāw (`ـُو`)

| Word | Translit. | Gloss | IPA |
|---|---|---|---|
| نُور | nūr | light | `/nuːr/` |
| مَكْتُوب | maktūb | written, letter | `/makˈtuːb/` |
| يَكُون | yakūn | he is / will be | `/jaˈkuːn/` |

*Notes.* The wāw is a length-marker homorganic with ḍamma, giving `/uː/`, NOT the glide of `/aw/` (which follows fatḥa + sukūn). Contrast نُور *nūr* `/nuːr/` with لَوْن *lawn* `/lawn/`. Note the orthographic quirk of the 3rd-person-plural verb ending `وا` (alif al-wiqāya / 'protective alif'), e.g. كَتَبُوا *katabū* `/kataˈbuː/` 'they wrote', where the final alif is silent and the vowel is `/uː/`.

### Writing Length & Diphthongs in the Abjad

How quantity and glides are encoded in the abjad:

- A SHORT vowel is a haraka diacritic alone (fatḥa `ـَ` `/a/`, kasra `ـِ` `/i/`, ḍamma `ـُ` `/u/`) with no following carrier letter; harakāt are optional and usually omitted in running text.
- A LONG vowel is a haraka + a HOMORGANIC carrier letter that bears no vowel: fatḥa + `ا` = `/aː/`, kasra + `ي` = `/iː/`, ḍamma + `و` = `/uː/`. The carrier IS written even in unvocalized text, so length is recoverable from the consonantal skeleton.
- A DIPHTHONG is fatḥa + a NON-homorganic glide carrier bearing sukūn: fatḥa + `يْ` = `/aj/`, fatḥa + `وْ` = `/aw/`. In vocalized text the sukūn on `و`/`ي` is the explicit signal that distinguishes a diphthong from a long vowel.
- Therefore the contrast between `/aj iː/` and between `/aw uː/` rests entirely on the preceding haraka (fatḥa vs kasra/ḍamma); in unvocalized text بيت can be read *bayt* `/bajt/` or *bīt* `/biːt/` and نور as *nūr* `/nuːr/` vs (hypothetically) *nawr* — vocalization (تشكيل *tashkīl*) resolves the ambiguity.

#### Minimal Pairs

| Pair | Contrast |
|---|---|
| بَيْت *bayt* `/bajt/` 'house' vs بِيت *bīt* `/biːt/` 'spend the night (imperative)' | `/aj/` (fatḥa + yāʾ·sukūn) vs `/iː/` (kasra + yāʾ) |
| لَوْن *lawn* `/lawn/` 'colour' vs نُور *nūr* `/nuːr/` 'light' | `/aw/` (fatḥa + wāw·sukūn) vs `/uː/` (ḍamma + wāw) |
| كَتَبَ *kataba* `/ˈkataba/` 'he wrote' vs كَاتَبَ *kātaba* `/ˈkaːtaba/` 'he corresponded' | short `/a/` vs long `/aː/` (mater alif) — phonemic length |

### Monophthongization

The dialectal collapse of `/aj aw/` to mid long monophthongs is the defining diphthong isogloss between the shipped reference standards and the documented-only dialects.

| Register | Treatment of `/aj/` `/aw/` |
|---|---|
| Classical / Quranic | PRESERVE the true diphthongs [aj] and [aw]; monophthongizing them is considered a recitation error (*laḥn*) in careful Quranic reading. This is the register-appropriate target for scripture. |
| MSA | Formal MSA reading nominally preserves `/aj/` `/aw/`, but many speakers carry a dialectal substrate and may realise them as [eː]/[oː] in less careful speech; the prescriptive standard keeps the diphthongs. |
| Dialectal | Across most modern spoken varieties `/aj/` → [eː] and `/aw/` → [oː] (e.g. *bayt* → [beːt], *yawm* → [joːm]). Some conservative dialects (notably parts of the Gulf, Bedouin varieties, and traditional Maghrebi) retain [aj]/[aw]; a few retain a narrow [ej]/[ow]. The result is that many dialects effectively expand the long-vowel inventory from three (`/aː iː uː/`) to five (adding `/eː oː/`), the two new mid vowels being almost entirely reflexes of the old diphthongs (plus a handful of loanwords). |

**Semitic parallel.** This `/aj/`→`/eː/`, `/aw/`→`/oː/` shift is a SHARED Central-Semitic tendency: the same monophthongization is documented in Syriac (where it is largely complete — see the Peshitta guide's 'diphthongs' section) and in Biblical Hebrew (Tiberian, partial). Arabic, especially Classical/Quranic, is the most CONSERVATIVE of the three siblings in retaining the diphthongs intact, which makes Classical Arabic a uniquely faithful witness to the older common-Semitic \*`/aj/` \*`/aw/`.

### Cross-Reference to the Semitic Siblings

Sibling-language framing for the diphthong/long-vowel system — Arabic is a Central-Semitic sister of the source Syriac/Aramaic and of Hebrew.

| Sibling | Diphthong / long-vowel correspondence |
|---|---|
| Syriac (Peshitta) | Syriac has `/aj/` and `/aw/` formed by Yudh/Waw after a Pthakha (fatḥa) vowel, but most have monophthongized to `/eː/` `/oː/`; Syriac also records `/ej/` and `/oj/`. Arabic matches the `/aj/` `/aw/` core 1:1 and shares the monophthongization tendency, but preserves the diphthongs more fully in its Classical register. |
| Biblical Hebrew | Hebrew has `/aj/` (Patach + Yod), `/aw/` (Patach/Qamats + Vav) and `/ej/` (Tsere + Yod), with the same `/aj/`→`/eː/`, `/aw/`→`/oː/` collapse. Arabic lacks a native phonemic `/ej/` at the Classical level (its [eː] is a dialectal reflex of `/aj/`, not an inherited diphthong). |

**Peshitta reader-tier note.** For the Arabic Peshitta reader tiers, the source's monophthongized `/eː/` `/oː/` are mapped onto Arabic via the backbone gap-resolution (e → kasra/ī, o → ḍamma/ū), and source diphthongs `/aj/` `/aw/` map directly onto Arabic `ـَيْ` `/aj/` and `ـَوْ` `/aw/`. Vowel length from source matres is preserved with the Arabic matres `ا`/`و`/`ي`; RTL verse bodies are emitted in logical order wrapped in RLI…PDI bidi isolates.

### Unicode Reference

| Sign / Letter | Codepoint & Name | Role |
|---|---|---|
| `ـَ` | `U+064E` ARABIC FATHA | short `/a/` |
| `ـِ` | `U+0650` ARABIC KASRA | short `/i/` |
| `ـُ` | `U+064F` ARABIC DAMMA | short `/u/` |
| `ـْ` | `U+0652` ARABIC SUKUN | marks the glide of a diphthong |
| `ـّ` | `U+0651` ARABIC SHADDA | gemination of glides `/jj/` `/ww/` |
| `ا` | `U+0627` ARABIC LETTER ALEF | mater for `/aː/` |
| `آ` | `U+0622` ARABIC LETTER ALEF WITH MADDA ABOVE | word-initial long `/aː/` |
| `ى` | `U+0649` ARABIC LETTER ALEF MAKSURA | final `/aː/` written as dotless yāʾ |
| `و` | `U+0648` ARABIC LETTER WAW | mater for `/uː/` and glide of `/aw/` |
| `ي` | `U+064A` ARABIC LETTER YEH | mater for `/iː/` and glide of `/aj/` |

*Note.* Logical (not presentation-form) order; harakāt are combining marks following their base consonant. The same letters `و`/`ي` serve as both length-matres and diphthong-glides — the disambiguator is the preceding haraka and the presence/absence of sukūn.

---

*Standard Arabic distinguishes exactly TWO phonemic diphthongs, `/aj/` (`ـَيْ`) and `/aw/` (`ـَوْ`), each a fatḥa followed by a sukūn-bearing glide (yāʾ or wāw), from the three LONG VOWELS `/aː iː uː/`, written with the same carrier letters `ا`/`و`/`ي` acting as homorganic matres lectionis after fatḥa/kasra/ḍamma. The single contrast separating the systems is the haraka on the consonant preceding the carrier and whether the carrier bears sukūn. Classical/Quranic Arabic and careful MSA PRESERVE the true diphthongs [aj]/[aw], while most modern dialects MONOPHTHONGIZE them to long [eː]/[oː] — the same Central-Semitic `/aj/`→`/eː/`, `/aw/`→`/oː/` collapse seen in Syriac and Hebrew, with Arabic the most conservative of the three siblings. Vowel length is phonemic at every quality (كَتَبَ vs كَاتَبَ), making the matres structurally load-bearing.*

— Shin

## Consonant–Vowel IPA Matrix

Consonant + vowel (CV) IPA combination matrix for a **representative** set of Modern Standard Arabic consonants paired with the full vowel system: the three short qualities /a i u/ (fatḥa `ـَ`, kasra `ـِ`, ḍamma `ـُ`) and their three long counterparts /aː iː uː/ (long via the *matres lectionis* `ا` `و` `ي`). Each cell gives the **vocalized** Arabic syllable (consonant + haraka, with the long syllables carrying the appropriate mater), an ALA-LC/DIN-style romanization, the phonemic IPA, and a phonetic note. The note flags **emphatic / uvular backing**: after the emphatics `ط` /tˤ/, `ص` /sˤ/, `ض` /dˤ/, `ظ` /ðˤ/ and the uvular `ق` /q/ (and adjacent to the pharyngeals `ح` /ħ/, `ع` /ʕ/ to a lesser degree), the low vowel /a aː/ retracts to [ɑ ɑː], /u uː/ backs/lowers toward [o oː~ʊ], and /i iː/ centralizes toward [ɪ].

This guide is Arabic, a Semitic **sister** of the source (Syriac/Aramaic) and of Hebrew, so the consonant backbone here mirrors the Peshitta and Biblical Hebrew matrices (cf. `peshitta_pronunciation_guide.json` and `biblical_hebrew_pronunciation_guide.json`, key `consonant_vowel_ipa_matrix`); the matrix is a representative selection (not the exhaustive 28 × 6) chosen to demonstrate the plain vs. emphatic vs. pharyngeal vs. interdental contrasts that make Arabic the most faithful match for the source inventory.

- **Reference standard:** MSA — Modern Standard Arabic (الفصحى *al-fuṣḥā*)
- **Secondary reference standard:** Classical / Quranic Arabic (لغة القرآن, *tajwīd* careful-recitation register)
- **Transcription level:** phonemic

### Selection Principle

Representative, not exhaustive (**23 of the 28 consonants**). The set foregrounds every contrast that distinguishes Arabic from its Semitic siblings: plain vs. emphatic (t/tˤ, s/sˤ, d/dˤ, ð/ðˤ), the interdentals (θ ð ðˤ), the pharyngeals (ħ ʕ), the uvular/velar back set (q x ɣ), the glottal stop (ʔ), and the matched pair sˤ/tˤ + q that trigger vowel backing.

The **five** consonants sampled out are `ز` /z/, `ش` /ʃ/, `ف` /f/, `ن` /n/, and `ه` /h/: plain sonorants/labials/dentals that behave like their listed neighbours across vowel contexts (z patterns with s; n with m; f with b/m) are omitted to avoid redundancy, while `ش` /ʃ/ (the only postalveolar sibilant) and `ه` /h/ (the only glottal/laryngeal **fricative**, as opposed to the glottal **stop** /ʔ/ which IS listed) are the two genuine place/manner gaps — they are not exemplified in this curated CV grid but follow the regular plain-consonant pattern (no vowel backing) and are documented in full in `consonants.json`.

> **Note:** `ف` /f/ is also the Peshitta-reader landing site for the source /v/ (v→`ف` merge) — that mapping is discussed in the companion guide even though `ف` has no row here.

### Reference Vowels

The six monophthongs used as columns in the matrix: three short harakāt and their three long counterparts (long via the *matres lectionis* `ا` `و` `ي`). Phonemic IPA keeps /a i u (ː)/; the phonetic notes give the backed allophones triggered by emphasis (*tafkhīm*).

| Vowel | Name | Arabic name | Haraka / Mater | Unicode | IPA | Length | Note |
|---|---|---|---|---|---|---|---|
| a | fatḥa (short a) | فَتْحَة | `ـَ` | `U+064E` | /a/ | short | open/near-open front-central unrounded; backs to [ɑ] in emphatic/uvular environments (*tafkhīm*); may raise toward [æ~ɛ] (*imāla*) in plain front contexts in Classical/dialectal recitation. |
| i | kasra (short i) | كَسْرَة | `ـِ` | `U+0650` | /i/ | short | close/near-close front unrounded; centralizes toward [ɪ] next to emphatics and back consonants. |
| u | ḍamma (short u) | ضَمَّة | `ـُ` | `U+064F` | /u/ | short | close/near-close back rounded; lowers/backs toward [o~ʊ] in emphatic/uvular environments. |
| aː | long ā (fatḥa + alif) | أَلِف الْمَدّ | `ـَا` (mater `ا` alif, `U+0627`) | `U+064E` + `U+0627` | /aː/ | long | long open front-central; retracts to [ɑː] after emphatics/`ق`, the most salient cue of *tafkhīm*. |
| iː | long ī (kasra + yāʾ) | يَاء الْمَدّ | `ـِي` (mater `ي` yāʾ, `U+064A`) | `U+0650` + `U+064A` | /iː/ | long | long close front unrounded; resists backing but lowers slightly to [iˤ~ɪː] under heavy emphasis spread. |
| uː | long ū (ḍamma + wāw) | وَاو الْمَدّ | `ـُو` (mater `و` wāw, `U+0648`) | `U+064F` + `U+0648` | /uː/ | long | long close back rounded; backs/lowers toward [oː] after emphatics and `ق`. |

> **Diphthongs.** Beyond the six monophthongs above, MSA has two diphthongs, /aj/ (fatḥa + sukūn-yāʾ, e.g. بَيْت *bayt* 'house' [bajt]) and /aw/ (fatḥa + sukūn-wāw, e.g. يَوْم *yawm* 'day' [jawm]); these are not enumerated per-consonant in this CV matrix but follow the same backing behavior after emphatics (e.g. طَيْر *ṭayr* [tˤɑjr]).

### Backing Legend (tafkhīm)

The term for the velarization/emphasis is **tafkhīm** (تَفْخِيم 'velarization/emphasis'); the opposite, plain articulation, is **tarqīq** (تَرْقِيق). Phonemic IPA cells keep /a i u/; the phonetic note gives the backed allophone.

**Primary backing triggers:**

| Letter | IPA |
|---|---|
| `ط` | /tˤ/ |
| `ص` | /sˤ/ |
| `ض` | /dˤ/ |
| `ظ` | /ðˤ/ |
| `ق` | /q/ |

**Secondary backing triggers:**

| Letter | IPA |
|---|---|
| `ح` | /ħ/ |
| `ع` | /ʕ/ |
| `خ` | /x/ |
| `غ` | /ɣ/ |
| `ر` | /r/ (in many contexts) |

**Effects on vowel quality:**

| Vowel | Backed allophone |
|---|---|
| a / aː | [ɑ ɑː] (retracted, lowered) |
| u / uː | [o oː] ~ [ʊ] (backed, lowered) |
| i / iː | [ɪ ɪː] (centralized; least affected) |

### CV Matrix

Each cell gives the **vocalized** Arabic syllable, its romanization, and the phonemic IPA; where emphasis/backing applies, the bracketed phonetic allophone [ ] is shown beneath the phonemic value. Columns are the six reference vowels; the **Base** column gives the consonant on its own (letter + IPA + name).

| Consonant | Base | a `ـَ` | i `ـِ` | u `ـُ` | aː `ـَا` | iː `ـِي` | uː `ـُو` |
|---|---|---|---|---|---|---|---|
| `ب` *bāʾ* (بَاء) | /b/ | بَ *ba* /ba/ | بِ *bi* /bi/ | بُ *bu* /bu/ | بَا *bā* /baː/ | بِي *bī* /biː/ | بُو *bū* /buː/ |
| `ت` *tāʾ* (تَاء) | /t/ | تَ *ta* /ta/ | تِ *ti* /ti/ | تُ *tu* /tu/ | تَا *tā* /taː/ | تِي *tī* /tiː/ | تُو *tū* /tuː/ |
| `ط` *ṭāʾ* (طَاء) | /tˤ/ | طَ *ṭa* /tˤa/ [tˤɑ] | طِ *ṭi* /tˤi/ [tˤɪ] | طُ *ṭu* /tˤu/ [tˤo] | طَا *ṭā* /tˤaː/ [tˤɑː] | طِي *ṭī* /tˤiː/ [tˤɪː] | طُو *ṭū* /tˤuː/ [tˤoː] |
| `س` *sīn* (سِين) | /s/ | سَ *sa* /sa/ | سِ *si* /si/ | سُ *su* /su/ | سَا *sā* /saː/ | سِي *sī* /siː/ | سُو *sū* /suː/ |
| `ص` *ṣād* (صَاد) | /sˤ/ | صَ *ṣa* /sˤa/ [sˤɑ] | صِ *ṣi* /sˤi/ [sˤɪ] | صُ *ṣu* /sˤu/ [sˤo] | صَا *ṣā* /sˤaː/ [sˤɑː] | صِي *ṣī* /sˤiː/ [sˤɪː] | صُو *ṣū* /sˤuː/ [sˤoː] |
| `د` *dāl* (دَال) | /d/ | دَ *da* /da/ | دِ *di* /di/ | دُ *du* /du/ | دَا *dā* /daː/ | دِي *dī* /diː/ | دُو *dū* /duː/ |
| `ض` *ḍād* (ضَاد) | /dˤ/ | ضَ *ḍa* /dˤa/ [dˤɑ] | ضِ *ḍi* /dˤi/ [dˤɪ] | ضُ *ḍu* /dˤu/ [dˤo] | ضَا *ḍā* /dˤaː/ [dˤɑː] | ضِي *ḍī* /dˤiː/ [dˤɪː] | ضُو *ḍū* /dˤuː/ [dˤoː] |
| `ث` *thāʾ* (ثَاء) | /θ/ | ثَ *tha* /θa/ | ثِ *thi* /θi/ | ثُ *thu* /θu/ | ثَا *thā* /θaː/ | ثِي *thī* /θiː/ | ثُو *thū* /θuː/ |
| `ذ` *dhāl* (ذَال) | /ð/ | ذَ *dha* /ða/ | ذِ *dhi* /ði/ | ذُ *dhu* /ðu/ | ذَا *dhā* /ðaː/ | ذِي *dhī* /ðiː/ | ذُو *dhū* /ðuː/ |
| `ظ` *ẓāʾ* (ظَاء) | /ðˤ/ | ظَ *ẓa* /ðˤa/ [ðˤɑ] | ظِ *ẓi* /ðˤi/ [ðˤɪ] | ظُ *ẓu* /ðˤu/ [ðˤo] | ظَا *ẓā* /ðˤaː/ [ðˤɑː] | ظِي *ẓī* /ðˤiː/ [ðˤɪː] | ظُو *ẓū* /ðˤuː/ [ðˤoː] |
| `ح` *ḥāʾ* (حَاء) | /ħ/ | حَ *ḥa* /ħa/ [ħä] | حِ *ḥi* /ħi/ | حُ *ḥu* /ħu/ | حَا *ḥā* /ħaː/ [ħäː] | حِي *ḥī* /ħiː/ | حُو *ḥū* /ħuː/ |
| `ع` *ʿayn* (عَيْن) | /ʕ/ | عَ *ʿa* /ʕa/ [ʕä] | عِ *ʿi* /ʕi/ | عُ *ʿu* /ʕu/ | عَا *ʿā* /ʕaː/ [ʕäː] | عِي *ʿī* /ʕiː/ | عُو *ʿū* /ʕuː/ |
| `ق` *qāf* (قَاف) | /q/ | قَ *qa* /qa/ [qɑ] | قِ *qi* /qi/ [qɪ] | قُ *qu* /qu/ [qo] | قَا *qā* /qaː/ [qɑː] | قِي *qī* /qiː/ [qɪː] | قُو *qū* /quː/ [qoː] |
| `ك` *kāf* (كَاف) | /k/ | كَ *ka* /ka/ | كِ *ki* /ki/ | كُ *ku* /ku/ | كَا *kā* /kaː/ | كِي *kī* /kiː/ | كُو *kū* /kuː/ |
| `خ` *khāʾ* (خَاء) | /x/ | خَ *kha* /xa/ [xɑ̈] | خِ *khi* /xi/ | خُ *khu* /xu/ | خَا *khā* /xaː/ [xɑ̈ː] | خِي *khī* /xiː/ | خُو *khū* /xuː/ |
| `غ` *ghayn* (غَيْن) | /ɣ/ | غَ *gha* /ɣa/ [ɣɑ̈] | غِ *ghi* /ɣi/ | غُ *ghu* /ɣu/ | غَا *ghā* /ɣaː/ [ɣɑ̈ː] | غِي *ghī* /ɣiː/ | غُو *ghū* /ɣuː/ |
| `ء` *hamza* (هَمْزَة) | /ʔ/ | أَ *ʾa* /ʔa/ | إِ *ʾi* /ʔi/ | أُ *ʾu* /ʔu/ | آ *ʾā* /ʔaː/ | إِي *ʾī* /ʔiː/ | أُو *ʾū* /ʔuː/ |
| `ج` *jīm* (جِيم) | /dʒ/ | جَ *ja* /dʒa/ [dʒa]~[ɡa]~[ʒa] | جِ *ji* /dʒi/ | جُ *ju* /dʒu/ | جَا *jā* /dʒaː/ | جِي *jī* /dʒiː/ | جُو *jū* /dʒuː/ |
| `ر` *rāʾ* (رَاء) | /r/ | رَ *ra* /ra/ [rˤɑ] | رِ *ri* /ri/ [ri] | رُ *ru* /ru/ [rˤo] | رَا *rā* /raː/ [rˤɑː] | رِي *rī* /riː/ [riː] | رُو *rū* /ruː/ [rˤoː] |
| `ل` *lām* (لاَم) | /l/ | لَ *la* /la/ | لِ *li* /li/ | لُ *lu* /lu/ | لَا *lā* /laː/ | لِي *lī* /liː/ | لُو *lū* /luː/ |
| `م` *mīm* (مِيم) | /m/ | مَ *ma* /ma/ | مِ *mi* /mi/ | مُ *mu* /mu/ | مَا *mā* /maː/ | مِي *mī* /miː/ | مُو *mū* /muː/ |
| `ي` *yāʾ* (يَاء) | /j/ | يَ *ya* /ja/ | يِ *yi* /ji/ | يُ *yu* /ju/ | يَا *yā* /jaː/ | يِي *yī* /jiː/ | يُو *yū* /juː/ |
| `و` *wāw* (وَاو) | /w/ | وَ *wa* /wa/ | وِ *wi* /wi/ | وُ *wu* /wu/ | وَا *wā* /waː/ | وِي *wī* /wiː/ | وُو *wū* /wuː/ |

> For `ج` /dʒ/, the bracketed alternatives are register/regional: [dʒa] (MSA) ~ [ɡa] (Egyptian) ~ [ʒa] (Levantine).

### Phonetic Notes

Class membership and principal allophonic realizations for each consonant onset. These describe how the phonemic CV cells above surface in actual speech, including the backing (*tafkhīm*) and Semitic-source cognate relationships.

| Consonant | Class | Phonetic Note |
|---|---|---|
| `ب` /b/ | plain plosive | Voiced bilabial plosive. Stable across all vowels; no backing. No native /p/ in Arabic — the source /p/ maps here in the Peshitta reader tier (p→`ب`). |
| `ت` /t/ | plain plosive (PLAIN member of the t / tˤ pair) | Voiceless plain (denti-)alveolar plosive. Plain, unaspirated [t]; vowels keep their front/neutral quality. Contrast directly with emphatic `ط` — تِين *tīn* 'fig' [tiːn] vs طِين *ṭīn* 'clay/mud' [tˤɪːn]. |
| `ط` /tˤ/ | emphatic plosive (BACKING TRIGGER) | Voiceless emphatic (pharyngealized) denti-alveolar plosive. Pharyngealized [tˤ] with a raised tongue back; STRONGLY BACKS the following vowel (*tafkhīm*): /a aː/→[ɑ ɑː], /u uː/→[o oː], /i iː/→[ɪ ɪː]. Cognate with source/Hebrew Ṭet (Teth). E.g. طَالِب *ṭālib* 'student' [tˤɑːlib]; طُوبَى *ṭūbā* 'blessed' [tˤoːbaː]. |
| `س` /s/ | plain sibilant (PLAIN member of the s / sˤ pair) | Voiceless plain alveolar sibilant fricative. Plain [s]; vowels stay front/neutral. Contrast with emphatic `ص` — سَيْف *sayf* 'sword' [sajf] vs صَيْف *ṣayf* 'summer' [sˤɑjf]. |
| `ص` /sˤ/ | emphatic sibilant (BACKING TRIGGER) | Voiceless emphatic (pharyngealized) alveolar sibilant fricative. Pharyngealized [sˤ]; STRONGLY BACKS the following vowel: /a aː/→[ɑ ɑː], /u uː/→[o oː], /i iː/→[ɪ ɪː]. Cognate with source/Hebrew Ṣade. E.g. صَابِر *ṣābir* 'patient' [sˤɑːbir]; صُورَة *ṣūra* 'image/form' [sˤoːra]. |
| `د` /d/ | plain plosive (PLAIN member of the d / dˤ pair) | Voiced plain (denti-)alveolar plosive. Plain [d]; non-connecting letter (no left-join). Contrast with emphatic `ض` below. |
| `ض` /dˤ/ | emphatic plosive (BACKING TRIGGER) | Voiced emphatic (pharyngealized) denti-alveolar plosive. Pharyngealized [dˤ]; the iconic 'letter of the Arabs' (لغة الضاد). BACKS the following vowel: /a aː/→[ɑ ɑː], /u uː/→[o oː], /i iː/→[ɪ ɪː]. NOTE for the source: the Syriac/Aramaic source inventory lacks dˤ (and ðˤ) — these are Arabic-only emphatics, so they have no 1:1 source counterpart. E.g. ضَابِط *ḍābiṭ* 'officer' [dˤɑːbitˤ]. |
| `ث` /θ/ | interdental (plain) | Voiceless interdental fricative. Interdental [θ] (as English 'th' in 'thin'); one of the contrasts that makes Arabic faithful to the source (urban Levantine collapses θ→[t], which is why Levantine is documented-only). Cognate with source/Hebrew Taw-spirant. E.g. ثَوْب *thawb* 'garment' [θawb]. |
| `ذ` /ð/ | interdental (plain) | Voiced interdental fricative. Interdental [ð] (as English 'th' in 'this'); non-connecting letter. Cognate with source/Hebrew Dalet-spirant (ð). E.g. ذَهَب *dhahab* 'gold' [ðahab]. |
| `ظ` /ðˤ/ | emphatic interdental (BACKING TRIGGER) | Voiced emphatic (pharyngealized) interdental fricative. Pharyngealized interdental [ðˤ] (NOT [zˤ] in careful MSA/Classical; many dialects merge it with `ض`). BACKS the following vowel like the other emphatics. Arabic-only emphatic with no source/Aramaic counterpart. E.g. ظَالِم *ẓālim* 'unjust' [ðˤɑːlim]; ظُهْر *ẓuhr* 'noon' [ðˤohr]. |
| `ح` /ħ/ | pharyngeal | Voiceless pharyngeal fricative. Voiceless pharyngeal [ħ], not glottal [h]; a true Semitic pharyngeal cognate with source/Hebrew Ḥet. Does NOT pharyngealize like the emphatics, but its pharyngeal constriction LOWERS/retracts adjacent /a/ toward [ɑ̈~ä] and colors neighboring vowels. E.g. حَبِيب *ḥabīb* 'beloved' [ħabiːb]; حُبّ *ḥubb* 'love' [ħubː]. |
| `ع` /ʕ/ | pharyngeal | Voiced pharyngeal fricative/approximant. Voiced pharyngeal [ʕ] (often a pharyngealized approximant/stricture); the hallmark Semitic sound, cognate with source/Hebrew ʿAyin. Retracts and lowers adjacent /a/ toward [ɑ̈~ä]; not a full emphatic-style trigger but audibly colors the vowel. E.g. عَالَم *ʿālam* 'world' [ʕäːlam]; عِيد *ʿīd* 'feast' [ʕiːd]. |
| `ق` /q/ | uvular (BACKING TRIGGER; often grouped with the emphatics) | Voiceless uvular plosive. Uvular [q] (further back than velar [k]); grouped with the emphatics for backing — STRONGLY retracts /a aː/→[ɑ ɑː] and backs /u uː/→[o oː]. Cognate with source/Hebrew Qof. Urban Levantine collapses q→[ʔ], which is why it is documented-only. E.g. قَلْب *qalb* 'heart' [qɑlb]; قُرْآن *qurʾān* 'Quran' [qorʔaːn]. |
| `ك` /k/ | plain velar (PLAIN counterpart to uvular `ق`) | Voiceless velar plosive. Plain velar [k]; fronts slightly before front vowels but does NOT back the vowel. Contrast with uvular `ق` — كَلْب *kalb* 'dog' [kalb] vs قَلْب *qalb* 'heart' [qɑlb]. |
| `خ` /x/ | back fricative (secondary backing trigger) | Voiceless velar/uvular fricative. Voiceless velar~uvular [x] (Scottish 'loch'); a back consonant that lightly retracts adjacent /a/. Cognate with source/Hebrew Kaf-spirant (x). E.g. خَيْر *khayr* 'good' [xajr]; خُبْز *khubz* 'bread' [xubz]. |
| `غ` /ɣ/ | back fricative (secondary backing trigger) | Voiced velar/uvular fricative. Voiced velar~uvular [ɣ] (a 'gargled' r-like fricative); cognate with source/Hebrew Gimel-spirant (ɣ). Lightly retracts adjacent /a/. E.g. غَيْم *ghaym* 'cloud' [ɣajm]; غُرْفَة *ghurfa* 'room' [ɣurfa]. |
| `ء` /ʔ/ | glottal | Voiceless glottal stop. Glottal stop [ʔ]; seat varies (`أ` `إ` `ؤ` `ئ` or standalone `ء`). Cognate with source/Hebrew ʾAlef/ʾAlaph. No backing effect. E.g. أَب *ʾab* 'father' [ʔab]; إِيمَان *ʾīmān* 'faith' [ʔiːmaːn]. |
| `ج` /dʒ/ | affricate (realization varies) | Voiced postalveolar affricate (MSA). MSA realization [dʒ]; Egyptian/some Classical [ɡ]; Levantine [ʒ]. In the Peshitta reader tier the source /ɡ/ maps to `ج` (ɡ→`ج`). No vowel backing. E.g. جَمَل *jamal* 'camel' [dʒamal]. |
| `ر` /r/ | rhotic (variable emphasis) | Voiced alveolar trill/tap. Trilled/tapped [r~ɾ]; non-connecting letter. In *tajwīd* and MSA, /r/ is EMPHATIC (velarized [rˤ], backing the vowel) next to /a aː u uː/ and plain next to /i iː/ — so رَ is [rˤɑ] but رِ is [ri]. E.g. رَبّ *rabb* 'lord' [rˤɑbː]; رِيح *rīḥ* 'wind' [riːħ]. |
| `ل` /l/ | lateral (clear; emphatic only in الله) | Voiced alveolar lateral approximant. Clear [l] in nearly all contexts; backs to dark/velarized [ɫ] only in the name اللّٰه *Allāh* (after /a u/, giving [ɑɫˤɑːh]). Forms the definite article `ال`, which assimilates to following SUN LETTERS. E.g. لَيْل *layl* 'night' [lajl]. |
| `م` /m/ | nasal (plain) | Voiced bilabial nasal. Stable [m] across all vowels; no backing. E.g. مَاء *māʾ* 'water' [maːʔ]; مِيم *mīm* (letter name) [miːm]. |
| `ي` /j/ | glide / mater lectionis | Voiced palatal approximant (glide). Glide [j] as a consonant; the same letter `ي` serves as the mater for long /iː/ and in the diphthong /aj/. No backing. E.g. يَد *yad* 'hand' [jad]; يَوْم *yawm* 'day' [jawm]. |
| `و` /w/ | glide / mater lectionis | Voiced labial-velar approximant (glide). Glide [w] as a consonant; non-connecting letter. The same letter `و` serves as the mater for long /uː/ and in the diphthong /aw/. No backing. E.g. وَرْد *ward* 'roses' [ward]; وُجُود *wujūd* 'existence' [wudʒuːd]. |

### Accent Notes

**MSA vs. Classical.** The phonemic CV values above are identical in Modern Standard Arabic (الفصحى) and Classical/Quranic Arabic — both preserve the full plain/emphatic/pharyngeal/interdental contrast set. Classical *tajwīd* recitation realizes the SAME phonemes with finer, codified detail: stronger, more consistent *tafkhīm* on the emphatics and `ق`; careful interdental `ظ` as [ðˤ] (never [zˤ]); precise vowel length (*madd*); and *idghām*/assimilation rules. MSA permits a touch more variation (e.g. `ج` as [dʒ] vs regional [ɡ]/[ʒ]; occasional weakening of ðˤ→[zˤ]) but the contrasts themselves are intact in both registers — which is exactly why MSA + Classical are the shipped standards and dialects are documented-only.

**Emphasis spread.** Emphasis (*tafkhīm*) is not confined to the CV cell: pharyngealization SPREADS bidirectionally from an emphatic (`ط` `ص` `ض` `ظ`, and `ق`) across adjacent vowels and often the whole syllable/word, backing every vowel in its domain and frequently velarizing intervening sonorants (l, r, m, n). The per-cell phonetic notes show only the immediately following vowel; in running text the backing colors a wider span (e.g. مَطَار *maṭār* 'airport' → [mɑtˤɑːr], the first /a/ also backed). The plain (*tarqīq*) consonants block/limit spread, which is why the plain-vs-emphatic minimal pairs (تين/طين, سيف/صيف, كلب/قلب) are audibly distinct on the VOWEL as much as the consonant.

**Jīm realization.** `ج` (*jīm*) is the one consonant in this set with major register/regional variation in its base realization: [dʒ] is the MSA/Levantine-broadcast and pan-Arab norm and the value used in the matrix; [ɡ] is standard in Egyptian Arabic and is also a well-attested Classical/old value (hence the source /ɡ/ → `ج` mapping in the Peshitta reader tier); [ʒ] is typical of urban Levantine and North African speech. None of these variants back the following vowel.

**Pharyngeal coloring.** `ح` /ħ/ and `ع` /ʕ/ are pharyngeals, not emphatics: they do not pharyngealize the consonant string but their pharyngeal stricture lowers and centralizes an adjacent low vowel (/a aː/ → [ä~ɑ̈]) and gives neighboring high vowels a slightly retracted, 'pressed' quality. This coloring is gentler and more local than full emphatic spread and is shared with the Semitic source (Syriac Ḥeth/ʿE, Hebrew Ḥet/ʿAyin), reinforcing Arabic's status as the most faithful sibling match.

**Imāla and pausal forms.** Two further allophonic effects, documented elsewhere in the guide, interact with this matrix: (1) *imāla* — in some Classical/dialectal contexts a plain /aː/ raises toward [eː~iː] in front (non-emphatic) environments, the mirror image of emphatic backing; (2) pausal form (*waqf*) — utterance-finally, short final vowels and *tanwīn* are dropped, so a final CV cell like بَ may surface bare as [b] phrase-finally. Neither alters the citation CV values tabulated here.

### Cross-References

| Resource | Location |
|---|---|
| English template (structural model) | `English/english_pronunciation_guide.json` › `consonant_vowel_ipa_matrix` |
| Peshitta sibling (Semitic source) | `peshitta_pronunciation_guide.json` › `consonant_vowel_ipa_matrix` — shares ʔ b d h w z ħ tˤ j k l m n s ʕ q r š θ ð ɣ x; source lacks Arabic dˤ ðˤ and has v p ɡ that Arabic lacks |
| Hebrew sibling | `biblical_hebrew_pronunciation_guide.json` › `consonant_vowel_ipa_matrix` — same pharyngeals ħ ʕ, emphatic tˤ, interdentals ð θ, uvular/back q x ɣ |
| Companion guide | `Arabic/arabic_pronunciation_guide.md` |
| Reader tier (vocalized) | `Arabic/Peshita_Arabic/Vocalized/` |
| Reader tier (unvocalized) | `Arabic/Peshita_Arabic/Unvocalized/` |

---

*Section compiled by Shin.*

## Suprasegmentals

Prosodic and suprasegmental features of Arabic pronunciation, documented in parallel for two reference standards: MSA (Modern Standard Arabic, العربية الفصحى *al-fuṣḥā*) and Classical/Quranic Arabic (لُغَة القُرْآن, the careful *tajwīd* recitation register). In contrast to the source's English template — where lexical stress is phonemic — Arabic stress is RULE-BASED and PREDICTABLE (weight-sensitive, non-contrastive). What IS phonemic in Arabic is CONSONANT LENGTH (gemination, *shadda*) and VOWEL LENGTH (short /a i u/ vs long /aː iː uː/). Arabic has NO lexical tone. Additional suprasegmental domains include emphasis spread (*tafkhīm*) projecting from the emphatic/pharyngealized consonants, the morpho-prosody of *tanwīn* (nunation) and *iʿrāb* (case/mood desinences), pausal (*waqf*) reduction, and sentence-level intonation. As a Semitic sister of the source language (Syriac/Aramaic) and of Hebrew, Arabic shares the templatic root-and-pattern backbone in which gemination and vowel length carry grammatical, not merely lexical, weight.

### Tone

Arabic is NOT a tone language: pitch is never used lexically or grammatically to distinguish word meaning. There are no lexical tones and no register/contour-tone contrasts. Pitch operates only at the phrase/utterance level as INTONATION (see the [Intonation](#intonation) field below). This matches the source language (Syriac/Aramaic) and Hebrew, all of which are atonal Semitic languages.

| Property | Value |
|---|---|
| Status | Absent (no lexical or grammatical tone) |
| Contrast with template | The English template likewise has no lexical tone; English is a stress-accent language. Arabic differs in that even STRESS is non-contrastive — the load borne by stress in English is borne in Arabic by phonemic gemination and phonemic vowel length. |

### Stress

Arabic word stress (النَّبْر *an-nabr*) is RULE-BASED, PREDICTABLE, and WEIGHT-SENSITIVE — it is NOT phonemic. Unlike the English template, where stress placement alone distinguishes words (*record*-noun vs *record*-verb), Arabic has essentially NO minimal pairs distinguished by stress; once syllable structure and vowel/consonant length are fixed, stress position follows automatically from the syllable-weight rules. Stress is realized mainly by greater duration and slightly higher pitch and intensity on the stressed syllable; crucially, Arabic does NOT reduce unstressed vowels to schwa (vowel quality is preserved regardless of stress — the opposite of English).

- **IPA notation:** `ˈ` placed immediately before the stressed syllable (primary); `ˌ` for secondary stress in long words.
- **Phonemic status:** NON-phonemic (predictable). Stress is fully determined by syllable weight and position; it is not lexically contrastive.

#### Syllable Weight

Stress assignment depends on syllable WEIGHT. Arabic syllables are classified as light, heavy, or superheavy.

| Weight | Shape | Definition | Example(s) |
|---|---|---|---|
| Light | CV | A short vowel with no coda: a single consonant + short vowel. | كَ /ka/, the first syllable of كَتَبَ /ˈka.ta.ba/ |
| Heavy | CVː or CVC | Either a long vowel (CVː) or a short vowel closed by one consonant (CVC). Both count as heavy for stress. | كِتاب /ki.ˈtaːb/ — penult كِ light, final تاب CVːC superheavy/heavy attracts stress; مَكْتَب /ˈmak.tab/ — مَكْ is CVC (heavy), takes stress |
| Superheavy | CVːC, CVCC | A long vowel + coda, or a short vowel + two-consonant coda. Occurs chiefly word-finally; a final superheavy syllable attracts stress. | كِتاب /ki.ˈtaːb/ (CVːC final); مُهِمّ /mu.ˈhimm/ (CVCC final, geminate coda) |

#### Rules

A widely used formulation of the MSA stress rule (variations exist across descriptions and regional reading norms, but the core is shared):

| # | Ordered rule |
|---|---|
| 1 | If the FINAL syllable is SUPERHEAVY (CVːC or CVCC), it takes the stress. e.g., كِتاب /ki.ˈtaːb/ 'book'; مُهِمّ /mu.ˈhimm/ 'important'. |
| 2 | Otherwise, if the PENULTIMATE (second-to-last) syllable is HEAVY (CVː or CVC), it takes the stress. e.g., مُعَلِّم /mu.ˈʕal.lim/ 'teacher' (penult عَلْ heavy, closed by the first half of the geminate لّ → penult stress); مُهَنْدِس /mu.ˈhan.dis/ 'engineer' (penult هَنْ = CVC heavy → penult stress). |
| 3 | Otherwise, stress falls on the ANTEPENULTIMATE (third-from-last) syllable, or on the first syllable of the word if it is shorter than three syllables. e.g., كَتَبَ /ˈka.ta.ba/ 'he wrote' (all light → antepenult); مَكْتَبة /ˈmak.ta.ba/ 'library' (penult تَ light → fall through to antepenult مَكْ); مَدْرَسة /ˈmad.ra.sa/ 'school' (penult رَ light → antepenult مَدْ). |
| 4 | Stress never falls further back than the antepenult. |

**Note:** Reading-tradition details differ (e.g., whether a final CVC counts as stressable, treatment of word-final long vowels, and Egyptian vs Levantine vs Classical reading norms). The shipped MSA standard follows the mainstream weight-sensitive rule above; the Classical/*tajwīd* register agrees on word stress but adds finer recitation prosody (*madd* lengthening, see below).

#### Worked Examples

| Word | Gloss | Syllabification | Stress | Rule |
|---|---|---|---|---|
| كَتَبَ | he wrote | ka.ta.ba (CV.CV.CV — all light) | /ˈka.ta.ba/ | No superheavy final, no heavy penult → antepenult. |
| كِتاب | book | ki.taːb (CV.CVːC) | /ki.ˈtaːb/ | Final syllable superheavy (CVːC) → final stress. |
| مَكْتَبة | library | mak.ta.ba (CVC.CV.CV) | /ˈmak.ta.ba/ | No superheavy final, penult تَ light → antepenult مَكْ (which is heavy). |
| مُعَلِّم | teacher | mu.ʕal.lim (CV.CVC.CVC — note geminate لّ) | /mu.ˈʕal.lim/ | Final لِم heavy but not superheavy; penult عَلْ heavy → penult stress. |
| مُسْتَشْفى | hospital | mus.taʃ.faː (CVC.CVC.CVː) | /mus.ˈtaʃ.faː/ | Final faː heavy (CVː) but penult تَشْ heavy → penult stress (per common MSA reading). |
| العَرَبِيّة | Arabic (the language) | al.ʕa.ra.bij.ja (with geminate يّ) | /al.ʕa.ra.ˈbij.ja/ | Penult بِيْ heavy (closed by first half of geminate) → penult stress. |

#### Clitics and Particles

Proclitics and enclitics attach to the host word and the whole unit is restressed as one prosodic word. The definite article الـ *al-* and conjunction وَ *wa-* are proclitic and unstressed; pronominal suffixes (ـهُ *-hu*, ـكَ *-ka*, ـنا *-nā*) and the like restress the host.

- **Example:** كِتاب /ki.ˈtaːb/ 'book' → كِتابُهُ /ki.ˈtaː.bu.hu/ 'his book' (stress stays on the now-penult long syllable per the weight rules).

**Contrast with template:** Where the English template devotes most of its stress section to PHONEMIC contrasts (noun/verb pairs, compound vs phrasal stress), Arabic has no such contrasts: there is no Arabic analog of *'ˈrecord* vs *reˈcord'*. The Arabic stress section instead documents the deterministic weight-based algorithm. The functional load English assigns to stress is carried in Arabic by gemination and vowel length (below).

### Gemination

Consonant length (gemination, التَّشْديد *at-tashdīd*) is PHONEMIC in Arabic and is the single most important suprasegmental contrast — it is marked orthographically by the SHADDA ـّ (`U+0651`) written over the doubled consonant. A geminate is a single consonant held roughly twice as long; phonologically it closes the preceding syllable (as coda) and opens the following one (as onset). Gemination is contrastive: it distinguishes otherwise identical words, and it is the morphological engine of the root-and-pattern system (Form II verbs double the middle radical to derive causatives/intensives).

- **IPA notation:** `ː` after the consonant (e.g., درّس /darrasa/ → [darːasa]), or by writing the consonant twice (/darrasa/ ~ /darːasa/). Both notations appear; this guide uses the doubled-letter convention /CC/ with [Cː] as the phonetic realization.
- **Orthography:** Shadda ـّ (`U+0651`) sits above the geminated consonant; it may combine with a harakat (e.g., ـَّ shadda+fatḥa, ـِّ shadda+kasra, ـُّ shadda+ḍamma). In fully vocalized text the shadda is obligatory for geminates; in unvocalized text it is normally omitted and inferred.

#### Phonemic Contrast (Single vs Geminate Minimal Pairs)

Single vs geminate consonants form true minimal pairs, frequently with a derivational meaning difference (Form I vs Form II).

| Single | Single IPA | Single gloss | Geminate | Geminate IPA | Geminate gloss | Note |
|---|---|---|---|---|---|---|
| دَرَسَ | /ˈda.ra.sa/ | he studied (Form I) | دَرَّسَ | /ˈdar.ra.sa/ | he taught / made (someone) study (Form II, causative) | The signature minimal pair: gemination of the middle radical /r/ derives the causative. |
| كَسَرَ | /ˈka.sa.ra/ | he broke | كَسَّرَ | /ˈkas.sa.ra/ | he smashed to pieces (intensive) | — |
| عَلِمَ | /ˈʕa.li.ma/ | he knew | عَلَّمَ | /ˈʕal.la.ma/ | he taught (causative) | — |
| سَكَنَ | /ˈsa.ka.na/ | he dwelt / became still (Form I) | سَكَّنَ | /ˈsak.ka.na/ | he calmed / put (a consonant) into sukūn (Form II, causative) | — |
| حَجَ | /ˈħa.dʒa/ | (illustrative) | حَجّ | /ħadʒdʒ/ | pilgrimage (Hajj); final geminate jīm | — |

**Note:** Gemination is doubly significant in a templatic Semitic language: beyond lexical contrast it is a productive morphological operation (Form II/V verbs, the D-stem) cognate with the source's and Hebrew's *piʿel*/*paʿʿel* intensive.

#### Phonological Effect

A geminate /CːC.../ is heterosyllabic: the first mora closes the preceding syllable, making it HEAVY, which feeds the stress rules (e.g., مُعَلِّم /mu.ˈʕal.lim/ is penult-stressed precisely because عَلْ is closed by the first half of the geminate لّ).

**All consonants geminable:** Unlike Hebrew (where gutturals and *resh* resist gemination) and Western Syriac (where historical gemination was largely lost), Arabic permits gemination of ALL 28 consonants, including the gutturals/pharyngeals ح ع ه ء and ر, and it is fully phonemic across MSA and Classical alike.

#### Tradition Difference

| Register | Realization |
|---|---|
| MSA | Gemination is robust and phonemic; shadda is pronounced as a held/doubled consonant in all careful speech. |
| Classical (*tajwīd*) | Gemination is meticulously realized; *tajwīd* treats the مُشَدَّد (geminated letter) with full length and, for nasals/specific contexts, with *ghunna* (nasalization) held for the prescribed duration (see *idghām* below). |
| Source contrast | Cross-reference: in the source's Eastern Syriac tradition gemination is preserved and phonemic (parallel to Arabic), whereas Western Syriac simplified it — Arabic patterns with the conservative Eastern system and with Biblical Hebrew's *dagesh forte*. |

### Vowel Length

Vowel length is PHONEMIC in Arabic: each of the three vowel qualities exists short and long — /a i u/ vs /aː iː uː/ — and length alone distinguishes words. Short vowels are written with HARAKAT (fatḥa ـَ /a/, kasra ـِ /i/, ḍamma ـُ /u/); long vowels are written with the MATRES LECTIONIS ا (alif, for /aː/), ي (yāʾ, for /iː/), و (wāw, for /uː/), typically carried by the preceding harakat. This is a core contrast inherited from Proto-Semitic and shared with the source and Hebrew.

- **IPA notation:** `ː` after the vowel marks length (/aː/, /iː/, /uː/). Short vowels carry no length mark.

#### Short Vowels

| Vowel | Harakat | Notes |
|---|---|---|
| /a/ | fatḥa ـَ | backed to [ɑ] near emphatics/pharyngeals; raised toward [e]/[æ] by *imāla* in some Classical/dialectal contexts |
| /i/ | kasra ـِ | — |
| /u/ | ḍamma ـُ | — |

#### Long Vowels

| Vowel | Mater lectionis | Notes |
|---|---|---|
| /aː/ | alif ا | preceded by fatḥa; [ɑː] near emphatics |
| /iː/ | yāʾ ي | preceded by kasra |
| /uː/ | wāw و | preceded by ḍamma |

#### Phonemic Contrast (Short vs Long Minimal Pairs)

Minimal pairs distinguished solely by vowel length. As with gemination, the contrast is often morphologically loaded (e.g., active participle CāCiC has long /aː/).

| Short | Short IPA | Short gloss | Long | Long IPA | Long gloss |
|---|---|---|---|---|---|
| كَتَبَ | /ˈka.ta.ba/ | he wrote (perfect verb) | كاتَبَ | /ˈkaː.ta.ba/ | he corresponded with (Form III, long /aː/) |
| كَتَب (kataba) | /ˈka.ta.ba/ | he wrote | كاتِب | /ˈkaː.tib/ | writer / writing (active participle, CāCiC) |
| عَلِمَ | /ˈʕa.li.ma/ | he knew | عالِم | /ˈʕaː.lim/ | scholar / knowing (active participle) |
| جَمَل | /ˈdʒa.mal/ | camel | جَمال | /dʒa.ˈmaːl/ | beauty |
| سَلَم | /ˈsa.lam/ | peace / safety (also advance-payment sale, fiqh term) | سَلام | /sa.ˈlaːm/ | peace / greeting (long /aː/ in the second syllable) |

**Length and syllable:** Long vowels project a heavy (CVː) or superheavy (CVːC) syllable and therefore interact directly with stress: a final CVːC attracts stress (كِتاب /ki.ˈtaːb/), and a heavy penult CVː blocks antepenultimate stress.

**Shortening:** Long vowels SHORTEN in certain closed-syllable and connected-speech contexts (vowel shortening in superheavy environments and before clusters), and word-final long vowels may be shortened in pause; this is a regular allophonic process and does not neutralize the underlying contrast in citation forms. *Example:* Final long vowels in some forms shorten utterance-medially before a following consonant cluster; cf. pausal behavior below.

#### Tradition Difference

| Register | Realization |
|---|---|
| MSA | Three-quality, two-length system as above; diphthongs /aj/ (ـَيْ) and /aw/ (ـَوْ) are commonly monophthongized to [eː]/[oː] in many speakers/dialects but kept as diphthongs in careful MSA and Classical. |
| Classical (*tajwīd*) | Length is governed by the precise MADD system (see *madd* field): obligatory short vowels vs natural long (*madd ṭabīʿī*, 2 counts) vs derived/lengthened *madd* (4–6 counts). Quranic recitation quantizes vowel length to counted morae far more strictly than MSA prose. |
| Source contrast | The source (Syriac/Aramaic) and Hebrew also have phonemic vowel length; the Arabic Peshitta reader tier maps the source's /e/→kasra/ī and /o/→ḍamma/ū (vowel collapse to the three Arabic qualities) while PRESERVING length via the matres lectionis — see [Cross-Reference](#cross-reference). |

### Emphasis Spread

EMPHASIS (التَّفْخيم *at-tafkhīm*, 'velarization/pharyngealization') is a SUPRASEGMENTAL DOMAIN, not just a property of a single segment: the emphatic/pharyngealized consonants project a backing colour onto neighbouring segments within a prosodic span. This is one of the most characteristic Arabic suprasegmentals and a key reason Arabic faithfully matches the emphatic series of the source language.

- **IPA notation:** `ˤ` (superscript pharyngealization) on the emphatic consonant; the spread is shown by backing the affected vowels: /a/ → [ɑ], /i/ → [ɪ], /u/ → [ʊ], and a generally darker, retracted-tongue-root quality on intervening consonants.

#### Trigger Consonants

**Primary emphatics:**

| Letter | IPA | Name |
|---|---|---|
| ص | /sˤ/ | ṣād |
| ض | /dˤ/ | ḍād |
| ط | /tˤ/ | ṭāʾ |
| ظ | /ðˤ/ | ẓāʾ |

**Often grouped:**

- ق /q/ (qāf — uvular, induces backing)
- Some traditions also list خ /x/ and غ /ɣ/, and the pharyngeals ح /ħ/, ع /ʕ/, plus emphatic allophones of ر /rˤ/ and ل /lˤ/ (as in اللَّه /alˤˈlˤɑːh/) and م/ب in specific words.
- Cross-note: the source language has tˤ and sˤ but NOT dˤ or ðˤ; Arabic's fuller emphatic series (all four) makes it a richer host for the contrast.

#### Domain

Emphasis typically spreads bidirectionally from the trigger across the syllable and often the whole prosodic word, though leftward (regressive) and rightward (progressive) reach can differ and certain segments (notably high front /i(ː)/, /j/, /ʃ/) can BLOCK or attenuate the spread.

- **Scope:** Minimally the adjacent vowels; commonly the entire syllable; frequently the whole phonological word in careful pronunciation.

#### Examples

| Word | Gloss | IPA / with spread | Note |
|---|---|---|---|
| طالِب | student | /ˈtˤɑː.lɪb/ — the emphatic ط backs the following /aː/ → [ɑː] and colours the word | cf. plain /t/ in تالِب would have clear [aː] |
| صَيْف | summer | /sˤɑjf/ → [sˤɑjf] | ṣād backs the diphthong nucleus |
| ضَرَبَ | he hit | /ˈdˤɑ.rɑ.bɑ/ | ḍād spreads emphasis across the verb |
| اللَّه | God (Allāh) | /alˤˈlˤɑːh/ | The lām is emphatic (velarized [lˤ]) when preceded by fatḥa/ḍamma, backing the /aː/ → [ɑː]; after kasra (e.g., بِسْمِ اللَّه) the lām is plain [l]. |

**Minimal contrast:** سَيْف /sajf/ [sajf] 'sword' vs صَيْف /sˤɑjf/ [sˤɑjf] 'summer' — the plain/emphatic contrast on the consonant carries through to the vowel colour, a small minimal demonstration that emphasis is a domain feature.

#### Tradition Difference

| Register | Realization |
|---|---|
| MSA | Emphasis spread is consistently present; degree of spread and blocking varies by speaker and dialect substrate. |
| Classical (*tajwīd*) | *Tafkhīm* (heavy/emphatic articulation) vs *tarqīq* (light/clear articulation) is a formally codified *tajwīd* topic — e.g., the rules for heavy vs light ر (rāʾ) and for the lām of *lafẓ al-jalāla* اللَّه — with prescribed conditioning by the surrounding vowels. |
| Source contrast | The source's pharyngealization note (its tˤ/sˤ backing adjacent vowels /a/→[ɑ], /i/→[ɪ], /u/→[ʊ]) is the direct parallel; Arabic extends the same mechanism over a larger emphatic inventory and a wider spreading domain. |

### Tanwīn and Iʿrāb Prosody

Arabic morpho-prosody adds two phenomena absent from the English template: TANWĪN (nunation) and IʿRĀB (desinential case/mood inflection). Both attach short-vowel + (for *tanwīn*) /n/ material to word endings and shape the prosodic shape of citation forms. Because the SOURCE IPA is caseless, the *iʿrāb* desinences are documented here DESCRIPTIVELY but are NOT emitted in the Peshitta reader tier (see note).

#### Tanwīn (Nunation)

TANWĪN (التَّنْوين, nunation) is an indefinite-marking final /n/ realized as a doubled harakat: fatḥatān ـً /-an/, kasratān ـٍ /-in/, ḍammatān ـٌ /-un/. It is a suffixal /Vn/ that appears on indefinite nouns/adjectives in full (non-pausal) pronunciation.

- **IPA notation:** /-an/, /-in/, /-un/ written after the stem; fatḥatān is carried on an alif ـًا except after tāʾ marbūṭa / hamza.

| Form | IPA | Gloss |
|---|---|---|
| كِتابٌ | /ki.ˈtaː.bun/ | 'a book' (nominative indefinite) |
| كِتاباً | /ki.ˈtaː.ban/ | 'a book' (accusative indefinite) |
| كِتابٍ | /ki.ˈtaː.bin/ | 'a book' (genitive indefinite) |
| شُكْراً | /ˈʃuk.ran/ | 'thanks' (frozen adverbial accusative — survives even in casual speech) |

#### Iʿrāb (Case/Mood)

IʿRĀB (الإعْراب) is the system of CASE (on nouns: nominative -u مرفوع, accusative -a منصوب, genitive -i مجرور) and MOOD (on verbs: indicative -u, subjunctive -a, jussive ∅/sukūn) marked by final short vowels. These desinences are prosodically light (short vowels) and are the first material lost in pause.

- **IPA notation:** Final /-u/, /-a/, /-i/ (definite) or /-un/, /-an/, /-in/ (indefinite, with *tanwīn*).

| Form | IPA | Gloss |
|---|---|---|
| الكِتابُ | /al.ki.ˈtaː.bu/ | 'the book' (NOM) |
| الكِتابَ | /al.ki.ˈtaː.ba/ | 'the book' (ACC) |
| الكِتابِ | /al.ki.ˈtaː.bi/ | 'the book' (GEN) |
| يَكْتُبُ | /ˈjak.tu.bu/ | 'he writes' (indicative) |
| يَكْتُبَ | /ˈjak.tu.ba/ | 'he writes' (subjunctive) |
| يَكْتُبْ | /ˈjak.tub/ | 'he writes' (jussive) |

**Prosodic note:** *Iʿrāb* and *tanwīn* vowels are NEVER stressed (stress never reaches a final light desinence) and are realized only in careful/formal full forms (وَصْل, connected reading). In ordinary speech and at utterance end they are dropped (pausal forms, below).

**Emission policy:** Because the source (Syriac/Aramaic) IPA used to build the Peshitta reader is CASELESS, the *iʿrāb* desinential vowels and *tanwīn* /n/ are treated as descriptive metadata here and are NOT generated into the source-aligned reader output — i.e., the reader uses pausal/caseless forms. This keeps the Arabic Peshitta near-reversible against the caseless source.

### Pausal Forms

PAUSAL forms (الوَقْف *al-waqf*) are the reduced shapes words take utterance-finally (or before a major break). In pause, final short-vowel desinences (*iʿrāb*) and most *tanwīn* are DROPPED; the prosodic word is re-shaped. This is the default register for the caseless Peshitta reader and matches everyday speech.

- **IPA notation:** Final short vowel/*tanwīn* removed; the resulting word may end in a consonant (new closed final syllable).

#### Rules

| # | Pausal rule |
|---|---|
| 1 | Final /-u/, /-i/ (and their *tanwīn* /-un/, /-in/) are dropped: كِتابٌ /ki.ˈtaː.bun/ → pausal كِتابْ /ki.ˈtaːb/. |
| 2 | Final *tanwīn* fatḥa /-an/ becomes a long /aː/ (the alif is realized): كِتاباً /ki.ˈtaː.ban/ → pausal كِتابا /ki.ˈtaː.baː/. |
| 3 | Tāʾ marbūṭa ة is realized as /h/ (or silent) in pause rather than /t/: مَدْرَسةٌ /mad.ra.sa.tun/ → pausal مَدْرَسة /ˈmad.ra.sah/ ~ /ˈmad.ra.sa/. |
| 4 | Pausal loss can shift the stressable window because the final syllable changes weight. |

#### Tradition Difference

| Register | Realization |
|---|---|
| MSA | Pausal dropping of *iʿrāb* is the norm in speech and even in much read-aloud prose; full desinences are reserved for formal recitation and grammatical citation. |
| Classical (*tajwīd*) | *Waqf* is a heavily codified topic in *tajwīd* (types of pause — وقف لازم, جائز, etc., and the sukūn/*madd* applied on the final letter); reciters apply specific pausal rules at marked stopping points. |
| Reader-tier note | The Arabic Peshitta reader emits pausal/caseless forms by default, aligning with the source IPA. |

### Madd Lengthening

MADD (المَدّ, 'prolongation') is the Classical/Quranic system of QUANTIZED vowel lengthening that goes beyond the basic short/long contrast of MSA prose. It is a *tajwīd*-specific suprasegmental: vowel length is measured in counts (حَرَكات *ḥarakāt*, beats), and specific orthographic/phonetic environments mandate 2-, 4-, or 6-count vowels. This field is primarily Classical/Quranic; MSA prose uses only the binary short vs long distinction.

- **IPA notation:** Longer holds may be shown with multiple length marks or a numeric count, e.g., /aː/ (2 counts) vs /aːː/ ~ /aː(4–6)/ for derived *madd*. This guide notes the count rather than inventing fine IPA length tiers.

#### Types

| Name | Length | Description | Example |
|---|---|---|---|
| المَدّ الطَّبيعي (*madd ṭabīʿī*, natural madd) | 2 counts | The basic natural long vowel /aː iː uː/ with no following hamza or sukūn. This is the same length as an MSA long vowel. | قالَ /ˈqɑː.la/ 'he said' — natural 2-count /aː/. |
| المَدّ المُتَّصِل (*madd muttaṣil*, connected/obligatory madd) | 4–5 counts | A long vowel followed by a hamza ء WITHIN the same word — obligatorily lengthened. | جاءَ /dʒaː(ː)ʔa/ 'he came' — /aː/ before ء held 4–5 counts. |
| المَدّ المُنْفَصِل (*madd munfaṣil*, separated madd) | 2, 4, or 5 counts (by *riwāya*) | A word-final long vowel followed by a hamza beginning the NEXT word; length varies by recitation transmission. | بِما أُنْزِلَ /bi.maː ʔun.zila/ — /aː/ at the word boundary before أُ. |
| المَدّ اللازِم (*madd lāzim*, necessary madd) | 6 counts | A long vowel followed by an original sukūn or by a geminate (shadda) — the longest madd, held 6 counts. | الضّالِّينَ /adˤ.dˤɑːlˤ.lˤiː.na/ — /aː/ before the geminate لّ held 6 counts. |
| مَدّ العِوَض (*madd ʿiwaḍ*, compensatory madd) | 2 counts | In pause, *tanwīn* fatḥa ـً is replaced by a 2-count /aː/ (the same process noted under pausal forms, formalized in *tajwīd*). | عَليماً → pausal عَليما /ʕa.ˈliː.maː/. |

#### Tradition Difference

| Register | Realization |
|---|---|
| MSA | Does NOT use the *madd* count system; only the phonemic short vs long (≈1 vs 2 counts) distinction applies. |
| Classical (*tajwīd*) | *Madd* is fully operative and is one of the defining prosodic features distinguishing recitation (*tartīl*/*tajwīd*) from ordinary speech; counts vary by *riwāya* (e.g., Ḥafṣ ʿan ʿĀṣim). |

### Idghām and Assimilation

Connected-speech assimilations that operate at the suprasegmental/word-boundary level. The two signature processes are the DEFINITE-ARTICLE assimilation (sun vs moon letters) and *tajwīd* IDGHĀM (merging of *nūn*/*tanwīn* and certain consonants), often accompanied by GHUNNA (nasalization).

#### Definite-Article Assimilation (Sun vs Moon Letters)

The definite article الـ /al-/ assimilates its lām to a following SUN LETTER (الحُروف الشَّمْسِيّة), producing a geminate; before a MOON LETTER (الحُروف القَمَرِيّة) the lām stays clear. This is a productive suprasegmental gemination at the article boundary.

| Class | Letters | Behaviour |
|---|---|---|
| Sun letters (الحُروف الشَّمْسِيّة) | ت ث د ذ ر ز س ش ص ض ط ظ ل ن (14 coronals) | lām assimilates: الشَّمْس /aʃ.ˈʃams/ 'the sun' [ʃː]. |
| Moon letters (الحُروف القَمَرِيّة) | ء ب ج ح خ ع غ ف ق ك م ه و ي (14) | lām stays clear: القَمَر /al.ˈqa.mar/ 'the moon'. |

**Examples:**

| Form | IPA | Note |
|---|---|---|
| الشَّمْس | /aʃ.ˈʃams/ | sun letter ش — lām → geminate ʃː |
| النّور | /an.ˈnuːr/ | sun letter ن |
| الرَّحْمن | /ar.ˈraħ.maːn/ | sun letter ر |
| القَمَر | /al.ˈqa.mar/ | moon letter ق — lām clear |
| الكِتاب | /al.ki.ˈtaːb/ | moon letter ك |

#### Idghām (Tajwīd)

In *tajwīd*, a final *nūn*/*tanwīn* assimilates (*idghām*) into a following ي ر م ل و ن (the يَرْمَلون set), with *ghunna* (nasalization, ~2 counts) for ي و م ن and without *ghunna* for ل ر. Other rules cover *iqlāb* (ن→م before ب) and *ikhfāʾ* (partial nasal hiding). These are Classical/recitation features.

| Form | IPA | Process |
|---|---|---|
| مَن يَقول | /maj.ja.quːl/ | nūn + ي, idghām with *ghunna* |
| مِن رَبِّهِم | /mir.rab.bi.him/ | nūn + ر, idghām without *ghunna* |
| مِن بَعْد | /mim.baʕd/ | iqlāb: nūn → م before ب |

#### Tradition Difference

| Register | Realization |
|---|---|
| MSA | Sun/moon article assimilation is universal in all registers. *Tajwīd idghām* of *nūn*/*tanwīn* is a recitation feature; in plain MSA speech *nūn* is often pronounced clearly. |
| Classical (*tajwīd*) | Full *idghām*/*iqlāb*/*ikhfāʾ*/*ghunna* system applies with prescribed counts. |
| Source contrast | The article-assimilation parallel: the source and Hebrew also show assimilation phenomena (e.g., Hebrew *dagesh* after the article, *nun* assimilation); the sun/moon split is the Arabic-specific realization. |

### Hamzat al-Waṣl

HAMZAT AL-WAṢL (هَمْزة الوَصْل, the elidable/connecting hamza) is a prosodic-juncture phenomenon: word-initial Arabic syllables cannot begin with a vowel or a cluster, so an initial /ʔ/+vowel is supplied utterance-initially but ELIDED when the word follows another in connected speech, with the preceding word's vowel carrying over. It chiefly appears on the article الـ and on Form VII–X verbs and certain nouns (اسم, ابن).

- **IPA notation:** Initial [ʔV] in isolation; in connection the [ʔ] and its vowel drop and the prior vowel links directly.

| Word | Isolation | In connection | Note |
|---|---|---|---|
| الكِتاب | /ʔal.ki.ˈtaːb/ | فِي الكِتاب /fi‿l.ki.ˈtaːb/ | the /ʔa/ elides → liaison |
| اسْم 'name' | /ʔism/ | بِسْمِ اللَّه /bis.mil.laːh/ | *waṣl* hamza of اسم elided |
| ابْن 'son' | /ʔibn/ | (initial hamza elides in connection) | — |

**Relation to clusters:** This is Arabic's repair for the ban on word-initial consonant clusters and onsetless syllables — the functional analog of an epenthetic/prosthetic vowel; it operates at the phrase-prosodic level (sandhi/liaison).

### Intonation

Intonation (التَّنْغيم *at-tanghīm*) is the only use of pitch in Arabic (recall: NO lexical tone). Pitch contours over the intonation phrase signal sentence type, focus, continuation vs completion, and speaker attitude. The inventory of contours is broadly the cross-linguistic fall / rise / fall-rise / level set; the contrasts below are robust across MSA and Classical reading, with attitudinal and dialectal nuance.

- **IPA notation:** Phrase boundaries `|` (minor) `‖` (major); global rise ↗ and fall ↘; nuclear pitch movements on the most prominent (final-stressed) syllable. Iconic marks: `ˋ` fall, `ˊ` rise, `ˇ` fall-rise.

#### Patterns

| Type | Contour | Example |
|---|---|---|
| Declarative (statement, جُمْلة خَبَرِيّة) | Overall falling; final fall ↘ on the nuclear syllable conveying completeness. | هٰذا كِتابٌ. ↘ /ˈhaː.ðaː ki.ˈtaː.bun/ 'This is a book.' |
| Yes/No question (سُؤال — هل / أ or intonation-only) | Rising ↗; the final rise marks interrogation. May be introduced by هَلْ /hal/ or the interrogative hamza أَ, or signalled by rising intonation alone on an otherwise declarative string. | هَلْ هٰذا كِتابٌ؟ ↗ /hal ˈhaː.ðaː ki.ˈtaː.bun/ 'Is this a book?' — and intonation-only: هٰذا كِتابٌ؟ ↗ (same words, rising = question). |
| Wh-question (أَداة استفهام: ما، مَن، أَيْنَ، كَيْفَ ...) | Typically falling ↘ (like statements), since the question word carries the interrogative load; high onset on the wh-word. | أَيْنَ الكِتابُ؟ ↘ /ˈʔaj.na‿l.ki.ˈtaː.bu/ 'Where is the book?' |
| Continuation / listing (non-final) | Rising or level ↗/→ on non-final items, falling ↘ on the last, signalling 'more to come' then closure. | كِتابٌ، ↗ وقَلَمٌ، ↗ ودَفْتَرٌ. ↘ 'a book, a pen, and a notebook.' |
| Command / exclamation (أمر / تَعَجُّب) | Falling, often with raised intensity/range; emphatic fall ↘. | اِقْرَأْ! ↘ /ˈʔiq.raʔ/ 'Read!' |

#### Focus

Like the English template's tonicity, Arabic marks FOCUS/new information by placing the nuclear pitch accent on the focused word; fronting (تَقْديم) and the particle إِنَّ can also mark emphasis/topic. Default broad focus puts the nucleus on the last content word.

- **Example:** أَحْمَدُ كَتَبَ الرِّسالةَ ↘ (neutral) vs أَحْمَدُ ↘ كَتَبَ الرِّسالةَ ('AḤMAD wrote the letter', contrastive nucleus on the subject).

#### Tradition Difference

| Register | Realization |
|---|---|
| MSA | Pan-Arab broadcast/standard intonation as above; regional substrate colours pitch range and the exact rise shapes. |
| Classical (*tajwīd*) | Quranic recitation (*tartīl*) has its own melodic prosody layered on top of segmental *tajwīd* — measured pacing, *waqf*-conditioned pitch resolution, and (in *murattal*/*mujawwad* styles) elaborated melodic contours — but this is a recitation art, not lexical/grammatical tone. |
| Source contrast | The source and Hebrew likewise use phrase intonation (and Hebrew adds cantillation/*teʿamim* that encode syntax and chant melody); Arabic's *tajwīd waqf* system is the functional cousin of those liturgical prosodic systems. |

### Summary Table

At-a-glance: which suprasegmentals are PHONEMIC (contrastive) vs predictable/allophonic vs absent in Arabic, contrasted with the English template.

| Feature | Arabic | English template |
|---|---|---|
| Lexical tone | ABSENT — no lexical/grammatical tone | Absent (stress-accent language) |
| Word stress | PREDICTABLE (weight-sensitive, rule-based) — NOT phonemic; no stress minimal pairs | PHONEMIC — stress alone contrasts words (record N vs V) |
| Consonant length (gemination/shadda) | PHONEMIC — درس /darasa/ vs درّس /darrasa/; also morphological (Form II) | Not phonemic (only across morpheme boundaries) |
| Vowel length | PHONEMIC — /a i u/ vs /aː iː uː/; كتب vs كاتب | Allophonic (pre-fortis clipping); tense/lax mainly qualitative |
| Vowel reduction in unstressed syllables | ABSENT — vowel quality preserved regardless of stress | Pervasive — reduction to schwa /ə/; weak forms |
| Emphasis spread (tafkhīm) | Suprasegmental DOMAIN feature — emphatics back adjacent vowels/consonants | No analog |
| Morpho-prosodic desinences (tanwīn, iʿrāb) | Present (case/mood + nunation); dropped in pause; NOT emitted in caseless reader | No analog |
| Intonation (phrase-level pitch) | Present — fall/rise/level for sentence type & focus | Present — nuclear-tone system (fall, rise, fall-rise, rise-fall, level) |

### Cross-Reference

Suprasegmental cross-references to the Semitic siblings and to the Peshitta reader tiers.

| Target | Cross-reference |
|---|---|
| To source (Syriac/Aramaic) | The source's suprasegmental notes (penultimate-default stress, phonemic gemination in Eastern Syriac, phonemic vowel length, pharyngealization of tˤ/sˤ backing adjacent vowels) all have direct Arabic counterparts. Arabic patterns with the CONSERVATIVE Eastern tradition: it keeps phonemic gemination (vs Western Syriac's loss) and the full emphatic series. |
| To Hebrew | Biblical Hebrew shares phonemic gemination (*dagesh forte*) and phonemic vowel length and an atonal phrase-intonation system; Hebrew differs in that its stress is phonologically significant (*milra*/*milel* with morphological conditioning), whereas Arabic stress is purely weight-predictable. Arabic gemination is freer (no guttural/*resh* restriction, unlike Hebrew). |
| To Peshitta reader | In the Arabic Peshitta reader tiers (Scholarly, Pretty, Vocalized abjad, Unvocalized abjad), gemination is rendered with shadda ـّ in the Vocalized tier and inferred in the Unvocalized tier; vowel length is preserved via the matres lectionis (ا و ي); *iʿrāb*/*tanwīn* are NOT emitted (pausal/caseless forms used) to stay reversible against the caseless source IPA; emphasis spread is implicit in the emphatic letters chosen. Source gap resolutions affecting prosody: e→kasra/ī and o→ḍamma/ū (the source's mid vowels collapse into Arabic's three qualities while length is retained). |

---

*Section: Suprasegmentals — Arabic Pronunciation Guide. Compiled by Shin.*

## Syllable Structure

Syllable structure of Arabic (`العربية`), covering Modern Standard Arabic (MSA, `الفصحى` *al-fuṣḥā*) and Classical/Quranic Arabic in parallel. Arabic phonotactics are remarkably restrictive and symmetric: every syllable begins with EXACTLY ONE consonant (a strictly obligatory onset), so there are NO vowel-initial and NO consonant-cluster onsets — word-initial clusters are resolved by HAMZAT AL-WAṢL (an elidable connecting hamza) or a prosthetic vowel. The nucleus is a single short or long vowel; the coda is zero, one, or (word-finally/pausally only) two consonants. This yields a tight inventory of templates: CV, CVː, CVC, CVːC, CVCC. As in its Semitic sisters, syllable WEIGHT (light vs. heavy vs. superheavy) is the engine that drives Arabic's rule-based, predictable stress. This section is the Arabic counterpart of the English guide's `syllable_structure` section and the Peshitta (Syriac) guide's `syllable_structure` section; where Syriac tolerates true onset clusters (CCVC, e.g. /ʃmaʕ/), native Arabic does NOT — a key contrast that the Peshitta–Arabic transducer must mediate.

**IPA template:** `CV(ː)(C)(C)`

**Expanded:** `C V(ː) (C)(C)` — onset = obligatory single C; nucleus = single short or long V; coda = 0, 1, or 2 C (two only word-finally/pausally)

**Maximal syllable:** `CVːC` or `CVCC` (superheavy, word-final only)

**Minimal syllable:** `CV` (light, open)

**Components:**

- **Onset:** exactly ONE consonant preceding the nucleus *(obligatory — never zero, never a cluster)*
- **Nucleus:** a single short or long vowel *(required)*
- **Coda:** 0, 1, or 2 consonants following the nucleus *(optional; two only word-finally/pausally)*

### Obligatory Onset

Every Arabic syllable MUST begin with exactly one consonant.

Unlike English (which allows onsetless syllables like /æt/ 'at' and clusters like /spr/), Arabic permits neither a zero onset nor a complex onset. A surface-vowel-initial word in fact begins with a consonant: either a phonemic hamza `ء` /ʔ/ (*hamzat al-qaṭʕ*, a 'cutting' glottal stop that is always pronounced) or the elidable *hamzat al-waṣl* (see below). There is therefore no /V/ or /VC/ syllable type in Arabic, and no onset cluster (no /CCV…/).

| Property | Value |
|---|---|
| Single consonant only | yes |
| No onset clusters | yes |
| No zero onset | yes |

### Onset

Exactly ONE consonant. Obligatory in every syllable. Any of the 28 consonants may serve as an onset, including hamza `ء` /ʔ/, the pharyngeals `ح` ħ and `ع` ʕ, the emphatics `ط` tˤ `ص` sˤ `ض` dˤ `ظ` ðˤ, and the geminate-first-half of a shadda. Onset clusters (two consonants before the vowel) are PHONOTACTICALLY ILLEGAL in native Arabic.

- **Minimum consonants:** 1
- **Maximum consonants:** 1
- **Optional:** no

**No clusters:** Word-initial consonant clusters do not occur. A would-be initial cluster is repaired by *hamzat al-waṣl* plus a prosthetic vowel (see [Hamzat al-Waṣl](#hamzat-al-waṣl)).

| IPA | Arabic | Onset | Note |
|---|---|---|---|
| /ba/ | `بَ` | `b ب` | plain stop onset |
| /ʔa/ | `أَ` | `ʔ ء` (*hamzat al-qaṭʕ*) | even a 'vowel-initial' word like `أَكَلَ` /ʔa.ka.la/ 'he ate' opens with a phonemic glottal stop |
| /ʕa/ | `عَ` | `ʕ ع` | pharyngeal onset, as in `عَرَبِيّ` /ʕa.ra.bijj/ 'Arab' |

### Nucleus

The obligatory core: a SINGLE vowel, either short (/a/, /i/, /u/) or long (/aː/, /iː/, /uː/). There are no syllabic consonants (contrast English /bʌt.l̩/), and no nuclei filled by anything but a vowel. The two diphthongs /aj/ (*ay*) and /aw/ (*aw*) are analyzed as a short vowel + glide coda (Vw, Vj), i.e. they pattern as CVC-type rhymes, not as complex nuclei.

- **Required:** yes

**Short vowels:**

| Vowel | Harakah |
|---|---|
| /a/ | *fatḥa* `ـَ` |
| /i/ | *kasra* `ـِ` |
| /u/ | *ḍamma* `ـُ` |

**Long vowels:**

| Vowel | Mater lectionis |
|---|---|
| /aː/ | *alif* `ا` |
| /iː/ | *yāʾ* `ي` |
| /uː/ | *wāw* `و` |

**Diphthongs as VC:** Falling diphthongs are phonotactically a short vowel nucleus + a glide in the coda.

| IPA | Arabic | Gloss | Analysis |
|---|---|---|---|
| /bajt/ | `بَيْت` | house | one CVC syllable: /ba/ + glide coda /j/ + /t/ |
| /jawm/ | `يَوْم` | day | one CVC syllable: /ja/ + glide coda /w/ + /m/ |

**Allophony note:** Near emphatics/pharyngeals, /a/ backs to [ɑ] (*tafkhīm*); in some Classical/dialectal contexts /a(ː)/ raises toward [e]/[i] (*imāla*). These are allophonic and do not change syllable count.

### Coda

0, 1, or 2 consonants after the nucleus. A single-consonant coda is fully general (medially and finally). A TWO-consonant coda (CC) occurs ONLY word-finally — and most robustly in PAUSAL position (*waqf*), where final short vowels and *tanwīn* are dropped, exposing a final cluster. Word-medial two-consonant codas do not occur; an intervocalic CC sequence is always split by syllabification (the first C is a coda, the second an onset). Gemination (*shadda*) likewise splits across the syllable boundary: the first half closes one syllable (coda), the second half opens the next (onset).

- **Minimum consonants:** 0
- **Maximum consonants:** 2
- **Optional:** yes
- **Two-consonant coda:** word-final only

| IPA | Arabic | Coda | Gloss | Type |
|---|---|---|---|---|
| /baːb/ | `بَاب` | `b` | door | CVːC, single coda |
| /bint/ | `بِنْت` | `nt` | girl/daughter | CVCC, final two-consonant coda (pausal) |
| /ʕabd/ ~ pausal of `عَبْد` | `عَبْد` | `bd` | servant/slave | CVCC pausal; in context `عَبْدُ` /ʕab.du/ resyllabifies |

### Syllable Weight

Arabic syllables are classified by WEIGHT (mora count), which is the sole determinant of stress placement (stress is rule-based and predictable, NOT phonemic). This weight sensitivity is shared with the Semitic sisters and is central to both MSA and *tajwīd* prosody.

| Weight | Label | Templates | Morae | Description |
|---|---|---|---|---|
| light | `خفيف` *khafīf* | `CV` | 1 | Open syllable with a short vowel. The only light syllable type. |
| heavy | `ثقيل` *thaqīl* | `CVː`, `CVC` | 2 | Either an open syllable with a long vowel (CVː) or a closed syllable with a short vowel (CVC). Both count as two morae. |
| superheavy | `ثقيل جدًّا / مفرط` (overlong) | `CVːC`, `CVCC` | 3 | A long vowel plus a coda (CVːC), or a short vowel plus a two-consonant coda (CVCC). Restricted to WORD-FINAL / PAUSAL position. Always attracts stress when present. |

**Examples by weight:**

| Weight | IPA | Arabic | Template | Context / Gloss |
|---|---|---|---|---|
| light | /ka/ | `كَ` | CV | first syllable of `كَتَبَ` /ka.ta.ba/ 'he wrote' |
| heavy | /kaː/ | `كَا` | CVː | `كَاتِب` /kaː.tib/ 'writer' |
| heavy | /kat/ | `كَتْ` | CVC | first syllable of `مَكْتَب` /mak.tab/ 'office' |
| superheavy | /ki.taːb/ | `كِتَاب` | …CVːC | 'book' — final superheavy syllable /taːb/ is stressed |
| superheavy | /bint/ | `بِنْت` | CVCC | 'girl' — final two-consonant coda, pausal |

**Stress link:** Stress falls on a final superheavy syllable; otherwise on a heavy penult; otherwise it retracts to the antepenult (within a three-syllable window). Because weight is fully recoverable from the syllable template, MSA stress is algorithmic — see the suprasegmentals/stress section for the full rule set.

### Syllable Types

| Type | Description | Weight | IPA example | Arabic | In word | Frequency |
|---|---|---|---|---|---|---|
| CV | Open light syllable: onset + short vowel. The most common syllable and the minimal well-formed syllable. | light | /ka/ | `كَ` | `كَتَبَ` /ka.ta.ba/ 'he wrote (CV.CV.CV)' | Most common |
| CVː | Open heavy syllable: onset + long vowel. Long vowel written with a mater lectionis (`ا/و/ي`). | heavy | /kaː/ | `كَا` | `كَاتِب` /kaː.tib/ 'writer (CVː.CVC)' | Very common |
| CVC | Closed heavy syllable: onset + short vowel + single coda. | heavy | /min/ | `مِنْ` | `مَكْتَب` /mak.tab/ 'office (CVC.CVC)' | Very common |
| CVːC | Closed superheavy syllable: onset + long vowel + single coda. Word-final / pausal. | superheavy | /baːb/ | `بَاب` | `كِتَاب` /ki.taːb/ 'book (CV.CVːC)' | Common (word-final) |
| CVCC | Closed superheavy syllable: onset + short vowel + two-consonant coda. Word-final / pausal ONLY; in connected (non-pausal) speech a case/desinential vowel or an epenthetic vowel typically breaks the cluster. | superheavy | /bint/ | `بِنْت` | `عَبْد` /ʕabd/ 'servant (pausal CVCC; context `عَبْدُ` /ʕab.du/)' | Common in pause; resolved in context |

### Non-occurring Types

Types that are normal in English (and partly in Syriac) but are PHONOTACTICALLY ABSENT in native Arabic.

| Type | Reason |
|---|---|
| V / VC | No onsetless syllables; every syllable needs a single consonant onset (a hamza supplies it for 'vowel-initial' words). |
| CCV / CCVC | No onset clusters; word-initial clusters are repaired by *hamzat al-waṣl* + prosthetic vowel. (Contrast Syriac CCVC /ʃmaʕ/.) |
| CCCV… | Three-consonant onsets are impossible (contrast English /spr/). |
| …CCC | Three-consonant codas do not occur; the maximal coda is two consonants, word-finally only. |

### Hamzat al-Waṣl

*Hamzat al-waṣl* (`هَمْزَة الوَصْل`, the 'connecting hamza') is the principal repair for Arabic's ban on onsetless syllables AND on word-initial clusters. Many words whose stem begins with a consonant cluster (e.g. the imperative, Form VII–X verbs and their *masdars*, and the definite article `ال`) are written with a prosthetic alif carrying an elidable hamza. At the START of an utterance it is pronounced [ʔ] + a prosthetic vowel, supplying a legal CV onset; WITHIN an utterance, after a preceding vowel, the hamza and its vowel ELIDE and the word links directly to the prior syllable.

**Prosthetic vowel:**

| Context | Prosthetic vowel |
|---|---|
| Default | /i/ (*kasra*) — the most common prosthetic vowel |
| Imperatives with u-stem | /u/ (*ḍamma*) when the imperative's stem vowel is /u/ (e.g. `اُكْتُبْ` *uktub* 'write!') |
| Definite article | /a/ (*fatḥa*) — the article is `الـ` /ʔal/ utterance-initially |

**Examples:**

| Form | Utterance-initial IPA | In-context IPA | Gloss | Note |
|---|---|---|---|---|
| `اِسْم` | /ʔism/ | `بِسْم` → /bis.mi/ (in `بِسْمِ اللّٰه`) | name | The stem is /sm-/, an illegal initial cluster; waṣl supplies /ʔi/ initially (/ʔism/), but after `بِـ` /bi/ it elides: `بِسْمِ` /bis.mi/. |
| `اُكْتُبْ` | /ʔuk.tub/ | `وَاكْتُبْ` → /wak.tub/ | write! (imperative) | Prosthetic /u/; after `وَ` /wa/ the waṣl elides → /wak.tub/. |
| `اِبْن` | /ʔibn/ | `يَا ابْن` → /jaː.bn/ (waṣl elided after `يَا`; long ā preserved) | son | — |

**Contrast with *hamzat al-qaṭʕ*:** *Hamzat al-qaṭʕ* (`همزة القطع`, written `أ إ ؤ ئ` or `ء`) is a PHONEMIC, always-pronounced /ʔ/ that never elides (e.g. `أَكَلَ` /ʔa.ka.la/ 'he ate'). Only *hamzat al-waṣl* elides.

### The Definite Article and Waṣl

The definite article `ال` (*al-*) is the most frequent carrier of *hamzat al-waṣl* and a showcase of how onset/coda and waṣl interact. Utterance-initially it is /ʔal/; in context the waṣl elides to /l/-. Its lām /l/ then either surfaces (moon letters) or assimilates totally into a geminate (sun letters), reshaping the following syllable's onset/coda.

#### Moon Letters (`الحروف القمرية`, *al-ḥurūf al-qamariyya*)

**Rule:** Before a MOON letter the lām /l/ is pronounced and closes the article syllable: /ʔal.C…/. The 14 moon letters are `ء ب ج ح خ ع غ ف ق ك م ه و ي`.

| Form | IPA | Gloss | Syllabification |
|---|---|---|---|
| `القَمَر` | /ʔal.qa.mar/ | the moon | ʔal.qa.mar (CVC.CV.CVC); lām is an audible coda |

#### Sun Letters (`الحروف الشمسية`, *al-ḥurūf aš-šamsiyya*)

**Rule:** Before a SUN letter the lām assimilates totally to the following consonant (*idghām*), producing a geminate; the lām is NOT pronounced but the doubled consonant is. The 14 sun letters are `ت ث د ذ ر ز س ش ص ض ط ظ ل ن`.

| Form | IPA | Gloss | Syllabification |
|---|---|---|---|
| `الشَّمْس` | /ʔaʃ.ʃams/ | the sun | ʔaʃ.ʃams (CVC.CVCC); the first half of the geminate /ʃ/ is the coda of the article syllable, the second half the onset of the noun |

#### In-context Elision

After a preceding vowel the article's waṣl hamza and its /a/ elide, so the lām (or geminate) attaches directly to the prior syllable.

| Form | IPA | Gloss | Note |
|---|---|---|---|
| `فِي القَمَر` | /fil.qa.mar/ | in the moon | fī + al → /fil/ (waṣl /ʔa/ elided; lām surfaces, moon letter) |
| `فِي الشَّمْس` | /fiʃ.ʃams/ | in the sun | fī + aš → /fiʃ/ (waṣl /ʔa/ AND lām elided into the geminate, sun letter) |

### Syllabification

**Principle:** Onset-first, single-onset parsing (a maximal-onset of exactly one consonant). Because onsets are always a single consonant and codas may be one (medially) or two (finally), an intervocalic VCV is parsed V.CV, and an intervocalic VCCV is parsed VC.CV (the only legal split). Gemination is parsed across the boundary (VC.CV). There is never a medial onset cluster.

**Rules:**

- Every syllable starts with exactly one consonant; assign one and only one consonant to each onset.
- A single intervocalic consonant joins the FOLLOWING syllable: V.CV (e.g. `كَتَبَ` → /ka.ta.ba/).
- A medial cluster of two consonants splits VC.CV — the first is a coda, the second an onset (e.g. `مَكْتَب` → /mak.tab/).
- A geminate (*shadda*) splits VC.CV across its two halves (e.g. `مُدَرِّس` → /mu.dar.ris/ 'teacher').
- A two-consonant coda is tolerated only at the end of an utterance (pause); within a phrase a final cluster is broken by the case/connecting vowel or by epenthesis.
- Long vowels (CVː) are never followed by a tautosyllabic two-consonant coda except word-finally in pause; medial CVːC closed syllables shorten or are avoided (vowel shortening in closed syllables).

**Examples:**

| Word | IPA | Syllables | Gloss | Note |
|---|---|---|---|---|
| `كَتَبَ` | /ka.ta.ba/ | ka (CV) · ta (CV) · ba (CV) | — | three light open syllables; each medial consonant goes to the following onset |
| `مَكْتَبَة` | /mak.ta.ba/ | mak (CVC) · ta (CV) · ba (CV) | library | medial /kt/ splits CVC.CV; final tāʾ marbūṭa /a/ in pause |
| `مُدَرِّس` | /mu.dar.ris/ | mu (CV) · dar (CVC) · ris (CVC) | teacher | shadda geminate /rr/ splits across the dar.ris boundary |
| `اِسْتَقْبَلَ` | /ʔis.taq.ba.la/ | ʔis (CVC) · taq (CVC) · ba (CV) · la (CV) | he received/welcomed (Form X) | initial waṣl /ʔi/ supplies a legal onset for the stem-initial cluster /st/ |
| `الكِتَاب` | /ʔal.ki.taːb/ | ʔal (CVC) · ki (CV) · taːb (CVːC) | the book | moon-letter article; final superheavy /taːb/ takes stress |

### Constraints

- Every syllable has an obligatory onset of exactly ONE consonant; there are no onsetless (V-, VC-) syllables.
- No word-initial consonant clusters; a stem-initial cluster is repaired by *hamzat al-waṣl* + a prosthetic vowel (default /i/, /u/ in u-imperatives, /a/ in the article).
- No onset clusters anywhere (no CCV, CCVC, CCCV); the onset is always a single consonant — a sharp contrast with English (/spr/) and even with Syriac (/ʃmaʕ/ CCVC).
- The nucleus is exactly one vowel (short or long); there are no syllabic consonants and no complex nuclei (diphthongs /aj aw/ are V + glide-coda).
- Codas are 0–2 consonants; a two-consonant coda (CVCC) occurs ONLY word-finally and chiefly in pausal forms.
- No three-consonant codas and no word-medial two-consonant codas; medial CC always splits VC.CV.
- Syllable templates are exactly: CV (light), CVː and CVC (heavy), CVːC and CVCC (superheavy, word-final).
- Syllable weight is contrastive for stress placement, which is rule-based and predictable (not phonemic); superheavy > heavy penult > antepenult.
- Gemination (*shadda*) is phonemic and always straddles a syllable boundary (VC.CV); it never forms an onset or coda cluster on its own.
- Long vowels generally shorten in closed syllables except utterance-finally (vowel shortening in closed syllables); a medial CVːC is dispreferred.
- In pause (*waqf*), final short vowels and *tanwīn* are dropped, which is what exposes word-final CVCC/CVːC superheavy syllables.
- Emphasis spread (*tafkhīm*) and ʿayn/ḥāʾ pharyngealization affect vowel quality within and across syllables but never change syllable count or the C/V skeleton.

### Cross-references

- **To English:** The English guide permits up to CCCVCCCC; Arabic is far stricter (CV(ː)(C)(C) with single onsets), making Arabic syllabification more deterministic. English has onsetless syllables and syllabic consonants; Arabic has neither.
- **To Peshitta (Syriac):** Classical Syriac (the source) tolerates true two-consonant ONSETS (CCVC, e.g. /ʃmaʕ/) which native Arabic forbids. Arabic resolves an equivalent initial cluster with *hamzat al-waṣl* + prosthetic vowel. Both languages share weight-sensitive prosody, single-vowel nuclei, and word-final two-consonant codas.
- **To Hebrew:** Biblical Hebrew (a Semitic sister) likewise requires an onset and uses shewa/epenthesis where Arabic uses *hamzat al-waṣl*; both restrict heavy/superheavy syllables and tie weight to stress. Hebrew marks the article by a prefix + gemination (dagesh forte) much as Arabic's `ال` geminates before sun letters.
- **Peshitta–Arabic transducer note:** In the Peshitta Arabic reader tiers, the transducer renders SOURCE Syriac onset clusters by stacking a sukun on the first consonant — e.g. `بְּרֵאשִׁית`-style `بْرِيشِيث` (*b-rīšīṯ*) — which DISPLAYS a CCV(C) onset that native Arabic phonotactics do not allow. This is a deliberate TRANSCRIPTION LIBERTY taken to preserve the source's syllable skeleton near-reversibly; it should be flagged as non-native Arabic structure, not as evidence that Arabic permits onset clusters.

---

*Section: Syllable Structure — Arabic Pronunciation Guide. Signed, Shin.*

## Phonological Rules

Systematic phonological and morphophonological processes that apply when underlying lexical/templatic forms of Arabic are realized in connected speech and careful recitation. Documented in parallel for the two shipped reference standards: **Modern Standard Arabic** (MSA, الفُصْحَى *al-fuṣḥā*) and **Classical/Quranic Arabic** (the *tajwīd* careful-recitation register, لُغَة القُرْآن). Each rule marks where the two standards diverge in the register-scope and notes fields (`MSA`, `Classical`, or `both`). As a Central-Semitic sister of the source language (Syriac/Aramaic) and of Hebrew, Arabic shares the deep architecture of these processes — definite-article assimilation, emphasis/pharyngealization spread, gemination, vowel reduction in unstressed syllables, pausal phenomena — but realizes them with its own richer codified detail (notably the *tajwīd* rules of *nūn sākina* and *tanwīn*). IPA is given with /slashes/ for phonemic underlying forms and [brackets] for phonetic surface forms; input → output shows the change.

> **Note on emission:** *iʿrāb* (case/mood desinential vowels) and connected-*tanwīn* are **descriptive here only** — the source IPA the readers are built from is caseless and pausal, so these word-final inflectional vowels are **NOT emitted** in the Peshitta reader tiers (see notes on `iʿrāb_desinential_inflection` and `pausal_forms_waqf`).

### Ordering of the Rules

The rules below are ordered to reflect the natural derivational/feeding sequence in deriving a surface utterance from underlying forms, and roughly from word-internal lexical processes to phrase-level *sandhi* to utterance-final pausal processes:

1. **gemination realization** (*shadda*, lexical);
2. **emphasis/pharyngealization spread** (allophonic, feeds vowel quality);
3. **imāla raising** (allophonic vowel quality);
4. **vowel shortening in closed syllables and unstressed vowel reduction** (syllable-level);
5. **definite-article ال assimilation** — sun vs moon letters (word-/clitic-internal *sandhi*);
6. **hamzat al-waṣl elision** (phrasal liaison);
7. **the *tajwīd* rules of *nūn sākina* and *tanwīn*** — *iẓhār* / *idghām* / *iqlāb* / *ikhfāʾ* — and general *idghām* assimilation (phrasal, recitation-level);
8. **iʿrāb desinential inflection** (descriptive morphosyntactic layer);
9. **pausal forms (waqf)** — applied last, utterance-finally, and counter-bleeds *iʿrāb*/*tanwīn* by deleting them.

Where a process is purely allophonic (emphasis spread, *imāla*) it logically precedes the syllable- and phrase-level processes that operate on the resulting qualities; pausal deletion is ordered last because it removes the very inflectional material that *iʿrāb* supplies. This sequence is a descriptive convenience, not a strict ordered-rule grammar.

### Rules at a Glance

| # | Rule | Process | Register |
|---|---|---|---|
| 1 | التشديد / الشدة (*at-tashdīd / aš-šadda*) — Gemination | `C → Cː` (held ~1.5–2× a singleton) | both |
| 2 | التفخيم وانتشار الإطباق (*at-tafkhīm*) — Emphasis (pharyngealization) spread | `/CˤV/ → [CˤVˤ]` ([+RTR] backing of vowels) | both |
| 3 | الإمالة (*al-imāla*) — Raising/fronting of ā | `/aː/ → [eː]~[ɛː]~[iː]` | Classical (variably); marginal in MSA |
| 4 | تقصير الصائت في المقطع المغلق (*taqṣīr aṣ-ṣāʾit*) — Vowel shortening / reduction | `Vː → V̆ / __C.C` | both |
| 5 | لام التعريف: الشمسية والقمرية (*lām at-taʿrīf*) — Article assimilation (sun vs moon) | `/al-/+Cˢᵘⁿ → [aC-Cˢᵘⁿ]`; `/al-/+Cᵐᵒᵒⁿ → [al-Cᵐᵒᵒⁿ]` | both |
| 6 | همزة الوصل (*hamzat al-waṣl*) — Elidable (connecting) hamza | `#ʔV → ∅V / X_` (after vowel-final word) | both |
| 7 | أحكام النون الساكنة والتنوين (*aḥkām an-nūn as-sākina*) — *nūn sākina* / *tanwīn* rules | `/n/ → [n] / [CC]+ghunna / [m] / [n̆]` | Classical (codified); looser in MSA |
| 8 | الإعراب (*al-iʿrāb*) — Desinential case/mood inflection (descriptive) | `-u / -a / -i` (nom./acc./gen.); `-un/-an/-in` | Classical (full); MSA (formal/read only) |
| 9 | الوقف (*al-waqf*) — Pausal forms (utterance-final) | `final V → ∅`; `tanwīn → ∅`; `ة → [h]/∅` | both |

---

### Rule 1: التشديد / الشدة (*at-tashdīd / aš-šadda*) — Gemination (consonant doubling)

A consonant marked with shadda (`ـّ`) is geminated — articulated as a single long/doubled segment held noticeably longer than its singleton counterpart. Gemination is **phonemic and contrastive** in Arabic: it distinguishes lexemes and is the morphological signature of the form-II (*faʿʿala*) intensive/causative and form-V verb stems, as well as the assimilated definite article on sun letters. Geminates are written with one consonant letter plus shadda, never two letters.

**Category:** gemination / lexical-contrastive
**IPA example:** `/darrasa/` → `[dar.ra.sa]` — دَرَّسَ *darrasa* 'he taught' (form II, geminated `رّ`); contrast دَرَسَ *darasa* `/da.ra.sa/` → `[da.ra.sa]` 'he studied'
**IPA notation:** `C → Cː` (phonemic, marked by shadda `ـّ`); held ~1.5–2× a singleton
**Environment:** Any position except absolute utterance-final, where a geminate is typically simplified/shortened in pausal release; fully realized intervocalically and word-medially. Sun-letter article assimilation (Rule 5) and *idghām* (Rule 7) both create surface geminates.
**Register:** both

**Notes:** Sibling parallel: this is the same contrastive gemination seen in Syriac Pa''el (*qattel*) and Hebrew *dagesh forte* / *piʿʿel*. Eastern Syriac preserves gemination while Western Syriac tends to simplify it; Arabic robustly preserves it in both MSA and Classical. In the Peshitta reader tiers the shadda is written and audible. Minimal pairs distinguish singleton from geminate, e.g. جَنَة *janah* 'small garden' vs جَنَّة *jannah* 'paradise' (shadda on `ن`), or the rule's own دَرَسَ *darasa* 'studied' vs دَرَّسَ *darrasa* 'taught'.

---

### Rule 2: التفخيم وانتشار الإطباق (*at-tafkhīm wa-intišār al-iṭbāq*) — Emphasis (pharyngealization) spread

The emphatic (pharyngealized) consonants `ط` /tˤ/, `ص` /sˤ/, `ض` /dˤ/, `ظ` /ðˤ/ — and, in many analyses, `ق` /q/ and the back consonants /ħ ʕ x ɣ/ and `ر` as [rˤ] — carry a secondary pharyngeal/uvular constriction (*tafkhīm*, 'thickening', the *iṭbāq* 'covering' gesture). This [+RTR retracted-tongue-root] feature **spreads** to neighbouring segments: adjacent vowels are backed and lowered (/a/ → [ɑ], /i/ → backed [ɪ], /u/ → backed [ʊ]), and flanking consonants take on emphatic colouring. The opposite, plain/clear quality of non-emphatic consonants is termed *tarqīq* ('thinning'). Emphasis is the single most pervasive allophonic process shaping Arabic vowel quality.

**Category:** allophonic / secondary-articulation spreading
**IPA example:** طَالِب `/tˤaːlib/` → `[tˤɑːlɪb]` 'student' (backed [ɑ] from emphatic `ط`) contrasts with تَالِف `/taːlif/` → `[taːlif]` 'spoiled' (plain `ت`, front [a]); cf. صَيْف `/sˤajf/` → `[sˤɑjf]` 'summer'
**IPA notation:** `/CˤV/ → [CˤVˤ]`; emphatic [+RTR] spreads to adjacent vowels and (gradiently) consonants within the syllable/foot. `a → [ɑ]`, `i → [ɪ~e backed]`, `u → [ʊ~o backed]`
**Environment:** Triggered by an emphatic/back consonant; spreads bidirectionally to tautosyllabic and often adjacent-syllable vowels and consonants until blocked (high front vowels /i iː/ and /j ʃ/ partially block leftward spread in some analyses). Domain ranges from the syllable to the whole word.
**Register:** both

**Notes:** Direct sibling of Syriac/Hebrew 'pharyngealization spread' / 'emphatic spreading' — same [+RTR] mechanism (cf. Hebrew /tˤ sˤ q/ backing adjacent vowels). Arabic has the larger emphatic set: it natively hosts `ط` and `ص` like the source, **plus** `ض` /dˤ/ and `ظ` /ðˤ/ which the 34-symbol source inventory **lacks**. The *lām* of the name الله (*Allah*) is velarized/emphatic [ɫ] after /a/ or /u/ (*Allāh* [ʔɑɫˈɫɑːh]) but clear after /i/ (*bismillāh*) — a special lexicalized case of this rule. Backing is allophonic, not separately written; the reader tiers inherit it via the underlying IPA. MSA and Classical agree; *tajwīd* codifies the degrees of *tafkhīm* explicitly.

---

### Rule 3: الإمالة (*al-imāla*) — Imāla (raising/fronting of ā toward [eː]/[iː])

*Imāla* ('inclination') is the raising and fronting of long /aː/ (and sometimes short /a/) toward [eː], [ɛː] or even [iː]. It is conditioned by a neighbouring high front vowel or /j/ in the word, and is **blocked** by emphatic, pharyngeal, and back consonants (which instead trigger backing, the antithesis of *imāla* — see emphasis spread). It is the mirror-image process to emphatic backing: front-colouring vs back-colouring of the low vowel.

**Category:** allophonic / vowel quality (register- and dialect-conditioned)
**IPA example:** كِتَاب `/kitaːb/` → `[kɪteːb]` 'book' (*imāla* of /aː/ to [eː] in a recitation tradition / dialect that applies it); cf. Quranic recitation مَجْرَاهَا *majrāhā* with *imāla* → `[meʒreːheː]` in Ḥamza's reading
**IPA notation:** `/aː/` (and `/a/`) `→ [eː]~[ɛː]~[iː]` / in fronting environments (esp. near /i iː j/, and away from emphatics/back consonants)
**Environment:** Long/short /a/ in a word containing or adjacent to /i iː j/, in non-emphatic, non-back contexts. Heavily realized in certain Quranic recitation traditions (*qirāʾāt*, notably Ḥamza and al-Kisāʾī) and many dialects; only sporadic/lexicalized in standard MSA.
**Register:** Classical (variably); marginal in MSA

**Notes:** Sibling of Hebrew/Aramaic raising tendencies and the source's /a/ → [e]/[i] shifts; relevant to the project gap-resolution where source *e*/*o* map onto Arabic *kasra*/*ḍamma* or *ī*/*ū*. In standard MSA the canonical realization keeps [aː]; *imāla* is documented as a Classical/*qirāʾāt* and dialectal phenomenon and is **NOT applied by default** in the reader tiers (which target the neutral *fuṣḥā* value [aː]). MSA vs Classical: the contrast is precisely that Classical recitation traditions productively apply *imāla*, MSA largely does not.

---

### Rule 4: تقصير الصائت في المقطع المغلق (*taqṣīr aṣ-ṣāʾit fī l-maqṭaʿ al-mughlaq*) — Vowel shortening in closed syllables / unstressed reduction

Long vowels are shortened in syllables that become closed (CVːC or CVːCC reduces toward CVC) because Arabic strongly disprefers super-heavy syllables medially. When morphology or connected speech would create a long vowel in a closed syllable, the vowel shortens to its short counterpart. Relatedly, in rapid MSA short vowels in some unstressed open syllables may be reduced or, marginally, elided; classical *fuṣḥā* and *tajwīd* preserve full vowel quality and quantity more faithfully.

**Category:** syllable-structure / quantity adjustment
**IPA example:** قَالَ `/qaːla/` `[qɑːla]` 'he said' vs قُلْتُ `/qultu/` `[qʊltu]` 'I said' — the long *ā* of the root shortens (here to /u/ by ablaut) when the syllable closes with the /t/ of the suffix; geminate/cluster closure forces a short nucleus
**IPA notation:** `Vː → V̆ / __C.C` (in a syllable closed by a consonant cluster, or word-finally before a coda in pausal/connected contexts); also `V → reduced/elided` in some rapid-speech unstressed open syllables
**Environment:** A long vowel followed by a consonant cluster or geminate, or in a closed unstressed syllable; and (for reduction) short vowels in unstressed open syllables in fast speech. Blocked / not applicable at major pause where lengthening dominates (see pausal forms).
**Register:** both

**Notes:** Parallel to Hebrew/Aramaic vowel reduction in (pretonic, closed) syllables and the source's 'vowel reduction in unstressed syllables'. The reader tiers preserve vowel **length** via the *matres lectionis* (`ا`/`و`/`ي`), so where the underlying source vowel is long it is kept long; shortening here is the surface phonetic norm, not an orthographic deletion. MSA tolerates more reduction in casual speech; Classical/*tajwīd* maintains precise quantities (and conversely lengthens at *madd* points).

---

### Rule 5: لام التعريف: الحروف الشمسية والقمرية (*lām at-taʿrīf: al-ḥurūf aš-šamsiyya wa-l-qamariyya*) — Definite-article assimilation: sun vs moon letters

The definite article is written ال (alif + lām) before every noun, but its *lām* /l/ is pronounced only before **moon letters** (*al-ḥurūf al-qamariyya*) and **assimilates** — disappearing and geminating the following consonant — before **sun letters** (*al-ḥurūf aš-šamsiyya*). The 14 sun letters are the coronals: `ت ث د ذ ر ز س ش ص ض ط ظ ل ن`. The 14 moon letters are the rest: `ا ب ج ح خ ع غ ف ق ك م ه و ي` — and word-initial hamza `ء` likewise does not assimilate, patterning with the moon letters. Orthographically the *lām* is still written; the assimilation is marked by placing shadda on the sun letter (and no *sukūn* on the *lām*).

**Category:** morphophonological / clitic assimilation (*idghām* of *lām*)

**Sun letters (الحروف الشمسية, *lām* assimilates → gemination)**

| Group | Letters |
|---|---|
| Coronals (14) | `ت` `ث` `د` `ذ` `ر` `ز` `س` `ش` `ص` `ض` `ط` `ظ` `ل` `ن` |

**Moon letters (الحروف القمرية, *lām* pronounced [l])**

| Group | Letters |
|---|---|
| Remaining consonants (14) + initial hamza | `ا` `ب` `ج` `ح` `خ` `ع` `غ` `ف` `ق` `ك` `م` `ه` `و` `ي` (+ `ء`) |

**IPA example:** الشَّمْس `/al-ʃams/` → `[aʃˈʃams]` 'the sun' (sun letter `ش`: *lām* assimilates, `ش` geminates — and is itself the eponymous 'sun' word); القَمَر `/al-qamar/` → `[alˈqamar]` 'the moon' (moon letter `ق`: *lām* pronounced [l] — the eponymous 'moon' word)
**IPA notation:** `/al-/ + Cˢᵘⁿ → [aC-Cˢᵘⁿ]` (*lām* → gemination of following coronal); `/al-/ + Cᵐᵒᵒⁿ → [al-Cᵐᵒᵒⁿ]` (*lām* retained)
**Environment:** Definite article ال immediately preceding a noun/adjective; sun letter following → total regressive assimilation (*idghām*) of /l/; moon letter following → /l/ pronounced [l].
**Register:** both

**Notes:** A signature Arabic rule and a strong sibling parallel to the Hebrew definite article הַ + *dagesh forte* (gemination of the following consonant) — both are prefixed articles that geminate. Hebrew geminates **all** consonants (with guttural exceptions); Arabic geminates only the coronal 'sun' set, leaving moon letters with an audible /l/. The initial /a/ of the article is itself a *hamzat al-waṣl* and elides in connected speech (see next rule), e.g. *fī š-šams*. In the **vocalized** reader tier the shadda makes the assimilation explicit; the **unvocalized** tier relies on the reader's knowledge of the sun/moon distinction. MSA and Classical fully agree.

---

### Rule 6: همزة الوصل (*hamzat al-waṣl*) — Elidable (connecting) hamza

Arabic forbids word-initial consonant clusters, so words that underlyingly begin with a cluster (the definite article ال, form VII–X verbs, certain nouns like ابن *ibn* 'son' and اسم *ism* 'name') carry a prosthetic 'connecting hamza' (*hamzat al-waṣl*, written `ٱ` or as a plain alif). It is pronounced [ʔ] + helping vowel **only** utterance-initially; in connected speech after a preceding vowel it **elides** entirely (both the glottal stop and its vowel), linking the words. This contrasts with *hamzat al-qaṭʿ* (the 'cutting' / stable hamza `أ` `إ` `ؤ` `ئ` `ء`), which is always pronounced.

**Category:** phrasal liaison / vowel elision (*waṣl*)
**IPA example:** اِسْم in isolation `[ʔismun]`; in بِسْمِ اللَّه `/bi+ism+allaːh/` → `[bis.mil.laːh]` — the *hamzat al-waṣl* of اسم elides after بِ, and the article's *waṣl* elides too: 'in the name of God' (← بِ + اسْم + اللَّه)
**IPA notation:** `#ʔV (waṣl) → ∅V / X_` (after a preceding word ending in a vowel, the prosthetic glottal stop AND its vowel elide); utterance-initially → `[ʔV]` is pronounced
**Environment:** Word-initial *hamzat al-waṣl* preceded (in the same breath group) by a vowel-final word → elides; utterance-initial or after a true pause → realized as [ʔ] + helping vowel (default /i/, /a/ for the article, /u/ before a root with /u/).
**Register:** both

**Notes:** This is Arabic's answer to no-initial-clusters, functionally analogous to the source's resolution of clusters and to Hebrew's helping/prosthetic vowels and the article's behavior. Differs from English liaison (linking-R): Arabic liaison is **deletion** of a prosthetic onset, not insertion. In the reader tiers, verse-internal liaison may surface the elided forms; utterance-initial forms keep [ʔ]. MSA and Classical agree; *tajwīd* codifies the helping-vowel choice precisely.

---

### Rule 7: أحكام النون الساكنة والتنوين والإدغام (*aḥkām an-nūn as-sākina wa-t-tanwīn wa-l-idghām*) — Rules of *nūn sākina* / *tanwīn* and general assimilation (*tajwīd*)

A vowelless *nūn* (`نْ`) or *tanwīn* (nunation, the indefinite case-endings `ـً`/`ـٍ`/`ـٌ` pronounced *-an*/*-in*/*-un*) undergoes four codified behaviours depending on the following letter — the cornerstone of *tajwīd*. The same *idghām* principle assimilates other consonants too (e.g. the Ethpeel-type and final-/n/ assimilations seen across Semitic).

**Category:** phrasal assimilation / *tajwīd* nasal rules

**The four behaviours of *nūn sākina* / *tanwīn***

| # | Rule | Triggering letters | Outcome |
|---|---|---|---|
| 1 | **IẒHĀR** (clear pronunciation) | the six throat letters `ء` `ه` `ع` `ح` `غ` `خ` | /n/ stays `[n]` |
| 2 | **IDGHĀM** (merging) | `ي` `ر` `م` `ل` `و` `ن` | /n/ assimilates into the next consonant — **with** nasal hum (*ghunna*, *bi-ghunna*) for `ي` `ن` `م` `و`; **without** *ghunna* for `ل` `ر` |
| 3 | **IQLĀB** (conversion) | `ب` | /n/ → `[m]` with *ghunna* |
| 4 | **IKHFĀʾ** (concealment) | the remaining 15 letters | /n/ is a light nasalized `[n̆]` with *ghunna*, articulated toward the place of the following consonant |

**IPA example:** مِنْ بَعْد `/min baʕd/` → `[mim baʕd]` (*iqlāb*: `نْ`→[m] before `ب`); مَنْ يَعْمَل `/man jaʕmal/` → `[maj.jaʕmal]` (*idghām* of `نْ` into `ي` with *ghunna*); مِنْ خَيْر `/min xajr/` → `[min xajr]` (*iẓhār*: `نْ` stays [n] before throat-letter `خ`)
**IPA notation:** `/n/` (*nūn sākina* `ـْن` or *tanwīn* `ـً ـٍ ـٌ`) → `[n]` (*iẓhār*) | → `[CC]/[w̃]/[j̃]` + *ghunna* (*idghām*) | → `[m]` (*iqlāb*) | → `[n̆` nasalized, *ghunna*`]` (*ikhfāʾ*), conditioned by the **following** consonant
**Environment:** *nūn sākina* or *tanwīn* immediately followed by another consonant, within a word or across a word boundary in the breath group; the four outcomes are selected by the place/identity of that following consonant.
**Register:** Classical (fully codified in *tajwīd*); applied more loosely / variably in MSA

**Notes:** Strong sibling parallel: Semitic 'assimilation of Nun' (Syriac/Hebrew /n/ → following C with gemination) is the same regressive nasal assimilation that Arabic has elaborated into the full four-way *tajwīd* system. **Mark MSA vs Classical clearly:** the *iẓhār*/*idghām*/*iqlāb*/*ikhfāʾ* distinctions and *ghunna* timing are obligatory and fine-grained in Classical/Quranic recitation (*tajwīd*), whereas everyday MSA applies *idghām*/*iqlāb* informally and often skips the precise *ghunna* durations. Because the source IPA is pausal/caseless, word-final *tanwīn* is generally absent in the reader tiers (it is an *iʿrāb*-bearing ending dropped at pause); the *nūn-sākina* rules still apply to lexical `نْ`.

---

### Rule 8: الإعراب: حركات الإعراب (*al-iʿrāb: ḥarakāt al-iʿrāb*) — Desinential case/mood inflection (descriptive only)

*Iʿrāb* is the system of short desinential vowels (and *tanwīn*) marking **case** on nouns/adjectives and **mood** on imperfect verbs. They attach to the final consonant: e.g. *al-baytu* (nom.) / *al-bayta* (acc.) / *al-bayti* (gen.). In fully vocalized Classical Arabic every word in context carries its *iʿrāb*; in MSA they are realized in careful read/formal registers and routinely **dropped** at pause and in colloquial-influenced delivery.

**Category:** morphosyntactic / desinential inflection (**NOT emitted in source-aligned readers**)

**Desinential inflection paradigm**

| Domain | Value | Ending |
|---|---|---|
| Nominal case | nominative (رَفْع) | `-u` |
| Nominal case | accusative (نَصْب) | `-a` |
| Nominal case | genitive (جَرّ) | `-i` |
| Nominal case (indefinite *tanwīn*) | nom. / acc. / gen. | `-un` / `-an` / `-in` |
| Verbal mood | indicative | `-u` |
| Verbal mood | subjunctive | `-a` |
| Verbal mood | jussive | `-ø` / *sukūn* |

All on the word-final syllable.

**IPA example:** الوَلَدُ `/al-waladu/` `[al.wa.la.du]` 'the boy (NOM)'; الوَلَدَ `[al.wa.la.da]` '(ACC)'; الوَلَدِ `[al.wa.la.di]` '(GEN)' — same word, three case vowels. Cf. كَتَبَ الوَلَدُ *kataba l-waladu* / رَأَيْتُ الوَلَدَ *raʾaytu l-walada* / بَيْتُ الوَلَدِ *baytu l-waladi*
**IPA notation:** Nominal case: `-u` (nominative رَفْع), `-a` (accusative نَصْب), `-i` (genitive جَرّ); indefinite *tanwīn* `-un`/`-an`/`-in`. Verbal mood: `-u` (indicative), `-a` (subjunctive), `-ø`/*sukūn* (jussive).
**Environment:** Word-final position, determined by the word's syntactic role (case) or the verb's mood-governing particle. Suppressed utterance-finally by pausal rules (*waqf*).
**Register:** Classical (fully pronounced); MSA (realized in formal/read speech, dropped in pausal/colloquial delivery)

**Notes:** **Descriptive only — important for the project:** the source (Syriac/Aramaic) IPA the readers are derived from is **caseless**, and the Peshitta reader tiers are emitted in **pausal** form, so *iʿrāb* desinential vowels and indefinite *tanwīn* are **NOT emitted** in the Arabic reader tiers. They are documented here so a scholar understands what a fully-inflected *fuṣḥā* reading would add. No direct sibling equivalent in Syriac (which lost productive case); Hebrew likewise lost case but kept vestiges — Arabic uniquely preserves the full Proto-Semitic triptote system. Mark MSA vs Classical: Classical recitation pronounces *iʿrāb* medially and uses pausal forms only at stops; MSA speakers frequently apply pausal/uninflected forms much more broadly.

---

### Rule 9: الوقف: الصيغ الوقفية (*al-waqf: aṣ-ṣiyagh al-waqfiyya*) — Pausal forms (utterance-final waqf)

When an utterance or breath group **ends**, Arabic neutralizes most word-final inflectional material — the phenomenon of *waqf* ('stopping/pause'). The final short case/mood vowel is dropped; indefinite *tanwīn* is dropped (the accusative `ـً` surfacing as a long [aː] written with alif, e.g. كِتَابًا *kitāban* → [kitaːbaː] → pausal [kitaːb]); the *tāʾ marbūṭa* `ة` is read as [h] or silent rather than [t]; and certain final vowels are lengthened. This is why citation/dictionary forms look 'caseless'.

**Category:** utterance-final / prosodic neutralization (pausal)
**IPA example:** مَدِينَةٌ `/madiːnatun/` `[ma.diː.na.tun]` 'a city' in context → at pause `[ma.diː.nah]` (final *-un tanwīn* dropped; `ة` read as [h], not [t]); كِتَابٌ `/kitaːbun/` → pausal `[kitaːb]`. (مَدِينَةٌ → في الوقف مَدِينَهْ)
**IPA notation:** At pause (`#`): final short vowel → `∅` (final V deleted); *tanwīn* `-an/-in/-un` → `∅` (and `-an` → `[aː]` via alif); final `ة` *tāʾ marbūṭa* → `[h]/∅` (not [t]); some final vowels lengthened; final geminate simplified
**Environment:** Word in absolute utterance-final / breath-group-final position (before a true pause), as opposed to connected (*waṣl*) position where *iʿrāb* and *tanwīn* are realized.
**Register:** both

**Notes:** **Crucial for the project:** the Peshitta reader tiers **emit pausal forms**, which is exactly why *iʿrāb*/*tanwīn* (see previous rule) are absent — pausal *waqf* is the register that matches the caseless, utterance-final shape of the source IPA. Direct sibling of Hebrew/Aramaic pausal forms (Hebrew pausal lengthening at *silluq*/*atnaḥ*, Syriac final-vowel and final-He behavior). Note the *tāʾ-marbūṭa* → [h] pausal reading parallels Hebrew/Aramaic final ה. **Ordered last:** it counter-bleeds *iʿrāb* by deleting the very endings *iʿrāb* supplies. MSA and Classical share the mechanism; Classical/*tajwīd* codifies permissible *waqf* points and the optional final-vowel treatments (*rawm*, *ishmām*, *sukūn*) in detail.

---

*— Shin*

## MSA vs. Classical/Quranic (Register & Dialect)

Systematic differences between the two **reference standards** of literary Arabic, expressed in IPA. The two coexisting standardized systems documented here in parallel are **Modern Standard Arabic** (MSA, الفُصْحَى *al-fuṣḥā*) — the contemporary pan-Arab literary and formal-broadcast register — and **Classical / Quranic Arabic** (لُغَة القُرْآن, the careful *tajwīd* recitation register) — the older codified form preserved in scripture. Crucially, these are **NOT two dialects**: they are the same phonemic system at two registers of carefulness, much as Eastern (Madnhaya) and Western (Serto) Syriac, or General American and Received Pronunciation, are two standardized realizations rather than rival 'correct' versions. Classical/Quranic recitation realizes the FULL system — every desinential vowel (*iʿrāb*), every assimilation (*idghām*), every prescribed lengthening (*madd*) and nasal hum (*ghunna*); MSA speech typically pauses *iʿrāb* and applies *tajwīd* rules only optionally. The genuinely divergent SPOKEN vernaculars (Egyptian, Levantine, Gulf, Maghrebi, Iraqi) are documented as clearly-secondary ASIDES below and are NOT shipped reader standards, because they collapse the very contrasts (*qāf*, the interdentals, the emphatics) that make Arabic a faithful sibling-match for the Syriac/Aramaic source. Phonemic transcriptions use /slashes/ and phonetic detail uses [brackets].

### Reference standards

| Label | Standard |
|---|---|
| **MSA** | Modern Standard Arabic (الفُصْحَى *al-fuṣḥā*) — the modern pan-Arab literary standard |
| **Classical/Quranic** | Classical / Quranic Arabic (لُغَة القُرْآن) — the older codified *tajwīd* recitation register |

- **MSA:** Modern Standard Arabic (الفُصْحَى *al-fuṣḥā*) — the modern pan-Arab literary standard used in news, books, formal speech and education. Phonemically identical to Classical Arabic in its consonant and vowel inventories, but in ordinary spoken delivery it tends to drop utterance-final case/mood vowels (pausal *iʿrāb*), apply *tajwīd* assimilation/lengthening rules only loosely, and tolerate hamza simplification. The /dʒ/–[ɡ]–[ʒ] realization of `ج` and emphasis-spread are present but speaker-variable.
- **Classical/Quranic:** Classical / Quranic Arabic (لُغَة القُرْآن) — the older codified register, transmitted with the prescriptive science of تَجْوِيد *tajwīd* for Quranic recitation. It preserves every MSA contrast plus finer, rule-governed phonetic detail: fully realized *iʿrāb* in connected (*waṣl*) speech, obligatory *madd* (vowel prolongation) of fixed durations, *ghunna* (two-mora nasalization), the complete *idghām* / *ikhfāʾ* / *iqlāb* / *izhār* system for *nūn sākina* and *tanwīn*, careful hamza articulation, and conservative lexical/morphological archaisms. This is the genre-appropriate register for scripture and is the more faithful preserver of the source-language contrast set.

### Differences

| Feature | MSA | Classical/Quranic | Example | Explanation |
|---|---|---|---|---|
| *Iʿrāb* (إعْراب) — desinential case & mood vowels | Largely realized in careful reading, but routinely DROPPED in connected speech and always utterance-finally (pausal); fully voweled only in formal recitation of a written text | FULLY realized in connected (*waṣl*) recitation: every short case vowel (`ـُ` -u nominative, `ـَ` -a accusative, `ـِ` -i genitive) and mood vowel, plus *tanwīn* (nunation `ـٌ ـً ـٍ`), is pronounced when a word is joined to the next | كِتابُ اللهِ *kitābu-llāhi* 'the Book of God' — Classical/recited: /kiˈtaːbu‿lˈlaːhi/ with both case vowels sounded across the join; MSA careful pause / speech: كِتاب الله [kiˈtaːb alˈlaːh], final -u and -i dropped | The single largest register difference. Classical/Quranic recitation sounds the full system of *iʿrāb* when words are run together (*waṣl*), so grammar is audible in the vowels. MSA speakers overwhelmingly speak in pausal-like forms, dropping these endings except when reading aloud with deliberate care; the project's source IPA is itself caseless, so the Arabic guide treats *iʿrāb* as DESCRIPTIVE-ONLY and does NOT emit case vowels in the reader tiers. |
| Pausal forms (الوَقْف *al-waqf*) | Pausal stopping is the DEFAULT even mid-utterance in casual speech; final short vowels and *tanwīn* are dropped, `ـة` *tāʾ marbūṭa* → [h]/[a], accusative *tanwīn* `ـً` → long [aː] | Pause is rule-governed and reserved for prescribed stopping points (with marked *waqf* signs in the *muṣḥaf*); within a breath-group everything is joined (*waṣl*) and fully voweled; rich pausal sub-rules (*sukūn*, *rawm*, *ishmām*, *ibdāl*) at the stop | رَحْمَةٌ *raḥmatun* 'a mercy' → in pause رَحْمَه [ˈraħma(h)] (*tanwīn* gone, *tāʾ marbūṭa* → [a]/[h]); كِتابًا *kitāban* → pause كِتابا [kiˈtaːbaː] | Both registers share the same pausal machinery, but they deploy it differently. Classical recitation joins words across a verse and only applies *waqf* at sanctioned breaks, where it may use subtle devices — *rawm* (a whispered hint of the vowel) and *ishmām* (silent lip-rounding for /u/) — that ordinary MSA speech never bothers with. MSA effectively lives in pausal form most of the time. |
| *Madd* (المَدّ) — prescriptive vowel prolongation | Only the inherent two-mora length of /aː iː uː/ is observed; no extra graded lengthening | A graded system of obligatory/permissible prolongation measured in *ḥarakāt* (morae): *madd ṭabīʿī* ≈ 2, *madd muttaṣil* / *munfaṣil* ≈ 4–5, *madd lāzim* ≈ 6, applied where a long vowel meets a hamza or a *sukūn*/*shadda* | جاءَ *jāʾa* 'he came' (long ā + hamza) → recited with *madd muttaṣil* [dʒaːʔa] held ~4–5 morae; ٱلضَّآلِّينَ *aḍ-ḍāllīn* (Q1:7) → *madd lāzim* [adˤˈdˤɑːlliːn], the long ā held ~6 morae over the geminate (plain) *lām* | *Tajwīd* quantizes vowel length far beyond the binary short/long contrast of MSA. A long vowel adjacent to a hamza or to a geminate/*sukūn* is stretched to a fixed mora-count; this is purely a Classical-recitation feature, inaudible in ordinary MSA where /aː/ is simply 'long'. The reader tiers preserve only the phonemic short/long distinction, not the graded *madd*. |
| *Ghunna* (الغُنَّة) — nasalization of *nūn*/*mīm* | Plain [n]/[m]; nasal humming not systematically applied | A two-mora nasal hum [ⁿ] obligatory on a geminated `نّ` / `مّ` and on `نْ` / *tanwīn* in *idghām* and *ikhfāʾ* contexts | إِنَّ *inna* 'verily' → recited [ˈinːⁿa] with held nasal hum on `نّ`; مِن نُّورٍ *min nūrin* → *idghām* with *ghunna* [miⁿˈnuːrin] | *Ghunna* is the prescribed prolonged nasal resonance that accompanies certain *nūn* and *mīm* articulations in recitation, timed to roughly two morae. It is a hallmark of *tajwīd* and is absent as a systematic feature from MSA, where the same letters are read as plain nasals. |
| *Nūn sākina* & *tanwīn* rules — *idghām*, *ikhfāʾ*, *iqlāb*, *izhār* | *Idghām* (assimilation of the definite-article *lām* into sun letters, الشَّمْس *aš-šams*) and a few sandhi assimilations are observed; the finer *nūn*/*tanwīn* rules are largely ignored | A complete four-way system governs `نْ` and *tanwīn* before the next consonant: *izhār* (clear) before gutturals, *idghām* (assimilation, ± *ghunna*) before يرملون, *iqlāb* (`نْ` → [m]) before ب, *ikhfāʾ* (nasalized concealment) before the remaining letters | مِن بَعْدِ *min baʿdi* → *iqlāb* [mim ˈbaʕdi] (`نْ` becomes [m] before ب); مَن يَقُولُ *man yaqūlu* → *idghām* with *ghunna* [maⁿ.jaˈquːlu] | Both registers honor the sun/moon-letter behavior of the article ال (الشَّمْس *aš-šams* vs القَمَر *al-qamar*). Beyond that, Classical recitation applies the full *tajwīd* treatment of *nūn sākina* and *tanwīn* — clarity, assimilation, conversion to [m] before *bāʾ*, and nasal concealment — whereas MSA speech generally pronounces these clearly (*izhār*-like) regardless of the following letter. |
| Hamza (الهَمْزَة ء) realization | Generally a clean glottal stop [ʔ], but in fast/relaxed MSA and across *hamzat al-waṣl* it is freely softened, dropped, or replaced by compensatory lengthening / a glide | Carefully and consistently articulated as a full glottal stop [ʔ] in *taḥqīq* (precise) recitation; the prescribed *tashīl*, *ibdāl*, and *naql* variants (e.g. 'easing' a hamza to a glide-like sound) are applied only where the *qirāʾa* specifies | السَّماء *as-samāʾ* 'the sky' → Classical careful [asːaˈmaːʔ] with crisp final hamza; relaxed MSA often [asaˈmaː] with the hamza weakened; *hamzat al-waṣl* in اِسْم *ism* is elided after a vowel (وَٱسْمُهُ *wa-smuhu*) | Hamza is phonemic in both registers, but Classical recitation insists on its precise articulation (and codifies exactly when it may be eased), while MSA tolerates considerable hamza-weakening in connected speech. *Hamzat al-waṣl* (the elidable connecting hamza of the article and certain verbs/nouns) is dropped after a preceding vowel in both registers — a shared sandhi rule rather than a register difference. |
| Emphasis spread (تَفْخِيم *tafkhīm*) and *tarqīq* of /r/, /l/ | Emphatics tˤ sˤ dˤ ðˤ (and often q) pharyngealize, backing adjacent /a/ → [ɑ]; the precise extent of spread and the velarization of `رّ` / `ل` of الله is speaker-variable | *Tafkhīm* (heavy/velarized) vs *tarqīq* (light) is rule-governed for ر, for the `لـ` of اللّٰه, and for ALL emphatics, with defined trigger vowels and exact spread domains | صِراط *ṣirāṭ* 'path' → both registers [sˤɑˈrˤɑːtˤ] with backed [ɑ] throughout; اللّٰه *Allāh* → heavy [ɑlˤˈlˤɑːh] after *fatḥa*/*ḍamma* but light [alˈlaːh] after *kasra* (بِسْمِ اللّٰهِ *bismi-llāhi*) | The phonetic mechanism (pharyngealization backing neighboring vowels) is identical in both registers and matches the source's emphatic set. Classical *tajwīd*, however, codifies precisely WHEN ر is heavy or light, and when the *lām* of the divine name is velarized vs clear — distinctions MSA speakers make intuitively and inconsistently rather than by rule. |
| ج (*jīm*) realization | Standard pan-Arab MSA is the affricate [dʒ]; [ʒ] (Levantine-influenced) and [ɡ] (Egyptian-influenced) surface depending on the speaker's background | Described by the classical grammarians (Sībawayh) as a voiced PALATAL stop/affricate — the conservative reconstruction is [ɟ] (or a palatalized affricate); the Egyptian [ɡ] is one regional reflex sometimes claimed to preserve an early backed value, though this is debated and is generally analyzed as a secondary de-affrication rather than a direct retention. [dʒ] is the mainstream recited form today | رَجُل *rajul* 'man' → MSA [ˈradʒul]; Egyptian-style / archaic-leaning recitation [ˈraɡul]; some Levantine-influenced speakers [ˈraʒul] | ج is the one consonant whose very phoneme value varies across both registers and dialects. The conservative reconstruction of the historical sound is a voiced palatal [ɟ]/palatalized affricate, which fronted to the affricate [dʒ] that MSA now treats as standard; the Egyptian velar [ɡ] is a debated regional reflex (often analyzed as a secondary backing rather than a straight retention of the proto value). The source-language gap resolution maps the Syriac /ɡ/ onto ج (ɡ→ج), leaning on exactly this [ɟ]~[ɡ]~[dʒ] flexibility. |
| *Imāla* (الإمالَة) — raising of /aː/ toward [eː]/[iː] | Essentially absent; /aː/ is kept as back/open [aː]~[ɑː] | A recognized feature of certain *qirāʾāt* (notably the recitation of Ḥamza and al-Kisāʾī): a fronted/raised realization of long ā toward [eː] or [iː] in defined contexts | مَجْراها *majrāhā* (Q11:41) → recited with *imāla* as [madʒˈreːha] in the *qirāʾa* of Ḥamza, vs plain [madʒˈraːha] elsewhere | *Imāla* — the conditioned raising of /aː/ — is a Classical/dialectal phenomenon preserved in specific Quranic reading traditions and in some old poetry; MSA has standardized it out. It is mentioned here as an archaism of the Classical register; the guide's reference IPA does not apply it. |
| Lexical & morphological archaisms | Modernized vocabulary and simplified usage; rare classical particles, dual-of-verb forms, and energetic mood (*nūn al-tawkīd*) seldom appear in everyday MSA | Retains archaic lexemes, the energetic mood `ـَنَّ`/`ـَنْ` (e.g. لَيَسْجُنَنَّ *la-yusjananna*), older particle usages, and conservative orthographic-phonetic spellings (e.g. superscript dagger alif صلوٰة *ṣalāh*) | Energetic: لَنَسْفَعًا *la-nasfaʿan* (Q96:15) ends in the light energetic *nūn* read as [an]; everyday MSA would not use this mood at all | Beyond phonology, the Classical/Quranic register keeps grammatical and lexical material that MSA has largely shed — the emphatic energetic mood, certain archaic particles, and traditional spellings that carry their own recitation conventions. These are register (diachronic) differences layered atop the shared phonemic system. |

MSA (الفُصْحَى) and Classical/Quranic recitation differ most audibly in (1) *iʿrāb* — Classical recitation sounds the full system of connected case/mood endings while MSA defaults to pausal forms; (2) the *tajwīd* machinery of graded *madd*, two-mora *ghunna*, and the complete *idghām*/*ikhfāʾ*/*iqlāb*/*izhār* treatment of *nūn* and *tanwīn*, all realized in Classical recitation and applied only loosely in MSA; and (3) finer prescriptions — crisp hamza, rule-governed *tafkhīm*/*tarqīq*, and conditioned *imāla* — together with lexical/morphological archaisms preserved in the Classical register. Because the source IPA is caseless and length-binary, the reader tiers track the shared phonemic core and treat *iʿrāb*, graded *madd*, and *imāla* as descriptive-only.

### Spoken dialect asides (العامِّيَّة / اللَّهَجات)

**Status — SECONDARY / DOCUMENTED-ONLY.** The following are spoken vernaculars (العامِّيَّة *al-ʿāmmiyya* / اللَّهَجات *al-lahajāt*), NOT shipped reader standards. They are recorded here for orientation only. The Arabic Peshitta reader tiers follow *fuṣḥā* (MSA + Classical) exclusively, because every major vernacular collapses one or more of the contrasts — *qāf*, the interdentals ث/ذ/ظ, the affricate/emphatic values — that make Arabic a near-1:1 sibling match for the Syriac/Aramaic source. A single shared written *fuṣḥā* unites the Arab world, while these spoken forms are frequently mutually distant; diglossia (the coexistence of high *fuṣḥā* and low *ʿāmmiyya*) is the defining sociolinguistic fact of Arabic.

> **Note on the homeland.** Levantine is geographically the Peshitta's own homeland (Syria, Lebanon, Palestine, the Aramaic heartland), yet it is phonologically the LOSSIEST major dialect for this project: it merges *qāf* → [ʔ] and shifts the interdentals to stops, erasing the exact features that align Arabic with Syriac. Geography and faithfulness diverge — hence *fuṣḥā*, not Levantine, is the basis of the reader.

#### Vernacular reflexes by dialect

| Dialect | ق (*qāf*) | ج (*jīm*) | Interdentals ث/ذ/ظ | Notes |
|---|---|---|---|---|
| **Egyptian** (المَصْرِيَّة, Cairene) | ق → [ʔ] glottal stop in Cairene (rural/Saʿīdi keep [ɡ]) | ج → [ɡ] velar stop (the famous Cairene reflex; matches the old Classical value) | ث → [t]/[s], ذ → [d]/[z], ظ → [zˤ]/[dˤ] (interdentals lost in everyday speech) | The most widely understood vernacular thanks to Egyptian media. Its [ɡ] for ج is unique among the majors and coincides with the archaic Classical *jīm*; its [ʔ] for ق is heavily contrast-lossy. |
| **Levantine** (الشّامِيَّة; Syrian, Lebanese, Palestinian, Jordanian) | ق → [ʔ] glottal stop in urban speech (Druze and some rural retain [q]; Bedouin [ɡ]) | ج → [ʒ] voiced postalveolar fricative | ث → [t]/[s], ذ → [d]/[z], ظ → [zˤ]/[dˤ] in urban varieties (rural/Bedouin may retain interdentals) | The Aramaic homeland dialect, but phonologically lossy: urban Levantine destroys *qāf* and the interdentals, the very source-matching contrasts. Strong *imāla* (raising of final `ـة` and of /aː/) is characteristic. Documented-only — explicitly NOT a reader standard. |
| **Gulf** (الخَلِيجِيَّة; Kuwait, Bahrain, Qatar, UAE, eastern Saudi) | ق → [ɡ] (which then further affricates to [dʒ] before front vowels in some areas) | ج → [dʒ] (close to MSA), with [j] in some words | ث [θ], ذ [ð], ظ [ðˤ] are LARGELY PRESERVED — phonologically among the most conservative | Together with Najdi/Bedouin varieties, Gulf Arabic is the most conservative major group for the interdentals and for a non-glottal *qāf*; affrication of ك → [tʃ] and of *qāf*'s [ɡ] reflex → [dʒ] before front vowels (*kashkasha*/*gahawa*-type phenomena) is common. |
| **Maghrebi** (المَغْرِبِيَّة / الدّارِجة; Morocco, Algeria, Tunisia, Libya) | ق → [q] or [ɡ] depending on region/lexeme | ج → [ʒ] | ث/ذ/ظ often → stops [t]/[d]/[dˤ] in urban Morocco/Algeria; preserved in many Bedouin and Tunisian varieties | The most divergent group from MSA: heavy short-vowel reduction/deletion yields large consonant clusters, Berber (Amazigh) and Romance substrate vocabulary, and a distinctive prosody — frequently unintelligible to Mashriqi (Eastern) speakers without exposure. |
| **Iraqi** (العِراقِيَّة; Mesopotamian, esp. Baghdadi *gilit*) | ق → [ɡ] in the southern/Bedouin-derived *gilit* dialects ([q] in the northern *qeltu* dialects of Mosul and among some communities) | ج → [dʒ], with [j] in some etyma | ث [θ], ذ [ð], ظ [ðˤ] largely PRESERVED in *gilit* Iraqi | Spoken in the historic Aramaic/Mesopotamian heartland; conservative for the interdentals. Strong affrication: ك → [tʃ] and *qāf*'s [ɡ] reflex → [dʒ] before front vowels (e.g. چِان *čān* 'was'). Shows notable Aramaic/Persian/Turkish substrate influence. |

### Summary

MSA (الفُصْحَى) and Classical/Quranic Arabic are not rival dialects but two registers of one phonemic system: they share an identical consonant and vowel inventory, and differ chiefly in how MUCH of the rule-set is realized. The Classical/*tajwīd* register sounds the full machinery — connected *iʿrāb*, graded *madd*, two-mora *ghunna*, the complete *idghām*/*ikhfāʾ*/*iqlāb*/*izhār* treatment of *nūn* and *tanwīn*, crisp hamza, rule-governed *tafkhīm*/*tarqīq*, and conditioned *imāla* — plus lexical/morphological archaisms; MSA speech defaults to pausal forms, applies *tajwīd* only loosely, and modernizes the lexicon. Because the source IPA is caseless and length-binary, the reader tiers track the shared phonemic core (and treat *iʿrāb*, graded *madd*, and *imāla* as descriptive-only). The genuinely divergent SPOKEN dialects — Egyptian (ج=[ɡ], ق=[ʔ]), Levantine (ق=[ʔ], interdentals→stops), Gulf, Maghrebi, Iraqi — are mutually-distant vernaculars united only by the written *fuṣḥā*; they are documented as asides and deliberately excluded as reader standards because they collapse the *qāf*, interdental, and emphatic contrasts that make Arabic the most faithful Semitic sibling-match for the Syriac/Aramaic source.

---

*Section compiled by Shin.*

## Orthography: The Arabic Abjad

Arabic is written in the **Arabic abjad** — a consonantal, **right-to-left**, fully **cursive** script. Its 28 letters encode the consonants and the three long vowels (via *matres lectionis* `ا و ي`); the three **short** vowels and other prosodic detail are normally **unwritten**, supplied only by optional diacritics (**harakat** / *tashkīl* تشكيل) added above and below the consonantal skeleton. This makes the script an **abjad** (consonant-primary) rather than a full alphabet — the same Semitic design as its sibling scripts: the Arabic abjad أبجد is cognate, letter-for-letter and in original order, with the Hebrew אבגד and Syriac ܐܒܓܕ abjads, all descended from the Phoenician/Aramaic stock.

Unlike the Latin script (one shape per letter), Arabic is obligatorily **joined**: every letter has up to **four** contextual shapes (initial / medial / final / isolated) selected automatically by the shaping engine, and **six** letters (`ا د ذ ر ز و`) are **non-connecting** — they join to a preceding letter on their right but never to a following letter on their left, forcing a break in the cursive run. Vowels are recoverable from a known root-and-pattern lexicon, so fully vocalized text (with all harakat) is used mainly for the Quran, poetry, children's books, and pronunciation guides like this one.

The grapheme→phoneme mapping is far more transparent than English: each consonant letter maps to essentially **one** phoneme (*jīm* and the dual-role matres are the chief exceptions), and each haraka to one short vowel — Arabic spelling is close to phonemic once the harakat are supplied. The Arabic Peshitta therefore ships **both** a **vocalized** abjad tier (full harakat, near-reversible to IPA) and an **unvocalized** tier (harakat stripped, the everyday Arabic reading experience).

**Script profile:**

| Property | Value |
|---|---|
| Script type | Abjad (consonantary): consonant-primary, long vowels via matres lectionis, short vowels via optional diacritics |
| Direction | Right-to-left (RTL); digits and embedded LTR runs are bidi-isolated (RLI `U+2067` … PDI `U+2069`) |
| Cursive | Yes — obligatorily joined, four contextual shapes per letter |
| Letter count | 28 |

*Letter-count note:* The canonical alphabet is 28 letters. In the consonant table below, hamza (`ء`) and alif (`ا`) are listed as two separate entries (29 rows) for clarity, but they occupy a single alphabet slot in the classic count of 28: alif `ا` is the long-vowel/seat letter and hamza `ء` is the glottal-stop sign that rides on it (or on waw/yaa, or sits on the line). Counting alif+hamza as one yields 28.

**Reference standards:**

| Standard | Description |
|---|---|
| MSA | Modern Standard Arabic (الفُصْحَى *al-fuṣḥā*) — contemporary pan-Arab literary standard |
| Classical / Quranic | Classical / Quranic Arabic (لُغَة القُرْآن) — *tajwīd* careful-recitation register; preserves every MSA contrast plus finer orthoepic detail |

### The Two Letter Orders

Arabic has two coexisting letter orderings — the older **abjad** order (shared with Hebrew/Syriac and used for numerals/gematria) and the modern **hijāʾī** order (grouped by letter shape, used in dictionaries and spelling).

#### Hijāʾī Order (الترتيب الهجائي — *tartīb hijāʾī*)

- **Principle:** Letters grouped by **shared skeleton** (*rasm*), then disambiguated by dots: `ب ت ث ، ج ح خ ، د ذ ، ر ز ، س ش ، ص ض ، ط ظ ، ع غ ، ف ق …`
- **Order:** `ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي`
- **Use:** Modern default — dictionaries, indexes, spelling-out, alphabetization.

#### Abjad Order (الترتيب الأبجدي — *tartīb abjadī*)

- **Principle:** The original Semitic order, preserved as mnemonic nonsense-words; carries the **numerical** (gematria) values.
- **Mnemonic words:** أَبْجَدْ هَوَّزْ حُطِّي كَلَمُنْ سَعْفَصْ قَرَشَتْ ثَخَّذْ ضَظَغْ
- **Order:** `ا ب ج د ه و ز ح ط ي ك ل م ن س ع ف ص ق ر ش ت ث خ ذ ض ظ غ`
- **Use:** Numerals (abjad numerals / *ḥisāb al-jummal*), outlines (1-2-3 = أ-ب-ج), poetry, chronograms.
- **Note:** The first four mnemonic letters **ABJAD** ↔ Hebrew **אבגד** ↔ Syriac **ܐܒܓܕ** give the script family its name.

### Contextual (Positional) Forms

Arabic letters change shape by position in the cursive word. The shaping is automatic (handled by the rendering engine / Unicode bidi+joining algorithm); logical-order text stores only the base codepoints. There are four positional classes:

| Form | Arabic | When |
|---|---|---|
| Isolated | منفصلة | Standalone, or after a non-connecting letter and before a space |
| Initial | ابتدائية | First joined letter of a run (joins **left** to the next letter) |
| Medial | وسطية | Between two joining letters (joins both sides) |
| Final | نهائية | Last letter of a run (joins **right** to the previous letter) |

#### Non-Connecting Letters

There are **six** non-connecting letters: `ا` `د` `ذ` `ر` `ز` `و`.

**Rule:** These six join to a **preceding** letter (on their right) but **never** to a **following** letter (on their left). They therefore have only **two** shapes (isolated/final ≈ initial/medial) and force a visual break in the cursive run.

**Example:** دَرَس (*d-r-s*): `د` and `ر` both refuse to connect leftward, so the word shows breaks: د‧ر‧س joined only at سـ.

#### Ligatures

| Sequence | Ligature | Note |
|---|---|---|
| `ل` + `ا` | لا | Obligatory **lām-alif** ligature; an isolated/final pair, e.g. لا /laː/ 'no'. |

*Note:* Presentation-Forms ligatures (Forms-A `U+FB50–U+FDFF`, Forms-B `U+FE70–U+FEFF`) are **glyph artifacts** of shaping — they are **not** used in logical-order/stored text. اللّٰه /alˤːaːh/ has a famous calligraphic ligature (`U+FDF2`).

### Consonant Graphemes

The 28 letters in modern hijāʾī order. Each letter maps to essentially **one** consonant phoneme (near 1:1 grapheme→phoneme), with *jīm* and the dual-role matres (`و` *wāw*, `ي` *yāʾ*) the notable exceptions. Of these, ~25 match the source 34-symbol Syriac inventory directly: the pharyngeals `ح`/`ع`, emphatics `ط`/`ص`, interdentals `ث`/`ذ`/`ظ`, and `خ`/`غ`/`ق`/`ش`/`ء`. Arabic **adds** the emphatics `ض`/`ظ` (absent from the source) and **lacks** native /v p ɡ/ (resolved in the reader tier: v→`ف`, p→`ب`, ɡ→`ج`).

Hamza (`ء`) and alif (`ا`) are listed as separate rows (29 rows) but count as a single alphabet slot — see the letter-count note above. The **Hijāʾī** column gives the modern dictionary order; **Abjad #** gives the abjad numerical (gematria) value.

| Hijāʾī | Letter | Name | Transliteration | Unicode | Dec | IPA | Place | Manner | Voicing | Abjad # | Examples |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `ء` | همزة | hamza | `U+0621` | 1569 | /ʔ/ | glottal | plosive | voiceless | 1 | سَأَلَ /saʔala/ 'he asked'; قَرَأَ /qaraʔa/ 'he read' |
| 2 | `ا` | ألف | ʾalif | `U+0627` | 1575 | /aː/ (long-vowel carrier); ∅ as bearer | — | vowel carrier | — | 1 | كِتَاب /kitaːb/ 'book'; بَاب /baːb/ 'door' |
| 3 | `ب` | باء | bāʾ | `U+0628` | 1576 | /b/ | bilabial | plosive | voiced | 2 | بَيْت /bajt/ 'house'; كَلْب /kalb/ 'dog' |
| 4 | `ت` | تاء | tāʾ | `U+062A` | 1578 | /t/ | alveolar/dental | plosive | voiceless | 400 | تِين /tiːn/ 'figs'; بِنْت /bint/ 'girl' |
| 5 | `ث` | ثاء | thāʾ | `U+062B` | 1579 | /θ/ | dental (interdental) | fricative | voiceless | 500 | ثَلَاثَة /θalaːθa/ 'three'; حَدِيث /ħadiːθ/ 'speech, hadith' |
| 6 | `ج` | جيم | jīm | `U+062C` | 1580 | /dʒ/ ~ /ɡ/ ~ /ʒ/ | post-alveolar/palatal | affricate/fricative/plosive | voiced | 3 | جَمَل /dʒamal/ 'camel'; رَجُل /radʒul/ 'man' |
| 7 | `ح` | حاء | ḥāʾ | `U+062D` | 1581 | /ħ/ | pharyngeal | fricative | voiceless | 8 | حُبّ /ħubb/ 'love'; رُوح /ruːħ/ 'spirit' |
| 8 | `خ` | خاء | khāʾ | `U+062E` | 1582 | /x/ | velar/uvular | fricative | voiceless | 600 | خُبْز /xubz/ 'bread'; أَخ /ʔax/ 'brother' |
| 9 | `د` | دال | dāl | `U+062F` | 1583 | /d/ | alveolar/dental | plosive | voiced | 4 | دَار /daːr/ 'house'; وَلَد /walad/ 'boy' |
| 10 | `ذ` | ذال | dhāl | `U+0630` | 1584 | /ð/ | dental (interdental) | fricative | voiced | 700 | ذَهَب /ðahab/ 'gold'; هَذَا /haːðaː/ 'this' |
| 11 | `ر` | راء | rāʾ | `U+0631` | 1585 | /r/ | alveolar | trill | voiced | 200 | رَأْس /raʔs/ 'head'; نَهْر /nahr/ 'river' |
| 12 | `ز` | زاي | zāy | `U+0632` | 1586 | /z/ | alveolar | fricative | voiced | 7 | زَيْت /zajt/ 'oil'; أَرُزّ /ʔaruzz/ 'rice' |
| 13 | `س` | سين | sīn | `U+0633` | 1587 | /s/ | alveolar | fricative | voiceless | 60 | سَمَاء /samaːʔ/ 'sky'; شَمْس /ʃams/ 'sun' |
| 14 | `ش` | شين | shīn | `U+0634` | 1588 | /ʃ/ | post-alveolar | fricative | voiceless | 300 | شَمْس /ʃams/ 'sun'; عَيْش /ʕajʃ/ 'living, bread' |
| 15 | `ص` | صاد | ṣād | `U+0635` | 1589 | /sˤ/ | alveolar | fricative | voiceless | 90 | صَبْر /sˤabr/ 'patience'; قَصْر /qasˤr/ 'palace' |
| 16 | `ض` | ضاد | ḍād | `U+0636` | 1590 | /dˤ/ | alveolar | plosive | voiced | 800 | ضَوْء /dˤawʔ/ 'light'; أَرْض /ʔardˤ/ 'earth' |
| 17 | `ط` | طاء | ṭāʾ | `U+0637` | 1591 | /tˤ/ | alveolar | plosive | voiceless | 9 | طَيْر /tˤajr/ 'bird'; خَطّ /xatˤː/ 'line, script' |
| 18 | `ظ` | ظاء | ẓāʾ | `U+0638` | 1592 | /ðˤ/ | dental (interdental) | fricative | voiced | 900 | ظِلّ /ðˤill/ 'shade'; حَظّ /ħaðˤː/ 'luck' |
| 19 | `ع` | عين | ʿayn | `U+0639` | 1593 | /ʕ/ | pharyngeal | fricative | voiced | 70 | عَيْن /ʕajn/ 'eye, spring'; سَمِعَ /samiʕa/ 'he heard' |
| 20 | `غ` | غين | ghayn | `U+063A` | 1594 | /ɣ/ | velar/uvular | fricative | voiced | 1000 | غَيْم /ɣajm/ 'cloud'; لُغَة /luɣa/ 'language' |
| 21 | `ف` | فاء | fāʾ | `U+0641` | 1601 | /f/ | labiodental | fricative | voiceless | 80 | فَم /fam/ 'mouth'; سَيْف /sajf/ 'sword' |
| 22 | `ق` | قاف | qāf | `U+0642` | 1602 | /q/ | uvular | plosive | voiceless | 100 | قَلْب /qalb/ 'heart'; صِدْق /sˤidq/ 'truthfulness' |
| 23 | `ك` | كاف | kāf | `U+0643` | 1603 | /k/ | velar | plosive | voiceless | 20 | كَلْب /kalb/ 'dog'; مَلِك /malik/ 'king' |
| 24 | `ل` | لام | lām | `U+0644` | 1604 | /l/ | alveolar | lateral approximant | voiced | 30 | لَيْل /lajl/ 'night'; عَقْل /ʕaql/ 'mind' |
| 25 | `م` | ميم | mīm | `U+0645` | 1605 | /m/ | bilabial | nasal | voiced | 40 | مَاء /maːʔ/ 'water'; اسْم /ism/ 'name' |
| 26 | `ن` | نون | nūn | `U+0646` | 1606 | /n/ | alveolar | nasal | voiced | 50 | نَار /naːr/ 'fire'; عَيْن /ʕajn/ 'eye' |
| 27 | `ه` | هاء | hāʾ | `U+0647` | 1607 | /h/ | glottal | fricative | voiceless | 5 | هُوَ /huwa/ 'he'; وَجْه /wadʒh/ 'face' |
| 28 | `و` | واو | wāw | `U+0648` | 1608 | /w/ ~ /uː/ ~ /aw/ (diphthong) | labial-velar | approximant / vowel carrier | voiced | 6 | وَلَد /walad/ 'boy' (=/w/); نُور /nuːr/ 'light' (=/uː/); يَوْم /jawm/ 'day' (=/aw/) |
| 29 | `ي` | ياء | yāʾ | `U+064A` | 1610 | /j/ ~ /iː/ ~ /aj/ (diphthong) | palatal | approximant / vowel carrier | voiced | 10 | يَد /jad/ 'hand' (=/j/); كَبِير /kabiːr/ 'big' (=/iː/); بَيْت /bajt/ 'house' (=/aj/) |

**Per-letter notes:**

| Letter | Note |
|---|---|
| `ء` hamza | The glottal-stop letter. Independent `ء` sits **on the line** or on a seat (`أ إ ؤ ئ`); see *Hamza and Its Seats*. Not counted among the 28 'shapes' in some traditions because it rides alif/waw/yaa; abjad value is carried by its alif seat (=1). |
| `ا` ʾalif | Pure long-vowel letter /aː/ — **no** consonant value of its own. Carries hamza/madda/waṣla. Non-connecting (joins right, never left). Word-initial alif is usually a **hamza** or **waṣla** seat, not a vowel. |
| `ب` bāʾ | In the Peshitta reader tier, source /p/ (which Arabic lacks) is merged onto bāʾ. |
| `ت` tāʾ | Sun letter — assimilates the article lām (التِّين *at-tīn*). Word-final feminine /t/ is written `ة` tāʾ marbūṭa (see *Special Letters*). |
| `ث` thāʾ | Interdental, cognate with Hebrew/Syriac ת(soft)/ܬ(soft). Sun letter. Urban Levantine merges it to [t]/[s] — **not** followed here. |
| `ج` jīm | Realization varies: [dʒ] MSA standard, [ɡ] Egyptian/Classical reflex, [ʒ] Levantine. Cognate slot of Hebrew gimel ג / Syriac gamal ܓ. Receives source /ɡ/ in the Peshitta reader tier. |
| `ح` ḥāʾ | Voiceless pharyngeal — a signature Semitic consonant shared 1:1 with Hebrew ח / Syriac ܚ. Not a guttural [h]; produced deep in the throat. |
| `خ` khāʾ | Voiceless velar fricative. Cognate of the spirantized Hebrew/Syriac khaf/kaf. Distinct dotted shape from `ح` ḥāʾ and `ج` jīm (same skeleton, different dots). |
| `د` dāl | Non-connecting (joins right only). Sun letter (الدَّار *ad-dār*). |
| `ذ` dhāl | Voiced interdental, cognate Hebrew/Syriac soft dalet. Non-connecting. Sun letter. Levantine merges to [d]/[z] — not followed here. |
| `ر` rāʾ | Alveolar trill [r]; can be velarized/emphatic [rˤ] near back/emphatic vowels. Non-connecting. Sun letter (الرَّأْس *ar-raʾs*). |
| `ز` zāy | Non-connecting. Sun letter (الزَّيْت *az-zayt*). |
| `س` sīn | Plain (non-emphatic) /s/; contrasts with emphatic `ص` ṣād. Sun letter. |
| `ش` shīn | Cognate of Hebrew shin ש / Syriac shin ܫ. The article fully assimilates: الشَّمْس *aš-šams*. Sun letter. |
| `ص` ṣād | Emphatic (pharyngealized) /s/. Triggers *tafkhīm* — backs adjacent vowels (a→[ɑ]). Cognate of Hebrew/Syriac ṣade ܨ/צ. Sun letter. |
| `ض` ḍād | Emphatic /d/ — the iconic 'لُغَة الضَّاد *lughat aḍ-ḍād*' (language of the ḍād). **No** source-inventory equivalent (the 34-symbol Syriac set lacks dˤ). Sun letter. |
| `ط` ṭāʾ | Emphatic /t/. Cognate of Hebrew/Syriac ṭet ܛ/ט (one of the few emphatics shared with the source). Sun letter. |
| `ظ` ẓāʾ | Emphatic interdental /ðˤ/ (often realized [zˤ] in dialects). **No** source equivalent (Syriac set lacks ðˤ). Sun letter. Highest-numbered emphatic; abjad value 900. |
| `ع` ʿayn | Voiced pharyngeal — the most distinctively Semitic consonant; shared 1:1 with Hebrew ע / Syriac ܥ. Voiced counterpart of `ح` ḥāʾ. |
| `غ` ghayn | Voiced velar fricative; voiced counterpart of `خ` khāʾ. Highest abjad value (1000). Same skeleton as `ع` ʿayn with one dot. |
| `ف` fāʾ | Only labiodental fricative in the inventory; Arabic has **no** native /v/. Receives source /v/ (→`ف` merge) in the Peshitta reader tier. |
| `ق` qāf | Voiceless **uvular** plosive — backs adjacent vowels like an emphatic. A signature contrast lost in urban Levantine (→[ʔ]), which is why Levantine is documented-only. Cognate Hebrew/Syriac qoph ܩ/ק. |
| `ك` kāf | Plain velar /k/; contrasts with uvular `ق` qāf. Cognate Hebrew/Syriac kaph ܟ/כ. |
| `ل` lām | The article's lām assimilates to following sun letters (see *The Definite Article*). With alif forms the special ligature لا (lām-alif). Velarized [ɫ] only in the word اللّٰه /alˤːaːh/. |
| `م` mīm | Moon letter (القَمَر *al-qamar*). Cognate Hebrew/Syriac mem ܡ/מ. |
| `ن` nūn | Sun letter. Carries tanwīn (nunation) when written as ـً ـٍ ـٌ — an /n/ heard but not spelled with the letter. *Idghām* of nūn is a core tajwīd rule. |
| `ه` hāʾ | Glottal /h/ (NOT pharyngeal `ح`). Moon letter. Skeleton resembles tāʾ marbūṭa `ة` (which is hāʾ with two dots). |
| `و` wāw | Dual role: consonant /w/ **and** mater lectionis for long /uː/ and the diphthong /aw/. Non-connecting. Receives source /o/ → ḍamma/ū in the Peshitta reader tier. |
| `ي` yāʾ | 28th of the 28 alphabet letters (hamza/alif counted as one slot in the classic 28). Dual role: consonant /j/ **and** mater for long /iː/ and diphthong /aj/. Receives source /e/ → kasra/ī in the Peshitta reader tier. |

### Vowel Orthography

Arabic distinguishes three vowel **qualities** /a i u/ in two **lengths**. **Long** vowels are written into the skeleton with matres lectionis — `ا` (alif) = /aː/, `و` (wāw) = /uː/, `ي` (yāʾ) = /iː/ — and the diphthongs /aw/ /aj/ with `و`/`ي`. **Short** vowels carry no skeletal letter and are supplied only by the harakat diacritics below. The two diphthongs are spelled fatḥa+wāw (`ـَوْ` = /aw/) and fatḥa+yāʾ (`ـَيْ` = /aj/).

#### Long Vowels (Matres Lectionis)

| Vowel | Spelling | Example | Note |
|---|---|---|---|
| /aː/ | fatḥa + `ا` (alif) | بَاب /baːb/ 'door' | Also the dagger alif `ـٰ` in a few frozen words (هَٰذَا). |
| /uː/ | ḍamma + `و` (wāw) | نُور /nuːr/ 'light' | — |
| /iː/ | kasra + `ي` (yāʾ) | دِين /diːn/ 'religion' | — |

#### Diphthongs

| Diphthong | Spelling | Example |
|---|---|---|
| /aw/ | fatḥa + sukūn-wāw (`ـَوْ`) | يَوْم /jawm/ 'day' |
| /aj/ | fatḥa + sukūn-yāʾ (`ـَيْ`) | بَيْت /bajt/ 'house' |

#### Harakat (تشكيل *tashkīl*)

Optional pointing: short-vowel marks, the vowel-absence mark, the gemination mark, and the indefinite nunation (*tanwīn*). Normally omitted; written in full for scripture, pedagogy, and this guide.

| Name | Transliteration | Char | Unicode | Dec | IPA | Type | Position | Example |
|---|---|---|---|---|---|---|---|---|
| فَتْحَة | fatḥa | `َ` | `U+064E` | 1614 | /a/ | short vowel | above | كَتَبَ /kataba/ 'he wrote' |
| كَسْرَة | kasra | `ِ` | `U+0650` | 1616 | /i/ | short vowel | below | مِنْ /min/ 'from' |
| ضَمَّة | ḍamma | `ُ` | `U+064F` | 1615 | /u/ | short vowel | above | كُتُب /kutub/ 'books' |
| سُكُون | sukūn | `ْ` | `U+0652` | 1618 | ∅ (no vowel) | vowel absence marker | above | مِنْ /min/ — sukūn on nūn |
| شَدَّة | shadda | `ّ` | `U+0651` | 1617 | gemination (Cː) | consonant doubler | above | مُدَرِّس /mudarris/ 'teacher'; حَجّ /ħadʒː/ 'pilgrimage' |
| فَتْحَتَان (تَنْوِين الفَتْح) | fatḥatān / tanwīn al-fatḥ | `ً` | `U+064B` | 1611 | /an/ | nunation (indefinite) | above | شُكْرًا /ʃukran/ 'thanks' |
| كَسْرَتَان (تَنْوِين الكَسْر) | kasratān / tanwīn al-kasr | `ٍ` | `U+064D` | 1613 | /in/ | nunation (indefinite) | below | بَيْتٍ /bajtin/ 'a house (gen.)' |
| ضَمَّتَان (تَنْوِين الضَّم) | ḍammatān / tanwīn aḍ-ḍamm | `ٌ` | `U+064C` | 1612 | /un/ | nunation (indefinite) | above | بَيْتٌ /bajtun/ 'a house (nom.)' |
| أَلِف خَنْجَرِيَّة | alif khanjariyya (dagger / superscript alif) | `ٰ` | `U+0670` | 1648 | /aː/ | long-vowel diacritic | above | هَٰذَا /haːðaː/ 'this'; اللّٰه /alˤːaːh/ 'Allah' |

**Haraka notes:**

- **fatḥa** — Short open vowel /a/; backs to [ɑ] near emphatics/uvular q (*tafkhīm*); raises toward [e] in *imāla* contexts (Classical/dialectal).
- **kasra** — Short close-front /i/. Long counterpart written with yāʾ mater (`ـِي` = /iː/). Source /e/ collapses here in the reader tier.
- **ḍamma** — Short close-back rounded /u/. Long counterpart written with wāw mater (`ـُو` = /uː/). Source /o/ collapses here in the reader tier.
- **sukūn** — Marks a vowelless (coda) consonant, closing a syllable. Absence of any haraka.
- **shadda** — Doubles (geminates) the consonant; **phonemic** and contrastive (دَرَسَ *darasa* 'studied' vs دَرَّسَ *darrasa* 'taught'). Combines with a following haraka written above the shadda.
- **fatḥatān / tanwīn al-fatḥ** — Accusative indefinite nunation = vowel + unwritten /n/. Usually borne on an alif (`ـًا`). Dropped in pausal/waqf forms and not emitted in the caseless source IPA.
- **kasratān / tanwīn al-kasr** — Genitive indefinite nunation. Iʿrāb/case material — descriptive only; dropped in pause.
- **ḍammatān / tanwīn aḍ-ḍamm** — Nominative indefinite nunation. Iʿrāb/case material — descriptive only; dropped in pause.
- **alif khanjariyya** — A superscript miniature alif marking long /aː/ where no full alif is written; frozen in a small set of high-frequency words.

### Hamza and Its Seats

The glottal stop /ʔ/ is written with hamza `ء`, which is orthographically a 'rider' rather than a full skeletal letter. Its written form depends on the surrounding vowels: it sits on a **seat** (alif, wāw, or dotless yāʾ) or, in some positions, alone on the line. A separate connecting hamza — *hamzat al-waṣl* `ٱ` — is **elided** in connected speech.

| Seat | Name | Unicode | Dec | IPA | Use | Example |
|---|---|---|---|---|---|---|
| `أ` | alif with hamza above | `U+0623` | 1571 | /ʔ/ | Initial /ʔ/ with /a/ or /u/, or medial after fatḥa | أَكَلَ /ʔakala/ 'he ate' |
| `إ` | alif with hamza below | `U+0625` | 1573 | /ʔ/ | Initial /ʔ/ with /i/ (kasra) | إِبْرَة /ʔibra/ 'needle' |
| `ؤ` | wāw with hamza | `U+0624` | 1572 | /ʔ/ | Medial/final hamza when the strongest neighbouring vowel is /u/ | سُؤَال /suʔaːl/ 'question' |
| `ئ` | (dotless) yāʾ with hamza | `U+0626` | 1574 | /ʔ/ | Medial/final hamza when the strongest neighbouring vowel is /i/; connects on both sides | سَائِل /saːʔil/ 'liquid' |
| `ء` | hamza on the line (seatless) | `U+0621` | 1569 | /ʔ/ | Word-final after a long vowel/sukūn, or medial after certain long vowels | سَمَاء /samaːʔ/ 'sky' |

#### Hamzat al-Waṣl (the connecting hamza)

**Character:** `ٱ` (`U+0671`, dec 1649). **IPA:** /ʔ/ utterance-initially; ∅ (elided) in connected speech.

The 'connecting hamza' — a prosthetic glottal stop pronounced only when an utterance **begins** on it; inside a phrase it drops and the following consonant attaches to the preceding word. It heads the definite article `ال` and Form VII–X verb/derived-noun prefixes, and exists precisely because Arabic forbids word-initial consonant clusters.

**Example:** بِسْمِ ٱللَّٰه /bismi‿llaːh/ 'in the name of God' — the article's hamza is elided after بِسْمِ.

#### Madda

**Character:** `آ` (`U+0622`, dec 1570) — *alif madda*. **IPA:** /ʔaː/.

Alif with a madda (~) sign = hamza + long /aː/ (i.e. `أ` + `ا` collapsed). Written when /ʔ/ is followed by /aː/.

**Example:** آدَم /ʔaːdam/ 'Adam'. *Note:* Madda also marks /ʔ/+alif sequences to avoid two stacked alifs.

### Special Letters and Devices

Letters and orthographic devices that are not independent phonemes but carry specific reading rules.

| Device | Name | Unicode | Dec | IPA | Description |
|---|---|---|---|---|---|
| `ة` | تَاء مَرْبُوطَة (tāʾ marbūṭa) | `U+0629` | 1577 | [a]/[at] (→ /t/ in construct or before a suffix/case ending) | The 'tied tāʾ' — a hāʾ-shaped letter with two dots marking the feminine ending. Pronounced as a bare /a/ in pause, but surfaces as /t/ in *iḍāfa* (construct) or before suffixes. |
| `ى` | أَلِف مَقْصُورَة (alif maqṣūra) | `U+0649` | 1609 | /aː/ (word-final) | 'Shortened alif' — a dotless-yāʾ-shaped letter pronounced as final long /aː/. Distinguishes etymological roots; reverts to `ـا` alif before suffixes. |
| `ال` | أَل التَّعْرِيف (al-taʿrīf, the definite article) | `U+0627 U+0644` | 1575 1604 | /al/ (moon letters) ~ /aC-/ (sun letters, lām assimilated) | The prefixed definite article 'the'. See *The Definite Article* below. |
| `ـ` | تَطْوِيل / كَشِيدَة (taṭwīl / kashīda) | `U+0640` | 1600 | ∅ (no phonetic value) | An elongation glyph that stretches the joining stroke for justification/calligraphy. Purely typographic — carries no sound and is not part of the abjad; never emitted in the reader tiers. |

**Examples:**

- `ة` tāʾ marbūṭa: مَدِينَة /madiːna/ 'city' (pause) → مَدِينَةُ النَّبِيّ /madiːnatu‿n-nabijj/ 'city of the Prophet'
- `ى` alif maqṣūra: عَلَى /ʕalaː/ 'on'; مُوسَى /muːsaː/ 'Moses'
- `ـ` taṭwīl: كتاب → كــتــاب (same word, stretched)

#### The Definite Article (ال)

The prefixed definite article `ال` 'the'. Its lām is **realized** before **moon** letters (القَمَر *al-qamar*) but **assimilated** (silent, geminating the next consonant) before the 14 **sun** letters (الشَّمْس *aš-šams*). Spelled identically in both cases. The leading alif is a *hamzat al-waṣl*, elided phrase-medially.

| Class | Letters | Example |
|---|---|---|
| Sun letters (14, lām assimilated) | `ت` `ث` `د` `ذ` `ر` `ز` `س` `ش` `ص` `ض` `ط` `ظ` `ل` `ن` | الشَّمْس /aʃ-ʃams/ 'the sun' (sun letter ʃ) |
| Moon letters (lām realized /al/) | `ا(ء)` `ب` `ج` `ح` `خ` `ع` `غ` `ف` `ق` `ك` `م` `ه` `و` `ي` | القَمَر /al-qamar/ 'the moon' (moon letter q) |

### Eastern Arabic Numerals

Eastern Arabic-Indic digits used across much of the Arab East alongside the Western 'Arabic numerals' 0–9. Numbers are written **left-to-right** even inside RTL text. Range: `U+0660–U+0669`.

| Value | Glyph | Unicode | Dec | Name |
|---|---|---|---|---|
| 0 | ٠ | `U+0660` | 1632 | ARABIC-INDIC DIGIT ZERO |
| 1 | ١ | `U+0661` | 1633 | ARABIC-INDIC DIGIT ONE |
| 2 | ٢ | `U+0662` | 1634 | ARABIC-INDIC DIGIT TWO |
| 3 | ٣ | `U+0663` | 1635 | ARABIC-INDIC DIGIT THREE |
| 4 | ٤ | `U+0664` | 1636 | ARABIC-INDIC DIGIT FOUR |
| 5 | ٥ | `U+0665` | 1637 | ARABIC-INDIC DIGIT FIVE |
| 6 | ٦ | `U+0666` | 1638 | ARABIC-INDIC DIGIT SIX |
| 7 | ٧ | `U+0667` | 1639 | ARABIC-INDIC DIGIT SEVEN |
| 8 | ٨ | `U+0668` | 1640 | ARABIC-INDIC DIGIT EIGHT |
| 9 | ٩ | `U+0669` | 1641 | ARABIC-INDIC DIGIT NINE |

*Note:* The Maghreb uses the Western digits 0–9 (themselves descended from these). Distinct again are the Extended/Persian forms ۰۱۲۳ (`U+06F0–U+06F9`), **not** used for Arabic.

### Abjad Numerals (ḥisāb al-jummal)

Before positional Indic digits, letters doubled as numbers in abjad (gematria / *ḥisāb al-jummal*) order — identical in principle to Hebrew gematria and Syriac letter-numerals. Each letter's value is listed in its consonant-grapheme row above (Abjad #).

**Scheme:** Units 1–9 (`ا ب ج د ه و ز ح ط`), Tens 10–90 (`ي ك ل م ن س ع ف ص`), Hundreds 100–900 (`ق ر ش ت ث خ ذ ض ظ`), Thousand 1000 (`غ`).

**Example:** A chronogram where letter values sum to a year — the year is encoded as a phrase whose letters add up.

### Romanization Schemes

Three standard romanization schemes are shown side-by-side. **ALA-LC** and **DIN 31635** are scholarly (diacritic-based, used in libraries and linguistics); **Buckwalter** is a strict 1:1 ASCII transliteration designed for computing (each Arabic glyph ↔ one ASCII byte, fully reversible). The project's language-neutral 'Pretty' Latin tier is its own scheme (byte-identical to English) and is **not** one of these — these three are documented for reviewer cross-checking.

| Letter | IPA | ALA-LC | DIN 31635 | Buckwalter |
|---|---|---|---|---|
| `ء` | /ʔ/ | ʾ | ʾ | `'` |
| `ا` | /aː/ | ā | ā | `A` |
| `ب` | /b/ | b | b | `b` |
| `ت` | /t/ | t | t | `t` |
| `ث` | /θ/ | th | ṯ | `v` |
| `ج` | /dʒ/ | j | ǧ | `j` |
| `ح` | /ħ/ | ḥ | ḥ | `H` |
| `خ` | /x/ | kh | ḫ | `x` |
| `د` | /d/ | d | d | `d` |
| `ذ` | /ð/ | dh | ḏ | `*` |
| `ر` | /r/ | r | r | `r` |
| `ز` | /z/ | z | z | `z` |
| `س` | /s/ | s | s | `s` |
| `ش` | /ʃ/ | sh | š | `$` |
| `ص` | /sˤ/ | ṣ | ṣ | `S` |
| `ض` | /dˤ/ | ḍ | ḍ | `D` |
| `ط` | /tˤ/ | ṭ | ṭ | `T` |
| `ظ` | /ðˤ/ | ẓ | ẓ | `Z` |
| `ع` | /ʕ/ | ʿ | ʿ | `E` |
| `غ` | /ɣ/ | gh | ġ | `g` |
| `ف` | /f/ | f | f | `f` |
| `ق` | /q/ | q | q | `q` |
| `ك` | /k/ | k | k | `k` |
| `ل` | /l/ | l | l | `l` |
| `م` | /m/ | m | m | `m` |
| `ن` | /n/ | n | n | `n` |
| `ه` | /h/ | h | h | `h` |
| `و` | /w/, /uː/ | w / ū | w / ū | `w` |
| `ي` | /j/, /iː/ | y / ī | y / ī | `y` |
| `ة` | [a]/[at] | h / t | a / at | `p` |
| `ى` | /aː/ | á | ā | `Y` |
| `َ` (fatḥa) | /a/ | a | a | `a` |
| `ُ` (ḍamma) | /u/ | u | u | `u` |
| `ِ` (kasra) | /i/ | i | i | `i` |
| `ْ` (sukūn) | ∅ | (none) | (none) | `o` |
| `ّ` (shadda) | Cː | (double consonant) | (double consonant) | `~` |
| `ً` (tanwīn fatḥ) | /an/ | an | an | `F` |
| `ٌ` (tanwīn ḍamm) | /un/ | un | un | `N` |
| `ٍ` (tanwīn kasr) | /in/ | in | in | `K` |

**Notes:**

- ALA-LC and DIN 31635 differ mainly in **digraph vs diacritic** choices (th/dh/kh/sh/gh vs ṯ/ḏ/ḫ/š/ġ) and ǧ vs j for jīm.
- Buckwalter is unambiguous and reversible (one ASCII byte per glyph), trading readability for machine-tractability — note its non-letter symbols (`' * $ ~ F N K`) for hamza, dhāl, shīn, shadda and tanwīn.

### Cognate Abjad Order (Arabic · Hebrew · Syriac)

Because Arabic, Hebrew, and Syriac are Semitic siblings sharing the Phoenician/Aramaic ancestral alphabet, their abjad **order** and per-letter **numerical** values line up letter-for-letter through the first 22 positions (Hebrew and Syriac have 22 letters; Arabic kept all 22 cognates and **appended** six extra letters — `ث خ ذ ض ظ غ`, the *rawādif* — to spell sounds the 22-letter set could not, placing them at the end with values 500–1000). The shared head **ABJAD** ↔ **אבגד** ↔ **ܐܒܓܕ** names the family.

| Value | Arabic | Arabic name | Hebrew | Hebrew name | Syriac | Syriac name | IPA |
|---|---|---|---|---|---|---|---|
| 1 | `ا` | ʾalif | `א` | ʾalef | `ܐ` | ʾalaph | /ʔ/, /aː/ |
| 2 | `ب` | bāʾ | `ב` | bet | `ܒ` | beth | /b/ |
| 3 | `ج` | jīm | `ג` | gimel | `ܓ` | gamal | /dʒ/ (Heb/Syr /ɡ/) |
| 4 | `د` | dāl | `ד` | dalet | `ܕ` | dalath | /d/ |
| 5 | `ه` | hāʾ | `ה` | he | `ܗ` | he | /h/ |
| 6 | `و` | wāw | `ו` | vav | `ܘ` | waw | /w/, /uː/ |
| 7 | `ز` | zāy | `ז` | zayin | `ܙ` | zayn | /z/ |
| 8 | `ح` | ḥāʾ | `ח` | ḥet | `ܚ` | kheth | /ħ/ |
| 9 | `ط` | ṭāʾ | `ט` | ṭet | `ܛ` | ṭeth | /tˤ/ |
| 10 | `ي` | yāʾ | `י` | yod | `ܝ` | yodh | /j/, /iː/ |
| 20 | `ك` | kāf | `כ` | kaf | `ܟ` | kaph | /k/ |
| 30 | `ل` | lām | `ל` | lamed | `ܠ` | lamadh | /l/ |
| 40 | `م` | mīm | `מ` | mem | `ܡ` | mim | /m/ |
| 50 | `ن` | nūn | `נ` | nun | `ܢ` | nun | /n/ |
| 60 | `س` | sīn | `ס` | samekh | `ܣ` | semkath | /s/ |
| 70 | `ع` | ʿayn | `ע` | ʿayin | `ܥ` | ʿe | /ʕ/ |
| 80 | `ف` | fāʾ | `פ` | pe | `ܦ` | pe | /f/ (Heb/Syr /p~f/) |
| 90 | `ص` | ṣād | `צ` | tsadi | `ܨ` | ṣade | /sˤ/ |
| 100 | `ق` | qāf | `ק` | qof | `ܩ` | qoph | /q/ |
| 200 | `ر` | rāʾ | `ר` | resh | `ܪ` | resh | /r/ |
| 300 | `ش` | shīn | `ש` | shin | `ܫ` | shin | /ʃ/ |
| 400 | `ت` | tāʾ | `ת` | tav | `ܬ` | taw | /t/ |
| 500 | `ث` | thāʾ | — | (none — rādifa) | — | (none — rādifa) | /θ/ |
| 600 | `خ` | khāʾ | — | (none — rādifa) | — | (none — rādifa) | /x/ |
| 700 | `ذ` | dhāl | — | (none — rādifa) | — | (none — rādifa) | /ð/ |
| 800 | `ض` | ḍād | — | (none — rādifa) | — | (none — rādifa) | /dˤ/ |
| 900 | `ظ` | ẓāʾ | — | (none — rādifa) | — | (none — rādifa) | /ðˤ/ |
| 1000 | `غ` | ghayn | — | (none — rādifa) | — | (none — rādifa) | /ɣ/ |

*Note:* The six '*rawādif*' (`ث خ ذ ض ظ غ`) are Arabic-only additions appended after taw/tav at values 500–1000. Note the order **divergence** between the two abjad-numeral schemes: this guide uses the **Mashriqī** values (ف=80, ص=90, …, غ=1000) shown above, matching Hebrew/Syriac gematria; the **Maghrebī** abjad instead assigns ص=60, ض=90, س=300, ظ=800, غ=900, ش=1000.

### Grapheme → Phoneme Summary

Compact lookup of the regular grapheme→phoneme map. Read alongside the *Consonant Graphemes* (full detail) and *Vowel Orthography* tables above.

#### Consonant Map

| Grapheme | IPA | Grapheme | IPA |
|---|---|---|---|
| `ء/أ/إ/ؤ/ئ` | /ʔ/ | `ض` | /dˤ/ |
| `ب` | /b/ | `ط` | /tˤ/ |
| `ت` | /t/ | `ظ` | /ðˤ/ |
| `ث` | /θ/ | `ع` | /ʕ/ |
| `ج` | /dʒ/ (~[ɡ]/[ʒ]) | `غ` | /ɣ/ |
| `ح` | /ħ/ | `ف` | /f/ |
| `خ` | /x/ | `ق` | /q/ |
| `د` | /d/ | `ك` | /k/ |
| `ذ` | /ð/ | `ل` | /l/ |
| `ر` | /r/ | `م` | /m/ |
| `ز` | /z/ | `ن` | /n/ |
| `س` | /s/ | `ه` | /h/ |
| `ش` | /ʃ/ | `و` | /w/ |
| `ص` | /sˤ/ | `ي` | /j/ |
| — | — | `ة` | [a] / /t/ |
| — | — | `ى` | /aː/ |

#### Vowel Map

| Grapheme | IPA | Grapheme | IPA |
|---|---|---|---|
| `َ` (fatḥa) | /a/ | `ـَوْ` | /aw/ |
| `ِ` (kasra) | /i/ | `ـَيْ` | /aj/ |
| `ُ` (ḍamma) | /u/ | `ْ` (sukūn) | ∅ |
| `ـَا / ـٰ` | /aː/ | `ّ` (shadda) | (gemination Cː) |
| `ـِي` | /iː/ | `ً` | /an/ |
| `ـُو` | /uː/ | `ٍ` | /in/ |
| — | — | `ٌ` | /un/ |

### Unicode Blocks

Unicode ranges relevant to Arabic text in this guide.

| Range | Name | Contents |
|---|---|---|
| `U+0600–U+06FF` | Arabic | Core letters (`U+0621–U+064A`), harakat (`U+064B–U+0652`), hamza `U+0621`, alif `U+0627`, dagger alif `U+0670`, waṣla `U+0671`, Eastern digits `U+0660–U+0669`, tatweel `U+0640`. |
| `U+0750–U+077F` | Arabic Supplement | Extra letters for non-Arabic languages (not used for MSA/Classical core). |
| `U+FB50–U+FDFF` | Arabic Presentation Forms-A | Contextual/ligature glyphs incl. the Allah ligature `U+FDF2` — display artifacts, **not** used in logical-order stored text. |
| `U+FE70–U+FEFF` | Arabic Presentation Forms-B | Positional shaping glyphs and the tatweel — display artifacts, **not** used in logical-order stored text. |
| `U+2066–U+2069` | Bidi isolates | LRI/RLI/FSI/PDI; verse bodies are wrapped RLI (`U+2067`) … PDI (`U+2069`) so RTL Arabic and LTR digits/Latin sit cleanly in mixed text. |

### Reader-Tier Cross-Reference

How this orthography maps into the Arabic Peshitta reader tiers. Arabic is the most faithful / near-reversible reader tier in the project because it is a Semitic sibling of the source.

**Tiers shipped:**

1. Scholarly (IPA-anchored)
2. Pretty (language-neutral Latin, byte-identical to English)
3. Vocalized Arabic abjad (full harakat)
4. Unvocalized Arabic abjad (harakat stripped)

**Gap resolutions:**

| Gap | Resolution |
|---|---|
| v → `ف` (fāʾ) | Arabic lacks /v/; merged to /f/. |
| p → `ب` (bāʾ) | Arabic lacks /p/; merged to /b/. |
| ɡ → `ج` (jīm) | Source /ɡ/ uses the jīm slot (its Classical/Egyptian reflex is [ɡ]). |
| e → kasra / `ـِي` (ī) | Source /e/ collapses to /i/-quality, matching attested Western Syriac vocalism. |
| o → ḍamma / `ـُو` (ū) | Source /o/ collapses to /u/-quality, matching attested Western Syriac vocalism. |
| vowel length | Preserved via matres lectionis (`ا و ي`). |

**RTL handling:** Verse bodies emitted in **logical** (not visual) order and wrapped in RLI `U+2067` … PDI `U+2069` bidi isolates.

**Companion files:**

- `Arabic/arabic_pronunciation_guide.md`
- `Arabic/Peshita_Arabic/Vocalized/`
- `Arabic/Peshita_Arabic/Unvocalized/`

### Key Points

- Arabic is an **abjad**: long vowels are in the skeleton (matres `ا و ي`) but short vowels are diacritics (harakat) that are normally **omitted** — fully vocalized text is the exception (scripture, pedagogy, this guide).
- Grapheme→phoneme is near **1:1** once harakat are supplied — far more transparent than English's morphophonemic spelling; the main one-to-many letters are jīm `ج` ([dʒ]/[ɡ]/[ʒ]) and the dual-role matres `و`/`ي` (consonant vs long vowel).
- The script is obligatorily **cursive** with four contextual shapes per letter; six letters (`ا د ذ ر ز و`) are non-connecting and break the join — a feature with no Latin parallel.
- Hamza `ء` is the orthography's trickiest device: it is the /ʔ/ phoneme written on variable seats (`أ إ ؤ ئ`) or on the line, and is distinct from the **elidable** hamzat al-waṣl `ٱ` that heads the article and derived stems.
- The definite article `ال` is spelled invariantly but pronounced two ways: lām realized before **moon** letters, lām assimilated (gemination) before the 14 **sun** letters.
- Two orderings coexist: modern **hijāʾī** (shape-grouped, for dictionaries) and the original **abjad** (for numerals/gematria); the abjad order and numerical values are cognate with Hebrew and Syriac, the head ABJAD↔אבגד↔ܐܒܓܕ naming the whole family.
- Arabic's 28 letters cover ~25 of the 28 native consonants 1:1 with the source Syriac inventory (pharyngeals `ح`/`ع`, emphatics `ط`/`ص`, interdentals `ث`/`ذ`/`ظ`, plus `خ`/`غ`/`ق`/`ش`/`ء`); it **adds** emphatics `ض`/`ظ` (no source equivalent) and **lacks** /v p ɡ/ (reader-tier merges v→`ف`, p→`ب`, ɡ→`ج`).
- Eastern Arabic-Indic digits ٠–٩ (`U+0660–U+0669`) are written left-to-right even within RTL text; the Maghreb uses the Western 0–9 set descended from them.
- Iʿrāb (case/mood desinential vowels) and indefinite tanwīn ـً ـٍ ـٌ are written/described here but are **not** emitted into the IPA reader tier, which is caseless and uses pausal (waqf) forms.

---

*Authored as part of the multilingual Aramaic Pronouncement Guides project. Compiled by Shin.*

## Connected Speech & Liaison

Connected-speech and sandhi phenomena at word boundaries in Arabic — the Arabic counterpart to the English guide's *Weak Forms & Connected Speech* and to the Peshitta/Hebrew assimilation, definite-article, and pausal sub-systems. Arabic differs typologically from English here: its boundary action is **NOT** English-style vowel **reduction** (Arabic has no schwa and does not centralise unstressed vowels) but rather **liaison** (waṣl / وَصْل), **assimilation** (idghām / ikhfāʾ / iqlāb — إِدْغَام، إِخْفَاء، إِقْلَاب), the case/mood desinences (iʿrāb / إِعْرَاب) that connect words in continuous flow, and their systematic **dropping** in pause (waqf / وَقْف). Because Arabic is a Semitic sister of Syriac and Hebrew, the same processes that the Peshitta guide files under *phonological_rules* (nūn assimilation, vowel reduction in unstressed syllables) and that the Hebrew guide files under *definite_article* (article + dagesh-forte gemination) and *pausal_forms* (verse-final vowel shifts) reappear here in cognate form: Arabic sun-letter assimilation ↔ Hebrew assimilatory dagesh forte; Arabic waqf ↔ Hebrew pausal forms; Arabic nūn-sākina idghām ↔ Syriac/Hebrew nun assimilation.

**Applies to:** Continuous (connected) Arabic in both shipped reference standards. In citation/isolation a word is given its **pausal** form (final short vowel and tanwīn dropped); in continuous syntactic flow (waṣl) the full desinential vowels surface, hamzat al-waṣl elides, and the cross-boundary assimilations of the definite article and of nūn-sākina/tanwīn apply. The tajwīd assimilation rules (iẓhār, idghām, iqlāb, ikhfāʾ) are obligatory and codified in Classical/Quranic recitation and are descriptively present, more loosely, in careful MSA.

### Reference Standards

| Standard | Description |
|---|---|
| **MSA** | Modern Standard Arabic (الفُصْحَى *al-fuṣḥā*) — the contemporary pan-Arab literary standard. Liaison and sun/moon assimilation are fully active; full iʿrāb is realised in careful/formal continuous reading but is routinely dropped (pausal/colloquialised) in ordinary delivery; the finer tajwīd nūn-sākina sub-rules (ikhfāʾ, iqlāb) are observed loosely. |
| **Classical / Quranic** | Classical / Quranic Arabic (لُغَة القُرْآن, the tajwīd careful-recitation register) — preserves every MSA boundary contrast plus the fully codified nūn-sākina/tanwīn system (iẓhār ḥalqī, idghām bi-ghunna/bi-lā ghunna, iqlāb, ikhfāʾ) and the obligatory rules of waqf and ibtidāʾ (stopping and starting). This is the genre-appropriate register for scripture and is the maximal form of every rule below. |

### Contrast with English

Arabic's connected-speech engine is **liaison + assimilation + desinential (iʿrāb) connection**, NOT vowel reduction. English collapses unstressed function words onto schwa /ə/ and reshapes vowel quality at boundaries; Arabic keeps every vowel's full quality (it has only /a i u/ × length and no central reduced vowel), and instead:

- **(a)** links words by realising or eliding the connecting hamza and the case/mood vowels,
- **(b)** assimilates the lām of the article and the nūn-sākina/tanwīn to following consonants, and
- **(c)** strips final short vowels and nunation in pause.

There is therefore **no** Arabic "weak-form vs strong-form" dictionary pairing; the analogous variation is **connected (waṣl) form vs pausal (waqf) form**.

**No-schwa note:** Arabic has NO schwa /ə/ and no vowel-reduction target. The element the English guide calls the "weak vowel" has two distinct Arabic analogues:

1. The **prosthetic/connecting vowel** of hamzat al-waṣl (a default /i/, or /u/ before a stem with /u/, or /a/ on the article), which is INSERTED to satisfy the no-initial-cluster constraint and is ELIDED in continuous speech; and
2. The **desinential short vowels** of iʿrāb, which are present in continuous flow and absent in pause.

Neither is a reduction of a full vowel; both are grammatically/prosodically conditioned **presence-vs-absence** of a full short vowel.

### Boundary Phenomena

#### Waṣl liaison / hamzat al-waṣl elision (وَصْل + هَمْزَة الوَصْل)

**Category:** liaison

Arabic forbids word-initial consonant clusters, so words that begin phonologically with a cluster carry a prosthetic "connecting hamza" (hamzat al-waṣl, written `ٱ` or bare alif) plus a helping vowel that appears ONLY utterance-initially. In continuous speech, when such a word is preceded by another word, the connecting hamza and its vowel are ELIDED and the preceding word links straight onto the following consonant — the signature Arabic liaison.

**Rules:**

- Hamzat al-waṣl is pronounced (with its helping vowel) only at the START of an utterance (ibtidāʾ); medially it drops entirely.
- Helping vowel choice utterance-initially: /a/ on the definite article `ال`; /i/ as the default on Form VII/VIII/X verbs, their verbal nouns, and on nouns like `ٱبْن، ٱسْم، ٱثْنَان`; /u/ on imperatives whose stem vowel is /u/ (e.g. `ٱكْتُبْ` → `اُكْتُبْ` /uktub/).
- On elision, the final vowel of the preceding word (a case/mood desinence or a long vowel) connects directly to the first root consonant of the following word.
- If the preceding word ends in a consonant or sukūn, a liaison helping vowel (usually /i/, sometimes /a/ or /u/ by assimilation) is supplied to break the cluster created at the join (e.g. `مِنَ ٱلْبَيْت`).

| Vocalized | Romanization | IPA |
|---|---|---|
| بِسْمِ ٱللّٰهِ → بِسْمِ اللهِ | bismi (a)llāh(i) | [bis.mil.laːh] |

The /a/ of the article's hamzat al-waṣl is elided; mīm of `اسم` links straight onto the lām of `الله` (the doubled *l* in [bis.mil.laːh] is the lām-shadda true geminate /l.l/, syllabified across the boundary; the lām is light here because it follows kasra /i/ — see the **Allāh-tafkhīm** phenomenon below).

> **Note:** Utterance-initial counterpart pronounces the connecting vowel: `ٱسْم` alone = [is.mun] / pausal [ism].

**Cross-reference:** Functionally parallel to English catenation/liaison ("an apple" → [ə.ˈnæ.pl̩]) but grammaticalised: where English re-syllabifies a final consonant onto a following vowel, Arabic deletes an epenthetic onset hamza so the words fuse. Cognate to Syriac ālaph quiescence (the Peshitta guide's *Alaph quiescence*, /ʔ/ → ∅ in connected/medial position).

#### Definite-article lām assimilation: sun vs moon letters (الْحُرُوف الشَّمْسِيَّة والقَمَرِيَّة)

**Category:** assimilation

The lām of the definite article `ال` assimilates totally and regressively to a following "sun letter" (a coronal: `ت ث د ذ ر ز س ش ص ض ط ظ ل ن`), producing a geminate first consonant; before a "moon letter" (the rest: `ء ب ج ح خ ع غ ف ق ك م ه و ي`) the lām stays [l]. The article's hamzat al-waṣl is the same elidable connecting hamza, so this assimilation is itself a cross-word-boundary sandhi when the article is preceded by another word.

**Rules:**

- Before a **SUN** letter, the lām is not pronounced; the following consonant is geminated and carries shadda (e.g. `الشَّمْس` *aš-šams*).
- Before a **MOON** letter, the lām is pronounced [l] with sukūn (e.g. `الْقَمَر` *al-qamar*).
- The article vowel /a/ (its hamzat al-waṣl) surfaces only utterance-initially; medially the whole `أَل` reduces to a geminating [C(ː)] or [l] attached to the previous word.
- Sun-letter assimilation is purely orthographic-phonological gemination — it does NOT depend on iʿrāb and applies in both pausal and connected delivery.

| Letter class | Members |
|---|---|
| **Sun letters** (lām assimilates → geminate) | `ت ث د ذ ر ز س ش ص ض ط ظ ل ن` |
| **Moon letters** (lām stays [l]) | `ء ب ج ح خ ع غ ف ق ك م ه و ي` |

| Vocalized | Romanization | IPA |
|---|---|---|
| الشَّمْس | aš-šams | [aʃ.ʃams] (sun: lām → geminate ʃ) |
| القَمَر | al-qamar | [al.qa.mar] (moon: lām stays l) |

> **Note:** In continuous flow with a preceding word: `وَالشَّمْس` [waʃ.ʃams], `فِي القَمَر` [fil.qa.mar].

**Cross-reference:** Directly cognate to Hebrew's definite-article behaviour (the Hebrew guide's *definite_article*): Hebrew `הַ` + dagesh-forte geminates the following consonant just as Arabic `ال` geminates a sun letter; Arabic's moon-letter [l] retention parallels Hebrew compensatory non-gemination before gutturals/Resh. Both are assimilatory gemination triggered by the article. Compare also the Syriac/Hebrew *Assimilation of Nun* total-assimilation pattern.

#### Pausal vs connected forms — iʿrāb and tanwīn dropping in waqf (الوَقْف)

**Category:** pausal

Utterance-finally and at any licensed stopping place, Arabic takes a **PAUSAL** form: the final short desinential vowel (the case/mood iʿrāb) and the nunation (tanwīn) are dropped. In continuous flow (waṣl) those same endings are pronounced and serve to LINK the word onto the next. This presence-in-flow / absence-in-pause alternation is Arabic's structural analogue to English strong-vs-weak-form variation.

**Rules:**

- Final short vowels **-u** (nominative), **-i** (genitive), **-a** (accusative) are dropped in pause: `كِتَابٌ` *kitābun* → pausal [ki.taːb].
- Tanwīn `ـٌ` `ـٍ` is dropped in pause; accusative tanwīn `ـً` becomes a final long [aː] (the alif of tanwīn is realised): `كِتَابًا` *kitāban* → pausal [ki.taː.baː] (often written `كِتَابَا` in pause).
- Final `ة` (tāʾ marbūṭa) is pronounced [t] only in connected speech with a following vowel/desinence; in pause it becomes [h] or silent: `مَدِينَةٌ` *madīnatun* → pausal [ma.diː.nah].
- iʿrāb is **DESCRIPTIVE** here only: because the source Syriac IPA is caseless, the shipped reader tiers emit the PAUSAL (caseless) form and do not add case vowels — the connected desinences are documented, not emitted.
- Long vowels and gemination are **NOT** affected by pause; only final SHORT vowels and tanwīn are.

| Vocalized | Romanization | IPA |
|---|---|---|
| كِتَابٌ (connected) → كِتَاب (pausal) | kitābun → kitāb | [ki.taː.bun] (in flow) → [ki.taːb] (in pause) |
| رَحِيمًا → رَحِيمَا | raḥīman → raḥīmā | [ra.ħiː.man] → [ra.ħiː.maː] |

> **Note:** Genitive/nominative tanwīn vanish in pause; accusative tanwīn surfaces as final long [aː].

**Cross-reference:** The exact Semitic-sibling counterpart of the Hebrew guide's *pausal_forms* (verse-final/atnah vowel changes triggered by Silluq/Atnah). Arabic waqf **drops** endings where Hebrew pausal forms **lengthen/shift** them — both are prosodically-conditioned boundary alternations. Also the Arabic analogue of English "strong form retained utterance-finally": the stranded/final element surfaces in its citation (pausal) shape.

#### Nūn-sākina & tanwīn assimilation across boundaries: iẓhār, idghām, iqlāb, ikhfāʾ (أَحْكَام النُّون السَّاكِنَة والتَّنْوِين)

**Category:** assimilation

A vowelless nūn (`نْ`) or the /n/ of tanwīn behaves identically across a word boundary, and its realisation depends entirely on the FOLLOWING consonant. The tajwīd system codifies four behaviours: **iẓhār** (clear [n]), **idghām** (merger into the next consonant, with or without nasal hum *ghunna*), **iqlāb** (→ [m] before bāʾ), and **ikhfāʾ** (nasalised partial concealment).

| Rule | Arabic | Trigger consonants | Realisation | Example |
|---|---|---|---|---|
| **Iẓhār** | إِظْهَار | `ء ه ع ح غ خ` (six guttural/throat letters) | [n] pronounced clearly | مِنْ هَادٍ [min haːd] |
| **Idghām** | إِدْغَام | `ي ر م ل و ن` | merges into following consonant; **with ghunna** before `ي ن م و` (يَنْمُو), **without ghunna** before `ل ر` | مِن رَّبِّهِم [mir.rab.bi.him] |
| **Iqlāb** | إِقْلَاب | `ب` (bāʾ) | → [m], usually nasalised | مِنْ بَعْدِ → [mim.baʕd] |
| **Ikhfāʾ** | إِخْفَاء | remaining 15: `ت ث ج د ذ ز س ش ص ض ط ظ ف ق ك` | partly concealed (nasalised glide with ghunna, articulating toward following place) | مِنْ كُلِّ [miŋ̟.kul.li] |

**Rules (verbatim detail):**

- **IẒHĀR (إِظْهَار):** [n] pronounced clearly before the six guttural/throat letters `ء ه ع ح غ خ`. Example: `مِنْ هَادٍ` [min haːd].
- **IDGHĀM (إِدْغَام):** nūn/tanwīn merges into a following `ي ر م ل و ن`. With ghunna (nasal hum) before `ي ن م و` (يَنْمُو); without ghunna before `ل ر`. Example: `مِن رَّبِّهِم` [mir.rab.bi.him].
- **IQLĀB (إِقْلَاب):** nūn/tanwīn → [m] before bāʾ `ب`, usually nasalised. Example: `مِنْ بَعْدِ` → [mim.baʕd].
- **IKHFĀʾ (إِخْفَاء):** nūn/tanwīn is partly concealed (a nasalised glide with ghunna, articulating toward the following place) before the remaining 15 consonants (`ت ث ج د ذ ز س ش ص ض ط ظ ف ق ك`). The nasal's oral place ANTICIPATES the following consonant — it is dental before ت/د/ط, alveolar before س/ز/ص, etc. — so it is not uniformly velar; the [ŋ̟] shown is **specifically** the pre-velar realisation before /k/ and is **not** the universal ikhfāʾ symbol. Example: `مِنْ كُلِّ` [miŋ̟.kul.li] (slightly-fronted velar nasal anticipating /k/).
- These apply WITHIN a word and ACROSS the word boundary identically — the boundary is transparent to the rule.

| Vocalized | Romanization | IPA |
|---|---|---|
| مِن رَّبِّهِمْ | min rabbihim → mir-rabbihim | idghām [mir.rab.bi.him] |
| مِنْ بَعْدِ | min baʿdi → mim-baʿd | iqlāb [mim.baʕd] |
| مِنْ كُلِّ | min kulli → min(g) kulli | ikhfāʾ [miŋ̟.kul.li] |

> **Note:** All three start from the same /n/ of `مِنْ`; the following consonant alone selects idghām, iqlāb, or ikhfāʾ.

**Cross-reference:** The direct Semitic cognate of the Peshitta guide's *Assimilation of Nun* (/n/ → [C] before a following consonant) and of Hebrew nun-assimilation via dagesh forte (`מִן־` + C → geminate). Arabic refines the same inherited /n/-assimilation into a four-way tajwīd taxonomy. Functionally akin to English regressive place assimilation of final /n/ ("ten boys" → [tem]), but obligatory and codified rather than gradient.

#### Elision / shortening of short vowels in connected speech (حَذْف وقَصْر)

**Category:** elision

Beyond hamzat al-waṣl elision, Arabic drops or shortens short vowels at boundaries to repair illegal sequences and to keep the no-initial-cluster, no-overlong-cluster prosody. This is **repair-driven deletion** of a full short vowel, never centralisation/reduction.

**Rules:**

- Final long vowel SHORTENED before a following consonant cluster created at the join (iltiqāʾ al-sākinayn avoidance): `فِي الْبَيْت` /fiː/ → [fil.bajt] (long /iː/ shortened, then linked to the article).
- When two vowelless consonants would meet across the boundary (iltiqāʾ as-sākinayn), a helping /i/ (sometimes /a/, /u/) is INSERTED on the first, or the preceding long vowel is shortened, to break the cluster.
- Helping/connecting vowels are themselves elided once flow makes them unnecessary, exactly like hamzat al-waṣl.
- Vowel quality is preserved throughout: deletion and length-adjustment occur, but /a i u/ never neutralise to a central vowel.

| Vocalized | Romanization | IPA |
|---|---|---|
| فِي الْبَيْت | fī al-bayt → fil-bayt | [fil.bajt] (final /iː/ shortened + article hamza elided) |
| قَالُوا اذْهَبُوا | qālū (i)dhhabū → qālu-dhhabū | [qaː.luð.ha.buː] (final /uː/ shortened, connecting hamza of اذهبوا elided) |

> **Note:** Cluster-avoidance shortens the preceding long vowel and deletes the connecting hamza in one motion.

**Cross-reference:** Parallels English elision of schwa / cluster simplification ("last night" → [lɑːs naɪt]) in FUNCTION (repairing/streamlining the boundary) but differs in mechanism: English deletes a reduced vowel or a medial /t,d/, Arabic shortens a long vowel or supplies/deletes a helping vowel to satisfy syllable-structure constraints. Compare the Peshitta guide's *Vowel reduction in unstressed syllables* as the nearest Semitic-sibling note (though Arabic shortens rather than reduces quality).

#### Velarised lām of the name Allāh — tafkhīm of the lām in ٱللّٰه (تَفْخِيم لَام لَفْظ الجَلَالَة)

**Category:** emphasis spread

The lām of the divine name `ٱللّٰه` (Allāh) is pronounced **DARK/velarised** [lˤ] when preceded by /a/ or /u/, and **clear** [l] when preceded by /i/. This is a lexically-restricted emphasis (tafkhīm) rule operating across the word boundary onto the next word's first consonant.

**Rules:**

- After fatḥa /a/ or ḍamma /u/: the lām of Allāh is velarised [lˤ] and the following /aː/ is backed to [ɑː] — e.g. `عَبْدُ ٱللّٰه`, `قَالَ ٱللّٰه`.
- After kasra /i/: the lām is clear/light [l] and the /aː/ is front [aː] — e.g. `بِسْمِ ٱللّٰه`, `فِي ٱللّٰه`.
- The shadda on the lām is a true geminate, so the velarised form is [lˤlˤ] held long.
- This tafkhīm is specific to the word Allāh (and its connected forms `اللَّهُمَّ`); it is the most salient instance of Arabic emphasis-spread acting at a boundary.

| Vocalized | Romanization | IPA |
|---|---|---|
| عَبْدُ ٱللّٰه | ʿabdu llāh | [ʕab.dul.lˤɑːh] (after /u/ → dark lām + backed [ɑː]) |
| بِسْمِ ٱللّٰه | bismi llāh | [bis.mil.laːh] (after /i/ → light lām + front [aː]) |

> **Note:** Same word `اللّٰه`, opposite lām quality, selected purely by the preceding vowel across the boundary.

**Cross-reference:** An instance of the backbone's EMPHASIS SPREAD (tafkhīm) realised cross-boundary; no direct English counterpart (English has no pharyngealised/velarised lateral and no comparable boundary-conditioned emphasis). Conceptually closest to the Hebrew/Aramaic notion of context-sensitive consonant quality, but Arabic-specific. See this guide's *phonological_rules* (emphasis spread) for the within-word rule.

### General Rules

| Rule | Description | Example |
|---|---|---|
| **Pausal (caseless) form is the shipped/citation form** | Because the source Syriac IPA is caseless, the Arabic reader tiers emit the PAUSAL form (no final iʿrāb, no tanwīn). Continuous-flow desinences are documented but not added to the output. | `كِتَابٌ` is emitted as `كِتَاب` [ki.taːb], not [ki.taː.bun]. |
| **Hamzat al-waṣl realised only at utterance start** | The connecting hamza and its helping vowel are pronounced only in ibtidāʾ (utterance-initial). Medially they elide and the words link. | `ٱلْكِتَاب` alone = [al.ki.taːb]; in `وَٱلْكِتَاب` = [wal.ki.taːb]. |
| **Sun/moon assimilation is independent of iʿrāb and of pause** | Article lām assimilation to sun letters (gemination) and retention before moon letters apply in every register and both in pause and in flow. | `النُّور` [an.nuːr] (sun) vs `البَاب` [al.baːb] (moon), in pause or connected alike. |
| **Nūn-sākina/tanwīn rule is selected by the FOLLOWING consonant only** | iẓhār / idghām / iqlāb / ikhfāʾ depend solely on the consonant after the /n/, and apply across word boundaries identically to word-internally. | `مِنْ` before ء/ه/ع/ح/غ/خ → iẓhār [n]; before ب → iqlāb [m]; before ي ر م ل و ن → idghām; otherwise ikhfāʾ. |
| **No vowel-quality reduction at any boundary** | Arabic shortens long vowels, deletes helping/connecting vowels, and drops final short vowels in pause, but never centralises /a i u/ to a schwa. There is no Arabic "weak form" in the English sense. | `فِي الْبَيْت` shortens /iː/→/i/ to [fil.bajt]; the /i/ keeps its quality. |

### Interaction of Boundary Processes

These boundary processes **cascade and feed one another**. A single Quranic phrase can stack several:

- `مِنْ رَبِّهِمْ` in flow shows **(1)** connected-form desinences, **(2)** idghām of nūn-sākina into rāʾ → [mir.rab.bi.him], then a following article would add **(3)** sun/moon assimilation and **(4)** hamzat al-waṣl elision.
- `بِسْمِ ٱللّٰهِ الرَّحْمٰنِ الرَّحِيم` chains hamzat al-waṣl elision + sun-letter gemination (`الرَّحْمٰن`، `الرَّحِيم`) + Allāh-lām tafkhīm + final pausal dropping.

**Ordering** is generally:

1. Select connected vs pausal form
2. Resolve hamzat al-waṣl / cluster repair (shortening or helping vowel)
3. Article sun/moon assimilation
4. Nūn-sākina/tanwīn assimilation
5. Allāh-lām tafkhīm

### Register Note

Unlike English connected-speech processes, the core Arabic boundary rules are NOT gradient stylistic options: **sun/moon assimilation, hamzat al-waṣl elision, iltiqāʾ as-sākinayn repair, and waqf-dropping are obligatory in every register of fuṣḥā.** The tajwīd nūn-sākina sub-rules (ikhfāʾ, iqlāb, fine idghām) and the strict realisation of full iʿrāb in flow are maximal in the Classical/Quranic recitation register and applied more loosely (or with pausal/colloquial simplification) in everyday MSA. Speed and formality therefore shift Arabic between "fully-cased careful tajwīd" and "pausal-dominant plain MSA", **not** between strong and weak word-forms.

### Cross-Reference

This section is the Arabic counterpart to the English guide's *weak_forms_and_connected_speech*, but Arabic's boundary action is liaison + assimilation + iʿrāb, not vowel reduction — there is no schwa and no strong/weak-form pairing (the analogue is connected/waṣl vs pausal/waqf). As a Semitic SISTER of the source, Arabic's sub-systems map cognately onto the Peshitta and Hebrew guides:

| Arabic sub-system | Cognate in sibling guide |
|---|---|
| Sun-letter assimilation | Hebrew guide's *definite_article* (article + dagesh-forte gemination) |
| Waqf-dropping | Hebrew guide's *pausal_forms* (Silluq/Atnah-triggered final-vowel changes) |
| Nūn-sākina/tanwīn idghām/iqlāb/ikhfāʾ | Peshitta guide's *phonological_rules* › *Assimilation of Nun* |
| Hamzat al-waṣl elision | Peshitta guide's *Alaph quiescence* |
| Cluster-repair vowel deletion | Peshitta guide's *Vowel reduction in unstressed syllables* |

See also this guide's own *phonological_rules* (definite-article assimilation, emphasis spread, hamzat al-waṣl, pausal forms, idghām) for the word-internal statements of these same processes.

---

*Section compiled by Shin.*

## Sample Words in IPA

34 illustrative Arabic words transcribed in IPA for two reference standards — **MSA** (Modern Standard Arabic, الفُصْحَى *al-fuṣḥā*) and **Classical/Quranic** (لُغَة القُرْآن, the *tajwīd* careful-recitation register) — modeled on the Peshitta guide's parallel Eastern/Western tradition columns and the English guide's GA/RP pair. The words are chosen to exercise the full segmental inventory (all 28 consonants, the four emphatics `ط ص ض ظ`, the pharyngeals `ح ع`, the interdentals `ث ذ`, the uvular `ق`, the glottal hamza `ء`, and `ج`; all three vowel qualities short and long; both diphthongs /aj/ and /aw/), the signature phonological processes (shadda gemination, sun-vs-moon definite-article assimilation, emphasis spread / *tafkhīm*, *hamzat al-waṣl*, pausal forms), and a set of Semitic cognates shared with Hebrew and Syriac that underline Arabic's sibling relationship to the source language. Each entry lists the phonemes and features it illustrates so the array as a whole forms a verifiable coverage matrix for the Arabic phonological system.

*Words were selected illustratively (not corpus-sliced) to guarantee complete coverage: collectively they realize all 28 consonant phonemes, supply at least one keyword per vowel quality and length, instantiate both diphthongs /aj aw/, demonstrate phonemic gemination (shadda), contrast sun-letter vs moon-letter article assimilation (الشَّمْس aš-šams vs الْقَمَر al-qamar), exhibit emphasis spread from the emphatics, and include Semitic cognates (سَلَام salām ~ Heb. שלום šālōm ~ Syr. `ܫܠܡܐ` šlāmā; كِتَاب kitāb ~ Heb. כתב k-t-b ~ Syr. `ܟܬܒܐ` kṯāḇā). Arabic-script forms are given VOCALIZED (full harakat) with their unvocalized counterparts; romanization is a simplified IJMES-style transliteration (correct digraphs th/dh/sh/kh/gh and j for jīm; the definite article is assimilated before sun letters, e.g. ash-shams, final tāʾ marbūṭa is written bare -a, and final alif maqṣūra as -ā) — chosen for pedagogical clarity rather than strict ALA-LC, which retains written al- before sun letters, romanizes pausal ة as -ah, and distinguishes final ى as -á. MSA and Classical/Quranic IPA are shown in parallel; where the two registers or major realizations diverge ([dʒ]~[ɡ]~[ʒ] for ج, emphatic backing, pausal vs. context forms, ḍād history) the divergence is noted.*

*MSA is the contemporary pan-Arab literary/formal standard; Classical/Quranic is the older codified tajwīd register that preserves every MSA contrast plus finer recitational detail. The two transcriptions are nearly identical at the phonemic level — Arabic has been phonologically conservative — so divergence is mostly allophonic/realizational: `ج` (jīm) is [dʒ] in mainstream MSA but classically/Egyptian [ɡ] (and Levantine [ʒ]); pausal forms (waqf) drop final short vowels and tanwīn utterance-finally in both registers but are obligatory and elaborated in tajwīd; emphasis spread (tafkhīm) and the precise length of madd vowels are codified more strictly in Quranic recitation. Caseless source IPA means desinential iʿrāb vowels are shown in pausal (caseless) form.*

*Note on `ج` (jīm): it has three principal reflexes across the Arabic world: [dʒ] (voiced postalveolar affricate — the prestige MSA value, used here as the primary transcription), [ɡ] (voiced velar plosive — Egyptian and a widely-cited Classical value; note Arabic otherwise lacks a native /ɡ/), and [ʒ] (voiced postalveolar fricative — Levantine and much of the Maghreb). All three descend from a Proto-Semitic \*g; the source Syriac letter gāmal `ܓ` is the etymological cognate, which is why the reader-tier gap resolution maps source /ɡ/ → ج.*

**Total sample words:** 34

| Word (vocalized) | Unvocalized | Romanization | MSA | Classical/Quranic | Gloss | Phonemes | Features |
|---|---|---|---|---|---|---|---|
| سَلَام | سلام | salām | `/saˈlaːm/` | `/saˈlaːm/` | peace; greeting | `s a l aː m` | Plain alveolar /s/ (NOT the emphatic ص), short /a/, long /aː/ via alif as mater lectionis, final /m/. SEMITIC COGNATE: triliteral root س-ل-م ~ Hebrew שלום (šālōm) ~ Syriac `ܫܠܡܐ` (šlāmā ~ shlama) — the classic sibling-language greeting, a near-perfect cognate set across all three Central Semitic sisters. |
| كِتَاب | كتاب | kitāb | `/kiˈtaːb/` | `/kiˈtaːb/` | book | `k i t aː b` | Voiceless velar /k/, short /i/ (kasra), long /aː/, plain dental /t/ + voiced /b/. SEMITIC COGNATE: root ك-ت-ب 'write' ~ Hebrew כתב (k-t-b) ~ Syriac `ܟܬܒܐ` (kṯāḇā 'book') — a templatic CiCāC pattern shared across the family; cf. the Peshitta guide's headword `ܟܬܒܐ`. |
| بَيْت | بيت | bayt | `/bajt/` | `/bajt/` | house | `b aj t` | DIPHTHONG /aj/ (fatḥa + yāʾ with sukūn) — one of Arabic's two diphthongs; CVCC syllable. SEMITIC COGNATE: ~ Hebrew בית (bayit) ~ Syriac `ܒܝܬܐ` (baytā). In many dialects /aj/ monophthongizes to [eː], but MSA and Classical keep the true diphthong. |
| يَوْم | يوم | yawm | `/jawm/` | `/jawm/` | day | `j aw m` | Palatal glide /j/ (yāʾ) onset + DIPHTHONG /aw/ (fatḥa + wāw with sukūn) — Arabic's second diphthong; CVCC. SEMITIC COGNATE: ~ Hebrew יום (yōm) ~ Syriac `ܝܘܡܐ` (yawmā). Dialectally /aw/ → [oː]. |
| نُور | نور | nūr | `/nuːr/` | `/nuːr/` | light | `n uː r` | Nasal /n/ onset + LONG /uː/ (ḍamma + wāw as mater lectionis) + trilled /r/. Exemplifies the long-back rounded vowel. SEMITIC COGNATE: ~ Hebrew נר (nēr 'lamp'), Syriac `ܢܘܗܪܐ` (nuhrā). Contrast vowel length with short /u/ in كُتُب below. |
| كُتُب | كتب | kutub | `/ˈkutub/` | `/ˈkutub/` | books (plural) | `k u t u b` | Two SHORT /u/ vowels (ḍamma) — the broken-plural CuCuC pattern of كِتَاب; minimal length contrast with نُور /uː/. All-short, light-syllable word showing predictable initial stress. |
| بِنْت | بنت | bint | `/bint/` | `/bint/` | girl; daughter | `b i n t` | SHORT /i/ (kasra) in a closed CVCC syllable; final consonant cluster /nt/. SEMITIC COGNATE: ~ Hebrew בת (bat) ~ Syriac `ܒܪܬ` (bart) — feminine of 'son'. Demonstrates the short high-front vowel and Arabic coda clustering. |
| حُبّ | حب | ḥubb | `/ħubb/` | `/ħubb/` | love | `ħ u b` | PHARYNGEAL /ħ/ (ḥāʾ — voiceless pharyngeal fricative) onset + GEMINATED /bb/ marked by shadda (phonemic gemination). Two signature Arabic features in one short word: the guttural ḥ and contrastive consonant length. |
| عَيْن | عين | ʿayn | `/ʕajn/` | `/ʕajn/` | eye; spring (of water) | `ʕ aj n` | PHARYNGEAL /ʕ/ (ʿayn — voiced pharyngeal fricative/approximant) onset + diphthong /aj/. SEMITIC COGNATE: ~ Hebrew עין (ʿáyin) ~ Syriac `ܥܝܢܐ` (ʿaynā). The letter ʿayn is also the namesake of العَرَبِيَّة al-ʿarabiyya. |
| ثَلَاثَة | ثلاثة | thalātha | `/θaˈlaːθa/` | `/θaˈlaːθatun/` | three | `θ a l aː` | INTERDENTAL /θ/ (thāʾ — voiceless interdental fricative) appearing TWICE; long /aː/. SEMITIC COGNATE: ~ Hebrew שלוש (šālōš) ~ Syriac `ܬܠܬܐ` (tlāṯā). PAUSAL vs CONTEXT: tāʾ marbūṭa ة is pausal [a] in MSA but recited with full tanwīn [-atun] in careful Classical — hence the register split in the IPA. |
| ذَهَب | ذهب | dhahab | `/ˈðahab/` | `/ˈðahab/` | gold | `ð a h a b` | INTERDENTAL /ð/ (dhāl — voiced interdental fricative) onset + glottal /h/ (hāʾ, distinct from pharyngeal ħ). SEMITIC COGNATE: ~ Hebrew זהב (zāhāv, with the regular Hebrew ð→z shift) ~ Syriac `ܕܗܒܐ` (dahbā, with d). A clean three-way illustration of how the sisters reflect Proto-Semitic \*ḏ. |
| ظِلّ | ظل | ẓill | `/ðˤɪlː/` | `/ðˤɪlː/` | shade; shadow | `ðˤ i l` | EMPHATIC INTERDENTAL /ðˤ/ (ẓāʾ — pharyngealized voiced interdental fricative, the rarest Arabic phoneme) + GEMINATED /ll/ (shadda). EMPHASIS SPREAD backs the /i/ to [ɪ]~[ɨ] adjacent to the emphatic. ẓāʾ has no counterpart in the source 34-symbol Syriac inventory (which lacks dˤ ðˤ). |
| صَبْر | صبر | ṣabr | `/sˤɑbr/` | `/sˤɑbr/` | patience | `sˤ a b r` | EMPHATIC /sˤ/ (ṣād — pharyngealized voiceless alveolar fricative) onset. EMPHASIS SPREAD (tafkhīm): the /a/ backs to [ɑ] throughout the syllable. Minimal contrast with plain /s/ in سَلَام (salām) above — the ص~س pair is one of Arabic's defining emphatic contrasts and matches the source's ṣ. |
| ضَيْف | ضيف | ḍayf | `/dˤɑjf/` | `/dˤɑjf/` | guest | `dˤ aj f` | EMPHATIC /dˤ/ (ḍād — pharyngealized voiced alveolar stop) + diphthong /aj/ (backed by emphasis to [ɑj]) + labiodental /f/. ḍād is so iconic that Arabic is called لُغَة الضَّاد lughat aḍ-ḍād 'the language of the ḍād'; classically it was a pharyngealized lateral, now a plain emphatic stop. No /dˤ/ in the source inventory. |
| طَرِيق | طريق | ṭarīq | `/tˤɑˈriːq/` | `/tˤɑˈriːq/` | road; path | `tˤ a r iː q` | EMPHATIC /tˤ/ (ṭāʾ — pharyngealized voiceless alveolar stop) onset with EMPHASIS SPREAD backing /a/→[ɑ]; long /iː/; UVULAR /q/ (qāf) coda. Two of Arabic's signature backed consonants (ṭ and q) in one word; ṭāʾ matches the source's ṭ. |
| قَلْب | قلب | qalb | `/qalb/` | `/qalb/` | heart | `q a l b` | UVULAR /q/ (qāf — voiceless uvular plosive) onset. SEMITIC COGNATE: ~ Hebrew לב (lev 'heart', root l-b-b) ~ Syriac `ܠܒܐ` (lebbā) — only a partial match: the Hebrew/Syriac 'heart' words share the l-b core but lack the qāf, while Arabic preserves the full triliteral root q-l-b (no clean three-way q-l-b cognate). NOTE: urban Levantine collapses qāf→[ʔ] (qalb→[ʔalb]), which is exactly why Levantine is documented-only here — preserving /q/ keeps the contrast with the source's qōp. |
| خُبْز | خبز | khubz | `/xubz/` | `/xubz/` | bread | `x u b z` | VOICELESS VELAR/UVULAR FRICATIVE /x/ (khāʾ) onset + voiced alveolar fricative /z/ coda. SEMITIC COGNATE NETWORK: /x/ corresponds to Syriac soft kāp and Hebrew khaf; matches the source's x. Final cluster /bz/. |
| غُرْفَة | غرفة | ghurfa | `/ˈɣurfa/` | `/ˈɣurfatun/` | room | `ɣ u r f` | VOICED VELAR/UVULAR FRICATIVE /ɣ/ (ghayn) onset — the voiced partner of خ /x/ + labiodental /f/. Matches the source's ɣ (Syriac soft gāmal). Tāʾ marbūṭa ة: pausal [a] (MSA) vs full [-atun] in Classical recitation. |
| جَمَل | جمل | jamal | `/ˈdʒamal/` | `/ˈdʒamal/ ~ /ˈɡamal/` | camel | `dʒ a m l` | ج (jīm): [dʒ] in mainstream MSA, classically/Egyptian [ɡ], Levantine [ʒ] — see the jīm note above. SEMITIC COGNATE: ~ Hebrew גמל (gāmāl) ~ Syriac `ܓܡܠܐ` (gamlā) — the Hebrew/Syriac /ɡ/ reflex underlies the reader-tier mapping source ɡ→ج. The same root also names the abjad letter (gīmel/gāmal/jīm). |
| أَب | أب | ab | `/ʔab/` | `/ʔabun/` | father | `ʔ a b` | GLOTTAL STOP /ʔ/ (hamza, here on an alif seat أ) — every Arabic word that 'begins with a vowel' actually begins with hamza. SEMITIC COGNATE: ~ Hebrew אב (ʾāv) ~ Syriac `ܐܒܐ` (abā). Pausal /ʔab/ (MSA) vs nominative /ʔabun/ (Classical context). |
| سُؤَال | سؤال | suʾāl | `/suˈʔaːl/` | `/suˈʔaːl/` | question | `s u ʔ aː l` | MEDIAL HAMZA /ʔ/ on a wāw seat (ؤ), demonstrating hamza's seat-variant orthography; short /u/ + long /aː/. Shows that hamza is a full consonant intervocalically, not merely a vowel onset. |
| الشَّمْس | الشمس | ash-shams | `/aʃˈʃams/` | `/aʃʃamsu/` | the sun | `ʃ a m s` | SUN LETTER assimilation: definite article ال + ش — the lām is NOT pronounced; instead the ش geminates ([aʃʃams], shadda on the šīn). Postalveolar /ʃ/ (šīn) ~ Hebrew/Syriac šin. The canonical sun-letter exemplar (الشَّمْس aš-šams). Contrast with الْقَمَر below. |
| الْقَمَر | القمر | al-qamar | `/alˈqamar/` | `/alqamaru/` | the moon | `a l q m r` | MOON LETTER (non-assimilating): definite article ال + ق — the lām /l/ IS pronounced ([al-qamar]), no gemination. The canonical moon-letter exemplar (الْقَمَر al-qamar), the textbook minimal pair with الشَّمْس aš-šams for the sun/moon rule. |
| اِبْن | ابن | ibn | `/ibn/` | `/ibnun/` | son | `i b n` | HAMZAT AL-WAṢL: the initial alif carries an elidable connecting hamza (waṣla), pronounced [ʔibn] utterance-initially but elided after a preceding vowel (e.g. أَبُو بْن abū bn). SEMITIC COGNATE: ~ Hebrew בן (bēn) ~ Syriac `ܒܪܐ` (brā). Illustrates Arabic's ban on word-initial clusters. |
| مُعَلِّم | معلم | muʿallim | `/muˈʕallim/` | `/muˈʕallimun/` | teacher | `m u ʕ a l i` | PHARYNGEAL /ʕ/ (ʿayn) medially + GEMINATED /ll/ (shadda) — the Form II فَعَّل faʿʿala active-participle pattern, whose doubled middle radical is exactly where gemination lives. Combines a guttural with phonemic length. |
| اللّٰه | الله | Allāh | `/ɑlˤˈlˤɑːh/` | `/ɑlˤˈlˤɑːh/` | God | `l aː h` | The DARK (velarized/emphatic) /lˤ/ of the divine name — the one lexical item where lām is pronounced emphatic [lˤ] after /a/ or /u/, backing the vowel to [ɑ]; geminated (shadda). Final /h/ (hāʾ). SEMITIC COGNATE: ~ Hebrew אלוה/אל (ʾēl, ʾelōah) ~ Syriac `ܐܠܗܐ` (alāhā). A famous emphasis/idgham showcase in tajwīd. |
| مَاء | ماء | māʾ | `/maːʔ/` | `/maːʔ/` | water | `m aː ʔ` | Long /aː/ + WORD-FINAL HAMZA /ʔ/ (on the line, after alif). SEMITIC COGNATE: ~ Hebrew מים (máyim) ~ Syriac `ܡܝܐ` (mayyā). Demonstrates phonemic final glottal stop, often weakened in casual speech but firm in Classical recitation. |
| رَأْس | رأس | raʾs | `/raʔs/` | `/raʔsun/` | head | `r a ʔ s` | Trilled /r/ onset + SYLLABLE-CODA HAMZA /ʔ/ (on alif seat أ with sukūn) + plain /s/. SEMITIC COGNATE: ~ Hebrew ראש (rōš) ~ Syriac `ܪܫܐ` (rēšā). Shows hamza closing a syllable medially. |
| شَجَرَة | شجرة | shajara | `/ˈʃadʒara/` | `/ˈʃadʒaratun/` | tree | `ʃ a dʒ r` | Postalveolar /ʃ/ (šīn) + ج (jīm) in the same word; three light /a/ syllables (the CaCaCa noun pattern). Tāʾ marbūṭa ة: pausal [a] (MSA) vs [-atun] (Classical). Pairs šīn with jīm for the two postalveolar letters. |
| زَيْتُون | زيتون | zaytūn | `/zajˈtuːn/` | `/zajˈtuːn/` | olives | `z aj t uː n` | Voiced /z/ (zāy) onset + diphthong /aj/ + long /uː/ in the same word — a compact vowel showcase. SEMITIC COGNATE: ~ Hebrew זית (záyit) ~ Syriac `ܙܝܬܐ` (zaytā). |
| فَجْر | فجر | fajr | `/fadʒr/` | `/fadʒr/` | dawn | `f a dʒ r` | Labiodental /f/ onset + ج (jīm) + final /dʒr/~/ɡr/ cluster. NOTE for the reader tier: Arabic natively lacks /v/ and /p/ — /f/ here is the merge target for source /v/→ف and /p/→ب in the Peshitta Arabic reader. Contrasts the affricate ج with the fricative ف. |
| هُدَى | هدى | hudā | `/huˈdaː/` | `/huˈdaː/` | guidance | `h u d aː` | Glottal /h/ (hāʾ — distinct from pharyngeal ħ) onset + voiced dental /d/ + final long /aː/ written with alif maqṣūra ى (dotless yāʾ functioning as a mater for /aː/). Shows the alif-maqṣūra spelling of word-final /aː/. |
| وَرْد | ورد | ward | `/ward/` | `/wardun/` | roses; flowers | `w a r d` | Labial-velar approximant /w/ (wāw as consonant, not mater) onset + trilled /r/ + voiced dental /d/. SEMITIC COGNATE: ~ Hebrew ורד (wéred) ~ Syriac `ܘܪܕܐ` (wardā). Demonstrates wāw's consonantal value (vs its mater role in نُور nūr). |
| كَلْب | كلب | kalb | `/kalb/` | `/kalbun/` | dog | `k a l b` | Voiceless velar /k/ onset — a MINIMAL PAIR with قَلْب (qalb, 'heart') above isolating the /k/ (velar) vs /q/ (uvular) contrast, one of Arabic's defining back-consonant oppositions and a faithful match for the source's kāp~qōp distinction. SEMITIC COGNATE: ~ Hebrew כלב (kélev) ~ Syriac `ܟܠܒܐ` (kalbā). |

### Coverage Matrix

*Verification matrix: every cell below is exemplified by at least one word in the array above. Together the 34 words realize all 28 consonants, all six vowel phonemes (three qualities × two lengths), both diphthongs, and every signature phonological process named in the canonical backbone.*

#### Consonants Covered

All 28 consonant phonemes, each with the sample word(s) that realize it.

| Letter (phoneme) | Exemplified by |
|---|---|
| `ء` (/ʔ/ hamza) | أَب (ab, initial seat), سُؤَال (suʾāl, wāw seat), مَاء (māʾ, final), رَأْس (raʾs, coda) |
| `ب` (/b/) | كِتَاب (kitāb), بَيْت (bayt), حُبّ (ḥubb) |
| `ت` (/t/) | كِتَاب (kitāb), بَيْت (bayt), زَيْتُون (zaytūn) |
| `ث` (/θ/) | ثَلَاثَة (thalātha, ×2) |
| `ج` (/dʒ~ɡ~ʒ/) | جَمَل (jamal), شَجَرَة (shajara), فَجْر (fajr) |
| `ح` (/ħ/ pharyngeal) | حُبّ (ḥubb) |
| `خ` (/x/) | خُبْز (khubz) |
| `د` (/d/) | هُدَى (hudā), وَرْد (ward) |
| `ذ` (/ð/ interdental) | ذَهَب (dhahab) |
| `ر` (/r/) | نُور (nūr), طَرِيق (ṭarīq), رَأْس (raʾs), وَرْد (ward) |
| `ز` (/z/) | خُبْز (khubz), زَيْتُون (zaytūn) |
| `س` (/s/ plain) | سَلَام (salām), سُؤَال (suʾāl), الشَّمْس (ash-shams) |
| `ش` (/ʃ/) | الشَّمْس (ash-shams), شَجَرَة (shajara) |
| `ص` (/sˤ/ emphatic) | صَبْر (ṣabr) |
| `ض` (/dˤ/ emphatic) | ضَيْف (ḍayf) |
| `ط` (/tˤ/ emphatic) | طَرِيق (ṭarīq) |
| `ظ` (/ðˤ/ emphatic interdental) | ظِلّ (ẓill) |
| `ع` (/ʕ/ pharyngeal) | عَيْن (ʿayn), مُعَلِّم (muʿallim) |
| `غ` (/ɣ/) | غُرْفَة (ghurfa) |
| `ف` (/f/) | ضَيْف (ḍayf), غُرْفَة (ghurfa), فَجْر (fajr) |
| `ق` (/q/ uvular) | طَرِيق (ṭarīq), قَلْب (qalb), الْقَمَر (al-qamar) |
| `ك` (/k/) | كِتَاب (kitāb), كُتُب (kutub), كَلْب (kalb — minimal pair with قَلْب qalb) |
| `ل` (/l/) | سَلَام (salām), قَلْب (qalb), ظِلّ (ẓill), مُعَلِّم (muʿallim), اللّٰه (Allāh) |
| `م` (/m/) | سَلَام (salām), يَوْم (yawm), جَمَل (jamal) |
| `ن` (/n/) | نُور (nūr), بِنْت (bint), عَيْن (ʿayn) |
| `ه` (/h/ glottal) | ذَهَب (dhahab), اللّٰه (Allāh), هُدَى (hudā) |
| `و` (/w/ consonant) | وَرْد (ward); as mater in نُور (nūr), يَوْم (yawm) |
| `ي` (/j/ consonant) | يَوْم (yawm); in diphthong بَيْت (bayt), عَيْن (ʿayn), ضَيْف (ḍayf), زَيْتُون (zaytūn) |

#### Vowels Covered

All six vowel phonemes (three qualities × two lengths).

| Vowel | Exemplified by |
|---|---|
| /a/ (short, fatḥa) | سَلَام, ذَهَب, قَلْب, جَمَل |
| /i/ (short, kasra) | كِتَاب, بِنْت, ظِلّ |
| /u/ (short, ḍamma) | كُتُب, حُبّ, خُبْز, غُرْفَة |
| /aː/ (long, alif) | سَلَام, كِتَاب, ثَلَاثَة, مَاء; alif maqṣūra ى in هُدَى |
| /iː/ (long, yāʾ) | طَرِيق |
| /uː/ (long, wāw) | نُور, زَيْتُون |

#### Diphthongs Covered

| Diphthong | Exemplified by |
|---|---|
| /aj/ (ay) | بَيْت (bayt), عَيْن (ʿayn), ضَيْف (ḍayf), زَيْتُون (zaytūn) |
| /aw/ (aw) | يَوْم (yawm) |

#### Phonological Processes Demonstrated

| Process | Exemplified by |
|---|---|
| Gemination (shadda, phonemic) | حُبّ (ḥubb /bb/), ظِلّ (ẓill /ll/), مُعَلِّم (muʿallim /ll/), اللّٰه (Allāh /lˤlˤ/), الشَّمْس (ash-shams /ʃʃ/ via assimilation) |
| Sun-letter assimilation | الشَّمْس (aš-šams — lām assimilates, ش geminates) |
| Moon-letter (non-assimilation) | الْقَمَر (al-qamar — lām pronounced) |
| Emphasis spread (tafkhīm) | صَبْر (ṣabr), ضَيْف (ḍayf), طَرِيق (ṭarīq), ظِلّ (ẓill), اللّٰه (Allāh) — adjacent /a i/ back to [ɑ ɪ] |
| Hamzat al-waṣl (elidable connecting hamza) | اِبْن (ibn) |
| Pausal vs context forms (waqf / iʿrāb) | أَب (ab~abun), وَرْد (ward~wardun), tāʾ marbūṭa words ثَلَاثَة/غُرْفَة/شَجَرَة ([a] pausal vs [-atun] context) |
| Matres lectionis (long-vowel spelling) | alif in سَلَام/كِتَاب, wāw in نُور, yāʾ in طَرِيق, alif maqṣūra in هُدَى |
| Hamza seat variants | أ in أَب/رَأْس, ؤ in سُؤَال, standalone ء in مَاء |

#### Register Divergences Illustrated

- `ج` realization [dʒ] (MSA) ~ [ɡ] (Classical/Egyptian) ~ [ʒ] (Levantine): جَمَل (jamal)
- Pausal vs full-vowel/tanwīn endings (waqf): ثَلَاثَة (thalātha~thalāthatun), أَب (ab~abun), وَرْد (ward~wardun)
- Qāf preserved as /q/ (vs Levantine [ʔ] collapse, documented-only): قَلْب (qalb), الْقَمَر (al-qamar)
- Emphatic backing codified more strictly in tajwīd: صَبْر, طَرِيق, اللّٰه

#### Semitic Cognates with Hebrew and Syriac

| Arabic ~ Hebrew ~ Syriac | Gloss |
|---|---|
| سَلَام salām ~ שלום šālōm ~ `ܫܠܡܐ` šlāmā | peace |
| كِتَاب kitāb ~ כתב k-t-b ~ `ܟܬܒܐ` kṯāḇā | book / write (root) |
| بَيْت bayt ~ בית bayit ~ `ܒܝܬܐ` baytā | house |
| يَوْم yawm ~ יום yōm ~ `ܝܘܡܐ` yawmā | day |
| عَيْن ʿayn ~ עין ʿayin ~ `ܥܝܢܐ` ʿaynā | eye / spring |
| ثَلَاثَة thalātha ~ שלוש šālōš ~ `ܬܠܬܐ` tlāṯā | three |
| ذَهَب dhahab ~ זהב zāhāv ~ `ܕܗܒܐ` dahbā | gold (Proto-Semitic \*ḏ reflexes) |
| جَمَل jamal ~ גמל gāmāl ~ `ܓܡܠܐ` gamlā | camel (the \*g reflex behind ج) |
| أَب ab ~ אב ʾāv ~ `ܐܒܐ` abā | father |
| اِبْن ibn ~ בן bēn ~ `ܒܪܐ` brā | son |
| مَاء māʾ ~ מים máyim ~ `ܡܝܐ` mayyā | water |
| رَأْس raʾs ~ ראש rōš ~ `ܪܫܐ` rēšā | head |
| زَيْتُون zaytūn ~ זית záyit ~ `ܙܝܬܐ` zaytā | olive |
| وَرْد ward ~ ורד wéred ~ `ܘܪܕܐ` wardā | rose |
| كَلْب kalb ~ כלב kélev ~ `ܟܠܒܐ` kalbā | dog |
| اللّٰه Allāh ~ אלוה ʾelōah ~ `ܐܠܗܐ` alāhā | God |

#### Source-Inventory Gaps Noted

- **Phonemes Arabic has but the source lacks:** dˤ (ضَيْف ḍayf) and ðˤ (ظِلّ ẓill) — the source 34-symbol Syriac inventory has tˤ sˤ but not these two emphatics.
- **Phonemes the source has but Arabic lacks (reader-tier merges):** v→ف and p→ب (Arabic has neither natively; cf. ف in فَجْر/ضَيْف/غُرْفَة and ب throughout); source ɡ realized via ج (جَمَل jamal).

---

*Compiled by Shin.*

## Unicode Reference

Unicode codepoint reference for every symbol used throughout this Arabic pronunciation guide: the IPA phonetic alphabet (consonants, vowels, diacritics, suprasegmentals) used to transcribe Modern Standard Arabic (MSA) and Classical/Quranic Arabic, **and** the Arabic abjad itself (28 consonantal letters `U+0621`–`U+064A`, the harakat/tashkīl marks `U+064B`–`U+0652`, plus the Unicode blocks, bidi-isolate controls, and Eastern Arabic-Indic digits that the Peshitta reader tiers rely on). Each entry gives the symbol/character, its Unicode codepoint (`U+XXXX`), decimal value, official Unicode character name, and its phonetic or orthographic role. Arabic being a Central-Semitic **sister** of the source language (Syriac/Aramaic) and of Hebrew, the abjad here is genealogically cognate with the source's script (ابجد ↔ Syriac ܐܒܓܕ ↔ Hebrew אבגד); cross-references to those sister blocks are noted. All IPA codepoints follow the IPA 2015 conventions; verify rendering of IPA with a font such as Charis SIL, Doulos SIL, or Gentium, and of the Arabic with a font such as Amiri, Scheherazade New, or Noto Naskh Arabic.

### IPA Consonant Symbols

IPA symbols for the 28 Arabic consonant phonemes plus key allophonic/dialectal realizations. Plain consonants (b t d z s f k l m n h w j) reuse Basic Latin letters; the Semitic-signature symbols — pharyngeals ħ ʕ, the velars/uvulars x ɣ q, the post-alveolar ʃ, the interdentals θ ð, and the glottal ʔ — are drawn from IPA Extensions, the Pharyngeal/Glottal letters, Greek (θ), and Latin-1 Supplement (ð). The four **emphatic** (pharyngealized) consonants tˤ sˤ dˤ ðˤ are written as a plain base letter plus the pharyngealization modifier ˤ (`U+02E4`), documented under diacritics. ج (jīm) is given as `[dʒ]` (MSA digraph), with `[ɡ]` (Egyptian/Classical) and `[ʒ]` (Levantine) as variants. Arabic has **no** native /v p ɡ/ (these surface only in loanwords / as ج's `[ɡ]` realization).

| Symbol | Letter | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|---|
| ʔ | `ء` | `U+0294` | 660 | LATIN LETTER GLOTTAL STOP | voiceless glottal stop `/ʔ/` — hamza ء (همزة); phonemic in all positions, e.g. سَأَلَ `/saʔala/` 'he asked', أَكَلَ `/ʔakala/` 'he ate'. Distinct from hamzat al-waṣl (the elidable connecting hamza of ال). |
| b | `ب` | `U+0062` | 98 | LATIN SMALL LETTER B | voiced bilabial plosive `/b/` — bāʾ ب, e.g. بَابٌ `/baːb/` 'door'. Also the reader-tier merge target for source /p/ (p→ب). |
| t | `ت` | `U+0074` | 116 | LATIN SMALL LETTER T | voiceless (plain, non-emphatic) alveolar/denti-alveolar plosive `/t/` — tāʾ ت, e.g. تَمْرٌ `/tamr/` 'dates'. Contrasts with emphatic tˤ ط. |
| θ | `ث` | `U+03B8` | 952 | GREEK SMALL LETTER THETA | voiceless (inter)dental fricative `/θ/` — thāʾ ث, e.g. ثَلاثَةٌ `/θalaːθa/` 'three'. Borrowed Greek theta, NOT Latin. Preserved in MSA/Classical; collapses to `[t]` in urban Levantine (a reason that register is documented-only). |
| dʒ | `ج` | `U+0064 + U+0292` | — | LATIN SMALL LETTER D + LATIN SMALL LETTER EZH (digraph) | voiced post-alveolar affricate `/dʒ/` — jīm ج (MSA prestige value), e.g. جَمَلٌ `/dʒamal/` 'camel'. Realization varies: `[ɡ]` in Egyptian and reconstructed Classical, `[ʒ]` in Levantine/Maghrebi. Tie-bar d͡ʒ may also be written. Reader-tier realization target for source /ɡ/ (ɡ→ج). |
| ħ | `ح` | `U+0127` | 295 | LATIN SMALL LETTER H WITH STROKE | voiceless pharyngeal fricative `/ħ/` — ḥāʾ ح, e.g. حُبٌّ `/ħubb/` 'love'. A core Semitic pharyngeal; contrasts with glottal h ه and uvular/velar x خ. Cognate to source ܚ `/ħ/` and Hebrew ח. |
| x | `خ` | `U+0078` | 120 | LATIN SMALL LETTER X | voiceless velar/uvular fricative `/x/` — khāʾ خ, e.g. خُبْزٌ `/xubz/` 'bread'. Voiceless counterpart of ɣ غ; cognate to source ܟ܂ (spirantized kaph) and rūkkākhā contexts. |
| d | `د` | `U+0064` | 100 | LATIN SMALL LETTER D | voiced (plain, non-emphatic) alveolar/denti-alveolar plosive `/d/` — dāl د, e.g. دَمٌ `/dam/` 'blood'. Contrasts with emphatic dˤ ض. |
| ð | `ذ` | `U+00F0` | 240 | LATIN SMALL LETTER ETH | voiced (inter)dental fricative `/ð/` — dhāl ذ, e.g. ذَهَبٌ `/ðahab/` 'gold'. Latin eth, distinct from Greek theta θ. Preserved in MSA/Classical; collapses to `[d]` in urban Levantine. Cognate to source spirantized dalath ܕ܂. |
| r | `ر` | `U+0072` | 114 | LATIN SMALL LETTER R | voiced alveolar trill/tap `/r/` — rāʾ ر, phonetically `[r]`~`[ɾ]`, e.g. رَأْسٌ `/raʔs/` 'head'. Undergoes emphatic backing of an adjacent /a/→`[ɑ]`; a velarized/emphatic `[rˤ]` allophone occurs near back vowels. |
| z | `ز` | `U+007A` | 122 | LATIN SMALL LETTER Z | voiced alveolar fricative `/z/` — zāy ز, e.g. زَيْتٌ `/zajt/` 'oil'. Voiced counterpart of s س. Cognate to source ܙ, Hebrew ז. |
| s | `س` | `U+0073` | 115 | LATIN SMALL LETTER S | voiceless (plain, non-emphatic) alveolar fricative `/s/` — sīn س, e.g. سَلامٌ `/salaːm/` 'peace'. Contrasts with emphatic sˤ ص. |
| ʃ | `ش` | `U+0283` | 643 | LATIN SMALL LETTER ESH | voiceless post-alveolar fricative `/ʃ/` — shīn ش, e.g. شَمْسٌ `/ʃams/` 'sun'. Cognate to source ܫ `/ʃ/`, Hebrew ש (shin-dot). |
| sˤ | `ص` | `U+0073 + U+02E4` | — | LATIN SMALL LETTER S + MODIFIER LETTER SMALL REVERSED GLOTTAL STOP (pharyngealized) | voiceless pharyngealized (emphatic) alveolar fricative `/sˤ/` — ṣād ص, e.g. صَبْرٌ `/sˤabr/` 'patience'. Emphasis spreads (tafkhīm), backing adjacent /a/→`[ɑ]`. Minimal pair with plain s: سار `/saːr/` vs صار `/sˤaːr/`. Cognate to source ܨ `/sˤ/`, Hebrew צ. |
| dˤ | `ض` | `U+0064 + U+02E4` | — | LATIN SMALL LETTER D + MODIFIER LETTER SMALL REVERSED GLOTTAL STOP (pharyngealized) | voiced pharyngealized (emphatic) alveolar plosive `/dˤ/` — ḍād ض, e.g. ضَوْءٌ `/dˤawʔ/` 'light'. The iconic 'letter of Arabic' (لُغَة الضاد); historically a pharyngealized lateral. NOT present in the source 34-symbol Syriac inventory (source has tˤ sˤ but no dˤ ðˤ). |
| tˤ | `ط` | `U+0074 + U+02E4` | — | LATIN SMALL LETTER T + MODIFIER LETTER SMALL REVERSED GLOTTAL STOP (pharyngealized) | voiceless pharyngealized (emphatic) alveolar plosive `/tˤ/` — ṭāʾ ط, e.g. طِفْلٌ `/tˤifl/` 'child'. Minimal pair with plain t: تين `/tiːn/` vs طين `/tˤiːn/`. Cognate to source ܛ `/tˤ/` (Teth), Hebrew ט. |
| ðˤ | `ظ` | `U+00F0 + U+02E4` | — | LATIN SMALL LETTER ETH + MODIFIER LETTER SMALL REVERSED GLOTTAL STOP (pharyngealized) | voiced pharyngealized (emphatic) interdental fricative `/ðˤ/` — ẓāʾ ظ, e.g. ظِلٌّ `/ðˤill/` 'shade'. Often realized `[zˤ]` in some registers; merges with ض in many dialects. The fourth emphatic; NOT in the source Syriac inventory. |
| ʕ | `ع` | `U+0295` | 661 | LATIN LETTER PHARYNGEAL VOICED FRICATIVE | voiced pharyngeal fricative/approximant `/ʕ/` — ʿayn ع, e.g. عَيْنٌ `/ʕajn/` 'eye/spring'. The voiced partner of ħ ح; a hallmark Semitic sound. Cognate to source ܥ `/ʕ/`, Hebrew ע. |
| ɣ | `غ` | `U+0263` | 611 | LATIN SMALL LETTER GAMMA | voiced velar/uvular fricative `/ɣ/` — ghayn غ, e.g. غَيْمٌ `/ɣajm/` 'cloud'. Voiced counterpart of x خ. Note: IPA gamma `U+0263`, distinct from script-g ɡ `U+0261` (which Arabic lacks natively). |
| f | `ف` | `U+0066` | 102 | LATIN SMALL LETTER F | voiceless labiodental fricative `/f/` — fāʾ ف, e.g. فَمٌ `/fam/` 'mouth'. The reader-tier merge target for source /v/ (v→ف), since Arabic has no native /v/. |
| q | `ق` | `U+0071` | 113 | LATIN SMALL LETTER Q | voiceless uvular plosive `/q/` — qāf ق, e.g. قَلْبٌ `/qalb/` 'heart'. Often grouped with the emphatics (back/tafkhīm consonant). Minimal pair with k: كلب `/kalb/` 'dog' vs قلب `/qalb/` 'heart'. Realized `[ʔ]` in urban Levantine (collapsing the q/ʔ contrast — documented-only). Cognate to source ܩ `/q/`, Hebrew ק. |
| k | `ك` | `U+006B` | 107 | LATIN SMALL LETTER K | voiceless velar plosive `/k/` — kāf ك, e.g. كِتابٌ `/kitaːb/` 'book'. Contrasts with uvular q ق. |
| l | `ل` | `U+006C` | 108 | LATIN SMALL LETTER L | voiced alveolar lateral approximant `/l/` — lām ل, e.g. لَيْلٌ `/lajl/` 'night'. Velarized/emphatic `[ɫ]` notably in اللّٰه `/ʔalˤˤaːh/` 'Allah' and near emphatics. The lām of the definite article ال assimilates to following **sun letters** (الشّمس `/aʃ.ʃams/`) but stays before **moon letters** (القمر `/al.qamar/`). |
| m | `م` | `U+006D` | 109 | LATIN SMALL LETTER M | voiced bilabial nasal `/m/` — mīm م, e.g. ماءٌ `/maːʔ/` 'water'. |
| n | `ن` | `U+006E` | 110 | LATIN SMALL LETTER N | voiced alveolar nasal `/n/` — nūn ن, e.g. نارٌ `/naːr/` 'fire'. Assimilates (idghām) to a following consonant in tajwīd; the nūn of tanwīn (nunation) is realized here. |
| h | `ه` | `U+0068` | 104 | LATIN SMALL LETTER H | voiceless glottal fricative `/h/` — hāʾ ه, e.g. هُوَ `/huwa/` 'he'. Distinct from pharyngeal ħ ح. Letter ة (tāʾ marbūṭa) is realized `[h]` or `[t]` depending on pause/iḍāfa. |
| w | `و` | `U+0077` | 119 | LATIN SMALL LETTER W | voiced labial-velar approximant `/w/` — wāw و, e.g. وَرْدٌ `/ward/` 'rose'. Doubles as the mater lectionis for long /uː/ and as the second element of the diphthong /aw/. |
| j | `ي` | `U+006A` | 106 | LATIN SMALL LETTER J | voiced palatal approximant `/j/` — yāʾ ي (the 'y' sound, NOT the affricate of English 'j'), e.g. يَدٌ `/jad/` 'hand'. Doubles as the mater lectionis for long /iː/ and as the second element of the diphthong /aj/. |

### IPA Vowel Symbols

Arabic has **three** vowel qualities /a i u/, each **short** or **long** (/aː iː uː/) — six phonemic vowels total. The plain qualities a i u reuse Basic Latin letters; length is marked with the IPA length sign ː (documented under suprasegmentals). The two principal **allophones** are ɑ (back/lowered `[a]` under emphatic/pharyngeal backing, tafkhīm) and e (raised `[a]`, the imāla effect of some Classical/dialectal contexts); both come from IPA Extensions / Basic Latin. The reader-tier vowel collapses map source e→kasra/ī and o→ḍamma/ū, matching attested Western-Syriac vocalism.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| a | `U+0061` | 97 | LATIN SMALL LETTER A | short open/central unrounded vowel `/a/` — written with fatḥa ـَ, e.g. كَتَبَ `/kataba/` 'he wrote'. Phonetically `[a]`~`[æ]` in plain/front contexts; backs to `[ɑ]` near emphatics and pharyngeals. |
| aː | `U+0061 + U+02D0` | — | LATIN SMALL LETTER A + MODIFIER LETTER TRIANGULAR COLON | long open/central unrounded vowel `/aː/` — fatḥa carried by the mater lectionis alif ا, e.g. بابٌ `/baːb/` 'door', كاتِبٌ `/kaːtib/` 'writer'. Backs to `[ɑː]` near emphatics. |
| i | `U+0069` | 105 | LATIN SMALL LETTER I | short close front unrounded vowel `/i/` — written with kasra ـِ, e.g. مِنْ `/min/` 'from'. Phonetically `[i]`~`[ɪ]`. Reader-tier collapse target for source /e/ (e→kasra/ī). |
| iː | `U+0069 + U+02D0` | — | LATIN SMALL LETTER I + MODIFIER LETTER TRIANGULAR COLON | long close front unrounded vowel `/iː/` — kasra carried by the mater lectionis yāʾ ي, e.g. كَبيرٌ `/kabiːr/` 'big', دينٌ `/diːn/` 'religion'. |
| u | `U+0075` | 117 | LATIN SMALL LETTER U | short close back rounded vowel `/u/` — written with ḍamma ـُ, e.g. كُتُبٌ `/kutub/` 'books'. Phonetically `[u]`~`[ʊ]`~`[o]`. Reader-tier collapse target for source /o/ (o→ḍamma/ū). |
| uː | `U+0075 + U+02D0` | — | LATIN SMALL LETTER U + MODIFIER LETTER TRIANGULAR COLON | long close back rounded vowel `/uː/` — ḍamma carried by the mater lectionis wāw و, e.g. نورٌ `/nuːr/` 'light', مَكْتوبٌ `/maktuːb/` 'written'. |
| ɑ | `U+0251` | 593 | LATIN SMALL LETTER ALPHA | open **back** unrounded vowel `[ɑ]` — the emphatic/pharyngeal **allophone** of /a/ (tafkhīm backing) adjacent to tˤ sˤ dˤ ðˤ q (and often r), e.g. صابِرٌ `[sˤɑːbir]` 'patient', طاب `[tˤɑːb]` 'it became good'. Allophonic, not phonemic. |
| e | `U+0065` | 101 | LATIN SMALL LETTER E | close-mid front unrounded vowel `[e]` — the imāla **allophone** (raising of /a/ toward `[e]`/`[i]`) found in certain Classical recitation and dialectal contexts, and the realization of tāʾ marbūṭa's preceding vowel in some traditions. Also the value the source /e/ collapses **from** in the reader tier. Allophonic in MSA, not a distinct phoneme. |

### Diacritics & Suprasegmentals

IPA marks for pharyngealization (emphasis), length, stress, gemination, aspiration, and nasalization used in this guide. The pharyngealization modifier ˤ, the length sign ː, the stress marks ˈ ˌ, and aspiration ʰ are spacing characters from Spacing Modifier Letters (`U+02B0`–`U+02FF`); the combining macron ◌̄ and combining tilde ◌̃ are non-spacing marks from Combining Diacritical Marks (`U+0300`–`U+036F`). Gemination (shadda, phonemic in Arabic) is transcribed by **doubling** the consonant letter or with the length sign on the consonant.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| ˤ | `U+02E4` | 740 | MODIFIER LETTER SMALL REVERSED GLOTTAL STOP | pharyngealization (emphasis / tafkhīm) diacritic ˤ; written superscript after the base consonant to mark the four emphatics tˤ sˤ dˤ ðˤ (and emphatic `[rˤ]` `[lˤ]`). Emphasis spreads to adjacent vowels (a→`[ɑ]`) and consonants. THE signature Semitic-emphatic mark of this guide. |
| ː | `U+02D0` | 720 | MODIFIER LETTER TRIANGULAR COLON | length sign ː; marks a long (geminate) segment — long vowels /aː iː uː/ realized via the matres ا و ي, and optionally consonant gemination (shadda), e.g. `/muʕallim/` 'teacher' may be written `/muʕalːim/`. Vowel length is phonemic in Arabic. |
| ˈ | `U+02C8` | 712 | MODIFIER LETTER VERTICAL LINE | primary stress mark ˈ; precedes the stressed syllable. Arabic stress is RULE-BASED and predictable (weight-sensitive, falling on a heavy penult/antepenult), NOT phonemic, e.g. `/makˈtaba/` 'library', `/madˈrasa/` 'school'. |
| ˌ | `U+02CC` | 716 | MODIFIER LETTER LOW VERTICAL LINE | secondary stress mark ˌ; precedes a syllable carrying secondary stress in longer words. |
| ʰ | `U+02B0` | 688 | MODIFIER LETTER SMALL H | aspiration diacritic ʰ; light aspiration on voiceless plosives `[tʰ kʰ]` in some careful pronunciations — minor in Arabic and not contrastive; included for completeness of phonetic transcription. |
| ◌̄ | `U+0304` | 772 | COMBINING MACRON | combining macron ◌̄; the romanization-tier mark for vowel length in ALA-LC / DIN 31635 transliteration (ā ī ū for /aː iː uː/) and for ṣ ḍ ṭ ẓ-style emphatics in some schemes. Non-spacing; attaches above the base letter. |
| ◌̃ | `U+0303` | 771 | COMBINING TILDE | nasalization diacritic ◌̃; marks the nasalized vowel quality of ghunna (nasal humming) in tajwīd, e.g. the prolonged nasalization of nūn/mīm with shadda, `[ãː]`. Non-spacing; attaches above the base vowel. |

### Arabic Letters

The Arabic abjad as encoded in the Arabic block `U+0600`–`U+06FF`. The 28 core consonantal letters run `U+0628`–`U+064A` in **hijāʾī** (modern dictionary) order, preceded by the hamza `U+0621` and the hamza/alif seat variants `U+0622`–`U+0627`. Letters are **contextual** (initial/medial/final/isolated forms — handled by font shaping, not by separate codepoints in logical text); six letters **do not connect to the left**: ا د ذ ر ز و. The 'abjad value' column gives the traditional **abjad** (gematria) numeral order (أبجد هوّز حطّي كلمن سعفص قرشت ثخذ ضظغ), cognate with Hebrew gematria and Syriac letter-numerals. Cross-reference: this abjad is genealogically cognate with the source ܐܒܓܕ (Syriac) and Hebrew אבגד.

| Letter | Arabic Name | Translit. | Codepoint | Decimal | Unicode Name | IPA | Abjad | Connects | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `ء` | همزة | hamza | `U+0621` | 1569 | ARABIC LETTER HAMZA | `/ʔ/` | 1 | non-joining (seat-dependent) | Glottal stop. Written alone or on a seat: أ إ ؤ ئ (see seat variants). |
| `آ` | ألف مدّة | alif madda | `U+0622` | 1570 | ARABIC LETTER ALEF WITH MADDA ABOVE | `/ʔaː/` | 1 | non-joining (left) | Seat variant: alif carrying madda = hamza + long /aː/, e.g. آدَم `/ʔaːdam/` 'Adam'. |
| `أ` | ألف همزة فوق | alif hamza above | `U+0623` | 1571 | ARABIC LETTER ALEF WITH HAMZA ABOVE | `/ʔ/` (+ a/u) | 1 | non-joining (left) | Hamza seated on alif (for /ʔa/ or /ʔu/), e.g. أَكَلَ `/ʔakala/`. |
| `ؤ` | واو همزة | wāw hamza | `U+0624` | 1572 | ARABIC LETTER WAW WITH HAMZA ABOVE | `/ʔ/` | 6 | non-joining (left) | Hamza seated on wāw (typically after /u/), e.g. مُؤْمِن `/muʔmin/` 'believer'. |
| `إ` | ألف همزة تحت | alif hamza below | `U+0625` | 1573 | ARABIC LETTER ALEF WITH HAMZA BELOW | `/ʔi/` | 1 | non-joining (left) | Hamza seated below alif (for /ʔi/), e.g. إِسْلام `/ʔislaːm/`. |
| `ئ` | ياء همزة | yāʾ hamza | `U+0626` | 1574 | ARABIC LETTER YEH WITH HAMZA ABOVE | `/ʔ/` | 10 | dual-joining | Hamza on a (dotless) yāʾ seat (typically after /i/), e.g. سُئِلَ `/suʔila/` 'he was asked'. |
| `ا` | ألف | alif | `U+0627` | 1575 | ARABIC LETTER ALEF | `/aː/` (mater); `/ʔ/` or carrier | 1 | non-joining (left) | Mater lectionis for long /aː/; also bare carrier of hamzat al-waṣl (الـ). One of the six non-connectors. |
| `ب` | باء | bāʾ | `U+0628` | 1576 | ARABIC LETTER BEH | `/b/` | 2 | dual-joining | First letter of hijāʾī order. |
| `ت` | تاء | tāʾ | `U+062A` | 1578 | ARABIC LETTER TEH | `/t/` | 400 | dual-joining | Plain (non-emphatic) /t/. See also ة tāʾ marbūṭa `U+0629`. |
| `ث` | ثاء | thāʾ | `U+062B` | 1579 | ARABIC LETTER THEH | `/θ/` | 500 | dual-joining | Voiceless interdental. |
| `ج` | جيم | jīm | `U+062C` | 1580 | ARABIC LETTER JEEM | `/dʒ/` (MSA); `[ɡ]`/`[ʒ]` variants | 3 | dual-joining | Realization varies by region. Reader-tier target for source /ɡ/. |
| `ح` | حاء | ḥāʾ | `U+062D` | 1581 | ARABIC LETTER HAH | `/ħ/` | 8 | dual-joining | Voiceless pharyngeal fricative. |
| `خ` | خاء | khāʾ | `U+062E` | 1582 | ARABIC LETTER KHAH | `/x/` | 600 | dual-joining | Voiceless velar/uvular fricative. |
| `د` | دال | dāl | `U+062F` | 1583 | ARABIC LETTER DAL | `/d/` | 4 | non-joining (left) | Plain /d/. One of the six non-connectors. |
| `ذ` | ذال | dhāl | `U+0630` | 1584 | ARABIC LETTER THAL | `/ð/` | 700 | non-joining (left) | Voiced interdental. One of the six non-connectors. |
| `ر` | راء | rāʾ | `U+0631` | 1585 | ARABIC LETTER REH | `/r/` | 200 | non-joining (left) | Alveolar trill/tap. One of the six non-connectors. |
| `ز` | زاي | zāy | `U+0632` | 1586 | ARABIC LETTER ZAIN | `/z/` | 7 | non-joining (left) | Voiced alveolar fricative. One of the six non-connectors. |
| `س` | سين | sīn | `U+0633` | 1587 | ARABIC LETTER SEEN | `/s/` | 60 | dual-joining | Plain /s/. |
| `ش` | شين | shīn | `U+0634` | 1588 | ARABIC LETTER SHEEN | `/ʃ/` | 300 | dual-joining | Voiceless post-alveolar fricative. A SUN LETTER (assimilates lām of ال). |
| `ص` | صاد | ṣād | `U+0635` | 1589 | ARABIC LETTER SAD | `/sˤ/` | 90 | dual-joining | Emphatic (pharyngealized) /sˤ/. |
| `ض` | ضاد | ḍād | `U+0636` | 1590 | ARABIC LETTER DAD | `/dˤ/` | 800 | dual-joining | Emphatic /dˤ/; the 'letter of Arabic'. Not in source Syriac inventory. |
| `ط` | طاء | ṭāʾ | `U+0637` | 1591 | ARABIC LETTER TAH | `/tˤ/` | 9 | dual-joining | Emphatic /tˤ/. Cognate to source ܛ Teth. |
| `ظ` | ظاء | ẓāʾ | `U+0638` | 1592 | ARABIC LETTER ZAH | `/ðˤ/` | 900 | dual-joining | Emphatic interdental /ðˤ/ (often `[zˤ]`). Not in source Syriac inventory. |
| `ع` | عين | ʿayn | `U+0639` | 1593 | ARABIC LETTER AIN | `/ʕ/` | 70 | dual-joining | Voiced pharyngeal fricative. Cognate to source ܥ, Hebrew ע. |
| `غ` | غين | ghayn | `U+063A` | 1594 | ARABIC LETTER GHAIN | `/ɣ/` | 1000 | dual-joining | Voiced velar/uvular fricative. Highest single-letter abjad value (1000). |
| `ف` | فاء | fāʾ | `U+0641` | 1601 | ARABIC LETTER FEH | `/f/` | 80 | dual-joining | Reader-tier merge target for source /v/. |
| `ق` | قاف | qāf | `U+0642` | 1602 | ARABIC LETTER QAF | `/q/` | 100 | dual-joining | Voiceless uvular plosive. Cognate to source ܩ, Hebrew ק. |
| `ك` | كاف | kāf | `U+0643` | 1603 | ARABIC LETTER KAF | `/k/` | 20 | dual-joining | Voiceless velar plosive. |
| `ل` | لام | lām | `U+0644` | 1604 | ARABIC LETTER LAM | `/l/` | 30 | dual-joining | The lām of the definite article ال; forms the obligatory ligature لا (lām-alif) `U+FEFB`. |
| `م` | ميم | mīm | `U+0645` | 1605 | ARABIC LETTER MEEM | `/m/` | 40 | dual-joining | Bilabial nasal. |
| `ن` | نون | nūn | `U+0646` | 1606 | ARABIC LETTER NOON | `/n/` | 50 | dual-joining | Alveolar nasal; the consonant underlying tanwīn (nunation). |
| `ه` | هاء | hāʾ | `U+0647` | 1607 | ARABIC LETTER HEH | `/h/` | 5 | dual-joining | Glottal /h/. Related glyph ة tāʾ marbūṭa `U+0629`. |
| `و` | واو | wāw | `U+0648` | 1608 | ARABIC LETTER WAW | `/w/`, `/uː/` (mater) | 6 | non-joining (left) | Consonant /w/ and mater lectionis for /uː/ and diphthong /aw/. One of the six non-connectors. |
| `ي` | ياء | yāʾ | `U+064A` | 1610 | ARABIC LETTER YEH | `/j/`, `/iː/` (mater) | 10 | dual-joining | Consonant /j/ and mater lectionis for /iː/ and diphthong /aj/. Last letter of hijāʾī order. |

#### Related Orthographic Forms

Letters/glyphs in the `U+0621`–`U+064A` range that are positional or morphological variants rather than additional members of the 28-letter alphabet.

| Character | Arabic Name | Translit. | Codepoint | Decimal | Unicode Name | IPA | Notes |
|---|---|---|---|---|---|---|---|
| `ة` | تاء مربوطة | tāʾ marbūṭa | `U+0629` | 1577 | ARABIC LETTER TEH MARBUTA | `/a/` ~ `[-ah]` (pause) / `/t/` (in iḍāfa, before suffix) | Feminine ending; realized `[a]`/`[ah]` utterance-finally (pausal) or `[t]` when linked, e.g. مَدِينَة `/madiːna/` 'city' vs مَدِينَةُ النّبي `/madiːnatu n.nabiː/`. |
| `ى` | ألف مقصورة | alif maqṣūra | `U+0649` | 1609 | ARABIC LETTER ALEF MAKSURA | `/aː/` | Dotless-yāʾ glyph spelling final long /aː/, e.g. عَلى `/ʕalaː/` 'on/upon', مُوسى `/muːsaː/` 'Moses'. Non-joining to the left. |
| `ـ` | تطويل / كَشيدة | taṭwīl / kashīda | `U+0640` | 1600 | ARABIC TATWEEL | ∅ (no phonetic value) | Justification elongation joining two connecting letters; purely typographic, carries no sound. |

### Arabic Harakat (Tashkīl)

The harakat / tashkīl (تشكيل) — short-vowel, nunation, gemination, and quiescence marks of the Arabic block, `U+064B`–`U+0652`, plus the closely allied superscript alif `U+0670` and madda `U+0653`. All are non-spacing **combining** marks attaching above or below a consonant carrier; they are normally **unwritten** in everyday Arabic and supplied only in the vocalized reader tier (and in Quranic mushaf orthography). The vocalized Arabic Peshitta tier emits full harakat; the unvocalized tier strips `U+064B`–`U+0652`.

| Character | Arabic Name | Translit. | Codepoint | Decimal | Unicode Name | IPA | Role |
|---|---|---|---|---|---|---|---|
| `ً` | فَتحتان (تنوين فتح) | fatḥatān (tanwīn fatḥ) | `U+064B` | 1611 | ARABIC FATHATAN | `/an/` | nunation (tanwīn) — indefinite accusative /-an/, e.g. كِتابًا `/kitaːban/`. Dropped in pause (waqf), where it becomes long /aː/. |
| `ٌ` | ضمّتان (تنوين ضمّ) | ḍammatān (tanwīn ḍamm) | `U+064C` | 1612 | ARABIC DAMMATAN | `/un/` | nunation — indefinite nominative /-un/, e.g. كِتابٌ `/kitaːbun/`. Dropped in pause. |
| `ٍ` | كسرتان (تنوين كسر) | kasratān (tanwīn kasr) | `U+064D` | 1613 | ARABIC KASRATAN | `/in/` | nunation — indefinite genitive /-in/, e.g. كِتابٍ `/kitaːbin/`. Dropped in pause. |
| `َ` | فَتْحة | fatḥa | `U+064E` | 1614 | ARABIC FATHA | `/a/` | short /a/ above the consonant, e.g. كَتَبَ `/kataba/` 'he wrote'. Long /aː/ when followed by alif. |
| `ُ` | ضَمّة | ḍamma | `U+064F` | 1615 | ARABIC DAMMA | `/u/` | short /u/ above the consonant, e.g. كُتُب `/kutub/` 'books'. Long /uː/ when followed by wāw. Reader-tier target for source /o/. |
| `ِ` | كَسْرة | kasra | `U+0650` | 1616 | ARABIC KASRA | `/i/` | short /i/ below the consonant, e.g. مِنْ `/min/` 'from'. Long /iː/ when followed by yāʾ. Reader-tier target for source /e/. |
| `ّ` | شَدّة | shadda | `U+0651` | 1617 | ARABIC SHADDA | (consonant gemination, e.g. /Cː/) | gemination/doubling of the consonant — PHONEMIC in Arabic, e.g. دَرَّسَ `/darrasa/` 'he taught' vs دَرَسَ `/darasa/` 'he studied'. Combines with a following vowel mark, which stacks on it. |
| `ْ` | سُكون | sukūn | `U+0652` | 1618 | ARABIC SUKUN | ∅ (no vowel) | vowel absence — marks a consonant closing a syllable (coda), e.g. مِنْ `/min/`, مَكْتَب `/maktab/` 'office'. |

#### Allied Marks

Vowel-bearing marks adjacent to `U+064B`–`U+0652` that complete the vocalization system.

| Character | Arabic Name | Translit. | Codepoint | Decimal | Unicode Name | IPA | Role |
|---|---|---|---|---|---|---|---|
| `ٓ` | مَدّة | madda | `U+0653` | 1619 | ARABIC MADDAH ABOVE | `/ʔaː/` | Placed on alif (آ) to mark hamza + long /aː/, e.g. القُرْآن `/alqurʔaːn/` 'the Qurʾān'. |
| `ٰ` | ألف خنجرية / ألف صغيرة | alif khanjariyya (dagger alif) | `U+0670` | 1648 | ARABIC LETTER SUPERSCRIPT ALEF | `/aː/` | Superscript (dagger) alif marking an unwritten long /aː/, e.g. هٰذا `/haːðaː/` 'this', اللّٰه `/alˤˤaːh/` 'Allah'. Combining mark despite 'LETTER' in its Unicode name. |

### Unicode Blocks Used

The Unicode blocks and control characters from which every symbol in this guide is drawn — the IPA blocks for the phonetic transcription, the Arabic script blocks for the abjad/reader tiers, the bidirectional-isolate controls used to wrap right-to-left verse bodies in otherwise left-to-right JSON/markdown, and the Eastern Arabic-Indic digits. Note that Arabic Presentation Forms (A and B) are **shaping/ligature** blocks used only by legacy rendering pipelines — text in this project is stored in **logical** order using the base Arabic block (`U+0600`–`U+06FF`), and shaping is left to the font.

| Block | Range | Usage |
|---|---|---|
| Basic Latin | `U+0000`–`U+007F` | Plain IPA consonant letters (b t d z s f q k l m n h w j) and the cardinal vowel letters a i u e; ASCII used by the language-neutral Latin (Scholarly/Pretty) reader tiers. |
| Latin-1 Supplement | `U+0080`–`U+00FF` | IPA ð voiced interdental fricative (`U+00F0`). |
| IPA Extensions | `U+0250`–`U+02AF` | Specialized IPA letters: pharyngeal/glottal ʔ (`U+0294`) ʕ (`U+0295`), velar/uvular fricatives ɣ (`U+0263`, gamma) x (`U+0078` is Basic Latin), post-alveolar ʃ (`U+0283`) ʒ (`U+0292`), the back-allophone vowel ɑ (`U+0251`), and ħ (`U+0127`, Latin Extended-A). |
| Latin Extended-A | `U+0100`–`U+017F` | ħ voiceless pharyngeal fricative (`U+0127`, h with stroke). |
| Spacing Modifier Letters | `U+02B0`–`U+02FF` | Spacing IPA diacritics: pharyngealization ˤ (`U+02E4`, emphasis mark), length ː (`U+02D0`), primary/secondary stress ˈ ˌ (`U+02C8`/`U+02CC`), aspiration ʰ (`U+02B0`). |
| Combining Diacritical Marks | `U+0300`–`U+036F` | Non-spacing IPA marks: nasalization ◌̃ (`U+0303`, ghunna) and the macron ◌̄ (`U+0304`, romanization vowel length). |
| Greek and Coptic | `U+0370`–`U+03FF` | θ voiceless interdental fricative, borrowed Greek theta (`U+03B8`). |
| Arabic | `U+0600`–`U+06FF` | THE primary block: the 28 abjad letters and seat/positional variants (hamza `U+0621`, alif `U+0627`, letters through yāʾ `U+064A`), the harakat/tashkīl marks (`U+064B`–`U+0652`), madda (`U+0653`), superscript/dagger alif (`U+0670`), tatwīl (`U+0640`), and the Eastern Arabic-Indic digits (`U+0660`–`U+0669`). Stored in LOGICAL order, right-to-left. *Cross-reference:* cognate with source Syriac block `U+0700`–`U+074F` and Hebrew/Block-Aramaic block `U+0590`–`U+05FF`. |
| Arabic Supplement | `U+0750`–`U+077F` | Extended Arabic letters for non-Arabic languages (e.g. extra dotted forms); NOT used for Standard Arabic text in this guide, listed for completeness of the Arabic-script range. |
| Arabic Extended-A | `U+08A0`–`U+08FF` | Further Arabic-script extensions and Quranic annotation marks; not used in this guide's MSA/Classical core, noted for range completeness. |
| Arabic Presentation Forms-A | `U+FB50`–`U+FDFF` | Pre-composed contextual/ligature glyphs (e.g. ﷲ ALLAH ligature `U+FDF2`) for legacy rendering. NOT used in logical-order text — shaping is done by the font from the base Arabic block. |
| Arabic Presentation Forms-B | `U+FE70`–`U+FEFF` | Positional (initial/medial/final/isolated) glyph forms and the lām-alif ligature (e.g. ﻻ `U+FEFB`). SHAPING block — NOT used in logical-order text; included only to document why these codepoints must NOT appear in stored data. |
| General Punctuation (bidi isolates) | `U+2066`–`U+2069` | Directional-isolate controls. RIGHT-TO-LEFT ISOLATE (RLI) `U+2067` opens, POP DIRECTIONAL ISOLATE (PDI) `U+2069` closes; RTL Arabic verse bodies are wrapped RLI…PDI so they render correctly inside otherwise LTR JSON/markdown. |

#### Bidi Isolate Controls

The exact directional-formatting control characters used to embed right-to-left Arabic strings inside left-to-right documents.

| Codepoint | Decimal | Name | Abbr. | Role |
|---|---|---|---|---|
| `U+2067` | 8295 | RIGHT-TO-LEFT ISOLATE | RLI | Opens a right-to-left directional isolate; placed before an RTL Arabic verse body. |
| `U+2069` | 8297 | POP DIRECTIONAL ISOLATE | PDI | Closes the most recent directional isolate; placed after the RTL Arabic verse body. |

#### Eastern Arabic-Indic Digits

The Eastern Arabic-Indic digits (٠١٢٣٤٥٦٧٨٩) of the Arabic block, used for verse/chapter numbering in Arabic-script presentation; distinct from the Western 'Arabic numerals' 0–9 (Basic Latin) and from the Extended Arabic-Indic digits `U+06F0`–`U+06F9` (Persian/Urdu).

| Character | Codepoint | Decimal | Name | Value |
|---|---|---|---|---|
| `٠` | `U+0660` | 1632 | ARABIC-INDIC DIGIT ZERO | 0 |
| `١` | `U+0661` | 1633 | ARABIC-INDIC DIGIT ONE | 1 |
| `٢` | `U+0662` | 1634 | ARABIC-INDIC DIGIT TWO | 2 |
| `٣` | `U+0663` | 1635 | ARABIC-INDIC DIGIT THREE | 3 |
| `٤` | `U+0664` | 1636 | ARABIC-INDIC DIGIT FOUR | 4 |
| `٥` | `U+0665` | 1637 | ARABIC-INDIC DIGIT FIVE | 5 |
| `٦` | `U+0666` | 1638 | ARABIC-INDIC DIGIT SIX | 6 |
| `٧` | `U+0667` | 1639 | ARABIC-INDIC DIGIT SEVEN | 7 |
| `٨` | `U+0668` | 1640 | ARABIC-INDIC DIGIT EIGHT | 8 |
| `٩` | `U+0669` | 1641 | ARABIC-INDIC DIGIT NINE | 9 |

### Cross-Reference to Sister Scripts

Because Arabic is a Central-Semitic **sister** of the source language (Syriac/Aramaic) and of Hebrew, its abjad and Unicode block are genealogically cognate with theirs. This table situates the Arabic block among its sibling Semitic Unicode blocks for the reader-tier round-trip.

| Language | Script | Unicode Block | Role in Project |
|---|---|---|---|
| Arabic | Arabic abjad | Arabic `U+0600`–`U+06FF` (letters `U+0621`–`U+064A`) | First target language in the SAME family as the source; ships the most faithful / near-reversible reader tier (vocalized + unvocalized abjad). |
| Syriac/Aramaic (**source**) | Syriac abjad ܐܒܓܕ | Syriac `U+0700`–`U+074F` (letters `U+0710`–`U+072C`) | The 34-symbol source inventory; Arabic natively hosts ~25 of its 34 symbols 1:1 (pharyngeals, emphatics tˤ/sˤ, interdentals, x ɣ q ʃ ʔ). |
| Biblical Hebrew | Hebrew square script אבגד | Hebrew `U+0590`–`U+05FF` (letters `U+05D0`–`U+05EA`) | Sister-language parallel guide; shares the pharyngeals ħ ʕ, emphatics, and q with Arabic. |

---

*Signed: Shin*

## Cross-Reference to the Semitic & Companion Guides

Cross-reference relating this Arabic IPA pronunciation guide to its companion guides across the project, with a deliberately rich Semitic-family subsection because Arabic (العَرَبِيَّة *al-ʿarabiyya*) is the FIRST target language documented in the SAME family as the source. Where the Indo-European guides (English, French, Spanish) and the CJK guides (Korean, Japanese, Chinese) document a typological GAP bridged only by the shared IPA apparatus, Arabic instead documents genuine GENETIC kinship: it is a Central Semitic sister of the source Syriac/Aramaic and of Biblical Aramaic and Biblical Hebrew. The three abjads are cognate (ابجد ↔ אבגד ↔ ܐܒܓܕ), the root-and-pattern morphology is shared, and the consonant inventory overlaps almost completely — pharyngeals, emphatics, interdentals, and uvular q. This makes Arabic the most faithful, near-reversible Peshitta reader tier in the whole project, in sharp contrast to the lossy phonetic re-spelling forced on the CJK readers.

### Shared Framework

Every guide in the project — Arabic, the source Peshitta (Syriac), Biblical Aramaic, Biblical Hebrew, English, French, Spanish, Korean, Japanese, and Chinese — is built on one common descriptive apparatus, which makes their pronunciation data directly comparable even where the languages are unrelated. For Arabic specifically, the shared apparatus is reinforced by genuine genetic kinship with the source.

- Primary and sole pronunciation system is the International Phonetic Alphabet (IPA), 2015 revision; the Arabic abjad / orthography is documented but is never the authoritative phonetic record.
- Phonemic transcriptions are written between /slashes/; narrow phonetic (allophonic) transcriptions are written between [brackets] — e.g. phonemic /a/ realized [ɑ] under emphasis spread.
- Consonants are classified by place of articulation, manner of articulation, and voicing (the IPA pulmonic consonant chart); Arabic adds the secondary articulation of pharyngealization, written with the superscript `◌ˤ` (`tˤ sˤ dˤ ðˤ`).
- Vowels are classified by height, backness, roundedness, and length; Arabic's three qualities /a i u/ each occur short and long (/aː iː uː/), with length marked by the IPA triangular colon `ː`.
- Suprasegmental marks are shared: `ˈ` primary stress, `ˌ` secondary stress, `ː` length, and gemination shown by doubling the consonant symbol (the shadda ـّ, e.g. مُدَرِّس *mudarris* [muˈdarris]).
- Each guide documents two (or more) parallel reference registers of one language. Arabic ships Modern Standard Arabic (MSA, الفُصْحَى *al-fuṣḥā*) and Classical/Quranic (tajwīd) in parallel — the GA/RP analog — mirroring the Peshitta's Eastern (Madnhāyā) / Western (Serṭā) pair, Hebrew/Biblical-Aramaic Tiberian reconstruction, and English GA/RP.

> **Note:** Because the framework is identical, an IPA symbol denotes the same articulatory target in every guide. `/b/`, `/t/`, `/s/`, `/m/`, `/ħ/`, `/ʕ/`, `/tˤ/`, `/sˤ/`, `/q/` mean the same sounds in Arabic as in Syriac, Aramaic, or Hebrew; the guides differ in their phoneme inventories, distributions, and phonological rules, not in what the symbols mean. The crucial Arabic point is that, unlike the Indo-European and CJK guides, the symbols are not merely a shared notation — they label sounds Arabic actually shares with the source by common Proto-Semitic descent.

### The Semitic Family

The heart of this cross-reference. Arabic, the source Peshitta Syriac, Biblical Aramaic, and Biblical Hebrew are all Semitic languages descended from Proto-Semitic. Arabic is Central Semitic, a SISTER of Aramaic (the Syriac/Aramaic source) and of the Canaanite branch (Hebrew). This is not a typological analogy but a family tree: the four guides describe four leaves of one branch, and the correspondences below are inherited, not borrowed.

#### Family Tree

- **Proto-Semitic** — Common ancestor reconstructed with a full set of pharyngeals, emphatics, interdentals, and a uvular/post-velar series — the very features that survive intact in Arabic.

| Branch | Guide(s) | Description |
|---|---|---|
| Central Semitic (Arabic) | Arabic (this guide) | Conservatively retains the largest Proto-Semitic consonant inventory of any living Semitic language (28 consonants), including all the pharyngeals, emphatics, interdentals, and uvular q that the source uses. |
| Northwest Semitic (Aramaic) | source Peshitta (Classical Syriac), Biblical Aramaic | Within Northwest Semitic, the closest sub-branch to Arabic; Aramaic and Arabic are sisters at the Central Semitic node (Central Semitic splits into Arabic vs. Northwest Semitic). |
| Northwest Semitic (Canaanite) | Biblical Hebrew | Closely related to Aramaic and to Arabic. |

#### Shared Proto-Semitic Inventory

Sound classes inherited from Proto-Semitic that Arabic shares with the source and the other Semitic guides. These are exactly the classes the Indo-European and CJK guides LACK, and exactly what makes Arabic a faithful host for the source inventory.

| Sound class | Detail |
|---|---|
| Pharyngeals | ح /ħ/ (voiceless pharyngeal fricative) and ع /ʕ/ (voiced pharyngeal fricative) — present in Arabic, Syriac (Kheth ܚ, ʿE ܥ), Biblical Aramaic and Hebrew (Chet ח, Ayin ע). Absent from every Indo-European and CJK guide. |
| Glottals | ء /ʔ/ (hamza, glottal stop) and ه /h/ (glottal fricative) — Arabic ↔ Syriac Ālaph ܐ / He ܗ ↔ Hebrew/Aramaic Alef א / He ה. |
| Emphatics | Pharyngealized consonants: ط /tˤ/ and ص /sˤ/ are shared by all four Semitic guides (Syriac Ṭeth ܛ, Ṣādhē ܨ; Hebrew/Aramaic Tet ט, Tsadi צ). Arabic UNIQUELY adds two further emphatics, ض /dˤ/ and ظ /ðˤ/, that the source does NOT have — see Typological Contrasts and Shared IPA Symbols. |
| Interdentals | ث /θ/, ذ /ð/, ظ /ðˤ/ — Arabic preserves the Proto-Semitic interdentals as full phonemes. The source has them only as Begadkephat spirantization allophones of Taw/Dalath (ܬ→θ, ܕ→ð); Arabic shows them as independent letters, a conservative match. |
| Uvular / post-velar | ق /q/ (voiceless uvular plosive), خ /x/, غ /ɣ/ — Arabic ↔ Syriac Qaph ܩ and the spirantized Kaph/Gamal ([x], [ɣ]) ↔ Hebrew/Aramaic Qof ק and spirantized Kaf/Gimel. |
| Sibilants | س /s/, ز /z/, ش /ʃ/, ص /sˤ/ — the Proto-Semitic sibilant set, shared across all four. Arabic ش /ʃ/ ↔ Syriac Shin ܫ ↔ Hebrew Shin שׁ. |

#### Cognate Abjad

The single most vivid sign of kinship: the three great Semitic abjads descend from one Phoenician/Aramaic letter stock, in the SAME traditional order and with cognate letter NAMES. The ancient abjadī order (أَبْجَد هَوَّز حُطِّي كَلَمُن ...) is itself the inherited Proto-Canaanite sequence shared with Hebrew and Syriac.

**Letter-order cognates:** أَبْجَد *ʾabjad* ↔ Hebrew אבגד *ʾalef-bet-gimel-dalet* ↔ Syriac ܐܒܓܕ *ʾālaph-bēth-gāmal-dālath*. The first four letters and their order are identical across the three scripts — a direct inheritance.

| Arabic | Hebrew | Syriac | IPA |
|---|---|---|---|
| أَلِف *ʾalif* | אָלֶף *ʾalef* | ܐܠܦ Alaph | /ʔ/ |
| بَاء *bāʾ* | בֵּית *bet* | ܒܝܬ Beth | /b/ |
| جِيم *jīm* | גִּימֶל *gimel* | ܓܡܠ Gamal | /dʒ/ (Arabic) ↔ /ɡ/~/ɣ/ (Hebrew/Syriac) |
| دَال *dāl* | דָּלֶת *dalet* | ܕܠܬ Dalath | /d/~/ð/ |
| مِيم *mīm* | מֵם *mem* | ܡܝܡ Mim | /m/ |
| نُون *nūn* | נוּן *nun* | ܢܘܢ Nun | /n/ |
| قَاف *qāf* | קוֹף *qof* | ܩܘܦ Qaph | /q/ |
| شِين *shīn* | שִׁין *shin* | ܫܝܢ Shin | /ʃ/ |

> **Two orders:** Arabic preserves BOTH the ancient abjadī order (cognate with Hebrew/Syriac, still used for numbering as ḥisāb al-jummal) and the modern hijāʾī order grouped by letter shape (ا ب ت ث ...). The numeric values of the abjadī order match the Hebrew gematria / Syriac numbering letter-for-letter (ا=1, ب=2, ج=3, د=4 ... ق=100, ر=200), another inherited system.

#### Root-and-Pattern Morphology

All four Semitic guides share nonconcatenative, templatic morphology: meaning is carried by a discontinuous (usually triconsonantal) consonantal root interleaved with a vocalic/affixal pattern. This is the shared morphological signature of the family and has no equivalent in any Indo-European or CJK companion guide.

**Shared example root** — k-t-b 'write':

| Language | Forms |
|---|---|
| Arabic (ك-ت-ب) | كَتَبَ *kataba* 'he wrote', كِتَاب *kitāb* 'book', كَاتِب *kātib* 'writer', مَكْتُوب *maktūb* 'written/letter' |
| Syriac (ܟ-ܬ-ܒ) | *kthab* 'he wrote', *kthābā* 'book' |
| Hebrew (כ-ת-ב) | *katav*, *ketav* |

The same three consonants thread the same semantic field through all three languages.

> **Note:** Because pattern morphology is shared, an Arabic reader of the Peshitta perceives the source's roots and binyan/stem patterns as the same KIND of structure as their own — unlike a CJK or Indo-European reader, for whom root-and-pattern is wholly foreign.

#### Cognate Vocabulary

Inherited (and sometimes contact-shared) Semitic vocabulary, showing regular sound correspondences across the family. These cognates let an Arabic reader recognize source words on sight, reinforcing Arabic's status as the most faithful reader tier.

| Gloss | Arabic | Syriac | Hebrew | Note |
|---|---|---|---|---|
| peace / greeting | سَلَام *salām* | ܫܠܡܐ *shlāmā* | שָׁלוֹם *shalom* | Same root š-l-m; Arabic س s ↔ Syriac/Hebrew ש /ʃ/ reflects the regular Proto-Semitic *\*š* correspondence. |
| king | مَلِك *malik* | ܡܠܟܐ *malkā* | מֶלֶךְ *melekh* | Root m-l-k across all three. |
| house | بَيْت *bayt* | ܒܝܬܐ *baytā* | בַּיִת *bayit* | Root b-y-t; the diphthong /aj/ (ay) is shared. |
| son | اِبْن *ibn* | ܒܪܐ *bar* / ܒܢ̈ܝܐ *bnayyā* (pl.) | בֵּן *ben* | Root b-n; Aramaic shows the regular *\*n→r* shift in the singular *bar*. |
| name | اِسْم *ism* | ܫܡܐ *shmā* | שֵׁם *shem* | Root š-m; Arabic س ↔ Syriac/Hebrew ש. |
| earth / land | أَرْض *ʾarḍ* | ܐܪܥܐ *arʿā* | אֶרֶץ *ʾeretz* | Shows the famous Proto-Semitic emphatic interdental *\*ṣ́* split: Arabic ض /dˤ/, Aramaic ע /ʕ/, Hebrew צ /sˤ/ — three reflexes of one ancestral sound, and the very reason Arabic ض has no single source counterpart. |

#### Why Arabic Is the Most Faithful Reader Tier

Why this kinship makes the Arabic Peshitta the most faithful, near-reversible reader tier in the project.

- Arabic natively hosts roughly 25 of the source's 34-symbol inventory 1:1 — all pharyngeals (ح ع), emphatics tˤ/sˤ (ط ص), interdentals (ث ذ ظ), and x/ɣ/q/ʃ/ʔ (خ غ ق ش ء) — so almost nothing is collapsed in transcription.
- Only three source consonants lack a native Arabic phoneme: /v p ɡ/. These resolve with minimal, principled merges/realizations — v→ف (f), p→ب (b), ɡ→ج (jīm) — far gentler than the wholesale phonemic loss the CJK readers force.
- Vowel length is preserved via the matres lectionis (ا و ي), matching the source's long/short distinction; source /e o/ collapse to kasra/ī and ḍamma/ū, matching attested Western Syriac vocalism.
- RTL verse bodies are emitted in LOGICAL order wrapped in U+2067 RLI … U+2069 PDI bidi isolates, preserving the source's right-to-left directionality natively rather than transliterating it away.

### Typological Contrasts

How Arabic compares, feature by feature, with the two NON-Semitic guide groups in the project: the Indo-European guides (English, French, Spanish) and the CJK guides (Korean, Japanese, Chinese). With the Semitic source itself the relationship is kinship (see The Semitic Family); here it is contrast. The recurring theme: Arabic, as the third great Semitic abjad, mirrors the source where the others diverge.

| Feature | Arabic | Indo-European guides | CJK guides |
|---|---|---|---|
| Language family | Afro-Asiatic › Semitic › Central Semitic — a genetic SISTER of the Syriac/Aramaic source and of Hebrew. | English (Germanic), French and Spanish (Italic/Romance) — Indo-European, genetically UNRELATED to the source; the IPA framework is the only bridge. | Korean (Koreanic / often called an isolate), Japanese (Japonic), Chinese (Sino-Tibetan › Sinitic) — all unrelated to the source and to each other's families. |
| Writing system and direction | Right-to-left ABJAD (28 consonantal letters; short vowels optional via harakat) — cognate with the source's Syriac abjad and Hebrew square abjad. The third great Semitic abjad. | Left-to-right Latin alphabet (true alphabet writing both consonants and vowels). | Korean alphabetic Hangul (featural, syllable-blocked); Japanese mixed logographic Kanji + syllabic kana; Chinese logographic Hanzi (no phonetic spelling of the morpheme). None is an abjad; none is RTL. |
| Morphological type | Root-and-pattern (templatic, nonconcatenative) — the SAME morphological signature as the source: triconsonantal roots × vocalic patterns (k-t-b → *kataba, kitāb, maktūb*). | Concatenative — fusional/inflectional (Spanish, French) or analytic-leaning (English); affixes added linearly, no root interdigitation. | Korean agglutinative; Japanese agglutinative; Chinese isolating/analytic (largely monosyllabic morphemes, minimal inflection). None uses root-and-pattern. |
| Pharyngeals and emphatics | Full guttural + emphatic series matching the source: pharyngeals ح /ħ/, ع /ʕ/; emphatics ط /tˤ/, ص /sˤ/ (shared with source) PLUS ض /dˤ/, ظ /ðˤ/ (Arabic-only, absent in source); uvular ق /q/; emphasis spread (tafkhīm) backs adjacent vowels just as in the source. | NO pharyngeals, NO emphatics, NO uvular q. English/French/Spanish have at most /x/ (Spanish j) and uvular rhotics (French r) — none of the source's signature contrasts. | NO pharyngeals or emphatics. Korean has a three-way lax/tense/aspirated stop contrast; Mandarin has aspirated/unaspirated; none maps to pharyngealization. |
| Interdentals | Phonemic ث /θ/, ذ /ð/, ظ /ðˤ/ — preserves the Proto-Semitic interdentals as full letters; the source has [θ ð] as Begadkephat allophones. | English has /θ ð/ (thin, this); French and Spanish lack /θ/ except Peninsular Spanish /θ/ (ciudad). Partial overlap at best. | No /θ/ or /ð/ in Korean, Japanese, or Standard Mandarin; these are among the hardest sounds for CJK learners. |
| Vowel system | Compact and source-like: three qualities /a i u/ × two lengths (/aː iː uː/) + diphthongs /aj/ (ay), /aw/ (aw) — closely parallel to the source's small vowel inventory and its /aj aw/ diphthongs. | Large vowel systems: English ~11–12 monophthongs + many diphthongs; French adds nasal vowels and front rounded /y ø œ/; Spanish a tidy 5-vowel system (the nearest, but no length or pharyngeal backing). | Korean ~7–8 vowels; Japanese 5 vowels with phonemic LENGTH (closest to Arabic on length); Mandarin a mid-sized system dominated by TONE. |
| Suprasegmental backbone | Rule-based, predictable, weight-sensitive STRESS (not phonemic); phonemic GEMINATION (shadda); NO lexical tone — matching the source's prosodic type. | Contrastive lexical stress (English ˈrecord vs reˈcord; Spanish/French more fixed); no phonemic gemination (Italian-style); no tone. | Tone/pitch is central: Mandarin has 4 lexical TONES + neutral; Japanese has pitch-accent; Korean has no lexical tone but phonation contrasts. Tone is wholly alien to the source. |
| Faithfulness as a Peshitta reader tier | MOST FAITHFUL / near-reversible: ~25/34 source symbols hosted natively; only v→ف, p→ب, ɡ→ج merges; vowel length kept via matres; RTL kept. The abjad re-encodes the source almost letter-for-letter. | Lossy: Latin-script re-spelling of pharyngeals/emphatics via digraphs or approximations; RTL flattened to LTR; root structure invisible. | MOST lossy — a genuine COLLAPSE: pharyngeals, emphatics, interdentals, and most consonant clusters have no host and are merged or dropped; Hangul/kana/Hanzi force the source into an alien syllable shape, and the reader tiers (e.g. Chinese Hanzi, Japanese katakana) are explicitly one-way, NOT reversible — the polar opposite of the Arabic tier. |

**Summary:** Read top to bottom, the contrast is consistent: on family, script direction, abjad type, morphology, pharyngeals/emphatics, interdentals, vowel compactness, and prosodic type, Arabic SIDES WITH THE SOURCE and DIFFERS FROM the Indo-European and CJK guides. Arabic is the third great Semitic abjad, and the Arabic Peshitta is correspondingly the project's high-fidelity, near-reversible reader tier — the antithesis of the CJK collapse.

### Companion Guides

All companion pronunciation guides in the project, with repo-relative paths. The three Semitic guides are siblings of Arabic (see The Semitic Family); the Indo-European and CJK guides are the typological foils (see Typological Contrasts).

#### Semitic Siblings

- **Peshitta** — `peshitta_pronunciation_guide.json`. The SOURCE language. Classical Syriac (Aramaic), the Peshitta reading tradition — Arabic's nearest documented sibling. Documents Eastern (Madnhāyā) and Western (Serṭā) traditions, Begadkephat spirantization, guttural and emphatic consonants, and the Syriac abjad (U+0700–U+074F). See its `cross_reference_to_aramaic_and_hebrew` section.
- **Biblical Aramaic** — `biblical_aramaic_pronunciation_guide.json`. Biblical/Jewish Literary Aramaic (Daniel, Ezra) in Tiberian pointing — same Aramaic branch as the source, Hebrew square abjad. Shares emphatics, gutturals, interdentals, and triconsonantal roots with Arabic.
- **Biblical Hebrew** — `biblical_hebrew_pronunciation_guide.json`. Biblical (Classical) Hebrew, Tiberian reading tradition — Northwest Semitic Canaanite branch, Hebrew square abjad with Tiberian niqqud. Closest non-Aramaic Semitic relative; cognate abjad and root morphology with Arabic. See its `cross_reference_to_aramaic` section.

#### Indo-European Foils

- **English** — `English/english_pronunciation_guide.json`. Indo-European (Germanic). Contrastive bridge — shares IPA but no pharyngeals/emphatics, LTR Latin alphabet, large vowel system.
- **French** — `French/french_pronunciation_guide.json`. Indo-European (Romance/Italic). Nasal vowels and front rounded vowels; uvular rhotic; no pharyngeals/emphatics; LTR Latin alphabet.
- **Spanish** — `Spanish/spanish_pronunciation_guide.json`. Indo-European (Romance/Italic). Tidy 5-vowel system (nearest to Arabic's qualities) and /x/ (j); but no pharyngeals/emphatics, no length, LTR Latin alphabet.

#### CJK Foils

- **Korean** — `Korean/korean_pronunciation_guide.json`. Koreanic (isolate). Featural Hangul; lax/tense/aspirated stops; no pharyngeals/emphatics. Ships 4 reader tiers (Scholarly, Pretty, Hangul, Revised Romanization) — lossy, not reversible.
- **Japanese** — `Japanese/japanese_pronunciation_guide.json`. Japonic. Kanji + kana; 5 vowels with phonemic length; pitch-accent. Ships 5 reader tiers (Scholarly, Pretty, Katakana, Hiragana, Romaji) — heavy collapse into mora structure.
- **Chinese** — `Chinese/chinese_pronunciation_guide.json`. Sino-Tibetan › Sinitic (Standard Mandarin). Logographic Hanzi; 4 tones; no pharyngeals/emphatics/clusters. Ships 6 reader tiers (Scholarly, Pretty, Pinyin, Zhuyin, Hanzi-Simplified, Hanzi-Traditional) — the most lossy, one-way mapping in the project.

### Shared IPA Symbols

IPA values shared between Arabic and the source (and, where noted, the other Semitic guides). Because Arabic is a Semitic sibling, the overlap is near-total: almost ALL of the source's ~34-symbol inventory has a native Arabic host. The symbol denotes the same articulatory target everywhere; only distribution and phonological patterning differ. This table is the technical backbone of the "most faithful reader tier" claim.

#### Consonants Shared with the Source

| IPA | Name | Arabic | Source | Note |
|---|---|---|---|---|
| `ʔ` | glottal stop | ء hamza | ܐ Ālaph | Direct 1:1. |
| `b` | voiced bilabial plosive | ب bāʾ | ܒ Bēth (hard) | Also the host for source /p/ → ب. |
| `t` | voiceless alveolar/dental plosive | ت tāʾ | ܬ Taw (hard) | Distinct from emphatic ط /tˤ/. |
| `θ` | voiceless interdental fricative | ث thāʾ | ܬ Taw (spirantized, Begadkephat) | Arabic has it as a full phoneme; source as an allophone. |
| `d` | voiced alveolar/dental plosive | د dāl | ܕ Dālath (hard) | Distinct from emphatic ض /dˤ/. |
| `ð` | voiced interdental fricative | ذ dhāl | ܕ Dālath (spirantized) | Full phoneme in Arabic; allophone in source. |
| `r` | alveolar trill | ر rāʾ | ܪ Rīsh | Both trills (Hebrew Tiberian Resh is uvular /ʁ/ instead). |
| `z` | voiced alveolar fricative | ز zāy | ܙ Zayn | Direct 1:1. |
| `s` | voiceless alveolar fricative | س sīn | ܣ Semkath | Distinct from emphatic ص /sˤ/. |
| `ʃ` | voiceless postalveolar fricative | ش shīn | ܫ Shin | Direct 1:1; also the host for the regular *\*š* correspondence (*salām*/*shlāmā*). |
| `sˤ` | emphatic (pharyngealized) s | ص ṣād | ܨ Ṣādhē | Shared emphatic; spreads tafkhīm to adjacent vowels in both. |
| `tˤ` | emphatic (pharyngealized) t | ط ṭāʾ | ܛ Ṭeth | Shared emphatic. |
| `ʕ` | voiced pharyngeal fricative | ع ʿayn | ܥ ʿE | Direct 1:1; one of the hallmark Semitic gutturals. |
| `ɣ` | voiced velar/uvular fricative | غ ghayn | spirantized Gāmal ܓ | Phoneme in Arabic; spirantization allophone in source. |
| `f` | voiceless labiodental fricative | ف fāʾ | ܦ Pe (spirantized) | Arabic ف also hosts source /v/ and /p/ where spirantized. |
| `q` | voiceless uvular plosive | ق qāf | ܩ Qaph | Direct 1:1; preserved in MSA/Classical (urban Levantine collapses it to [ʔ], which is why Levantine is documented-only). |
| `k` | voiceless velar plosive | ك kāf | ܟ Kaph (hard) | Direct 1:1. |
| `x` | voiceless velar/uvular fricative | خ khāʾ | ܟ Kaph (spirantized) | Phoneme in Arabic; allophone in source. |
| `l` | voiced alveolar lateral approximant | ل lām | ܠ Lamadh | Direct 1:1. |
| `m` | voiced bilabial nasal | م mīm | ܡ Mīm | Direct 1:1. |
| `n` | voiced alveolar nasal | ن nūn | ܢ Nun | Direct 1:1. |
| `h` | voiceless glottal fricative | ه hāʾ | ܗ He | Direct 1:1. |
| `w` | voiced labial-velar approximant | و wāw | ܘ Waw | Also a mater lectionis for /uː/ in both. |
| `j` | voiced palatal approximant | ي yāʾ | ܝ Yudh | Also a mater lectionis for /iː/ in both. |
| `ħ` | voiceless pharyngeal fricative | ح ḥāʾ | ܚ Kheth | Direct 1:1; the second hallmark Semitic guttural. |

#### Vowels and Diphthongs Shared

| IPA | Arabic | Source | Note |
|---|---|---|---|
| `a / aː` | fatḥa ـَ / alif ا | Ptāḥā / Zqāphā (short/long a) | Backed to [ɑ] near emphatics in both. |
| `i / iː` | kasra ـِ / yāʾ ي | Ḥbāṣā | Source /e/ also collapses here in the Arabic reader tier (e→kasra/ī). |
| `u / uː` | ḍamma ـُ / wāw و | ʿṢāṣā / Rwāḥā | Source /o/ also collapses here (o→ḍamma/ū), matching Western Syriac vocalism. |
| `aj` | ـَيْ (ay) | aj diphthong | Shared (*bayt*/*baytā*). |
| `aw` | ـَوْ (aw) | aw diphthong | Shared. |

#### Arabic Gaps for Source Consonants

The handful of source consonants Arabic does NOT host natively, and how the Arabic Peshitta reader tier resolves them. There are only three, and the resolutions are minimal — the basis of the near-reversibility claim.

| IPA | Issue | Resolution |
|---|---|---|
| `v` | Arabic has no native /v/. | v → ف (f) — merges with /f/, the nearest native fricative. |
| `p` | Arabic has no native /p/. | p → ب (b) — merges with /b/, the nearest native plosive. |
| `ɡ` | Arabic ج jīm is /dʒ/ in MSA, not plain /ɡ/. | ɡ → ج (jīm) — a realization choice; ج is /ɡ/ in Egyptian/Classical Arabic, so this is faithful in that register. |

#### Arabic-Only Consonants Absent in the Source

Arabic phonemes with NO counterpart in the source's inventory — the two extra emphatics. They reflect Proto-Semitic sounds that Aramaic/Syriac merged away but Arabic kept, so they are surplus capacity in the reader tier (they simply go unused when transcribing source text, which never needs them).

| IPA | Arabic | Name | Note |
|---|---|---|---|
| `dˤ` | ض ḍād | emphatic (pharyngealized) d | The famous letter of Arabic (لُغَة الضَّاد 'the language of the ḍād'). Proto-Semitic *\*ṣ́* surfaces as ض in Arabic but as ע /ʕ/ in Aramaic and צ /sˤ/ in Hebrew (cf. *ʾarḍ* / *arʿā* / *ʾeretz*). The source has no ض. |
| `ðˤ` | ظ ẓāʾ | emphatic (pharyngealized) interdental | Emphatic counterpart of ذ /ð/. Merged into other consonants in Aramaic/Syriac; absent from the source inventory. |

> **Note:** The arithmetic of fidelity: of the source's consonants, Arabic natively hosts ~25 with matching IPA values (including the rare pharyngeals, emphatics tˤ/sˤ, interdentals, and uvular q that every non-Semitic guide lacks). Only /v p ɡ/ require resolution, via gentle merges/realization. Arabic even has surplus phonemes (ض ظ) the source never needs. This overlap is categorically larger than any Indo-European guide's and incomparably larger than any CJK guide's — quantitative proof that the Arabic Peshitta is the project's most faithful, near-reversible reader tier.

> **Note:** This cross-reference is intentionally the richest in the Arabic guide because Arabic is the FIRST project target in the SAME family as the source. Where the English/French/Spanish guides offer only a contrastive bridge over an Indo-European gap, and the Korean/Japanese/Chinese guides document an outright phonetic collapse, Arabic documents genuine Semitic KINSHIP: a cognate abjad in cognate order (ابجد ↔ אבגד ↔ ܐܒܓܕ), shared root-and-pattern morphology, inherited cognate vocabulary (سَلَام *salām* ↔ ܫܠܡܐ *shlāmā* ↔ שָׁלוֹם *shalom*), and a near-total consonant overlap that includes the pharyngeals, emphatics, interdentals, and uvular q. Arabic is the third great Semitic abjad, and the Arabic Peshitta is correspondingly the most faithful — and most nearly reversible — reader tier in the entire project.

---

*Compiled by Shin.*
