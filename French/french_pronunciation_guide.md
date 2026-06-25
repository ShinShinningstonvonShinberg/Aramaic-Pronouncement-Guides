# French IPA Pronunciation Guide

**Version:** 1.0.0
**Date:** 2026-06-24
**Language:** French (ISO 639-3: `fra`)  
**Encoding:** UTF-8  
**IPA Standard:** IPA (International Phonetic Alphabet, 2015 revision)  
**Reference Accents:** Standard Metropolitan French (SMF) and Quebec French (QC)  

Machine-readable IPA-based pronunciation guide for Modern French. All pronunciation data is encoded in the International Phonetic Alphabet (IPA, 2015 revision) as the primary and only system. Designed for AI-assisted pronunciation, text-to-speech reference, second-language teaching, and language documentation. Two reference accents are documented in parallel: Standard Metropolitan (European/Parisian) French and Quebec (Canadian) French.

### Varieties Covered

- **Standard Metropolitan French (français standard, SMF)** — France and continental Europe (supraregional Parisian-based standard; the norm of broadcast media, education, and dictionaries). The reference variety of European French, historically based on educated Parisian speech. Its modern oral norm shows several mergers relative to the conservative system: the front /a/ vs back /ɑ/ contrast is largely lost (most speakers have a single low vowel `/a/`), the nasal /ɛ̃/ vs /œ̃/ contrast is largely lost (brin = brun for most speakers, both `/ɛ̃/`), and the long /ɛː/ (maître, fête) has merged with /ɛ/. The rhotic is a voiced uvular fricative or approximant `/ʁ/`. Mid-vowel quality (/e/ vs /ɛ/, /o/ vs /ɔ/, /ø/ vs /œ/) is governed largely by the loi de position (open syllable favors close mid vowels, closed syllable favors open mid vowels), with lexical exceptions. Schwa `/ə/` (e caduc) is frequently deleted. Vowel length is largely non-distinctive.
- **Quebec French (français québécois, QC)** — Quebec and francophone Canada (Laurentian French; the principal North American variety). The principal variety of Canadian French. It is phonologically more conservative than Metropolitan French in its vowel oppositions yet has distinctive innovations. It MAINTAINS the contrasts that Metropolitan French has largely merged: front /a/ vs back /ɑ/ (e.g. patte `/pat/` vs pâte `/pɑt/`) and nasal /ɛ̃/ vs /œ̃/ (brin `/bʁɛ̃/` vs brun `/bʁœ̃/`). Characteristic Quebec features include: AFFRICATION of /t/ and /d/ to `[t͡s]` and `[d͡z]` before the high front vowels and glides /i y j ɥ/ (e.g. tu `[t͡sy]`, dire `[d͡zɪːʁ]`, dur `[d͡zyːʁ]`); LAXING of the high vowels /i y u/ to `[ɪ ʏ ʊ]` in closed, non-final stressed syllables (e.g. vite `[vɪt]`, jupe `[ʒʏp]`, route `[ʁʊt]`); DIPHTHONGIZATION of long vowels in stressed closed syllables (e.g. père `[pɑɛ̯ʁ]`, fête `[faɪ̯t]`, tard `[tɑɔ̯ʁ]`); and retention of more contrastive vowel length. The historical rhotic varied (apical `[r]` vs uvular `[ʁ]`); the uvular `/ʁ/` is now dominant, especially among younger speakers.

### Companion Files

- `peshitta_pronunciation_guide.json`
- `biblical_aramaic_pronunciation_guide.json`
- `biblical_hebrew_pronunciation_guide.json`
- `english_pronunciation_guide.json`

### Notes

- French is written left-to-right in the Latin (Roman) script, unlike the right-to-left Semitic companion guides.
- Stress in French is NOT lexical or contrastive: it is fixed and falls on the final full syllable of a rhythmic group (groupe rythmique / phrase-final). Individual words have no inherent contrastive stress, so this guide does NOT mark word stress — a major typological contrast with English, where stress is phonemic (e.g. ˈrecord vs reˈcord).
- French is syllable-timed (each syllable takes roughly equal time), unlike stress-timed English; this gives French its characteristic even rhythm and resists the vowel reduction that pervades English unstressed syllables.
- Liaison and enchaînement are central to French connected speech: a normally silent final consonant may be pronounced and resyllabified onto a following vowel-initial word (liaison, e.g. les amis `[le.z‿a.mi]`), and a pronounced final consonant is regularly carried over as the onset of a following vowel-initial syllable (enchaînement). These processes reshape syllable and word boundaries in the phonetic stream.
- French has a system of contrastive NASAL VOWELS (/ɛ̃ ɑ̃ ɔ̃/, plus /œ̃/ where maintained), encoded with the combining tilde U+0303 on the base vowel — a feature absent from the English and Semitic companion guides.
- French has three FRONT ROUNDED vowels /y ø œ/ (e.g. tu, peu, peur), a marked feature cross-linguistically and a notorious difficulty for English-speaking learners.
- The French rhotic is a UVULAR `/ʁ/` (voiced uvular fricative/approximant), not the alveolar /r/ or /ɹ/ of the companion languages; older and some regional/Quebec varieties retain apical `[r]`.
- French has three SEMIVOWELS (glides) /j ɥ w/, including the rare labio-palatal /ɥ/ (huit `/ɥit/`, lui `/lɥi/`), which contrasts with /w/ (Louis `/lwi/`) and /j/.
- Mid-vowel quality is largely governed by the loi de position (positional law): close mid vowels /e o ø/ tend to appear in open syllables and open mid vowels /ɛ ɔ œ/ in closed syllables, with lexical and accent-dependent exceptions.
- The schwa `/ə/` (e caduc / e muet) is frequently deleted depending on speech rate, register, and the surrounding consonant cluster (loi des trois consonnes), making its surface presence variable.
- French orthography preserves many SILENT letters, especially silent final consonants (petit `/pə.ti/`) and silent final -e, yet remains comparatively regular in the reading (grapheme→phoneme) direction, so IPA is the authoritative pronunciation record here.
- The two reference accents differ systematically: Quebec French maintains the /a/~/ɑ/ and /ɛ̃/~/œ̃/ contrasts (largely merged in Metropolitan French), affricates /t d/ to `[t͡s d͡z]` before /i y j ɥ/, laxes high vowels to `[ɪ ʏ ʊ]` in closed syllables, diphthongizes long vowels, and preserves more contrastive vowel length.

## Table of Contents

- [How to Read This Guide](#how-to-read-this-guide)
  - [Phonemic vs phonetic notation](#phonemic-vs-phonetic-notation)
  - [Stress (fixed / phrase-final)](#stress-fixed--phrase-final)
  - [The two reference accents](#the-two-reference-accents)
  - [Nasal vowels (tilde notation)](#nasal-vowels-tilde-notation)
  - [Length (ː)](#length-ː)
- [Phonological Inventory](#phonological-inventory)
  - [Consonant Phonemes](#consonant-phonemes)
  - [Semivowels](#semivowels)
  - [Vowel Phonemes](#vowel-phonemes)
- [Consonants](#consonants)
  - [Consonant Inventory](#consonant-inventory)
  - [Natural Classes](#natural-classes)
- [Oral Vowels](#oral-vowels)
  - [Vowel Classes](#vowel-classes)
  - [Loi de Position Overview](#loi-de-position-overview)
  - [Oral Vowel Inventory](#oral-vowel-inventory)
  - [The `/a/`~`/ɑ/` Merger](#the-aɑ-merger)
  - [Vowel Length](#vowel-length)
  - [Quebec Features Overview](#quebec-features-overview)
  - [IPA Symbol Summary](#ipa-symbol-summary)
- [Nasal Vowels](#nasal-vowels)
  - [Inventory](#inventory)
  - [Reference-accent realization](#reference-accent-realization)
  - [The /ɛ̃/~/œ̃/ Merger](#the-ɛœ-merger)
  - [Nasalization Rule](#nasalization-rule)
  - [Orthography (IPA Notation)](#orthography-ipa-notation)
  - [No Phonemic Diphthongs](#no-phonemic-diphthongs)
  - [Summary](#summary)
- [Semivowels (Glides)](#semivowels-glides)
  - [The Three Glides](#the-three-glides)
  - [Vowel–Glide Correspondence](#vowelglide-correspondence)
  - [Distribution and Rounding/Place Contrast](#distribution-and-roundingplace-contrast)
  - [Minimal and Near-Minimal Pairs](#minimal-and-near-minimal-pairs)
  - [Phonetic Notes by Glide](#phonetic-notes-by-glide)
  - [Cross-Accent Summary](#cross-accent-summary)
- [Consonant–Vowel IPA Matrix](#consonantvowel-ipa-matrix)
  - [Reference Vowels](#reference-vowels)
  - [CV Matrix](#cv-matrix)
  - [Quebec Combinations (Affrication)](#quebec-combinations-affrication)
  - [Phonetic Notes](#phonetic-notes)
  - [Accent Notes](#accent-notes)
- [Suprasegmentals](#suprasegmentals)
  - [Stress (fixed phrase-final, NOT lexical)](#stress-fixed-phrase-final-not-lexical)
  - [Rhythm (syllable-timed)](#rhythm-syllable-timed)
  - [Vowel Length](#vowel-length-1)
  - [No Vowel Reduction](#no-vowel-reduction)
  - [Intonation](#intonation)
- [Syllable Structure](#syllable-structure)
  - [Open-Syllable Preference](#open-syllable-preference)
  - [Components](#components)
  - [Resyllabification](#resyllabification)
  - [Syllable Types](#syllable-types)
  - [Constraints](#constraints)
- [Phonological Rules](#phonological-rules)
  - [Rules at a Glance](#rules-at-a-glance)
  - [Rule 1: Liaison (latent final consonant)](#rule-1-liaison-latent-final-consonant)
  - [Rule 2: Enchaînement (consonantal resyllabification)](#rule-2-enchaînement-consonantal-resyllabification)
  - [Rule 3: Élision (vowel deletion before a vowel)](#rule-3-élision-vowel-deletion-before-a-vowel)
  - [Rule 4: E-caduc / schwa deletion (e muet)](#rule-4-e-caduc--schwa-deletion-e-muet)
  - [Rule 5: Vowel nasalization (V + coda N → nasal vowel)](#rule-5-vowel-nasalization-v--coda-n--nasal-vowel)
  - [Rule 6: Loi de position (mid-vowel quality by syllable type)](#rule-6-loi-de-position-mid-vowel-quality-by-syllable-type)
  - [Rule 7: Regressive voicing assimilation](#rule-7-regressive-voicing-assimilation)
  - [Rule 8: Final-consonant silence](#rule-8-final-consonant-silence)
  - [Rule 9: H aspiré vs h muet](#rule-9-h-aspiré-vs-h-muet)
  - [Rule 10: Affrication of /t d/ before high front vocoids (Quebec)](#rule-10-affrication-of-t-d-before-high-front-vocoids-quebec)
  - [Rule 11: High-vowel laxing in closed syllables (Quebec)](#rule-11-high-vowel-laxing-in-closed-syllables-quebec)
  - [Rule 12: Long-vowel diphthongization (Quebec)](#rule-12-long-vowel-diphthongization-quebec)
  - [Rule 13: /a/ ~ /ɑ/ and /ɛ̃/ ~ /œ̃/ contrasts](#rule-13-a--ɑ-and-ɛ--œ-contrasts)
  - [Rule 14: Devoicing and weakening of the uvular R](#rule-14-devoicing-and-weakening-of-the-uvular-r)
  - [Rule 15: Semivowel formation (gliding of high vowels before a vowel)](#rule-15-semivowel-formation-gliding-of-high-vowels-before-a-vowel)
  - [Notes](#notes)
- [Liaison & Connected Speech](#liaison--connected-speech)
  - [Reference Accents](#reference-accents)
  - [Liaison](#liaison)
  - [Élision](#élision)
  - [Enchaînement](#enchaînement)
  - [E-caduc](#e-caduc)
  - [Clitics](#clitics)
  - [Quebec-Specific Processes](#quebec-specific-processes)
  - [How the Processes Interact](#how-the-processes-interact)
- [Standard Metropolitan vs. Quebec French](#standard-metropolitan-vs-quebec-french)
  - [The Two Reference Accents](#the-two-reference-accents-1)
  - [Table of Differences](#table-of-differences)
  - [Summary](#summary-1)
- [Orthography: Grapheme–Phoneme Correspondences](#orthography-graphemephoneme-correspondences)
  - [General Principles](#general-principles)
  - [Vowel Graphemes](#vowel-graphemes)
  - [Consonant Graphemes](#consonant-graphemes)
  - [Silent Letters](#silent-letters)
  - [Diacritics](#diacritics)
  - [Notes](#notes-1)
- [Sample Words in IPA](#sample-words-in-ipa)
- [Unicode Reference](#unicode-reference)
  - [IPA Consonant Symbols](#ipa-consonant-symbols)
  - [IPA Semivowel Symbols](#ipa-semivowel-symbols)
  - [IPA Vowel Symbols](#ipa-vowel-symbols)
  - [Nasal & Diacritics](#nasal--diacritics)
  - [Unicode Blocks Used](#unicode-blocks-used)
- [Cross-Reference to the Companion Guides](#cross-reference-to-the-companion-guides)
  - [Shared Framework](#shared-framework)
  - [Typological Contrasts](#typological-contrasts)
  - [Companion Guides](#companion-guides)
  - [Shared IPA Symbols](#shared-ipa-symbols)

## How to Read This Guide

This guide encodes all pronunciation data in the International Phonetic Alphabet (IPA, 2015 revision). The conventions below explain how to read the transcriptions.

### Phonemic vs phonetic notation

Phonemic transcriptions use `/ /` slashes and represent contrastive sound units (phonemes) abstracted away from predictable variation — e.g. tu `/ty/`. Phonetic transcriptions use `[ ]` brackets and record finer allophonic detail, including accent-specific realizations — e.g. Quebec tu `[t͡sy]`. Throughout this guide the `/slashes/` and `[brackets]` are preserved exactly as in the source data; do not interconvert them.

### Stress (fixed / phrase-final)

French stress is NOT lexical and NOT contrastive. It is fixed: prominence falls on the final full syllable of a rhythmic group (groupe rythmique), i.e. it is phrase-final rather than word-bound. Because individual words carry no inherent contrastive stress, this guide does NOT use word-stress marks (no `/ˈ/` primary-stress or `/ˌ/` secondary-stress diacritics on lexical entries). This is a major typological contrast with English, where stress is phonemic (e.g. ˈrecord vs reˈcord).

### The two reference accents

Two reference accents are documented in parallel and treated as co-equal standards:

- **Standard Metropolitan French (SMF)** — the supraregional, Parisian-based European norm.
- **Quebec French (QC)** — the principal North American (Laurentian) variety.

Wherever the data distinguishes them, both accents are given side by side. Note in particular the QC features absent from SMF: the /a/~/ɑ/ and /ɛ̃/~/œ̃/ contrasts, affrication of /t d/ to `[t͡s d͡z]` before /i y j ɥ/, high-vowel laxing to `[ɪ ʏ ʊ]`, and diphthongization of long vowels. (This guide does NOT use Wells lexical sets, which are specific to the English guide.)

### Nasal vowels (tilde notation)

French has contrastive nasal vowels: `/ɛ̃/`, `/ɑ̃/`, `/ɔ̃/`, and `/œ̃/` (the last largely merged into `/ɛ̃/` in much of France but kept distinct in Quebec French). A nasal vowel is written as its base oral vowel symbol plus the combining tilde U+0303 (◌̃) — for example `/ɛ̃/` in vin `/vɛ̃/`. The tilde marks nasality (airflow through the nose) and is part of the vowel symbol, not a separate diacritic to be dropped.

### Length (ː)

The length mark `ː` (the IPA triangular colon, U+02D0) indicates a long vowel — for example `/ɛː/`. Vowel length is largely non-distinctive in Standard Metropolitan French (where `/ɛː/` has mostly merged with `/ɛ/`) but is more robust and contrastive in Quebec French, where long vowels in stressed closed syllables also tend to diphthongize.

## Phonological Inventory

The complete phonemic inventory of Modern French, organized by IPA categories (2015 revision). Documented in parallel for two reference accents: **Standard Metropolitan French** (*français standard*, European/Parisian-based) and **Quebec French** (*français québécois*, Canadian). The consonant system is essentially shared across both accents; the principal phonetic divergence is the Quebec affrication of `/t d/` to `[t͡s d͡z]` before high front vocoids. The vowel systems diverge more substantially: Metropolitan French has largely lost the `/a/`~`/ɑ/` and `/ɛ̃/`~`/œ̃/` oppositions and tends to neutralise vowel-length and several mid-vowel contrasts, whereas Quebec French preserves the `/a/`~`/ɑ/` and `/ɛ̃/`~`/œ̃/` contrasts, laxes high vowels `[ɪ ʏ ʊ]` in closed syllables, and diphthongises long vowels. French stress is not lexical or contrastive: prominence falls on the final full syllable of a rhythmic group only and is therefore not marked on individual phonemes here.

### Consonant Phonemes

All consonant phonemes of Modern French arranged by place and manner of articulation. The consonant inventory is virtually identical between Standard Metropolitan French and Quebec French; the main difference is allophonic (Quebec affrication of dental `/t d/` before `/i y j ɥ/`).

**Total consonant phonemes:** 18 (17 fully native + 1 marginal)  
6 plosives `/p b t d k ɡ/` + 6 fricatives `/f v s z ʃ ʒ/` + 3 nasals `/m n ɲ/` + 1 lateral approximant `/l/` + 1 uvular fricative `/ʁ/` + the marginal velar nasal `/ŋ/` = 18. The velar nasal `/ŋ/` is marginal: it occurs almost exclusively in English loanwords (e.g. 'parking' `[paʁkiŋ]`, 'camping' `[kɑ̃piŋ]`) and word-final '-ing' borrowings, and is not native to the inherited French stock; counting only the native consonants gives 17. Note that not every '-ing' spelling yields `/ŋ/`: 'shampooing' is realised `/ʃɑ̃pwɛ̃/` with the nasal vowel `/ɛ̃/` and no `/ŋ/` at all, so it is a counter-example rather than an instance of `/ŋ/`. The rhotic `/ʁ/` is a voiced uvular fricative (the standard French R), realised as an approximant or even voiceless `[χ]` depending on context; older or rural varieties may use an apical trill `[r]`. The dental plosives `/t d/` are affricated to `[t͡s d͡z]` before the high front vowels and glides `/i y j ɥ/` in Quebec French (e.g. 'tu' `[t͡sy]`, 'dire' `[d͡ziːʁ]`) but not in Metropolitan French. The palatal nasal `/ɲ/` ('agneau') is increasingly realised as the sequence `[nj]` by younger Metropolitan speakers. Voiceless plosives `/p t k/` are unaspirated in French, unlike English. The semivowels `/j ɥ w/` are treated in the separate Semivowels section and are not included in this consonant count.

#### IPA Consonant Chart

IPA consonant chart for Modern French (rows = manner, columns = place). Where two symbols appear in a cell, voiceless precedes voiced. Semivowels `/j ɥ w/` are charted separately under Semivowels.

| Manner | Bilabial | Labiodental | Dental/Alveolar | Postalveolar | Palatal | Velar | Uvular |
|---|---|---|---|---|---|---|---|
| Plosive | p b |  | t d |  |  | k ɡ |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | ʁ |
| Lateral approximant |  |  | l |  |  |  |  |

*The velar nasal `/ŋ/` is shown in the velar column but is marginal (loanwords only). The dental plosives `/t d/` and nasal `/n/` and lateral `/l/` are dental in French though placed in the shared Dental/Alveolar column with the alveolar fricatives `/s z/`. The uvular `/ʁ/` occupies the uvular column. All 18 consonants are accounted for: p b t d k ɡ (6) + f v s z ʃ ʒ (6) + m n ɲ ŋ (4) + l (1) + ʁ (1) = 18. The three approximant glides `/j ɥ w/` are not included here; see Semivowels.*

#### Notes by Place of Articulation

- **Bilabial:** `/p b m/`. `/p/` as in 'pain', `/b/` as in 'bain'; both are unaspirated (no `[pʰ]`). `/m/` as in 'main'. The labial-velar glide `/w/` also has a bilabial component but is listed under semivowels.
- **Labiodental:** `/f v/`. `/f/` as in 'fou', `/v/` as in 'vous'. The only labiodental pair in the system; spellings include 'f', 'ff', 'ph' for `/f/` and 'v', 'w' (loanwords) for `/v/`.
- **Dental/Alveolar:** `/t d s z n l/`. French `/t d n l/` are laminal dental (not alveolar as in English), articulated with the tongue against the upper teeth. `/t/` as in 'tout', `/d/` as in 'doux', `/s/` as in 'sou', `/z/` as in 'zoo', `/n/` as in 'nous', `/l/` as in 'loup'. `/l/` is clear `[l]` in all positions (no dark/velarised `[ɫ]` coda allophone as in English). In Quebec French `/t/` and `/d/` are affricated to `[t͡s]` and `[d͡z]` before `/i y j ɥ/` ('petit' `[pət͡si]`, 'aujourd'hui' `[oʒuʁd͡zɥi]`); in the same context `/s z/` may show light assibilation. The fricatives `/s z/` are alveolar.
- **Postalveolar:** `/ʃ ʒ/`. `/ʃ/` as in 'chou' and `/ʒ/` as in 'joue'. Unlike English, French has no postalveolar affricates `/tʃ dʒ/` in native vocabulary; these occur only in loanwords ('match', 'jean') and are usually analysed as `/t/`+`/ʃ/` and `/d/`+`/ʒ/` sequences rather than unit phonemes.
- **Palatal:** `/ɲ/` is the palatal nasal as in 'agneau', 'montagne', 'gagner'. It is in retreat in Metropolitan French, where many younger speakers replace it with the cluster `[nj]`; it remains more robust word-medially and in Quebec. The palatal glide `/j/` is listed under semivowels.
- **Velar:** `/k ɡ ŋ/`. `/k/` as in 'cou' (spellings 'c', 'qu', 'k', 'ch' in Greek loans), `/ɡ/` as in 'goût' (spellings 'g', 'gu'); both unaspirated. `/ŋ/` is the marginal velar nasal found only in loanwords, chiefly English borrowings in '-ing' ('parking' `[paʁkiŋ]`, 'camping' `[kɑ̃piŋ]`); it does not occur in native French and is not part of the inherited inventory. Note that the '-ing' spelling does not guarantee `/ŋ/`: 'shampooing' is pronounced `/ʃɑ̃pwɛ̃/`, ending in the nasal vowel `/ɛ̃/` rather than `/ŋ/`, and so is a counter-example, not an instance of `/ŋ/`.
- **Uvular:** `/ʁ/` is the voiced uvular fricative, the standard French R as in 'roue', 'Paris', 'rare'. Its realisation varies allophonically: a voiced fricative or approximant `[ʁ̞]` between voiced sounds, a voiceless fricative `[χ]` adjacent to voiceless consonants or word-finally ('quatre' `[katχ]`). Conservative, regional, and older varieties (and some Quebec speakers, especially traditional Montreal) may retain an apical alveolar trill/tap `[r ɾ]`; the uvular variant is the modern standard in both Metropolitan and Quebec French.

### Semivowels

The three semivowels (glides) of French. Each corresponds to a high vowel and patterns as the non-syllabic counterpart of that vowel: `/j/` ~ `/i/`, `/ɥ/` ~ `/y/`, `/w/` ~ `/u/`. They contrast in pairs distinguished only by lip-rounding and front/back articulation. Their phonemic status is supported by minimal and near-minimal pairs, though in some analyses they are treated as positional realisations of the corresponding high vowels.

**Total semivowels:** 3  
`/j/` (palatal), `/ɥ/` (labio-palatal), `/w/` (labio-velar). The labio-palatal approximant `/ɥ/` is cross-linguistically rare and is one of the most distinctive features of French phonology. Minimal/near-minimal triplets demonstrate their independence: 'abeille' `[abɛj]`, 'huile' `[ɥil]`, 'oui' `[wi]`; and the contrast `/ɥi/` vs `/wi/` in 'huit' `[ɥit]` vs 'ouïe' `[wi]`. In Quebec French, `/j/` and `/ɥ/` trigger affrication of a preceding `/t d/` ('tien', 'duel').

#### IPA Semivowel Chart

IPA approximant (glide) chart for French semivowels, by place and lip-rounding.

| Manner | Palatal (unrounded) | Labio-palatal (rounded) | Labio-velar (rounded) |
|---|---|---|---|
| Approximant | j | ɥ | w |

*All three glides are voiced approximants. `/j/` is palatal and unrounded; `/ɥ/` is labio-palatal (front + rounded); `/w/` is labio-velar (back + rounded). Together with the high vowels `/i y u/` they form a tidy 3-by-2 system distinguished by backness and rounding.*

#### Semivowel Inventory

| IPA | Name | Corresponding Vowel | Rounding | Example | Distribution |
|---|---|---|---|---|---|
| `/j/` | voiced palatal approximant | `/i/` | unrounded | yeux `[jø]`, paille `[paj]`, travail `[tʁavaj]`, hier `[jɛʁ]` | Occurs in onsets and codas; very frequent. Spelled 'y', 'i' (before vowel), 'il'/'ill'. Arises from glide formation when `/i/` precedes a vowel. |
| `/ɥ/` | voiced labio-palatal approximant | `/y/` | rounded | huit `[ɥit]`, lui `[lɥi]`, nuit `[nɥi]`, puis `[pɥi]` | The non-syllabic counterpart of front rounded `/y/`; cross-linguistically rare. Occurs chiefly before a following vowel, prototypically before `/i/`. Arises from glide formation when `/y/` precedes a vowel. |
| `/w/` | voiced labio-velar approximant | `/u/` | rounded | oui `[wi]`, moi `[mwa]`, roi `[ʁwa]`, jouer `[ʒwe]` | The non-syllabic counterpart of back rounded `/u/`. Spelled 'ou' (before vowel), 'w' (loanwords), and is the second element of the 'oi' `[wa]` and 'oin' `[wɛ̃]` graphemes. Arises from glide formation when `/u/` precedes a vowel. |

### Vowel Phonemes

The vowel phonemes of Modern French, divided into oral vowels and nasal vowels and documented in parallel for Standard Metropolitan French and Quebec French. French is unusual among European languages in possessing a set of front rounded vowels `/y ø œ/` and a series of phonemic nasal vowels. The two reference accents differ in the size of the oral inventory (Metropolitan French has largely merged `/a/`~`/ɑ/`, while Quebec keeps them distinct) and in the nasal inventory (Metropolitan French has largely merged `/œ̃/` into `/ɛ̃/`, while Quebec preserves the four-way nasal contrast). Quebec additionally laxes high vowels to `[ɪ ʏ ʊ]` in closed syllables and diphthongises long vowels.

#### Oral Vowels

The oral (non-nasal) vowel phonemes of French, organised by height, backness and lip-rounding. The core system comprises three high vowels `/i y u/`, two pairs of mid vowels divided by the *loi de position* into close-mid `/e ø o/` and open-mid `/ɛ œ ɔ/`, the open vowel `/a/`, and the schwa `/ə/` (*e caduc*). The back open `/ɑ/` and the long open-mid `/ɛː/` are marginal in Metropolitan French (largely merged with `/a/` and `/ɛ/` respectively) but are robust phonemes in Quebec French.

**Metropolitan oral-vowel count:** 11 | **Quebec oral-vowel count:** 13  
Metropolitan oral-vowel count = 11: `/i e ɛ a ɔ o u y ø œ ə/`. Standard Metropolitan French has largely lost the back `/ɑ/` (so 'patte' and 'pâte' are homophonous as `/pat/` for many speakers) and the long `/ɛː/` (so 'mettre' and 'maître' merge to `/ɛ/`), and the `/ø/`~`/œ/` and `/e/`~`/ɛ/` and `/o/`~`/ɔ/` oppositions are partly governed by the *loi de position* and are unstable in some positions; counting these mergers gives the commonly cited Metropolitan total of around 11 oral qualities. Quebec oral-vowel count = 13: the same 11 plus the retained back open `/ɑ/` (so 'patte' `[pat]` vs 'pâte' `[pɑːt]`, with `/ɑ/` often diphthongised `[pɑʊ̯t]`) and the retained long open-mid `/ɛː/` ('mettre' `[mɛtʁ]` vs 'maître' `[mɛːtʁ]`), giving 13. In Quebec, high vowels `/i y u/` are laxed to `[ɪ ʏ ʊ]` in syllables closed by a non-lengthening consonant ('vite' `[vɪt]`, 'butte' `[bʏt]`, 'route' `[ʁʊt]`), and the long vowels `/ɑ ɛː o ø ɑ̃/` etc. diphthongise in closed stressed syllables (`[ɑʊ̯ ɛɪ̯ oʊ̯]`). The marginal status of `/ɑ/` and `/ɛː/` in Metropolitan French is the analog of the cot-caught instability noted for English; here the difference is between the two reference accents rather than within one.

##### Metropolitan Oral Vowel Chart

IPA vowel quadrilateral for Standard Metropolitan French oral monophthongs (rows = height, columns = backness/rounding). Front rounded vowels are listed in the front-rounded column. The schwa `/ə/` sits centrally.

| Height | Front (unrounded) | Front (rounded) | Central | Back (rounded) |
|---|---|---|---|---|
| close | i | y |  | u |
| close-mid | e | ø | ə | o |
| open-mid | ɛ | œ |  | ɔ |
| open | a |  |  |  |

##### Quebec Oral Vowel Chart

IPA vowel quadrilateral for Quebec French oral monophthongs (rows = height, columns = backness/rounding). Front rounded vowels are listed in the front-rounded column. The schwa `/ə/` sits centrally.

| Height | Front (unrounded) | Front (rounded) | Central | Back (rounded) |
|---|---|---|---|---|
| close | i | y |  | u |
| close-mid | e | ø | ə | o |
| open-mid | ɛ / ɛː | œ |  | ɔ |
| open | a |  |  | ɑ |

*Both accents share the front-rounded series `/y ø œ/`, which is the typological hallmark of French. Metropolitan French collapses the open vowels to a single `/a/` and lacks a distinct long `/ɛː/`; Quebec retains back open `/ɑ/` (open back, distinct from front `/a/`) and long `/ɛː/`. In Quebec the close vowels `/i y u/` have lax allophones `[ɪ ʏ ʊ]` in closed syllables (not separate phonemes), and long vowels diphthongise under stress. The distribution of close-mid `/e ø o/` versus open-mid `/ɛ œ ɔ/` is largely predictable from syllable structure (loi de position: close-mid in open syllables, open-mid in closed syllables) but is contrastive in some minimal pairs ('é' `/e/` vs 'è' `/ɛ/` in final open syllables: 'fée' `/fe/` vs 'fait' `/fɛ/`).*

##### Metropolitan Oral Vowel Inventory

These eleven oral vowels constitute the Standard Metropolitan French inventory.

| IPA | Height | Backness | Rounding | Example | Distribution |
|---|---|---|---|---|---|
| `/i/` | close | front | unrounded | si, vie, île | Close front unrounded vowel; tense and short. Quebec laxes it to `[ɪ]` in closed syllables. |
| `/e/` | close-mid | front | unrounded | été, fée, parler, nez | Close-mid front unrounded vowel ('é'). Occurs chiefly in open syllables; contrasts with `/ɛ/` in final open syllables ('fée' `/fe/` vs 'fait' `/fɛ/`). |
| `/ɛ/` | open-mid | front | unrounded | mère, faire, sept, lait | Open-mid front unrounded vowel ('è', 'ê', 'ai'). Occurs chiefly in closed syllables. In Metropolitan French it has absorbed the historical long `/ɛː/`. |
| `/a/` | open | front (central) | unrounded | patte, la, ami, salle | Open front/central unrounded vowel. In Metropolitan French it is the sole open vowel, having absorbed historical back `/ɑ/` ('patte' = 'pâte' = `/pat/` for most speakers). |
| `/ɔ/` | open-mid | back | rounded | sort, donner, bonne, col | Open-mid back rounded vowel. Occurs chiefly in closed syllables (loi de position); contrasts with `/o/` in some pairs ('sotte' `/sɔt/` vs 'saute' `/sot/`). |
| `/o/` | close-mid | back | rounded | mot, beau, rose, saute | Close-mid back rounded vowel. Occurs in open syllables and before `/z/`, spelled 'o', 'au', 'eau'. Phonetically long in closed syllables ('rose' `[ʁoːz]`). |
| `/u/` | close | back | rounded | fou, vous, route, tout | Close back rounded vowel ('ou'). Quebec laxes it to `[ʊ]` in closed syllables ('route' `[ʁʊt]`). |
| `/y/` | close | front | rounded | tu, vu, rue, sur | Close front ROUNDED vowel, a typological hallmark of French; contrasts with `/i/` ('si'/'su') and `/u/` ('vu'/'vous'). Quebec laxes it to `[ʏ]` in closed syllables and affricates a preceding `/t d/` ('tu' `[t͡sy]`). |
| `/ø/` | close-mid | front | rounded | peu, deux, jeûne, bleu | Close-mid front rounded vowel. Occurs chiefly in open syllables; contrasts with `/œ/` in some pairs ('jeûne' `/ʒøn/` vs 'jeune' `/ʒœn/`). |
| `/œ/` | open-mid | front | rounded | peur, sœur, jeune, neuf | Open-mid front rounded vowel. Occurs chiefly in closed syllables (loi de position). Its distribution with `/ø/` is largely positional. |
| `/ə/` | mid | central | rounded (mid) | le, je, petit, demain | The '*e caduc*' / schwa (*e muet*); phonetically close to `/ø/` in Metropolitan French. It is frequently deleted ('petit' `[pti]`) and its presence is governed by the *loi des trois consonnes*; occurs only in unstressed positions and never in word-final closed syllables. |

##### Quebec Additional Oral Vowels

Quebec French retains two further oral vowels beyond the eleven above, giving its total of 13. Both are marginal/merged in Standard Metropolitan French.

| IPA | Height | Backness | Rounding | Example | Distribution |
|---|---|---|---|---|---|
| `/ɑ/` | open | back | unrounded | pâte, âge, tas, gâteau | Open BACK unrounded vowel, retained as a distinct phoneme in Quebec (and conservative Metropolitan) French: 'patte' `[pat]` vs 'pâte' `[pɑːt]`. In Quebec it is typically long and often diphthongised to `[ɑʊ̯]` in closed stressed syllables. Marginal/merged into `/a/` in Standard Metropolitan French. |
| `/ɛː/` | open-mid (long) | front | unrounded | fête, maître, rêve, paître | Long open-mid front unrounded vowel, retained as distinct from short `/ɛ/` in Quebec (and conservative Metropolitan) French: 'mettre' `[mɛtʁ]` vs 'maître' `[mɛːtʁ]`, 'faite' `[fɛt]` vs 'fête' `[fɛːt]`. Often diphthongised `[ɛɪ̯]` in Quebec closed stressed syllables. Marginal/merged into `/ɛ/` in Standard Metropolitan French. |

#### Nasal Vowels

The phonemic nasal vowels of French, produced with lowering of the velum so that air escapes through the nose; they are written as a base vowel plus a combining tilde (U+0303). They derive historically from a vowel followed by a nasal consonant (VN), and in modern French the nasal consonant is no longer pronounced when the vowel is nasalised ('pain' `/pɛ̃/`, not `[pɛn]`). They are phonemically contrastive with their oral counterparts ('beau' `/bo/` vs 'bon' `/bɔ̃/`; 'lait' `/lɛ/` vs 'lin' `/lɛ̃/`).

**Metropolitan nasal-vowel count:** 3 | **Quebec nasal-vowel count:** 4  
Quebec nasal-vowel count = 4 (the full historical set, with all four kept distinct): `/ɛ̃ ɑ̃ ɔ̃ œ̃/`. Metropolitan nasal-vowel count = 3 for most contemporary speakers: the front rounded `/œ̃/` ('brun', 'un', 'parfum') has merged into unrounded `/ɛ̃/` ('brin', 'hein', 'pain'), so that 'brun' and 'brin' are homophones `/bʁɛ̃/`, leaving the three-way system `/ɛ̃ ɑ̃ ɔ̃/`. The `/œ̃/`~`/ɛ̃/` merger is the nasal analog of the oral `/a/`~`/ɑ/` merger: complete or near-complete in Standard Metropolitan French, but resisted in Quebec French, where 'brun' `/bʁœ̃/` stays distinct from 'brin' `/bʁɛ̃/`. Phonetic note: contemporary Parisian French has shifted the qualities of the nasal vowels, with `/ɛ̃/` often lowered/backed toward `[æ̃]` and `/ɔ̃/` raised/rounded toward `[õ]`; Quebec realisations differ (e.g. `/ɛ̃/` may be raised toward `[ẽ]`, `/ɑ̃/` fronted). All nasal vowels are phonemically long-ish and may diphthongise in Quebec closed stressed syllables.

| IPA | Name | Oral Counterpart | Rounding | Example | Distribution |
|---|---|---|---|---|---|
| `/ɛ̃/` | open-mid front nasal (unrounded) | `/ɛ/` | unrounded | pain, vin, main, fin, plein | Spelled 'in', 'im', 'ain', 'ein', 'yn', etc. In Metropolitan French it has absorbed the merged `/œ̃/`, so it also covers 'un', 'brun' for most speakers. Often realised `[æ̃]` (lowered) in modern Parisian speech. |
| `/ɑ̃/` | open back nasal (unrounded) | `/ɑ/` / `/a/` | unrounded | an, dans, temps, enfant, vent | Spelled 'an', 'am', 'en', 'em'. The lowest and backest nasal vowel; in Parisian French it tends to back and round toward `[ɒ̃]`. Diphthongises in Quebec closed stressed syllables (`[ɑ̃ʊ̯]`). |
| `/ɔ̃/` | open-mid to close-mid back nasal (rounded) | `/ɔ/` / `/o/` | rounded | bon, son, pont, nom, ombre | Spelled 'on', 'om'. In modern Parisian French it is raised and tensed toward `[õ]`, increasing the perceptual distance from `/ɑ̃/`. Contrasts with `/ɑ̃/` ('temps' `/tɑ̃/` vs 'thon' `/tɔ̃/`). |
| `/œ̃/` | open-mid front nasal (rounded) | `/œ/` | rounded | un, brun, parfum, lundi, chacun | Spelled 'un', 'um'. Kept distinct in Quebec French ('brun' `/bʁœ̃/` vs 'brin' `/bʁɛ̃/`) and in conservative/southern Metropolitan French, but MERGED into `/ɛ̃/` for most contemporary Standard Metropolitan (Parisian) speakers, who pronounce 'un' as `/ɛ̃/`. Listed as the fourth nasal vowel; marginal in Metropolitan French. |

## Consonants

The consonant phonemes of Modern French, documented in parallel for two reference accents: Standard Metropolitan French (français standard, the Parisian-based European norm) and Quebec French (français québécois, the Canadian norm). The core obstruent and nasal inventory is shared across both accents, so each phoneme carries a single set of IPA, place, manner and voicing values; accent-specific and context-specific surface realisations are recorded in the allophony notes. The most salient accent split is the Quebec affrication of `/t d/` to `[t͡s d͡z]` before the close front vowels and glides `/i y j ɥ/`, which is absent in Metropolitan French. Phonemic values are given in /slashes/ and phonetic realisations in [brackets], following IPA (2015 revision). The French rhotic `/ʁ/` is a voiced uvular fricative, the defining 'French R'; `/ŋ/` is marginal, occurring chiefly in English and other loanwords (parking, camping); and `/ɲ/` (palatal nasal, 'gn') is in retreat, increasingly merging with the sequence `/nj/`. French has no phonemic affricates, no dental fricatives `/θ ð/`, and no `/h/` (orthographic h is silent, though 'h aspiré' blocks liaison and elision without itself being pronounced). French stress is not lexical: it falls on the final full syllable of a rhythmic group, so it is not marked on individual words below.

**Consonant phonemes:** 18 | **Effective phonemes:** 17  
Seventeen consonants are fully native and contrastive (`/p b t d k ɡ f v s z ʃ ʒ m n ɲ l ʁ/`); `/ŋ/` is an eighteenth, marginal phoneme restricted to loanwords and not part of the inherited Latin-derived system. `/ɲ/` is increasingly unstable, varying with the sequence `/nj/`, so some analyses count the stable native inventory as effectively 16–17. French consonant spelling is heavily many-to-one and complicated by silent final consonants (the written -s, -t, -d, -p, -x of most word-final positions are not pronounced except in liaison), double letters that map to a single phoneme (-ll-, -tt-, -mm-), and digraphs (ch = `/ʃ/`, gn = `/ɲ/`, ph = `/f/`, qu = `/k/`). French has no phonemic affricates: the Quebec `[t͡s d͡z]` are allophones of `/t d/`, not separate phonemes.

### Consonant Inventory

The 18 consonant phonemes with their IPA value, phonetic name, spelling graphemes, example words (with IPA), and allophony notes. Where the JSON gives accent-specific transcriptions, both Standard Metropolitan and Quebec forms are shown.

| # | IPA | Name | Spellings | Example Words | Allophony Notes |
|---|---|---|---|---|---|
| 1 | `/p/` | voiceless bilabial plosive | p, pp | pain `/pɛ̃/`; appel `/a.pɛl/`; cap `/kap/` | Unaspirated `[p]` in all positions: unlike English, French voiceless stops have no aspiration in stressed onsets (pain `[pɛ̃]`, not `[pʰɛ̃]`), a hallmark of a French accent. Word-final stops are typically released, often with a light audible release burst or a trailing schwa-like offset in careful or southern Metropolitan speech (cap `[kap]` ~ `[kapə]`). Final -p is silent in many words (trop `/tʁo/`, coup `/ku/`) and pronounced only in others (cap, stop). Assimilates in voicing to a following obstruent across word/morpheme boundaries (e.g. 'cape grise' shows no change, but voiced contexts can briefly voice it). Quebec and Metropolitan pattern alike. |
| 2 | `/b/` | voiced bilabial plosive | b, bb | beau `/bo/`; abbé `/a.be/`; robe `/ʁɔb/` | Fully and actively voiced `[b]` in onset and between voiced sounds, with voicing maintained throughout the closure (French is a true-voicing language, contrasting voicing lead, not aspiration). Subject to regressive voicing assimilation: before a voiceless obstruent it devoices to `[b̥]`/`[p]` (e.g. 'absent' `[ap.sɑ̃]`, 'observer' `[ɔp.sɛʁ.ve]`). Word-finally `/b/` tends to keep its voicing more than in English but may be partially devoiced `[b̥]` before a pause. Devoices before the voiceless onset of a following word in connected speech. Same in Quebec and Metropolitan French. |
| 3 | `/t/` | voiceless alveolar plosive | t, tt, th, d (in liaison) | table `/tabl/`; petit `/pə.ti/`; tu `/ty/` (Metropolitan), `/t͡sy/` (Quebec) | Articulated as a true unaspirated dental-to-alveolar `[t]` (often laminal denti-alveolar `[t̪]`) and never flapped, unlike North American English `/t/`. Quebec French: `/t/` AFFRICATES to `[t͡s]` before the close front vowels and glides `/i y j ɥ/` ('tu' `[t͡sy]`, 'petit' `[pə.t͡si]`, 'tiens' `[t͡sjɛ̃]`, 'tuile' `[t͡sɥil]`); this is automatic and a defining feature of québécois, ABSENT from Metropolitan French where 'tu' is plain `[ty]`. In liaison, final orthographic -d is realised as `[t]` ('grand homme' `[ɡʁɑ̃.tɔm]`, 'quand il' `[kɑ̃.til]`). Final -t is silent in most words (petit `/pə.ti/`, chat `/ʃa/`) but pronounced in some (net, brut, est 'east'). Subject to regressive voicing assimilation, voicing to `[d]` before a voiced obstruent: this is clearest in fixed word-internal clusters ('anecdote' shows the parallel `/k/` → `[ɡ]` in `[a.nɛɡ.dɔt]`) and can also occur across a word boundary in fast connected speech (e.g. 'cette banque' `[sɛd.bɑ̃k]`). |
| 4 | `/d/` | voiced alveolar plosive | d, dd | dent `/dɑ̃/`; addition `/a.di.sjɔ̃/` (Metropolitan), `/a.d͡zi.sjɔ̃/` (Quebec); dur `/dyʁ/` (Metropolitan), `/d͡zyʁ/` (Quebec) | Fully voiced laminal dental-to-alveolar `[d̪]`/`[d]`, never flapped. Quebec French: `/d/` AFFRICATES to `[d͡z]` before `/i y j ɥ/` ('dur' `[d͡zyʁ]`, 'dire' `[d͡ziːʁ]`, 'dieu' `[d͡zjø]`, 'aujourd'hui' `[o.ʒuʁ.d͡zɥi]`), mirroring the `/t/` → `[t͡s]` rule; ABSENT in Metropolitan French ('dur' plain `[dyʁ]`). Subject to regressive voicing assimilation, devoicing to `[t]` before a voiceless obstruent ('médecin' `[met.sɛ̃]`, 'svelte' patterns). Word-finally `/d/` may be partly devoiced before a pause but keeps voicing more robustly than English. Final -d is usually silent (grand `/ɡʁɑ̃/`, pied `/pje/`) and surfaces as `[t]` in liaison. |
| 5 | `/k/` | voiceless velar plosive | c, qu, k, q, cc, ch (in Greek loans), ck | café `/ka.fe/`; qui `/ki/`; sac `/sak/` | Unaspirated `[k]` in all positions (qui `[ki]`, not `[kʰi]`). The place of articulation fronts toward palatal `[k̟]` before front vowels (qui, képi) and backs before back vowels (cou, car), but this is purely allophonic and non-contrastive. Spelled 'c' for `/k/` before a, o, u and consonants, but 'qu' before e, i and elsewhere; 'c' before e, i, y is `/s/`. Final -c is pronounced in many words (sac, lac, bec) but silent in others (tabac `/ta.ba/`, blanc `/blɑ̃/`, estomac `/ɛs.tɔ.ma/`). Subject to regressive voicing assimilation, voicing to `[ɡ]` before a voiced obstruent ('anecdote' `[a.nɛɡ.dɔt]`). Same in Quebec and Metropolitan French. |
| 6 | `/ɡ/` | voiced velar plosive | g, gu, gg, c (in 'second') | gare `/ɡaʁ/`; guerre `/ɡɛʁ/`; bague `/baɡ/` | Fully voiced `[ɡ]`, fronting to `[ɡ̟]` before front vowels (guêpe, guide) and backing before back vowels (gomme), non-contrastively. Spelled 'g' for `/ɡ/` before a, o, u and consonants, but 'gu' before e, i, y (guerre, guide); plain 'g' before e, i, y is `/ʒ/`. Subject to regressive voicing assimilation, devoicing to `[k]` before a voiceless obstruent. Word-finally may be partly devoiced `[ɡ̊]` before a pause. Final -g is generally silent (long `/lɔ̃/`, sang `/sɑ̃/`) and surfaces as `[k]` in rare liaison ('sang impur' `[sɑ̃.kɛ̃.pyʁ]`). Same in Quebec and Metropolitan French. |
| 7 | `/f/` | voiceless labiodental fricative | f, ff, ph | feu `/fø/`; café `/ka.fe/`; photo `/fɔ.to/` | Stable `[f]` in all positions, spelled 'f', 'ff', or 'ph' (in Greek-derived words: photo, philosophie). Final -f is usually pronounced (chef `/ʃɛf/`, neuf `/nœf/`) but goes silent in a few set forms: in 'œuf' `[œf]` / plural 'œufs' `[ø]` and 'bœuf' `[bœf]` / 'bœufs' `[bø]` the final consonant and vowel both change; in 'neuf' (nine) before a vowel-initial word, `/f/` exceptionally voices to `[v]` in liaison ('neuf heures' `[nœ.vœʁ]`, 'neuf ans' `[nœ.vɑ̃]`). Subject to regressive voicing assimilation. Same in Quebec and Metropolitan French. |
| 8 | `/v/` | voiced labiodental fricative | v, w (in some loans), f (in liaison of 'neuf') | vin `/vɛ̃/`; avril `/a.vʁil/`; rêve `/ʁɛv/` | Fully voiced `[v]` in onset and intervocalically. Subject to regressive voicing assimilation, devoicing to `[v̥]`/`[f]` before a voiceless obstruent. Word-finally `/v/` retains voicing better than its English counterpart but may partly devoice `[v̥]` before a pause. Spelled 'w' for `/v/` in some Germanic loans (wagon `/va.ɡɔ̃/`) though many w-loans use `/w/` (week-end `/wi.kɛnd/`). Same in Quebec and Metropolitan French. |
| 9 | `/s/` | voiceless alveolar sibilant fricative | s, ss, c (before e, i, y), ç, sc, t (in -tion), x (in 'six', 'dix') | sac `/sak/`; poisson `/pwa.sɔ̃/`; ça `/sa/` | Stable hissing `[s]` with many spellings: 's' initially and next to consonants, 'ss' between vowels (where single intervocalic 's' is `/z/`), 'c'/'ç' for the soft-c value (ça, ceci, leçon), 'sc' (science), and 't' in the -tion/-tie suffixes (nation `/na.sjɔ̃/`). Final -s is normally silent (les `/le/`, temps `/tɑ̃/`) but surfaces as `[z]` in liaison ('les amis' `[le.za.mi]`) and is pronounced `[s]` word-finally in some words (bus `/bys/`, fils `/fis/`, sens `/sɑ̃s/`). Subject to regressive voicing assimilation, voicing to `[z]` before a voiced obstruent ('Strasbourg' `[stʁaz.buʁ]`). Same in Quebec and Metropolitan French; note Quebec can show slight assibilation effects but `/s/` itself is plain. |
| 10 | `/z/` | voiced alveolar sibilant fricative | z, s (single, between vowels), x (in 'deuxième', liaison) | zéro `/ze.ʁo/`; maison `/mɛ.zɔ̃/`; chose `/ʃoz/` | Fully voiced buzzing `[z]`, spelled 'z' or as a single intervocalic 's' (maison, rose, base). It is the regular liaison value of an underlying final -s, -x or -z before a vowel ('les amis' `[le.za.mi]`, 'deux ans' `[dø.zɑ̃]`, 'chez elle' `[ʃe.zɛl]`). Subject to regressive voicing assimilation, devoicing to `[z̥]`/`[s]` before a voiceless obstruent. May partly devoice word-finally before a pause. Same in Quebec and Metropolitan French. |
| 11 | `/ʃ/` | voiceless postalveolar sibilant fricative | ch, sch (in loans), sh (in loans) | chat `/ʃa/`; chien `/ʃjɛ̃/` (Metropolitan), `/ʃjɛ̃/` (Quebec); vache `/vaʃ/` | Stable `[ʃ]`, typically with some lip rounding (labialisation), normally spelled 'ch' (chat, chien, riche); 'ch' is instead `/k/` in many Greek-derived words (chœur `/kœʁ/`, technique `/tɛk.nik/`, orchestre `/ɔʁ.kɛstʁ/`). Loans may use 'sh' (shampooing) or 'sch' (schéma `/ʃe.ma/`). Subject to regressive voicing assimilation, voicing to `[ʒ]` before a voiced obstruent. In some traditional/popular Quebec speech the contrast `/ʃ/`–`/s/` and `/ʒ/`–`/z/` can be weakened or these can desibilate slightly, but standard Quebec keeps `[ʃ]` as in Metropolitan French. |
| 12 | `/ʒ/` | voiced postalveolar sibilant fricative | j, g (before e, i, y), ge (before a, o, u) | jour `/ʒuʁ/`; girafe `/ʒi.ʁaf/`; rouge `/ʁuʒ/` | Fully voiced `[ʒ]`, usually labialised, spelled 'j' (jour, jeu), soft 'g' before e/i/y (girafe, géant, gymnastique), or 'ge' before a/o/u to preserve the soft value (mangeons `/mɑ̃.ʒɔ̃/`, gageure). Subject to regressive voicing assimilation, devoicing to `[ʒ̥]`/`[ʃ]` before a voiceless obstruent. May partly devoice word-finally before a pause (rouge `[ʁuʒ̥]`). In conservative/popular Quebec French `/ʒ/` may show slight desibilation or affrication tendencies, but standard usage matches Metropolitan `[ʒ]`. |
| 13 | `/m/` | voiced bilabial nasal | m, mm | main `/mɛ̃/`; femme `/fam/`; pomme `/pɔm/` | Fully voiced `[m]` in all positions. Crucially, an orthographic vowel + 'm'/'n' often spells a NASAL VOWEL rather than a vowel-plus-consonant sequence: word-finally or before a consonant 'am, em, om, im' etc. yield nasal vowels with no `[m]` pronounced (faim `/fɛ̃/`, nom `/nɔ̃/`, parfum `/paʁ.fœ̃/` or `/paʁ.fɛ̃/`), whereas double 'mm' or 'm' before a vowel gives a true `[m]` and an oral vowel (pomme `/pɔm/`, immense `/i.mɑ̃s/`). May be syllabic `[m̩]` in casual reduction before another consonant. Same in Quebec and Metropolitan French. |
| 14 | `/n/` | voiced alveolar nasal | n, nn | nez `/ne/`; année `/a.ne/`; bonne `/bɔn/` | Fully voiced alveolar `[n]`, laminal denti-alveolar `[n̪]` before dentals. As with `/m/`, vowel + 'n' word-finally or before a consonant typically spells a nasal vowel with no `[n]` surfacing (bon `/bɔ̃/`, vin `/vɛ̃/`, dans `/dɑ̃/`), while 'nn' or 'n' before a vowel gives true `[n]` and an oral vowel (bonne `/bɔn/`, année `/a.ne/`). `/n/` is the consonant that resurfaces in many liaisons of nasal-vowel words ('bon ami' `[bɔ.na.mi]`, often with denasalisation of the vowel). May be syllabic `[n̩]`. Same in Quebec and Metropolitan French. |
| 15 | `/ɲ/` | voiced palatal nasal | gn, ni (before vowel, variably) | agneau `/a.ɲo/`; montagne `/mɔ̃.taɲ/`; signe `/siɲ/` | A single palatal nasal `[ɲ]`, spelled 'gn' (agneau, montagne, peigne). It is increasingly UNSTABLE and in modern Metropolitan French frequently merges with the sequence `/nj/` = `[nj]` (so 'montagne' may be heard as `[mɔ̃.tanj]`, and 'gn' overlaps with words spelled 'ni' + vowel such as 'panier' `/pa.nje/`). Word-finally and before a consonant it can be realised with a palatal off-glide. Conservative and many Quebec speakers preserve a clearer distinct `[ɲ]`; the `/ɲ/` ~ `/nj/` variation is the main locus of variation. Note 'gn' is exceptionally `[ɡn]` in a few learned words (diagnostic `[djaɡ.nɔs.tik]`). |
| 16 | `/ŋ/` | voiced velar nasal | ng (in loanwords) | parking `/paʁ.kiŋ/`; camping `/kɑ̃.piŋ/`; shampooing `/ʃɑ̃.pwɛ̃/` | A MARGINAL phoneme, not native to the inherited French system; it occurs essentially only in English and other loanwords ending in '-ing' (parking, camping, jogging, smoking, meeting) and a few borrowings (gong, ping-pong). Frequently realised by speakers as `[ŋ]` but commonly reinforced or replaced by a following or substitute `[ɡ]` — `[ŋɡ]` or `[ŋk]` — especially in less anglicised pronunciations (parking `[paʁ.kiŋ]` ~ `[paʁ.kiŋɡ]`). Some speakers nativise the ending toward a nasal vowel. Quebec, with heavier English contact, tends to render a clean `[ŋ]`; Metropolitan realisations vary more. Note: the spelling 'shampooing' is exceptional and pronounced `/ʃɑ̃.pwɛ̃/`, not with `[ŋ]`. |
| 17 | `/l/` | voiced alveolar lateral approximant | l, ll | lit `/li/`; ville `/vil/`; sel `/sɛl/` | Realised as a CLEAR (non-velarised) `[l]` in all positions, including syllable codas — French has no 'dark' `[ɫ]`, so 'sel', 'mille', 'belle' all take the same clear `[l]`, unlike English. Devoiced to `[l̥]` after a voiceless obstruent in clusters, especially finally (peuple `[pœpl̥]`, table `[tabl̥]`, where the cluster `/pl/`, `/bl/` closes the word). May be syllabic `[l̩]` in such reductions. Note that 'll' after 'i' often spells the glide `/j/`, not `[l]` (fille `/fij/`, travailler `/tʁa.va.je/`), though some words keep `[l]` (ville `/vil/`, mille `/mil/`, tranquille `/tʁɑ̃.kil/`). In some popular/Quebec registers a final `/l/` in clitics (il, elle) may be dropped ('il' → `[i]`, 'elle' → `[a]` ~ `[ɛ]`), but standard `/l/` is clear `[l]` in both accents. |
| 18 | `/ʁ/` | voiced uvular fricative | r, rr, rh | rue `/ʁy/`; Paris `/pa.ʁi/`; mère `/mɛʁ/` | The 'French R', phonemically a voiced uvular fricative `/ʁ/` but with a wide allophonic range: voiced uvular fricative `[ʁ]`, a more open uvular approximant `[ʁ̞]` (very common intervocalically and in onsets), a voiceless uvular fricative `[χ]` when adjacent to voiceless consonants or word-finally after a pause (quatre `[katχ]`, lettre `[lɛtχ]`), and a uvular trill `[ʀ]` in emphatic, operatic, or some conservative speech. Devoices fully to `[χ]` in voiceless clusters (e.g. 'prêt' `[pχɛ]`, 'trois' `[tχwa]`). Historically French had an apical/alveolar trill `[r]`, now retained only in some rural, Occitan-influenced, older southern Metropolitan, and certain traditional registers. Quebec French: classically used an apical/alveolar `[r]` (the 'R roulé' of older and rural Quebec), but the uvular `[ʁ]` has become dominant in modern urban Quebec, especially Montreal, so both accents now converge on uvular realisations with `[r]` as a recessive variant. Final `/ʁ/` in the cluster of an infinitive-type ending is usually present (parler keeps it), but the -er infinitive ending and many -er nouns are `/e/` with NO `/ʁ/` pronounced (parler `/paʁ.le/`, boucher `/bu.ʃe/`). |

### Natural Classes

Groupings of the consonant phonemes by shared phonological features, drawn from the source data.

| Class | Members |
|---|---|
| Plosives | `/p/`, `/b/`, `/t/`, `/d/`, `/k/`, `/ɡ/` |
| Fricatives | `/f/`, `/v/`, `/s/`, `/z/`, `/ʃ/`, `/ʒ/`, `/ʁ/` |
| Nasals | `/m/`, `/n/`, `/ɲ/`, `/ŋ/` |
| Lateral approximants | `/l/` |
| Obstruents | `/p/`, `/b/`, `/t/`, `/d/`, `/k/`, `/ɡ/`, `/f/`, `/v/`, `/s/`, `/z/`, `/ʃ/`, `/ʒ/`, `/ʁ/` |
| Sonorants | `/m/`, `/n/`, `/ɲ/`, `/ŋ/`, `/l/` |
| Voiceless | `/p/`, `/t/`, `/k/`, `/f/`, `/s/`, `/ʃ/` |
| Voiced | `/b/`, `/d/`, `/ɡ/`, `/v/`, `/z/`, `/ʒ/`, `/ʁ/`, `/m/`, `/n/`, `/ɲ/`, `/ŋ/`, `/l/` |
| Sibilants | `/s/`, `/z/`, `/ʃ/`, `/ʒ/` |
| Labials | `/p/`, `/b/`, `/f/`, `/v/`, `/m/` |
| Coronals | `/t/`, `/d/`, `/s/`, `/z/`, `/ʃ/`, `/ʒ/`, `/n/`, `/l/` |
| Dorsals | `/k/`, `/ɡ/`, `/ɲ/`, `/ŋ/`, `/ʁ/` |

> **On the lateral-approximant class:** French has no non-lateral consonantal approximants. `/l/` is the only consonantal approximant in the inventory, and the glides `/j ɥ w/` (the only other approximant-like segments) are treated as semivowels in a separate section. The class is therefore labelled 'lateral approximants' rather than the looser 'approximants'.

## Oral Vowels

The French oral (non-nasal) vowel inventory, organized by phonetic dimensions (height, backness, rounding) rather than by lexical sets, which are an English-specific device. Two reference accents are documented in parallel, mirroring the GA/RP pairing of the English guide:

- **Metropolitan (METRO)** — Standard Metropolitan French (*français standard*, European, Parisian-based).
- **Quebec (QUEBEC)** — Quebec French (*français québécois*, Canadian).

French has an unusually large oral-vowel system featuring three FRONT ROUNDED vowels `/y ø œ/` that are typologically rare. The phonemic inventory is `/i e ɛ a ɔ o u y ø œ ə/`, with two further vowels — long `/ɛː/` and back `/ɑ/` — that are phonemic for conservative and Quebec speakers but largely lost in Metropolitan French (see the Metropolitan/Quebec notes on the relevant entries).

The distribution of the close~open mid-vowel pairs `/e/`~`/ɛ/`, `/ø/`~`/œ/` and `/o/`~`/ɔ/` is governed by a syllable-structure principle, the **loi de position** (*law of position*): close-mid in open syllables, open-mid in closed syllables, with lexical exceptions. `/ə/` (*e caduc* / schwa) is special in being deletable. Nasal vowels `/ɛ̃ ɑ̃ ɔ̃ œ̃/` are treated in a separate section.

All values are IPA (2015 revision); `/slashes/` mark phonemic transcription and `[brackets]` mark phonetic detail. Length is marked with `/ː/`.

> **Note on stress:** French stress is not lexical or contrastive — it falls predictably on the final full syllable of a rhythmic group — so no stress marks are placed on the individual citation words below.

### Vowel Classes

French oral vowels can be grouped along three articulatory dimensions. By **backness/rounding**: front unrounded, front rounded, and back (the back group is defined by backness only, since `/ɑ/` is unrounded while `/u o ɔ/` are rounded). By **height**: close, close-mid, open-mid, and open. A separate functional class is the unstable *e caduc* `/ə/` — a front-of-central rounded vowel and the only deletable vowel; it is listed under "unstable" rather than "front rounded" to keep its central/unstable status clear. The three close~open mid pairs form the locus of the loi de position.

| Class | Members |
|---|---|
| Front unrounded | `/i/` `/e/` `/ɛ/` `/a/` |
| Front rounded | `/y/` `/ø/` `/œ/` |
| Back | `/u/` (rounded), `/o/` (rounded), `/ɔ/` (rounded), `/ɑ/` (unrounded) |
| Mid pairs (loi de position) | `/e/`~`/ɛ/`, `/ø/`~`/œ/`, `/o/`~`/ɔ/` |
| Unstable | `/ə/` |

### Loi de Position Overview

The **loi de position** (*law of position*) is the syllable-structure tendency governing the three mid-vowel pairs. In a phonetically OPEN syllable (one ending in a vowel) the CLOSE-mid member is favoured (`/e ø o/`); in a phonetically CLOSED syllable (one ending in a consonant) the OPEN-mid member is favoured (`/ɛ œ ɔ/`). It is a strong distributional tendency, not an exceptionless law: numerous lexical and morphological exceptions exist (e.g. lexical `/ɛ/` in open syllables for some speakers, `/o/` before `/z/` as in *rose* `/ʁoz/`, `/ø/` before `/z/` as in *creuse* `/kʁøz/`), and the mid pairs remain marginally phonemic.

| Syllable type | Favoured mid vowels |
|---|---|
| Open syllable (ends in vowel) | `/e/` `/ø/` `/o/` |
| Closed syllable (ends in consonant) | `/ɛ/` `/œ/` `/ɔ/` |

**Marginal minimal pairs** (showing the mid pairs are still phonemic):

| Pair | Transcription |
|---|---|
| *épée* vs *épais* | `/epe/` vs `/epɛ/` |
| *jeune* vs *jeûne* | `/ʒœn/` (jeune) vs `/ʒøn/` (jeûne) |
| *pomme* vs *paume* | `/pɔm/` (pomme) vs `/pom/` (paume) |

- **Metropolitan:** Metropolitan French applies the loi de position fairly consistently, and the close~open distinction is heavily neutralized in many positions; the `/e/`~`/ɛ/` contrast in final open syllables (*é* vs *è/ai*) is weakening for many younger Parisian speakers, who may merge them toward `[e]`~`[ɛ]` regardless of spelling.
- **Quebec:** Quebec French preserves the mid-vowel oppositions more robustly and the loi de position applies with characteristic Quebec refinements: open-mid vowels in closed syllables are often lowered/laxed, and long close-mid vowels in closed syllables diphthongize (e.g. *fête* `[faɛ̯t]`, *pâte* `[pɑʊ̯t]`, *neutre* `[nøy̯tʁ]`).

### Oral Vowel Inventory

The full underlying inventory is `/i e ɛ (ɛː) a (ɑ) ɔ o u y ø œ ə/`. The table below covers each vowel with its phonetic class, articulatory description, example words, and the parallel Metropolitan and Quebec realizations. Where the loi de position governs a vowel, that is noted in the final column.

| IPA | Class | Description | Examples | Metropolitan | Quebec | Loi de position |
|---|---|---|---|---|---|---|
| `/i/` | close front unrounded | Close front unrounded vowel `[i]`. Spread lips, tongue high and front. Tenser and shorter than English FLEECE; a pure monophthong with no offglide. | *lit* `/li/`, *midi* `/midi/`, *ville* `/vil/` | Steady close `[i]` in all positions. In a final stressed (rhythm-group-final) closed syllable it may be slightly lengthened before a voiced fricative (*vive* `[viːv]`) but does not laxen. | Laxes to `[ɪ]` in a CLOSED syllable (Quebec lax-high-vowel rule): *vite* `[vɪt]`, *ville* `[vɪl]`. Stays tense `[i]` in open syllables (*midi* `[midi]`) and when lengthened/diphthongized before a voiced lengthening consonant (*livre* `[liːvʁ]`~`[lɪi̯vʁ]`). Note also Quebec affrication: `/t d/` become `[t͡s d͡z]` before `/i/`, so *petit* = `[pət͡si]`, *dix* = `[d͡zɪs]`. | — |
| `/y/` | close front rounded | Close front ROUNDED vowel `[y]` — one of the three typologically rare French front rounded vowels. Articulated like `/i/` (high, front, spread-tongue position) but with rounded, protruded lips. Contrasts with both `/i/` (*lit* `/li/` vs *lu* `/ly/`) and `/u/` (*rue* `/ʁy/` vs *roue* `/ʁu/`); the `/y/`~`/u/` contrast is a classic difficulty for English learners, who lack `/y/`. | *lu* `/ly/`, *rue* `/ʁy/`, *tu* `/ty/` | Steady close front rounded `[y]` in all positions. The corresponding glide is `/ɥ/` (e.g. *huit* `/ɥit/`, *lui* `/lɥi/`). | Laxes to `[ʏ]` in a CLOSED syllable (*jupe* `[ʒʏp]`, *lutte* `[lʏt]`); stays tense `[y]` in open syllables (*tu* `[ty]`) and when lengthened/diphthongized before a voiced lengthening consonant. Quebec affrication applies: `/t d/` become `[t͡s d͡z]` before `/y/`, so *tu* = `[t͡sy]`, *du* = `[d͡zy]`. | — |
| `/u/` | close back rounded | Close back rounded vowel `[u]`. Tongue high and back, strong lip rounding. Purer and often less back-diphthongal than English GOOSE. Spelled `<ou>`. Contrasts with `/y/` (*roue* `/ʁu/` vs *rue* `/ʁy/`). | *loup* `/lu/`, *vous* `/vu/`, *roue* `/ʁu/` | Steady close back `[u]` in all positions. The corresponding glide is `/w/` (e.g. *oui* `/wi/`, *jouer* `/ʒwe/`). | Laxes to `[ʊ]` in a CLOSED syllable (*toute* `[tʊt]`, *rouge* may lengthen/diphthongize as `[ʁuːʒ]`~`[ʁʊu̯ʒ]`); stays tense `[u]` in open syllables (*vous* `[vu]`). Quebec also shows variable nasal-context laxing/centralization. | — |
| `/e/` | close-mid front unrounded | Close-mid front unrounded vowel `[e]` (cardinal-2-like), tenser and without the offglide of English FACE. The close-mid member of the e/ɛ pair. Spelled `<é>`, and `<-er -ez -ai>` in many endings. Favoured in open syllables. | *été* `/ete/`, *parler* `/paʁle/`, *nez* `/ne/` | Realized `[e]`. For many younger Metropolitan speakers the final-open-syllable `/e/`~`/ɛ/` contrast is weakening, so *fée*, *fait* and *fais* may all tend toward `[e]` or a merged mid value; in pre-tonic syllables `/e/` and `/ɛ/` are widely neutralized. | Realized `[e]` in open syllables and kept distinct from `/ɛ/`. Quebec maintains the `/e/`~`/ɛ/` opposition robustly; in final open syllables conservative Quebec usage keeps *fée* `[fe]` vs *fait* `[fɛ]`. | By the loi de position, `[e]` is the expected mid front vowel in OPEN syllables (*été* `/ete/`, *parler* `/paʁle/`); in closed syllables the open-mid `/ɛ/` appears (*faire* `/fɛʁ/`). The `/e/`~`/ɛ/` opposition is therefore largely predictable, surfacing contrastively mainly in final open syllables (*épée* `/epe/` vs *épais* `/epɛ/`). |
| `/ɛ/` | open-mid front unrounded | Open-mid front unrounded vowel `[ɛ]` (cardinal-3-like), similar to English DRESS but a pure monophthong. The open-mid member of the e/ɛ pair. Spelled `<è ê ai ei et>` and elsewhere. Favoured in closed syllables. | *mère* `/mɛʁ/`, *faire* `/fɛʁ/`, *treize* `/tʁɛz/` | Realized `[ɛ]`; short. The historical LONG counterpart `/ɛː/` (spelled `<ê>`, `<ai>`+C, as in *fête*, *maître*) has merged with short `/ɛ/` for nearly all Metropolitan speakers, so *mettre* and *maître* are homophonous `/mɛtʁ/`; vowel length is no longer phonemic in Metropolitan French. | Realized `[ɛ]`, and Quebec often LOWERS it toward `[æ]`~`[a]` in closed syllables (*mère* `[maɛ̯ʁ]`~`[maʁ]`). Crucially, Quebec PRESERVES the long `/ɛː/` vs short `/ɛ/` contrast: long `/ɛː/` diphthongizes in closed syllables, so *fête* `[faɛ̯t]`~`[fɛːt]` is distinct from *faite* `[fɛt]`, and *maître* `/mɛːtʁ/` is distinct from *mettre* `/mɛtʁ/`. | By the loi de position, `[ɛ]` is the expected mid front vowel in CLOSED syllables (*mère* `/mɛʁ/`, *sept* `/sɛt/`), complementary to `/e/` in open syllables. Lexical/morphological exceptions place `/ɛ/` in some open syllables (final `<-ai/-ais/-ait>` for many speakers, *parfait* `/paʁfɛ/`). |
| `/ɛː/` | open-mid front unrounded, long | Long open-mid front unrounded vowel `[ɛː]` — the historical long counterpart of short `/ɛ/`. Marginal/recessive: phonemic only where the long~short contrast survives. Spelled `<ê>` (*fête*, *tête*), `<ai>`+consonant (*maître*), and in a few `<-aître/-aine>` words. | *fête* `/fɛːt/`, *maître* `/mɛːtʁ/`, *tête* `/tɛːt/` | LOST in Metropolitan French: `/ɛː/` has merged with short `/ɛ/`, eliminating phonemic vowel length. *fête* `/fɛt/` = *faite* `/fɛt/`; *maître* `/mɛtʁ/` = *mettre* `/mɛtʁ/`. The circumflex is now purely orthographic for these speakers. | RETAINED in Quebec French as a genuine phonemic long vowel, and characteristically DIPHTHONGIZED in closed syllables: *fête* `[faɛ̯t]`, *tête* `[taɛ̯t]`, *maître* `[maɛ̯tʁ]`. The contrast *fête* (long) vs *faite* (short) is maintained. | Outside the loi de position proper: where retained, `/ɛː/` contrasts with short `/ɛ/` in the SAME closed-syllable position, so it is a residual length opposition rather than a height alternation. |
| `/a/` | open front (central) unrounded | Open front-to-central unrounded vowel `[a]` — the default, far more frequent of the two French open vowels. Fronter and lower than English TRAP; close to cardinal 4. The unmarked `/a/` that has absorbed most former `/ɑ/` words in Metropolitan French. | *patte* `/pat/`, *la* `/la/`, *table* `/tabl/` | Realized as central `[a]`~`[ä]`. The `/a/`~`/ɑ/` contrast is LARGELY MERGED: most speakers have a single open vowel `[a]`, so *patte* and *pâte* are commonly homophonous `/pat/`, with `/ɑ/` surviving only residually/optionally for some (often older or careful) speakers in a limited word set. | Realized as a clear FRONT `[a]` in most positions, and Quebec KEEPS `/a/` distinct from back `/ɑ/`. Word-finally in an open syllable, Quebec `/a/` may BACK and round toward `[ɑ]`~`[ɔ]` (*Canada* `[kanadɑ]`, *là* `[lɑ]`) — a separate, position-conditioned phenomenon — but the phonemic `/a/`~`/ɑ/` opposition (*patte* vs *pâte*) is preserved. | — |
| `/ɑ/` | open back (rounded-ish) unrounded | Open back unrounded (sometimes faintly rounded) vowel `[ɑ]` — the marked, recessive *a postérieur*. Tongue retracted and low, darker timbre than `/a/`. Historically distinct in words spelled `<â>` (*pâte*), `<as/asse>` (*classe*), and in some `<-ation>` contexts. | *pâte* `/pɑt/`, *âme* `/ɑm/`, *bas* `/bɑ/` | LARGELY MERGED into `/a/` in Metropolitan French: the `/a/`~`/ɑ/` opposition has collapsed for most speakers, so *patte* = *pâte* = `/pat/`. Where it survives it is a sociolinguistic/lexical residue (some speakers keep *pâte* `/pɑt/`, *âme* `/ɑm/`, sentence-final *bas* `/bɑ/`), but it is no longer reliably contrastive and the circumflex is largely orthographic. | RETAINED and robust in Quebec French: `/ɑ/` is clearly distinct from front `/a/`, so *pâte* `/pɑt/` ≠ *patte* `/pat/`, *tâche* ≠ *tache*. In a CLOSED syllable Quebec `/ɑ/` characteristically diphthongizes/rounds toward `[ɑʊ̯]`~`[ɑɔ̯]` (*pâte* `[pɑʊ̯t]`). This is one of the salient vowel differences between Quebec and Metropolitan French. | — |
| `/o/` | close-mid back rounded | Close-mid back rounded vowel `[o]` (cardinal-7-like), pure monophthong without the English GOAT offglide. The close-mid member of the o/ɔ pair. Spelled `<ô>`, `<au/eau>`, and `<o>` in open syllables. Favoured in open syllables. | *mot* `/mo/`, *beau* `/bo/`, *rose* `/ʁoz/` | Realized close-mid `[o]`. The `/o/`~`/ɔ/` contrast is alive mainly in final closed syllables (*saute* `/sot/` vs *sotte* `/sɔt/`, *paume* `/pom/` vs *pomme* `/pɔm/`) but is neutralized in non-final/pre-tonic syllables. | Realized `[o]`, kept distinct from `/ɔ/`. When long (e.g. before `/z/`) and in closed syllables it lengthens and diphthongizes: *rose* `[ʁoːz]`~`[ʁou̯z]`, *pôle* `[poːl]`~`[pou̯l]`. Word-final `/o/` stays a clean `[o]` (*mot* `[mo]`). | By the loi de position, `[o]` is favoured in OPEN syllables (*mot* `/mo/`, *pot* `/po/`) and is complementary to `/ɔ/` in closed syllables. Systematic exceptions: `<ô>` and `<au>` are `[o]` even when closed (*côte* `/kot/`, *saute* `/sot/`), and `/o/` regularly appears before `/z/` (*rose* `/ʁoz/`, *chose* `/ʃoz/`). Minimal pair: *paume* `/pom/` vs *pomme* `/pɔm/`. |
| `/ɔ/` | open-mid back rounded | Open-mid back rounded vowel `[ɔ]` (cardinal-6-like), opener and laxer than `/o/`, similar in quality to RP LOT but as a stable monophthong. The open-mid member of the o/ɔ pair. Spelled `<o>` in most closed syllables. Favoured in closed syllables. | *botte* `/bɔt/`, *pomme* `/pɔm/`, *sort* `/sɔʁ/` | Realized open-mid `[ɔ]` in closed syllables. Does not occur word-finally in open syllables (where `/o/` appears instead); neutralized with `/o/` pre-tonically. | Realized `[ɔ]`, kept distinct from `/o/`, and often somewhat lowered. In closed syllables it remains short and stable (*botte* `[bɔt]`); the contrast with `/o/` (*cote* `/kɔt/` vs *côte* `/kot/`) is preserved. | By the loi de position, `[ɔ]` is favoured in CLOSED syllables (*botte* `/bɔt/`, *sort* `/sɔʁ/`), complementary to `/o/` in open syllables. Exceptions follow spelling (`<o>` before `/z/` → `/o/`, `<au>` → `/o/`), giving residual minimal pairs like *sotte* `/sɔt/` vs *saute* `/sot/`. |
| `/ø/` | close-mid front rounded | Close-mid front ROUNDED vowel `[ø]` — the second of the three rare French front rounded vowels. Articulated like `/e/` (close-mid, front) but with lip rounding; the rounded counterpart of `/e/` and the close-mid member of the ø/œ pair. Spelled `<eu>` and `<œu>`. Favoured in open syllables. | *peu* `/pø/`, *deux* `/dø/`, *jeûne* `/ʒøn/` | Realized close-mid rounded `[ø]`. The `/ø/`~`/œ/` contrast is largely predictable by the loi de position, surfacing contrastively in the small *jeûne*/*jeune* type set. | Realized `[ø]`, kept distinct from `/œ/`. When long in a closed syllable it diphthongizes: *neutre* `[nøy̯tʁ]`, *creuse* `[kʁøːz]`~`[kʁøy̯z]`. Open-syllable `/ø/` stays a clean `[ø]` (*peu* `[pø]`). | By the loi de position, `[ø]` is favoured in OPEN syllables (*peu* `/pø/`, *deux* `/dø/`) and is complementary to `/œ/` in closed syllables. Exceptions: `/ø/` occurs in closed syllables before `/z/` (*creuse* `/kʁøz/`), before `/t/` (*meute* `/møt/`), and in `<-eux>` endings, and in *jeûne* `/ʒøn/`. Minimal pair: *jeûne* `/ʒøn/` vs *jeune* `/ʒœn/`. |
| `/œ/` | open-mid front rounded | Open-mid front ROUNDED vowel `[œ]` — the third rare French front rounded vowel. Articulated like `/ɛ/` (open-mid, front) but with lip rounding; the rounded counterpart of `/ɛ/` and the open-mid member of the ø/œ pair. Spelled `<eu>` and `<œu>` in closed syllables. Favoured in closed syllables. (Distinct from schwa `/ə/`, with which it is phonetically very close.) | *peur* `/pœʁ/`, *jeune* `/ʒœn/`, *sœur* `/sœʁ/` | Realized open-mid rounded `[œ]` in closed syllables. It is phonetically very close to schwa `/ə/`; many analyses treat unstressed `/ə/` as effectively the same quality as `/œ/` (see schwa entry). | Realized `[œ]`, kept distinct from `/ø/`, and may be somewhat lowered/laxed in closed syllables (*peur* `[pœːʁ]`~`[paœ̯ʁ]` with lengthening before `/ʁ/`). The *jeune*/*jeûne* opposition is maintained. | By the loi de position, `[œ]` is favoured in CLOSED syllables (*peur* `/pœʁ/`, *jeune* `/ʒœn/`, *sœur* `/sœʁ/`), complementary to `/ø/` in open syllables. The principal lexical contrast is *jeune* `/ʒœn/` vs *jeûne* `/ʒøn/`. |
| `/ə/` | mid front-of-central rounded (*e caduc* / schwa); unstable/deletable | The *e caduc* ("unstable e"), also called *e muet* or schwa. Phonetically a mid front-of-central ROUNDED vowel, in French typically `[ə]`~`[œ]`~`[ø]` — i.e. rounded, unlike English schwa, and articulated forward of true central (close to the `/œ/`~`/ø/` region). Its defining property is DELETABILITY: it alternates with zero. Spelled `<e>` with no accent (*le*, *petit*, *samedi*, final *porte*). Grouped under "unstable" rather than "front rounded" since its deletability and central-ish quality set it apart from the stable front rounded vowels `/y ø œ/`. | *le* `/lə/`, *petit* `/pəti/`, *samedi* `/samdi/` | When pronounced, Metropolitan `/ə/` is rounded `[ə]`~`[œ̈]` and is frequently DELETED, especially in casual speech and in word-final position (*porte* `/pɔʁt/`, not `*/pɔʁtə/`, except in some Southern Metropolitan / Midi French which retains final schwa: *porte* `[pɔʁtə]`). It often merges in quality with `/œ/`. | Quebec `/ə/` is likewise deletable and rounded; it is frequently dropped in the same prosodic conditions (*petit* `[pt͡si]` with the `/t/` then affricating before `/i/`). When retained it patterns with the `/œ/`~`/ø/` region as in Metropolitan French. | Outside the loi de position: `/ə/` does not participate in the close~open mid alternation. Its quality, when realized, hovers near `/œ/`~`/ø/`; its distinctive behaviour is alternation with zero, not height conditioning. |

#### Deletability of `/ə/`

`/ə/` is the only deletable French vowel. It drops freely where consonant clusters remain pronounceable: *samedi* `/samdi/` (schwa dropped), *petit* `[p(ə)ti]`, final *porte* `/pɔʁt/`. Deletion is constrained by the **loi des trois consonnes** (the schwa is generally kept to avoid three consecutive consonants) and by rhythm/register. In phrases, alternating schwas are dropped in alternation (*je ne te le demande pas* → variable retention).

### The `/a/`~`/ɑ/` Merger

The `/a/` (*a antérieur*, front) vs `/ɑ/` (*a postérieur*, back) opposition. Historically two distinct open vowels: front `/a/` (*patte*, *la*) and back `/ɑ/` (*pâte*, *âme*, *bas*). Spelling clues for historical `/ɑ/` include `<â>` and word-final `<-as>`.

| Accent | Status |
|---|---|
| Metropolitan | LARGELY MERGED to a single front-central `[a]` for most speakers; *patte* = *pâte* = `/pat/`. `/ɑ/` survives only as a residual, variable, often sociolectal/lexical feature. |
| Quebec | PRESERVED: front `/a/` vs back `/ɑ/` remain contrastive (*patte* `/pat/` vs *pâte* `/pɑt/`). Quebec additionally backs final-open-syllable `/a/` toward `[ɑ]` and diphthongizes closed-syllable `/ɑ/` toward `[ɑʊ̯]`. |

**Example pair:** *patte* `/pat/` vs *pâte* `/pɑt/`.

### Vowel Length

Vowel length in French is NOT independently phonemic in Metropolitan French: it is mostly an automatic effect of the following consonant (*allongement* — vowels lengthen before the voiced "lengthening" consonants `/ʁ v z ʒ/` and before `/vʁ/`) and is therefore predictable. The one historical phonemic length opposition was `/ɛ/` vs `/ɛː/` (*faite* vs *fête*).

| Accent | Status |
|---|---|
| Metropolitan | Phonemic length LOST: `/ɛː/` has merged with `/ɛ/`, so *fête* `/fɛt/` = *faite* `/fɛt/`. Remaining length is purely allophonic (predictable lengthening before `/ʁ v z ʒ/`: *rêve* `[ʁɛːv]`, *rose* `[ʁoːz]`). |
| Quebec | Phonemic length RETAINED for `/ɛː/` vs `/ɛ/` (*fête* vs *faite*) and reflected in a system of "long" vowels that DIPHTHONGIZE in closed syllables: `/ɛː ø o ɑ/` and lengthened high vowels surface as `[aɛ̯ øy̯ ou̯ ɑʊ̯]` etc. (*fête* `[faɛ̯t]`, *neutre* `[nøy̯tʁ]`, *pâte* `[pɑʊ̯t]`, *rose* `[ʁou̯z]`). |

**Lengthening consonants:** `/ʁ/`, `/v/`, `/z/`, `/ʒ/`, `/vʁ/`.

### Quebec Features Overview

Systematic Quebec-French realizations affecting the oral vowels, distinguishing them from Metropolitan French.

| Feature | Description |
|---|---|
| Lax high vowels | `/i y u/` laxen to `[ɪ ʏ ʊ]` in CLOSED syllables (*vite* `[vɪt]`, *jupe* `[ʒʏp]`, *toute* `[tʊt]`); they stay tense in open syllables. |
| Diphthongization | Long vowels (notably `/ɛː ø o ɑ œ/` before lengthening consonants and in closed syllables) diphthongize: *fête* `[faɛ̯t]`, *neutre* `[nøy̯tʁ]`, *rose* `[ʁou̯z]`, *pâte* `[pɑʊ̯t]`. |
| Affrication | `/t d/` become affricates `[t͡s d͡z]` before the high front/close vowels and glides `/i y j ɥ/`: *petit* `[pət͡si]`, *tu* `[t͡sy]`, *dire* `[d͡zɪːʁ]`, *dur* `[d͡zyʁ]`. |
| Preserved contrasts | Quebec keeps the `/a/`~`/ɑ/` opposition and (in the nasal-vowel section) the `/ɛ̃/`~`/œ̃/` opposition, both of which are largely merged in Metropolitan French; it also keeps the long/short `/ɛː/`~`/ɛ/` contrast. |
| Final-vowel backing | Word-final open-syllable `/a/` may back/round toward `[ɑ]`~`[ɔ]` (*Canada* `[kanadɑ]`, *là* `[lɑ]`). |

### IPA Symbol Summary

Quick reference of the French oral-vowel phonemes by accent. Bracketed symbols are marginal/recessive in the given variety.

| Accent | Oral vowel phonemes |
|---|---|
| Metropolitan | `/i/` `/e/` `/ɛ/` `/a/` `/ɔ/` `/o/` `/u/` `/y/` `/ø/` `/œ/` `/ə/` |
| Metropolitan (marginal) | (`/ɛː/` — merged into `/ɛ/`), (`/ɑ/` — merged into `/a/`) |
| Quebec | `/i/` `/e/` `/ɛ/` `/ɛː/` `/a/` `/ɑ/` `/ɔ/` `/o/` `/u/` `/y/` `/ø/` `/œ/` `/ə/` |

The full underlying inventory is `/i e ɛ (ɛː) a (ɑ) ɔ o u y ø œ ə/`. Metropolitan French has collapsed `/ɛː/`→`/ɛ/` and `/ɑ/`→`/a/` for most speakers (11-vowel system); Quebec French retains both, giving a 13-vowel oral system, and additionally adds the lax allophones `[ɪ ʏ ʊ]` and diphthongal realizations of long vowels in closed syllables. The three front rounded vowels `/y ø œ/` and the deletable schwa `/ə/` are present in both varieties.

## Nasal Vowels

French nasal vowels are phonemic vowels produced with the velum lowered so that the airstream resonates simultaneously through the mouth and the nasal cavity, contrasting with the corresponding oral vowels. They form a distinctive subsystem of the French vowel inventory and occupy the structural slot that closing/centring diphthongs occupy in English: that is, they are the language's signature, cross-linguistically marked vowel set. Standard French has NO phonemic diphthongs; every vowel, oral or nasal, is a steady-state monophthong, so where English contrasts FACE/PRICE/GOAT etc., French contrasts oral versus nasal monophthongs. The system has three nasal vowels that are stable across all reference accents (`/ɛ̃/`, `/ɑ̃/`, `/ɔ̃/`) and a fourth, `/œ̃/`, whose status is the principal point of divergence between the two reference accents: most of Metropolitan France has merged `/œ̃/` into `/ɛ̃/` (so 'brun' = 'brin'), while Quebec French, Belgian French, and conservative/older Metropolitan speakers keep `/œ̃/` distinct. Nasal vowels arise historically and synchronically from the nasalization rule: an oral vowel followed by a coda nasal consonant (orthographic n or m) within the same syllable nasalizes, and the conditioning n/m is then itself NOT pronounced (it leaves only the nasalization on the vowel). In IPA the nasal vowels are written as a base oral-vowel symbol plus a COMBINING TILDE, Unicode U+0303 (e.g. `/ɛ/` + U+0303 = `/ɛ̃/`), not as a vowel followed by a separate nasal consonant.

### Inventory

The four-way nasal-vowel system `/ɛ̃ ɑ̃ ɔ̃ œ̃/`. The first three are stable across both reference accents; `/œ̃/` is the marginal fourth vowel whose phonemic status differs between Standard Metropolitan French and Quebec French (see the merger note below).

| IPA | Name | Type | Spelling patterns | Examples | Description |
|---|---|---|---|---|---|
| `/ɛ̃/` | front nasal (IN) | nasal monophthong | in, im (before p/b), yn, ym, ain, aim, ein, eim, and — in the merged dialects that have absorbed `/œ̃/` — also un, um. The nasalizing n/m is silent. The nasal value holds only when the n/m is in coda position; a following vowel (or doubled nn/mm) blocks nasalization and the vowel is read orally with an oral [n]/[m] ('vin' `/vɛ̃/` but 'vinaigre' `/vinɛɡʁ/`; 'plein' `/plɛ̃/` but 'pleine' `/plɛn/`). | vin `/vɛ̃/`; pain `/pɛ̃/`; plein `/plɛ̃/` | Open-mid-to-near-open front unrounded nasalized vowel; the nasal counterpart of `/ɛ/` (with a fairly open, fronted tongue position; in modern Parisian speech often realized phonetically as [æ̃]), articulated with a lowered velum. It is a steady monophthong, never a diphthong. |
| `/ɑ̃/` | back nasal (AN) | nasal monophthong | an, am (before p/b), en, em (before p/b). The nasalizing n/m is silent. Nasalization is blocked by a following vowel or geminate ('an' `/ɑ̃/` but 'année' `/ane/`; 'dent' `/dɑ̃/` but 'dentaire' `/dɑ̃tɛʁ/` keeps the nasal because the n is still in coda). Word-final spellings -ent in verb 3rd-person plural endings are silent altogether (they do not give `/ɑ̃/`): 'ils mangent' `/il mɑ̃ʒ/`. | an `/ɑ̃/`; temps `/tɑ̃/`; dent `/dɑ̃/` | Open back (slightly rounded in Metropolitan) nasalized vowel; the nasal vowel with the most open, retracted tongue position, articulated with a lowered velum. A steady monophthong. |
| `/ɔ̃/` | round back nasal (ON) | nasal monophthong | on, om (before p/b). The nasalizing n/m is silent. Nasalization is blocked by a following vowel or geminate ('bon' `/bɔ̃/` but 'bonne' `/bɔn/`; 'son' `/sɔ̃/` but 'sonner' `/sɔne/`). | on `/ɔ̃/`; bon `/bɔ̃/`; pont `/pɔ̃/` | Close-mid-to-open-mid back rounded nasalized vowel; the nasal counterpart of the rounded back oral vowels, articulated higher and more rounded than `/ɑ̃/`, with a lowered velum. A steady monophthong. |
| `/œ̃/` | round front nasal (UN) | nasal monophthong | un, um (the latter mainly word-finally, e.g. 'parfum'). The nasalizing n/m is silent. In dialects that preserve `/œ̃/`, these spellings are the (almost) exclusive source of the vowel; in merged dialects the same un/um spellings are simply read as `/ɛ̃/`. | un `/œ̃/` (merged Metropolitan `/ɛ̃/`); brun `/bʁœ̃/` (merged Metropolitan `/bʁɛ̃/`); parfum `/paʁfœ̃/` (merged Metropolitan `/paʁfɛ̃/`) | Open-mid front rounded nasalized vowel; the nasal counterpart of `/œ/`, articulated with a lowered velum, front tongue position, and lip rounding. A steady monophthong. This is the fourth, marginal nasal vowel whose phonemic status differs between the reference accents. |

### Reference-accent realization

The two reference accents differ both in the phonetic quality of the three stable nasals and, crucially, in whether `/œ̃/` exists as a separate phoneme.

| IPA | Standard Metropolitan French | Quebec French |
|---|---|---|
| `/ɛ̃/` | Realized fairly open and somewhat raised/centralized, commonly transcribed phonetically as [æ̃] in modern Parisian speech, so 'vin' is often heard as [væ̃]. Because most of Metropolitan France has undergone the `/œ̃/`~`/ɛ̃/` merger, `/ɛ̃/` has absorbed the historical `/œ̃/` class: 'brun' [bʁɛ̃] = 'brin' [bʁɛ̃], 'un' [ɛ̃]. The merged `/ɛ̃/` is thus the single front nasal of most younger and Parisian speakers. | Keeps `/ɛ̃/` distinct from `/œ̃/` (see `/œ̃/` below) and typically realizes `/ɛ̃/` closer and fronter than Metropolitan, often around [ẽ]~[ɛ̃] rather than the open Parisian [æ̃]. Like all long/stressable Quebec vowels, `/ɛ̃/` may undergo allophonic diphthongization in stressed closed syllables (e.g. 'pain' phrase-finally toward [pãɛ̃]~[paɛ̃]); this is a phonetic property of the dialect, not a phonemic diphthong (see dialect_differences). |
| `/ɑ̃/` | Back and somewhat rounded and raised, frequently realized phonetically toward [ɒ̃]~[ɑ̃]; it contrasts clearly with the more open/front `/ɛ̃/` and the higher rounded `/ɔ̃/`. This vowel is stable and not affected by the `/œ̃/`~`/ɛ̃/` merger. | Realized as a notably fronter, more open [ã] in many speakers (sometimes perceived as close to a fronted [a]-quality), a salient marker of the Canadian accent. In stressed closed syllables it commonly diphthongizes allophonically toward [ãʊ̃]~[aũ] ('grande' [ɡʁãʊ̃d]); again an allophonic phonetic diphthongization, not a phonemic diphthong (see dialect_differences). |
| `/ɔ̃/` | Realized rather close and tightly rounded, often phonetically closer to [õ] than to a fully open-mid [ɔ̃], which keeps it well separated from `/ɑ̃/`. It is stable and unaffected by the `/œ̃/`~`/ɛ̃/` merger. | Also has `/ɔ̃/` as a distinct close rounded back nasal; it may be realized slightly more open or more diphthongized than Metropolitan in stressed closed syllables (toward [õʊ̃]), an allophonic long-vowel diphthongization rather than a phonemic diphthong (see dialect_differences). |
| `/œ̃/` | In most of Metropolitan France, and especially among younger and Parisian speakers, `/œ̃/` has MERGED into `/ɛ̃/`: the historical brun/brin contrast is lost and 'brun' = 'brin' = [bʁɛ̃], 'un' = [ɛ̃]. Functionally `/œ̃/` therefore no longer exists as a separate phoneme for most Metropolitan speakers, which reduces the standard nasal-vowel system to three (`/ɛ̃ ɑ̃ ɔ̃/`). A distinct `/œ̃/` survives only among conservative, older, southern, or regional Metropolitan speakers. | KEEPS `/œ̃/` distinct from `/ɛ̃/` (like Belgian French): 'brun' `/bʁœ̃/` and 'brin' `/bʁɛ̃/` remain a minimal pair, and 'un' is `/œ̃/`. The four-way nasal system `/ɛ̃ ɑ̃ ɔ̃ œ̃/` is intact. As elsewhere in Quebec, `/œ̃/` may diphthongize allophonically in stressed closed syllables, a phonetic effect distinct from any phonemic diphthong (see dialect_differences). |

### The /ɛ̃/~/œ̃/ Merger

The fourth nasal vowel `/œ̃/` is the chief point of divergence between the two reference accents:

- **Standard Metropolitan French:** Largely MERGED `/œ̃/` into `/ɛ̃/`. The historical brun/brin contrast is lost — 'brun' = 'brin' = [bʁɛ̃], 'un' = [ɛ̃] — reducing the standard nasal system to three (`/ɛ̃ ɑ̃ ɔ̃/`). A distinct `/œ̃/` survives only among conservative, older, southern, or regional speakers. In merged dialects, the un/um spellings that historically gave `/œ̃/` are simply read as `/ɛ̃/`.
- **Quebec French:** KEEPS the four-way distinction `/ɛ̃ ɑ̃ ɔ̃ œ̃/` (as do Belgian French and conservative Metropolitan varieties). 'brun' `/bʁœ̃/` and 'brin' `/bʁɛ̃/` remain a minimal pair, and 'un' is `/œ̃/`.

### Nasalization Rule

Synchronic and historical source of the nasal vowels: an oral vowel followed by a CODA nasal consonant (orthographic n or m) within the same syllable becomes a nasal vowel, and the conditioning n/m is then NOT pronounced (it surfaces only as nasalization on the preceding vowel). Nasalization is BLOCKED when the n/m is followed by a vowel (it then begins the next syllable and is pronounced as an oral [n]/[m] with an oral vowel) or when the consonant is doubled (nn/mm): compare 'bon' `/bɔ̃/` (silent n, nasal vowel) with 'bonne' `/bɔn/` and 'bonifier' `/bɔnifje/` (pronounced n, oral vowel); 'plein' `/plɛ̃/` with 'pleine' `/plɛn/`; 'an' `/ɑ̃/` with 'année' `/ane/`. The orthographic m variant appears regularly before p and b (em, im, om, um as in 'temps', 'simple', 'tomber', 'parfum').

### Orthography (IPA Notation)

In this guide and in IPA generally, French nasal vowels are written as a base oral-vowel symbol carrying a COMBINING TILDE, Unicode code point U+0303 (COMBINING TILDE): `/ɛ̃/` = ɛ + U+0303, `/ɑ̃/` = ɑ + U+0303, `/ɔ̃/` = ɔ + U+0303, `/œ̃/` = œ + U+0303. The tilde marks nasalization of the vowel itself; it is NOT a following nasal consonant. Do not transcribe a French nasal vowel as vowel + [n]/[m] (e.g. 'vin' is `/vɛ̃/`, never \*`/vɛn/`).

### No Phonemic Diphthongs

Standard French has NO phonemic closing or centring diphthongs: contrasts that English carries on diphthongs (FACE, PRICE, GOAT, NEAR, SQUARE, CURE) have no counterpart here. Every French vowel, oral or nasal, is a steady-state monophthong; apparent vowel+glide sequences (e.g. 'travail' `/tʁavaj/`, 'huit' `/ɥit/`, 'oui' `/wi/`) are vowel-plus-semivowel (`/j ɥ w/`) sequences, not unitary diphthong phonemes. The nasal vowels documented here occupy the structural slot that diphthongs hold in the parallel English guide precisely because they, rather than any diphthong, are French's distinctive marked vowel subsystem. Quebec French does exhibit ALLOPHONIC diphthongization of long/stressable vowels (oral and nasal) in stressed closed syllables (e.g. 'père' [paɛ̯ʁ], 'pâte' [pɑʊ̯t], 'grande' [ɡʁãʊ̃d]); this is a low-level phonetic realization of underlying monophthongs, not a set of contrastive diphthong phonemes. See dialect_differences for the full treatment of Quebec long-vowel diphthongization and the `/a/`~`/ɑ/` and `/ɛ̃/`~`/œ̃/` contrasts.

### Summary

French nasal vowels (`/ɛ̃ ɑ̃ ɔ̃/`, plus marginal `/œ̃/`) are the phonologically distinctive vowel subsystem of the language and stand in the structural position that diphthongs occupy in English, even though French has no phonemic diphthongs. Three nasals (`/ɛ̃ ɑ̃ ɔ̃/`) are stable across both reference accents. The fourth, `/œ̃/`, is the chief accent difference: Standard Metropolitan French has largely MERGED `/œ̃/` into `/ɛ̃/` (brun = brin = [bʁɛ̃]), reducing its nasal system to three, whereas Quebec French (with Belgian and conservative Metropolitan varieties) keeps the four-way distinction `/ɛ̃ ɑ̃ ɔ̃ œ̃/`. All nasal vowels arise by the nasalization rule (oral vowel + silent coda n/m), are written with a base vowel plus the combining tilde U+0303, and are pure monophthongs; Quebec adds only allophonic long-vowel diphthongization, not phonemic diphthongs.

## Semivowels (Glides)

French has three semivowels (also called glides or approximants): `/j/`, `/ɥ/` and `/w/`. They are documented here in parallel for the two reference accents of this guide — **Standard Metropolitan French** (*français standard*, European/Parisian-based) and **Quebec French** (*français québécois*, Canadian). These are non-syllabic approximants that pattern with consonants in the syllable (they occupy onset or off-glide positions and never form a syllable nucleus), yet each corresponds articulatorily to one of the three high vowels: `/j/` to `/i/`, `/ɥ/` to `/y/`, and `/w/` to `/u/`. The labio-palatal approximant `/ɥ/` is cross-linguistically rare and is one of the most characteristic sounds of French.

Phonemic values are given in `/slashes/` and phonetic realisations in `[brackets]`, following the IPA (2015 revision). Because French stress is fixed and phrase-final (not lexical), no stress marks appear on individual glides or words. The two reference accents share the same three-glide inventory; their differences lie in distribution and in the consonantal context — most notably Quebec affrication of `/t d/` to `[t͡s d͡z]` before `/j/` and `/ɥ/` (and before `/i y/`).

**Inventory:** 3 glides — `/j ɥ w/` (effective phoneme count: 3).

### The Three Glides

| IPA | Name | Spellings | Examples | Derivation |
|-----|------|-----------|----------|------------|
| `/j/` | voiced palatal approximant (yod) | `i` + vowel (pied, lion, miel); `y` + vowel (yeux, voyage); `-il` finally after a vowel (travail, soleil); `-ill-` after a vowel (paille, fille, oreille, abeille); `-ill-` after a consonant usually = `/ij/` (famille, billet) — exceptions ville `/vil/`, mille `/mil/`, tranquille `/tʁɑ̃kil/`; word-initial `y-` (yaourt, yacht); `j` (loanwords, rare) | paille `/paj/` (Met. citation; conservative `/pɑj/`; Quebec `/paj/`~`/pɑj/`), "straw"; fille `/fij/`, "girl, daughter"; yeux `/jø/`, "eyes" | Non-syllabic realisation of `/i/` before another vowel: `/i/` + V → `[j]` + V when not preceded by an obstruent + liquid cluster (scier `/sje/`, pied `/pje/`). After a consonant + liquid cluster the high vowel stays syllabic and `[j]` is inserted: plier `/pli.je/`, crier `/kʁi.je/`, oublier `/ublije/`. `/j/` also arises lexically after a vowel as an off-glide (`-il`, `-ill-`: travail `/tʁavaj/`, paille `/paj/`), where it is not derived from a following vowel. |
| **`/ɥ/`** ⚠️ *rare* | **voiced labio-palatal approximant** (ué / glide of "huit") | `u` + vowel where `<u>` = `/y/` glided (huit, lui, nuit, puis, depuis); `u` + `i` is the prototypical context — `-ui-` (lui, nuit, fruit, bruit, juin); `u` + other vowels (tuer `/tɥe/`, muet `/mɥɛ/`, nuage `/nɥaʒ/`, situation `/sitɥasjɔ̃/`) | huit `/ɥit/`, "eight"; lui `/lɥi/`, "him / to him"; nuit `/nɥi/`, "night" | Non-syllabic realisation of `/y/` before another vowel, prototypically before `/i/`. `/y/` + V → `[ɥ]` + V when not blocked by a preceding obstruent + liquid cluster: tuer `/ty/` → `/tɥe/`, lui `/lɥi/`, nuage `/nɥaʒ/`. After a consonant + liquid cluster `/y/` stays syllabic and does NOT glide: cruel `/kʁy.ɛl/` (not *`/kʁɥɛl/`), truelle `/tʁy.ɛl/`. Most consistent before `/i/` (`-ui-`); before other vowels speakers vary between `[ɥ]` and a fuller `[y]`. |
| `/w/` | voiced labio-velar approximant (glide of "oui" / "oua") | `ou` + vowel where `<ou>` = `/u/` glided (oui, ouest, jouer, fouet, Louis); `oi` = `/wa/` (roi, moi, trois, voiture, boire); `oî` = `/wa/` (boîte `/bwat/`); `oin` = `/wɛ̃/` (loin, point, coin, soin); `w` in loanwords (week-end, kiwi, wagon `/vagɔ̃/` — note `<w>` = `/v/` in some loans); `oê` / `oe` (rare: moelle `/mwal/`, poêle `/pwal/`) | oui `/wi/`, "yes"; roi `/ʁwa/`, "king"; moi `/mwa/`, "me" | Non-syllabic realisation of `/u/` before another vowel: joue `/ʒu/` → jouer `/ʒwe/`, oui `/wi/`, ouest `/wɛst/`. A preceding obstruent + liquid cluster blocks gliding and keeps `/u/` syllabic: cloué `/klu.e/`, brouette `/bʁu.ɛt/` (not *`/bʁwɛt/`). The spellings `<oi>` `/wa/` and `<oin>` `/wɛ̃/` are frozen lexical sequences in which `/w/` does not alternate with a syllabic `/u/`. |

> ⚠️ **The rare glide `/ɥ/`.** Few of the world's languages contrast a front-rounded glide `/ɥ/` with `/w/`, which makes `/ɥ/` highly characteristic of French. Articulatorily `/ɥ/` = `/w/` with the tongue body fronted (palatal instead of velar) while keeping lip rounding; it is the glide counterpart of front-rounded `/y/`. It is the most restricted of the three glides: it occurs essentially only in onset position before a vowel and **never** as a syllable-final off-glide (there is no *`/Vɥ/`* coda).

### Vowel–Glide Correspondence

Each glide is the non-syllabic counterpart of a high vowel; the three high vowels and the three glides differ only in syllabicity.

| Vowel | Glide | Shared features | Example |
|-------|-------|-----------------|---------|
| `/i/` | `/j/` | front, unrounded, high/close | scier `/sje/` ~ si `/si/` |
| `/y/` | `/ɥ/` | front, rounded, high/close | tuer `/tɥe/` ~ tu `/ty/` |
| `/u/` | `/w/` | back, rounded, high/close | jouer `/ʒwe/` ~ joue `/ʒu/` |

### Distribution and Rounding/Place Contrast

`/j/`, `/ɥ/` and `/w/` are distinguished by lip rounding and frontness/backness, mirroring the `/i/`–`/y/`–`/u/` contrast:

- **`/j/` = unrounded front.** The most frequent and least restricted glide. It occurs both as an onset glide before a vowel AND as a coda/off-glide after a vowel (ail `/aj/`, travail `/tʁavaj/`, soleil `/sɔlɛj/`), and after consonant + liquid clusters.
- **`/ɥ/` = rounded front.** `/ɥ/` is essentially `[w]` articulated with the tongue body in front (palatal) rather than back (velar). The rarest of the three: it never occurs as a syllable-final off-glide and is largely restricted to onset position before a vowel, prototypically before `/i/`.
- **`/w/` = rounded back.** Moderately frequent. Like `/ɥ/` it occurs only as an onset glide before a vowel, not as a syllable-final off-glide. It is found in very high-frequency words via `<oi>` = `/wa/` (moi, toi, roi, voir) and `<oin>` = `/wɛ̃/` (loin, point).

### Minimal and Near-Minimal Pairs

The phonemic status of the glides is partly debatable: in many contexts a glide is the predictable non-syllabic realisation of a high vowel before another vowel (derived `/j ɥ w/`). But the following pairs — together with post-consonantal glides before a vowel — show they must be listed as independent segments.

| Contrast | Pair | Note |
|----------|------|------|
| `/ɥi/` vs `/wi/` | lui `/lɥi/` vs Louis `/lwi/` | front-rounded vs back-rounded glide before `/i/` — the clearest `/ɥ/`~`/w/` minimal pair |
| `/ɥi/` vs `/wi/` | huit `/ɥit/` vs ouïe `/wi/` (or "oui" `/wi/`) | near-minimal; "huit" begins with the front-rounded glide, "oui/ouïe" with the back-rounded glide |
| `/ɥ/` vs `/j/` | muette `/mɥɛt/` vs miette `/mjɛt/` | rounded vs unrounded front glide |
| `/w/` vs `/ɥ/` | fouine `/fwin/` vs juin `/ʒɥɛ̃/` (near-minimal) | back-rounded vs front-rounded glide |
| glide vs full vowel (syllabicity) | lions `/ljɔ̃/` (1 syll., glide) — noun "lions" = verb "nous lions" (we tie) — vs "nous liions" `/li.jɔ̃/` (2 syll. in the ending, imperfect "we were tying") | shows the glide `/j/` is contrastive with syllabic `/i/`: "liane" `/ljan/` is one syllable with the glide, while the hiatus pronunciation `/li.an/` is two; likewise "lions" `/ljɔ̃/` (1 syll.) vs the disyllabic ending of "liions" `/li.jɔ̃/` |

### Phonetic Notes by Glide

**`/j/` — yod.** The most stable of the three glides across both accents. Unlike `/ɥ/` and `/w/`, `/j/` occurs both as an onset glide before a vowel and as a coda/off-glide after a vowel (ail `/aj/`, travail `/tʁavaj/`, soleil `/sɔlɛj/`). After a vowel, a sequence vowel + `/j/` is sometimes analysed as a closing diphthong but is standardly `/Vj/`. Devoiced `[j̥]` after voiceless consonants (pied `[pj̥e]`). **Quebec:** before `/j/`, the dental stops `/t d/` affricate to `[t͡s d͡z]` when the underlying trigger is a front high vowel context; plain `/t d/` + `/j/` from `<ti, di>` (e.g. tiens `/tjɛ̃/`) may surface as `[t͡sjɛ̃]` for some speakers — affrication is most robust before `/i y/` and the glides derived from them.

**`/ɥ/` — labio-palatal glide.** Cross-linguistically rare and highly characteristic of French (see callout above). Key contrasts: lui `/lɥi/` vs Louis `/lwi/` (vs `/w/`), and muette `/mɥɛt/` vs miette `/mjɛt/` (vs `/j/`). Devoiced `[ɥ̥]` after voiceless stops (puis `[pɥ̥i]`). In careful or southern Metropolitan speech `/ɥ/` may be partly resyllabified toward `[y]`. **Quebec:** before `/ɥ/` the dental stops `/t d/` affricate to `[t͡s d͡z]` (tuile `[t͡sɥil]`, réduit `[ʁed͡zɥi]`); this affrication before `/y/`-derived glides is one of the most salient *québécois* traits.

**`/w/` — labio-velar glide.** Doubly articulated (lip rounding + back/velar tongue body); the back-rounded counterpart of `/ɥ/`. Key `/w/`~`/ɥ/` contrast: Louis `/lwi/` vs lui `/lɥi/`; oui `/wi/` vs huit `/ɥit/`. The nasal context `<oin>` = `/wɛ̃/` holds in both accents. Devoiced `[w̥]` after voiceless stops (trois `[tʁw̥ɑ]`). Unlike English, French has no `/ʍ/` ("wh") and no contrast of voiced vs voiceless `/w/`. **Quebec:** the `/wa/` of `<oi>` shows notable variation — alongside standard `[wa]` one hears older/regional `[we]` and `[wɛ]` (e.g. moi, toi, roi), and in some words historical `[wɛ]` is now standard (e.g. droit).

### Cross-Accent Summary

| Feature | Standard Metropolitan French | Quebec French |
|---------|------------------------------|---------------|
| Glide inventory | All three glides `/j ɥ w/` present with the distribution above | Same three-glide inventory; `/ɥ/`~`/w/`~`/j/` three-way rounding/place contrast preserved exactly |
| `/t d/` before high front glides | No affrication of `/t d/` before high front glides | Dental stops `/t d/` affricate to `[t͡s d͡z]` before `/j/` and `/ɥ/` and before `/i y/` (tuile `[t͡sɥil]`, dieu `[d͡zjø]`) |
| `/ɥ/` | Fully maintained as a distinct front-rounded glide | Maintained; affrication before `/y/`-derived glides is a salient marker |
| `<oi>` = `/wa/` | `[wa]` is the standard realisation | `[wa]` plus additional regional variants `[we]`/`[wɛ]` |
| Other | — | Long vowels adjacent to glides may diphthongise in stressed closed syllables |

## Consonant–Vowel IPA Matrix

Matrice systématique de combinaisons consonne + voyelle (CV) en API pour les consonnes du français appariées à un ensemble représentatif de 8 voyelles orales. Chaque cellule donne la chaîne API de la consonne suivie de la voyelle de référence. Les transcriptions sont phonémiques (entre barres obliques au niveau conceptuel) ; consulter le `phonetic_note` de chaque consonne pour les réalisations allophoniques principales. La matrice couvre 20 consonnes (17 consonnes pleines + 3 semi-voyelles `/j ɥ w/`) × 8 voyelles. Pour les consonnes dont la réalisation diffère entre le français standard métropolitain et le français québécois (notamment l'affrication de `/t d/` devant `/i y/`), un champ « Combinaisons (Québec) » distinct est fourni ; en l'absence de ce champ, les combinaisons sont identiques dans les deux accents. Certaines cellules (ex. `/ɲ/` à l'initiale absolue, `/ji/`, `/wu/`, `/ɥy/`) sont marginales ou phonotactiquement rares et figurent uniquement pour la complétude systématique.

- **Reference accent:** Standard Metropolitan French
- **Secondary reference accent:** Quebec French (français québécois)
- **Transcription level:** phonemic

### Reference Vowels

Les huit voyelles de référence utilisées comme colonnes de la matrice. Les qualités vocaliques suivent les valeurs du français standard métropolitain (base parisienne).

| Vowel | Name | Example | Note |
|---|---|---|---|
| i | voyelle fermée antérieure non arrondie | lit `/li/` | fermée, antérieure, étirée ; brève en français standard. En syllabe fermée, laxée en `[ɪ]` en français québécois (« vite » `[vɪt]`). |
| e | voyelle mi-fermée antérieure non arrondie | thé `/te/`, été `/ete/` | mi-fermée, antérieure ; surtout en syllabe ouverte. S'oppose à `/ɛ/`, opposition partiellement neutralisée chez certains locuteurs métropolitains. |
| ɛ | voyelle mi-ouverte antérieure non arrondie | mer `/mɛʁ/`, lait `/lɛ/` | mi-ouverte, antérieure ; typiquement en syllabe fermée. Une variante longue `/ɛː/` (« maître ») subsiste surtout en québécois et se diphtongue `[aɪ̯]`. |
| a | voyelle ouverte antérieure non arrondie | patte `/pat/`, la `/la/` | ouverte, antérieure/centrale. L'opposition `/a/`~`/ɑ/` est largement neutralisée en français standard métropolitain mais maintenue en français québécois. |
| ɔ | voyelle mi-ouverte postérieure arrondie | sort `/sɔʁ/`, botte `/bɔt/` | mi-ouverte, postérieure, arrondie ; typiquement en syllabe fermée. S'oppose à `/o/` (« saute » `/sot/` vs « sotte » `/sɔt/`). |
| u | voyelle fermée postérieure arrondie | loup `/lu/`, tout `/tu/` | fermée, postérieure, arrondie. En syllabe fermée, laxée en `[ʊ]` en français québécois (« toute » `[tʊt]`). |
| y | voyelle fermée antérieure arrondie | lu `/ly/`, tu `/ty/` | fermée, antérieure, ARRONDIE ; phonème absent de l'anglais, fréquent en français. En syllabe fermée, laxé en `[ʏ]` en français québécois (« lutte » `[lʏt]`). |
| ə | schwa / e caduc (phonème `/ə/` ; réalisation arrondie antérieure proche de `[œ]`/`[ø]` en français standard) | le `/lə/`, petit `/pəti/` | e muet/caduc, symbole phonémique `/ə/` ; souvent supprimé à l'oral (« petit » `[pti]`). En français standard métropolitain, la réalisation phonétique n'est pas une vraie voyelle centrale mais une voyelle arrondie plutôt antérieure, proche de `[œ]` (parfois `[ø]` en syllabe ouverte). |

### CV Matrix

Chaque cellule donne la séquence phonémique consonne + voyelle. Les colonnes sont les huit voyelles de référence ; la colonne **Base IPA** donne le phonème consonantique isolé.

| Consonant | Name | Example | Base IPA | i | e | ɛ | a | ɔ | u | y | ə |
|---|---|---|---|---|---|---|---|---|---|---|---|
| p | occlusive bilabiale sourde | pas `/pa/`, pis `/pi/` | p | pi | pe | pɛ | pa | pɔ | pu | py | pə |
| b | occlusive bilabiale sonore | bas `/ba/`, bu `/by/` | b | bi | be | bɛ | ba | bɔ | bu | by | bə |
| t | occlusive alvéolaire sourde | tas `/ta/`, tu `/ty/` | t | ti | te | tɛ | ta | tɔ | tu | ty | tə |
| d | occlusive alvéolaire sonore | dos `/do/`, du `/dy/` | d | di | de | dɛ | da | dɔ | du | dy | də |
| k | occlusive vélaire sourde | cas `/ka/`, qui `/ki/` | k | ki | ke | kɛ | ka | kɔ | ku | ky | kə |
| ɡ | occlusive vélaire sonore | gars `/ɡa/`, gui `/ɡi/` | ɡ | ɡi | ɡe | ɡɛ | ɡa | ɡɔ | ɡu | ɡy | ɡə |
| f | fricative labiodentale sourde | fa `/fa/`, fil `/fil/` | f | fi | fe | fɛ | fa | fɔ | fu | fy | fə |
| v | fricative labiodentale sonore | va `/va/`, vu `/vy/` | v | vi | ve | vɛ | va | vɔ | vu | vy | və |
| s | fricative alvéolaire sourde | sa `/sa/`, si `/si/` | s | si | se | sɛ | sa | sɔ | su | sy | sə |
| z | fricative alvéolaire sonore | zut `/zyt/`, zéro `/zeʁo/` | z | zi | ze | zɛ | za | zɔ | zu | zy | zə |
| ʃ | fricative post-alvéolaire sourde | chat `/ʃa/`, chic `/ʃik/` | ʃ | ʃi | ʃe | ʃɛ | ʃa | ʃɔ | ʃu | ʃy | ʃə |
| ʒ | fricative post-alvéolaire sonore | joue `/ʒu/`, gîte `/ʒit/` | ʒ | ʒi | ʒe | ʒɛ | ʒa | ʒɔ | ʒu | ʒy | ʒə |
| m | nasale bilabiale | ma `/ma/`, mou `/mu/` | m | mi | me | mɛ | ma | mɔ | mu | my | mə |
| n | nasale alvéolaire | na `/na/`, nu `/ny/` | n | ni | ne | nɛ | na | nɔ | nu | ny | nə |
| ɲ | nasale palatale | gnon `/ɲɔ̃/`, agneau `/aɲo/` | ɲ | ɲi | ɲe | ɲɛ | ɲa | ɲɔ | ɲu | ɲy | ɲə |
| ʁ | fricative/approximante uvulaire voisée (R français) | ras `/ʁa/`, rue `/ʁy/` | ʁ | ʁi | ʁe | ʁɛ | ʁa | ʁɔ | ʁu | ʁy | ʁə |
| l | latérale alvéolaire | la `/la/`, lit `/li/` | l | li | le | lɛ | la | lɔ | lu | ly | lə |
| j | semi-voyelle (approximante) palatale | hier `/jɛʁ/`, yeux `/jø/` | j | ji | je | jɛ | ja | jɔ | ju | jy | jə |
| ɥ | semi-voyelle (approximante) labio-palatale | huit `/ɥit/`, lui `/lɥi/` | ɥ | ɥi | ɥe | ɥɛ | ɥa | ɥɔ | ɥu | ɥy | ɥə |
| w | semi-voyelle (approximante) labio-vélaire | oui `/wi/`, oua `/wa/` | w | wi | we | wɛ | wa | wɔ | wu | wy | wə |

### Quebec Combinations (Affrication)

En français québécois, `/t/` et `/d/` s'affriquent en `[t͡s]` et `[d͡z]` devant les voyelles antérieures hautes `/i y/` (et les glides `/j ɥ/`). Cette affrication est absente du français standard métropolitain. Pour ces deux consonnes uniquement, les combinaisons québécoises diffèrent de la matrice standard ci-dessus aux colonnes `i` et `y` ; toutes les autres consonnes ont des combinaisons identiques dans les deux accents.

| Consonant | i | e | ɛ | a | ɔ | u | y | ə |
|---|---|---|---|---|---|---|---|---|
| t | t͡si | te | tɛ | ta | tɔ | tu | t͡sy | tə |
| d | d͡zi | de | dɛ | da | dɔ | du | d͡zy | də |

### Phonetic Notes

Réalisations allophoniques principales de chaque attaque consonantique. Ces notes décrivent comment les cellules CV phonémiques ci-dessus se réalisent dans la parole.

| Consonant | Phonetic Note |
|---|---|
| p | Non aspirée en français, contrairement à l'anglais : `[p]` pur sans bouffée d'air, même à l'initiale d'une syllabe accentuée (français standard et québécois). |
| b | Pleinement voisée à l'initiale et en intervocalique ; voisement maintenu plus complètement qu'en anglais. Peut s'assourdir en finale devant pause (`[b̥]`). |
| t | Non aspirée et plus dentale `[t̪]` qu'en anglais. En français québécois, `/t/` s'affrique en `[t͡s]` devant les voyelles antérieures hautes `/i y/` et les glides `/j ɥ/` (ex. « tu » `[t͡sy]`, « petit » `[pət͡si]`) ; cette affrication est absente du français standard métropolitain. |
| d | Pleinement voisée et dentale `[d̪]`. En français québécois, `/d/` s'affrique en `[d͡z]` devant `/i y j ɥ/` (ex. « dur » `[d͡zyʁ]`, « dire » `[d͡ziʁ]`) ; absent du français standard métropolitain. |
| k | Non aspirée. Lieu d'articulation avancé (palatalisé) devant les voyelles antérieures `/i e ɛ y/` (`[k̟]`), reculé devant les voyelles postérieures `/a ɔ u/`. |
| ɡ | Pleinement voisée. Lieu d'articulation avancé devant les voyelles antérieures, reculé devant les postérieures. |
| f | Stable dans tous les contextes vocaliques (français standard et québécois). |
| v | Pleinement voisée. Peut s'assourdir partiellement en finale absolue (`[v̥]`). |
| s | Sourde et nette. Reste `[s]` devant `/i y/` en français standard (pas d'affrication) ; à distinguer du comportement de `/t d/` en québécois. |
| z | Pleinement voisée en intervocalique (souvent issue de la liaison ou d'un -s- intervocalique). Peut s'assourdir partiellement en finale (`[z̥]`). |
| ʃ | Lèvres légèrement arrondies/protruses. Stable dans tous les contextes vocaliques. |
| ʒ | Pleinement voisée ; lèvres légèrement arrondies. Peut s'assourdir partiellement en finale (`[ʒ̥]`). |
| m | Sonante nasale stable. Ne nasalise pas systématiquement la voyelle suivante (la nasalité vocalique est phonémique et distincte en français). |
| n | Sonante nasale dentale/alvéolaire stable dans tous les contextes. |
| ɲ | Nasale palatale. En français contemporain, souvent réalisée comme une séquence `[nj]` par certains locuteurs, mais reste phonémique ; rare à l'initiale absolue de mot mais possible (« gnangnan »). Donnée pour la complétude systématique. |
| ʁ | Le « R » français standard : fricative uvulaire voisée `[ʁ]`, souvent réalisée comme approximante uvulaire `[ʁ̞]` ou assourdie `[χ]` au contact d'une consonne sourde. En français québécois traditionnel, un R apical/alvéolaire roulé `[r]` ou battu `[ɾ]` coexistait, mais le `[ʁ]` uvulaire est aujourd'hui majoritaire à Montréal. |
| l | Latérale « claire » `[l]` dans tous les contextes en français, sans vélarisation (pas de « dark l » comme en anglais), aussi bien à l'attaque qu'en coda. |
| j | Glide palatal, contrepartie consonantique de `/i/`. Donné ici en attaque devant les voyelles. La séquence `/ji/` est rare/redondante mais listée pour la complétude. |
| ɥ | Glide labio-palatal, contrepartie de `/y/` ; phonème typologiquement rare propre au français. Apparaît surtout devant les voyelles, fréquemment devant `/i/` (« huit » `[ɥit]`). Certaines combinaisons (ex. `/ɥy/`) sont marginales et listées pour la complétude. |
| w | Glide labio-vélaire, contrepartie de `/u/`. Apparaît en attaque devant les voyelles (« oui » `[wi]`, « moi » `/mwa/`). La séquence `/wu/` est marginale et listée pour la complétude. |

### Accent Notes

**Français standard métropolitain vs. français québécois.** Les qualités vocaliques de cette matrice suivent les valeurs du français standard métropolitain (base parisienne). Différences systématiques principales avec le français québécois : (1) AFFRICATION — en québécois, `/t d/` se réalisent `[t͡s d͡z]` devant les voyelles antérieures hautes `/i y/` et les glides `/j ɥ/` (« tu » `[t͡sy]`, « dire » `[d͡ziʁ]`), réalisation absente du standard métropolitain ; ces cas sont donnés dans le tableau « Quebec Combinations » ci-dessus. (2) VOYELLES RELÂCHÉES — en québécois, `/i y u/` se laxent en `[ɪ ʏ ʊ]` en syllabe fermée. (3) DIPHTONGAISON — les voyelles longues se diphtonguent en québécois (« père » `[paɛ̯ʁ]`, « pâte » `[pɑʊ̯t]`). (4) Les oppositions `/a/`~`/ɑ/` et nasales `/ɛ̃/`~`/œ̃/`, largement neutralisées en français standard métropolitain, sont maintenues en français québécois. L'inventaire consonantique est par ailleurs identique dans les deux variétés.

**Pas d'aspiration.** Aucune occlusive sourde française (`/p t k/`) n'est aspirée, contrairement à l'anglais : les attaques CV se réalisent avec `[p t k]` non aspirés dans les deux accents. C'est une différence majeure pour les apprenants anglophones.

**Accent (stress).** L'accent n'est PAS lexical en français : il ne porte pas sur une syllabe particulière du mot mais se fixe sur la dernière syllabe pleine du groupe rythmique. Aucune marque d'accent n'est donc portée sur les combinaisons CV isolées de cette matrice.

## Suprasegmentals

Prosodic and suprasegmental features of Modern French pronunciation, documented in parallel for two reference accents: Standard Metropolitan French (français standard, European/Parisian-based) and Quebec French (français québécois, Canadian). French is fundamentally different from English at the suprasegmental level: it has NO lexical/contrastive stress, it is SYLLABLE-TIMED rather than stress-timed, and it does NOT reduce unstressed vowels to schwa. Prominence is a property of the rhythmic GROUP, not of the individual word: a fixed, predictable group accent falls on the final full syllable of each prosodic phrase ('accent tonique de groupe'), supplemented by an optional initial emphatic accent ('accent d'insistance'). These properties give French its characteristic even, machine-gun rhythm and its melodic, group-final prominence — the 'mélodie de la phrase'.

### Stress (fixed phrase-final, NOT lexical)

CRUCIAL CONTRAST WITH ENGLISH: French has no lexical (word) stress. Stress is NOT phonemic and is NEVER used to distinguish otherwise identical words; there are no French analogues of English noun/verb pairs like 'récord'/'recórd'. Instead, prominence is fixed and rhythmic: the last full syllable (any syllable not containing a final schwa `/ə/`) of a RHYTHMIC/PROSODIC GROUP ('groupe rythmique', 'groupe de souffle') receives the regular group accent ('accent tonique de groupe', also 'accent final'). Because the accent attaches to the group rather than the word, an isolated word is stressed on its last full syllable, but the same word loses that prominence when it sits non-finally inside a longer group. A separate, optional emphatic accent ('accent d'insistance') may additionally fall on the FIRST consonant-initial syllable of a word for emphasis or contrast.

#### Key Difference From English

| Language | Stress System |
|---|---|
| English | Lexical stress is phonemic and lexically stored: its position is unpredictable, can distinguish minimal pairs (PREsent vs preSENT), and is cued by duration, pitch, full vowel quality, and loudness on a designated syllable of each content word. |
| French | There is no word-level stress to learn or store. The regular accent is automatic and group-final; it shifts as the boundaries of the rhythmic group shift. Pitch and (residual) length, not loudness or vowel-quality change, are its main correlates. Learners must avoid importing English-style word stress (e.g., do not say 'TÉlephone' with a strong first-syllable beat; the regular prominence is on the final syllable of the group: 'téléphone' → `[te.le.ˈfɔn]` when phrase-final). |

#### Regular Group Accent (accent tonique de groupe / accent final)

The default, obligatory prominence of every rhythmic group. It falls on the LAST FULL SYLLABLE of the group — i.e., the final syllable, skipping a final 'e caduc' `/ə/` if one is pronounced. It is realized mainly by a small lengthening of the accented vowel and by pitch movement at the group boundary, not by extra loudness.

**IPA notation:** `ˈ` placed immediately before the final full syllable of the GROUP (not of the word). A lengthened accented vowel may additionally carry the half-long or long mark (`ˑ` / `ː`). Group boundaries may be shown with `|` (minor) and `‖` (major).

**Phonetic correlates:** Final-syllable lengthening of the vowel and a pitch event (rise in non-final groups, fall in the final group); little or no loudness increase and NO change in vowel quality.

| Isolated word | IPA (isolated) | In group | IPA (in group) | Note |
|---|---|---|---|---|
| Paris | `[pa.ˈʁi]` | Paris est loin | `[pa.ʁi.ɛ.ˈlwɛ̃]` | Isolated, the accent is on '-ris'; inside the longer group the regular accent moves to the group-final syllable '-loin', and 'Paris' loses its prominence. |
| université | `[y.ni.vɛʁ.si.ˈte]` | l'université de Montréal | `[ly.ni.vɛʁ.si.te.də.mɔ̃.ʁe.ˈal]` | The single group accent is always group-final; the long word 'université' is fully unstressed within the larger group. |
| petite | `[pə.ˈtit]` | une petite maison | `[yn.pə.tit.mɛ.ˈzɔ̃]` | Final full syllable carries the accent; the regular accent is rhythmic and group-final, never lexically fixed on 'pe-'. |

#### Emphatic / Insistence Accent (accent d'insistance)

An OPTIONAL, expressive prominence used for emphasis, contrast, insistence, or emotion. Unlike the regular accent, it typically falls on the FIRST syllable of the word that begins with a consonant (or the first syllable generally), is realized by extra intensity and often a sharp pitch rise plus consonant lengthening (gemination of the onset consonant), and co-exists with — does not replace — the group-final regular accent.

**IPA notation:** `ˈ` (or an upstep `↑`) before the emphasized syllable; the onset consonant is often geminated/lengthened, shown by doubling or the long mark (e.g., `[fːɔʁ.mi.ˈdabl]`).

**Phonetic correlates:** Increased intensity, a pitch peak, and lengthening of the initial consonant of the emphasized word; the regular group accent still applies group-finally.

| Word | Neutral | Emphatic | Note |
|---|---|---|---|
| formidable | `[fɔʁ.mi.ˈdabl]` | `[ˈfːɔʁ.mi.ˈdabl]` | Emphatic accent on the initial syllable with consonant lengthening: 'C'est FORmidable!' |
| épouvantable | `[e.pu.vɑ̃.ˈtabl]` | `[ˈe.pu.vɑ̃.ˈtabl]` | Initial-syllable emphasis for an expressive, intensified reading. |
| impossible | `[ɛ̃.pɔ.ˈsibl]` | `[ɛ̃.ˈpːɔ.ˈsibl]` | Insistence often targets the first consonant-initial syllable (here 'po-'), geminating the onset; 'C'est imPOSSible!' |

#### No Phonemic Contrast

Because stress is never lexical in French, there are NO minimal pairs distinguished by stress alone, and there is NO French analogue of the English compound-vs-phrase or noun-vs-verb stress alternations. Differences such as 'un grand homme' (a great man) vs 'un homme grand' (a tall man) are conveyed by word order and meaning, not by a stress shift; both phrases simply take the regular accent on their group-final syllable.

**Note:** Mastering French prosody is largely a matter of UNLEARNING the English habit of placing a strong, variable beat on a designated syllable of each content word. In French the only obligatory beat is the group-final one.

#### Accent Difference

| Accent | Stress Behavior |
|---|---|
| Metropolitan | Group-final regular accent realized mainly by vowel lengthening and pitch; 'accent d'insistance' common in formal, media, and emphatic speech. No length-based vowel contrasts to interact with the accent. |
| Quebec | The same group-final accent system. Quebec additionally retains genuine long vowels and diphthongization (see Vowel Length), so the lengthening on an accented final syllable can be more salient and may surface as a diphthong (e.g., 'tard' `[taːʁ]` → `[taɔ̯ʁ]`); the location of the regular accent, however, is identical to Metropolitan French. |

### Rhythm (syllable-timed)

French is the textbook example of a SYLLABLE-TIMED language: every syllable tends to occupy roughly the same span of time, giving an even, regular, 'staccato' or 'machine-gun' rhythm. This contrasts directly with STRESS-TIMED English, where stressed syllables recur at roughly regular intervals and intervening unstressed syllables are compressed and reduced. In French there is no such compression: unstressed syllables keep nearly the same duration and full vowel quality as the accented one, so the number of syllables, not the number of stresses, sets the pace.

#### Syllable Timing

The rhythmic unit of French is the SYLLABLE, not the stress foot. Because syllables are near-isochronous, the time taken to say a phrase scales with its syllable count, and there is little durational difference between the accented final syllable and the preceding ones (apart from modest final lengthening).

**Example:** 'Le petit chat est noir' `[lə.pə.ti.ʃa.ɛ.ˈnwaʁ]` is delivered as a sequence of roughly equal syllables, with the only durational/pitch prominence on the group-final '-noir'. Compare the English 'The little cat is black', where 'lit-', 'cat', 'black' form stress beats and 'the', '-tle', 'is' are compressed.

**IPA notation:** Syllable boundaries shown with the period (`.`); the single group accent shown with `ˈ` before the final full syllable. There is no foot-internal compression to mark.

#### Groupe Rythmique (rhythmic group)

The relevant prosodic domain is the GROUPE RYTHMIQUE (rhythmic group), also called the 'groupe de souffle' (breath group) or 'mot phonétique'. It is a sense unit (e.g., a noun and its determiners/adjectives, a verb and its clitics) pronounced as one uninterrupted run of even syllables with a single regular accent on its last full syllable. Liaison and enchaînement operate within the group, reinforcing its cohesion and blurring word boundaries.

**Example:** 'Les enfants | jouent dans le jardin' parses into two rhythmic groups, each a smooth string of equal syllables ending in a group accent: `[le.zɑ̃.ˈfɑ̃ | ʒu.dɑ̃.lə.ʒaʁ.ˈdɛ̃]`.

**IPA notation:** Group boundaries marked with `|` (minor) / `‖` (major); enchaînement and liaison consonants are resyllabified onto a following vowel within the group.

#### Isochrony

French approximates SYLLABLE ISOCHRONY: inter-syllable intervals are perceived as roughly equal. As with stress-timing in English, strict acoustic equality is an idealization — final lengthening and intrinsic vowel durations create variation — but French sits clearly at the syllable-timed end of the rhythmic continuum, with a low normalized variability of vocalic intervals compared with English.

**Consequence:** Adding syllables to a French phrase lengthens it roughly in proportion (no English-style squeezing of weak syllables). This is why French sounds 'even' and why a heavy English-style reduction of medial syllables is one of the most noticeable foreign-accent errors.

#### Accent Difference

| Accent | Rhythmic Behavior |
|---|---|
| Metropolitan | Strongly syllable-timed; near-equal syllable durations with group-final lengthening. |
| Quebec | Also syllable-timed, but the retention of phonemic/positional long vowels and of diphthongization (see Vowel Length) introduces somewhat greater durational contrast between long and short vowels than in Metropolitan French, slightly loosening the strict equal-timing impression while remaining clearly syllable-timed and non-reducing. |

### Vowel Length

Vowel length is largely NON-CONTRASTIVE and reduced in Standard Metropolitan French, but is much better preserved — and in part phonemic — in Quebec French. In older and conservative Metropolitan French a length contrast existed (e.g., 'maître' `[mɛːtʁ]` vs 'mettre' `[mɛtʁ]`; 'pâte' `[pɑːt]` vs 'patte' `[pat]`), but in present-day Parisian French these distinctions are mostly lost or reduced to a quality difference, and most length is now merely positional (an automatic lengthening of the accented final vowel).

**IPA notation:** `ː` marks a long vowel, `ˑ` a half-long vowel; absence of either marks a short vowel. Quebec diphthongized long vowels may be shown with an offglide (e.g., `[ɛɪ̯]`, `[aʊ̯]`, `[oʊ̯]`).

#### Standard Metropolitan French

Length is essentially positional/allophonic. The accented final vowel of a rhythmic group is somewhat lengthened; otherwise vowels are short. The historic phonemic long vowels have largely merged: 'maître'/'mettre', 'pâte'/'patte', 'jeûne'/'jeune' are increasingly homophonous or distinguished only by vowel quality, not length.

**Lengthening rule:** An accented (group-final) vowel is lengthened before a final voiced continuant — the so-called LENGTHENING CONSONANTS `/ʁ z v ʒ vʁ/` — and before any consonant for the inherently long vowels in conservative usage.

| Word | IPA | Note |
|---|---|---|
| rose | `[ˈʁoːz]` | Vowel lengthened before final `/z/` (a lengthening consonant) when group-final. |
| rêve | `[ˈʁɛːv]` | Lengthening before final `/v/`. |
| neige | `[ˈnɛːʒ]` | Lengthening before final `/ʒ/`. |
| tard | `[ˈtaːʁ]` | Lengthening before final `/ʁ/`. |

**Residual phonemic length:** A few speakers and registers keep a residual long `/ɛː/` contrast (the historic 'ê'/'ai' vowel), e.g., 'mettre' `[mɛtʁ]` vs 'maître' `[mɛːtʁ]`, but for most Metropolitan speakers this is merged.

| Pair | Short | Long | Status |
|---|---|---|---|
| patte vs pâte | patte `/pat/` `[pat]` | pâte (historically `/pɑːt/`) `[pɑt]` or `[pat]` | The `/a/`–`/ɑ/` length-and-quality contrast is largely lost in Metropolitan French; most speakers merge to a single `[a]`. |
| mettre vs maître | mettre `/mɛtʁ/` `[mɛtʁ]` | maître (historically `/mɛːtʁ/`) `[mɛtʁ]` | Length contrast lost for most Metropolitan speakers. |

#### Quebec French

Quebec French RETAINS distinctive long vowels and is much more conservative about length. It preserves long `/ɛː/`, `/œː/`, `/ɑː/`, `/oː/` (and others) as genuinely long, keeps the `/a/`–`/ɑ/` and length distinctions that Metropolitan French has merged, and additionally LENGTHENS vowels before final voiced fricatives. Crucially, long vowels in stressed/closed syllables are typically DIPHTHONGIZED, a hallmark of the accent.

**Long vowels** — phonemic or strongly positional long vowels kept distinct in Quebec French.

| Vowel | Word | IPA | Note |
|---|---|---|---|
| `/ɛː/` | fête | `[faɛ̯t]` | Long `/ɛː/` (vs short `/ɛ/` in 'faite' `[fɛt]`); diphthongized to `[aɛ̯]` in a stressed closed syllable. |
| `/œː/` | heure | `[œœ̯ʁ]` ~ `[aœ̯ʁ]` | Long `/œː/`, diphthongized; contrasts with short `/œ/`. |
| `/ɑː/` | pâte | `[pɑːt]` ~ `[pɑʊ̯t]` | Long back `/ɑː/` kept clearly distinct from short front `/a/` in 'patte' `[pat]`; the `/a/`–`/ɑ/` contrast is alive in Quebec, merged in Metropolitan. |
| `/oː/` | tôt / saute | `[toː]` ~ `[toʊ̯]` | Long `/oː/` diphthongizes to `[oʊ̯]` in stressed closed syllables ('saute' `[soʊ̯t]`). |

**Lengthening before voiced fricatives:** A vowel is lengthened (and typically diphthongized) before a word-final VOICED FRICATIVE `/v z ʒ ʁ/`.

| Word | IPA | Note |
|---|---|---|
| neige | `[nɛɪ̯ʒ]` | Lengthening + diphthongization before final `/ʒ/`. |
| vive | `[vɪv]` → stressed `[vaɪ̯v]` | Lengthening before final `/v/` with diphthongization in the long realization. |
| douze | `[duːz]` ~ `[duʊ̯z]` | Lengthening before final `/z/`. |

**Diphthongization:** Long vowels in stressed CLOSED syllables are characteristically diphthongized in Quebec French, a key audible difference from Metropolitan French.

| Word | IPA | Note |
|---|---|---|
| père | `[paɛ̯ʁ]` | `/ɛː/` → `[aɛ̯]`. |
| fort | `[fɔɔ̯ʁ]` ~ `[faɔ̯ʁ]` | Lengthened `/ɔ/` before `/ʁ/` diphthongizes. |
| tard | `[taɔ̯ʁ]` | Long `/ɑː/`-type vowel diphthongizes before `/ʁ/`; cf. Metropolitan `[taːʁ]` without diphthong. |

#### Accent Difference

| Accent | Length Behavior |
|---|---|
| Metropolitan | Length mostly positional and non-contrastive; historic long vowels and the `/a/`–`/ɑ/` contrast largely merged; accented final vowels lengthened before `/ʁ z v ʒ/`. |
| Quebec | Retains phonemic/strongly positional long vowels (`/ɛː œː ɑː oː/`), keeps `/a/`–`/ɑ/` distinct, lengthens before final voiced fricatives, and diphthongizes long vowels in stressed closed syllables. |

### No Vowel Reduction

ESSENTIAL CONTRAST WITH ENGLISH: French does NOT reduce unstressed vowels. Every vowel — accented or not — keeps its FULL, distinct quality. There is no French equivalent of the pervasive English reduction of unstressed vowels to schwa `/ə/` or lax `/ɪ/`. The vowel of an unaccented syllable is pronounced as clearly as that of the accented one: in 'téléphone' `[te.le.ˈfɔn]` all three vowels keep their full `[e]`/`[e]`/`[ɔ]` qualities, whereas an English-style reduction would wrongly give something like `[tʰə.lə.ˈfoʊn]`. This full-vowel maintenance, together with syllable timing, is what makes French sound even and 'clear-voweled'.

#### Contrast With English

| Language | Reduction Behavior |
|---|---|
| English | Unstressed vowels collapse toward `/ə/`, `/ɪ/`, or a syllabic consonant; weak forms of function words (e.g., 'to' `/tə/`, 'of' `/əv/`) are the norm. Reduction is obligatory for natural rhythm. |
| French | Unstressed vowels are NOT centralized or weakened; they retain their full place and rounding. French has no system of strong/weak forms for function words analogous to English. The only vowel that can disappear is the 'e caduc' `/ə/`, and that is DELETION (the whole vowel drops), never gradient reduction to a centralized quality. |

**Example:** English 'photography' `/fəˈtɑɡrəfi/` reduces three of its vowels to `/ə/`; the French cognate 'photographie' `[fɔ.tɔ.ɡʁa.ˈfi]` keeps every vowel full: `[ɔ]`, `[ɔ]`, `[a]`, `[i]`.

#### The 'e caduc' (e muet / e instable)

The 'e caduc' (also 'e muet', 'e instable', 'schwa français'), phonemically `/ə/`, is the ONLY French vowel that behaves like a 'weak' vowel — but its behaviour is categorical DELETION, not reduction. In a given context it is either fully pronounced as a rounded mid-central/front-rounded `[ə]`~`[œ]` or dropped entirely; it never blurs into a reduced, centralized version of another vowel the way English unstressed vowels do.

**Quality note:** Phonetically French `/ə/` is rounded and front-of-central, close to `[œ]`/`[ø]`; it is NOT the unrounded mid-central `[ə]` of English 'about'. Thus even when pronounced, it has a full, definite quality.

| Word | Full | Dropped | Note |
|---|---|---|---|
| petit | `[pə.ti]` | `[pti]` | The `/ə/` is fully pronounced or fully deleted depending on rhythm and surrounding consonants (loi des trois consonnes); there is no in-between reduced quality. |
| samedi | `[sam.də.di]` | `[sam.di]` | Medial `/ə/` commonly deleted in casual speech. |
| je ne sais pas | `[ʒə.nə.sɛ.ˈpa]` | `[ʒ(ə).n.sɛ.ˈpa]` ~ `[ʃsɛ.ˈpa]` | Multiple `/ə/` deletions in connected speech; remaining vowels keep full quality. |

**Retention rule:** Whether `/ə/` is kept is governed largely by the 'loi des trois consonnes' (it is retained to avoid a sequence of three consonants) and by rhythm/register, NOT by stress-driven reduction.

| Accent | 'e caduc' Behavior |
|---|---|
| Metropolitan | Word-final `/ə/` is almost always silent ('table' `[tabl]`, not `[tablə]`); internal `/ə/` is variably deleted; in southern Metropolitan ('accent du Midi') `/ə/` is retained far more often, including word-finally (`[ta.blə]`). |
| Quebec | Patterns of `/ə/` deletion are broadly similar to standard Metropolitan; the realized vowel may be more clearly rounded `[œ]`. In all varieties the key point holds: `/ə/` is deleted, not reduced, and all OTHER vowels keep full quality. |

**Implication for learners:** Anglophone learners must resist centralizing French unstressed vowels. Each written vowel letter generally corresponds to a clearly articulated full vowel; pronouncing 'animal' as `[a.ni.ˈmal]` (full vowels) rather than the English-style `[ˈæ.nə.məl]` is essential to a native-like rhythm.

### Intonation

French intonation — the 'mélodie de la phrase' — is the structured use of pitch over the rhythmic group and the larger intonation phrase. Its building block is the rhythmic group, each of which ends with a pitch movement on its group-final accented syllable. The basic system pits CONTINUATION RISES (signalling 'more to come') against a TERMINAL FALL (signalling completion), with a distinctive overall RISE marking yes/no questions. Because prominence is group-final and fixed, French intonation does much of the grammatical and pragmatic work that stress placement does in English.

#### Structure of the Intonation Phrase

The **intonation phrase** is the domain of one complete melodic contour, composed of one or more rhythmic groups and bounded by perceptible breaks; the final rhythmic group of the phrase carries the terminal contour.

**Components:**

- **Rhythmic groups (groupes rythmiques)** — each a string of near-equal syllables ending in a group-final accented syllable that carries a local pitch movement.
- **Non-final group-final syllables** — typically carry a CONTINUATION RISE (montée / continuation majeure or mineure).
- **Phrase-final group-final syllable** — carries the terminal contour: a FALL for statements/commands/wh-questions, a RISE for yes/no questions.

**IPA notation:** Group boundaries: `|` (minor) and `‖` (major). Global pitch movements: `↗` rise (continuation, question), `↘` fall (terminal). The accented syllable bearing the movement is the group-final full syllable (marked `ˈ`).

#### Contours

| Contour | Symbol | Description | Typical Functions | Example |
|---|---|---|---|---|
| Continuation rise (continuation majeure) | `↗` | A pitch RISE on the group-final accented syllable of a NON-FINAL rhythmic group, signalling that the utterance is incomplete and more is to follow. The major continuation (higher rise) marks the boundary of a major syntactic constituent; a minor continuation (smaller rise) marks an internal group boundary. | Non-finality, linking of successive groups, listing non-final items, marking the subject group before the predicate. | Les enfants ↗ \| jouent dans le jardin ↘ — rise on '-fants' (continuation), fall on '-din' (terminal). `[le.zɑ̃.ˈfɑ̃↗ \| ʒu.dɑ̃.lə.ʒaʁ.ˈdɛ̃↘]` |
| Terminal fall (chute / intonation conclusive) | `↘` | A pitch FALL on the group-final accented syllable of the LAST rhythmic group, signalling completion and finality. | Declarative statements, commands/imperatives, and wh-questions (questions with an interrogative word). Conveys definiteness and closure. | Il est arrivé ↘. (a complete statement) `[i.lɛ.ta.ʁi.ˈve↘]`; Où vas-tu ↘? (wh-question typically falls) `[u.va.ˈty↘]` |
| Yes/no-question rise (interrogation totale) | `↗` | An overall final RISE, with a marked pitch climb on the phrase-final accented syllable, characteristic of total (yes/no) questions — especially questions formed by intonation alone, without inversion or 'est-ce que'. | Polar (yes/no) questions; the rise alone can turn a declarative into a question ('Tu viens ↘.' statement vs 'Tu viens ↗?' question). | Tu viens ↗? (yes/no question by intonation) `[ty.ˈvjɛ̃↗]`; Vous avez compris ↗? `[vu.za.ve.kɔ̃.ˈpʁi↗]` |
| Implication / suspensive fall-rise | `↘↗` | A fall followed by a rise (or a suspended mid-level), used for reservation, politeness, or an implied unstated continuation ('... mais'). | Reservation, hesitation, polite qualification, leaving something implied. | Oui ↘↗... (yes, but...) — a hedged, non-committal 'oui'. |
| Emphatic / exclamatory contour | `↑↘` | A high onset (often combined with the 'accent d'insistance' on the first syllable of a key word) followed by a fall, used for exclamation and strong emotion. | Exclamations, strong assertion, surprise, indignation. | C'est magnifique ↑↘! (with emphatic high onset on 'ma-') `[sɛ.ma.ɲi.ˈfik]` |

#### Functions Overview

- **Grammatical:** Distinguishes sentence types where syntax does not: a yes/no question identical in word order to a statement is signalled by the final rise ('Tu viens.' vs 'Tu viens?'). Continuation rises and terminal falls mark constituent and clause boundaries.
- **Rhythmic grouping:** Pitch movements delimit the rhythmic groups: a rise at each non-final group boundary, a fall (or rise, for questions) at the phrase end. This grouping carries the information structure that English would partly convey through nucleus placement and reduction.
- **Attitudinal:** Conveys speaker attitude — politeness, doubt, surprise, irritation, enthusiasm — largely through the height and shape of the final movement and through the emphatic accent.
- **Focus:** Because the regular accent is fixed group-finally, French marks contrastive FOCUS chiefly by the optional 'accent d'insistance' (emphatic prominence on the focused word) and by syntactic devices (clefting: 'C'est MOI qui l'ai fait', dislocation: 'Moi, je...'), rather than by freely shifting a nuclear stress as English does.

#### Focus and Emphasis

Whereas English shifts its nuclear stress to mark focus ('I bought a RED car' vs 'I BOUGHT a red car'), French generally keeps the regular accent group-final and instead uses (a) the 'accent d'insistance' for emphatic/contrastive prominence and (b) syntactic restructuring (clefts, dislocations) to foreground the focused element.

| Utterance | Device |
|---|---|
| C'est une voiture ROUGE. | Emphatic accent (accent d'insistance) on 'rouge' for contrastive focus on the colour. |
| C'est MOI qui l'ai acheté. | Cleft construction ('c'est ... qui') foregrounding the subject — the French strategy where English would simply stress 'I'. |
| Moi, je préfère le thé. | Left dislocation foregrounding the topic, with the pronoun resumed — common in spoken French to manage focus/topic without moving the regular accent. |

#### Accent Difference

| Accent | Intonation Behavior |
|---|---|
| Metropolitan | Standard descriptions of the continuation-rise / terminal-fall / question-rise system are based on Parisian Metropolitan French; pitch range is moderate and the final-syllable movement is the principal cue. |
| Quebec | The same inventory of continuation rises, terminal falls, and question rises applies. Quebec French is often described as having a somewhat wider pitch range and more salient melodic movement, and yes/no questions are frequently marked with the interrogative particle '-tu' ('Tu viens-tu?') in addition to, or instead of, a pure intonational rise; the core fall-vs-rise melodic functions are shared with Metropolitan French. |

**Note:** The fundamental opposition — continuation rise for non-finality, terminal fall for statements/wh-questions, overall rise for yes/no questions — is shared by both reference accents; differences lie mainly in pitch range, the prevalence of certain question strategies, and the greater melodic amplitude often attributed to Quebec French.

## Syllable Structure

Syllable structure patterns in Modern French, documented for two reference accents: Standard Metropolitan French (français standard, Parisian-based) and Quebec French (français québécois). French strongly prefers OPEN syllables of the shape `/CV/`: the open syllable is the unmarked, statistically dominant type, and connected speech actively reshapes word boundaries to maximize open syllables (see resyllabification). Onset and coda clusters exist but are far simpler and less frequent than in English; codas in particular are light, and a great many word-final written consonants are silent, leaving a vowel-final (open) syllable. French syllabification is governed by the Maximal Onset Principle and, crucially, applies ACROSS word boundaries through enchaînement and liaison. This section is the French equivalent of the Peshitta guide's syllable_structure section.

**IPA template:** `(C)(C)(C)V(C)(C)`

**Maximal syllable:** `CCCV(C)(C)`

**Preferred syllable:** `CV`

### Open-Syllable Preference

French is typologically a language with a strong open-syllable (`/CV/`) bias. The majority of syllables in running speech end in a vowel. Two forces reinforce this:

1. Most etymological word-final consonants have become silent in the standard language, so words like 'chat' `/ʃa/`, 'trop' `/tʁo/`, 'les' `/le/`, 'beaucoup' `/bo.ku/` end in a vowel.
2. At word boundaries, enchaînement and liaison move a pronounced final consonant onto a following vowel-initial syllable, keeping the original syllable open.

The result is that a phrase such as 'il a une amie' is syllabified `[i.la.y.na.mi]` — five consecutive open syllables.

| Word | IPA | Note |
|---|---|---|
| chat | `/ʃa/` | final written 't' silent; open syllable |
| beaucoup | `/bo.ku/` | two open syllables CV.CV |
| papa | `/pa.pa/` | canonical CV.CV |

### Components

- **Onset:** 0 to 3 consonants preceding the nucleus *(optional)*
- **Nucleus:** a single vowel (oral or nasal) — French has NO syllabic consonants *(required)*
- **Coda:** 0 to 2 consonants following the nucleus *(optional)*

#### Onset

0 to 3 consonants preceding the nucleus. A single onset consonant may be any of the French consonants `/p b t d k ɡ f v s z ʃ ʒ m n ɲ l ʁ/` (`/ŋ/` does not begin native syllables). Two-consonant onsets are dominated by the 'obstruent + liquid' type — a stop or fricative followed by `/l/` or `/ʁ/` — which obeys rising sonority, e.g. `/pl/`, `/bl/`, `/kl/`, `/ɡl/`, `/fl/`, `/pʁ/`, `/bʁ/`, `/tʁ/`, `/dʁ/`, `/kʁ/`, `/ɡʁ/`, `/fʁ/`, `/vʁ/`. A semivowel `/j ɥ w/` may also follow a consonant, e.g. `/pj/`, `/tw/`, `/lɥ/`. `/s/` + stop clusters (`/sp st sk/`) occur word-medially and in loans but, unlike English, are NOT freely word-initial in inherited vocabulary. Three-consonant onsets are restricted to 'obstruent + liquid + glide' or 's + stop + liquid', e.g. `/stʁ/`, `/skl/`.

- **Minimum consonants:** 0
- **Maximum consonants:** 3

**Sonority sequencing:** Within an onset, sonority rises toward the vowel (obstruent < nasal < liquid < glide < vowel). The productive native pattern is obstruent + liquid (`/pl/`, `/tʁ/`, …), optionally followed by a glide. `/s/` + voiceless-stop clusters are the chief sonority-reversal type and appear chiefly word-medially or in learned/borrowed words.

**Two-consonant onsets** — structure: obstruent + `/l/` or `/ʁ/` (most productive); also obstruent/liquid + glide `/j ɥ w/`.

Attested clusters: `pl`, `bl`, `kl`, `ɡl`, `fl`, `pʁ`, `bʁ`, `tʁ`, `dʁ`, `kʁ`, `ɡʁ`, `fʁ`, `vʁ`, `pj`, `tw`, `lɥ`, `mw`.

| Word | IPA | Note |
|---|---|---|
| plus | `/ply/` | |
| trop | `/tʁo/` | |
| frère | `/fʁɛʁ/` | |
| pied | `/pje/` | C + glide `/j/` |
| lui | `/lɥi/` | C + glide `/ɥ/` |
| toi | `/twa/` | C + glide `/w/` |

**Three-consonant onsets** — structure: obstruent + liquid + glide, or `/s/` + voiceless stop + liquid.

Attested clusters: `stʁ`, `skl`, `skʁ`, `spl`, `pʁj`, `kʁɥ`, `tʁw`.

| Word | IPA | Note |
|---|---|---|
| stress | `/stʁɛs/` | loan; `/s/` + stop + liquid `/stʁ/` onset |
| strict | `/stʁikt/` | `/stʁ/` onset; standard Metropolitan French fully pronounces the word-final 'ct' cluster `/kt/` |
| sclérose (first syllable `/skle/`) | `/skle.ʁoz/` | |
| prier | `/pʁje/` | obstruent + liquid + glide `/pʁj/` |
| cruel | `/kʁɥɛl/` | `/kʁɥ/` obstruent + liquid + glide |

#### Nucleus

The obligatory core of the syllable, always a vowel in French (French has NO syllabic consonants — unlike English `/l̩ n̩ m̩ r̩/`, a French sonorant never forms a syllable on its own). The nucleus is a single oral or nasal vowel; French has no phonemic diphthongs in the standard language, though Quebec French diphthongizes long vowels phonetically. Semivowels `/j ɥ w/` are NOT nuclei: they belong to the onset (or coda) and are distinguished from their vowel counterparts `/i y u/`.

**Vowel nucleus:** Filled by one oral vowel `/i e ɛ (ɛː) a (ɑ) ɔ o u y ø œ ə/` or one nasal vowel `/ɛ̃ ɑ̃ ɔ̃ (œ̃)/`. Metropolitan French largely merges `/a/`~`/ɑ/` and `/ɛ̃/`~`/œ̃/`, whereas Quebec French keeps both contrasts. The schwa `/ə/` (e caduc) is a special nucleus that may be deleted, yielding consonant adjacencies and resyllabification.

| IPA | Example | Type |
|---|---|---|
| `/i/` | i (in 'lit' `/li/`) | oral high front |
| `/y/` | u (in 'tu' `/ty/`) | oral front rounded |
| `/ɑ̃/` | an (in 'an' `/ɑ̃/`) | nasal |
| `/ə/` | e (in 'le' `/lə/`) | schwa / e caduc, deletable |

**Quebec nucleus note:** In Quebec French the high vowels `/i y u/` become lax `[ɪ ʏ ʊ]` when in a closed syllable ending in a non-lengthening consonant, and long vowels diphthongize in closed stressed syllables.

| Word | Metropolitan | Quebec | Note |
|---|---|---|---|
| petite | `/pətit/` | `[pt͡sɪt]` | Quebec lax `[ɪ]` in closed syllable + affrication of `/t/` before `/i/` |
| chute | `/ʃyt/` | `[ʃʏt]` | Quebec lax `[ʏ]` |
| père | `/pɛːʁ/` | `[paɛ̯ʁ]` | Quebec diphthongization of long vowel in closed stressed syllable |

**No syllabic consonants:** Unlike English, French has no syllabic consonants. A sequence like 'quatre' is `/katʁ/` with a single nucleus `/a/`; the final `/tʁ/` is a coda cluster, optionally supported by an inserted schwa `[katʁə]` rather than a syllabic `/ʁ̩/`.

#### Coda

0 to 2 consonants following the nucleus in the unmarked case (occasionally more in word-final clusters built from obstruent + liquid + the silent-e support). French codas are LIGHT compared with English: the open syllable is preferred, a large proportion of historical final consonants are silent, and only a small set of consonants is freely word-final. The four consonants `/k r f l/` — captured by the mnemonic 'CaReFuL' — are the ones most reliably pronounced word-finally; many other final letters are mute (e.g. 't' in 'chat', 's' in 'les', 'd' in 'grand'). When a coda cluster is heavy, an optional schwa may surface to open the syllable (e.g. 'quatre' `[katʁ]` ~ `[katʁə]`).

- **Minimum consonants:** 0
- **Maximum consonants:** 2

**Single codas:** The most common coda is a single consonant. The reliably pronounced word-final consonants cluster around `/k ʁ f l/` (CaReFuL), though others occur.

| Word | IPA | Coda |
|---|---|---|
| avec | `/avɛk/` | `k` |
| bourg | `/buʁ/` | `ʁ` |
| neuf | `/nœf/` | `f` |
| seul | `/sœl/` | `l` |

**Two-consonant codas:** Word-final two-consonant codas are typically obstruent + liquid (e.g. `/tʁ/`, `/bl/`) or liquid/nasal + obstruent (e.g. `/ʁk/`, `/ʁs/`). They are often resolved in casual speech by liquid deletion or by epenthetic schwa.

| Word | IPA | Coda | Note |
|---|---|---|---|
| quatre | `/katʁ/` | `tʁ` | casual `[kat]` (liquid drop) or careful `[katʁ(ə)]` |
| table | `/tabl/` | `bl` | |
| forte | `/fɔʁt/` | `ʁt` | |
| arc | `/aʁk/` | `ʁk` | |

**Coda constraints:** `/h/` has no consonantal value in French (no `[h]` is pronounced; 'h aspiré' merely blocks liaison/elision). `/ŋ/` appears only word-finally in loanwords ('parking' `/paʁ.kiŋ/`). The semivowels `/j ɥ w/` may close a syllable after a vowel (e.g. 'travail' `/tʁa.vaj/`, coda `/j/`).

### Resyllabification

**Principle:** Maximal Onset Principle applied ACROSS word boundaries.

A defining trait of French: syllabification is computed over the whole rhythmic group (groupe rythmique), not word by word. A consonant that ends one word is preferentially attached as the ONSET of a following vowel-initial word, so the phrase is reorganized into a clean string of mostly open syllables. Two distinct but related mechanisms drive this: enchaînement (a normally-pronounced final consonant moves onto the next vowel) and liaison (a normally-SILENT final consonant is resurrected and moves onto the next vowel). Both serve the open-syllable preference and erase the original word boundaries phonetically.

#### Enchaînement

Enchaînement: a consonant that is ALWAYS pronounced at the end of a word is resyllabified as the onset of the next word when that word begins with a vowel. No new segment is added; only the syllable boundary shifts.

| Phrase | Naive | Resyllabified | Note |
|---|---|---|---|
| il a | `/il/ /a/` | `[i.la]` | the always-pronounced `/l/` of 'il' becomes the onset of 'a' → open syllables |
| elle est | `/ɛl/ /ɛ/` | `[ɛ.lɛ]` | `/l/` moves onto the next vowel |
| pour elle | `/puʁ/ /ɛl/` | `[pu.ʁɛl]` | final `/ʁ/` becomes onset of 'elle' |
| une autre amie | `/yn/ /otʁ/ /ami/` | `[y.no.tʁa.mi]` | chained enchaînement across three words |

#### Liaison

Liaison: a word-final consonant that is otherwise SILENT (the latent consonant) is pronounced and attached as the onset of a following vowel-initial word within the same phrase. The most frequent liaison consonants are `/z/` (from final 's'/'x'/'z'), `/t/` (from final 't'/'d'), and `/n/` (from a nasal vowel's denasalizing or non-denasalizing 'n'). Liaison is blocked before 'h aspiré' and before certain words; it is obligatory in some contexts (determiner + noun), optional in others, and forbidden in still others.

| Phrase | Isolated | With liaison | Latent consonant | Note |
|---|---|---|---|---|
| les amis | `/le/` + `/ami/` | `[le.za.mi]` | `z` | silent final 's' of 'les' becomes `/z/` and onsets 'amis' → all open syllables; obligatory liaison |
| un ami | `/œ̃/` (Quebec) ~ `/ɛ̃/` (Metro) + `/ami/` | `[œ̃.na.mi]` (Quebec) ~ `[ɛ̃.na.mi]` (Metro) | `n` | latent `/n/` resyllabified as onset |
| un grand homme | `/ɡʁɑ̃/` + `/ɔm/` | `[ɡʁɑ̃.tɔm]` | `t` | final 'd' surfaces as `/t/` in liaison |
| les héros | `/le/` + `/eʁo/` | `[le.eʁo]` (NO liaison) | — | 'héros' has h aspiré, so liaison and enchaînement are BLOCKED; hiatus is tolerated here |

#### Elision

Elision: a related boundary process where a final schwa or vowel (chiefly `/ə/` in 'le, je, ne, de, que', and 'a' in 'la') is DELETED before a vowel-initial word, written with an apostrophe, again avoiding hiatus and preserving open-syllable rhythm.

| Phrase | IPA | Note |
|---|---|---|
| le ami → l'ami | `[la.mi]` | 'le' `/lə/` loses its schwa before the vowel |
| je ai → j'ai | `[ʒe]` | elision of `/ə/` in 'je' |

#### Word-Internal Syllabification

Word-internally the Maximal Onset Principle assigns as many medial consonants to the following onset as form a legal French onset; the rest stay in the preceding coda.

| Word | IPA | Note |
|---|---|---|
| secret | `/sə.kʁɛ/` | `/kʁ/` is a legal onset, so the break falls before it → first syllable open |
| parler | `/paʁ.le/` | `/ʁl/` is not a legal onset; `/ʁ/` stays in the first (closed) syllable |
| actuel | `/ak.tɥɛl/` | `/kt/` is not a legal onset; the break splits the cluster |
| appliquer | `/a.pli.ke/` | `/pl/` is a legal onset; first syllable stays open |

### Syllable Types

| Type | Description | IPA example | Word | Frequency |
|---|---|---|---|---|
| V | Bare vowel; no onset, no coda (open syllable) | `/a/` | a (3sg of 'avoir') | Common (function words, articles, weak syllables) |
| CV | Open syllable (single consonant + vowel) — the canonical, most frequent French syllable | `/lə/` | le | Most common (the preferred French type) |
| CVCV | Sequence of two open syllables — the prototypical French word shape | `/pa.pa/` | papa | Very common |
| VC | Vowel + single coda (no onset) | `/yn/` | une → `/yn/` | Common |
| CVC | Closed syllable (onset + vowel + coda) | `/ʃat/` | chatte | Common |
| CCV | Two-consonant onset (obstruent + liquid) + vowel (open) | `/tʁo/` | trop | Common |
| CGV | Consonant + glide `/j ɥ w/` + vowel (open); the glide is part of the onset, not the nucleus | `/lɥi/` | lui | Common |
| CCVC | Two-consonant onset + vowel + single coda (closed) | `/fʁɛʁ/` | frère | Common |
| CVCC | Single-consonant onset + vowel + two-consonant coda (closed syllable with a two-consonant coda; genuine native two-onset + two-coda CCVCC words are vanishingly rare, so the realistic French closed-cluster case is CVCC) | `/fɔʁt/` | forte | Occasional |
| CCCVCC | Three-consonant onset (`/s/`+stop+liquid) + vowel + two-consonant coda; 'strict' `/stʁikt/` has the `/stʁ/` onset, nucleus `/i/`, and a fully pronounced word-final `/kt/` cluster (standard Metropolitan French pronounces the 'ct') | `/stʁikt/` | strict | Rare (mostly learned/loan vocabulary) |

### Constraints

- French strongly prefers OPEN `/CV/` syllables; both word-internal syllabification (Maximal Onset Principle) and boundary processes (enchaînement, liaison, elision) operate to maximize vowel-final syllables.
- French has NO syllabic consonants: a sonorant `/l n m ʁ/` never forms a syllable nucleus on its own (contrast English `/ˈbɒt.l̩/`). Heavy final clusters are instead resolved by an optional supporting schwa, e.g. 'quatre' `[katʁ]` ~ `[katʁə]`.
- The nucleus is always a single vowel; standard French has no phonemic diphthongs. Glides `/j ɥ w/` are consonantal (onset or coda) and contrast with the vowels `/i y u/`. A clear minimal contrast of glide-coda vs hiatus is 'abeille' `/a.bɛj/` (glide `/j/` closing the syllable) vs 'haïr' `/a.iʁ/` (two vowels in hiatus, `/a/` and `/i/` in separate syllables); compare also 'paye' `/pɛj/` (~ `/pɛ.i/` for some speakers) vs 'pays' `/pe.i/`.
- Most etymological word-final consonants are silent, producing open syllables; the consonants most reliably pronounced word-finally are `/k ʁ f l/` (the 'CaReFuL' set), though exceptions exist in both directions.
- `/h/` has no phonetic value: no `[h]` is ever pronounced. 'h muet' allows liaison/elision while 'h aspiré' blocks both, forcing hiatus (e.g. 'les héros' `[le.eʁo]`, not *`[le.zeʁo]`).
- `/ŋ/` is marginal and occurs only word-finally in loanwords ('parking' `/paʁ.kiŋ/`, 'camping' `/kɑ̃.piŋ/`); it never begins a native syllable.
- Native two-consonant onsets are predominantly obstruent + liquid (`/pl bl kl ɡl fl pʁ bʁ tʁ dʁ kʁ ɡʁ fʁ vʁ/`) obeying rising sonority; `/s/`+stop onsets (`/sp st sk/`) are largely confined to learned and borrowed words and are not freely word-initial in inherited vocabulary.
- Onsets obey the Sonority Sequencing Principle (rising sonority toward the nucleus); `/s/`+stop clusters are the chief sonority-reversal exception.
- Loi de position: the mid vowels' height is partly conditioned by syllable shape — in OPEN syllables the higher mid vowels `/e ø o/` are favored, and in CLOSED syllables the lower mid vowels `/ɛ œ ɔ/` are favored (e.g. open 'les' `/le/`, 'ceux' `/sø/`, 'beau' `/bo/` vs closed 'sel' `/sɛl/`, 'sœur' `/sœʁ/`, 'sol' `/sɔl/`). This tendency, the 'loi de position', ties vowel quality directly to syllable structure, though lexical exceptions and dialect differences exist.
- The schwa `/ə/` (e caduc) is freely deletable in many positions; its deletion creates consonant adjacencies that are then resyllabified (e.g. 'petite' `/pə.tit/` → `[ptit]`, with `/pt/` becoming a derived onset).
- Word-final coda clusters of the type obstruent + liquid (`/tʁ/`, `/bl/`) are frequently simplified in casual speech by liquid deletion ('quatre' `[kat]`, 'table' `[tab]`) or supported by an epenthetic schwa.
- Quebec French: the dental stops `/t d/` become affricates `[t͡s d͡z]` before the high front vowels and glides `/i y j ɥ/` ('petite' `[pt͡sɪt]`, 'dur' `[d͡zyʁ]`); high vowels `/i y u/` laxen to `[ɪ ʏ ʊ]` in closed syllables; and long vowels diphthongize in closed stressed syllables — all of which interact with syllable shape.
- Quebec French preserves the `/a/`~`/ɑ/` and nasal `/ɛ̃/`~`/œ̃/` contrasts (e.g. 'patte' `/pat/` vs 'pâte' `/pɑt/`; 'brin' `/bʁɛ̃/` vs 'brun' `/bʁœ̃/`), whereas Metropolitan French largely merges each pair.
- The Maximal Onset Principle governs medial consonant assignment and, distinctively for French, extends across word boundaries within a rhythmic group, subject to the resulting onset being an independently legal French onset.

## Phonological Rules

Active connected-speech and allophonic processes in Modern French, documented in parallel for Standard Metropolitan French (français standard, European/Parisian-based) and Quebec French (français québécois, Canadian). These rules describe systematic, largely automatic changes that apply to underlying phonemic forms to yield surface phonetic forms. Many operate at word boundaries within the rhythmic group (groupe rythmique / mot phonétique) as sandhi phenomena — French famously resyllabifies and chains words together, so the phonological word rarely coincides with the orthographic word. French has no lexical/contrastive stress; prominence falls only on the final full syllable of a rhythmic group, so these rules make no reference to word-level stress. Accent scope is marked as 'Metropolitan', 'Quebec', or 'both'; where a process applies in both varieties but differs in detail, the divergence is noted in the description. IPA examples are given as input → output, with /slashes/ for phonemic underlying forms and [brackets] for phonetic surface forms (IPA 2015 revision). Nasal vowels are written as base vowel + combining tilde.

### Rules at a Glance

| # | Rule | Process | Accents |
|---|---|---|---|
| 1 | Liaison (latent final consonant) | `C(latent) → [C] / __ # V`; s,x → [z]; d → [t]; f → [v] | both |
| 2 | Enchaînement (consonantal resyllabification) | `C(final) . V → . C V` | both |
| 3 | Élision (vowel deletion before a vowel) | `final /ə, a, i/ → ∅ / __ # V` | both |
| 4 | E-caduc / schwa deletion (e muet) | `/ə/ → (∅) / V C __ C V` | both |
| 5 | Vowel nasalization (V + coda N → nasal vowel) | `V N → Ṽ / __ {C, #}` | both |
| 6 | Loi de position (mid-vowel quality by syllable type) | `mid V → [e ø o] / open σ; → [ɛ œ ɔ] / closed σ` | both |
| 7 | Regressive voicing assimilation | `C[αvoice] → C[βvoice] / __ C[βvoice]` | both |
| 8 | Final-consonant silence | `C(orthographic) → ∅ / __ #` | both |
| 9 | H aspiré vs h muet | h-aspiré blocks liaison/elision; h-muet transparent | both |
| 10 | Affrication of /t d/ before high front vocoids | `/t d/ → [t͡s d͡z] / __ {i, y, j, ɥ}` | Quebec |
| 11 | High-vowel laxing in closed syllables | `/i y u/ → [ɪ ʏ ʊ] / __ C#` | Quebec |
| 12 | Long-vowel diphthongization | `Vː → [V̯V̯] / __ C#` | Quebec |
| 13 | /a/ ~ /ɑ/ and /ɛ̃/ ~ /œ̃/ contrasts | contrastive in Quebec, neutralized in Metropolitan | both |
| 14 | Devoicing and weakening of the uvular R | `/ʁ/ → [χ]` near voiceless C; `→ [ʁ̞ ~ ∅]` in coda clusters | both |
| 15 | Semivowel formation (gliding of high vowels) | `/i y u/ → [j ɥ w] / __ V` | both |

### Rule 1: Liaison (latent final consonant)

An orthographic final consonant that is normally silent in isolation surfaces and is pronounced when the next word in the same rhythmic group begins with a vowel (or h muet). The liaison consonant is resyllabified as the onset of the following vowel-initial word: les‿amis [le.za.mi]. Several liaison consonants undergo a fixed change in quality: final ‹s› and ‹x› link as [z] (les‿amis, deux‿heures [dø.zœʁ]), final ‹d› links as [t] (un grand‿homme [ɡʁɑ̃.tɔm], quand‿il [kɑ̃.til]), and final ‹f› links as [v] in a few items (neuf‿heures, neuf‿ans). Final ‹n› is realized as a pronounced nasal onset, often with retained or partly denasalized vowel (un‿ami, on‿a). Liaisons are classified as obligatory (determiner + noun, pronoun + verb, monosyllabic preposition + complement), optional (often after est, plural noun + adjective in elevated style), and forbidden (after a singular noun, after et, before h aspiré). Quebec French preserves the same core obligatory liaisons but tends to make fewer optional/stylistic liaisons than careful Metropolitan registers.

**IPA example:** `/z/` : les amis `/le + ami/` → `[le.za.mi]`; un grand homme `/ɡʁɑ̃ + ɔm/` → `[œ̃.ɡʁɑ̃.tɔm]`; neuf heures `/nœf + œʁ/` → `[nœ.vœʁ]`  
**IPA notation:** `C(latent) → [C] / __ # V (within the rhythmic group); s,x → [z]; d → [t]; f → [v]; n → nasal link`  
**Environment:** Latent word-final consonant immediately before a vowel-initial (or h-muet) word inside the same rhythmic group; blocked before h aspiré and after 'et'  
**Accents:** both  

### Rule 2: Enchaînement (consonantal resyllabification)

A consonant that is already pronounced at the end of a word is resyllabified as the onset of a following vowel-initial word, with no change in the consonant's identity. Thus 'elle est' is syllabified [ɛ.lɛ], not [ɛl.ɛ], and 'il arrive' becomes [i.la.ʁiv]. Enchaînement differs from liaison in that the consonant is pronounced even in isolation (it is not a latent consonant); only its syllabic affiliation shifts. The result is that French syllable boundaries cut across orthographic word boundaries, favouring open syllables (CV) and producing the characteristic smooth chaining of the rhythmic group. The process is fully general and automatic in both reference accents.

**IPA example:** `/l/` : elle est `/ɛl + ɛ/` → `[ɛ.lɛ]`; une autre `/yn + otʁ/` → `[y.notʁ]`; il arrive `/il + aʁiv/` → `[i.la.ʁiv]`  
**IPA notation:** `C(pronounced, final) . V → . C V (coda consonant becomes onset of next syllable)`  
**Environment:** Word-final pronounced consonant immediately before a vowel-initial word within the rhythmic group  
**Accents:** both  

### Rule 3: Élision (vowel deletion before a vowel)

A small set of high-frequency function words ending in a vowel drop that vowel before a vowel-initial (or h-muet) word, marked orthographically by an apostrophe. The clitics le, la → l' (l'homme [lɔm], l'eau [lo]); je → j' (j'arrive); de → d' (d'accord [da.kɔʁ]); ne → n' (n'est [nɛ]); que → qu' (qu'on [kɔ̃]); ce → c' (c'est [sɛ]); me, te, se → m', t', s'. The conjunction 'si' elides only before 'il(s)': s'il [sil], s'ils [sil], but 'si elle' stays [si.ɛl]. Élision deletes the vowel entirely (unlike e-caduc, which may merely be unrealized), and feeds resyllabification. The process is obligatory and identical in both reference accents.

**IPA example:** `/ə/ → ∅` : le ami → l'ami `/lami/` → `[la.mi]`; je ai → j'ai `/ʒe/` → `[ʒe]`; que il → qu'il `[kil]`; si il → s'il `[sil]`  
**IPA notation:** `final /ə, a, i(in 'si')/ → ∅ / __ # V (orthographic apostrophe)`  
**Environment:** Clitic/function word ending in /ə/ (or 'la' /a/, or 'si' before il) immediately before a vowel-initial or h-muet word; blocked before h aspiré  
**Accents:** both  

### Rule 4: E-caduc / schwa deletion (e muet)

The schwa /ə/ (e caduc, e muet, e instable) is variably deleted depending on the surrounding consonant cluster, speech rate, and register. It deletes most readily when its loss does not create a cluster of three consonants that is hard to syllabify. The governing constraint is the 'loi des trois consonnes' (three-consonant law): a schwa is retained when deleting it would bring three consonants together at the relevant juncture, and deleted when only two would remain. Thus 'samedi' → [sam.di] (deletion leaves /m.d/, fine), but 'vendredi' keeps its schwa [vɑ̃.dʁə.di] because deletion would yield the cluster /dʁd/. Word-final schwa is normally silent in both varieties (table [tabl], porte [pɔʁt]). Metropolitan French deletes schwa extensively, including word-initially in casual speech (petit [pti], je ne sais pas [ʃsɛpa]). Quebec French also deletes schwa freely and, in addition, frequently devoices or drops high vowels in similar weak positions; final schwa is likewise absent. Southern Metropolitan (Midi) varieties, by contrast, retain many more schwas — but that is outside the two reference accents documented here.

**IPA example:** `/ə/ → ∅` : samedi `/sam.ə.di/` → `[sam.di]`; petit `/pə.ti/` → `[pti]` (casual); une petite table → `[yn.ptit.tabl]`  
**IPA notation:** `/ə/ → (∅) / V C __ C V  (kept by loi des trois consonnes: …CC__C…)`  
**Environment:** Unstable /ə/ in non-final and final syllables; retention governed by the three-consonant law and by rhythmic-group position  
**Accents:** both  

### Rule 5: Vowel nasalization (V + coda N → nasal vowel)

Historically and synchronically, a vowel followed by a tautosyllabic nasal consonant in coda (i.e. with no following pronounced vowel) is realized as a nasal vowel, and the nasal consonant itself is not separately articulated: 'bon' [bɔ̃], 'vin' [vɛ̃], 'chambre' [ʃɑ̃bʁ]. When a vowel follows the nasal (often via a following suffix or liaison), nasalization is undone and the oral vowel + oral nasal consonant reappear: bon [bɔ̃] vs. bonne [bɔn], plein [plɛ̃] vs. pleine [plɛn], un [œ̃] vs. une [yn]. French has four phonemic nasal vowels /ɛ̃ ɑ̃ ɔ̃ œ̃/. A key accent split concerns /ɛ̃/ vs /œ̃/ ('brin' vs 'brun'): the two are largely merged to [ɛ̃] in Standard Metropolitan/Parisian French, but kept distinct in Quebec French, where 'brun' remains [bʁœ̃]. Quebec also tends to lower and back the nasal vowels phonetically (e.g. /ɛ̃/ → [ẽ]~[ãẽ̯], /ɔ̃/ → [õ]~[ũ]).

**IPA example:** `/Vn/ → [Ṽ]` : bon `/bɔn/` → `[bɔ̃]`; vin `/vɛn/` → `[vɛ̃]`; an `/an/` → `[ɑ̃]`; un `/œn/` → `[œ̃]~[ɛ̃]`  
**IPA notation:** `V N → Ṽ / __ {C, #} (no following pronounced vowel); N absorbed into the vowel`  
**Environment:** Oral vowel + nasal consonant in the same syllable coda, with no following pronounced vowel; reverses before a vowel  
**Accents:** both  

### Rule 6: Loi de position (mid-vowel quality by syllable type)

The three pairs of mid vowels — front unrounded /e ɛ/, front rounded /ø œ/, and back rounded /o ɔ/ — distribute partly by syllable structure, a tendency called the 'loi de position' (law of position). In an open syllable (ending in the vowel) the close (higher) member tends to occur: les [le], peu [pø], pot [po]. In a closed syllable (ending in a consonant) the open (lower) member tends to occur: sel [sɛl], seul [sœl], sort [sɔʁ]. The law is a strong tendency rather than an absolute rule and is overridden by lexical contrasts and orthography (e.g. word-final phonemic /ɛ/ vs /e/ in 'fait' vs 'fée'; /o/ before /z/ as in 'rose' [ʁoz]; /o/ from spelling ‹ô, au, eau›). The loi de position is far more rigorously and automatically applied in Quebec French (and in southern Metropolitan French) than in Standard Parisian French, where several lexical mid-vowel contrasts in final position survive more robustly.

**IPA example:** `/E,EU,O/` : open syll → close [e ø o] : 'les' `[le]`, 'peu' `[pø]`, 'pot' `[po]`; closed syll → open [ɛ œ ɔ] : 'sel' `[sɛl]`, 'peur' `[pœʁ]`, 'sort' `[sɔʁ]`  
**IPA notation:** `mid V → [+close e ø o] / open σ (V#) ; → [−close/open ɛ œ ɔ] / closed σ (VC#)`  
**Environment:** Stressable mid vowels; close allophone in open syllables, open allophone in closed syllables, modulated by lexical and orthographic factors  
**Accents:** both  

### Rule 7: Regressive voicing assimilation

When two obstruents come into contact (typically after schwa deletion or across a morpheme/word boundary), the first assimilates in voicing to the second: assimilation is regressive (right-to-left). A voiced obstruent devoices before a voiceless one and a voiceless obstruent voices before a voiced one. After e-caduc deletion, 'médecin' surfaces as [met.sɛ̃] (the /d/ devoices to [t] before voiceless [s]); 'absurde' is [ap.syʁd] (etymological /b/ devoiced to [p] before [s]). Conversely, voicing can spread leftward into a voiceless consonant before a voiced obstruent, e.g. 'anecdote' [a.nɛɡ.dɔt] (the ‹c› /k/ voices to [ɡ] before [d]). The voicing of the trigger dominates; the assimilated consonant generally keeps its own place and manner. The process operates in both reference accents and is fed by schwa deletion, which constantly creates new obstruent clusters.

**IPA example:** `/d/→[t]` : médecin `/me.dsɛ̃/` → `[met.sɛ̃]`; `/b/→[p]` : absurde `/ap.syʁd/` → `[ap.syʁd]`; `/s/→[z]` : 'cheval de course' anecdote → voicing spreads leftward  
**IPA notation:** `C[αvoice] → C[βvoice] / __ C[βvoice]  (obstruent takes voicing of the following obstruent)`  
**Environment:** Obstruent immediately followed by another obstruent of opposite voicing, especially clusters created by schwa deletion or at word boundaries  
**Accents:** both  

### Rule 8: Final-consonant silence

Most orthographic word-final consonants are not pronounced in isolation: ‹s, t, d, p, x, z, n (when nasalizing)› are typically silent — trop [tʁo], petit [pti], deux [dø], nez [ne], chaud [ʃo]. These silent consonants are 'latent' and may resurface in liaison (see Liaison). A common mnemonic is that the consonants in the word CaReFuL (‹c, r, f, l›) are MORE often pronounced word-finally than others: sac [sak], avec [a.vɛk], mer [mɛʁ], chef [ʃɛf], sel [sɛl] — though numerous exceptions exist (clef [kle], nerf [nɛʁ], gentil [ʒɑ̃.ti], the infinitival/‹-er› ‹r› silent as in parler [paʁ.le]). The pattern holds in both reference accents: in 'bout' [bu] and 'lit' [li] the orthographic final ‹t› is silent in every standard variety including Quebec (Quebec merely laxes the vowel of 'lit' to [lɪ], adding no [t]). Quebec does retain a final consonant in a handful of lexical items where Metropolitan usage may drop it — e.g. the numeral/adverb 'tout' keeps [tut] in fixed expressions and Quebec preserves final ‹t› in some words like 'fait' (noun) [fɛt] and certain borrowings — but these are isolated lexical facts, not a general audible-final-/t/ rule.

**IPA example:** `C(final) → ∅` : trop `/tʁo/` → `[tʁo]`; petit `/pə.ti/` → `[pti]`; tard → `[taʁ]` (r kept); avec → `[a.vɛk]` (k kept)  
**IPA notation:** `C(orthographic) → ∅ / __ # (most written final consonants silent; latent for liaison)`  
**Environment:** Word-final orthographic consonant at the end of a rhythmic group (no following vowel to trigger liaison/enchaînement)  
**Accents:** both  

### Rule 9: H aspiré vs h muet

Orthographic ‹h› is always silent in French, but words spelled with initial ‹h› fall into two lexically specified classes. With 'h muet' (mute h), the word behaves exactly as if it began with a vowel: élision and liaison apply normally — l'homme [lɔm], l'heure [lœʁ], les‿hommes [le.zɔm], un‿hôtel [œ̃.no.tɛl]. With 'h aspiré' (aspirate h — historically of Germanic origin, though no [h] is pronounced), the word behaves as consonant-initial for sandhi: it BLOCKS élision and liaison and prevents enchaînement, leaving a perceptible juncture (and sometimes a slight glottal onset). Thus 'le héros' is [lə.e.ʁo] (not *[le.ʁo]), 'les héros' is [le.e.ʁo] with no liaison [z], 'le haricot' [lə.a.ʁi.ko], 'le hibou' [lə.i.bu]. Class membership is lexical and must be learned word by word. Both reference accents observe the distinction, though h aspiré is eroding in casual usage and a few items vary by speaker.

**IPA example:** h aspiré: le héros `/lə + e.ʁo/` → `[lə.e.ʁo]` (no liaison/elision); h muet: l'homme `/lɔm/` → `[lɔm]`; les hommes → `[le.zɔm]`  
**IPA notation:** `Ø(h aspiré) blocks liaison/elision/enchaînement;  Ø(h muet) transparent (treated as vowel-initial)`  
**Environment:** Word-initial silent ‹h›: h-muet words pattern as vowel-initial (allow liaison/elision); h-aspiré words pattern as consonant-initial (block liaison/elision)  
**Accents:** both  

### Rule 10: Affrication of /t d/ before high front vocoids (Quebec)

A hallmark of Quebec (Laurentian) French: the alveolar stops /t/ and /d/ are affricated to [t͡s] and [d͡z] when they immediately precede a high front vowel /i/ or /y/, or the corresponding glides /j/ and /ɥ/. Thus 'petit' is [pt͡si], 'tu' is [t͡sy], 'dire' is [d͡ziʁ], 'dieu' is [d͡zjø], 'tien' is [t͡sjɛ̃], 'tuile' is [t͡sɥɪl], and 'mardi' is [maʁd͡zi]. The affrication does NOT occur before non-high or back vowels (tard [taʁ], deux [dø], tout [tu] keep plain [t d]). This is an automatic, fully productive allophonic rule in Quebec French and a primary perceptual marker of the accent. Standard Metropolitan French has no such affrication: /t d/ remain plain stops in all positions ([pti], [ty], [diʁ]).

**IPA example:** `/t d/ → [t͡s d͡z]` : petit `/pəti/` → `[pt͡si]`; dire `/diʁ/` → `[d͡ziʁ]`; tu `/ty/` → `[t͡sy]`; dieu → `[d͡zjø]`  
**IPA notation:** `/t d/ → [t͡s d͡z] / __ {i, y, j, ɥ}  (before high front vowels and their glides)`  
**Environment:** Alveolar stops /t d/ directly before high front vowels /i y/ or glides /j ɥ/; not before other vowels  
**Accents:** Quebec  

### Rule 11: High-vowel laxing in closed syllables (Quebec)

In Quebec French the close vowels /i y u/ are laxed to [ɪ ʏ ʊ] when they occur in a closed syllable that is final in the rhythmic group, provided the closing consonant is not one of the 'lengthening' consonants /ʁ v z ʒ/ (and not before a syllable-final vocoid). Thus 'petite' is [pt͡sɪt], 'vite' [vɪt], 'lune' [lʏn], 'jupe' [ʒʏp], 'route' [ʁʊt], 'douze' however keeps tense [duz] because /z/ lengthens. The laxing typically also spreads to harmonize earlier high vowels in the word (vowel harmony). The vowels remain tense [i y u] in open syllables (lit [li], vu [vy], loup [lu]) and before lengthening consonants (livre, vive, ruse). Standard Metropolitan French does not lax high vowels: /i y u/ are uniformly tense [i y u] in all syllable types.

**IPA example:** `/i y u/ → [ɪ ʏ ʊ]` : petite `/ptit/` → `[pt͡sɪt]`; lune `/lyn/` → `[lʏn]`; route `/ʁut/` → `[ʁʊt]`; vite → `[vɪt]`  
**IPA notation:** `/i y u/ → [ɪ ʏ ʊ] / __ C# (final closed syllable, not before lengthening cons.)`  
**Environment:** Close vowels /i y u/ in a final closed syllable, except before the lengthening consonants /ʁ v z ʒ/; subject to high-vowel harmony  
**Accents:** Quebec  

### Rule 12: Long-vowel diphthongization (Quebec)

In Quebec French, phonologically long vowels in a stressed (rhythmic-group-final) closed syllable are commonly realized as diphthongs (a glide-on or glide-off). Long /ɛː/ diphthongizes to [aɛ̯]~[aɪ̯] (père [paɛ̯ʁ], fête [faɛ̯t], neige [naɛ̯ʒ]); /ɑ/ to [ɑʊ̯]~[ɑɔ̯] (pâte [pɑʊ̯t]); the rounded mid and back vowels and nasal vowels likewise glide (fort [fɑɔ̯ʁ], peur [paœ̯ʁ], chose [ʃoʊ̯z], monde [mõʊ̯̃d]). The diphthongization targets vowels lengthened either lexically or by a following lengthening consonant /ʁ v z ʒ/. It is a salient feature of basilectal and colloquial Quebec speech, attenuated in formal registers. Standard Metropolitan French has lost most distinctive vowel length and does not diphthongize: these vowels stay monophthongal ([pɛʁ], [pat], [fɔʁ]).

**IPA example:** `/ɛː ɑ ø o ɔ̃/` : père `/pɛːʁ/` → `[paɛ̯ʁ]`; pâte `/pɑt/` → `[pɑʊ̯t]`; fort `/fɔʁ/` → `[fɑɔ̯ʁ]`; neige → `[naɛ̯ʒ]`  
**IPA notation:** `Vː → [V̯V̯] / __ C# (stressed long vowels in final closed syllables diphthongize)`  
**Environment:** Long/lengthened vowels in a stressed final closed syllable, especially before lengthening consonants; register-dependent  
**Accents:** Quebec  

### Rule 13: /a/ ~ /ɑ/ and /ɛ̃/ ~ /œ̃/ contrasts

Two historical contrasts of the French vowel system are maintained in Quebec French but largely merged in Standard Metropolitan/Parisian French. (1) The front /a/ vs back /ɑ/ opposition ('patte' [pat] vs 'pâte' [pɑt], 'mal' vs 'mâle', 'tache' vs 'tâche') is robustly kept in Quebec — where /ɑ/ is markedly back and may be rounded toward [ɒ] and is often the vowel that diphthongizes — but is mostly lost in Parisian French, where many speakers use a single front [a] for both. (2) The nasal contrast /ɛ̃/ vs /œ̃/ ('brin' [bʁɛ̃] vs 'brun' [bʁœ̃], 'empreinte' vs 'emprunte') is preserved in Quebec but neutralized to [ɛ̃] for most Metropolitan speakers, so that 'brin' and 'brun' are homophones in Paris but distinct in Montreal. These are inventory/contrast differences rather than purely allophonic rules, and they interact with nasalization, the loi de position, and Quebec diphthongization.

**IPA example:** `/a/ vs /ɑ/` : 'patte' `[pat]` vs 'pâte' `[pɑt]`; `/ɛ̃/ vs /œ̃/` : 'brin' `[bʁɛ̃]` vs 'brun' `[bʁœ̃]`  
**IPA notation:** `/a/–/ɑ/ and /ɛ̃/–/œ̃/ : contrastive in Quebec, largely neutralized in Metropolitan`  
**Environment:** Lexically specified /a/–/ɑ/ pairs and /ɛ̃/–/œ̃/ nasal pairs; kept distinct in Quebec, merged in Standard Metropolitan  
**Accents:** both  

### Rule 14: Devoicing and weakening of the uvular R

The French rhotic /ʁ/ is a voiced uvular fricative/approximant, but it is highly context-sensitive. Adjacent to a voiceless consonant it devoices to the voiceless uvular fricative [χ] (quatre [katχ], propre [pχ-]); intervocalically it is a smooth voiced [ʁ] (Paris [pa.ʁi]); in word-final post-consonantal clusters it is frequently weakened, syllabified, or dropped in casual speech ('quatre' → [kat], 'autre' → [ot]), which feeds the three-consonant law and schwa retention. Both reference accents use a uvular R as the standard variant (the older apical/trilled [r] persists only in conservative or rural Quebec and some southern Metropolitan speech and is now recessive). Quebec French has historically shown more variation between apical [r] and uvular [ʁ]/[ʀ], with younger urban (Montreal) speakers having largely shifted to the posterior [ʁ] shared with Metropolitan French.

**IPA example:** `/ʁ/ → [χ]` : 'quatre' `/katʁ/` → `[katχ̩]~[kat]`; 'lettre' `/lɛtʁ/` → `[lɛtχ̩]`; intervoc. [ʁ] in 'Paris' `[pa.ʁi]`  
**IPA notation:** `/ʁ/ → [χ] / next to voiceless C ; → [ʁ̞ ~ ∅] / in coda clusters (casual)`  
**Environment:** Devoicing next to voiceless obstruents; weakening/deletion in word-final consonant clusters in casual speech  
**Accents:** both  

### Rule 15: Semivowel formation (gliding of high vowels before a vowel)

The high vowels /i y u/ are realized as the corresponding semivowels (glides) [j ɥ w] when they directly precede another vowel within the same syllable, reducing a potential two-vowel sequence (hiatus) to a single tautosyllabic glide-plus-vowel: 'lier' [lje], 'nuit' [nɥi], 'oui' [wi], 'louer' [lwe]. The labio-palatal glide [ɥ] (from /y/, as in 'huit' [ɥit], 'lui' [lɥi], 'nuage' [nɥaʒ]) is cross-linguistically rare and is a distinctive feature of French. Gliding is blocked, and hiatus retained, after certain heavy onsets (e.g. obstruent + liquid, as in 'oublier' which keeps [li.e] for many speakers, 'crier' [kʁi.je]), and h-aspiré or morphological factors can also force a hiatus. Both reference accents form these glides; Quebec usage shows somewhat more variation in retaining hiatus and in the realization of /ɥ/, but the core process is shared.

**IPA example:** `/i y u/ → [j ɥ w]` : 'lier' `/li.e/` → `[lje]`; 'lui' `/lyi/` → `[lɥi]`; 'louer' `/lu.e/` → `[lwe]`; 'huit' → `[ɥit]`  
**IPA notation:** `/i y u/ → [j ɥ w] / __ V (high vowel becomes corresponding glide before another vowel)`  
**Environment:** Underlying high vowel /i y u/ immediately before another vowel in the same syllable; blocked after some complex onsets, yielding hiatus  
**Accents:** both  

### Notes

Many of these processes are gradient, rate-dependent, and register-sensitive: they apply more fully in fast, casual speech and may be suppressed in careful or formal styles (e.g. extensive schwa deletion, optional liaisons, h-aspiré erosion). The defining sandhi processes of French — liaison, enchaînement, élision, and schwa deletion under the three-consonant law — operate across word boundaries within the rhythmic group (groupe rythmique) and continually resyllabify the speech stream into open CV syllables, so the phonological word seldom matches the orthographic word; voicing assimilation is regressive and is fed by the clusters that schwa deletion creates. Because French stress is non-lexical and falls only on the final full syllable of the rhythmic group, none of these rules refer to word-level stress. The principal Metropolitan/Quebec divergences in this section are: in Quebec, automatic affrication of /t d/ → [t͡s d͡z] before high front vocoids, laxing of /i y u/ → [ɪ ʏ ʊ] in final closed syllables, diphthongization of long vowels, a more rigorous loi de position, and preservation of the /a/–/ɑ/ and /ɛ̃/–/œ̃/ contrasts; Standard Metropolitan French lacks the affrication, laxing, and diphthongization and largely merges /a/ with /ɑ/ and /œ̃/ with /ɛ̃/. Liaison, enchaînement, élision, nasalization, semivowel formation, the silence of most final consonants, and the h-muet/h-aspiré distinction are shared by both reference accents.

## Liaison & Connected Speech

The segmental processes of connected (running) speech in Modern French, occupying the slot that "weak forms" occupy in the English guide. French has **no** English-style strong/weak-form alternation: function words are not reduced to a central schwa under stresslessness, because French stress is **phrasal** (fixed on the final full syllable of a rhythmic group), not lexical. Instead, French reshapes word boundaries through four signature sandhi processes — **liaison** (sounding of a normally silent word-final consonant before a following vowel), **élision** (deletion of a final vowel, usually orthographic e/a/i, before a following vowel), **enchaînement** (re-syllabification of a pronounced final consonant as the onset of the next syllable), and the variable presence/absence of **e-caduc** (schwa, the "mute e") — plus the chaining of clitic pronouns. These conspire to keep French speech maximally open-syllabled and vowel-onset-free across word boundaries.

**Applies to:** Spontaneous and fluent connected speech in both reference accents. Obligatory liaison and obligatory élision apply at every register; optional liaison, e-caduc retention, and enchaînement detail are gradient and register-dependent — optional liaisons increase with formality, careful reading, oratory, song, and classical theatre, and decrease in casual conversation. The processes are computed left-to-right across the rhythmic group (groupe rythmique / mot phonologique); they do not cross a major prosodic boundary (pause, end of intonation phrase).

### Reference Accents

- **Standard Metropolitan:** Français standard / European Parisian-based French (non-rhotic in the English sense; uvular `/ʁ/`; `/a/`~`/ɑ/` and nasal `/ɛ̃/`~`/œ̃/` contrasts largely **merged**; no high-vowel laxing; no affrication of `/t d/`).
- **Quebec:** Français québécois / Canadian French (uvular or apical R; `/t d/` **affricate** to `[t͡s d͡z]` before `/i y j ɥ/`; high vowels `/i y u/` **lax** to `[ɪ ʏ ʊ]` in closed final syllables; long vowels **diphthongise** under stress; `/a/`~`/ɑ/` and nasal `/ɛ̃/`~`/œ̃/` contrasts **kept** distinct).

**No weak forms note:** Unlike English (a, the, of, to → `/ə/`), French function words do not centralise to schwa when unstressed. "de", "le", "que", "ne", "je", "ce" etc. contain a lexical e-caduc `/ə/` in their citation form already; in connected speech that `/ə/` is variably **deleted** (je ne sais pas → `[ʒən sɛ pa]` ~ `[ʒ‿sɛ pa]`), not reduced from a fuller vowel. The French analog of "reduction" is therefore e-caduc deletion and clitic chaining, documented below, not vowel centralisation. Where English neutralises vowel quality, French preserves vowel quality and instead manipulates the consonant–vowel sequencing at the boundary (liaison, élision, enchaînement).

### Liaison

**Liaison** is the pronunciation of a word-final consonant that is **silent** in the word's isolation (citation) form but surfaces — and re-syllabifies as the onset of the next syllable — when the following word begins with a vowel or mute h. The liaison consonant belongs phonologically to the first word (a "latent" final consonant) but is realised in the syllable of the second word.

#### Liaison Consonant Values

The orthographic letter that triggers a liaison does **not** always surface with its citation value: latent finals undergo fixed voicing/fortition changes when they liaise.

| Orthography | Liaison value | Notes | Example |
|---|---|---|---|
| s, x, z | `[z]` | Final orthographic -s and -x are silent in isolation but surface as voiced `[z]` in liaison (devoicing of the latent consonant does not occur prevocalically). | les enfants `[le.z‿ɑ̃.fɑ̃]`; deux hommes `[dø.z‿ɔm]`; chez elle `[ʃe.z‿ɛl]`; aux États-Unis `[o.z‿e.ta.zy.ni]` |
| d | `[t]` | Final -d surfaces as **voiceless** `[t]` in liaison (final-obstruent fortition); chiefly in "grand", "quand", and inverted 3sg verb forms (prend-il, attend-elle). | un grand homme `[œ̃ ɡʁɑ̃.t‿ɔm]`; quand il `[kɑ̃.t‿il]`; prend-il `[pʁɑ̃.t‿il]` |
| f | `[v]` | Final -f surfaces as **voiced** `[v]` in liaison, but ONLY in the two fixed expressions "neuf ans" and "neuf heures"; elsewhere "neuf" keeps `[f]` (neuf élèves `[nœf e.lɛv]`, not `[v]`). | neuf heures `[nœ.v‿œʁ]`; neuf ans `[nœ.v‿ɑ̃]` |
| n | `[n]` (with variable de-nasalisation of the preceding vowel) | After a nasal vowel, liaison surfaces the `[n]`. In "bon, en, on, un, mon, ton, son, rien, bien, aucun" the vowel may **de-nasalise** (bon ami `[bɔ.n‿a.mi]`, oral `[ɔ]`) or, in many speakers/Quebec, stay nasal with an added `[n]` (bon ami `[bɔ̃.n‿a.mi]`). Possessives "mon/ton/son" and "on/en/un" typically keep the nasal vowel. | un bon ami `[œ̃ bɔ.n‿a.mi]` ~ `[œ̃ bɔ̃.n‿a.mi]`; on a `[ɔ̃.n‿a]`; en avion `[ɑ̃.n‿a.vjɔ̃]`; mon ami `[mɔ̃.n‿a.mi]` |
| t | `[t]` | Final -t (silent in isolation) surfaces as `[t]`; very common in verb endings (-ent, -t, -ait, est, sont, ont), the never-liaising conjunction "et" **excepted** (see forbidden). | est-il `[ɛ.t‿il]`; ils sont arrivés `[il sɔ̃.t‿a.ʁi.ve]`; un petit ami `[œ̃ pə.ti.t‿a.mi]`; tout entier `[tu.t‿ɑ̃.tje]` |
| r | `[ʁ]` | After ordinal/numeral-type "-er" words such as "premier", "dernier", "-r" liaison (latent `[ʁ]`) is a normal, commonly-made liaison in ordinary careful speech, though optional. In "-er" infinitives and other -r-final words the resurfacing of -r is marginal/literary and confined to elevated or sung style. | premier étage `[pʁə.mje.ʁ‿e.taʒ]`; léger ennui `[le.ʒe.ʁ‿ɑ̃.nɥi]` |
| p, g | `[p]`, `[k]` | Highly restricted, archaic/literary only: "trop", "beaucoup" → `[p]`; "long", "sang" historically → `[k]` (sang impur, "La Marseillaise"). Not productive in ordinary speech. | trop heureux `[tʁo.p‿ø.ʁø]`; sang impur `[sɑ̃.k‿ɛ̃.pyʁ]` (anthem/literary) |

#### Obligatory Liaison

Obligatory liaison is categorical: it is present at every speech rate and register. It binds within tight syntactic units.

| Context | Description | Example |
|---|---|---|
| Determiner + noun/adjective | Article, possessive, demonstrative, or quantifier and the following noun or prenominal adjective are bound; liaison is obligatory. | les enfants `[le.z‿ɑ̃.fɑ̃]`; un homme `[œ̃.n‿ɔm]`; ces amis `[se.z‿a.mi]`; mes idées `[me.z‿i.de]`; deux ans `[dø.z‿ɑ̃]`; aux hommes `[o.z‿ɔm]` |
| Subject/object clitic pronoun + verb | The proclitic pronouns (nous, vous, ils, elles, on, en, y, les) bind to the verb; liaison obligatory. | nous avons `[nu.z‿a.vɔ̃]`; vous êtes `[vu.z‿ɛt]`; ils ont `[il.z‿ɔ̃]`; elles aiment `[ɛl.z‿ɛm]`; on a `[ɔ̃.n‿a]`; ils en ont `[il.z‿ɑ̃.n‿ɔ̃]` |
| Verb + clitic pronoun (inversion) | In inverted (interrogative) order the latent verb-final consonant liaises onto the postposed pronoun; obligatory. | est-il `[ɛ.t‿il]`; sont-elles `[sɔ̃.t‿ɛl]`; vont-ils `[vɔ̃.t‿il]`; prend-on `[pʁɑ̃.t‿ɔ̃]` (the `[t]` is the latent final -d of "prend" fortified to `[t]`, not an inserted -t-); a-t-il `[a.t‿il]` (genuine epenthetic -t-, inserted because the verb "a" ends in a vowel) |
| Prenominal adjective + noun | A monosyllabic or common prenominal adjective binds to its noun; liaison obligatory. | petit ami `[pə.ti.t‿a.mi]`; petit enfant `[pə.ti.t‿ɑ̃.fɑ̃]`; grand homme `[ɡʁɑ̃.t‿ɔm]`; bon élève `[bɔ.n‿e.lɛv]`; gros effort `[ɡʁo.z‿e.fɔʁ]` |
| Monosyllabic preposition + complement | Short prepositions/particles (en, dans, chez, sans, sous, dès) liaise obligatorily with a vowel-initial complement. | en avion `[ɑ̃.n‿a.vjɔ̃]`; dans un an `[dɑ̃.z‿œ̃.n‿ɑ̃]`; chez elle `[ʃe.z‿ɛl]`; sans elle `[sɑ̃.z‿ɛl]`; sous un arbre `[su.z‿œ̃.n‿aʁbʁ]` |
| Monosyllabic adverb + adjective/adverb | Degree adverbs "très", "plus", "bien", "trop", "moins" liaise obligatorily with a following vowel-initial word they modify. | très important `[tʁɛ.z‿ɛ̃.pɔʁ.tɑ̃]`; plus utile `[ply.z‿y.til]`; bien aimable `[bjɛ̃.n‿ɛ.mabl]`; moins étrange `[mwɛ̃.z‿e.tʁɑ̃ʒ]` |
| Fixed/lexicalised expressions | Frozen phrases carry an obligatory internal liaison regardless of the general rules. | tout à fait `[tu.t‿a.fɛ]`; de temps en temps `[də tɑ̃.z‿ɑ̃ tɑ̃]`; les États-Unis `[le.z‿e.ta.zy.ni]`; comment allez-vous `[kɔ.mɑ̃.t‿a.le vu]`; petit à petit `[pə.ti.t‿a pə.ti]` |

#### Optional Liaison

Optional liaison is gradient: it increases with formality, careful reading, oratory and song, and is dropped in casual conversation.

| Context | Description | Example |
|---|---|---|
| Plural noun + following adjective | After a plural noun the latent `[z]` may or may not liaise onto a vowel-initial adjective; present in careful/formal speech, dropped in casual. | des enfants intelligents `[de.z‿ɑ̃.fɑ̃(.z‿)ɛ̃.te.li.ʒɑ̃]` — liaison on "enfants" optional |
| Forms of être + complement | After "est, sont, était, étaient, suis, es" etc., liaison onto a vowel-initial predicate is optional (frequent but not required). | il est arrivé `[i.l‿ɛ(.t‿)a.ʁi.ve]`; ils sont allés `[il sɔ̃(.t‿)a.le]`; c'est important `[sɛ(.t‿)ɛ̃.pɔʁ.tɑ̃]` (very commonly made) |
| Auxiliary/modal verb + past participle or infinitive | After "avoir", "aller", "vouloir", "devoir", "pouvoir" forms, liaison onto a following vowel-initial verb is optional and formal. | j'ai été `[ʒe(.t)‿e.te]` (rare); ils ont eu `[il.z‿ɔ̃(.t)‿y]`; on doit aller `[ɔ̃ dwa(.t)‿a.le]` |
| Polysyllabic preposition / adverb + complement | After "après, depuis, pendant, toujours, jamais, beaucoup, assez" liaison is optional and tends toward formal register; in casual speech it is dropped. | toujours utile `[tu.ʒu.ʁ(‿)y.til]`; pendant un an `[pɑ̃.dɑ̃(.t‿)œ̃.n‿ɑ̃]`; jamais aimé `[ʒa.mɛ(.z‿)e.me]`; beaucoup aimé `[bo.ku(.p‿)e.me]` (formal) |

#### Forbidden Liaison

In some contexts the latent consonant must stay silent even before a vowel; the boundary (`|`) blocks linking.

| Context | Description | Example |
|---|---|---|
| After a singular noun | No liaison from a singular noun onto a following vowel-initial word; the latent consonant stays silent. (Plural nouns allow optional liaison; singular nouns forbid it.) | un enfant intelligent `[œ̃.n‿ɑ̃.fɑ̃` `|` `ɛ̃.te.li.ʒɑ̃]` — NO liaison after "enfant"; un repas excellent `[œ̃ ʁə.pa` `|` `ɛk.se.lɑ̃]` |
| After the conjunction "et" | "et" (and) NEVER liaises; its final -t is permanently silent even before a vowel. This prevents confusion with "est". | et il `[e` `|` `il]` (never `[e.t‿il]`); un homme et une femme `[œ̃.n‿ɔm e` `|` `yn fam]`; lui et elle `[lɥi e` `|` `ɛl]` |
| Before h aspiré (aspirate h) | Words beginning with "h aspiré" (historically Germanic, lexically marked) block liaison and élision, behaving as consonant-initial. Contrast with "h muet" (mute h), which permits liaison/élision. | les héros `[le` `|` `e.ʁo]` (h aspiré, no liaison) vs les hommes `[le.z‿ɔm]` (h muet, liaison); en haut `[ɑ̃` `|` `o]`; les haricots `[le` `|` `a.ʁi.ko]`; le hibou `[lə` `|` `i.bu]` (no élision) |
| Before "onze", "oui", "yaourt", "huit/un" (counting numerals as enumerated items) | Certain vowel-initial words behave like h-aspiré words and block liaison: "onze", "oui", "huit" (variably), "yaourt", and "un/huit" when cited as numbers. | les onze joueurs `[le | ɔ̃z ʒu.œʁ]`; un oui `[œ̃ | wi]`; les huit `[le | ɥit]` |
| Before a pause / across a major prosodic boundary | Liaison cannot cross a comma, clause boundary, or any pause; it is internal to the rhythmic group only. | Ils sont partis, `|` et ils reviennent — no liaison across the comma boundary |
| After the interrogative "comment" (except the fixed "comment allez-vous") | Outside the frozen greeting, "comment" before a vowel generally does not liaise in modern usage. | Comment es-tu venu? `[kɔ.mɑ̃ ɛ ty və.ny]` (no liaison) vs fixed: comment allez-vous `[kɔ.mɑ̃.t‿a.le vu]` |

### Élision

**Élision** is the obligatory deletion of a word-final vowel (orthographically marked by an apostrophe) when the next word begins with a vowel or h muet, avoiding hiatus. It targets the final vowel of a closed set of monosyllabic function words.

**Type:** vowel deletion (anti-hiatus)

| Word(s) | Elided form | IPA example |
|---|---|---|
| le, la (articles / object clitics) | l' | l'ami `[l‿a.mi]`; l'eau `[l‿o]`; l'heure `[l‿œʁ]` (h muet); je l'aime `[ʒə l‿ɛm]` |
| de (preposition) | d' | d'accord `[d‿a.kɔʁ]`; pas d'eau `[pa d‿o]`; beaucoup d'amis `[bo.ku d‿a.mi]` |
| je, me, te, se, ce, ne, que (clitics / complementiser) | j', m', t', s', c', n', qu' | j'ai `[ʒ‿e]`; il m'aime `[il m‿ɛm]`; je t'aime `[ʒə t‿ɛm]`; il s'appelle `[il s‿a.pɛl]`; c'est `[s‿ɛ]`; je n'ai pas `[ʒə n‿e pa]`; qu'il vienne `[k‿il vjɛn]` |
| si (only before "il", "ils") | s' | s'il vous plaît `[s‿il vu plɛ]`; s'ils arrivent `[s‿il.z‿a.ʁiv]`. Note: "si elle" does NOT elide (`[si ɛl]`). |
| lorsque, puisque, quoique, jusque (conjunctions ending in -que) | lorsqu', puisqu', quoiqu', jusqu' | lorsqu'il `[lɔʁ.sk‿il]`; puisqu'on `[pɥi.sk‿ɔ̃]`; jusqu'à `[ʒys.k‿a]` |
| la (in "la" demonstrative "-là" and a few others — limited) | — | Élision does NOT apply to "la" as the adverb/stressed deictic; only the article/clitic "la" elides. |

**h muet vs h aspiré:** Élision (like liaison) is governed by the h muet / h aspiré distinction. Before **h muet**, élision is obligatory: l'homme `[l‿ɔm]`, l'hôtel `[l‿o.tɛl]`, d'habitude `[d‿a.bi.tyd]`. Before **h aspiré**, élision is **blocked**: le héros `[lə e.ʁo]`, la hauteur `[la o.tœʁ]`, de honte `[də ɔ̃t]`. The h is silent in BOTH cases; only its phonological behaviour at the boundary differs.

**Quebec note:** Quebec colloquial speech extends élision-like deletion further in casual register (e.g. "t'es" for "tu es" `[t‿e]`, "chu" / "chui" for "je suis" `[ʃy]`/`[ʃɥi]`), and frequently reduces "il/ils" to `[i]` and "elle" to `[a]`/`[ɛ]` before consonants, but the orthographic élisions above are shared with the standard.

### Enchaînement

**Enchaînement** is the re-syllabification of an **already-pronounced** word-final consonant as the onset of a following vowel-initial syllable, so the consonant is heard at the start of the next word. It differs from liaison in that the consonant is pronounced in isolation too (not latent); enchaînement merely re-locates the syllable boundary.

**Type:** re-syllabification (linking)

**Contrast with liaison:** Liaison surfaces a **silent** (latent) consonant: "petit ami" `[pə.ti.t‿a.mi]` — the -t is silent in "petit" alone `[pə.ti]`. Enchaînement re-syllabifies an **always-pronounced** consonant: "petite amie" `[pə.ti.t‿a.mi]` — the -t is already pronounced in "petite" `[pə.tit]`; it just shifts onset. Audibly similar, structurally distinct.

| Phrase | IPA | Note |
|---|---|---|
| une amie | `[y.n‿a.mi]` | The `/n/` of "une" (pronounced `[yn]` in isolation) becomes the onset of "a-": `[y.na.mi]`. |
| avec elle | `[a.vɛ.k‿ɛl]` | Final `/k/` of "avec" (always pronounced) re-syllabifies as onset of "elle". |
| il arrive | `[i.l‿a.ʁiv]` | Final `/l/` of "il" becomes onset of "arrive": `[i.la.ʁiv]`. |
| quelle heure | `[kɛ.l‿œʁ]` | Final `/l/` of "quelle" re-syllabifies onto "heure" (h muet). |
| cette histoire | `[sɛ.t‿is.twaʁ]` | Final `/t/` of "cette" (always pronounced) onsets "histoire". Compare liaison "cet homme" `[sɛ.t‿ɔm]` where the -t is latent. |

**Global consequence:** Enchaînement + liaison + élision together make French an "open-syllable, no-glottal-onset" language across boundaries: vowel-initial words almost never begin with a true glottal/vowel onset in connected speech; an onset consonant is supplied from the left context. (Hiatus, when unavoidable, is tolerated but not bridged by a glide as systematically as in English: "il y a un" `[i.lja œ̃]` uses `/j/` lexically, not as inserted liaison.)

### E-caduc

**E-caduc** (also "e muet", "e instable", schwa `/ə/`) is a vowel that is variably **present** or **deleted** depending on its phonetic environment, position, register, and speech rate. Orthographically it is the letter "e" without an accent in an open syllable or word-finally. Its deletion is the principal "reduction" mechanism of French connected speech (the functional analog of English vowel reduction, though it is **deletion** of `/ə/`, not centralisation **to** `/ə/`).

**Phonetic value:** Realised as a rounded mid-central-to-front-rounded vowel, conventionally `[ə]` but phonetically close to `[œ]`~`[ø]` in standard French; fully rounded. NOT the unrounded English schwa.

#### Deletion Rules

| Rule | Description | Example |
|---|---|---|
| Word-final e-caduc: deleted | Final orthographic -e is silent (deleted) in standard French, except where needed to support a final consonant cluster or in poetry/song. | table `[tabl]` (final e deleted); une petite femme `[yn pə.tit fam]`; porte `[pɔʁt]`. In Southern French / sung verse it may surface: `[ta.blə]`. |
| Loi des trois consonnes (three-consonant law) | An internal e-caduc is **retained** when its deletion would create a cluster of three or more consonants difficult to syllabify; it is **deleted** when deletion leaves an acceptable two-consonant sequence. | RETAINED: "gouvernement" `[ɡu.vɛʁ.nə.mɑ̃]` (deleting `/ə/` → `/ʁnm/` illicit); "vendredi" `[vɑ̃.dʁə.di]`. DELETED: "samedi" `[sam.di]` (→ `/md/` ok); "maintenant" `[mɛ̃t.nɑ̃]`; "acheter" `[aʃ.te]`. |
| Initial-syllable e-caduc in clitics (monosyllable-chain reduction) | In the proclitic monosyllables je, me, te, se, ce, le, de, ne, que, the e-caduc deletes freely in casual speech when the result is pronounceable, often producing assimilation of the stranded consonant. | je ne sais pas `[ʒə nə sɛ pa]` → `[ʒən sɛ pa]` → casual `[ʃ sɛ pa]` (j' devoiced before `/s/`); je te le donne `[ʒə tə lə dɔn]` → `[ʒtə l dɔn]` ~ `[ʃtə l dɔn]`; ce que `[skə]`. |
| Phrase-initial / post-pause retention | An e-caduc at the very start of a rhythmic group (preceded by pause) is normally **retained**, since there is no preceding vowel to support cluster simplification. | "Je pense" utterance-initial `[ʒə pɑ̃s]` (retained) vs mid-phrase "et je pense" `[e ʒpɑ̃s]` (deletable). |
| Successive e-caducs (alternation) | In a string of consecutive e-caduc syllables, they delete in **alternation** (every other one) to keep clusters legal; which ones delete depends on direction of scanning and dialect. | "je ne te le redemande" — alternating deletion, e.g. `[ʒən tə l ʁə.də.mɑ̃d]` ~ `[ʒ nə t lə ʁ.də.mɑ̃d]`; "je ne le" → `[ʒən lə]` or `[ʒ nə l]`. |
| Final -e supporting liaison/enchaînement | When the deleted final -e would otherwise strand a consonant needing an onset, enchaînement onto the next word's vowel resolves it. | "une autre idée" `[y.n‿o.tʁ‿i.de]` — final -e of "autre" deleted, `/tʁ/` enchaîné onto "idée". |

#### Register and Dialect

| Variety | E-caduc behaviour |
|---|---|
| Standard Metropolitan | Northern/Parisian standard deletes e-caduc aggressively; word-final -e is essentially always silent and internal -e drops wherever the three-consonant law permits. |
| Southern French (Méridional) | Retains e-caduc much more (table `[ta.blə]`, une petite `[y.nə pə.ti.tə]`), giving the characteristic "accent du Midi" — noted for contrast though not a target accent here. |
| Quebec | Generally patterns with the northern standard for e-caduc deletion, but with its own affrication consequences: when a `/t/` or `/d/` is stranded before a high front vowel after e-caduc deletion, it **affricates** — e.g. "petit" `[pt͡si]`~`[p(ə)t͡si]`, "de" often `[d͡z(ə)]` before `[i]`/`[y]`. |

### Clitics

French **clitics** are unstressable monosyllabic grammatical words (subject pronouns, object/reflexive pronouns, the negative "ne", determiners, short prepositions, "y" and "en") that attach phonologically to an adjacent host (usually the verb) and form a single prosodic word with it. Their internal e-caduc is subject to the deletion rules above; their final consonants feed liaison/enchaînement.

#### Subject Clitics

**Members:** je, tu, il(s), elle(s), on, nous, vous

**Behaviour:** Proclitic to the finite verb. Liaise obligatorily when latent-consonant-final and prevocalic (nous avons `[nu.z‿a.vɔ̃]`, ils ont `[il.z‿ɔ̃]`, on a `[ɔ̃.n‿a]`). "je" elides (j'ai) and its `/ʒ/` assimilates in voice to a following voiceless clitic ("je suis" → casual `[ʃ(ɥ)i]`). In Quebec colloquial, "il(s)" → `[i]`, "elle" → `[a]`/`[ɛ]`, "tu es" → `[t‿e]`.

- **Example:** ils en ont eu `[il.z‿ɑ̃.n‿ɔ̃.t‿y]` — chained liaisons across subject + en + ont + (optional) eu

#### Object and Reflexive Clitics

**Members:** me, te, se, le, la, les, lui, leur, nous, vous, y, en

**Ordering:** Fixed preverbal order (me/te/se/nous/vous > le/la/les > lui/leur > y > en) in declaratives; the cluster forms one phonological word with the verb, within which e-caducs delete by the three-consonant law and alternation rules.

- **Example:** je te le donne `[ʒə.t(ə).lə.dɔn]` → casual `[ʒtə l dɔn]` ~ `[ʃtə l dɔn]`; il m'en a parlé `[il m‿ɑ̃.n‿a paʁ.le]`; je les y ai vus `[ʒə le.z‿i e vy]`; donne-le-moi `[dɔn.lə.mwa]` (postverbal in imperative, e-caduc more stable).

#### Negative Clitic "ne"

**Behaviour:** "ne" is proclitic; its e-caduc deletes readily (je ne sais → `[ʒən sɛ]`), and in casual/colloquial spoken French "ne" is frequently **dropped** entirely ("je sais pas" `[ʒ(ə) sɛ pa]`, "j'sais pas" `[ʃe pa]`). Retained in careful/formal speech and writing.

- **Example:** je ne comprends pas `[ʒə.n(ə) kɔ̃.pʁɑ̃ pa]` → colloquial `[ʒ(ə) kɔ̃.pʁɑ̃ pa]`

#### Clitic Chain Example

**Phrase:** je ne te le redonnerai pas

- **Careful:** `[ʒə nə tə lə ʁə.dɔn.ʁe pa]`
- **Casual:** `[ʒ nə t lə ʁ.dɔn.ʁe pa]` ~ `[ʃ tə l ʁ.dɔn.ʁe pa]` (with "ne"-drop: `[ʒ tə l ʁ.dɔn.ʁe pa]`)

This illustrates simultaneous e-caduc alternation, ne-drop, and `/ʒ/` devoicing — the French functional equivalent of an English weak-form cascade.

### Quebec-Specific Processes

| Process | Description | IPA example |
|---|---|---|
| Affrication of /t d/ in liaison and clitics | When a liaison or enchaînement `/t/` or `/d/` lands before a high front vowel/glide `/i y j ɥ/`, Quebec affricates it: `[t͡s d͡z]`. This interacts with clitic e-caduc deletion. | "tout y est" `[tu.t͡s‿i e]`; "quand il" `[kɑ̃.d͡z‿il]` — the liaison `/d/` precedes high front `[i]`, so it affricates; Metropolitan `[tu.t‿i e]`, `[kɑ̃.t‿il]`. (Note: "grand individu" does NOT affricate, since the liaison `/t/` there precedes the nasal `[ɛ̃]`, which is not a high front vowel/glide: Quebec and Metropolitan alike `[ɡʁɑ̃.t‿ɛ̃.di.vi.dy]`.) |
| High-vowel laxing feeding e-caduc/cluster contexts | Quebec `/i y u/` lax to `[ɪ ʏ ʊ]` in closed final syllables; after e-caduc deletion creates a newly closed syllable, the high vowel may lax. | "petite" `[pt͡sɪt]` (laxed `[ɪ]`, affricated `[t͡s]`) vs Metropolitan `[pə.tit]`. |
| Retention of contrasts that affect boundary vowels | Quebec keeps `/a/`~`/ɑ/` and `/ɛ̃/`~`/œ̃/` distinct, so de-nasalising/nasal liaison outcomes and the quality of boundary vowels differ from merged Metropolitan French (e.g. "un" = `[œ̃]` in Quebec, `[ɛ̃]` for most Metropolitan speakers). | "un ami" Quebec `[œ̃.n‿a.mi]` with distinct `[œ̃]`; Metropolitan typically `[œ̃.n‿a.mi]`~`[ɛ̃.n‿a.mi]` (merged). |

### How the Processes Interact

The four processes feed one another in a left-to-right cascade across the rhythmic group. Ordering generally:

1. **E-caduc deletion** is computed (three-consonant law, alternation), which may strand consonants;
2. **Élision** deletes final vowels before vowels (obligatory, lexical);
3. **Liaison** surfaces latent final consonants before the resulting vowel onsets;
4. **Enchaînement** re-syllabifies ALL pronounced final consonants (latent-now-surfaced or always-present) as onsets of the following syllable.

**Example cascade:** "je ne les ai pas entendus" → ne-drop/e-caduc `[ʒ le.z‿e pa.z‿ɑ̃.tɑ̃.dy]` with liaison `[z]` on "les" and "pas", enchaîné onsets throughout, yielding fully open syllables `[ʒ.le.ze.pa.zɑ̃.tɑ̃.dy]`.

**Rate and register:** Obligatory liaison and obligatory élision are categorical and present at every speech rate and register. Optional liaison, e-caduc retention, and "ne"-drop are gradient: optional liaisons and e-caduc retention **increase** with formality, careful reading, oratory, classical theatre and song (where e-caduc may even be fully syllabic for the metre); they **decrease** in fast casual conversation, where "ne"-drop and maximal e-caduc deletion dominate. Dictionary citation forms list the isolated word with its silent final consonant; the IPA of running French requires the liaison/élision/enchaînement/e-caduc computations above to sound native.

**Cross-reference:** This section is the French counterpart of the English guide's "Weak Forms & Connected Speech". Where English documents GA vs RP and its central divergence is rhoticity (linking-r, intrusive-r, flapping vs glottalling, schwa weak forms), French documents Standard Metropolitan vs Quebec and its central divergences are (a) Quebec affrication of `/t d/` before `/i y j ɥ/`, (b) Quebec high-vowel laxing and long-vowel diphthongisation, and (c) Quebec retention of the `/a/`~`/ɑ/` and `/ɛ̃/`~`/œ̃/` contrasts that Metropolitan French has largely merged. The mechanism that English handles via vowel reduction to schwa, French handles via e-caduc **deletion** and the liaison/élision/enchaînement sandhi system.

## Standard Metropolitan vs. Quebec French

Systematic pronunciation differences between the two reference accents of Modern French, expressed in IPA. The two traditions documented in parallel are **Standard Metropolitan French** (*français standard*, the European/Parisian-based prestige norm) and **Quebec French** (*français québécois*, the principal standardized variety of Canadian French). Neither accent is intrinsically more correct; they represent two coexisting standardized systems that diverged after the 17th-century settlement of New France, with Quebec conserving a number of older distinctions that Metropolitan French has since merged. French has no lexical stress, so no stress marks are placed on individual words; prominence falls only on the final full syllable of a rhythmic group. Phonemic transcriptions use `/slashes/` and phonetic detail uses `[brackets]`.

### The Two Reference Accents

- **Standard Metropolitan French** (*français standard*) — Parisian-based European norm. Uvular `/ʁ/`, no length contrast and no diphthongization of long vowels, the `/a/`~`/ɑ/` contrast largely lost (merged toward front `/a/`), and the nasal `/ɛ̃/`~`/œ̃/` contrast merged (both pronounced `[ɛ̃]` for most speakers).
- **Quebec French** (*français québécois*) — principal Canadian norm. Affrication of `/t d/` to `[t͡s d͡z]` before high front vocoids, lax high vowels `[ɪ ʏ ʊ]` in closed syllables, diphthongization of long vowels, conservation of the `/a/`~`/ɑ/` contrast and of the nasal `/ɛ̃/`~`/œ̃/` contrast, plus distinctive nasal-vowel qualities. Older apical `/r/` has largely given way to uvular `/ʁ/`.

### Table of Differences

| Feature | Metropolitan IPA | Quebec IPA | Examples | Explanation |
| --- | --- | --- | --- | --- |
| **Affrication of `/t d/` before high front vocoids** | `[t]` and `[d]` remain plain stops in all environments | `[t͡s]` and `[d͡z]` (alveolar affricates) before `/i y/` and the glides `/j ɥ/` | *tu*: Metropolitan `/ty/` — Quebec `[t͡sy]`; *dire*: Metropolitan `/diʁ/` — Quebec `[d͡ziːʁ]`; *petit*: Metropolitan `/pə.ti/` — Quebec `[pt͡si]`; *moitié*: Metropolitan `/mwa.tje/` — Quebec `[mwat͡sje]` | The single most recognizable marker of Quebec French. The coronal stops `/t/` and `/d/` are systematically affricated to `[t͡s]` and `[d͡z]` when immediately followed by one of the high front vocoids `/i y j ɥ/` (but not before `/e ɛ a o u/` etc.). This is an automatic allophonic process, not lexical: *type* is `[t͡sɪp]`, *tante* is plain `[tãːt]`. Metropolitan French has no such affrication and keeps clean stops everywhere. |
| **Laxing of high vowels `/i y u/` in closed syllables** | tense `[i y u]` in all syllable types | lax `[ɪ ʏ ʊ]` in syllables closed by a non-lengthening consonant | *vite*: Metropolitan `/vit/` — Quebec `[vɪt]`; *lune*: Metropolitan `/lyn/` — Quebec `[lʏn]`; *route*: Metropolitan `/ʁut/` — Quebec `[ʁʊt]`; *minute*: Metropolitan `/mi.nyt/` — Quebec `[mɪnʏt]` | In Quebec French the high vowels `/i y u/` become lax `[ɪ ʏ ʊ]` when they stand in a syllable closed by a consonant (except before the lengthening consonants `/ʁ v z ʒ/`, which keep the vowel tense and long). Laxing can also spread to other high vowels in the word by harmony. Metropolitan French never laxes these vowels, so *vite* keeps a fully tense `[i]`. This laxing, combined with affrication, gives Quebec words like *petite* `[pt͡sɪt]` their characteristic sound. |
| **Diphthongization of long vowels** | long vowels realized as steady (monophthongal), length itself largely lost | phonologically long vowels diphthongize in stressed closed syllables | *fête*: Metropolitan `/fɛt/` — Quebec `[faɪ̯t]`; *pâte*: Metropolitan `/pat/` — Quebec `[pɑʊ̯t]`; *neige*: Metropolitan `/nɛʒ/` — Quebec `[naɪ̯ʒ]`; *tard*: Metropolitan `/taʁ/` — Quebec `[tɑʊ̯ʁ]`; *fleur*: Metropolitan `/flœʁ/` — Quebec `[flœːʁ]` ~ `[flaœ̯ʁ]` | Quebec French preserves a phonemic vowel-length contrast (from old circumflex vowels, the `/ɛː/` of *fête*, and vowels before lengthening consonants) and breaks these long vowels into diphthongs when they are stressed and in a closed syllable: `/ɛː/` → `[aɪ̯]`, `/ɑ/` → `[ɑʊ̯]`, `/œ/` → `[aœ̯]`, `/oː/` → `[oʊ̯]`, etc. Metropolitan French has largely eliminated distinctive length altogether, so *fête* and *faite* are homophonous `[fɛt]` there, while in Quebec *fête* `[faɪ̯t]` stays audibly distinct from *faite* `[fɛt]`. |
| **The `/a/` ~ `/ɑ/` contrast** | largely merged — most speakers use a single front `/a/` | contrast retained — front `/a/` vs back `/ɑ/` (often long, `[ɑː]` ~ diphthongized `[ɑʊ̯]`) | *patte*: Metropolitan `/pat/` — Quebec `[pat]`; *pâte*: Metropolitan `/pat/` (merged) — Quebec `[pɑʊ̯t]`; *tache vs tâche*: Metropolitan `/taʃ/` = `/taʃ/` — Quebec `[taʃ]` vs `[tɑʊ̯ʃ]`; *là vs las*: Metropolitan `/la/` ≈ `/la/` — Quebec `[la]` vs `[lɑ]` | Classical French distinguished a front *a antérieur* `/a/` (*patte*) from a back *a postérieur* `/ɑ/` (*pâte*), historically associated with the circumflex. Metropolitan French has collapsed this opposition for the great majority of speakers, leaving a single front `/a/` so that *patte* and *pâte* are homophones. Quebec French robustly keeps the two apart: back `/ɑ/` is long and often diphthongizes to `[ɑʊ̯]`, making *pâte* `[pɑʊ̯t]` clearly different from *patte* `[pat]`. |
| **Nasal `/ɛ̃/` ~ `/œ̃/` merger (brin–brun)** | merged — both realized `[ɛ̃]` for most speakers | kept distinct — `/ɛ̃/` vs rounded `/œ̃/` | *brin*: Metropolitan `/bʁɛ̃/` — Quebec `/bʁɛ̃/`; *brun*: Metropolitan `/bʁɛ̃/` (merged) — Quebec `/bʁœ̃/`; *un*: Metropolitan `/ɛ̃/` — Quebec `/œ̃/`; *parfum*: Metropolitan `/paʁ.fɛ̃/` — Quebec `/paʁ.fœ̃/` | Standard Metropolitan French (especially Parisian) has merged the rounded front nasal `/œ̃/` into the unrounded `/ɛ̃/`, so *brin* and *brun*, *empreinte* and *emprunte* sound the same and the four-way nasal system has reduced to three (`/ɛ̃ ɑ̃ ɔ̃/`). Quebec French maintains the older four-way system with a distinct rounded `/œ̃/` in *un, brun, parfum, lundi*, keeping *brin* `/bʁɛ̃/` and *brun* `/bʁœ̃/` as a minimal pair. |
| **Quality and backing of the nasal vowels** | `/ɛ̃/` relatively open and slightly raised/backed `[æ̃~ɛ̃]`; `/ɑ̃/` back `[ɑ̃]`; `/ɔ̃/` close-mid rounded `[õ~ɔ̃]` | `/ɛ̃/` raised and fronted toward `[ẽ~ĩ]`; `/ɑ̃/` fronted/raised toward `[ã~aɪ̃]`; `/ɔ̃/` raised and tightly rounded `[õʊ̃]` | *vin*: Metropolitan `[vɛ̃]` — Quebec `[vẽ]` ~ `[vɪ̃]`; *blanc*: Metropolitan `[blɑ̃]` — Quebec `[blã]` ~ `[blaɪ̃]`; *bon*: Metropolitan `[bɔ̃]` — Quebec `[bõʊ̃]`; *maison*: Metropolitan `[mɛ.zɔ̃]` — Quebec `[mɛzõʊ̃]` | Beyond the merger difference, the nasal vowels carry distinct timbres in the two norms. Metropolitan (Parisian) French has in recent decades lowered `/ɛ̃/` toward `[æ̃]` and shifted `/ɑ̃/` and `/ɔ̃/` in a "rotation". Quebec French instead tends to raise and front `/ɛ̃/` (often near `[ẽ]` or even `[ĩ]`), to front and sometimes diphthongize `/ɑ̃/`, and to raise `/ɔ̃/` to a tightly rounded, diphthongal `[õʊ̃]`. These timbre differences are a major perceptual cue separating the two accents even on the shared nasal phonemes. |
| **Realization of `/ʁ/` (the French R)** | `[ʁ]` voiced uvular fricative (devoiced `[χ]` next to voiceless consonants) | `[ʁ]` uvular today; traditionally apical `[r]` (alveolar trill/tap) in older and rural speech | *rouge*: Metropolitan `[ʁuʒ]` — Quebec `[ʁʊʒ]` (older `[ruʒ]`); *Paris*: Metropolitan `/pa.ʁi/` — Quebec `[paʁi]` (older `[pari]`); *porte*: Metropolitan `/pɔʁt/` — Quebec `[pɔʁt]` (older `[pɔrt]`); *frère*: Metropolitan `/fʁɛʁ/` — Quebec `[fʁaɪ̯ʁ]` | Metropolitan French has a stable uvular `/ʁ/`, a voiced uvular fricative that devoices to `[χ]` adjacent to voiceless sounds (*quatre* `[katχ]`). Quebec French historically had two competing variants: an apical (alveolar) trill/tap `[r]`, traditionally associated with Montreal and the east, and a uvular `[ʁ]` associated with Quebec City and the west. Over the twentieth century the uvular `[ʁ]` has won out and is now the dominant and prestige realization across Quebec, with apical `[r]` surviving mainly in older and rural speakers. |
| **Rhythm and intonation** | syllable-timed; rising-falling group-final melody; final-syllable lengthening at phrase boundaries | syllable-timed with wider pitch range and more frequent pre-final rises; distinctive sentence-final fall, often perceived as more "sing-song" | *rhythmic group*: both stress only the last full syllable of the rhythmic group (no word-level stress); *question intonation*: Metropolitan high terminal rise — Quebec frequent rise-fall on the final group; *interrogative "-tu"*: Quebec colloquial "Tu viens-tu?" adds a marked intonational/morphological pattern absent in Metropolitan | Both accents are syllable-timed (syllables of roughly equal length) and place prominence only on the last full syllable of each rhythmic group, never on individual words — French has no contrastive lexical stress. They differ in melody: Quebec French typically uses a wider pitch range, more frequent rises within the utterance, and a characteristic terminal contour often described as more melodic or *chantant*, whereas Metropolitan French has a comparatively narrower, more even intonational pattern. These prosodic differences let listeners identify the accent before any single segment is decisive. |
| **Treatment of the schwa `/ə/` (e caduc)** | frequently dropped, especially in fast speech and word-finally; Parisian deletes it readily | frequently dropped and may trigger affrication/consonant clusters; word-final `/ə/` never pronounced | *petit*: Metropolitan `[pti]` — Quebec `[pt͡si]`; *samedi*: Metropolitan `[sam.di]` — Quebec `[samd͡zi]`; *je le*: Metropolitan `[ʒlə]` ~ `[ʒœl]` — Quebec `[ʒø]`/`[ʃ]` (e.g. "je suis" → `[ʃɥi]` ~ `[ʃy]`); *fenêtre*: Metropolitan `[fnɛtʁ]` — Quebec `[fnaɪ̯tʁ]` | Both norms delete the *e caduc* `/ə/` in many contexts, producing dense consonant clusters; in Quebec this deletion feeds the affrication rule, so dropping the schwa in *petit* yields `[pt͡si]`. Neither accent pronounces a final orthographic *e* as a vowel in normal speech (unlike conservative Southern/Meridional French). Quebec colloquial speech goes further with reductions such as "je suis" → `[ʃɥi]` or `[ʃy]`. The realization of retained schwa also differs in timbre, Metropolitan schwa being close to `[œ]`/`[ø]`. |
| **Southern / Meridional French (note)** | *(reference)* Parisian norm: schwa deleted, three nasal vowels `[ɛ̃ ɑ̃ ɔ̃]` | *(for contrast)* Quebec: four nasal vowels, length and diphthongs | *rose*: Standard `/ʁoz/` — Meridional `[ˈʁɔ.zə]` (final schwa pronounced); *pain*: Standard `[pɛ̃]` — Meridional `[pɛŋ]` (nasal vowel + velar nasal appendage); *vin*: Standard `[vɛ̃]` — Meridional `[vɛŋ]` | Beyond the two primary reference accents, Southern (Meridional/Occitan-substrate) French of southern France is worth a side note: it tends to pronounce the *e caduc* `/ə/` even word-finally ("une petite rose" with audible final `[ə]`), giving a more even syllable count, and it weakens the nasal-vowel system — nasal vowels are often realized as an oral vowel plus a nasal consonant appendage `[ɛŋ]`, reducing the distinctions that Parisian French maintains. This variety is descriptive context only; the parallel documented throughout this guide remains Standard Metropolitan vs Quebec French. |

### Summary

Standard Metropolitan and Quebec French diverge most audibly in:

1. **Quebec's allophonic processes** — affrication of `/t d/` to `[t͡s d͡z]` before `/i y j ɥ/`, laxing of `/i y u/` to `[ɪ ʏ ʊ]` in closed syllables, and diphthongization of long vowels (*fête* `[faɪ̯t]`, *pâte* `[pɑʊ̯t]`).
2. **Two phonemic contrasts that Quebec conserves but Metropolitan French has merged** — front `/a/` vs back `/ɑ/` (*patte* vs *pâte*) and the nasal `/ɛ̃/` vs `/œ̃/` (*brin* vs *brun*).
3. **Differing nasal-vowel timbres** and the now-completed shift from apical `[r]` to uvular `[ʁ]` in Quebec.
4. **Prosody** — Quebec French carrying a wider, more melodic intonation.

Southern/Meridional French, with its pronounced final schwa and weakened nasal-vowel system, stands as a further contrast outside the two main reference accents.

## Orthography: Grapheme–Phoneme Correspondences

French orthography is etymologically deep and conservative, but — unlike English — it is far more regular in the READING direction (spelling -> sound) than in the writing direction (sound -> spelling). A reader who knows the rules can pronounce almost any written word; a listener cannot reliably spell what they hear, because a single phoneme has many spellings (e.g. `/o/` <- o, ô, au, eau, aud, aut, aux; `/ɛ̃/` <- in, im, ain, ein, yn, eim, aim) and many letters are silent. The spelling fossilises Latin and Old French: most word-final consonants, once pronounced, fell silent between the 11th and 17th centuries but were kept on the page (and resurface in LIAISON before a vowel); a vast number of etymological letters were re-inserted by Renaissance scholars to show Latin roots (the 'p' of 'temps' < tempus, the 's' of 'forêt' marked by a circumflex < forest). Three further systematic traits dominate: (1) a contrast between an oral vowel and a NASAL vowel is signalled purely by a following m/n that is itself not pronounced as a consonant (bon `/bɔ̃/` vs bonne `/bɔn/`, vin `/vɛ̃/` vs vine `/vin/`); (2) DIACRITICS are phonemic, not decorative — the acute, grave and circumflex on 'e' distinguish `/e/`, `/ɛ/` and the cedilla forces soft 'c'; (3) the inherited Romance soft/hard alternation of c and g before front vs back vowels, repaired by silent 'e', 'u' and the cedilla. Two reference accents share this single orthography: STANDARD METROPOLITAN (European / Parisian-based) French and QUEBEC (Canadian) French. Differences read off the same spelling are noted throughout: chiefly Quebec affrication of `/t d/` to `[t͡s d͡z]` before `/i y j ɥ/`, Quebec lax high vowels `[ɪ ʏ ʊ]` in closed syllables, Quebec long-vowel diphthongisation, and the maintenance in Quebec of the `/a/`~`/ɑ/` and `/ɛ̃/`~`/œ̃/` contrasts that are largely merged in Metropolitan French. French stress is not lexical: it falls automatically on the last full syllable of a rhythmic group, so no stress is marked on individual graphemes below.

**Reference accents:**

| Label | Accent |
|---|---|
| STD | Standard Metropolitan French (français standard, European / Parisian-based) |
| QC | Quebec French (français québécois, Canadian) |

(`∅` denotes a silent/null realisation.)

### General Principles

Six organising principles govern how letters map to sounds in French.

- **Regular in the reading direction:** Grapheme-to-phoneme mapping is largely rule-governed and predictable; the irregularity of the system lies almost entirely in the reverse (sound-to-spelling) direction.
  - eau -> always `/o/` (eau, beau, château)
  - oi -> always `/wa/` (roi, moi, foie)
  - qu -> almost always `/k/` (qui, quand, banque)
  - gn -> `/ɲ/` (montagne, agneau)
- **Many-to-one spelling:** A single phoneme is spelled by many distinct graphemes, the chief source of French spelling difficulty.
  - `/o/` <- o (mot), ô (côte), au (sauter), eau (eau), -aud (chaud), -aut (saut), -aux (chevaux)
  - `/ɛ̃/` <- in (vin), im (timbre), ain (pain), ein (plein), yn (syndicat), eim (Reims), aim (faim)
  - `/s/` <- s (sac), ss (tasse), c (ciel), ç (ça), sc (scène), t (nation), x (six)
  - `/k/` <- c (car), qu (que), k (kilo), ch (chœur), q (coq), cqu (acquérir)
- **Silent final letters:** Most word-final consonants and the final 'e' are silent in isolation; the consonants resurface in liaison before a following vowel. This makes the written word longer than the spoken word.
  - petit `/pə.ti/` but petit ami `/pə.ti.t‿a.mi/` (t resurfaces)
  - les `/le/` but les amis `/le.z‿a.mi/` (s -> `/z/` in liaison)
  - grand `/ɡʁɑ̃/`, final d silent
  - table `/tabl/`, final e silent
- **Nasalisation by a silent nasal:** A vowel + m/n in the same syllable (i.e. not followed by a vowel or by a second m/n) becomes a nasal vowel, and the m/n is NOT pronounced as a consonant. Adding a vowel or doubling the nasal restores an oral vowel + oral nasal consonant.
  - bon `/bɔ̃/` vs bonne `/bɔn/`
  - vin `/vɛ̃/` vs vinaigre `/vi.nɛɡʁ/`
  - an `/ɑ̃/` vs année `/a.ne/`
  - un `/œ̃/` (STD often `/ɛ̃/`) vs une `/yn/`
- **Diacritics are phonemic:** Accents and the cedilla are not optional ornaments: they can change the phoneme, distinguish homographs, or force a consonant value. Their omission is a spelling error and can mislead pronunciation.
  - e `/ə/` vs é `/e/` vs è/ê `/ɛ/` (de, dé, dès, fête)
  - ç `/s/` vs c `/k/` before a/o/u (ça vs ca-, garçon vs garcon\*)
  - a (preposition à) vs a (verb a); ou `/u/` vs où `/u/` (lexical disambiguation only)
  - circumflex marks a lost 's': forêt < forest, hôpital < hospital
- **Positional soft/hard conditioning:** Inherited from Latin: c and g are 'soft' (sibilant/affricate) before the front letters e, i, y and 'hard' (plosive) before a, o, u and consonants; silent e, u and the cedilla are inserted to override the default.
  - c: cat-type car `/kaʁ/` vs soft ciel `/sjɛl/`; ç forces `/s/` before a/o/u (garçon)
  - g: hard gare `/ɡaʁ/` vs soft gel `/ʒɛl/`; gu keeps `/ɡ/` before e/i (guerre), ge keeps `/ʒ/` before a/o (mangeons)
  - Quebec note: this conditioning is identical in both accents; only the later `/t d/` affrication before `/i y/` differs.

### Vowel Graphemes

French vowel letters and digraphs map onto a 12-vowel oral inventory (`/i e ɛ a ɑ ɔ o u y ø œ ə/`) plus glides and nasal vowels. Vowel quality is largely conditioned by SYLLABLE STRUCTURE: the mid vowels obey the 'loi de position' — close `/e ø o/` tend to appear in open syllables, open `/ɛ œ ɔ/` in closed syllables — though spelling and diacritics override this. There is no English-style 'long/short' or 'magic-e' system; instead, diacritics and digraphs do the work. STD vs QUEBEC differences are pervasive in the vowels: Quebec keeps a back `/ɑ/` distinct from front `/a/` (largely merged to `/a/` in STD), laxes `/i y u/` to `[ɪ ʏ ʊ]` in closed syllables (vite `[vɪt]`), and diphthongises long vowels (père `[paɛ̯ʁ]`, pâte `[pɑʊ̯t]`).

#### Single Vowel Letters

| Grapheme | IPA | Examples | Note |
|---|---|---|---|
| a | `/a/`, `/ɑ/` | chat /a/; patte /a/; pâte /ɑ/ (STD often /a/); âge /ɑ/ | Default front `/a/`. A back `/ɑ/` exists historically (pâte, âme, classe, pas) but in STANDARD METROPOLITAN it is largely MERGED into `/a/`. QUEBEC keeps the `/a/`~`/ɑ/` contrast robustly and backs/rounds final `/ɑ/` toward `[ɑ ~ ɔ]` (pâte `[pɑʊ̯t]`, Canada `[kanadɑ]`). |
| e (unaccented) | `/ə/`, `/e/`, `/ɛ/`, `∅` | le /lə/; pied /e/ (open syll.); mer /ɛ/ (closed syll.); table /∅/ (final) | The most context-dependent grapheme. `/ə/` (e caduc) in open monosyllables and unstable interior syllables (le, petit `/pə.ti/`); `/e/` before a silent final consonant in -er/-ez (parler, nez); `/ɛ/` in a closed syllable (mer, sept, elle, sec) and before a doubled consonant; SILENT word-finally (table, porte) and in many interior positions (samedi `/sam.di/`). The e caduc is more readily dropped in STD than in QUEBEC and southern French. |
| é (accent aigu) | `/e/` | été; café; école; parlé | Close-mid front `/e/`, fixed by the accent regardless of syllable. QUEBEC may lax/lower it slightly in some closed contexts but the grapheme reliably signals `/e/`. The -é(e)(s) endings of past participles are all `/e/`. |
| è (accent grave) | `/ɛ/` | père; mère; très; élève | Open-mid front `/ɛ/`. Distinguishes `/ɛ/` from `/e/` (é) and from `/ə/` (e). QUEBEC lengthens and diphthongises it in closed final syllables (père `[paɛ̯ʁ]`, fête `[faɛ̯t]`). |
| ê (accent circonflexe) | `/ɛ/`, `/ɛː/` | tête; fenêtre; rêve; être | Open-mid `/ɛ/`, historically long `/ɛː/` (often from a lost s: forêt < forest, fête < feste). The length contrast `/ɛ/`~`/ɛː/` is lost in most STD but QUEBEC keeps it long and diphthongises (tête `[taɛ̯t]`). |
| i / î / ï | `/i/`, `/j/` | lit /i/; île /i/; midi /i/; lion /j/ (before vowel); maïs /a.is/ (tréma splits) | Close front `/i/`, very regular; the circumflex (î, gîte) marks etymology only. Before another vowel, i often becomes the glide `/j/` (lion, hier). The tréma (ï) forces a separate syllable (maïs, naïf). QUEBEC laxes `/i/` to `[ɪ]` in closed syllables (vite `[vɪt]`; lit unaffected if final-open). |
| o / ô | `/ɔ/`, `/o/` | robe /ɔ/; porte /ɔ/; mot /o/ (open/final); rose /o/ (before /z/); côte /o/ (circumflex) | Open `/ɔ/` in closed syllables; close `/o/` in open/final syllables, before `/z/`, and when written ô (côte, hôtel). The 'loi de position' governs the unaccented letter. QUEBEC backs and may diphthongise long `/oː/` (rose `[ʁoʊ̯z]`). |
| u / û | `/y/`, `/ɥ/` | tu /y/; mur /y/; sûr /y/; lui /lɥi/ (before vowel); nuit /nɥi/ | Close FRONT ROUNDED `/y/` — the characteristic French vowel, NOT English `/uː/`. Before another vowel it becomes the rare labio-palatal glide `/ɥ/` (lui, huit, nuage). The circumflex (û, dû, mûr) is etymological/disambiguating. QUEBEC laxes `/y/` to `[ʏ]` in closed syllables (lune `[lʏn]`) and affricates a preceding `/t d/` (tu `[t͡sy]`). |
| y | `/i/`, `/j/` | stylo /i/; cycle /i/; yeux /j/ (initial); pays /pe.i/; moyen /mwa.jɛ̃/ (y = i+i) | Vowel `/i/` in most positions (système, lycée); consonant glide `/j/` word-initially (yaourt, yoga). Between two vowels y often counts as two i's, triggering `/j/` + a vowel split (payer `/pe.je/`, moyen). |

#### Diacritic Summary (vowel interaction)

How the five French diacritics interact with vowel letters to fix or change the phoneme; expanded in the Diacritics tables below.

| Diacritic | Effect | Examples |
|---|---|---|
| accent aigu (é) | fixes `/e/` on the letter e | été; café |
| accent grave (è, à, ù) | fixes `/ɛ/` on e; on a/u it is purely homograph-disambiguating (à vs a, où vs ou), no sound change | très; à; où |
| accent circonflexe (â ê î ô û) | marks etymology (often a lost s) and historical length; phonemically: ê = `/ɛ(ː)/`, ô = `/o/`, â = `/ɑ/` (where the contrast survives) | forêt; côte; pâte |
| tréma (ë ï ü) | forces the marked vowel into a separate syllable (breaks a digraph) | Noël `/nɔ.ɛl/`; maïs `/ma.is/`; aiguë |
| cédille (ç) | forces soft `/s/` on c before a, o, u (consonant, not a vowel diacritic) | ça; garçon |

#### Vowel Digraphs

| Grapheme | IPA | Examples | Note |
|---|---|---|---|
| ai / aî | `/ɛ/`, `/e/` | maison /ɛ/; lait /ɛ/; maître /ɛ/; j'ai /e/; gai /e/ | Usually open `/ɛ/`; close `/e/` in a few open finals (j'ai, gai, quai variable) and the future/passé-simple endings -ai. QUEBEC keeps it open and long, diphthongising (maître `[maɛ̯tʁ]`). |
| ei / eî | `/ɛ/` | neige; reine; seize; beige | Open-mid `/ɛ/`, parallel to ai; very regular. |
| eu / œu | `/ø/`, `/œ/` | feu /ø/; peu /ø/; peur /œ/; sœur /œ/; œuf /œf/; œufs /ø/ (plural) | Front ROUNDED mid vowels. Close `/ø/` in open/final syllables and before `/z/` (heureuse); open `/œ/` in closed syllables (peur, jeune, neuf). œu is a ligature spelling of the same vowels (cœur `/kœʁ/`, vœu `/vø/`). Distinct from `/ə/`, with which `/œ/` partly overlaps phonetically. |
| au / aud / aut / aux | `/o/`, `/ɔ/` | auto /o/; chaud /o/; saut /o/; chevaux /o/; Paul /ɔl/ (before l) | Almost always close `/o/`; the trailing d/t/x are silent. Open `/ɔ/` only before a pronounced `/ʁ/` or in 'Paul', 'restaurant' (variable). QUEBEC may diphthongise long `/oː/`. |
| eau | `/o/` | eau; beau; château; bateau; oiseau | Invariably close `/o/`; one of the most regular French digraphs (etymologically e+a+u collapsed). The plural -eaux is also `/o/`. |
| ou / oû | `/u/`, `/w/` | vous /u/; rouge /u/; août /u/; oui /wi/ (before vowel); ouest /wɛst/ | Close BACK rounded `/u/` (the English-style 'oo'), as opposed to front `/y/` for plain u. Before another vowel it becomes the glide `/w/` (oui, ouest, jouer `/ʒwe/`). QUEBEC laxes `/u/` to `[ʊ]` in closed syllables (route `[ʁʊt]`). |
| oi / oî | `/wa/`, `/wɑ/` | roi /ʁwa/; moi; foie; boîte; trois | Glide + vowel `/wa/`, completely regular (historically `/we/` then `/wa/`). QUEBEC often has back `/wɑ/` and a more open/diphthongised realisation (moi `[mwɔ]`, trois `[tʁwɑ]`); colloquially even `[we]` in some words (moé, toé for moi/toi). |
| ui | `/ɥi/` | lui; nuit; huit; fruit; puis | The labio-palatal glide `/ɥ/` + `/i/`, a cross-linguistically rare sequence. In QUEBEC a preceding `/t d/` is affricated by the `/ɥ/` glide (tuile `[t͡sɥɪl]`, duel `[d͡zɥɛl]`); there is no affrication in nuit `[nɥi]` or lui `[lɥi]`, which lack a preceding `/t,d/`. |
| ay / ey / oy / uy (+ vowel) | `/ɛj/`, `/waj/`, `/ɥij/` | pays /pe.i/; essayer /e.se.je/; voyage /vwa.jaʒ/; appuyer /a.pɥi.je/ | Intervocalic y behaves as i+i: it closes the first syllable as a vowel and opens the next with `/j/`. Hence oy = `/wa/`+`/j/` (voyage), uy = `/ɥi/`+`/j/` (appuyer), ay = `/ɛ/`+`/j/` or `/e/`+`/j/` (essayer). |

#### Nasal Vowel Spellings

The defining feature of French vowel orthography: a vowel letter followed by m or n that is NOT itself followed by a vowel or a second m/n produces a NASAL VOWEL, and the m/n is silent (it merely marks nasalisation). m is used before p/b, n elsewhere. There are four nasal phonemes `/ɛ̃ ɑ̃ ɔ̃ œ̃/`; STANDARD METROPOLITAN has largely MERGED `/œ̃/` into `/ɛ̃/` (brin = brun for many speakers), whereas QUEBEC keeps `/ɛ̃/` and `/œ̃/` distinct and realises `/ɛ̃/` as a lower/backer `[ẽ ~ ãɪ̯̃]`. Doubling the nasal (nn, mm) or adding a vowel restores an oral vowel + oral `/n,m/`.

| Phoneme | Spellings | Examples | Note |
|---|---|---|---|
| `/ɑ̃/` | an, am, en, em, aon, aen | an `/ɑ̃/`; chambre `/ʃɑ̃bʁ/` (am); enfant `/ɑ̃.fɑ̃/` (en); temps `/tɑ̃/` (em); paon `/pɑ̃/` (aon); Caen `/kɑ̃/` (aen) | Low back nasal. 'en/em' = `/ɑ̃/` in most words (enfant, ensemble) but = `/ɛ̃/` in -ien, examen, bien (see `/ɛ̃/`). |
| `/ɛ̃/` | in, im, ain, aim, ein, eim, yn, ym, (i)en, (é)en | vin `/vɛ̃/` (in); timbre `/tɛ̃bʁ/` (im); pain `/pɛ̃/` (ain); faim `/fɛ̃/` (aim); plein `/plɛ̃/` (ein); syndicat `/sɛ̃.di.ka/` (yn); bien `/bjɛ̃/` (ien); examen `/ɛɡ.za.mɛ̃/` | Open front nasal — the spelling with the most variants. -ien, -éen and 'examen' give `/jɛ̃/` or `/ɛ̃/`, not `/ɑ̃/`. QUEBEC realises `/ɛ̃/` lower/diphthongised `[ãɪ̯̃]`; STD often centralises it toward `[æ̃]`. |
| `/ɔ̃/` | on, om | bon `/bɔ̃/` (on); non `/nɔ̃/`; nom `/nɔ̃/` (om); ombre `/ɔ̃bʁ/`; compter `/kɔ̃.te/` | Mid back rounded nasal, the most stable nasal spelling. om before p/b (ombre, tomber), on elsewhere. |
| `/œ̃/` | un, um | un `/œ̃/` (STD often `/ɛ̃/`); brun `/bʁœ̃/`; parfum `/paʁ.fœ̃/` (um); lundi `/lœ̃.di/` | Open front ROUNDED nasal. STANDARD METROPOLITAN largely MERGES it into `/ɛ̃/` (un = hein, brun = brin). QUEBEC and conservative/southern STD keep it DISTINCT as `/œ̃/`. Note: final 'um' in Latin loans = `/ɔm/` (album `/al.bɔm/`, forum), not nasal. |

**Denasalisation:** Nasalisation is BLOCKED when the m/n is doubled or followed by a vowel: an `/ɑ̃/` vs Anne `/an/` vs année `/a.ne/`; bon `/bɔ̃/` vs bonne `/bɔn/`; vin `/vɛ̃/` vs vinaigre `/vi.nɛɡʁ/`; brun `/bʁœ̃/` vs brune `/bʁyn/`. The oral vowel then takes its normal value and the `/n,m/` is pronounced.

### Consonant Graphemes

Single consonant letters are highly regular. The system's interest lies in the soft/hard alternation of c and g, the digraphs ch, gn, ph, th, qu, the two values of s and x, the silent h, and doubled consonants (which, unlike English, generally do NOT change the preceding vowel and merely reflect etymology). Quebec affricates `/t/` and `/d/` to `[t͡s]` and `[d͡z]` before the high front vowels `/i y/` and the glides `/j ɥ/`; this is the single most audible consonantal difference from Metropolitan French and is noted on the relevant entries.

#### Single Letters

| Grapheme | IPA | Examples | Note |
|---|---|---|---|
| b | `/b/` | bon; robe | Regular; devoiced/assimilated before a voiceless consonant (absent `[apsɑ̃]`). Silent final in plomb `/plɔ̃/`. |
| c | `/k/`, `/s/` | car /k/; ciel /s/; sac /k/ | Hard `/k/` before a, o, u, consonant and word-finally; soft `/s/` before e, i, y. See soft/hard alternation. Often silent word-finally (tabac `/ta.ba/`, blanc `/blɑ̃/`). |
| ç | `/s/` | ça; garçon; reçu; français | C-cédille: forces soft `/s/` before a, o, u, where plain c would be hard `/k/`. Never used before e, i, y (redundant there). |
| d | `/d/` | deux; ronde | Regular; usually silent word-finally (grand `/ɡʁɑ̃/`, pied `/pje/`) and surfaces as `/t/` in liaison (grand‿homme `/ɡʁɑ̃.t‿ɔm/`). QUEBEC: affricated to `[d͡z]` before `/i, y, j, ɥ/` (dire `[d͡zɪʁ]`, du `[d͡zy]`). |
| f | `/f/` | feu; neuf | Regular; one notable liaison voicing: neuf `/nœf/` -> `/v/` in 'neuf ans', 'neuf heures'. Silent f in 'clef' `/kle/`, 'œufs'/'bœufs' plural. |
| g | `/ɡ/`, `/ʒ/` | gare /ɡ/; gel /ʒ/; garage /ɡ.../ʒ/ | Hard `/ɡ/` before a, o, u and consonant; soft `/ʒ/` before e, i, y. See soft/hard alternation. Usually silent word-finally (long `/lɔ̃/`, sang `/sɑ̃/`). |
| h | `∅` | homme; héros; thé | Always silent as a sound. Two grammatical kinds: H MUET (mute h) allows elision/liaison (l'homme, les‿hommes); H ASPIRÉ blocks them (le héros, les /héros/ no liaison) though it too is voiceless. Part of digraphs ch, ph, th, gh. |
| j | `/ʒ/` | je; jour; jambe | Very regular voiced postalveolar fricative. `/dʒ/` only in recent English loans (jean, jazz, often nativised to `/dʒ/` or `/ʒ/`). |
| k | `/k/` | kilo; ski; képi | Rare; confined to loanwords and learned/Greek vocabulary. Native `/k/` is normally spelled c or qu. |
| l | `/l/`, `/j/`, `∅` | lit /l/; fille /j/ (ill); gentil ∅ | Clear `[l]` in all positions (no English-style dark l). After i, the digraph -ill- usually spells `/j/` (fille, travailler) — but `/l/` in ville, mille, tranquille. Silent in some finals (gentil `/ʒɑ̃.ti/`, fusil, outil). |
| m | `/m/`, (nasalising) | main /m/.../mɛ̃/; femme /fam/ | Oral `/m/` before a vowel or when doubled; otherwise it nasalises the preceding vowel and is itself silent (am/em/im/om/um). See Nasal Vowel Spellings. |
| n | `/n/`, (nasalising) | non /n/.../nɔ̃/; bonne /bɔn/ | Oral `/n/` before a vowel or when doubled; otherwise nasalises the preceding vowel and is silent (an/en/in/on/un). See Nasal Vowel Spellings. |
| p | `/p/`, `∅` | père /p/; trop ∅; sept /sɛt/ (p silent) | Regular `/p/`; silent in many finals (trop, coup, drap) and in the cluster of 'sept', 'compter', 'baptême', 'sculpteur'. |
| q | `/k/` | coq; cinq; qu (queue) | Almost always written qu = `/k/` (the u is silent). Bare q only word-finally (coq, cinq `/sɛ̃k/`). See qu in digraphs. |
| r | `/ʁ/` | rouge; mer; arbre | The French R is a VOICED UVULAR FRICATIVE `[ʁ]`, devoiced to `[χ]` next to voiceless consonants (quatre `[katχ]`). NOT the English alveolar `[ɹ]`. QUEBEC traditionally used an apical/alveolar trill `[r]` or tap, but the uvular `[ʁ]`/`[ʀ]` is now dominant in Montreal and among younger speakers. Often silent in the infinitive ending -er `/e/` (parler `/paʁ.le/`) and in -ier. |
| s | `/s/`, `/z/`, `∅` | sac /s/; rose /z/ (between vowels); les ∅ (final) | `/s/` word-initially and next to consonants; `/z/` between two vowels (maison `/mɛ.zɔ̃/`); silent word-finally but surfaces as `/z/` in liaison (les‿amis). Doubled ss = `/s/` (poisson `/s/` vs poison `/z/`). |
| t | `/t/`, `/s/`, `∅` | table /t/; nation /s/ (tion); petit ∅ (final) | `/t/` default; `/s/` in the suffix -tion and -tie/-tial (nation, partial); usually silent word-finally (petit, chat) and surfaces in liaison. QUEBEC: affricated to `[t͡s]` before `/i, y, j, ɥ/` (petit `[pt͡si]`, tu `[t͡sy]`, tien `[t͡sjɛ̃]`). |
| v | `/v/` | vous; rêve | Very regular voiced labiodental fricative; does not occur word-finally without a silent e. |
| w | `/w/`, `/v/` | wagon /v/ (older) ~ /w/; week-end /w/; kiwi /w/ | Loanword letter only. `/v/` in older Germanic borrowings (wagon, often `/v/`), `/w/` in English borrowings (week-end, whisky). |
| x | `/ks/`, `/ɡz/`, `/s/`, `/z/`, `∅` | taxi /ks/; examen /ɡz/; six /s/ (isolation); dixième /z/; deux ∅ (final) | `/ks/` default; `/ɡz/` in the prefix ex- before a vowel (examen, exact); `/s/` in 'six', 'dix', 'soixante'; `/z/` as the internal value in ordinals (dixième, sixième) and in liaison (deux‿amis, six‿heures); usually silent word-finally (paix, prix). |
| z | `/z/`, `∅` | zéro /z/; gaz /z/; nez ∅ (final) | `/z/` default; usually silent in the verb ending -ez `/e/` (parlez `/paʁ.le/`) and in 'nez', 'riz', surfacing as `/z/` in liaison (allez‿y). |

#### Digraphs

| Grapheme | IPA | Examples | Note |
|---|---|---|---|
| ch | `/ʃ/`, `/k/` | chat /ʃ/; chien /ʃ/; chœur /k/; orchestre /k/ | `/ʃ/` in native/Romance vocabulary (the regular value); `/k/` in Greek-origin learned words (chœur, écho, technique, archéologie, Christ). |
| gn | `/ɲ/` | montagne; agneau; gagner; signe | Palatal nasal `/ɲ/`, the regular value. Exceptionally `/ɡn/` in some learned words (diagnostic, gnose, magnum). |
| ph | `/f/` | photo; téléphone; philosophie | Greek-origin spelling of `/f/`; entirely regular, no `/v/` value (unlike English 'Stephen'). |
| th | `/t/` | thé; théâtre; mathématiques | Greek-origin spelling; always plain `/t/` in French (no dental fricative `/θ/`). The h is silent. |
| qu | `/k/`, `/kw/` | qui /k/; quand /k/; banque /k/; aquarium /kw/; équateur /kw/ | `/k/` by default (the u is silent), the overwhelmingly regular value; `/kw/` only in a few Latin/learned words before a (aquarium, square, quartz). QUEBEC: qu = `[k]` is NOT affricated (only `/t,d/` affricate before `/i,y,j,ɥ/`), so 'qui' = `[ki]`. |
| sc | `/s/`, `/sk/` | science /s/; scène /s/; scolaire /sk/; scandale /sk/ | `/s/` before e, i, y (the second c is soft, hence sci/sce = `/s/`); `/sk/` before a, o, u and consonants. |
| ti (+ vowel) | `/sj/`, `/tj/`, `/ti/` | nation /sjɔ̃/; patient /sjɑ̃/; moitié /tje/; partie /ti/ | In the Latinate suffix -tion/-tial/-tie the t spells `/s/` (nation, initial); elsewhere ti before a vowel stays `/tj/` (moitié, pitié) or `/ti/`. After s, -stion keeps `/tj/` (question `/kɛs.tjɔ̃/`). |
| ill | `/j/`, `/ij/`, `/il/` | fille /fij/; travailler /tʁa.va.je/; famille /fa.mij/; ville /vil/; mille /mil/ | After a vowel, -ill- = `/j/` (travail, abeille); after a consonant, -ill- = `/ij/` (fille, famille); but plain `/il/` in the closed set ville, mille, tranquille, Lille, million (`/mi.ljɔ̃/`). |

#### Doubled Consonants

A doubled consonant letter almost always spells a SINGLE consonant phoneme and, unlike in English, does NOT systematically shorten or change the preceding vowel — it is chiefly an etymological/morphological spelling. Its main phonemic consequence is to BLOCK nasalisation (the first nasal closes the syllable as a vowel marker only if it stands alone; a doubled mm/nn forces an oral vowel + `/m,n/`).

**Rule:** `<CC>` -> single `/C/`

| Word | IPA | Contrast | Note |
|---|---|---|---|
| pomme | `/pɔm/` | (no nasal: mm = oral `/ɔ/` + `/m/`, cf. 'nom' `/nɔ̃/`) | Double mm/nn defeats nasalisation. |
| bonne | `/bɔn/` | bon `/bɔ̃/` | nn -> oral `/ɔ/` + `/n/`; single n nasalises. |
| appeler | `/a.ple/` |  | pp = single `/p/`; vowel quality unaffected. |
| addition | `/a.di.sjɔ̃/` |  | dd = single `/d/`. |

Exceptions, where a doubled letter does more than spell a single consonant:

| Grapheme | IPA | Examples | Note |
|---|---|---|---|
| ss | `/s/` | tasse `/tas/`; poisson `/pwa.sɔ̃/` (vs poison `/pwa.zɔ̃/`) | ss = `/s/` between vowels, where single s would be `/z/`; this is the one doubling that changes the consonant phoneme (s/z), not just blocks gemination. |
| cc | `/k/`, `/ks/` | accord `/a.kɔʁ/` (`/k/`); accent `/ak.sɑ̃/` (`/ks/`); succès `/syk.sɛ/` (`/ks/`) | `/ks/` when the second c is soft (before e, i): the first c = `/k/`, the second = `/s/`. |
| gg | `/ɡ/`, `/ɡʒ/` | aggraver `/a.ɡʁa.ve/` (`/ɡ/`); suggérer `/syɡ.ʒe.ʁe/` (`/ɡʒ/`) | `/ɡʒ/` when the second g is soft (before e): first g = `/ɡ/`, second = `/ʒ/`. |
| ll (after i) | `/j/`, `/l/` | fille `/fij/`; ville `/vil/` | ill = `/j/` generally, but `/l/` in ville, mille, tranquille; see ill digraph. |

#### Soft/Hard Alternation of c and g

Inherited from Latin: c and g have a 'hard' (plosive) value before the back letters a, o, u and consonants, and a 'soft' (sibilant/affricate) value before the front letters e, i, y. Silent 'e', 'u' and the cedilla are inserted to override the default and keep a stem's consonant value constant across inflection.

| Letter | Value | IPA | Environment | Examples |
|---|---|---|---|---|
| c | hard | `/k/` | before a, o, u, consonant, word-finally | car; corps; cuir; classe; sac |
| c | soft | `/s/` | before e, i, y | ciel; celui; cycle; merci |
| g | hard | `/ɡ/` | before a, o, u, consonant, word-finally | gare; gomme; aigu; glace |
| g | soft | `/ʒ/` | before e, i, y | gel; girafe; gymnase; âge |

*g is far more regular than English g: French g is soft `/ʒ/` essentially WHENEVER it precedes e, i, y, with no native exceptions of the 'get/give' type.*

Preservation devices that keep or override a value:

| Device | Function | Examples |
|---|---|---|
| cédille ç | forces soft `/s/` before a, o, u | français; garçon; nous commençons; reçu |
| silent u after g (gu) | keeps g hard `/ɡ/` before e, i | guerre; guitare; fatigué; vague |
| silent e after g (ge) | keeps g soft `/ʒ/` before a, o | mangeons; nageait; bourgeois; pigeon |
| tréma on gu (güe/güi) | forces the u to be pronounced as a separate vowel | aiguë `/e.ɡy/` (1990 spelling aigüe); ambiguïté `/ɑ̃.bi.ɡɥi.te/` |

### Silent Letters

Letters retained in spelling that are not pronounced in the modern standard accents, the chief reason the written word is longer than the spoken word. Most are fossils of word-final consonants lost between Old French and the 17th century (they RESURFACE in liaison before a vowel), plus Renaissance etymological re-spellings and the ubiquitous silent final e. The IPA column gives the modern pronunciation of the example word.

| Grapheme | Example | IPA | Note |
|---|---|---|---|
| e (final, e muet) | table | `/tabl/` | Word-final e is silent in STD (porte `/pɔʁt/`, une `/yn/`); it only marks the preceding consonant as pronounced and may carry an accent's value. QUEBEC and southern/poetic registers may realise it faintly as `[ə]`. |
| s (final plural/other) | les / amis | `/le/`, `/a.mi/` | Final s is silent (les, amis, dans, temps) but resurfaces as `/z/` in liaison (les‿amis `/le.z‿a.mi/`). Almost all plural -s are silent. |
| t / d (final) | petit / grand | `/pə.ti/`, `/ɡʁɑ̃/` | Final t and d are silent (chat, lit, pied, nord); they resurface in liaison, d as `/t/` (grand‿homme `/ɡʁɑ̃.t‿ɔm/`, petit‿ami). |
| x / z (final) | prix / nez | `/pʁi/`, `/ne/` | Final x and z are silent (prix, deux, choux, nez, riz), resurfacing as `/z/` in liaison (deux‿ans, allez‿y). |
| p / b / g (final) | trop / plomb / long | `/tʁo/`, `/plɔ̃/`, `/lɔ̃/` | Final p (trop, coup, drap), b (plomb), g (long, sang, poing) are silent. Exceptions keep them (cap, club, joug variable). |
| c (final, after nasal) | blanc | `/blɑ̃/` | Final c silent after a nasal (blanc, franc, tronc) and in tabac, estomac, porc; but pronounced in sac, lac, bec, avec, sec. |
| r (in -er verbs/nouns) | parler | `/paʁ.le/` | Final r is SILENT in the infinitive -er and many -ier nouns (parler, premier `/pʁə.mje/`, boulanger). But r IS pronounced in monosyllables and -ir/-oir/-eur (mer, sur, finir, peur). |
| h (muet and aspiré) | homme / héros | `/ɔm/`, `/e.ʁo/` | h is never a sound. H muet allows liaison/elision (l'homme, les‿hommes); h aspiré silently BLOCKS them (le héros, le /haricot/, la /hache/). |
| u (in gu, qu) | guerre / qui | `/ɡɛʁ/`, `/ki/` | Silent u keeping g hard or forming qu = `/k/` (guitare, langue, quand, banque). Pronounced only with a tréma (aiguë) or in `/kw/` loans (aquarium). |
| circumflex's lost s (no letter) | forêt / hôpital | `/fɔ.ʁɛ/`, `/ɔ.pi.tal/` | The circumflex itself stands in for a deleted Latin/Old-French s (forest > forêt, hospital > hôpital, isle > île, beste > bête); the s is 'silent' by being absent yet visible in cognates (forestier, hospitalier). |
| p (etymological cluster) | compter / sept | `/kɔ̃.te/`, `/sɛt/` | Silent p re-inserted from Latin (computare): compter, sculpter, baptême, sept `/sɛt/` (p silent, t pronounced). |
| consonants in -ent (3pl verb) | ils parlent | `/il paʁl/` | The 3rd-person-plural verb ending -ent is TOTALLY SILENT (parlent `/paʁl/`, mangent `/mɑ̃ʒ/`, finissent `/fi.nis/`) — a major homophony with the singular. Distinct from the noun/adjective -ent `/ɑ̃/` (moment, content). |
| g (in doigt, vingt) | doigt / vingt | `/dwa/`, `/vɛ̃/` | Etymological silent letters: g in doigt (< digitus), gt in vingt (g and t silent in isolation; t resurfaces in 'vingt‿et un'). |

### Diacritics

French uses five diacritical marks. Unlike English (which has none natively), French diacritics are integral to the orthography and frequently PHONEMIC. They appear on a, e, i, o, u and the consonant c. Omitting a required diacritic is a spelling error and may change the word's identity or pronunciation. The 1990 spelling rectifications made the circumflex optional on i and u except where it disambiguates (dû, mûr, sûr, jeûne, and some verb forms).

| Name | Symbol | Applies to | Phonemic value | Function |
|---|---|---|---|---|
| accent aigu | ´ | e only (é) | `/e/` (close-mid front) | Marks `/e/` as opposed to `/ə/`, `/ɛ/` or silent e. |
| accent grave | ` | e (è), a (à), u (ù) | on e: `/ɛ/` (open-mid front); on a/u: no sound change | On e, marks open `/ɛ/` vs `/e/` or `/ə/`. On a and u it is purely a HOMOGRAPH disambiguator with no phonetic effect: à (preposition) vs a (verb 'has'); où (where) vs ou (or); là (there) vs la (the). 'ù' occurs only in 'où'. |
| accent circonflexe | ˆ | a (â), e (ê), i (î), o (ô), u (û) | ê = `/ɛ(ː)/`, ô = `/o/`, â = `/ɑ/` where the contrast survives; on î, û chiefly etymological/length | Marks (1) a historically lost letter, usually s (forêt < forest, île < isle, bête < beste, hôpital); (2) historical vowel length; (3) homograph disambiguation (sur `/syʁ/` 'on' vs sûr `/syʁ/` 'sure'; du 'of the' vs dû 'owed'; mur 'wall' vs mûr 'ripe'; jeune `/ʒœn/` 'young' vs jeûne `/ʒøn/` 'fast'). The length and â = `/ɑ/` values are best preserved in QUEBEC; mostly neutralised in STD. |
| tréma | ¨ | e (ë), i (ï), u (ü) | no value of its own; forces a syllable boundary | DIAERESIS: signals that the marked vowel begins a NEW syllable and must NOT merge with the preceding vowel into a digraph. Breaks would-be digraphs ai, oi, gu, etc. |
| cédille | ¸ | c only (ç) | `/s/` | Forces soft `/s/` on c before the back vowels a, o, u, where plain c would be hard `/k/`. Keeps a stem's `/s/` constant across inflection (commencer -> nous commençons; lancer -> il lança). Never written before e, i, y (where c is already soft). |

**Examples by diacritic:**

| Diacritic | Examples |
|---|---|
| accent aigu (é) | été `/e.te/`; café `/ka.fe/`; élève `/e.lɛv/` (note é then è); préféré |
| accent grave (è/à/ù) | père `/pɛʁ/`; très `/tʁɛ/`; à `/a/` vs a `/a/`; où `/u/` vs ou `/u/` |
| accent circonflexe (â ê î ô û) | forêt `/fɔ.ʁɛ/`; côte `/kot/`; pâte `/pɑt/` (QC) ~ `/pat/` (STD); sûr `/syʁ/`; âme `/ɑm/` |
| tréma (ë ï ü) | Noël `/nɔ.ɛl/` (not \*oe); maïs `/ma.is/` (not `/mɛ/` as 'mais'); naïf `/na.if/`; aiguë / aigüe `/e.ɡy/` (ü makes the u sound); Citroën `/si.tʁɔ.ɛn/` |
| cédille (ç) | ça `/sa/`; garçon `/ɡaʁ.sɔ̃/`; français `/fʁɑ̃.sɛ/`; reçu `/ʁə.sy/`; leçon `/lə.sɔ̃/` |

### Notes

- French spelling is far more regular for READING (spelling -> sound) than for WRITING (sound -> spelling): the same phoneme has many spellings, but a given spelling almost always yields one pronunciation, so the reverse of the English situation.
- The single largest source of the spoken/written mismatch is SILENT FINAL LETTERS: most final consonants and the final e are mute in isolation but resurface in LIAISON before a vowel (petit ami, les‿amis, grand‿homme), a phenomenon with no English parallel.
- NASAL VOWELS are signalled entirely by an orthographically silent m/n: a vowel + m/n in the same syllable nasalises (bon `/bɔ̃/`), while a doubled nasal or a following vowel denasalises (bonne `/bɔn/`, année `/a.ne/`). m is written before p/b, n elsewhere.
- DIACRITICS are phonemic in French: é/è/ê distinguish `/e/`, `/ɛ/` on the letter e; the cédille forces soft c; the tréma forces a syllable split; the circumflex records a lost s and historical length. Their omission changes meaning or pronunciation.
- The Romance SOFT/HARD alternation of c and g (soft before e/i/y, hard before a/o/u) is repaired by silent e, silent u and the cédille, and is far more regular than English (no 'get/give' exceptions for g).
- Many letters are ETYMOLOGICAL re-insertions from the Renaissance, kept to display Latin roots even though mute: the p of temps/compter (< tempus, computare), the g of doigt (< digitus), the s now shown by a circumflex (forêt, hôpital).
- The two reference accents share one orthography but diverge in reading it: QUEBEC affricates `/t d/` to `[t͡s d͡z]` before `/i y j ɥ/` (tu `[t͡sy]`, dire `[d͡zɪʁ]`), laxes high vowels in closed syllables (`[ɪ ʏ ʊ]`: vite, lune, route), diphthongises long vowels (père, pâte, rose), and KEEPS the `/a/`~`/ɑ/` and `/ɛ̃/`~`/œ̃/` contrasts that STANDARD METROPOLITAN has largely merged.
- The 3rd-person-plural verb ending -ent is entirely silent (ils parlent `/il paʁl/`), a systematic homophony with other verb forms that exists only on the page; contrast the fully pronounced nasal -ent `/ɑ̃/` of nouns and adjectives (moment, content).

## Sample Words in IPA

28 illustrative French words and short liaison phrases transcribed in IPA for two reference accents — Standard Metropolitan French (français standard, Parisian-based, the analog of the English guide's RP) and Quebec French (français québécois, the analog of GA). The items are chosen to exercise the full segmental inventory: all four nasal vowels (bon, vin, blanc, brun, pain), the three front rounded vowels (tu, peu, sœur, deux, lune), the uvular R /ʁ/ (rouge, Paris, mer), the palatal nasal /ɲ/ (agneau, montagne), all three semivowels with special attention to the rare /ɥ/ (huit, nuit, lui), the postalveolar fricatives /ʃ ʒ/ (chat, jour), e caduc / schwa /ə/ in stable, deletable, and obligatory positions (samedi, petit, fenêtre), the oral mid-vowel height contrasts (les/lait, beau/botte), liaison across word boundaries (les amis, petit ami, nous avons), and the glide /w/ (oui, roi). Each entry lists the phonemes it illustrates so the array as a whole forms a verifiable coverage matrix for the French phonological system. Because French stress is fixed on the final full syllable of a rhythmic group and is never lexically contrastive, no stress marks are placed on individual words.

*Words were selected illustratively (not corpus-sliced) to guarantee complete coverage: collectively they realize every consonant phoneme of core French (the marginal loan phoneme /ŋ/ is supplied by 'parking'), one keyword per oral and nasal vowel, all three semivowels /j ɥ w/, and the principal Metropolitan~Quebec divergences. Metropolitan and Quebec transcriptions are given in parallel; where the two accents do not differ, 'quebec_ipa' repeats the Metropolitan value. Where they diverge, both values are shown and the divergence is noted in the gloss: Quebec affrication of /t d/ to [t͡s d͡z] before /i y j ɥ/ (tu, dix, tien), Quebec laxing of high vowels to [ɪ ʏ ʊ] in closed syllables (vite, lune, route), Quebec diphthongization of long/tense vowels in closed syllables (pâte, fête, neige), the maintained /a/~/ɑ/ and /ɛ̃/~/œ̃/ contrasts in Quebec versus their near-merger in Metropolitan French (pâte vs patte; brun vs brin), and conservative retention of /ɲ/ and of distinct mid-vowel qualities.*

*Standard Metropolitan French is the Parisian-based European reference (analog of RP). Quebec French is the Canadian reference (analog of GA). The principal systematic differences exemplified across this array are: (1) Quebec affricates /t/ and /d/ to [t͡s] and [d͡z] before the high front vowels and glides /i y j ɥ/, absent in Metropolitan; (2) Quebec laxes /i y u/ to [ɪ ʏ ʊ] in syllables closed by a non-lengthening consonant, while Metropolitan keeps them tense; (3) Quebec diphthongizes phonologically long vowels (/ɛː oː øː ɑ̃ ɛ̃/ etc.) in closed stressed syllables; (4) Quebec preserves the /a/~/ɑ/ contrast and the /ɛ̃/~/œ̃/ nasal contrast that Metropolitan French has largely merged (most Metropolitan speakers pronounce 'brun' as /bʁɛ̃/ and have a single low /a/). The R is uvular /ʁ/ in both reference accents.*

**Total sample words:** 28

| Word | Metropolitan IPA | Quebec IPA | Gloss | Phonemes illustrated |
|---|---|---|---|---|
| bon | `/bɔ̃/` | `/bɔ̃/` | good (m.) | `b`, `ɔ̃` |
| vin | `/vɛ̃/` | `/vɛ̃/` | wine; the front nasal /ɛ̃/. Quebec lowers and diphthongizes it in a stressed closed syllable (phonetically [vẽɪ̯]~[vã...]), but the phonemic value remains /vɛ̃/ | `v`, `ɛ̃` |
| blanc | `/blɑ̃/` | `/blɑ̃/` | white (m.); the open back nasal /ɑ̃/, which Quebec diphthongizes to [ãʊ̯]~[ãɔ̯] in a stressed closed syllable | `b`, `l`, `ɑ̃` |
| brun | `/bʁɛ̃/` | `/bʁœ̃/` | brown (m.); the front rounded nasal /œ̃/. Quebec keeps /œ̃/ distinct from /ɛ̃/ (brun ≠ brin), whereas most Metropolitan speakers merge them, realizing 'brun' as [bʁɛ̃] | `b`, `ʁ`, `œ̃` |
| pain | `/pɛ̃/` | `/pɛ̃/` | bread; the front nasal /ɛ̃/. Quebec lowers and diphthongizes it in a stressed closed syllable ([pãɪ̯]); contrast 'brun' for the /ɛ̃/~/œ̃/ pair | `p`, `ɛ̃` |
| tu | `/ty/` | `/t͡sy/` | you (sg. informal); the close front rounded vowel /y/. In Quebec /t/ is affricated to [t͡s] before /y/, giving [t͡sy]; Metropolitan keeps a plain [t] | `t`, `y` |
| peu | `/pø/` | `/pø/` | little, few; the close-mid front rounded vowel /ø/ in an open syllable. Contrast with /œ/ in 'sœur' | `p`, `ø` |
| sœur | `/sœʁ/` | `/sœːʁ/` | sister; the open-mid front rounded vowel /œ/ before /ʁ/. Quebec lengthens the vowel before /ʁ/ and may diphthongize it ([sa̯œːʁ]) | `s`, `œ`, `ʁ` |
| deux | `/dø/` | `/dø/` | two; final orthographic -x is silent. /d/ is not affricated here because /ø/ is not a high front vowel — contrast 'dix' /d͡zis/ in Quebec | `d`, `ø` |
| lune | `/lyn/` | `/lʏn/` | moon; /y/ in a closed syllable. Quebec laxes /y/ to [ʏ] in this closed syllable, giving [lʏn]; Metropolitan keeps tense [y] | `l`, `y`, `n` |
| rouge | `/ʁuʒ/` | `/ʁuʒ/` | red; word-initial uvular /ʁ/ + GOOSE-like /u/ + final voiced postalveolar fricative /ʒ/ | `ʁ`, `u`, `ʒ` |
| Paris | `/paʁi/` | `/paʁi/` | Paris; intervocalic /ʁ/ between /a/ and /i/; final -s silent. /p/ is unaspirated, unlike English | `p`, `a`, `ʁ`, `i` |
| mer | `/mɛʁ/` | `/mɛʁ/` | sea; nasal /m/ + open-mid /ɛ/ + coda /ʁ/. Homophone of 'mère' (mother) and 'maire' (mayor) | `m`, `ɛ`, `ʁ` |
| agneau | `/aɲo/` | `/aɲo/` | lamb; intervocalic palatal nasal /ɲ/ + close-mid /o/ in final open syllable. Quebec conserves /ɲ/ robustly; some Metropolitan speakers approximate it as [nj] | `a`, `ɲ`, `o` |
| montagne | `/mɔ̃taɲ/` | `/mɔ̃taɲ/` | mountain; nasal /ɔ̃/ + /t/ (not affricated, as it precedes /a/) + word-final palatal nasal /ɲ/ | `m`, `ɔ̃`, `t`, `a`, `ɲ` |
| huit | `/ɥit/` | `/ɥit/` | eight; word-initial labio-palatal approximant /ɥ/ before /i/, a cross-linguistically rare glide. Final /t/ is pronounced here (irregular for a numeral) | `ɥ`, `i`, `t` |
| nuit | `/nɥi/` | `/nɥi/` | night; /n/ + glide /ɥ/ + /i/; final -t silent. Demonstrates /ɥ/ in onset cluster after a consonant | `n`, `ɥ`, `i` |
| lui | `/lɥi/` | `/lɥi/` | him, to him/her; /l/ + /ɥ/ + /i/. Minimal contrast of the glide /ɥ/ with /w/ (cf. 'Louis' /lwi/) and with /j/ | `l`, `ɥ`, `i` |
| chat | `/ʃa/` | `/ʃa/` | cat; word-initial voiceless postalveolar fricative /ʃ/ + open /a/; final -t silent | `ʃ`, `a` |
| jour | `/ʒuʁ/` | `/ʒuʁ/` | day; word-initial voiced postalveolar fricative /ʒ/ + /u/ + coda /ʁ/. Contrast the /ʃ/~/ʒ/ voicing pair with 'chat' | `ʒ`, `u`, `ʁ` |
| samedi | `/samdi/` | `/samd͡zi/` | Saturday; the medial e caduc /ə/ is normally deleted in connected speech (/samdi/, not /samədi/), illustrating schwa drop. Quebec affricates the final /d/ before /i/, giving [samd͡zi] | `s`, `a`, `m`, `ə`, `d`, `i` |
| petit | `/pəti/` | `/pət͡si/` | small (m.); first-syllable e caduc /ə/ retained in careful speech but droppable to [pti] in casual speech. Quebec affricates /t/ before /i/ ([pət͡si]); final -t silent | `p`, `ə`, `t`, `i` |
| fenêtre | `/fənɛtʁ/` | `/fnɛːt/` | window; first-syllable e caduc /ə/ (droppable to [fnɛtʁ]) and the circumflex marking a historically long /ɛː/. Quebec commonly drops the initial schwa, lengthens/diphthongizes the vowel ([fnaɛ̯t]), and simplifies the final /tʁ/ cluster to [t] | `f`, `ə`, `n`, `ɛ`, `t`, `ʁ` |
| les | `/le/` | `/le/` | the (pl.); close-mid /e/ in an open monosyllable. Contrast with open-mid /ɛ/ in 'lait' — the les/lait pair demonstrates the /e/~/ɛ/ height contrast in final open syllables | `l`, `e` |
| lait | `/lɛ/` | `/lɛ/` | milk; open-mid /ɛ/ in an open monosyllable, the lower member of the les/lait minimal pair. Many younger Metropolitan speakers neutralize this contrast toward /e/, but the reference keeps it distinct | `l`, `ɛ` |
| beau | `/bo/` | `/bo/` | beautiful (m.); close-mid back rounded /o/ in an open syllable, the higher member of the beau/botte pair illustrating the /o/~/ɔ/ height contrast | `b`, `o` |
| botte | `/bɔt/` | `/bɔt/` | boot; open-mid back rounded /ɔ/ in a syllable closed by /t/, the lower member of the beau/botte pair. /ɔ/ characteristically appears in closed syllables, /o/ in open ones (loi de position) | `b`, `ɔ`, `t` |
| oui | `/wi/` | `/wi/` | yes; word-initial labial-velar glide /w/ + /i/. With 'roi' it exemplifies /w/; contrast /w/ here with /ɥ/ in 'huit' and /j/ in 'yeux' | `w`, `i` |

## Unicode Reference

Unicode codepoint reference for every IPA symbol, semivowel, vowel, nasalization mark, and suprasegmental sign used throughout this French pronunciation guide. Each entry gives the symbol, its Unicode codepoint (U+XXXX), decimal value, official Unicode character name, and its IPA phonetic role in French (Standard Metropolitan French = SMF, Quebec French = QC). All codepoints follow the IPA 2015 revision conventions. Many plain symbols are drawn from the Basic Latin block, but the specialized French symbols (notably the uvular ʁ, the palatal nasal ɲ, the front rounded vowels y ø œ, and the labio-palatal glide ɥ) live in the IPA Extensions and Latin-1 Supplement blocks, while the four nasal vowels are built from a base vowel plus a non-spacing combining tilde from the Combining Diacritical Marks block.

### IPA Consonant Symbols

Key French consonant symbols that are NOT plain Basic Latin reuses. The French rhotic ʁ is a voiced uvular fricative (the standard French R), distinct from any English r-symbol; ɲ is the palatal nasal of 'agneau'; ŋ is marginal, appearing only in loanwords such as 'parking'; ʃ ʒ come from IPA Extensions; ɡ is the single-story script g of IPA Extensions, distinct from Latin small letter g U+0067. Plain consonants `/p b t d k f v s z m n l/` simply reuse their Basic Latin letters and are summarized in the blocks note below.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| ʁ | `U+0281` | 641 | LATIN LETTER SMALL CAPITAL INVERTED R | voiced uvular fricative `/ʁ/` (the French R, e.g. 'rouge', 'Paris'); devoiced `[χ]` next to voiceless consonants (e.g. 'quatre' `[katʁ̥]`); in QC and traditional/rural SMF an apical alveolar trill `[r]` or uvular trill `[ʀ]` may occur as a regional variant |
| ɲ | `U+0272` | 626 | LATIN SMALL LETTER N WITH LEFT HOOK | voiced palatal nasal `/ɲ/` (e.g. 'agneau', 'montagne'); increasingly merges with the sequence `/nj/` in modern SMF but remains robust in QC and conservative speech |
| ŋ | `U+014B` | 331 | LATIN SMALL LETTER ENG | voiced velar nasal `/ŋ/` (marginal phoneme, loanwords only, e.g. 'parking', 'camping', 'shampooing'); not native to the French sound system |
| ʃ | `U+0283` | 643 | LATIN SMALL LETTER ESH | voiceless postalveolar fricative `/ʃ/` (e.g. 'chat', 'chien'); spelled 'ch' in native vocabulary |
| ʒ | `U+0292` | 658 | LATIN SMALL LETTER EZH | voiced postalveolar fricative `/ʒ/` (e.g. 'jour', 'rouge', 'genou'); spelled 'j' or soft 'g' |
| ɡ | `U+0261` | 609 | LATIN SMALL LETTER SCRIPT G | voiced velar plosive `/ɡ/` (e.g. 'gare', 'guerre'); note: the single-story script g, distinct from Latin small letter g U+0067 |

### IPA Semivowel Symbols

The three French semivowels (glides). Each is the non-syllabic counterpart of a high vowel: j corresponds to `/i/`, ɥ to `/y/`, and w to `/u/`. The labio-palatal approximant ɥ is cross-linguistically rare and is a hallmark of the French system; it comes from IPA Extensions. j and w reuse Basic Latin letters. In QC, `/j ɥ w/` trigger affrication of preceding `/t d/` where the glide is followed by `/i y/` (e.g. 'tuile' `[t͡sɥɪl]`).

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| j | `U+006A` | 106 | LATIN SMALL LETTER J | voiced palatal approximant `/j/` (e.g. 'yeux', 'fille', 'travail'); NOT the affricate value of orthographic 'j', which is `/ʒ/` in French |
| ɥ | `U+0265` | 613 | LATIN SMALL LETTER TURNED H | voiced labio-palatal approximant `/ɥ/` (e.g. 'huit', 'lui', 'nuit'); the non-syllabic counterpart of `/y/`, cross-linguistically rare |
| w | `U+0077` | 119 | LATIN SMALL LETTER W | voiced labial-velar approximant `/w/` (e.g. 'oui', 'moi' `/mwa/`, 'loi'); the non-syllabic counterpart of `/u/` |

### IPA Vowel Symbols

Oral vowel qualities of French. The front rounded vowels y ø œ are a defining feature of French; y comes from Basic Latin, ø from Latin-1 Supplement, œ from Latin Extended-A (the oe ligature). The open-mid vowels ɛ ɔ, the schwa/e caduc ə, and the back ɑ come from IPA Extensions; e o a i u reuse Basic Latin letters. SMF largely merges `/a/` and `/ɑ/` into a single `/a/`, whereas QC maintains the `/a/`~`/ɑ/` contrast (e.g. 'patte' `[pat]` vs 'pâte' `[pɑːt]`). Distinctive length ɛː survives for some SMF speakers (e.g. 'maître') and is robust in QC.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| i | `U+0069` | 105 | LATIN SMALL LETTER I | close front unrounded vowel `/i/` (e.g. 'lit', 'midi'); laxes to `[ɪ]` in QC closed syllables ending in a non-lengthening consonant (e.g. 'vite' `[vɪt]`) |
| y | `U+0079` | 121 | LATIN SMALL LETTER Y | close front rounded vowel `/y/` (e.g. 'tu', 'lune', 'sur'); laxes to `[ʏ]` in QC closed syllables (e.g. 'lutte' `[lʏt]`) |
| u | `U+0075` | 117 | LATIN SMALL LETTER U | close back rounded vowel `/u/` (e.g. 'fou', 'tout', 'rouge'); laxes to `[ʊ]` in QC closed syllables (e.g. 'route' `[ʁʊt]`) |
| e | `U+0065` | 101 | LATIN SMALL LETTER E | close-mid front unrounded vowel `/e/` (e.g. 'été', 'nez', 'parler'); typically in open syllables under the loi de position |
| ɛ | `U+025B` | 603 | LATIN SMALL LETTER OPEN E | open-mid front unrounded vowel `/ɛ/` (e.g. 'mère', 'belle', 'fait'); the long `/ɛː/` (e.g. 'maître', 'fête') is distinctive for some SMF speakers and robust in QC |
| ø | `U+00F8` | 248 | LATIN SMALL LETTER O WITH STROKE | close-mid front rounded vowel `/ø/` (e.g. 'feu', 'deux', 'bleu'); generally in open syllables and before `/z/` |
| œ | `U+0153` | 339 | LATIN SMALL LIGATURE OE | open-mid front rounded vowel `/œ/` (e.g. 'peur', 'jeune', 'fleur'); typically in closed syllables, complementary to `/ø/` |
| ə | `U+0259` | 601 | LATIN SMALL LETTER SCHWA | mid central rounded vowel `/ə/` (the e caduc / e muet, e.g. 'le', 'petit', 'demain'); deletable in many contexts; phonetically close to `[œ]` and often unrounded centralized in QC |
| o | `U+006F` | 111 | LATIN SMALL LETTER O | close-mid back rounded vowel `/o/` (e.g. 'eau', 'mot', 'rose'); in open syllables, before `/z/`, and spelled 'au'/'ô' |
| ɔ | `U+0254` | 596 | LATIN SMALL LETTER OPEN O | open-mid back rounded vowel `/ɔ/` (e.g. 'sotte', 'port', 'donne'); typically in closed syllables, complementary to `/o/` |
| a | `U+0061` | 97 | LATIN SMALL LETTER A | open front/central unrounded vowel `/a/` (e.g. 'patte', 'chat', 'ami'); the default low vowel of SMF, which has largely merged `/a/` and `/ɑ/` |
| ɑ | `U+0251` | 593 | LATIN SMALL LETTER ALPHA | open back unrounded vowel `/ɑ/` (e.g. 'pâte', 'âme', 'pas'); contrasts with `/a/` in QC and conservative SMF, but the `/a/`~`/ɑ/` contrast is largely lost in modern SMF; often long `[ɑː]` and diphthongized `[ɑʊ̯]` in QC |

### Nasal & Diacritics

Nasalization, length, liaison, affrication, and the QC lax-vowel symbols. The four French nasal vowels are NOT single codepoints: each is built as a base oral vowel PLUS the non-spacing COMBINING TILDE U+0303 (ɛ̃ = ɛ + ◌̃, ɑ̃ = ɑ + ◌̃, ɔ̃ = ɔ + ◌̃, œ̃ = œ + ◌̃). The combining tilde and the affricate tie bar are Combining Diacritical Marks; length ː is a Spacing Modifier Letter; the liaison undertie ‿ is a General Punctuation symbol; the lax high vowels ɪ ʏ ʊ (used for QC closed-syllable laxing) come from IPA Extensions. Note that SMF largely merges `/œ̃/` into `/ɛ̃/` (e.g. 'brun' = 'brin'), whereas QC keeps `/ɛ̃/` and `/œ̃/` distinct.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| ̃ | `U+0303` | 771 | COMBINING TILDE | nasalization diacritic ◌̃; the building block of all French nasal vowels (combining, attaches above the base vowel glyph). Apply to `/ɛ ɑ ɔ œ/` to form `/ɛ̃ ɑ̃ ɔ̃ œ̃/` |
| ɛ̃ | `U+025B U+0303` | 603 + 771 | LATIN SMALL LETTER OPEN E + COMBINING TILDE | nasal vowel `/ɛ̃/` (e.g. 'vin', 'pain', 'brin'); two codepoints, not one; in SMF it also absorbs etymological `/œ̃/` ('brun' = 'brin') |
| ɑ̃ | `U+0251 U+0303` | 593 + 771 | LATIN SMALL LETTER ALPHA + COMBINING TILDE | nasal vowel `/ɑ̃/` (e.g. 'enfant', 'temps', 'sans'); two codepoints; phonetically often `[ã]` or rounded/backed `[ɒ̃]` in SMF |
| ɔ̃ | `U+0254 U+0303` | 596 + 771 | LATIN SMALL LETTER OPEN O + COMBINING TILDE | nasal vowel `/ɔ̃/` (e.g. 'bon', 'pont', 'nom'); two codepoints; often raised to `[õ]` phonetically in SMF |
| œ̃ | `U+0153 U+0303` | 339 + 771 | LATIN SMALL LIGATURE OE + COMBINING TILDE | nasal vowel `/œ̃/` (e.g. 'brun', 'un', 'parfum'); two codepoints; kept distinct from `/ɛ̃/` in QC and conservative SMF, but merged into `/ɛ̃/` in much of France |
| ː | `U+02D0` | 720 | MODIFIER LETTER TRIANGULAR COLON | length mark ː; marks vowel length, e.g. `/ɛː/` ('maître'), and is pervasive in QC where long vowels lengthen and diphthongize in closed final syllables (e.g. 'pâte' `[pɑːt]`, 'neige' `[nɛɪ̯ʒ]`) |
| ‿ | `U+203F` | 8255 | UNDERTIE | liaison undertie ‿; the IPA tie linking a normally-silent final consonant to a following vowel-initial word in liaison, e.g. 'les amis' `/le‿z‿ami/`, 'un petit enfant' |
| ͡ | `U+0361` | 865 | COMBINING DOUBLE INVERTED BREVE | affricate/double-articulation tie bar ◌͡◌; joins two symbols into one affricate (combining, spans two base glyphs). Used for the QC affricates `[t͡s]` and `[d͡z]` (e.g. 'tu' `[t͡sy]`, 'dire' `[d͡zɪʁ]`) |
| ɪ | `U+026A` | 618 | LATIN LETTER SMALL CAPITAL I | near-close near-front unrounded vowel `[ɪ]`; QC lax allophone of `/i/` in closed syllables, e.g. 'vite' `[vɪt]`, 'ministre' `[mɪnɪstʁ]`; not phonemic in SMF |
| ʏ | `U+028F` | 655 | LATIN LETTER SMALL CAPITAL Y | near-close near-front rounded vowel `[ʏ]`; QC lax allophone of `/y/` in closed syllables, e.g. 'lutte' `[lʏt]`, 'jupe' `[ʒʏp]`; not phonemic in SMF |
| ʊ | `U+028A` | 650 | LATIN SMALL LETTER UPSILON | near-close near-back rounded vowel `[ʊ]`; QC lax allophone of `/u/` in closed syllables, e.g. 'route' `[ʁʊt]`, 'soupe' `[sʊp]`; not phonemic in SMF |

### Unicode Blocks Used

Summary of the Unicode blocks from which every symbol in this French guide is drawn. Verify rendering with a font that fully supports IPA Extensions and combining marks (e.g. Charis SIL, Doulos SIL, Gentium). Remember that the four nasal vowels and the QC affricates are sequences of a base glyph plus a combining mark, not precomposed single codepoints.

| Block | Range | Usage |
|---|---|---|
| Basic Latin | U+0000–U+007F | Plain consonant letters (p b t d k f v s z m n l), the semivowels j and w, and the vowel letters i u e o a y. |
| Latin-1 Supplement | U+0080–U+00FF | ø close-mid front rounded vowel (U+00F8). |
| Latin Extended-A | U+0100–U+017F | œ open-mid front rounded vowel, the oe ligature (U+0153), and ŋ velar nasal eng (U+014B). |
| IPA Extensions | U+0250–U+02AF | Specialized IPA letters: the French rhotic ʁ (U+0281), palatal nasal ɲ (U+0272), script g ɡ (U+0261), fricatives ʃ ʒ, glide ɥ (U+0265), vowels ɛ ɔ ə ɑ, and the QC lax vowels ɪ ʏ ʊ. |
| Spacing Modifier Letters | U+02B0–U+02FF | The length mark ː (U+02D0), a spacing diacritic that occupies its own width. |
| Combining Diacritical Marks | U+0300–U+036F | Non-spacing marks that attach to a base glyph: the nasalization tilde ◌̃ (U+0303), used to build all four nasal vowels ɛ̃ ɑ̃ ɔ̃ œ̃, and the affricate tie bar ◌͡◌ (U+0361), used for QC `[t͡s]` and `[d͡z]`. |
| General Punctuation | U+2000–U+206F | The liaison undertie ‿ (U+203F), which links a liaison consonant to a following vowel-initial word. |

## Cross-Reference to the Companion Guides

Cross-reference relating this French IPA pronunciation guide to its companion guides: the English IPA guide and the three Semitic guides — Classical Syriac (Peshitta), Biblical Aramaic, and Biblical Hebrew. French is genetically related to English only distantly (both are Indo-European, but French is Romance/Italic and English is Germanic) and is entirely unrelated to the Semitic family (Afroasiatic). This section therefore does not assert genetic correspondence; it documents the typological and phonological GAP between French and each companion language while noting the shared descriptive apparatus (IPA 2015, phonemic vs phonetic notation, articulatory place/manner classification) that lets all five guides be read against one another. It is a contrastive bridge: the IPA symbols mean the same articulatory targets everywhere, but the phoneme inventories, distributions, and phonological rules differ. French is documented here in two parallel reference accents — Standard Metropolitan French (SMF, the European/Parisian-based norm) and Quebec French (QC, the principal North American variety) — analogous to the English guide's General American / Received Pronunciation and the Peshitta guide's Eastern (Madnhaya) / Western (Serto) traditions.

### Shared Framework

All five guides (French, English, Peshitta, Biblical Aramaic, Biblical Hebrew) are built on the same descriptive linguistic apparatus, which makes their pronunciation data directly comparable despite the languages belonging to three different families (Romance, Germanic, and Semitic).

- The primary and sole pronunciation system is the International Phonetic Alphabet (IPA), 2015 revision; spelling/orthography is never the authoritative record.
- Phonemic transcriptions are written between /slashes/; narrow phonetic transcriptions are written between [brackets].
- Consonants are classified by place of articulation, manner of articulation, and voicing (the IPA pulmonic consonant chart).
- Vowels are classified by height (close/mid/open), backness (front/central/back), roundedness, and — where contrastive — length and nasality (the IPA vowel chart plus the combining tilde U+0303 for nasalization).
- Diacritics and suprasegmental marks are shared across the guides: `ː` length, the combining tilde `◌̃` for nasal vowels, `◌̥` for devoicing, the tie bars `t͡s d͡z` for affricates, and the non-syllabic mark for glides. Note that French does NOT use the lexical stress marks `ˈ` and `ˌ` contrastively (see Typological Contrasts: stress), whereas the English and Semitic guides do mark word stress.
- Each guide documents two parallel reference traditions of one language: French uses Standard Metropolitan French (SMF) and Quebec French (QC); English uses General American (GA) and Received Pronunciation (RP/SSBE); the Semitic guides use Eastern/Western (Peshitta) or comparable reconstructed reading traditions (e.g. Tiberian for Hebrew and Biblical Aramaic).

Because the framework is identical, an IPA symbol denotes the same articulatory target in every guide. `/b/`, `/t/`, `/s/`, `/m/`, `/l/` mean the same sounds in French as in English, Syriac, Aramaic, or Hebrew; only the phoneme inventories, allophonic rules, and distributions differ. French contributes several segments rare among the companion guides — nasal vowels `/ɛ̃ ɑ̃ ɔ̃ (œ̃)/`, front rounded vowels `/y ø œ/`, the labio-palatal glide `/ɥ/`, and the voiced uvular fricative `/ʁ/`.

### Typological Contrasts

| Feature | French (SMF / QC) | Others (English & Semitic) |
|---|---|---|
| Language family | Indo-European > Italic > Romance > Gallo-Romance. French descends from spoken (Vulgar) Latin and is most closely related to the other Romance languages (Italian, Spanish, Occitan, Catalan, Portuguese, Romanian). | English is Indo-European > Germanic > West Germanic > Anglo-Frisian — so French and English share a distant Indo-European ancestor but sit on different branches (Romance vs Germanic), and most shared vocabulary is from Norman/Latinate borrowing, not common inheritance. The Semitic guides are Afroasiatic > Semitic and are genetically UNRELATED to French: Syriac and Biblical Aramaic are Northwest Semitic (Aramaic branch), Biblical Hebrew is Northwest Semitic (Canaanite branch). |
| Stress and accent | Stress is NOT lexical or contrastive. French has fixed, predictable accentuation on the final full syllable (the last syllable not containing `/ə/`) of the rhythmic/accentual group (*groupe rythmique*), not of the individual word; the stressed syllable is realized mainly by lengthening rather than loudness, and an emphatic/contrastive *accent d'insistance* may fall initially. Because stress falls at the phrase edge, French marks no per-word stress in transcription. | English has contrastive lexical stress that distinguishes words ('record noun vs re'cord verb, 'present vs pre'sent) and triggers vowel reduction in unstressed syllables; the English guide marks `ˈ` primary and `ˌ` secondary stress on every polysyllable. In the Semitic guides stress is largely predictable from word structure (typically final or penultimate) but is still a word-level property, marked per word — unlike French phrase-final accentuation. |
| Rhythm and timing | Syllable-timed: syllables recur at roughly equal intervals and tend toward equal duration, with little vowel reduction. French has no pervasive reduction to a central schwa; the so-called *e caduc* `/ə/` is frequently elided entirely rather than weakened, and full vowels keep their quality in unstressed position. (Quebec French departs slightly toward longer, sometimes diphthongized stressed-syllable vowels, but remains broadly syllable-timed.) | English is traditionally classed as stress-timed: stressed syllables recur at roughly regular intervals, unstressed syllables are compressed, and unstressed full vowels reduce massively to schwa `/ə/`. This is the single most audible rhythmic difference between French and English. The Semitic guides are not strongly stress-timed in the English sense; Hebrew/Aramaic reduced vowels (shewa) behave differently from both English schwa and the French *e caduc*. |
| Nasal vowels | A defining trait: French has phonemic nasal vowels `/ɛ̃ ɑ̃ ɔ̃/`, plus `/œ̃/` which is kept distinct from `/ɛ̃/` in Quebec and conservative speech but is largely merged into `/ɛ̃/` in much of Metropolitan France (*brin* = *brun*). Nasalization is contrastive (*beau* `/bo/` vs *bon* `/bɔ̃/`; *paix* `/pɛ/` vs *pain* `/pɛ̃/`) and is written with the combining tilde U+0303 over the base vowel. | Neither English nor the Semitic companion languages have phonemic nasal vowels. English nasalizes vowels only allophonically before a nasal consonant (e.g. `[æ̃]` in 'man'), with no contrast, and the Semitic guides likewise treat nasalization as non-distinctive. French nasal vowels are thus a category an English or Semitic speaker must learn anew. |
| Front rounded vowels | French has three contrastive front rounded vowels `/y ø œ/` (*lu*, *deux*, *peur*), produced with the tongue advanced as for `/i e ɛ/` but the lips rounded as for `/u o ɔ/`. They are fully phonemic (*lu* `/ly/` vs *loup* `/lu/`; *deux* `/dø/` vs *dos* `/do/`). | English has NO front rounded vowels at all; learners typically substitute `/u/` or `/ju/` for `/y/`. The Semitic companion inventories likewise lack front rounded vowels (their vowel systems are 5–7 plain qualities such as `/a ɛ e i ɔ o u/`). This is, with the nasal vowels, the other principal vowel-system gap between French and every companion guide. |
| The rhotic (French R) | Standard French `/ʁ/` is a voiced uvular fricative (or approximant), with a voiceless `[χ]` allophone next to voiceless consonants. Some traditional and southern/Quebec speech uses an apical alveolar trill or tap `[r ~ ɾ]`, but the supraregional norm in both SMF and QC is uvular. | English `/r/` is a postalveolar/retroflex APPROXIMANT `[ɹ]` in most accents — articulated at a completely different place (coronal, not uvular) and with no frication. Among the Semitic guides, Syriac and Biblical Aramaic Resh is an alveolar TRILL `/r/`, while Tiberian Hebrew Resh is reconstructed as uvular `/ʁ/` — the latter the closest cross-guide match to the French R, though Hebrew `/ʁ/` and French `/ʁ/` arose independently. |
| Semivowels (glides) | French has THREE phonemic semivowels: palatal `/j/` (*paille*), labio-velar `/w/` (*oui*), and the cross-linguistically rare labio-palatal `/ɥ/` (*huit*, *lui*) — the glide counterpart of the vowel `/y/`. The three contrast minimally in some pairs and arise from high vowels `/i u y/` before another vowel. | English and the Semitic guides have only two glides, `/j/` and `/w/` (Yodh and Waw in the Semitic abjads). None of the companion languages has `/ɥ/`, which an English or Semitic speaker must learn anew; it is one of the rarer segments documented across the whole guide set. |
| Liaison and enchaînement | French has pervasive external sandhi: a normally silent word-final consonant is pronounced and resyllabified onto a following vowel-initial word (liaison: *les amis* `/le.z‿a.mi/`, *petit ami* `/pə.ti.t‿a.mi/`), and final pronounced consonants link across word boundaries (enchaînement). Liaison is obligatory, optional, or forbidden depending on syntax and register. | English has only limited connected-speech linking (e.g. linking/intrusive r in non-rhotic accents) and nothing like the grammatically conditioned reappearance of latent consonants. The Semitic guides have their own sandhi phenomena (e.g. the Begadkephat spirantization rule, Hebrew article gemination), but these are internal allophonic/morphophonemic rules, not the cross-word liaison of latent final consonants characteristic of French. |
| Diphthongs | Standard French has NO phonemic diphthongs; vowels are pure monophthongs, and sequences that look like diphthongs in spelling are either single monophthongs (*eau* `/o/`) or glide + vowel sequences (`/wa/`, `/ɥi/`, `/jɛ/`). Quebec French does produce phonetic diphthongization of long/tense vowels in closed syllables (e.g. *tête* `[tɛɪ̯t]`, *pâte* `[pɑʊ̯t]`), but this is allophonic, not a set of contrastive diphthong phonemes. | English has a rich set of phonemic diphthongs (FACE `/eɪ/`, PRICE `/aɪ/`, CHOICE `/ɔɪ/`, MOUTH `/aʊ/`, GOAT `/oʊ~əʊ/`), keyed in its guide to the Wells (1982) Standard Lexical Sets — a system specific to English and not transferable to French. The Semitic guides treat diphthongs as marginal, arising from vowel + glide (Waw/Yodh) sequences rather than forming a large contrastive set. |
| Orthography and spelling depth | French uses the 26-letter Latin alphabet with five diacritics (aigu, grave, circonflexe, tréma, cédille) and the ligature œ. Its orthography is etymologically DEEP, preserving many silent letters — especially silent final consonants and silent final -e — but it is comparatively REGULAR in the reading direction (grapheme→phoneme is largely predictable), while phoneme→spelling is highly ambiguous. | English also uses the Latin alphabet but is notoriously irregular in BOTH directions (cough, though, through, bough). The Semitic guides use abjads (consonant-primary scripts) written right-to-left, where vowels are marked only by optional pointing — a fundamentally different orthographic principle from the French alphabet. |
| Writing system and direction | Written left-to-right in the Latin (Roman) alphabet, a true alphabet representing both consonants and vowels with separate letters (plus diacritics and the œ ligature). | English is likewise written left-to-right in the Latin alphabet. The three Semitic guides are written RIGHT-TO-LEFT: Syriac uses the Syriac abjad (U+0700–U+074F); Biblical Aramaic and Biblical Hebrew use the Hebrew square abjad with Tiberian niqqud. An abjad encodes consonants as letters and marks vowels only optionally — the deepest writing-system contrast in the guide set. |
| Consonant inventory — guttural and emphatic region | French has no pharyngeal, pharyngealized (emphatic), or glottal consonants. Its only back/dorsal obstruent is the uvular `/ʁ/` (the French R), and the velars `/k ɡ/`; there is no `/h/` at all (the orthographic h is silent, though 'h aspiré' blocks liaison). The marginal `/ŋ/` occurs only in loanwords (*parking*, *camping*). | English adds `/h/` (onset only) but likewise has no pharyngeals or emphatics. The Semitic guides have a rich guttural and emphatic series absent from French: pharyngeals `/ħ/` (Heth) and `/ʕ/` (Ayin), glottals `/ʔ/` (Aleph) and `/h/` (He), the uvular plosive `/q/` (Qoph), and emphatic (pharyngealized) `/tˤ/` (Teth) and `/sˤ/` (Tsade). These are the principal articulatory targets a French speaker would have to learn to read the Semitic guides. |
| Vowel inventory size | A large vowel system: about 11–13 oral vowels `/i e ɛ (ɛː) a (ɑ) ɔ o u y ø œ ə/` plus 3–4 nasal vowels `/ɛ̃ ɑ̃ ɔ̃ (œ̃)/`. SMF tends to merge `/a/`~`/ɑ/` and `/ɛ̃/`~`/œ̃/`, while QC robustly maintains both contrasts and adds lax high allophones `[ɪ ʏ ʊ]` in closed syllables and long-vowel diphthongization. | English has a comparably large system (roughly 11–12 monophthongs plus phonemic diphthongs), but built on different qualities (no front rounded vowels, no nasal vowels). The Semitic companion languages have SMALL vowel systems — typically 5–7 qualities (e.g. Peshitta Eastern `/a ɑ ɛ e i o u/` or Western `/a ɔ e i u/`; Tiberian `/a ɛ e i ɔ o u/`) — with no nasal or front rounded vowels and only marginal diphthongs. |
| Morphological type | Fusional/inflecting with strong analytic tendencies, inherited from Latin: grammatical categories are expressed by affixes fused onto stems and increasingly by free function words and fixed word order (much verbal inflection is audible only in liaison or is neutralized in speech, e.g. *parle/parles/parlent* all `/paʁl/`). | English is predominantly concatenative/fusional with even stronger analytic/isolating tendencies (little inflection, heavy reliance on word order and function words). The Semitic guides use root-and-pattern (templatic, nonconcatenative) morphology: a discontinuous triconsonantal root (e.g. k-t-b 'write') is interleaved with vowel/consonant templates (katab, ktib, maktub) — a system with no French or English equivalent. |

### Companion Guides

- **English** — `english_pronunciation_guide.json`. Modern English, documented in General American (GA) and Received Pronunciation (RP/SSBE) in parallel. Indo-European but Germanic (West Germanic > Anglo-Frisian), so it shares a distant ancestor with French but a different branch. The closest typological companion to French in script (Latin, left-to-right) and vowel-system size, but contrasting in rhythm (stress-timed vs French syllable-timed), lexical stress (contrastive vs French phrase-final), phonemic diphthongs (present vs absent in French), and its rhotic (`[ɹ]` vs French `/ʁ/`). Useful as a contrastive baseline for English-speaking learners of French.
- **Peshitta** — `peshitta_pronunciation_guide.json`. Classical Syriac (Aramaic), the Peshitta reading tradition. Documents Eastern (Madnhaya) and Western (Serto) traditions in parallel — the same two-tradition design that French mirrors with SMF and QC. Covers the Begadkephat spirantization rule, guttural and emphatic consonants, and the Syriac abjad (U+0700–U+074F). Afroasiatic > Semitic (Aramaic branch); genetically unrelated to French. Shares with French the IPA framework and the plain stops `/b d ɡ k t/`, the fricatives `/f v s z ʃ/`, the nasals `/m n/`, the lateral `/l/`, and the glides `/j w/`.
- **Biblical Aramaic** — `biblical_aramaic_pronunciation_guide.json`. Biblical Aramaic / Jewish Literary Aramaic, as preserved in the Tiberian pointing of the Aramaic portions of the Hebrew Bible (Daniel, Ezra). Northwest Semitic (Aramaic branch); uses the Hebrew square abjad with Tiberian niqqud, written right-to-left. Shares emphatic/guttural consonants and triconsonantal root morphology with Syriac and Hebrew — all features absent from French. Overlaps with French only in the shared IPA inventory of plain stops, sibilants, nasals, `/l/`, and the glides `/j w/`.
- **Biblical Hebrew** — `biblical_hebrew_pronunciation_guide.json`. Biblical (Classical) Hebrew in the Tiberian reading tradition. Northwest Semitic (Canaanite branch); uses the Hebrew square abjad with Tiberian niqqud, written right-to-left. Notable for the prefixed definite article `/ha-/` with following gemination, a 7-vowel system, and — uniquely among the Semitic guides — a uvular Resh reconstructed as `/ʁ/`, the single closest cross-guide match to the French rhotic `/ʁ/` (though the two arose independently).

### Shared IPA Symbols

IPA consonant symbols whose phonetic value is shared between French and one or more of the companion guides (English and the Semitic three), allowing direct cross-reference. Each symbol denotes the same articulatory target in every guide; the languages differ in how these phonemes pattern and distribute, not in what the symbols mean. French realizations are noted for both reference accents (SMF / QC) where they differ.

| IPA | Name | French | English | Semitic |
|---|---|---|---|---|
| `p` | voiceless bilabial plosive | `/p/` (*pain*, *cap*); unaspirated in French, unlike English aspirated `[pʰ]` | `/p/` (pea, cap); aspirated `[pʰ]` in stressed onset | Pe (hard/plosive allophone) in Syriac, Aramaic, Hebrew |
| `b` | voiced bilabial plosive | `/b/` (*beau*, *robe*) | `/b/` (bee, cab) | Beth (hard/plosive allophone) in all three Semitic guides |
| `t` | voiceless alveolar/dental plosive | `/t/` (*table*, *vite*); dental and unaspirated. In QC, affricated to `[t͡s]` before `/i y j ɥ/` (*tu* `[t͡sy]`, *petit* `[pə.t͡si]`) | `/t/` (tea, cat); aspirated `[tʰ]` in onset, flapped `[ɾ]` intervocalically in GA | Taw (hard/plosive allophone) in all three (distinct from emphatic Teth `/tˤ/`) |
| `d` | voiced alveolar/dental plosive | `/d/` (*deux*, *ronde*); dental. In QC, affricated to `[d͡z]` before `/i y j ɥ/` (*dire* `[d͡ziʁ]`, *du* `[d͡zy]`) | `/d/` (do, bed) | Daleth (hard/plosive allophone) in all three |
| `k` | voiceless velar plosive | `/k/` (*quai*, *sac*); unaspirated, unlike English `[kʰ]` | `/k/` (key, back); aspirated `[kʰ]` in stressed onset | Kaph (hard/plosive allophone) in all three |
| `ɡ` | voiced velar plosive | `/ɡ/` (*gare*, *bague*) | `/ɡ/` (go, bag) | Gimel (hard/plosive allophone) in all three |
| `f` | voiceless labiodental fricative | `/f/` (*feu*, *neuf*) | `/f/` (fee, leaf) | Pe (soft/spirantized allophone, Begadkephat) in all three |
| `v` | voiced labiodental fricative | `/v/` (*vin*, *rêve*) | `/v/` (vee, leave) | Beth (soft/spirantized allophone) in Aramaic and Hebrew; spirantized Beth is `[v]` in Western Syriac (Eastern Syriac tends toward `[w]`) |
| `s` | voiceless alveolar fricative | `/s/` (*sang*, *basse*) | `/s/` (see, bus) | Semkath / plain Samekh and Sin in all three (distinct from emphatic Tsade `/sˤ/`) |
| `z` | voiced alveolar fricative | `/z/` (*zéro*, *rose*); also the regular liaison consonant of plural -s (*les amis* `[le.z‿a.mi]`) | `/z/` (zoo, buzz) | Zayin in all three |
| `ʃ` | voiceless postalveolar fricative | `/ʃ/` (*chat*, *biche*) | `/ʃ/` (she, fish) | Shin in all three (contrasts with `/s/`) |
| `ʒ` | voiced postalveolar fricative | `/ʒ/` (*jour*, *rouge*); a full phoneme in French | `/ʒ/` (meaSure, beige); marginal/low-frequency phoneme | Absent as a primary phoneme from the Semitic companion inventories (the guides treat it as not contrastive) |
| `m` | voiced bilabial nasal | `/m/` (*main*, *pomme*) | `/m/` (me, sum) | Mem / Mim in all three |
| `n` | voiced alveolar nasal | `/n/` (*nous*, *bonne*) | `/n/` (no, sun) | Nun in all three |
| `l` | voiced alveolar lateral approximant | `/l/` (*lit*, *sel*); consistently CLEAR `[l]` in all positions, with no dark `[ɫ]` allophone | `/l/` with clear `[l]` (onset) and dark `[ɫ]` (coda) allophones | Lamadh / Lamed in all three (clear lateral) |
| `j` | voiced palatal approximant | `/j/` (*yeux*, *paille*, *bien*) | `/j/` (yes) | Yodh / Yud in all three |
| `w` | voiced labial-velar approximant | `/w/` (*oui*, *moi* `/mwa/`, *ouest*) | `/w/` (we) | Waw / Vav (consonantal value) in all three; in some Hebrew traditions realized as `/v/` |
| `ŋ` | voiced velar nasal | `/ŋ/` marginal, in loanwords only (*parking* `[paʁ.kiŋ]`, *camping*) | `/ŋ/` (siNG); a full phoneme in English | Not an independent phoneme (an allophone of `/n/` before velars at most) |

#### French-Distinctive Consonants

French consonant phonemes with no direct counterpart in English; some have a partial match in only one Semitic guide.

- `ʁ` (the French R — voiced uvular fricative/approximant, voiceless `[χ]` next to voiceless consonants; absent in English, whose `/r/` is `[ɹ]`; matched only by Tiberian Hebrew Resh `/ʁ/`, and contrasting with the alveolar trill `/r/` of Syriac and Biblical Aramaic Resh)
- `ɲ` (palatal nasal — *agneau*, *montagne*; an independent phoneme in conservative French, increasingly `[nj]` in SMF; absent as a phoneme in English and the Semitic guides)
- `ɥ` (labio-palatal approximant — *huit*, *lui*; the third French semivowel and a cross-linguistically rare segment; absent in English and all Semitic companion guides)

#### French-Distinctive Vowels

French oral and nasal vowel phonemes absent from the English and Semitic companion inventories — the front rounded `/y ø œ/`, the nasal `/ɛ̃ ɑ̃ ɔ̃ œ̃/`, and the back `/ɑ/` — plus the *e caduc* `/ə/`, which does have an English counterpart (the schwa `/ə/`, English's most frequent vowel) but differs behaviorally: in French it is frequently elided entirely and phonetically rounded, rather than being the obligatory product of unstressed-syllable reduction it is in English. These are the principal vocalic targets a learner from those languages must acquire or re-learn.

- `y` (close front rounded — *lu*, *tu*; absent in English and Semitic, where learners substitute `/u/` or `/ju/`)
- `ø` (close-mid front rounded — *deux*, *peu*; absent in English and Semitic)
- `œ` (open-mid front rounded — *peur*, *sœur*; absent in English and Semitic)
- `ə` (*e caduc* / schwa — *petit*, *le*; phonetically central rounded in French and frequently ELIDED, unlike the always-present English reduction schwa)
- `ɛ̃` (nasal front vowel — *pain*, *vin*; no phonemic nasal vowels in English or Semitic)
- `ɑ̃` (nasal open back vowel — *temps*, *blanc*)
- `ɔ̃` (nasal mid back rounded vowel — *bon*, *son*)
- `œ̃` (nasal open-mid front rounded vowel — *brun*, *parfum*; kept distinct in QC and conservative speech, merged into `/ɛ̃/` in much of Metropolitan France)
- `ɑ` (open back unrounded — *pâte*; contrasts with `/a/` in QC, largely merged in SMF)

#### Semitic-Only Consonants

Consonant phonemes of the Semitic companion guides with no counterpart in French (or English); these are the principal articulatory targets a French speaker must learn anew to read those guides.

- `ʔ` (Aleph/Alaph — glottal stop; in French only a marginal onset of vowel-initial words and the marker of 'h aspiré', not a phoneme)
- `ħ` (Heth/Kheth — voiceless pharyngeal fricative; absent in French)
- `ʕ` (Ayin — voiced pharyngeal fricative; absent in French)
- `tˤ` (Teth — emphatic/pharyngealized t; absent in French)
- `sˤ` (Tsade/Tsadi — emphatic/pharyngealized s; absent in French)
- `q` (Qoph — voiceless uvular plosive; absent in French, whose only uvular is the fricative `/ʁ/`)
- `x` (spirantized Kaph in Hebrew/Syriac/Aramaic; not a French phoneme — French has no voiceless velar/uvular fricative except the `[χ]` allophone of `/ʁ/`)
- `h` (He — voiceless glottal fricative; a phoneme in English and the Semitic guides but ABSENT in French, where orthographic h is silent)

> **Note:** Like the English guide's cross_reference, this section is fundamentally contrastive rather than genetic. French shares the IPA descriptive framework, the plain stops, the sibilants, the nasals, `/l/`, and the glides `/j w/` with all four companion guides, but it differs in family (Indo-European/Romance vs Germanic English vs Afroasiatic Semitic), in prosody (syllable-timed with fixed phrase-final accentuation vs English stress-timed lexical stress vs Semitic predictable word stress), in script direction (Latin left-to-right vs Semitic right-to-left abjad), and above all in inventory: French alone contributes phonemic nasal vowels `/ɛ̃ ɑ̃ ɔ̃ œ̃/`, front rounded vowels `/y ø œ/`, the third semivowel `/ɥ/`, the uvular rhotic `/ʁ/`, pervasive liaison, and an absence of both `/h/` and phonemic diphthongs. The IPA symbols mean the same everywhere; it is the systems they build that diverge.
