# English IPA Pronunciation Guide

**Version:** 1.0.0
**Date:** 2026-06-24
**Language:** English (ISO 639-3: `eng`)  
**Encoding:** UTF-8  
**IPA Standard:** IPA (International Phonetic Alphabet, 2015 revision)  
**Reference Accents:** General American (GA) and Received Pronunciation / Standard Southern British English (RP/SSBE)  

Machine-readable IPA-based pronunciation guide for Modern English. All pronunciation data is encoded in the International Phonetic Alphabet (IPA, 2015 revision) as the primary and only system. Designed for AI-assisted pronunciation, text-to-speech reference, second-language teaching, and language documentation. Two reference accents are documented in parallel: General American (GA) and Received Pronunciation / Standard Southern British English (RP/SSBE).

### Varieties Covered

- **General American (GA)** — United States (supraregional 'broadcast' or 'network' standard, lacking strongly marked regional features). Rhotic: non-prevocalic /r/ is pronounced in all positions (e.g. car, card, butter), so the historical NURSE/lettER/START/NORTH/FORCE/CURE vowels are r-colored. The most widely used reference accent for American English, with the FATHER–BOTHER merger (PALM = LOT), the LOT–THOUGHT (cot–caught) merger common in many speakers, a flapped /t/ and /d/ (`[ɾ]`) intervocalically, and TRAP/BATH with a single low front /æ/ vowel (no BATH broadening). This guide transcribes the GA reference as cot≠caught (unmerged): LOT as `/ɑ/` and THOUGHT as `/ɔ/`, treating them as distinct phonemes, while noting that the cot–caught merger is widespread among GA speakers.
- **Received Pronunciation / Standard Southern British English (RP/SSBE)** — England (supraregional southern British standard; 'BBC English', SSBE). Non-rhotic: non-prevocalic /r/ is NOT pronounced; historical coda /r/ is lost or realized as vowel length/quality and centring diphthongs (e.g. car `[kɑː]`, here `[hɪə]`). Linking and intrusive /r/ appear at word boundaries before a vowel. The traditional prestige reference accent of England, now usually described in its modern form as Standard Southern British English (SSBE), with the TRAP–BATH split (BATH = PALM `/ɑː/`), a distinct LOT `/ɒ/` vs THOUGHT `/ɔː/`, the LOT–PALM contrast, no T-flapping, and centring diphthongs for the NEAR/SQUARE/CURE sets.

### Companion Files

- `peshitta_pronunciation_guide.json`
- `biblical_aramaic_pronunciation_guide.json`
- `biblical_hebrew_pronunciation_guide.json`

### Notes

- English is written left-to-right in the Latin (Roman) script, unlike the right-to-left Semitic companion guides.
- English orthography is deep and opaque: the same letter or digraph can map to many phonemes and the same phoneme to many spellings, so IPA (not spelling) is the authoritative pronunciation record here.
- The two reference accents differ centrally in rhoticity: General American is rhotic (coda /r/ pronounced), Received Pronunciation is non-rhotic (coda /r/ lost), which reshapes the entire NURSE/NEAR/SQUARE/START/NORTH/FORCE/CURE region of the vowel system.
- Lexical (word) stress is contrastive and phonemic in English: many noun/verb pairs are distinguished solely by stress placement within a single lexeme (e.g. ˈrecord noun vs reˈcord verb; ˈpresent noun vs preˈsent verb; ˈobject noun vs obˈject verb), unlike the largely predictable stress of the Semitic companion languages.
- English has a large vowel inventory (~11–12 monophthongs plus a set of phonemic diphthongs such as /eɪ aɪ ɔɪ aʊ oʊ~əʊ/), far larger than the typical Semitic vowel system.
- English has no pharyngeal or pharyngealized/emphatic consonants and no uvular or trilled /r/; the rhotic is typically a postalveolar or retroflex approximant `[ɹ]`, not the alveolar trill /r/ of Syriac Resh.
- Phonemic transcriptions use / / slashes; phonetic transcriptions use [ ] brackets. Suprasegmentals: /ː/ marks vowel length, /ˈ/ marks primary stress, /ˌ/ marks secondary stress, /ʰ/ marks aspiration, and the under-ring /◌̩/ marks a syllabic consonant.
- Vowel reduction to schwa /ə/ in unstressed syllables is pervasive and is a defining feature of English rhythm (stress-timing); full vowels in unstressed syllables are comparatively rare.
- The voiceless plosives /p t k/ are aspirated `[pʰ tʰ kʰ]` in stressed syllable onsets, and in GA intervocalic /t d/ are commonly realized as an alveolar tap/flap `[ɾ]` (e.g. butter, ladder), an allophonic process absent from the companion languages.
- The phoneme /l/ has a 'clear' `[l]` allophone (before vowels) and a 'dark', velarized `[ɫ]` allophone (in coda and before consonants); in many accents coda /l/ may vocalize toward `[o~ʊ]`.
- The 24 consonant phonemes of English are: /p b t d k ɡ tʃ dʒ f v θ ð s z ʃ ʒ h m n ŋ l r j w/; the dental fricatives /θ ð/ and the velar nasal /ŋ/ are cross-linguistically marked sounds that recur as learner difficulties.

## Table of Contents

- [How to Read This Guide](#how-to-read-this-guide)
  - [Phonemic vs phonetic notation](#phonemic-vs-phonetic-notation)
  - [Stress marks](#stress-marks)
  - [Length](#length)
  - [The two reference accents](#the-two-reference-accents)
  - [Wells lexical sets](#wells-lexical-sets)
- [Phonological Inventory](#phonological-inventory)
  - [Consonant Phonemes](#consonant-phonemes)
  - [Vowel Phonemes](#vowel-phonemes)
- [Consonants](#consonants)
  - [Consonant Inventory](#consonant-inventory)
  - [Natural Classes](#natural-classes)
- [Vowels (Monophthongs)](#vowels-monophthongs)
  - [Vowel Classes](#vowel-classes)
  - [Monophthong Inventory by Lexical Set](#monophthong-inventory-by-lexical-set)
  - [Key Mergers and Splits](#key-mergers-and-splits)
  - [Rhoticity Overview](#rhoticity-overview)
  - [Weak Vowels Overview](#weak-vowels-overview)
  - [IPA Symbol Summary](#ipa-symbol-summary)
- [Diphthongs](#diphthongs)
  - [Detailed Notes](#detailed-notes)
- [Consonant–Vowel IPA Matrix](#consonantvowel-ipa-matrix)
  - [Reference Vowels](#reference-vowels)
  - [CV Matrix](#cv-matrix)
  - [Phonetic Notes](#phonetic-notes)
  - [Accent Notes](#accent-notes)
- [Suprasegmentals](#suprasegmentals)
  - [Stress](#stress)
  - [Rhythm](#rhythm)
  - [Vowel Reduction](#vowel-reduction)
  - [Aspiration](#aspiration)
  - [Vowel Length & Clipping](#vowel-length--clipping)
  - [Intonation](#intonation)
- [Syllable Structure](#syllable-structure)
  - [Onset](#onset)
  - [Nucleus](#nucleus)
  - [Coda](#coda)
  - [Syllable Types](#syllable-types)
  - [Syllabification](#syllabification)
  - [Constraints](#constraints)
- [Phonological Rules](#phonological-rules)
  - [Rules at a Glance](#rules-at-a-glance)
  - [Rule 1: Aspiration of voiceless stops](#rule-1-aspiration-of-voiceless-stops)
  - [Rule 2: T-flapping (tapping)](#rule-2-t-flapping-tapping)
  - [Rule 3: Glottal reinforcement (pre-glottalization)](#rule-3-glottal-reinforcement-pre-glottalization)
  - [Rule 4: T-glottalling](#rule-4-t-glottalling)
  - [Rule 5: L-velarization (clear vs. dark L)](#rule-5-l-velarization-clear-vs-dark-l)
  - [Rule 6: L-vocalization](#rule-6-l-vocalization)
  - [Rule 7: Vowel reduction to schwa](#rule-7-vowel-reduction-to-schwa)
  - [Rule 8: Nasal place assimilation](#rule-8-nasal-place-assimilation)
  - [Rule 9: Yod-coalescence (palatalization)](#rule-9-yod-coalescence-palatalization)
  - [Rule 10: Yod-dropping](#rule-10-yod-dropping)
  - [Rule 11: Linking-R and intrusive-R](#rule-11-linking-r-and-intrusive-r)
  - [Rule 12: Pre-fortis clipping](#rule-12-pre-fortis-clipping)
  - [Rule 13: Elision and cluster simplification](#rule-13-elision-and-cluster-simplification)
  - [Rule 14: Voicing assimilation of the regular -s and -ed suffixes](#rule-14-voicing-assimilation-of-the-regular--s-and--ed-suffixes)
  - [Rule 15: G-dropping (-ing velar fronting)](#rule-15-g-dropping--ing-velar-fronting)
  - [Rule 16: happY-tensing](#rule-16-happy-tensing)
  - [Notes](#notes-1)
- [General American vs. Received Pronunciation](#general-american-vs-received-pronunciation)
  - [Reference accents](#reference-accents)
  - [Differences](#differences)
- [Orthography: Grapheme–Phoneme Correspondences](#orthography-graphemephoneme-correspondences)
  - [General Principles](#general-principles)
  - [Consonant Graphemes](#consonant-graphemes)
  - [Vowel Graphemes](#vowel-graphemes)
  - [Silent Letters](#silent-letters)
  - [Notes](#notes-2)
- [Weak Forms & Connected Speech](#weak-forms--connected-speech)
  - [Reference Accents](#reference-accents-1)
  - [Weak Forms](#weak-forms)
  - [Weak-Form Rules](#weak-form-rules)
  - [Connected-Speech Processes](#connected-speech-processes)
  - [Interaction & Register](#interaction--register)
- [Sample Words in IPA](#sample-words-in-ipa)
- [Unicode Reference](#unicode-reference)
  - [IPA Consonant Symbols](#ipa-consonant-symbols)
  - [IPA Vowel Symbols](#ipa-vowel-symbols)
  - [Diacritics & Suprasegmentals](#diacritics--suprasegmentals)
  - [Unicode Blocks Used](#unicode-blocks-used)
- [Cross-Reference to the Semitic Guides](#cross-reference-to-the-semitic-guides)
  - [Shared Framework](#shared-framework)
  - [Typological Contrasts](#typological-contrasts)
  - [Companion Guides](#companion-guides)
  - [Shared IPA Symbols](#shared-ipa-symbols)

## How to Read This Guide

This guide records pronunciation in the International Phonetic Alphabet (IPA, 2015 revision). A few conventions are used throughout.

### Phonemic vs phonetic notation

- **Phonemic transcription** is written between forward slashes: `/ /`. It records the contrastive sound categories (phonemes) of the language, abstracting away from predictable detail — e.g. THOUGHT is `/θɔːt/` (RP).
- **Phonetic transcription** is written between square brackets: `[ ]`. It records the actual realized sounds, including allophonic detail — e.g. the aspirated onset in `[pʰ]` or the GA flap in butter `[ˈbʌɾɚ]`.

### Stress marks

English word stress is contrastive (phonemic), so it is always marked:

| Mark | Name | Meaning |
| --- | --- | --- |
| `ˈ` | primary stress | precedes the syllable carrying main stress (e.g. reˈcord, verb) |
| `ˌ` | secondary stress | precedes a syllable carrying weaker stress (e.g. ˌunderˈstand) |

### Length

- The length mark `ː` after a vowel signals a long vowel — e.g. FLEECE `/iː/`, THOUGHT `/ɔː/` (RP). Vowel length interacts with quality, so the length mark is part of the vowel symbol, not an independent feature.

### The two reference accents

Two co-equal reference accents are documented in parallel:

- **General American (GA)** — rhotic; coda /r/ is pronounced.
- **Received Pronunciation / SSBE (RP)** — non-rhotic; coda /r/ is lost or realized as length and centring diphthongs.

Where the two accents differ, both transcriptions are given side by side. The central systematic difference is rhoticity, which reshapes the NURSE/NEAR/SQUARE/START/NORTH/FORCE/CURE region of the vowel system.

### Wells lexical sets

English vowel phonemes are keyed to the Standard Lexical Sets of Wells (1982), *Accents of English*. Each keyword (written in SMALL CAPITALS by convention, e.g. KIT, DRESS, TRAP) names a set of words that share the same vowel within a given accent. The lexical sets let the same vowel category be tracked across GA and RP even where its phonetic realization differs, providing accent-neutral cross-reference labels.

## Phonological Inventory

The complete phonemic inventory of Modern English, organized by IPA categories. Documented in parallel for two reference accents: General American (GA) and Received Pronunciation (RP, Standard Southern British English). The consonant system is shared across both accents; the vowel systems diverge, the most consequential difference being rhoticity (GA is rhotic, RP is non-rhotic).

### Consonant Phonemes

All consonant phonemes of Modern English arranged by place and manner of articulation. The consonant inventory is essentially identical between General American and Received Pronunciation.

**Total consonant phonemes:** 24  
24 consonant phonemes: 6 plosives `/p b t d k ɡ/` + 2 affricates `/tʃ dʒ/` + 9 fricatives `/f v θ ð s z ʃ ʒ h/` + 3 nasals `/m n ŋ/` + 1 lateral approximant `/l/` + 1 rhotic approximant `/r/` + 2 central (glide) approximants `/j w/` = 24. Note: `/r/` is phonetically `[ɹ]` (post-alveolar/alveolar approximant) in most varieties; `/l/` has a clear allophone `[l]` (syllable onset) and a dark/velarised allophone `[ɫ]` (syllable coda); voiceless plosives `/p t k/` are aspirated `[pʰ tʰ kʰ]` in stressed onsets.

#### IPA Consonant Chart

IPA consonant chart for Modern English (rows = manner, columns = place). Where two symbols appear in a cell, voiceless precedes voiced.

| Manner | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|---|---|---|---|---|---|---|---|---|
| Plosive | p b |  |  | t d |  |  | k ɡ |  |
| Affricate |  |  |  |  | tʃ dʒ |  |  |  |
| Nasal | m |  |  | n |  |  | ŋ |  |
| Fricative |  | f v | θ ð | s z | ʃ ʒ |  |  | h |
| Approximant | w |  |  | r |  | j | w |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

*`/w/` is a labial-velar approximant and is not assignable to a single column in this simplified chart; because it patterns with both bilabial and velar, it is shown in BOTH the bilabial and velar cells of the approximant row (a single phoneme displayed in two places, not two phonemes). The rhotic `/r/` is shown in the alveolar column but is phonetically post-alveolar `[ɹ]`. `/h/` is placed in the glottal column. All 24 phonemes are accounted for: p b t d k ɡ (6) + tʃ dʒ (2) + m n ŋ (3) + f v θ ð s z ʃ ʒ h (9) + r j (2) + l (1) + w (1) = 24.*

#### Notes by Place of Articulation

- **Bilabial:** `/p b m/`. `/p/` is aspirated `[pʰ]` in stressed syllable onsets (e.g. 'pin'); `/b/` may be partially devoiced initially/finally. The labial-velar approximant `/w/` also has a bilabial component but is listed under labial-velar.
- **Labiodental:** `/f v/`. `/f/` as in 'fan'; `/v/` as in 'van'. The only minimal labiodental pair in the system.
- **Dental:** `/θ ð/`. `/θ/` (voiceless, as in 'thin') and `/ð/` (voiced, as in 'this') are interdental or dental fricatives. Both are spelled with the digraph 'th'.
- **Alveolar:** `/t d s z n l r/`. `/t/` is aspirated `[tʰ]` in stressed onsets; in GA it is commonly a flap `[ɾ]` intervocalically ('water'); `/t/` may be glottalised/glottalled `[ʔ]` in RP coda position. `/l/` is clear `[l]` before vowels and dark/velarised `[ɫ]` in codas ('feel'), and can be syllabic `[l̩]` ('bottle'). `/r/` is the rhotic phoneme, phonetically a post-alveolar approximant `[ɹ]` (often labialised `[ɹʷ]`); it is realised in RP only before vowels (non-rhotic).
- **Postalveolar:** `/tʃ dʒ ʃ ʒ/`. `/tʃ/` ('church') and `/dʒ/` ('judge') are the two English affricates. `/ʃ/` ('ship') is common; `/ʒ/` ('measure', 'beige') is the rarest English consonant, occurring mostly medially and in loanwords.
- **Palatal:** `/j/` is the palatal glide as in 'yes'. It participates in yod-dropping/yod-coalescence differences between accents (e.g. 'tune' GA `[tuːn]` vs RP `[tjuːn]`).
- **Velar:** `/k ɡ ŋ/`. `/k/` is aspirated `[kʰ]` in stressed onsets ('key'). `/ŋ/` (as in 'sing') occurs only in syllable codas and never word-initially; in many varieties it is a positional realisation that contrasts with `/n/` and `/ŋ/` minimally ('sin' vs 'sing').
- **Glottal:** `/h/` as in 'hat'; voiceless glottal fricative, occurring only in onsets. The glottal stop `[ʔ]` is a frequent allophone (e.g. of coda `/t/`) but is not a separate phoneme of English.
- **Labial-velar:** `/w/` is the voiced labial-velar (rounded) approximant as in 'wet'. Some conservative varieties retain a contrasting voiceless `[ʍ]` in 'which', but this 'wine-whine' merger is complete in mainstream GA and RP, so `[ʍ]` is not counted as a separate phoneme.

### Vowel Phonemes

The vowel phonemes of Modern English, documented in parallel for General American (GA, rhotic) and Received Pronunciation (RP, non-rhotic), organised by reference to the Wells (1982) Standard Lexical Sets. This section covers the simple vowels (monophthongs, including GA r-coloured vowels and RP centring diphthongs counted as units); closing diphthongs (FACE, PRICE, CHOICE, GOAT, MOUTH) are enumerated in the separate diphthongs section.

**General American monophthong count:** 12 | **Received Pronunciation monophthong count:** 12  
GA monophthong count = 12: 9 plain oral monophthongs (FLEECE `/i/`, KIT `/ɪ/`, DRESS `/ɛ/`, TRAP/BATH `/æ/`, LOT/PALM `/ɑ/`, THOUGHT/CLOTH `/ɔ/`, FOOT `/ʊ/`, GOOSE `/u/`, STRUT `/ʌ/`) + the reduced commA `/ə/` (1) + the two r-coloured central vowels NURSE `/ɝ/` and lettER `/ɚ/` (2) = 12. The remaining historical-/r/ sets (START, NORTH, FORCE, NEAR, SQUARE, CURE) are realised in rhotic GA as vowel+/r/ sequences and are catalogued under r-coloured vowels rather than counted as separate monophthongs; cot-caught-merged speakers collapse `/ɑ/` and `/ɔ/`, reducing the oral set further. RP monophthong count = 12: 7 short (KIT `/ɪ/`, DRESS `/e/`, TRAP `/æ/`, LOT/CLOTH `/ɒ/`, STRUT `/ʌ/`, FOOT `/ʊ/`, commA/lettER `/ə/`) + 5 long (FLEECE `/iː/`, GOOSE `/uː/`, PALM/BATH/START `/ɑː/`, THOUGHT/NORTH/FORCE `/ɔː/`, NURSE `/ɜː/`) = 12. The conservative RP centring diphthongs NEAR `/ɪə/`, SQUARE `/eə~ɛː/` and CURE `/ʊə/` are enumerated in the separate diphthongs section, as are the five closing diphthongs FACE, PRICE, CHOICE, GOAT and MOUTH; counting the three RP centring diphthongs as additional simple-vowel units would give the often-cited RP total of 15 'pure-vowel-plus-centring' qualities. Rhoticity: GA pronounces historical /r/ in all positions, producing r-coloured vowels; RP is non-rhotic, dropping coda /r/ and instead lengthening or diphthongising the preceding vowel, with linking-/r/ and intrusive-/r/ surfacing before a following vowel. The Wells Standard Lexical Sets (KIT, DRESS, TRAP, LOT, STRUT, FOOT, BATH, CLOTH, NURSE, FLEECE, FACE, PALM, THOUGHT, GOAT, GOOSE, PRICE, CHOICE, MOUTH, NEAR, SQUARE, START, NORTH, FORCE, CURE, happY, lettER, commA) provide the accent-neutral keywords used throughout this guide.

#### General American Vowel Chart

IPA vowel quadrilateral for General American monophthongs (rows = height, columns = backness/rounding).

| Height | Front (unrounded) | Central | Back (rounded) |
|---|---|---|---|
| close | i |  | u |
| near-close | ɪ |  | ʊ |
| mid |  | ə / ɚ |  |
| open-mid | ɛ | ʌ / ɝ | ɔ |
| open | æ |  | ɑ |

#### Received Pronunciation Vowel Chart

IPA vowel quadrilateral for Received Pronunciation monophthongs (rows = height, columns = backness/rounding).

| Height | Front (unrounded) | Central | Back (rounded) |
|---|---|---|---|
| close | iː |  | uː |
| near-close | ɪ |  | ʊ |
| mid | e | ə / ɜː |  |
| open-mid |  | ʌ | ɔː / ɒ |
| open | æ |  | ɑː |

*GA distinguishes the rhotacised central vowels `/ɝ/` (stressed NURSE) and `/ɚ/` (unstressed lettER) which have no RP monophthong equivalents (RP uses `/ɜː/` and `/ə/` respectively). RP `/e/` (DRESS) is transcribed `/ɛ/` in GA. RP maintains a LOT `/ɒ/` vs THOUGHT `/ɔː/` vs PALM/START `/ɑː/` three-way contrast; GA has the cot-caught contrast variably (LOT/PALM `/ɑ/` vs THOUGHT `/ɔ/`), with many speakers merging them to `/ɑ/`. Length marks (ː) are phonemic-relevant in RP but largely predictable in GA, where quality differences carry the contrast.*

#### General American Monophthong Inventory

| IPA | Lexical Set | Height | Backness | Rounding | Example | Distribution |
|---|---|---|---|---|---|---|
| `/i/` | FLEECE | close | front | unrounded | fleece, see, machine | Also realises word-final unstressed happY in GA ('happy' `[ˈhæpi]`). |
| `/ɪ/` | KIT | near-close | front (near-front) | unrounded | kit, ship, bid | Short lax front vowel. |
| `/ɛ/` | DRESS | open-mid | front | unrounded | dress, bed, head | Short lax front mid vowel; RP equivalent transcribed `/e/`. |
| `/æ/` | TRAP / BATH | near-open | front | unrounded | trap, cat, bath, dance | GA has TRAP-BATH merger: 'bath', 'dance', 'laugh' all take `/æ/` (often raised/tensed `[eə]` before nasals). RP splits BATH off to `/ɑː/`. |
| `/ɑ/` | LOT / PALM | open | back | unrounded | lot, palm, father, spa | GA father-bother merger: LOT and PALM share `/ɑ/`. For cot-caught-merged speakers, THOUGHT also falls in here. |
| `/ɔ/` | THOUGHT / CLOTH | open-mid | back | rounded | thought, cloth, law, dog | GA lot-cloth split places CLOTH with THOUGHT `/ɔ/`. Increasingly merged with LOT `/ɑ/` (cot-caught merger) across North American varieties. |
| `/ʊ/` | FOOT | near-close | back (near-back) | rounded | foot, put, book | Short lax back rounded vowel. |
| `/u/` | GOOSE | close | back | rounded | goose, two, blue | Often fronted/centralised `[ʉ]` in contemporary GA, especially after coronals. |
| `/ʌ/` | STRUT | open-mid | central (back-central) | unrounded | strut, cup, blood | Stressed-syllable counterpart of unstressed `/ə/`; phonetically central in GA. |
| `/ə/` | commA | mid | central | unrounded | comma, about, sofa | The reduced (schwa) vowel; occurs only in unstressed syllables. Non-rhotacised counterpart of `/ɚ/`. |
| `/ɝ/` | NURSE | open-mid to mid | central | unrounded | nurse, bird, word | Stressed r-coloured (rhotacised) central vowel, may be transcribed `[ɚ]` or `[ɜɹ]`. RP equivalent is non-rhotic `/ɜː/`. |
| `/ɚ/` | lettER | mid | central | unrounded | letter, mother, standard | Unstressed r-coloured schwa; the rhotacised counterpart of `/ə/`. RP equivalent is non-rhotic `/ə/`. |

#### Received Pronunciation Monophthong Inventory

| IPA | Lexical Set | Height | Backness | Rounding | Example | Distribution |
|---|---|---|---|---|---|---|
| `/iː/` | FLEECE | close | front | unrounded | fleece, see, machine | Long close front vowel; may be slightly diphthongised `[ɪi]`. |
| `/ɪ/` | KIT | near-close | front (near-front) | unrounded | kit, ship, bid | Short lax front vowel. |
| `/e/` | DRESS | open-mid (mid) | front | unrounded | dress, bed, head | Short front mid vowel; transcribed `/e/` in RP, `/ɛ/` in GA. Phonetically often `[ɛ]`. |
| `/æ/` | TRAP | near-open (open in modern RP) | front | unrounded | trap, cat, man | Modern RP realises this quite open, approaching `[a]`. Excludes BATH words, which take `/ɑː/`. |
| `/ɒ/` | LOT / CLOTH | open | back | rounded | lot, dog, cloth | Short open back rounded vowel. RP keeps LOT distinct from THOUGHT and PALM (unlike GA). |
| `/ʌ/` | STRUT | open-mid | central | unrounded | strut, cup, blood | Open-mid central; historically backer `[ʌ]`, now central in RP. |
| `/ʊ/` | FOOT | near-close | back (near-back) | rounded | foot, put, book | Short lax back rounded vowel. |
| `/uː/` | GOOSE | close | back | rounded | goose, two, blue | Long close back rounded vowel; increasingly fronted `[ʉː]` in contemporary RP. |
| `/ɑː/` | PALM / BATH / START | open | back | unrounded | palm, father, bath, dance, start, car | Long open back unrounded vowel. RP TRAP-BATH split sends 'bath, dance, laugh' here. Non-rhotic START is also realised as `/ɑː/` (the /r/ is dropped). |
| `/ɔː/` | THOUGHT / NORTH / FORCE | open-mid (mid) | back | rounded | thought, law, north, force, war, more | Long mid back rounded vowel. RP has NORTH-FORCE merger, both realised as non-rhotic `/ɔː/`; THOUGHT shares the same quality. CURE words increasingly merge here too (CURE-FORCE merger). |
| `/ɜː/` | NURSE | open-mid to mid | central | unrounded | nurse, bird, word, fur | Long central unrounded vowel; the non-rhotic counterpart of GA `/ɝ/` (the historical /r/ is dropped). |
| `/ə/` | commA / lettER | mid | central | unrounded | comma, about, letter, mother | The reduced (schwa) vowel; in non-rhotic RP it covers both commA and lettER (the rhotacised GA `/ɚ/` collapses to plain `/ə/`). Occurs only in unstressed syllables. Word-final unstressed happY in modern RP is tense `[i]` (FLEECE quality, short) and is conventionally grouped with FLEECE rather than treated as a separate monophthong. |

#### R-Coloured Vowels

R-coloured (rhotacised) vowels and the historical-/r/ lexical sets. In rhotic GA these surface as r-coloured vowels or vowel+`[ɹ]` sequences with full `[ɹ]` articulation; in non-rhotic RP coda /r/ is dropped, leaving a long vowel or a centring diphthong, with /r/ reappearing only as linking/intrusive `[ɹ]` before a following vowel.

GA is rhotic: every historical /r/ is pronounced, yielding rhotacised vowels. RP is non-rhotic: coda /r/ is vocalised or lost. NEAR, SQUARE and CURE are centring diphthongs in conservative RP but plain vowel+/r/ sequences in GA. START, NORTH and FORCE merge into long monophthongs in RP.

| Lexical Set | GA | RP | Example | Notes |
|---|---|---|---|---|
| NURSE | `/ɝ/` | `/ɜː/` | nurse, bird, word, fur | Stressed central rhotacised vowel in GA; long central monophthong (non-rhotic) in RP. The fern-fir-fur merger means GA does not distinguish the three historical NURSE qualities. |
| lettER | `/ɚ/` | `/ə/` | letter, mother, standard, doctor | Unstressed rhotacised schwa in GA; plain schwa `/ə/` in non-rhotic RP. |
| START | `/ɑr/` (`ɑɹ`) | `/ɑː/` | start, car, far, hard, art | GA `/ɑr/` keeps the rhotic; RP merges to the long open back monophthong `/ɑː/` (shared with PALM/BATH). |
| NORTH | `/ɔr/` (`ɔɹ`) | `/ɔː/` | north, for, war, horse, short | Historically the 'short-o + r' set. GA `/ɔr/`; RP `/ɔː/`. NORTH and FORCE are merged in both mainstream GA and RP (horse-hoarse merger). |
| FORCE | `/ɔr/` (`ɔɹ`) / `oʊr` | `/ɔː/` | force, four, more, sport, hoarse | Historically the 'long-o + r' set. Merged with NORTH for most speakers; conservative GA may retain a distinct `[oʊr~oɹ]`. RP `/ɔː/`. |
| NEAR | `/ɪr/` (`ɪɹ`) | `/ɪə/` | near, here, beer, fear, idea | GA realises as `/ɪr/` (rhotic); RP as the centring diphthong `/ɪə/` (non-rhotic), increasingly monophthongised to `[ɪː]`. |
| SQUARE | `/ɛr/` (`ɛɹ`) | `/eə/` (`ɛː`) | square, fair, bear, there, care | GA `/ɛr/` (rhotic); conservative RP centring diphthong `/eə/`, in modern RP commonly a long monophthong `[ɛː]`. |
| CURE | `/ʊr/` (`ʊɹ`) | `/ʊə/` (`ɔː`) | cure, poor, tour, sure, lure | GA `/ʊr/` (rhotic); conservative RP centring diphthong `/ʊə/`, but the CURE-FORCE merger sends many words to `/ɔː/` in modern RP ('poor', 'sure' = `/pɔː/`, `/ʃɔː/`). |

## Consonants

The 24 consonant phonemes of Modern English, documented in parallel for two reference accents: GA (General American) and RP (Received Pronunciation / Standard Southern British English). Unlike vowels, the English consonant inventory is highly stable across the two accents, so each phoneme carries a single set of IPA, place, manner and voicing values; accent-specific and context-specific surface realisations are recorded in the allophony notes. Phonemic values are given in /slashes/ and phonetic realisations in [brackets], following IPA (2015 revision). Note that `/r/` is phonetically `[ɹ]` (a postalveolar/alveolar approximant) in most varieties, and that the rhotacised inventory differs between rhotic GA (which keeps coda `/r/`) and non-rhotic RP (which drops it).

**Consonant phonemes:** 24 | **Effective phonemes:** 24  
24 consonant letters/digraphs map cleanly to 24 phonemes; English consonant spelling is many-to-one (e.g. `/k/` written c, k, ck, q, ch) and one-to-many is rare, so the letter-to-phoneme ratio is essentially 1:1 at the phoneme level. The affricates `/tʃ/` and `/dʒ/` are treated as single phonemes. `/h/`, `/j/`, `/w/`, `/ŋ/` and (in non-rhotic accents) `/r/` are positionally restricted.

### Consonant Inventory

The 24 consonant phonemes with their IPA value, phonetic name, spelling graphemes, example words (with IPA), and allophony notes.

| # | IPA | Name | Spellings | Example Words | Allophony Notes |
|---|---|---|---|---|---|
| 1 | `/p/` | voiceless bilabial plosive | p, pp | pen `/pɛn/`; happy `/ˈhæpi/`; stop `/stɒp/` (RP), `/stɑp/` (GA) | Aspirated `[pʰ]` when syllable-initial in a stressed syllable (pin `[pʰɪn]`); unaspirated `[p]` after `/s/` (spin `[spɪn]`) and word-finally; often unreleased `[p̚]` in coda before a consonant or finally (top `[tɒp̚]`). RP and GA pattern alike. Word-finally `/p/` may be partly glottalised or pre-glottalised `[ʔp]` in many speakers. |
| 2 | `/b/` | voiced bilabial plosive | b, bb | bed `/bɛd/`; rabbit `/ˈræbɪt/`; web `/wɛb/` | Fully voiced `[b]` between voiced sounds; often devoiced `[b̥]` initially and finally (so 'web' may end in a partially devoiced stop). Distinction from `/p/` in coda is carried largely by preceding vowel length (the vowel is longer before `/b/`) rather than by voicing alone. Same in GA and RP. |
| 3 | `/t/` | voiceless alveolar plosive | t, tt, ed, th | ten `/tɛn/`; butter `/ˈbʌtər/` (GA `[ˈbʌɾɚ]`), `/ˈbʌtə/` (RP); cat `/kæt/` | Aspirated `[tʰ]` in stressed onsets (top `[tʰɒp]`); unaspirated after `/s/` (stop). GA: intervocalic `/t/` (and `/nt/`) flaps to a voiced alveolar tap `[ɾ]` when the following syllable is unstressed (water `[ˈwɔːɾɚ]`, better `[ˈbɛɾɚ]`); 'winter' may merge with 'winner'. RP: intervocalic `/t/` is usually a true `[t]`, but T-glottalling to `[ʔ]` is widespread coda-finally and before consonants (button `[ˈbʌʔn̩]`, not `[nɒʔ]`). Before `/n/` both accents allow nasal release/glottal stop. Often unreleased `[t̚]` word-finally. |
| 4 | `/d/` | voiced alveolar plosive | d, dd, ed | dog `/dɒɡ/` (RP), `/dɔɡ/`~`/dɑɡ/` (GA); ladder `/ˈlædər/` (GA `[ˈlæɾɚ]`), `/ˈlædə/` (RP); bad `/bæd/` | GA: intervocalic `/d/` also taps to `[ɾ]`, so 'latter' and 'ladder' can be homophones (`[ˈlæɾɚ]`). Often devoiced `[d̥]` initially and finally; the `/t/`–`/d/` contrast in coda is reinforced by vowel length (longer vowel before `/d/`). Dental `[d̪]` before `/θ ð/` (width `[wɪd̪θ]`). Same general pattern in RP minus the flapping. |
| 5 | `/k/` | voiceless velar plosive | c, k, ck, q, ch, cc | key `/kiː/`; school `/skuːl/`; back `/bæk/` | Aspirated `[kʰ]` in stressed onsets (cat `[kʰæt]`); unaspirated after `/s/` (skill). Fronted (more palatal) `[k̟]` before front vowels (key) and backed before back vowels (cool). Often unreleased `[k̚]` finally. RP shows some pre-glottalisation/glottal reinforcement of coda `/k/`; GA aspirates and may release. Same inventory in both accents. |
| 6 | `/ɡ/` | voiced velar plosive | g, gg, gh, gu | go `/ɡoʊ/` (GA), `/ɡəʊ/` (RP); bigger `/ˈbɪɡər/` (GA), `/ˈbɪɡə/` (RP); dog `/dɒɡ/` (RP), `/dɔɡ/`~`/dɑɡ/` (GA) | Fully voiced between voiced sounds; devoiced `[ɡ̊]` initially and finally. Fronted `[ɡ̟]` before front vowels (geese), backed before back vowels (goose). The `/k/`–`/ɡ/` coda contrast is cued by preceding vowel length. Pattern identical in GA and RP. |
| 7 | `/tʃ/` | voiceless postalveolar affricate | ch, tch, t (before u) | chair `/tʃɛər/` (GA `/tʃɛr/`); nature `/ˈneɪtʃər/` (GA), `/ˈneɪtʃə/` (RP); watch `/wɒtʃ/` (RP), `/wɑtʃ/` (GA) | A single phoneme: a stop closure released into a `[ʃ]`-like fricative, articulated with lip rounding. Pre-glottalisation/glottal reinforcement of coda `/tʃ/` occurs in both accents (RP especially). Yod-coalescence creates `/tʃ/` across word and morpheme boundaries in casual speech (did you `[ˈdɪdʒu]`, got you `[ˈɡɒtʃu]`; the `/t+j/` source). No flapping. Realised essentially the same in GA and RP. |
| 8 | `/dʒ/` | voiced postalveolar affricate | j, g (before e/i/y), dg, dge | jump `/dʒʌmp/`; giant `/ˈdʒaɪənt/`; bridge `/brɪdʒ/` | Single phoneme; voiced counterpart of `/tʃ/`, with lip rounding. Devoiced `[d̥ʒ̊]` initially and finally. Yod-coalescence yields `/dʒ/` across boundaries (would you `[ˈwʊdʒu]`) and word-internally in many words (soldier, gradual, education). Behaviour is shared by GA and RP. |
| 9 | `/f/` | voiceless labiodental fricative | f, ff, ph, gh | fine `/faɪn/`; phone `/foʊn/` (GA), `/fəʊn/` (RP); laugh `/læf/` (GA), `/lɑːf/` (RP) | Stable across accents; no aspiration or flapping. Some speakers (notably TH-fronting varieties of English, non-standard) merge `/θ/` into `/f/`, but in reference GA and RP `/f/` and `/θ/` stay distinct. The example 'laugh' shows the TRAP/BATH split (GA `/æ/` vs RP `/ɑː/`), not a difference in `/f/` itself. |
| 10 | `/v/` | voiced labiodental fricative | v, vv, f (of), ph (rare) | van `/væn/`; every `/ˈɛvəri/`~`/ˈɛvri/`; love `/lʌv/` | Fully voiced intervocalically; partially devoiced `[v̥]` word-finally (love). The preceding vowel is longer before `/v/` than before `/f/`, reinforcing the contrast in coda. Same in GA and RP. |
| 11 | `/θ/` | voiceless dental fricative | th | thin `/θɪn/`; nothing `/ˈnʌθɪŋ/`; bath `/bæθ/` (GA), `/bɑːθ/` (RP) | Interdental or denti-alveolar `[θ̪]`. In reference GA and RP it is a distinct fricative. Non-standard TH-fronting (London, some AAVE) realises it as `[f]`; TH-stopping (some New York, Irish, AAVE) realises it as `[t̪]`; these are not part of standard GA/RP but are widespread. Tongue tip touches or nears the upper teeth. |
| 12 | `/ð/` | voiced dental fricative | th | this `/ðɪs/`; mother `/ˈmʌðər/` (GA), `/ˈmʌðə/` (RP); breathe `/briːð/` | Voiced interdental fricative; often a weak fricative or even an approximant intervocalically, and may assimilate to a dental stop `[d̪]` after `/n/` or in function words in fast speech (and then `[ən̪d̪ən]`). Word-initial `/ð/` in function words (the, this, they) is highly frequent. Non-standard TH-stopping yields `[d]`. Distinct from `/θ/` by voicing; minimal pairs are few (thigh/thy, ether/either in some accents). |
| 13 | `/s/` | voiceless alveolar sibilant fricative | s, ss, c (before e/i/y), sc, x (=/ks/) | see `/siː/`; city `/ˈsɪti/`; miss `/mɪs/` | High-pitched grooved sibilant. Stable across accents. The plural/3rd-singular/possessive suffix surfaces as `/s/` after voiceless non-sibilants (cats `/kæts/`), as `/z/` after voiced sounds (dogs `/dɒɡz/`), and as `/ɪz/`~`/əz/` after sibilants (buses). Coalesces with following `/j/` to `/ʃ/` in casual speech (miss you `[ˈmɪʃu]`). |
| 14 | `/z/` | voiced alveolar sibilant fricative | z, zz, s (between vowels / plural), x (=/ɡz/) | zoo `/zuː/`; busy `/ˈbɪzi/`; buzz `/bʌz/` | Fully voiced intervocalically; partially devoiced `[z̥]` word-finally (buzz), where the contrast with `/s/` is supported by greater length of the preceding vowel. Coalesces with `/j/` to `/ʒ/` in fast speech (as you `[ˈæʒu]`, where's your `[ˈwɛəʒɔː]`). Same in GA and RP. |
| 15 | `/ʃ/` | voiceless postalveolar fricative | sh, ti (in -tion), ci, ss, ch (French loans), s (sugar) | she `/ʃiː/`; nation `/ˈneɪʃən/`; fish `/fɪʃ/` | Produced with lip rounding/protrusion. Arises historically and synchronically from `/s+j/` and `/sj/` coalescence (issue, pressure). Stable across GA and RP; no voicing or flapping alternation. Tongue body raised toward the postalveolar/palatal region. |
| 16 | `/ʒ/` | voiced postalveolar fricative | si (in -sion), s (measure), g (French loans), ge (beige), zh | measure `/ˈmɛʒər/` (GA), `/ˈmeʒə/` (RP); vision `/ˈvɪʒən/`; beige `/beɪʒ/` | The rarest English consonant and the most marginal: it occurs almost only medially in Latinate words (vision, pleasure, usual) and in French loans where it may be word-final (beige, rouge, garage). Word-initially it appears only in recent loans (genre `[ˈʒɒnrə]`). Many speakers substitute `/dʒ/` in final position (garage as `[ɡəˈrɑːʒ]` or `[ˈɡærɑːʒ]`/`[ɡəˈrɑːdʒ]`); GA and RP differ in such loanword stress and final-consonant choice but share the phoneme. |
| 17 | `/h/` | voiceless glottal fricative | h, wh (who), j (loans, rare) | hat `/hæt/`; ahead `/əˈhɛd/`; behind `/bɪˈhaɪnd/` | Positionally restricted: occurs only syllable-initially (onset), never in coda. Phonetically a voiceless transition that takes the tongue/lip posture of the following vowel (`[h]` before different vowels has different formants). Intervocalically it is often voiced `[ɦ]` (ahead). H-dropping (omission of `/h/` in lexical words) is common in many non-standard British accents but absent from reference RP and GA. Function words 'have/has/him/her' lose `/h/` when unstressed in both accents (give him `[ɡɪv ɪm]`). |
| 18 | `/m/` | voiced bilabial nasal | m, mm, mb (silent b), mn (silent n) | man `/mæn/`; hammer `/ˈhæmər/` (GA), `/ˈhæmə/` (RP); thumb `/θʌm/` | Can be syllabic `[m̩]` in some reduced contexts (rhythm `[ˈrɪðm̩]`, though `/əm/` is also heard). Assimilates to labiodental `[ɱ]` before `/f v/` (symphony `[ˈsɪɱfəni]`, comfort). Same in GA and RP. |
| 19 | `/n/` | voiced alveolar nasal | n, nn, kn (silent k), gn (silent g), pn (loans) | no `/noʊ/` (GA), `/nəʊ/` (RP); dinner `/ˈdɪnər/` (GA), `/ˈdɪnə/` (RP); ten `/tɛn/` | Frequently syllabic `[n̩]` after alveolars when an unstressed vowel is lost (button `[ˈbʌtn̩]`, sudden `[ˈsʌdn̩]`). Dental `[n̪]` before `/θ ð/` (tenth `[tɛn̪θ]`); assimilates in place to `[m]` before labials and `[ŋ]` before velars in casual speech (ten boys `[tɛm bɔɪz]`, ten girls `[tɛŋ ɡɜːlz]`). Same in GA and RP. |
| 20 | `/ŋ/` | voiced velar nasal | ng, n (before k/g), ngue (tongue) | sing `/sɪŋ/`; singer `/ˈsɪŋər/` (GA), `/ˈsɪŋə/` (RP); think `/θɪŋk/` | Positionally restricted: never occurs word-initially. Historically from `/nɡ/`; in RP and GA the `/ɡ/` is deleted after `/ŋ/` word-finally and before a morpheme boundary (sing `[sɪŋ]`, singer `[ˈsɪŋə]`, with no `[ɡ]`) but retained within a morpheme (finger `[ˈfɪŋɡə]`, longer `[ˈlɒŋɡə]`). Some northern/Midlands English and parts of GA (NYC, Philadelphia) keep `[ɡ]` (sing `[sɪŋɡ]`) — 'velar nasal plus'. The -ing suffix alternates with `[ɪn]` ('g-dropping', singin') in casual registers of both accents. `/ŋ/` before `/k/` is the regular nasal there (think `[θɪŋk]`). |
| 21 | `/l/` | voiced alveolar lateral approximant | l, ll | leaf `/liːf/`; yellow `/ˈjɛloʊ/` (GA), `/ˈjeləʊ/` (RP); ball `/bɔːl/` | Classic clear vs dark allophony. RP: clear `[l]` in onsets/before vowels (leaf `[liːf]`), dark (velarised) `[ɫ]` in codas and before consonants (ball `[bɔːɫ]`, milk `[mɪɫk]`). GA: dark `[ɫ]` in nearly all positions, including many onsets, so American `/l/` is generally darker throughout. Syllabic `[l̩]` after consonants where a vowel is lost (bottle `[ˈbɒtl̩]`, GA `[ˈbɑːɾl̩]`). In some accents (Cockney, some Estuary, parts of the US South) coda `/l/` vocalises to `[o]`/`[ʊ]` (milk `[mɪʊk]`); this is non-standard for reference RP/GA. Devoiced `[l̥]` after aspirated `/p k/` in clusters (please `[pl̥iːz]`, clean). |
| 22 | `/r/` | voiced alveolar/postalveolar approximant | r, rr, wr (silent w), rh | red `/rɛd/` (`[ɹɛd]`); very `/ˈvɛri/`; car `/kɑːr/` (GA `[kɑɹ]`), `/kɑː/` (RP, non-rhotic) | Phonemically `/r/` but phonetically `[ɹ]` (a voiced postalveolar/alveolar approximant) in both reference accents — the trilled `[r]` is not used. GA is commonly more retroflex/bunched `[ɻ]` and rhotic: coda and pre-consonantal `/r/` are pronounced (car `[kɑɹ]`, hard `[hɑɹd]`) and vowel+`/r/` may fuse into r-coloured `[ɚ]`/`[ɝ]` (butter `[ˈbʌɾɚ]`, bird `[bɝd]`). RP is non-rhotic: `/r/` occurs only before a vowel, so coda `/r/` is dropped (car `[kɑː]`, hard `[hɑːd]`) but reappears as linking-R before a following vowel (car alarm `[kɑːr əˈlɑːm]`) and as intrusive-R where no historic `/r/` exists (idea of `[aɪˈdɪər əv]`). Devoiced `[ɹ̥]` after aspirated `/p t k/` (try `[tɹ̥aɪ]`, pray); after `/t d/` it is often slightly affricated (tree ≈ `[tʃɹiː]`, dream ≈ `[dʒɹiːm]`). |
| 23 | `/j/` | voiced palatal approximant | y, i (before vowel), j (loans, rare), u (=/juː/) | yes `/jɛs/`; few `/fjuː/`; beyond `/bɪˈjɒnd/` (RP), `/bɪˈjɑnd/` (GA) | A glide that occurs only before a vowel (onset). The `/juː/` sequence (the 'long u' of cute, music, view) underlies major accent differences: yod-dropping in GA removes `/j/` after coronal consonants (tune `/tuːn/`, new `/nuː/`, due `/duː/`), whereas RP keeps it (tune `/tjuːn/`, new `/njuː/`, though RP also drops it after `/r/` and in clusters: rule `/ruːl/`). Yod-coalescence merges `/tj dj sj zj/` into `/tʃ dʒ ʃ ʒ/` (tune `[tʃuːn]`, dune `[dʒuːn]`) in both accents to varying degrees. Devoiced `[j̥]` after `/p k h/` (pure `[pj̥ʊə]`, huge `[çuːdʒ]` with `[ç]`). |
| 24 | `/w/` | voiced labial-velar approximant | w, wh, u (after q/g), o (one) | we `/wiː/`; queen `/kwiːn/`; away `/əˈweɪ/` | Doubly articulated (lip rounding + velar raising); occurs only before a vowel (onset). Devoiced `[w̥]` after aspirated `/t k/` (twice `[tw̥aɪs]`, quick `[kw̥ɪk]`). The 'wine/whine' distinction: conservative speakers and some GA (and Scottish/Irish) realise <wh> as a voiceless `[ʍ]` (whine `[ʍaɪn]`), but most modern GA and RP have merged <wh> into plain `/w/`, so wine = whine. `/w/` is restricted to onsets and the second element of clusters (`/sw tw kw dw ɡw/`). |

### Natural Classes

Groupings of the consonant phonemes by shared phonological features, drawn from the source data.

| Class | Members |
|---|---|
| Plosives | `/p/`, `/b/`, `/t/`, `/d/`, `/k/`, `/ɡ/` |
| Affricates | `/tʃ/`, `/dʒ/` |
| Fricatives | `/f/`, `/v/`, `/θ/`, `/ð/`, `/s/`, `/z/`, `/ʃ/`, `/ʒ/`, `/h/` |
| Nasals | `/m/`, `/n/`, `/ŋ/` |
| Approximants | `/l/`, `/r/`, `/j/`, `/w/` |
| Obstruents | `/p/`, `/b/`, `/t/`, `/d/`, `/k/`, `/ɡ/`, `/tʃ/`, `/dʒ/`, `/f/`, `/v/`, `/θ/`, `/ð/`, `/s/`, `/z/`, `/ʃ/`, `/ʒ/`, `/h/` |
| Sonorants | `/m/`, `/n/`, `/ŋ/`, `/l/`, `/r/`, `/j/`, `/w/` |
| Voiceless | `/p/`, `/t/`, `/k/`, `/tʃ/`, `/f/`, `/θ/`, `/s/`, `/ʃ/`, `/h/` |
| Voiced | `/b/`, `/d/`, `/ɡ/`, `/dʒ/`, `/v/`, `/ð/`, `/z/`, `/ʒ/`, `/m/`, `/n/`, `/ŋ/`, `/l/`, `/r/`, `/j/`, `/w/` |
| Sibilants | `/s/`, `/z/`, `/ʃ/`, `/ʒ/`, `/tʃ/`, `/dʒ/` |

## Vowels (Monophthongs)

The English monophthong (single-target vowel) inventory, organized by Wells (1982) Standard Lexical Sets. Two reference accents are documented in parallel, mirroring the Eastern/Western traditions of the Peshitta guide: GA = General American (rhotic) and RP = Received Pronunciation / Standard Southern British English (non-rhotic). Diphthongs (FACE, GOAT, PRICE, CHOICE, MOUTH and the centring NEAR, SQUARE, CURE) are treated in a separate section. This section covers the checked (lax) vowels, the free (tense/long) vowels including the historically /r/-coloured START/NORTH/FORCE/NURSE sets, and the weak (reduced, unstressable) vowels. All values are given in IPA (2015 revision); /slashes/ mark phonemic transcription and [brackets] mark phonetic detail. Length is marked with `/ː/` and primary stress with `/ˈ/`.

### Vowel Classes

English monophthongs fall into three traditional distributional classes. Checked (lax) vowels cannot end a stressed open syllable. Free (tense/long) vowels can occur in open syllables and are longer. Weak vowels are inherently unstressed and reduced.

| Class | Description | Lexical sets |
|---|---|---|
| Checked (lax) | Cannot end a stressed open syllable | KIT, DRESS, TRAP, LOT, STRUT, FOOT, BATH, CLOTH |
| Free (tense/long) | Can occur in open syllables; longer | NURSE, FLEECE, PALM, THOUGHT, GOOSE, START, NORTH, FORCE |
| Weak (reduced) | Inherently unstressed and reduced | commA, happY, lettER |

### Monophthong Inventory by Lexical Set

The monophthongs keyed to Wells's Standard Lexical Sets, with parallel GA and RP transcriptions. Where the two accents diverge, both keyword forms are shown.

| Set | Keyword | Class | GA | RP | Examples | Notes |
|---|---|---|---|---|---|---|
| KIT | kit | checked | `/ɪ/` | `/ɪ/` | ship `/ʃɪp/`, bid `/bɪd/`, myth `/mɪθ/` | Near-close near-front unrounded [ɪ]. Stable across GA and RP. Distinct from FLEECE `/iː/` (ship vs sheep). In weak syllables KIT frequently neutralises with commA toward [ɪ]~[ɨ]~[ə] (the 'weak vowel merger' in some accents, e.g. Australian; conservative RP keeps roses `/ˈrəʊzɪz/` vs Rosa's `/ˈrəʊzəz/`). |
| DRESS | dress | checked | `/ɛ/` | `/e/` | bed `/bɛd/`, head `/hɛd/`, many `/ˈmɛni/` | Open-mid to mid front unrounded vowel. Transcribed `/ɛ/` in GA descriptions and conventionally `/e/` in RP, though the phonetic quality is similar (open-mid [ɛ]); the RP `/e/` symbol is traditional, not a claim of cardinal close-mid quality. No length contrast; checked vowel. |
| TRAP | trap | checked | `/æ/` | `/æ/` | cat `/kæt/`, bad `/bæd/`, man `/mæn/` | Near-open front unrounded [æ]. Modern RP is often opener, approaching [a]. GA exhibits æ-tensing/raising before nasals and voiced stops ([eə]-like raising, e.g. 'man', 'bad'), which is allophonic in many accents but phonemic in the 'Mid-Atlantic split' (Philadelphia/New York). Key locus of the TRAP–BATH split: words like 'trap', 'cat', 'man' keep `/æ/` in BOTH accents; only the BATH subset diverges (see BATH). |
| LOT | lot | checked | `/ɑ/` | `/ɒ/` | stop `/stɑp/` (GA), `/stɒp/` (RP); rock `/rɑk/` (GA), `/rɒk/` (RP); wash `/wɑʃ/` (GA), `/wɒʃ/` (RP) | GA keyword `/lɑt/`; RP keyword `/lɒt/`. RP has a short open back ROUNDED vowel [ɒ]. GA is UNROUNDED and merges LOT with PALM as [ɑ(ː)] (the 'father–bother' merger: 'bother' rhymes with 'father'). Thus GA 'lot' `/lɑt/` has the same vowel as 'palm'; RP keeps LOT `/ɒ/` distinct from PALM `/ɑː/`. See CLOTH and THOUGHT for the GA cot–caught merger that further conditions this vowel. |
| STRUT | strut | checked | `/ʌ/` | `/ʌ/` | cup `/kʌp/`, blood `/blʌd/`, love `/lʌv/` | Conventionally `/ʌ/`; phonetically open-mid to open central-back unrounded, [ɐ]~[ʌ]. RP STRUT is fairly open and central [ɐ]; GA is often a bit backer. Result of the FOOT–STRUT split (17th c.), absent in northern England English where 'strut' and 'foot' share `/ʊ/`. Distinct from commA/STRUT only by stress: STRUT is the stressed counterpart, commA `/ə/` the unstressed. |
| FOOT | foot | checked | `/ʊ/` | `/ʊ/` | put `/pʊt/`, good `/ɡʊd/`, could `/kʊd/` | Near-close near-back rounded [ʊ], often weakly rounded and somewhat centralised in modern RP [ʊ̈]. Contrasts with GOOSE `/uː/` (foot vs food). Northern English English lacks the FOOT–STRUT split, so FOOT and STRUT both = `/ʊ/` there. A small, variable set of words wavers between FOOT and GOOSE (e.g. 'room', 'roof'). |
| BATH | bath | checked | `/æ/` | `/ɑː/` | staff `/stæf/` (GA), `/stɑːf/` (RP); dance `/dæns/` (GA), `/dɑːns/` (RP); grass `/ɡræs/` (GA), `/ɡrɑːs/` (RP) | GA keyword `/bæθ/`; RP keyword `/bɑːθ/`. THE TRAP–BATH SPLIT. This lexical set comprises words where RP (and southern England English, Australian, South African) has long back `/ɑː/` — the same vowel as PALM/START — while GA (and northern England English) retains short front `/æ/`, identical to TRAP. The split set is historically conditioned: pre-fricative /f, θ, s/ ('staff', 'path', 'pass') and pre-nasal-plus-consonant ('dance', 'plant', 'sample'). It is lexically irregular (e.g. RP 'pass' `/pɑːs/` but 'mass' `/mæs/`; 'cant' `/kɑːnt/` but 'romantic' `/æ/`). For GA, BATH = TRAP with no merger consequence; for RP, BATH = PALM/START. |
| CLOTH | cloth | checked | `/ɔ/` | `/ɒ/` | off `/ɔf/` (GA), `/ɒf/` (RP); dog `/dɔɡ/` (GA), `/dɒɡ/` (RP); long `/lɔŋ/` (GA), `/lɒŋ/` (RP) | GA keyword `/klɔθ/`; RP keyword `/klɒθ/`. Historically the subset of LOT words before voiceless fricatives /f, θ, s/ and before /ŋ/ ('off', 'cloth', 'loss', 'long'). In RP, CLOTH has merged BACK into LOT `/ɒ/` (the older RP 'lost' `/lɔːst/` is now archaic). In GA, CLOTH instead aligns with THOUGHT `/ɔ/`, so 'cloth', 'dog', 'off' have the THOUGHT vowel — except where the cot–caught merger neutralises THOUGHT and LOT entirely (see THOUGHT). Net: RP CLOTH = LOT; GA CLOTH = THOUGHT (and = LOT for merged speakers). |
| NURSE | nurse | free (rhotic) | `/ɝ/` | `/ɜː/` | bird `/bɝd/` (GA), `/bɜːd/` (RP); term `/tɝm/` (GA), `/tɜːm/` (RP); word `/wɝd/` (GA), `/wɜːd/` (RP) | GA keyword `/nɝs/`; RP keyword `/nɜːs/`. The stressed r-coloured vowel. GA realises it as a single rhotacised (r-coloured) mid central vowel [ɝ] = [ɜ˞], often analysed as syllabic `/ɹ̩/`. RP, being non-rhotic, has a plain long open-mid central unrounded vowel [ɜː] with no r-colouring; the historical /r/ surfaces only before a vowel (linking r). NURSE is the merger of Middle English /ɛr/, /ɪr/, /ʊr/ ('term', 'bird', 'word') into one vowel before /r/ (the 'fir–fur–fern merger'). Stressed counterpart of weak lettER. |
| FLEECE | fleece | free | `/i/` | `/iː/` | see `/si/` (GA), `/siː/` (RP); meat `/mit/` (GA), `/miːt/` (RP); key `/ki/` (GA), `/kiː/` (RP) | GA keyword `/flis/`; RP keyword `/fliːs/`. Close front unrounded, long [iː] in RP; GA is phonetically long but length is non-contrastive so often written `/i/`. Tense counterpart of KIT `/ɪ/` (sheep vs ship). May be slightly diphthongal [ɪi] in some accents. Result of the merger of Middle English /eː/ (FLEECE) and /ɛː/ (meat-words) — the 'meet–meat merger', complete in standard accents. |
| PALM | palm | free | `/ɑ/` | `/ɑː/` | father `/ˈfɑðɚ/` (GA), `/ˈfɑːðə/` (RP); spa `/spɑ/` (GA), `/spɑː/` (RP); calm `/kɑm/` (GA), `/kɑːm/` (RP) | GA keyword `/pɑm/`; RP keyword `/pɑːm/`. Open back (to central) unrounded vowel, long [ɑː] in RP. In GA, PALM is merged with LOT as unrounded [ɑ] (father–bother merger), so GA 'palm' and 'lot' share a vowel; length is non-contrastive in GA. In RP, PALM `/ɑː/` is the same vowel as START (non-rhotic) and as the RP BATH subset, but distinct from short rounded LOT `/ɒ/`. The historic /l/ in 'palm', 'calm' is usually silent. |
| THOUGHT | thought | free | `/ɔ/` | `/ɔː/` | law `/lɔ/` (GA), `/lɔː/` (RP); caught `/kɔt/` (GA), `/kɔːt/` (RP); all `/ɔl/` (GA), `/ɔːl/` (RP) | GA keyword `/θɔt/`; RP keyword `/θɔːt/`. Open-mid back rounded, long [ɔː] in RP (often raised toward [oː] in modern RP). THE COT–CAUGHT (LOT–THOUGHT) MERGER: in much of GA — the western US, much of the inland/midland, and Canada generally — THOUGHT has merged with LOT/PALM into [ɑ]~[ɒ], so 'cot' and 'caught', 'stock' and 'stalk' are homophones. Conservative/eastern GA and RP keep THOUGHT `/ɔ(ː)/` distinct from LOT. GA CLOTH also falls together with THOUGHT (see CLOTH). RP THOUGHT additionally absorbs many words of the older NORTH/FORCE and CURE sets. |
| GOOSE | goose | free | `/u/` | `/uː/` | two `/tu/` (GA), `/tuː/` (RP); blue `/blu/` (GA), `/bluː/` (RP); food `/fud/` (GA), `/fuːd/` (RP) | GA keyword `/ɡus/`; RP keyword `/ɡuːs/`. Historically close back rounded long [uː], the tense counterpart of FOOT `/ʊ/` (food vs foot). Now strongly FRONTED in both modern RP and much of GA, to central [ʉː] or even front [yː]-like quality, especially after coronals and between palatals ('goose' [ɡʉːs]). Fronting is blocked/reduced before dark /l/ ('pool'). After /j/ (FEW/CURE-type onsets) the sequence `/juː/` may show yod-dropping in GA ('new' GA `/nu/` vs RP `/njuː/`). |
| START | start | free (rhotic) | `/ɑr/` | `/ɑː/` | car `/kɑr/` (GA), `/kɑː/` (RP); hard `/hɑrd/` (GA), `/hɑːd/` (RP); far `/fɑr/` (GA), `/fɑː/` (RP) | GA keyword `/stɑrt/`; RP keyword `/stɑːt/`. Historic /ɑ/ + /r/. RHOTICITY CONTRAST: rhotic GA pronounces the /r/ as [ɹ] (or r-colours the vowel: [ɑɹ]~[ɑ˞]), while non-rhotic RP drops coda /r/, leaving a plain long [ɑː] — identical in quality to RP PALM (so RP 'spa' and 'spar' can be homophones, and 'father' rhymes with 'starter'). In RP the /r/ resurfaces as linking/intrusive r before a following vowel ('far away' [fɑːr əˈweɪ]). |
| NORTH | north | free (rhotic) | `/ɔr/` | `/ɔː/` | for `/fɔr/` (GA), `/fɔː/` (RP); horse `/hɔrs/` (GA), `/hɔːs/` (RP); war `/wɔr/` (GA), `/wɔː/` (RP) | GA keyword `/nɔrθ/`; RP keyword `/nɔːθ/`. Historic /ɔ/ + /r/. GA: open-mid/close-mid back rounded vowel plus [ɹ], [ɔɹ]~[oɹ]. RP: non-rhotic long [ɔː], merged with THOUGHT (so RP 'caught', 'court', 'north' share `/ɔː/`). THE HORSE–HOARSE (NORTH–FORCE) MERGER: in nearly all modern GA and RP, NORTH and FORCE are merged, so 'horse'='hoarse', 'for'='four', 'war'='wore'. A few conservative accents (some Scottish, Irish, US Southern, Caribbean) keep NORTH (open [ɔ]) distinct from FORCE (closer [o]). |
| FORCE | force | free (rhotic) | `/ɔr/` | `/ɔː/` | four `/fɔr/` (GA), `/fɔː/` (RP); more `/mɔr/` (GA), `/mɔː/` (RP); hoarse `/hɔrs/` (GA), `/hɔːs/` (RP) | GA keyword `/fɔrs/`; RP keyword `/fɔːs/`. Historic /o/ + /r/. For the vast majority of GA and RP speakers FORCE is identical to NORTH owing to the completed NORTH–FORCE (horse–hoarse) merger: GA `/ɔr/`~[oɹ], RP `/ɔː/` (also merged with THOUGHT). Where the distinction survives, FORCE has a closer vowel ([oɹ] / [oə]) than NORTH ([ɔɹ] / [ɔə]). Listed separately from NORTH per Wells's lexical-set framework even though the two are merged in the reference accents. |
| commA | comma | weak | `/ə/` | `/ə/` | about `/əˈbaʊt/`; sofa `/ˈsoʊfə/` (GA), `/ˈsəʊfə/` (RP); banana `/bəˈnænə/` | GA keyword `/ˈkɑmə/`; RP keyword `/ˈkɒmə/`. Schwa: the unstressed mid central unrounded vowel [ə], the default reduction vowel of English. Occurs only in UNSTRESSED syllables and cannot bear stress; it is the weak/reduced counterpart of STRUT `/ʌ/` (and of many full vowels). Word-finally written as 'a' in 'comma', 'sofa', 'data'. In GA, non-final schwa is non-rhotic but the r-coloured weak vowel is lettER (see below). The commA–lettER distinction in GA is exactly schwa [ə] vs r-coloured schwa [ɚ]. |
| happY | happy | weak | `/i/` | `/i/` | city `/ˈsɪti/`; coffee `/ˈkɔfi/` (GA), `/ˈkɒfi/` (RP); very `/ˈvɛri/` | Keyword `/ˈhæpi/`. The weak unstressed front vowel in word-final position ('happy', 'city', 'coffee'). HAPPY-TENSING: in modern GA, modern (younger) RP, Australian, etc., it is realised as a tense close [i], close to FLEECE; written `/i/` (length-neutral) to distinguish it from both full FLEECE `/iː/` and lax KIT `/ɪ/`. Conservative/older RP used lax [ɪ] here ('happy' `/ˈhæpɪ/`). It is unstressable and so patterns with the weak vowels. |
| lettER | letter | weak (rhotic) | `/ɚ/` | `/ə/` | father `/ˈfɑðɚ/` (GA), `/ˈfɑːðə/` (RP); doctor `/ˈdɑktɚ/` (GA), `/ˈdɒktə/` (RP); standard `/ˈstændɚd/` (GA), `/ˈstændəd/` (RP) | GA keyword `/ˈlɛtɚ/`; RP keyword `/ˈlɛtə/`. The unstressed r-coloured central vowel. RHOTICITY CONTRAST: rhotic GA has r-coloured schwa [ɚ] = [ə˞] (often analysed as syllabic `/ɚ/`~`/ɹ̩/`), whereas non-rhotic RP simply has plain schwa [ə] — so in RP lettER and commA are IDENTICAL ([ə]), while GA keeps them distinct ([ɚ] vs [ə]). lettER is the unstressed counterpart of stressed NURSE (GA `/ɝ/` : `/ɚ/` :: RP `/ɜː/` : `/ə/`). In RP the historical /r/ may surface as linking/intrusive r before a vowel ('letter of' [ˈletər əv]). |

### Key Mergers and Splits

Cross-cutting historical and synchronic phenomena that reshape the monophthong inventory differently in GA and RP. Each entry names the affected Wells sets.

#### TRAP–BATH Split

- **Sets:** TRAP, BATH
- **GA:** No split: BATH = TRAP = `/æ/`.
- **RP:** Split: BATH = PALM/START = `/ɑː/`, distinct from TRAP `/æ/`.
- **Conditioning:** Pre-fricative /f θ s/ and pre-nasal-cluster environments; lexically irregular.
- **Example:** trap `/træp/` vs bath — RP `/bɑːθ/`, GA `/bæθ/`.

#### Father–Bother Merger

- **Sets:** PALM, LOT
- **GA:** Merged: PALM = LOT = unrounded `/ɑ/` ('father' rhymes with 'bother').
- **RP:** Distinct: PALM `/ɑː/` (long, unrounded) vs LOT `/ɒ/` (short, rounded).
- **Example:** GA palm `/pɑm/` and lot `/lɑt/` share the vowel; RP lot `/lɒt/`.

#### Cot–Caught Merger

- **Sets:** LOT, THOUGHT, CLOTH, PALM
- **GA:** Merged in much of GA (Western US, Canada, much of the Midland): THOUGHT = LOT = PALM = [ɑ]~[ɒ]; 'cot'='caught', 'stock'='stalk'. Eastern/conservative GA keeps them apart.
- **RP:** Not merged: THOUGHT `/ɔː/` remains distinct from LOT `/ɒ/`.
- **Example:** cot `/kɑt/`; caught (merged) `/kɑt/`; caught (unmerged GA) `/kɔt/`; caught (RP) `/kɔːt/`.

#### LOT–CLOTH–THOUGHT Relationship

CLOTH is the historic pre-voiceless-fricative / pre-/ŋ/ subset of LOT. In RP it merged back into LOT (CLOTH = LOT = `/ɒ/`). In GA it instead aligns with THOUGHT (CLOTH = THOUGHT = `/ɔ/`), and for cot–caught-merged GA speakers all three (LOT, CLOTH, THOUGHT) coincide as [ɑ].

| Set | GA | RP |
|---|---|---|
| LOT | `/ɑ/` | `/ɒ/` |
| CLOTH | `/ɔ/` | `/ɒ/` |
| THOUGHT | `/ɔ/` | `/ɔː/` |

#### FOOT–STRUT Split

- **Sets:** FOOT, STRUT
- **Standard:** Split present in GA and RP: FOOT `/ʊ/` vs STRUT `/ʌ/` ('put' vs 'putt').
- **Absent in:** Northern England English, where FOOT = STRUT = `/ʊ/`.
- **Example:** foot `/fʊt/` vs strut `/strʌt/`.

#### NURSE Merger and Rhoticity

- **Sets:** NURSE, lettER
- Stressed NURSE: GA r-coloured `/ɝ/` (= [ɜ˞], syllabic [ɹ̩]) vs RP plain long `/ɜː/`. Unstressed lettER: GA r-coloured `/ɚ/` vs RP plain `/ə/`. RP non-rhoticity makes lettER and commA identical ([ə]); GA rhoticity keeps lettER ([ɚ]) distinct from commA ([ə]).
- **Example:** nurse — GA `/nɝs/`, RP `/nɜːs/`; letter — GA `/ˈlɛtɚ/`, RP `/ˈlɛtə/`.

#### NORTH–FORCE Merger

- **Sets:** NORTH, FORCE
- **GA:** Merged: NORTH = FORCE = `/ɔr/`~[oɹ] ('horse'='hoarse', 'for'='four').
- **RP:** Merged: NORTH = FORCE = `/ɔː/` (and further merged with THOUGHT).
- **Retained in:** Some Scottish, Irish, US Southern, and Caribbean varieties.
- **Example:** horse `/hɔrs/` = hoarse `/hɔrs/`.

### Rhoticity Overview

GA is rhotic: historical coda /r/ is pronounced as [ɹ] (or as r-colouring on the preceding vowel). RP is non-rhotic: coda /r/ is lost, leaving a long or centring vowel, but /r/ resurfaces prevocalically as linking r ('far away') and is added by analogy as intrusive r ('idea-r-of').

The r-coloured sets are NURSE, START, NORTH, FORCE, and lettER.

| Context | GA symbol | RP outcome |
|---|---|---|
| Stressed (NURSE) | `/ɝ/` | `/ɜː/` |
| Unstressed (lettER) | `/ɚ/` | `/ə/` |
| START | `/ɑr/` | `/ɑː/` |
| NORTH / FORCE | `/ɔr/` | `/ɔː/` |
| After vowel (general) | `/r/` ([ɹ]) | (lost; linking/intrusive r prevocalically) |

*Centring-diphthong sets NEAR, SQUARE, CURE are also r-affected but are diphthongs and treated in the diphthongs section.*

### Weak Vowels Overview

Weak (reduced) vowels occur only in unstressed syllables and cannot carry lexical stress. They are the targets of vowel reduction.

| Set | GA | RP | Note |
|---|---|---|---|
| commA | `/ə/` | `/ə/` | Schwa; the default reduction vowel. |
| happY | `/i/` | `/i/` | Tense weak front vowel (happy-tensing); older RP `/ɪ/`. |
| lettER | `/ɚ/` | `/ə/` | R-coloured schwa in rhotic GA; plain schwa in non-rhotic RP. |

*Many accents also have a weak `/u/`~`/ʊ/` ('influence') and a weak `/ɪ/` vs `/ə/` contrast ('roses' `/ˈrəʊzɪz/` vs 'Rosa's' `/ˈrəʊzəz/`); accents with the weak-vowel merger collapse the latter to `/ə/`.*

### IPA Symbol Summary

Quick reference of the monophthong phonemes by accent.

| Accent | Monophthong phonemes |
|---|---|
| GA | `/ɪ/`, `/ɛ/`, `/æ/`, `/ɑ/`, `/ʌ/`, `/ʊ/`, `/ɔ/`, `/ɝ/`, `/i/`, `/u/`, `/ɚ/`, `/ə/`, `/ɑr/`, `/ɔr/` |
| RP | `/ɪ/`, `/e/`, `/æ/`, `/ɒ/`, `/ʌ/`, `/ʊ/`, `/ɑː/`, `/ɔː/`, `/ɜː/`, `/iː/`, `/uː/`, `/i/`, `/ə/` |

*GA r-coloured `/ɝ ɚ/` and the sequences `/ɑr ɔr/` correspond to RP's plain long vowels `/ɜː ɑː ɔː/` plus loss of coda /r/. The RP `/i/` listed here is the length-neutral weak happY vowel (happy-tensing), distinct from full FLEECE `/iː/`.*

## Diphthongs

English diphthongs are vowels that glide from one quality to another within a single syllable, organized here by Wells (1982) Standard Lexical Sets. Two broad types exist: CLOSING diphthongs, which glide toward a higher (closer) tongue position ending in a `[ɪ]`/`[i]`-like or `[ʊ]`/`[u]`-like offglide, and CENTRING diphthongs, which glide toward the central schwa `[ə]`. The five closing diphthongs (FACE, PRICE, CHOICE, GOAT, MOUTH) are shared by both reference accents, though their precise starting points and the GOAT onset differ between General American (GA) and Received Pronunciation (RP). The centring diphthongs (NEAR, SQUARE, CURE) are a property of non-rhotic RP, where historical /r/ after a vowel was lost and left a schwa offglide; in rhotic GA these same lexical sets are realized as a vowel plus the consonant /r/ (`[ɪr]`, `[ɛr]`, `[ʊr]`) rather than as true diphthongs. Diphthongs are phonemically single units; the offglide is not a separate consonant.

| Lexical Set | GA | RP | Type | Example Words | Notes |
|---|---|---|---|---|---|
| FACE | `/eɪ/` | `/eɪ/` | closing | `face /feɪs/`, `day /deɪ/`, `rain /reɪn/` | Close-mid-to-close front closing diphthong; starts near cardinal `[e]` and glides up toward `[ɪ]`. |
| PRICE | `/aɪ/` | `/aɪ/` | closing | `price /praɪs/`, `my /maɪ/`, `light /laɪt/` | Open-to-close closing diphthong; starts at an open central/front `[a]` and glides up toward `[ɪ]`. |
| CHOICE | `/ɔɪ/` | `/ɔɪ/` | closing | `choice /tʃɔɪs/`, `boy /bɔɪ/`, `noise /nɔɪz/` | Open-mid-back-to-close closing diphthong; starts at rounded `[ɔ]` and glides up and forward toward `[ɪ]`. |
| GOAT | `/oʊ/` | `/əʊ/` | closing | `goat /ɡoʊt/ (GA), /ɡəʊt/ (RP)`, `go /ɡoʊ/ (GA), /ɡəʊ/ (RP)`, `boat /boʊt/ (GA), /bəʊt/ (RP)` | Mid-back-to-close-back closing diphthong; the principal point of GA-vs-RP divergence among the closing diphthongs. |
| MOUTH | `/aʊ/` | `/aʊ/` | closing | `mouth /maʊθ/`, `now /naʊ/`, `loud /laʊd/` | Open-to-close-back closing diphthong; starts at open `[a]` and glides up and back toward `[ʊ]`. |
| NEAR | `/ɪr/` | `/ɪə/` | centring | `near /nɪə/ (RP), /nɪr/ (GA)`, `here /hɪə/ (RP), /hɪr/ (GA)`, `beard /bɪəd/ (RP), /bɪrd/ (GA)` | Centring diphthong in non-rhotic RP, gliding from near-close front `[ɪ]` to schwa `[ə]`; realized as vowel + /r/ in rhotic GA. |
| SQUARE | `/ɛr/` | `/eə/` | centring | `square /skweə/ (RP), /skwɛr/ (GA)`, `fair /feə/ (RP), /fɛr/ (GA)`, `bear /beə/ (RP), /bɛr/ (GA)` | Centring diphthong in non-rhotic RP, gliding from open-mid/mid front `[ɛ]` to schwa `[ə]`; realized as vowel + /r/ in rhotic GA. |
| CURE | `/ʊr/` | `/ʊə/` | centring | `cure /kjʊə/ (RP), /kjʊr/ (GA)`, `tour /tʊə/ (RP), /tʊr/ (GA)`, `pure /pjʊə/ (RP), /pjʊr/ (GA)` | Centring diphthong in non-rhotic RP, gliding from near-close back `[ʊ]` to schwa `[ə]`; realized as vowel + /r/ in rhotic GA. |

### Detailed Notes

- **FACE** — Broadly identical in GA and RP as `/eɪ/`. The onset is somewhat opener and more centralized in some broad RP and Australian/Cockney varieties (toward `[ʌɪ]`/`[æɪ]`), but Standard Southern British and General American share the close-mid onset. Historically descends from Middle English long /aː/ via the Great Vowel Shift. In some regional/conservative accents (e.g. Scottish English, Northern England, Caribbean) FACE may be monophthongized to a long `[eː]`.
- **PRICE** — Transcribed `/aɪ/` in both accents. The onset quality varies (more central `[ɐ]` in RP, slightly fronter in some GA). In many North American accents PRICE undergoes 'Canadian raising' before voiceless consonants, surfacing as `[ʌɪ]`/`[ɐɪ]` (e.g. 'write' `[ɹʌɪt]` vs 'ride' `[ɹaɪd]`). In US Southern English and African American Vernacular English PRICE is frequently monophthongized to `[aː]` ('time' `[taːm]`), especially before voiced segments and word-finally.
- **CHOICE** — Stable as `/ɔɪ/` across GA and RP; the only English diphthong with a rounded, back onset. The onset may be slightly closer (toward `[oɪ]`) in some RP speakers. CHOICE is the least variable of the closing diphthongs and is essentially never monophthongized in mainstream accents. It originates largely from Old French and Latinate loanwords.
- **GOAT** — The signature transatlantic difference: GA has a back rounded onset `/oʊ/` (close-mid back), whereas modern RP has a central unrounded onset `/əʊ/` (schwa gliding to `[ʊ]`). Older RP and many other accents used `[oʊ]`; the centralized RP onset is a 20th-century development. Before dark /l/, RP shows GOAT-allophony toward `[ɒʊ]` ('goal'). Conservative/regional accents (Northern England, Scotland, Wales, parts of the US Upper Midwest) often monophthongize GOAT to a long `[oː]`. This set is also called GOAT in Wells's terminology after the keyword.
- **MOUTH** — Transcribed `/aʊ/` in both accents. The onset is typically open central `[a]` but is notably fronted toward `[æ]` in much of GA and in broad RP/Estuary, and raised before voiceless consonants ('Canadian raising': 'house' noun `[hʌʊs]` vs 'house' verb `[haʊz]`) in Canadian and some Northern US English. US Southern and some regional accents may front and monophthongize the onset toward `[æː]`. Together with PRICE, MOUTH is one of the two diphthongs with an open onset.
- **NEAR** — A true centring diphthong only in non-rhotic RP, where post-vocalic historical /r/ was lost and left a schwa offglide; GA, being rhotic, keeps the /r/ and so has no diphthong here (the sequence is vowel + consonant /r/, phonetically an r-coloured `[ɪɹ]`). In contemporary RP, NEAR is increasingly realized as a long monophthong `[ɪː]` (smoothing) when not phrase-final. A linking/intrusive `[r]` reappears before a following vowel even in non-rhotic RP ('here is' `[hɪər ɪz]`).
- **SQUARE** — Centring `/eə/` in non-rhotic RP (the onset is the RP DRESS vowel /e/, phonetically often `[ɛ]`), but in present-day RP SQUARE has very commonly monophthongized to a long open-mid `[ɛː]` (sometimes transcribed `/eː/`), so 'square' may be heard as `[skwɛː]`; this is the most advanced of the RP centring monophthongizations. Rhotic GA realizes the set as vowel + /r/ `[ɛr]` (r-coloured `[ɛɹ]`), with no diphthong or monophthong distinction. Linking/intrusive `[r]` applies in RP before a vowel ('fair enough' `[feər ɪˈnʌf]`).
- **CURE** — The least stable centring diphthong. In non-rhotic RP, CURE `/ʊə/` is widely undergoing merger into the THOUGHT vowel /ɔː/ (the 'CURE-FORCE merger' / 'pour-poor merger'), so 'cure' is increasingly `[kjɔː]` and 'poor' = 'pour' `[pɔː]` for many RP speakers; the older `[ʊə]` survives chiefly after /j/ and in less common words. Rhotic GA keeps vowel + /r/ `[ʊr]` (r-coloured `[ʊɹ]`); GA also has a parallel tendency for some CURE words to shift toward the NORTH/FORCE vowel before /r/. Linking/intrusive `[r]` applies in RP before a following vowel.

*English distinguishes CLOSING diphthongs (FACE `/eɪ/`, PRICE `/aɪ/`, CHOICE `/ɔɪ/`, GOAT `/oʊ~əʊ/`, MOUTH `/aʊ/`), which glide toward a higher tongue position, from CENTRING diphthongs (NEAR `/ɪə/`, SQUARE `/eə/`, CURE `/ʊə/`), which glide toward central schwa. The centring diphthongs exist as true diphthongs only in NON-RHOTIC accents such as RP; in RHOTIC General American the same lexical sets are sequences of a vowel plus the consonant /r/ (`/ɪr/`, `/ɛr/`, `/ʊr/`), realized as r-coloured vowels rather than diphthongs. The principal closing-diphthong difference between the reference accents is GOAT, which has a back rounded onset `/oʊ/` in GA but a central unrounded onset `/əʊ/` in RP. Across many regional and conservative accents (Scottish, Northern English, Welsh, US Southern, African American Vernacular English, Caribbean), several diphthongs MONOPHTHONGIZE: FACE and GOAT to long `[eː]` and `[oː]`, PRICE and MOUTH to long `[aː]`/`[æː]`, and in RP the centring diphthongs SQUARE to `[ɛː]` and NEAR to `[ɪː]` by smoothing, with CURE frequently merging into /ɔː/.*

## Consonant–Vowel IPA Matrix

Systematic consonant + vowel (CV) IPA combination matrix for all 24 English consonant phonemes paired with a representative 8-vowel set. Each cell gives the phonemic IPA string for the consonant followed by the reference monophthong. Combinations are phonemic transcriptions; consult each consonant's phonetic note for the principal allophonic realizations (aspiration, flapping, devoicing, clear/dark /l/, etc.) that surface in actual CV syllables. The matrix is symmetrical and exhaustive (24 consonants × 8 vowels = 192 combinations); some cells (e.g. ŋ- onsets) are phonotactically unattested word-initially in English and are listed for systematic completeness only.

- **Reference accent:** General American
- **Secondary reference accent:** Received Pronunciation (Standard Southern British English)
- **Transcription level:** phonemic

### Reference Vowels

The eight reference monophthongs used as columns in the matrix, keyed to Wells lexical sets. Vowel qualities use General American (GA) values.

| Vowel | Lexical Set | Example | Note |
|---|---|---|---|
| i | FLEECE | fleece `/fliːs/` | close front unrounded; phonetically long/diphthongal [iː~ɪi] in GA. |
| ɪ | KIT | kit `/kɪt/` | near-close near-front unrounded (lax). |
| ɛ | DRESS | dress `/drɛs/` | open-mid front unrounded (lax). |
| æ | TRAP | trap `/træp/` | near-open front unrounded; GA often raised/tense [eə] before nasals. |
| ɑ | PALM/LOT | palm `/pɑːm/`, lot `/lɑt/` | open back unrounded; GA merges LOT/PALM as /ɑ/ (RP LOT is rounded /ɒ/). |
| ʌ | STRUT | strut `/strʌt/` | traditionally open-mid back unrounded; in modern GA realized more centrally, approaching [ɐ]. |
| u | GOOSE | goose `/ɡuːs/` | close back rounded; GA often fronted/diphthongal [ʉu]. |
| ə | commA | comma `/ˈkɑmə/` | mid-central unstressed schwa. |

### CV Matrix

Each cell gives the phonemic consonant + vowel sequence. Columns are the eight reference monophthongs; the **Base IPA** column gives the consonant phoneme on its own.

| Consonant | Name | Example | Base IPA | i | ɪ | ɛ | æ | ɑ | ʌ | u | ə |
|---|---|---|---|---|---|---|---|---|---|---|---|
| p | voiceless bilabial plosive | pat `/pæt/` | p | pi | pɪ | pɛ | pæ | pɑ | pʌ | pu | pə |
| b | voiced bilabial plosive | bat `/bæt/` | b | bi | bɪ | bɛ | bæ | bɑ | bʌ | bu | bə |
| t | voiceless alveolar plosive | tap `/tæp/` | t | ti | tɪ | tɛ | tæ | tɑ | tʌ | tu | tə |
| d | voiced alveolar plosive | dab `/dæb/` | d | di | dɪ | dɛ | dæ | dɑ | dʌ | du | də |
| k | voiceless velar plosive | cat `/kæt/` | k | ki | kɪ | kɛ | kæ | kɑ | kʌ | ku | kə |
| ɡ | voiced velar plosive | gap `/ɡæp/` | ɡ | ɡi | ɡɪ | ɡɛ | ɡæ | ɡɑ | ɡʌ | ɡu | ɡə |
| tʃ | voiceless postalveolar affricate | chat `/tʃæt/` | tʃ | tʃi | tʃɪ | tʃɛ | tʃæ | tʃɑ | tʃʌ | tʃu | tʃə |
| dʒ | voiced postalveolar affricate | jam `/dʒæm/` | dʒ | dʒi | dʒɪ | dʒɛ | dʒæ | dʒɑ | dʒʌ | dʒu | dʒə |
| f | voiceless labiodental fricative | fan `/fæn/` | f | fi | fɪ | fɛ | fæ | fɑ | fʌ | fu | fə |
| v | voiced labiodental fricative | van `/væn/` | v | vi | vɪ | vɛ | væ | vɑ | vʌ | vu | və |
| θ | voiceless dental fricative | thin `/θɪn/` | θ | θi | θɪ | θɛ | θæ | θɑ | θʌ | θu | θə |
| ð | voiced dental fricative | this `/ðɪs/` | ð | ði | ðɪ | ðɛ | ðæ | ðɑ | ðʌ | ðu | ðə |
| s | voiceless alveolar sibilant fricative | sap `/sæp/` | s | si | sɪ | sɛ | sæ | sɑ | sʌ | su | sə |
| z | voiced alveolar sibilant fricative | zap `/zæp/` | z | zi | zɪ | zɛ | zæ | zɑ | zʌ | zu | zə |
| ʃ | voiceless postalveolar sibilant fricative | ship `/ʃɪp/` | ʃ | ʃi | ʃɪ | ʃɛ | ʃæ | ʃɑ | ʃʌ | ʃu | ʃə |
| ʒ | voiced postalveolar sibilant fricative | vision `/ˈvɪʒən/` | ʒ | ʒi | ʒɪ | ʒɛ | ʒæ | ʒɑ | ʒʌ | ʒu | ʒə |
| h | voiceless glottal fricative | hat `/hæt/` | h | hi | hɪ | hɛ | hæ | hɑ | hʌ | hu | hə |
| m | voiced bilabial nasal | mat `/mæt/` | m | mi | mɪ | mɛ | mæ | mɑ | mʌ | mu | mə |
| n | voiced alveolar nasal | nap `/næp/` | n | ni | nɪ | nɛ | næ | nɑ | nʌ | nu | nə |
| ŋ | voiced velar nasal | sing `/sɪŋ/` | ŋ | ŋi | ŋɪ | ŋɛ | ŋæ | ŋɑ | ŋʌ | ŋu | ŋə |
| l | voiced alveolar lateral approximant | lap `/læp/` | l | li | lɪ | lɛ | læ | lɑ | lʌ | lu | lə |
| r | voiced alveolar/postalveolar approximant | rap `/ræp/` | r | ri | rɪ | rɛ | ræ | rɑ | rʌ | ru | rə |
| j | voiced palatal approximant | yes `/jɛs/` | j | ji | jɪ | jɛ | jæ | jɑ | jʌ | ju | jə |
| w | voiced labial-velar approximant | wet `/wɛt/` | w | wi | wɪ | wɛ | wæ | wɑ | wʌ | wu | wə |

### Phonetic Notes

Principal allophonic realizations for each consonant onset. These describe how the phonemic CV cells above surface in actual speech.

| Consonant | Phonetic Note |
|---|---|
| p | aspirated [pʰ] syllable-initially before a stressed vowel. |
| b | often partially devoiced [b̥] in initial/final position. |
| t | aspirated [tʰ] before a stressed vowel; flapped [ɾ] intervocalically in GA. |
| d | often partially devoiced [d̥] initially/finally; flapped [ɾ] intervocalically in GA. |
| k | aspirated [kʰ] before a stressed vowel; place fronts before front vowels. |
| ɡ | often partially devoiced [ɡ̊] initially/finally; place fronts before front vowels. |
| tʃ | single affricate phoneme; lips slightly rounded/protruded. |
| dʒ | single affricate phoneme; often partially devoiced initially/finally. |
| f | stable across vowel contexts. |
| v | often partially devoiced [v̥] finally. |
| θ | interdental/denti-alveolar; TH-fronting to [f] in some accents (not GA/RP standard). |
| ð | interdental/denti-alveolar; may be a stop [d̪] after nasals or word-initially in casual speech. |
| s | stable; high-frequency sibilant. |
| z | often partially devoiced [z̥] finally. |
| ʃ | lips slightly rounded/protruded. |
| ʒ | rare word-initially in native vocabulary; lips slightly rounded. |
| h | voiced [ɦ] intervocalically; only occurs syllable-initially in English. |
| m | can be syllabic [m̩] in unstressed contexts. |
| n | can be syllabic [n̩] in unstressed contexts. |
| ŋ | never occurs syllable-initially in English; given here for matrix completeness. |
| l | clear [l] before vowels (onset); dark/velarized [ɫ] in coda; can be syllabic [l̩]. |
| r | phonetically [ɹ]; often labialized [ɹʷ] before/with rounding; retroflex or bunched articulation in GA. |
| j | glide; forms onglide of GOOSE/CURE-type sequences; devoiced [j̥] after voiceless stops. |
| w | glide; devoiced [ʍ]~[w̥] after voiceless stops; WH-merger means whine=wine in GA/RP. |

### Accent Notes

**GA vs. RP.** Vowel qualities here use General American (GA) values. Principal RP (Received Pronunciation) differences for this representative set: GA /ɑ/ covers both LOT and PALM, whereas RP keeps LOT as rounded /ɒ/ and PALM/START as /ɑː/; GA /æ/ in BATH words corresponds to RP /ɑː/; GA STRUT /ʌ/ is often more centralized [ɐ] in modern RP; FLEECE /iː/ and GOOSE /uː/ are phonemically long in RP and frequently diphthongal/fronted in GA. Consonant inventory is identical across the two accents; the main consonantal difference is rhoticity — GA is rhotic (coda /r/ is pronounced) while RP is non-rhotic, which does not affect these CV (onset) combinations.

**Rhoticity.** All combinations in this matrix are consonant-initial (CV onset) sequences, so the GA/RP rhoticity contrast (which concerns syllable-final /r/) does not alter the cell values.

## Suprasegmentals

Prosodic and suprasegmental features of Modern English pronunciation, documented in parallel for two reference accents: GA (General American) and RP (Received Pronunciation, Standard Southern British English). English is a stress accent language in which lexical stress is phonemic, rhythm is stress-timed, and unstressed syllables undergo extensive vowel reduction. Aspiration, pre-fortis vowel clipping, and a system of nuclear intonation tones complete the suprasegmental inventory.

### Stress

English lexical stress is phonemic (contrastive): the position of stress alone can distinguish otherwise identical words and is not predictable from a single fixed rule, unlike fixed-stress languages. Stress is realized through a combination of greater duration, higher pitch, fuller (unreduced) vowel quality, and greater loudness on the stressed syllable.

#### Stress Levels

| Level | IPA Notation | Phonetic Correlates |
|---|---|---|
| Primary (tonic) stress | `ˈ` placed immediately before the stressed syllable (e.g., `/əˈbaʊt/`) | Pitch prominence (the syllable carries the main pitch accent), maximal duration, full vowel quality, increased intensity |
| Secondary stress | `ˌ` placed immediately before the syllable (e.g., `/ˌɛləˈveɪʃən/`) | Rhythmic prominence weaker than primary stress; the vowel typically remains full (unreduced) but lacks the main pitch accent |
| Unstressed (weak) | no mark; vowel commonly reduces to `/ə/`, `/ɪ/`, or syllabic consonant | Short duration, reduced vowel quality, no pitch prominence |

#### Phonemic Contrast (Stress-Based Minimal Pairs)

Stress placement alone is contrastive in English; minimal pairs differing only in stress exist, most famously in noun/verb (and adjective/verb) pairs where the noun/adjective stresses the first syllable and the verb stresses the second. The stress shift is often accompanied by a difference in vowel reduction.

| Spelling | Noun (GA) | Noun (RP) | Verb (GA) | Verb (RP) | Gloss |
|---|---|---|---|---|---|
| record | `/ˈrɛkərd/` | `/ˈrɛkɔːd/` | `/rɪˈkɔrd/` | `/rɪˈkɔːd/` | noun (a recording) vs verb (to record) |
| present | `/ˈprɛzənt/` | `/ˈprɛzənt/` | `/prɪˈzɛnt/` | `/prɪˈzɛnt/` | noun/adjective (a gift; present) vs verb (to present) |
| object | `/ˈɑbdʒɛkt/` | `/ˈɒbdʒɪkt/` | `/əbˈdʒɛkt/` | `/əbˈdʒɛkt/` | noun (a thing) vs verb (to object) |
| permit | `/ˈpɜrmɪt/` | `/ˈpɜːmɪt/` | `/pərˈmɪt/` | `/pəˈmɪt/` | noun (a permit) vs verb (to permit) |
| contrast | `/ˈkɑntræst/` | `/ˈkɒntrɑːst/` | `/kənˈtræst/` | `/kənˈtrɑːst/` | noun (a contrast) vs verb (to contrast) |
| increase | `/ˈɪnkris/` | `/ˈɪŋkriːs/` | `/ɪnˈkris/` | `/ɪnˈkriːs/` | noun (an increase) vs verb (to increase) |

**Note:** Not every spelling pair shifts stress (e.g., 'promise', 'visit' keep first-syllable stress for both parts of speech). The pattern is a strong tendency, not an exceptionless rule.

#### Compound vs. Phrasal Stress

Stress distinguishes compound nouns (a single lexical unit) from corresponding noun phrases (adjective + noun). Compounds typically carry primary stress on the FIRST element (fore-stress); the equivalent phrase carries primary (nuclear) stress on the SECOND element (end-stress).

| Compound | Compound (GA) | Compound (RP) | Compound Meaning | Phrase | Phrase (GA) | Phrase (RP) | Phrase Meaning |
|---|---|---|---|---|---|---|---|
| ˈgreenhouse | `/ˈɡrinˌhaʊs/` | `/ˈɡriːnˌhaʊs/` | a glass building for growing plants | green ˈhouse | `/ˌɡrin ˈhaʊs/` | `/ˌɡriːn ˈhaʊs/` | a house that is green in color |
| ˈblackbird | `/ˈblækˌbɜrd/` | `/ˈblækˌbɜːd/` | a species of bird (Turdus merula) | black ˈbird | `/ˌblæk ˈbɜrd/` | `/ˌblæk ˈbɜːd/` | any bird that is black |
| ˈWhite House | `/ˈwaɪt ˌhaʊs/` | `/ˈwaɪt ˌhaʊs/` | the U.S. presidential residence | white ˈhouse | `/ˌwaɪt ˈhaʊs/` | `/ˌwaɪt ˈhaʊs/` | a house that is white |
| ˈhotdog | `/ˈhɑtˌdɔɡ/` | `/ˈhɒtˌdɒɡ/` | a sausage in a bun | hot ˈdog | `/ˌhɑt ˈdɔɡ/` | `/ˌhɒt ˈdɒɡ/` | a dog that is hot |

**Note:** Compound stress is also called fore-stress or left-stress; phrasal stress is end-stress. There are well-known exceptions to the compound rule (e.g., place names and certain N+N compounds like 'apple ˈpie', 'Madison ˈAvenue' take end-stress).

#### Word Stress Tendencies

While not fully predictable, English word stress shows strong statistical tendencies conditioned by syllable weight, word class, and suffix type.

**Stress-attracting (the suffix itself is stressed):**

- -ee (employˈee)
- -eer (engiˈneer)
- -ese (Japaˈnese)
- -ette (cigaˈrette)

**Pre-accenting (stress falls on the syllable before the suffix):**

- -ic (photoˈgraphic / cf. ˈphotograph)
- -ity (curiˈosity)
- -ion (creˈation)
- -ial (proverbial → proˈverbial)
- -ical (geoˈgraphical)
- -graphy (phoˈtography)
- -logy (biˈology)

**Stress-neutral (do not change the stem's stress):**

- -ness (ˈhappiness)
- -less (ˈcareless)
- -ful (ˈbeautiful)
- -ly (ˈquickly)
- -er (ˈteacher)
- -ment (often, e.g. ˈgovernment)

**Example stress shift:** ˈphotograph `/ˈfoʊtəˌɡræf/` → phoˈtography `/fəˈtɑɡrəfi/` (GA), `/fəˈtɒɡrəfi/` (RP) → photoˈgraphic `/ˌfoʊtəˈɡræfɪk/`: the same root shows three stress positions depending on the suffix.

### Rhythm

English is traditionally classified as a STRESS-TIMED language: stressed syllables tend to recur at roughly regular intervals, and the unstressed syllables between them are compressed (shortened and reduced) to maintain that beat. This contrasts with syllable-timed languages (e.g., French, Spanish) in which every syllable takes roughly equal time.

#### The Metrical Foot

The metrical FOOT is the basic rhythmic unit: it begins with a stressed (strong) syllable and includes all following unstressed (weak) syllables up to the next stress.

**IPA notation:** Feet are typically bounded by the stress marks `ˈ` / `ˌ`; a vertical bar `|` is sometimes used to delimit feet in metrical transcription

**Example:** In 'ˈTuesday's the ˈbest day of the ˈweek', the feet are [ˈTuesday's the] [ˈbest day of the] [ˈweek], each ideally occupying a comparable span of time despite differing syllable counts.

#### Isochrony

ISOCHRONY is the claimed tendency for inter-stress intervals (feet) to be equal in duration. Strict acoustic isochrony is not well supported by measurement; the perceived regularity arises largely from the compression of unstressed syllables and listener expectation. English is therefore best described as having a tendency toward stress-timing rather than literal equal timing.

**Consequence:** The more unstressed syllables fall between two stresses, the faster (more compressed and reduced) they are pronounced, e.g., 'cats eat fish' vs 'the cats will have eaten the fish' keep the three stresses at a similar pace.

#### Accent Difference

| Accent | Rhythmic Type |
|---|---|
| GA | Stress-timed; strong reduction of unstressed syllables. |
| RP | Stress-timed; comparably strong reduction. Both reference accents share the stress-timed rhythmic type, in contrast to syllable-timed varieties such as many Caribbean, West African, and Indian Englishes. |

### Vowel Reduction

A direct consequence of stress and rhythm: vowels in UNSTRESSED syllables tend to lose their distinct quality and reduce, most commonly to schwa `/ə/` (the commA / lettER vowels) or to a near-close lax `/ɪ/` (sometimes transcribed `/ᵻ/`, the 'rosES' vowel). Reduction is one of the most pervasive features of spoken English and is essential to natural rhythm.

#### Reduction Targets

**Schwa — `/ə/`**

The most common reduced vowel; mid-central and lax. Realizes most unstressed full vowels.

| Word | IPA (GA) | IPA (RP) | Note |
|---|---|---|---|
| about | `/əˈbaʊt/` | `/əˈbaʊt/` | first syllable reduced |
| sofa | `/ˈsoʊfə/` | `/ˈsəʊfə/` | final commA vowel |
| photograph → photography | `/ˈfoʊtəˌɡræf/ → /fəˈtɑɡrəfi/` | `/ˈfəʊtəɡrɑːf/ → /fəˈtɒɡrəfi/` | vowels that are full under stress reduce to `/ə/` when stress moves away |

**Reduced `/ɪ/` (or `/ᵻ/`)**

A second common reduction target, especially in certain prefixes (e.g., 'be-', 'de-', 'e-', 're-') and the plural/past endings; lax near-close front.

| Word | IPA (GA) | IPA (RP) |
|---|---|---|
| rabbit | `/ˈræbɪt/` | `/ˈræbɪt/` |
| wanted | `/ˈwɑntɪd/` | `/ˈwɒntɪd/` |
| horses | `/ˈhɔrsɪz/` | `/ˈhɔːsɪz/` |

**Syllabic Consonant — `[l̩]`, `[n̩]`, `[m̩]`, `[r̩]` (GA)**

Reduction can eliminate the vowel entirely, leaving a syllabic consonant that carries the syllable nucleus.

| Word | IPA (GA) | IPA (RP) |
|---|---|---|
| bottle | `/ˈbɑt(ə)l/ → [ˈbɑɾl̩]` | `/ˈbɒtl̩/` |
| button | `/ˈbʌtn̩/` | `/ˈbʌtn̩/` |
| rhythm | `/ˈrɪðm̩/` | `/ˈrɪðm̩/` |

#### Weak Forms

Function words (articles, prepositions, auxiliaries, pronouns, conjunctions) typically have a STRONG (citation) form used when stressed or in isolation, and a WEAK (reduced) form used in connected, unstressed positions. Weak forms are the default in natural speech; overuse of strong forms sounds unnatural or emphatic.

| Word | Strong Form | Weak Form | Context |
|---|---|---|---|
| and | `/ænd/` | `/ən(d)/` or `/n̩/` | fish 'n' chips → `/ˈfɪʃ n̩ ˈtʃɪps/` |
| to | `/tu/` (GA), `/tuː/` (RP) | `/tə/` | go to bed → `/ˌɡoʊ tə ˈbɛd/` (GA), `/ˌɡəʊ tə ˈbed/` (RP) |
| of | `/ʌv/` (GA), `/ɒv/` (RP) | `/əv/` or `/ə/` | a cup of tea → `/ə ˌkʌp ə ˈti/` (GA), `/ə ˌkʌp ə ˈtiː/` (RP) |
| for | `/fɔr/` (GA), `/fɔː/` (RP) | `/fər/` (GA), `/fə/` (RP) | looking for it |
| can (auxiliary) | `/kæn/` | `/kən/` or `/kn̩/` | I can go → `/aɪ kən ˈɡoʊ/` |
| the | `/ði/` (GA), `/ðiː/` (RP) | `/ðə/` (before consonant), `/ði/` (before vowel) | the cat `/ðə ˈkæt/` vs the apple `/ði ˈæpl̩/` |
| you | `/ju/` (GA), `/juː/` (RP) | `/jə/` | Do you know? → `/dʒə ˈnoʊ/` (GA), `/dʒə ˈnəʊ/` (RP) |

**Note:** Weak forms are the mechanism by which vowel reduction operates at the phrase level and are inseparable from stress-timed rhythm.

### Aspiration

The voiceless plosives `/p/`, `/t/`, `/k/` are aspirated — released with a following puff of air `[ʰ]` and a delay in voice onset — when they begin a stressed syllable (especially syllable-initially before a vowel). The same plosives are UNASPIRATED after `/s/` in a cluster and are typically unaspirated (or unreleased) syllable-finally and in unstressed onsets.

**IPA notation:** `ʰ` superscript after the plosive marks aspiration (e.g., `[pʰ]`, `[tʰ]`, `[kʰ]`)

#### Aspirated Contexts

**Rule:** At the onset of a stressed syllable, `/p t k/` are strongly aspirated.

| Word | Phonemic | Phonetic | Note |
|---|---|---|---|
| pin | `/pɪn/` | `[pʰɪn]` | |
| top | `/tɑp/` (GA), `/tɒp/` (RP) | `[tʰɑp]` / `[tʰɒp]` | |
| key | `/ki/` | `[kʰiː]` | |
| appear | `/əˈpɪr/` (GA), `/əˈpɪə/` (RP) | `[əˈpʰɪɚ]` / `[əˈpʰɪə]` | aspirated because it onsets the stressed second syllable |

#### Unaspirated Contexts

**Rule:** After `/s/` in a tautosyllabic cluster, `/p t k/` are unaspirated; this is the classic minimal demonstration of the allophonic rule.

| Word | Phonemic | Phonetic | Contrast |
|---|---|---|---|
| spin | `/spɪn/` | `[spɪn]` | cf. pin `[pʰɪn]` |
| stop | `/stɑp/` (GA), `/stɒp/` (RP) | `[stɑp]` / `[stɒp]` | cf. top `[tʰɑp]` |
| skin | `/skɪn/` | `[skɪn]` | cf. kin `[kʰɪn]` |

#### Accent Difference

| Accent | Aspiration Behavior |
|---|---|
| GA | Aspiration of `/p t k/` is robust in stressed onsets. Word-final and intervocalic `/t/` is frequently tapped/flapped to `[ɾ]` (e.g., 'water' `[ˈwɔɾɚ]`) rather than aspirated, and `/t/` may be glottalized `[ʔ]` before syllabic `/n/` ('button' `[ˈbʌʔn̩]`). |
| RP | Aspiration of `/p t k/` in stressed onsets is also robust. RP increasingly shows glottal reinforcement/replacement of `/t/` (`[ʔ]`) in coda and certain medial positions ('bottle' `[ˈbɒʔl̩]`); it lacks the GA flapping of intervocalic `/t/`. |

**Note:** Aspiration, not voicing, is the primary perceptual cue distinguishing fortis `/p t k/` from lenis `/b d ɡ/` in initial position, since the lenis series is often only weakly voiced in English.

### Vowel Length & Clipping

Although English vowel length is not phonemically contrastive in the way it is in some languages, vowel DURATION varies allophonically and predictably. The chief process is PRE-FORTIS CLIPPING (also called pre-fortis shortening): a vowel (and any sonorant in the same syllable) is noticeably SHORTER before a voiceless (fortis) consonant than before a voiced (lenis) one in the same context.

**IPA notation:** `ː` marks full/long duration; absence of `ː` (or the half-long mark `ˑ`) indicates clipped duration. The diacritic for shortening is `◌̆`.

#### Pre-Fortis Clipping

**Rule:** Vowel before a voiced/lenis coda = long; the SAME vowel before a voiceless/fortis coda = clipped (shorter). This duration difference is in fact a major cue listeners use to distinguish final fortis vs lenis consonants, since final `/b d ɡ/` are often devoiced.

| Pair | Lenis (long) | Fortis (clipped) | Vowel |
|---|---|---|---|
| bead vs beat | bead `/biːd/` `[biːd]` | beat `/bit/` `[biˑt]` (clipped) | FLEECE |
| seed vs seat | seed `/siːd/` `[siːd]` | seat `/sit/` `[siˑt]` | FLEECE |
| bag vs back | bag `/bæɡ/` `[bæːɡ]` | back `/bæk/` `[bæk]` | TRAP |
| ridge vs rich | ridge `/rɪdʒ/` `[rɪːdʒ]` | rich `/rɪtʃ/` `[rɪtʃ]` | KIT |
| prize vs price | prize `/praɪz/` `[praɪz]` | price `/praɪs/` `[prɐɪs]` (clipped diphthong) | PRICE (also Canadian-Raising-type quality shift in some accents) |

#### Sonorant Clipping

The shortening applies to a tautosyllabic sonorant as well, not only the vowel.

**Example:** 'bend' `[bɛnd]` has a longer `/n/` than 'bent' `[bɛnt]`; 'felled' vs 'felt' likewise differ in the duration of `/l/` plus vowel.

#### Other Length Effects

- **Open-syllable lengthening:** Vowels are somewhat longer in open syllables and in word-final stressed position.
- **Intrinsic length:** So-called 'long' vowels and diphthongs (FLEECE `/iː/`, GOOSE `/uː/`, PALM/START `/ɑː/`, THOUGHT `/ɔː/`, NURSE `/ɜː/`, FACE, GOAT, PRICE, MOUTH, CHOICE) are intrinsically longer than the 'short'/lax vowels (KIT `/ɪ/`, DRESS `/ɛ/`, TRAP `/æ/`, LOT `/ɒ/`, FOOT `/ʊ/`, STRUT `/ʌ/`), but all are subject to pre-fortis clipping.

#### Accent Difference

| Accent | Length Marking & Clipping |
|---|---|
| GA | Often transcribed without length marks because the lax/tense distinction is treated as primarily qualitative; pre-fortis clipping still applies. Pre-/r/ and pre-nasal contexts add further allophonic length and quality variation. |
| RP | Conventionally uses length marks (`/iː/`, `/ɑː/`, `/ɔː/`, `/uː/`, `/ɜː/`) for the long monophthongs; pre-fortis clipping audibly shortens these (e.g., 'feet' is shorter than 'feed'). |

### Intonation

Intonation is the linguistically structured use of pitch over the stretch of an utterance (the intonation phrase). The British nuclear-tone framework analyzes each intonation phrase around its NUCLEUS — the most prominent (tonic) syllable, typically the last stressed syllable — which carries a NUCLEAR TONE (a pitch movement) that conveys much of the grammatical and attitudinal meaning.

#### Structure of the Intonation Phrase

The **intonation phrase** is the domain of one intonation contour, bounded by perceptible breaks; also called a tone unit or tone group.

**Components:**

- **(Pre-head)** — unstressed syllables before the first stress
- **(Head)** — from the first stressed syllable up to the nucleus
- **Nucleus (tonic syllable)** — the obligatory pitch-accented syllable carrying the nuclear tone
- **(Tail)** — any syllables after the nucleus, over which the tone continues

**IPA notation:** Boundaries: `|` (minor) and `‖` (major); tone marks placed before the nucleus: `ꜜ`/`↓` downstep, `↑` upstep; global rise `↗` and fall `↘`. Nuclear tones are commonly notated with iconic marks: `ˋ` fall, `ˊ` rise, `ˇ` fall-rise, `ˆ` rise-fall.

#### Nuclear Tones

| Tone | Symbol | Contour | Typical Functions | Example |
|---|---|---|---|---|
| Fall | `ˋ` / `↘` / `\` | High-to-low pitch glide on/from the nucleus | Finality and completeness: statements, wh-questions, commands, exclamations. Conveys definiteness and confidence. | It's ˋfinished. (a definite, complete statement) |
| Rise | `ˊ` / `↗` / `/` | Low-to-high pitch glide | Non-finality, openness, questioning. Yes/no questions, listing items (non-final), encouraging continuation, soliciting a response. | Are you ˊcoming? (a yes/no question) |
| Fall-Rise | `ˇ` / `↘↗` / `\/` | Pitch falls then rises on/from the nucleus | Reservation, implication, contrast, polite contradiction, partial agreement ('but...'). Signals 'there is more to say' or an unstated qualification. | I ˇlike it... (implying 'but there's a reservation') |
| Rise-Fall | `ˆ` / `↗↘` / `/\` | Pitch rises then falls on/from the nucleus | Strong feeling: being impressed, surprised, indignant, or asserting emphatically. Conveys heightened involvement. | It was ˆmarvellous! (strongly impressed) |
| Level | `‾` / `→` | Sustained, unmoving pitch | Routine, boredom, hesitation, or marking a non-final boundary (e.g., reading a list mechanically, or trailing off). | →one, →two, →three... |

#### Functions Overview

- **Grammatical:** Distinguishes sentence types (statement vs question), marks clause and phrase boundaries, signals continuation vs completion.
- **Focus and information:** The placement of the nucleus marks the FOCUS / new information of the utterance (nucleus placement = sentence stress). Moving the nucleus changes what is highlighted: 'I bought a ˋRED car' vs 'I ˋBOUGHT a red car'.
- **Attitudinal:** Conveys speaker attitude and emotion (politeness, surprise, sarcasm, reservation, enthusiasm).
- **Discourse:** Manages turn-taking, signals topic boundaries, and links/contrasts information across an exchange.

#### Tonicity and Focus

TONICITY refers to where the nucleus (tonic syllable) is placed. By default it falls on the last lexical (content) word of the intonation phrase (broad focus); it shifts earlier for contrastive/narrow focus or to mark given vs new information.

| Utterance | Focus |
|---|---|
| I'd like a cup of ˋcoffee. | Broad / default focus — nucleus on the last content word. |
| ˋI'd like a cup of coffee. (not you) | Contrastive focus on the subject. |
| I'd like a ˋcup of coffee. (not a mug) | Contrastive focus shifted leftward. |

#### Accent Difference

| Accent | Intonation Behavior |
|---|---|
| GA | Frequently uses falling nuclear tones for statements; the high-rising terminal ('uptalk', a rise on declaratives) is widespread in many American varieties. Pitch range and the use of plateau/level contours differ from RP. |
| RP | The traditional nuclear-tone descriptions (Halliday, O'Connor & Arnold) are based on RP. RP also shows uptalk in younger speakers, but the conservative system associates falls with statements/wh-questions and rises with yes/no questions and non-finality. |

**Note:** The fundamental inventory of nuclear tones (fall, rise, fall-rise, rise-fall, level) and their core functions is shared by GA and RP; differences are largely in distribution, pitch range, and the prevalence of innovations such as uptalk.

## Syllable Structure

Syllable structure patterns in Modern English (General American = GA and Received Pronunciation = RP). English permits unusually heavy onsets and codas compared with most languages, allowing up to three consonants before the vowel and up to four after it. Syllabification follows the Maximal Onset Principle. This section is the English equivalent of the Peshitta guide's syllable_structure section.

**IPA template:** `(C)(C)(C)V(C)(C)(C)(C)`

**Maximal syllable:** `CCCVCCCC`

**Components:**

- **Onset:** 0 to 3 consonants preceding the nucleus *(optional)*
- **Nucleus:** V — a vowel (monophthong or diphthong) or a syllabic consonant *(required)*
- **Coda:** 0 to 4 consonants following the nucleus *(optional)*

### Onset

0 to 3 consonants preceding the nucleus. Single consonants: any consonant except `/ŋ/`. Two-consonant clusters obey sonority sequencing (rising sonority from edge to nucleus), e.g. `/pl/`, `/br/`, `/tw/`, `/sk/`, `/sn/`, `/fl/`, `/θr/`, `/ʃr/`. Three-consonant clusters are tightly restricted: they must begin with `/s/`, followed by a voiceless stop `/p t k/`, followed by an approximant `/l r w j/`.

- **Minimum consonants:** 0
- **Maximum consonants:** 3

**Sonority sequencing:** Within an onset, sonority must rise toward the vowel (obstruent < nasal < liquid < glide < vowel). `/s/`-initial clusters are the main exception, as `/s/` can precede a less-sonorous stop (e.g. `/st/`, `/sp/`, `/sk/`).

**Three-consonant onsets** — structure: `/s/` + voiceless stop + approximant.

Attested clusters: `spl`, `spr`, `spj`, `str`, `stj`, `skl`, `skr`, `skw`, `skj`.

| Word | IPA |
|---|---|
| splash | `/splæʃ/` |
| spray | `/spreɪ/` |
| string | `/strɪŋ/` |
| square (GA) | `/skwɛr/` |
| scream | `/skriːm/` |
| spew | `/spjuː/` |

### Nucleus

The obligatory core of the syllable. It is filled either by a vowel (monophthong or diphthong, organized by the Wells lexical sets) or, in unstressed syllables, by a syllabic consonant — a sonorant that carries the syllable beat without a vowel.

**Vowel nucleus:** A monophthong (e.g. KIT `/ɪ/`, TRAP `/æ/`, GOOSE `/uː/`) or a diphthong (e.g. PRICE `/aɪ/`, MOUTH `/aʊ/`, CHOICE `/ɔɪ/`, GOAT `/əʊ/` in RP, `/oʊ/` in GA).

| Word | IPA | Lexical set |
|---|---|---|
| a | `/ə/` | commA |
| ee (in 'see') | `/iː/` | FLEECE |
| I | `/aɪ/` | PRICE |

**Syllabic consonant nucleus:** In unstressed syllables a sonorant `/l n m r/` may itself be the nucleus, marked with a syllabicity diacritic `[◌̩]`. `/r̩/` surfaces in GA (rhotic) where RP has `/ə/` (non-rhotic). The GA syllabic rhotic `/r̩/` is equivalently notated as r-colored schwa `/ɚ/`; this guide uses `/r̩/` in the syllabic-consonant set, but `/ɚ/` denotes the same nucleus.

Syllabic consonants: `l̩`, `n̩`, `m̩`, `r̩`.

| Word | IPA | GA | RP | Nucleus |
|---|---|---|---|---|
| bottle | `/ˈbɒt.l̩/` | `/ˈbɑt.l̩/` | `/ˈbɒt.l̩/` | `l̩` |
| button | `/ˈbʌt.n̩/` | — | — | `n̩` |
| rhythm | `/ˈrɪð.m̩/` | — | — | `m̩` |
| butter | `/ˈbʌt.r̩/` | `/ˈbʌt.r̩/` | `/ˈbʌt.ə/` | `r̩ (GA) / ə (RP)` |

### Coda

0 to 4 consonants following the nucleus. English codas are exceptionally rich. Long codas are typically built up by appending the coronal suffixes `/s z t θ/` (plural, possessive, past tense, ordinal/abstract endings), which fall outside the normal sonority constraints. `/h/` never appears in a coda.

- **Minimum consonants:** 0
- **Maximum consonants:** 4

**Four-consonant codas:** Maximal codas usually require a morphological suffix stacked on a heavy stem.

| Word | IPA | Coda |
|---|---|---|
| sixths | `/sɪksθs/` | `ksθs` |
| twelfths | `/twɛlfθs/` | `lfθs` |
| glimpsed | `/ɡlɪmpst/` | `mpst` |

### Syllable Types

| Type | Description | IPA example | Word | Frequency |
|---|---|---|---|---|
| V | Bare vowel; no onset, no coda (open syllable) | `/ə/` | a | Common (esp. function words and weak syllables) |
| CV | Open syllable (single consonant + vowel) | `/ðə/` | the | Most common |
| VC | Vowel + single coda (no onset) | `/æt/` | at | Common |
| CVC | Closed syllable (onset + vowel + coda) | `/kæt/` | cat | Very common |
| CCV | Two-consonant onset cluster + vowel (open) | `/bluː/` | blue | Common |
| CCVCC | Two-consonant onset + vowel + two-consonant coda | `/blɛndz/` | blends | Common |
| CCCVC | Three-consonant onset (`/s/` + stop + approximant) + vowel + single coda | `/sprɪŋ/` | spring | Occasional |
| CVCCCC | Onset + vowel + four-consonant coda (maximal coda, usually morphologically built) | `/sɪksθs/` | sixths | Rare |

### Syllabification

**Principle:** Maximal Onset Principle

When a sequence of consonants stands between two vowels, as many as can legally form a syllable onset are assigned to the following syllable, provided the result is a permissible English onset and the preceding syllable remains well-formed.

| Word | IPA | Note |
|---|---|---|
| astray | `/ə.ˈstreɪ/` | `/str/` is a legal onset, so it all joins the second syllable |
| secret | `/ˈsiː.krɪt/` | `/kr/` is a legal onset, so the break falls before it |
| winter | `/ˈwɪn.tə/` (RP) / `/ˈwɪn.tr̩/` (GA) | `/nt/` is not a legal onset; the `/n/` stays in the first (stressed, closed) syllable. RP base is non-rhotic `/ˈwɪn.tə/`; GA syllabic rhotic `/ˈwɪn.tr̩/` (equivalently `/ˈwɪn.tɚ/`) |
| happy | `/ˈhæp.i/` | ambisyllabic `/p/` after a stressed lax vowel; the stressed syllable needs a coda |

### Constraints

- `/ŋ/` never occurs in a syllable onset (it appears only in codas and intervocalically, e.g. 'sing' `/sɪŋ/`, 'singer' `/ˈsɪŋ.ər/`).
- `/h/` never occurs in a syllable coda; it is restricted to onset position (e.g. 'hat' `/hæt/`, never word-finally).
- `/ʒ/` is rare in word-initial onsets (mostly loanwords, e.g. 'genre'), and never appears as the second member of an onset cluster.
- `/j/` in onset clusters is restricted: it occurs chiefly before `/uː/` and historical 'long u' (e.g. 'cue' `/kjuː/`, 'few' `/fjuː/`, 'pure' `/pjʊr/`); GA drops `/j/` after coronals (yod-dropping), so 'tune' = GA `/tuːn/` vs RP `/tjuːn/`.
- `/w/` in onset clusters appears after stops and `/s/`; the productive set is `/tw/`, `/dw/`, `/kw/`, `/ɡw/` (e.g. 'Gwen'), `/skw/`, and `/sw/`. `/w/` does not cluster after a fricative other than `/s/`.
- In a three-consonant onset only `/s/` may occupy the first slot, and only a voiceless stop `/p t k/` may follow it before an approximant.
- Onsets obey the Sonority Sequencing Principle (rising sonority toward the nucleus); `/s/`-stop clusters (`/sp/`, `/st/`, `/sk/`) are the principal sonority-reversal exception.
- Two voiced obstruents or two voiceless obstruents rarely cluster in a tautosyllabic onset except across the `/s/` exception; clusters like `*/tl/` and `*/dl/` are disallowed in onsets (no English word begins with `/tl/` or `/dl/`).
- Long, complex codas of three or four consonants almost always arise from stacking coronal suffixes `/s z t θ/` (plural, 3rd-sg, possessive, past, ordinal) onto the stem, e.g. 'texts' `/tɛksts/`, 'glimpsed' `/ɡlɪmpst/`.
- Lax (short, 'checked') vowels — KIT `/ɪ/`, DRESS `/ɛ/`, TRAP `/æ/`, LOT `/ɒ~ɑ/`, STRUT `/ʌ/`, FOOT `/ʊ/` — cannot end a stressed syllable; they require a coda (cannot occur in a stressed open syllable).
- Tense (long/'free') vowels and diphthongs — FLEECE `/iː/`, GOOSE `/uː/`, FACE `/eɪ/`, GOAT `/oʊ~əʊ/`, PRICE `/aɪ/`, etc. — may freely end an open syllable.
- Syllabic consonants `/l̩ n̩ m̩ r̩/` occur only in unstressed syllables and never carry primary stress.
- The Maximal Onset Principle governs medial consonant assignment, subject to the constraint that the resulting onset and coda must each be independently legal.

## Phonological Rules

Active connected-speech and allophonic processes in Modern English, documented in parallel for General American (GA) and Received Pronunciation (RP). These rules describe systematic, largely automatic changes that apply to underlying phonemic forms to yield surface phonetic forms. Many operate at word boundaries in connected speech (sandhi); others are word-internal allophonic adjustments. Accent scope is marked as 'GA', 'RP', or 'both'; where a process applies in both accents but differs in detail, the divergence is noted in the description. IPA examples are given as input → output, with /slashes/ for phonemic underlying forms and [brackets] for phonetic surface forms.

### Rules at a Glance

| # | Rule | Process | Accents |
|---|---|---|---|
| 1 | Aspiration of voiceless stops | `/p t k/ → [pʰ tʰ kʰ]` | both |
| 2 | T-flapping (tapping) | `/t d/ → [ɾ]` | GA |
| 3 | Glottal reinforcement (pre-glottalization) | `/p t k tʃ/ → [ʔp ʔt ʔk ʔtʃ]` | both |
| 4 | T-glottalling | `/t/ → [ʔ]` | RP |
| 5 | L-velarization (clear vs. dark L) | `/l/ → [l]` / onset, `[ɫ]` / coda | both |
| 6 | L-vocalization | `/l/ → [o̯ ~ ʊ]` | RP |
| 7 | Vowel reduction to schwa | `/V/ → [ə]` | both |
| 8 | Nasal place assimilation | `/n/ → [m]/[ŋ]` | both |
| 9 | Yod-coalescence (palatalization) | `/tj dj sj zj/ → [tʃ dʒ ʃ ʒ]` | both |
| 10 | Yod-dropping | `/Cj/ → [C]` | GA |
| 11 | Linking-R and intrusive-R | `∅ → [r]` | RP |
| 12 | Pre-fortis clipping | `Vː → Vˑ` | both |
| 13 | Elision and cluster simplification | `/C/ → ∅` | both |
| 14 | Voicing assimilation of -s and -ed | `-s → [s/z/ɪz]`; `-ed → [t/d/ɪd]` | both |
| 15 | G-dropping (-ing velar fronting) | `/ŋ/ → [n]` | both |
| 16 | happY-tensing | `/ɪ/ → [i]` | both |

### Rule 1: Aspiration of voiceless stops

Voiceless stops /p t k/ are produced with a strong puff of aspiration when they begin a stressed syllable. Aspiration is suppressed after tautosyllabic /s/ (e.g. spin [spɪn], not [spʰɪn]) and is weaker syllable-finally or before an unstressed vowel. This is a robust, mostly automatic process in both reference accents.

**IPA example:** `/p t k/ → [pʰ tʰ kʰ]` : pin `/pɪn/` → `[pʰɪn]`, top `/tɒp~tɑp/` → `[tʰɒp]`  
**IPA notation:** `/p t k/ → [pʰ tʰ kʰ] / [+stress]σ[ onset, not after /s/`  
**Environment:** Syllable-initial before a stressed vowel; blocked after tautosyllabic /s/ (s+stop clusters)  
**Accents:** both  

### Rule 2: T-flapping (tapping)

In General American, intervocalic /t/ and /d/ are realized as a voiced alveolar tap [ɾ] when the following vowel is unstressed (and after a vowel or /r/). This neutralizes the /t/–/d/ contrast in pairs like 'latter'/'ladder'. The process also applies across word boundaries ('get it' [ˈɡɛɾɪt]). RP generally retains [t] here, though tapping occurs variably in casual RP.

**IPA example:** `/t d/ → [ɾ]` : water `/ˈwɔtɚ/` → `[ˈwɑɾɚ]`, city `/ˈsɪti/` → `[ˈsɪɾi]`, rider/writer → `[ˈɹaɪɾɚ]`  
**IPA notation:** `/t d/ → [ɾ] / V_(r)V̆ (intervocalic, before unstressed vowel)`  
**Environment:** Between a vowel (or /r/) and a following unstressed vowel, within or across words; foot-internal  
**Accents:** GA  

### Rule 3: Glottal reinforcement (pre-glottalization)

Voiceless stops and the affricate /tʃ/ are reinforced by an overlapping glottal closure when they occur in syllable coda before another consonant or a pause. The oral closure is preserved but preceded/accompanied by a glottal stop gesture. Common in both accents, especially advanced in RP.

**IPA example:** `/p t k tʃ/ → [ʔp ʔt ʔk ʔtʃ]` : back `/bæk/` → `[bæʔk]`, catch `/kætʃ/` → `[kæʔtʃ]`  
**IPA notation:** `/p t k tʃ/ → [ˀC] / V_{C, #} (syllable-final, before consonant or pause)`  
**Environment:** Syllable-final coda before a consonant or pause (not before a vowel)  
**Accents:** both  

### Rule 4: T-glottalling

In RP (and widely in British English), /t/ is fully replaced by a glottal stop [ʔ] in syllable-final position before a consonant, before a syllabic nasal, or at a pause/word boundary. Unlike glottal reinforcement, the oral closure is lost entirely. GA shows this mainly before syllabic /n/ (e.g. 'button' [ˈbʌʔn̩]) but resists it intervocalically, where tapping applies instead.

**IPA example:** `/t/ → [ʔ]` : button `/ˈbʌtən/` → `[ˈbʌʔn̩]`, Gatwick → `[ˈɡæʔwɪk]`, not now → `[nɒʔ naʊ]`  
**IPA notation:** `/t/ → [ʔ] / V_{C, #, syllabic N} (not pre-vocalic)`  
**Environment:** Syllable-final before a consonant, pause, or syllabic nasal; not before a stressed vowel  
**Accents:** RP  

### Rule 5: L-velarization (clear vs. dark L)

The phoneme /l/ has two principal allophones: a clear (non-velarized) [l] in syllable onset before a vowel, and a dark, velarized [ɫ] in syllable coda (before a consonant or pause). RP maintains a fairly clear onset [l]; GA tends toward a darker [ɫ] in all positions, including onsets, but the onset–coda contrast is present in both accents.

**IPA example:** `/l/ → [l]` / onset, `[ɫ]` / coda : leaf `/liːf/` → `[liːf]`, feel `/fiːl/` → `[fiːɫ]`, milk → `[mɪɫk]`  
**IPA notation:** `/l/ → [ɫ] (velarized) / _{C, #}; [l] (clear) / _V`  
**Environment:** Dark [ɫ] in coda (pre-consonantal, pre-pausal); clear [l] in pre-vocalic onset  
**Accents:** both  

### Rule 6: L-vocalization

Dark /l/ in coda position may lose its alveolar contact and be realized as a back vowel or glide [ʊ ~ o̯ ~ w]. This is characteristic of many British English varieties and increasingly heard in casual RP; it is far less general in mainstream GA. The process targets only the already-velarized (dark) coda allophone.

**IPA example:** `/l/ → [o̯ ~ ʊ]` : milk `/mɪlk/` → `[mɪʊ̯k]`, bottle → `[ˈbɒtʊ]`, full → `[fʊʊ̯]`  
**IPA notation:** `[ɫ] → [o̯ ~ ʊ ~ w] / _{C, #} (coda dark L → back vocoid)`  
**Environment:** Coda /l/ (after a vowel, before a consonant or pause); does not apply to clear onset [l]  
**Accents:** RP  

### Rule 7: Vowel reduction to schwa

Full vowels in unstressed syllables typically reduce to the central vowel schwa [ə] (or, in some lexical/positional contexts, to [ɪ ~ ɨ]). Reduction is governed by stress placement, so the same morpheme alternates between a full vowel under stress and schwa when unstressed (e.g. the second vowel of PHOtograph vs. phoTOgraphy). Pervasive in both accents and central to English rhythm.

**IPA example:** `/V/ → [ə]` : photograph `/ˈfoʊtəɡræf/` vs. photography `/fəˈtɒɡrəfi/`; banana → `[bəˈnænə]`  
**IPA notation:** `V → [ə] (or [ɪ]) / in unstressed syllables`  
**Environment:** Unstressed (weak) syllables, especially in function words and pretonic/post-tonic positions  
**Accents:** both  

### Rule 8: Nasal place assimilation

A word- or syllable-final alveolar nasal /n/ assimilates to the place of articulation of a following consonant: it becomes bilabial [m] before bilabials (/p b m/) and velar [ŋ] before velars (/k ɡ/). This regressive place assimilation operates across word boundaries in connected speech and is optional/gradient depending on speech rate. Active in both accents.

**IPA example:** `/n/ → [m]/[ŋ]` : ten boys `/tɛn bɔɪz/` → `[tɛm bɔɪz]`, ten girls → `[tɛŋ ɡɜːlz]`, in case → `[ɪŋ keɪs]`  
**IPA notation:** `N → [αPLACE] / _C[αPLACE] (coda nasal takes place of following consonant)`  
**Environment:** Coda nasal immediately before a consonant of a different place, especially across word boundaries  
**Accents:** both  

### Rule 9: Yod-coalescence (palatalization)

When a coronal obstruent /t d s z/ is followed by /j/ (the palatal glide of GOOSE-class words and word-internal sequences), the two coalesce into a single palato-alveolar segment: /tj/→[tʃ], /dj/→[dʒ], /sj/→[ʃ], /zj/→[ʒ]. Word-internal coalescence ('issue', 'measure', 'soldier') is established in both accents; coalescence across the onset of stressed syllables ('tune', 'dune') is more advanced in RP, while GA more often drops the yod instead (see yod-dropping).

**IPA example:** `/tj dj sj zj/ → [tʃ dʒ ʃ ʒ]` : tune `/tjuːn/` → `[tʃuːn]`, during → `[ˈdʒʊərɪŋ]`, issue `/ˈɪsjuː/` → `[ˈɪʃuː]`, measure → `[ˈmɛʒə]`  
**IPA notation:** `/t d s z/ + /j/ → [tʃ dʒ ʃ ʒ] / _/uː, ə/`  
**Environment:** Coronal obstruent + /j/, both word-internally and (in RP) syllable-initially before /uː/  
**Accents:** both  

### Rule 10: Yod-dropping

In General American, the glide /j/ is deleted after coronal consonants /t d n s z l θ/ (and after /r/, /tʃ/, /dʒ/) before /uː/, so 'new', 'tune', 'duke', 'suit' are [nuː tuːn duːk suːt]. RP retains the yod after /t d n/ and many coronals ('new' [njuː]), although it too drops /j/ after /r, l, dʒ, tʃ/ and palatalizes /t d/ via coalescence. Yod-dropping is thus much more extensive in GA.

**IPA example:** `/Cj/ → [C]` : new `/njuː/` → `[nuː]` (GA), tune → `[tuːn]` (GA), duke → `[duːk]` (GA); cf. RP `[njuː tjuːn djuːk]`  
**IPA notation:** `/j/ → ∅ / coronal C _/uː/ (GA, after /t d n s z l θ r/)`  
**Environment:** After coronal consonants before /uː/; far more general in GA than in RP  
**Accents:** GA  

### Rule 11: Linking-R and intrusive-R

Two related sandhi processes in non-rhotic accents like RP. LINKING-R: an /r/ spelled at the end of a word is silent before a pause or consonant but pronounced [ɹ] when the next word begins with a vowel ('car is' [kɑːr ɪz], 'four eggs' [fɔːr ɛɡz]). INTRUSIVE-R: by analogy, speakers insert an unetymological [ɹ] between a non-high back/central vowel (/ə ɑː ɔː ɪə/) and a following vowel even where no 'r' is spelled ('drawing' [ˈdrɔːrɪŋ], 'law and order' [lɔːr ən ˈɔːdə]). Rhotic GA pronounces all spelled /r/ unconditionally and has neither linking nor intrusive R as distinct processes.

**IPA example:** `∅ → [r]` : linking 'car is' `/kɑː ɪz/` → `[kɑːr ɪz]`, 'four eggs' → `[fɔːr ɛɡz]`; intrusive 'drawing' → `[ˈdrɔːrɪŋ]`, 'idea of' → `[aɪˈdɪər əv]`  
**IPA notation:** `∅ → [ɹ] / {non-high V}_V (etymological = linking-R; non-etymological = intrusive-R)`  
**Environment:** Non-rhotic accents only: after a (non-high) vowel before a vowel-initial word; etymological r → linking, no r → intrusive  
**Accents:** RP  

### Rule 12: Pre-fortis clipping

A vowel (and any following sonorant in the same syllable) is noticeably shortened when it precedes a voiceless (fortis) consonant in the coda, compared with the same vowel before a voiced (lenis) consonant. Thus the vowel of 'beat/seat/back' is shorter than that of 'bead/seed/bag'. This durational cue is a major perceptual marker of the coda voicing contrast and operates in both accents.

**IPA example:** `Vː → Vˑ` : bead `/biːd/` → `[biːd]` vs. beat `/biːt/` → `[biˑt]` (same FLEECE vowel, half-long/clipped); 'seed' `[siːd]` long vs. 'seat' `[siˑt]` clipped  
**IPA notation:** `Vː → Vˑ / _C[−voice] (long vowel half-long/clipped, same quality, before a fortis/voiceless coda)`  
**Environment:** Stressed vowel (and tautosyllabic sonorant) before a tautosyllabic voiceless obstruent  
**Accents:** both  

### Rule 13: Elision and cluster simplification

In connected and rapid speech, a consonant—typically a medial alveolar stop /t/ or /d/—is elided when it stands between two other consonants. Examples: 'friendship' [ˈfrɛnʃɪp], 'next day' [nɛks deɪ], 'last chance' [lɑːs tʃɑːns], 'mashed potatoes'. The deletion simplifies otherwise heavy consonant clusters and is gradient with speech rate. Common in both accents.

**IPA example:** `/C/ → ∅` : friendship `/ˈfrɛndʃɪp/` → `[ˈfrɛnʃɪp]`, next day → `[nɛks deɪ]`, handbag → `[ˈhænbæɡ]`  
**IPA notation:** `C → ∅ / C_C (medial obstruent deleted in three-consonant clusters)`  
**Environment:** A stop (usually /t d/) between two consonants across a syllable or word boundary  
**Accents:** both  

### Rule 14: Voicing assimilation of the regular -s and -ed suffixes

The regular inflectional suffixes each have three predictable allomorphs selected by the stem-final segment. The -s suffix (plural, 3rd-singular, possessive): [ɪz~əz] after a sibilant /s z ʃ ʒ tʃ dʒ/ ('buses', 'judges'); [s] after any other voiceless consonant ('cats', 'cups'); [z] elsewhere, after voiced consonants and vowels ('dogs', 'plays'). The -ed suffix (past, participle): [ɪd~əd] after an alveolar stop /t d/ ('wanted', 'ended'); [t] after any other voiceless consonant ('walked', 'kissed'); [d] elsewhere ('played', 'buzzed'). Both are governed by voicing agreement with the preceding segment plus schwa-epenthesis when the stem ends in a homorganic obstruent. Identical in both accents.

**IPA example:** -s: cats `/kæts/` → `[kæts]`, dogs → `[dɒɡz]`, horses → `[ˈhɔːsɪz]`; -ed: walked → `[wɔːkt]`, played → `[pleɪd]`, wanted → `[ˈwɒntɪd]`  
**IPA notation:** `-s → [s]/[−vc]_ , [z]/[+vc]_ , [ɪz]/[+sib]_ ; -ed → [t]/[−vc]_ , [d]/[+vc]_ , [ɪd]/{t,d}_`  
**Environment:** Suffix-initial morpheme boundary; conditioned by voicing and (for epenthesis) by stem-final sibilancy (-s) or stem-final /t,d/ (-ed)  
**Accents:** both  

### Rule 15: G-dropping (-ing velar fronting)

In casual and vernacular registers, the velar nasal /ŋ/ of the unstressed suffix '-ing' is fronted to the alveolar nasal [n], so 'running' is [ˈrʌnɪn]. Despite the name, no [ɡ] is actually dropped; the change is /ŋ/→[n]. It is a stylistic/sociolinguistic variable present in both accents, favored in informal speech and restricted to the unstressed verbal/nominal -ing ending.

**IPA example:** `/ŋ/ → [n]` : running `/ˈrʌnɪŋ/` → `[ˈrʌnɪn]`, walking → `[ˈwɔːkɪn]`, something → `[ˈsʌmθɪn]`  
**IPA notation:** `/ŋ/ → [n] / unstressed _# (in the suffix -ing)`  
**Environment:** Word-final unstressed suffix -ing; not in monosyllables like 'sing' or stressed /ŋ/  
**Accents:** both  

### Rule 16: happY-tensing

The unstressed final vowel of words like 'happy', 'city', 'coffee', 'very' (Wells's happY set) is realized as a close front [i] rather than the lax [ɪ] of KIT. This 'tensing' is general in GA and now standard in contemporary RP (older conservative RP used [ɪ]). The quality is typically shorter and laxer than fully stressed FLEECE /iː/.

**IPA example:** `/ɪ/ → [i]` : happy `/ˈhæpɪ/` → `[ˈhæpi]`, city → `[ˈsɪti]`, coffee → `[ˈkɒfi]`  
**IPA notation:** `/ɪ/ → [i] / unstressed word-final open syllable (happY lexical set)`  
**Environment:** Unstressed word-final position in open syllables (the happY lexical set)  
**Accents:** both  

### Notes

Many of these processes are gradient and rate-dependent: they apply more fully in fast, casual speech and may be suppressed in careful or formal styles. Sandhi rules (linking-R, intrusive-R, nasal assimilation, elision) operate across word boundaries and interact with rhythm and stress. The principal GA/RP divergences in this section are: t-flapping and extensive yod-dropping (GA), versus T-glottalling, l-vocalization, and linking/intrusive-R (RP, as a non-rhotic accent). happY-tensing and -s/-ed voicing assimilation are now shared across both reference accents.

## General American vs. Received Pronunciation

Systematic pronunciation differences between the two reference accents of Modern English, expressed in IPA. The two traditions documented in parallel are General American (GA), the most widely described accent of North American English, and Received Pronunciation (RP, also called Standard Southern British English), the prestige accent of England. As with the Eastern (Madnhaya) and Western (Serto) traditions of Syriac, neither accent is intrinsically more correct; they represent two coexisting standardized systems. Vowels are referenced by the Wells (1982) Standard Lexical Sets. Phonemic transcriptions use /slashes/ and phonetic detail uses [brackets].

### Reference accents

- **GA:** General American — rhotic, lacks the TRAP-BATH split, has the cot-caught merger for many speakers, flaps intervocalic /t/.
- **RP:** Received Pronunciation (Standard Southern British English) — non-rhotic, has the TRAP-BATH split, distinguishes LOT/THOUGHT, retains [t] (or glottal [ʔ]) for intervocalic /t/.

### Differences

| Feature | GA | RP | Examples | Explanation |
|---|---|---|---|---|
| Rhoticity (postvocalic /r/) | `[ɹ]` pronounced in all positions (rhotic) | `[ɹ]` silent except before a vowel (non-rhotic) | car: GA `/kɑɹ/` — RP `/kɑː/`; letter: GA `[ˈlɛɾɚ]` — RP `/ˈletə/`; hard: GA `/hɑɹd/` — RP `/hɑːd/` | The single most salient division. GA preserves /r/ everywhere it is written; RP drops /r/ unless a vowel follows immediately. In RP the lost /r/ usually leaves compensatory vowel length or an unstressed schwa, and resurfaces as linking-/r/ before a following vowel (e.g. 'car alarm' `[kɑːɹ əˈlɑːm]`). |
| LOT vowel | `/ɑ/` (unrounded open back) | `/ɒ/` (rounded open back) | lot: GA `/lɑt/` — RP `/lɒt/`; dog: GA `/dɑɡ/` — RP `/dɒɡ/`; stop: GA `/stɑp/` — RP `/stɒp/` | RP keeps a distinctly rounded short vowel /ɒ/ in words like 'lot, dog, hot'. GA has unrounded this vowel to /ɑ/, which is also the GA realization of the PALM/START vowel, contributing to the father-bother merger (both /ɑ/) in American English. |
| TRAP-BATH split | BATH = TRAP = `/æ/` (no split) | BATH = `/ɑː/`, distinct from TRAP `/æ/` (split present) | bath: GA `/bæθ/` — RP `/bɑːθ/`; trap: GA `/tɹæp/` — RP `/tɹæp/` (same in both); dance: GA `/dæns/` — RP `/dɑːns/`; grass: GA `/ɡɹæs/` — RP `/ɡɹɑːs/` | In RP a historical set of words (BATH lexical set: typically /æ/ before voiceless fricatives /f θ s/ and before some nasal clusters) shifted to long back /ɑː/, identical to the PALM/START vowel. GA did not undergo this lengthening and keeps /æ/ throughout, so 'bath' rhymes with 'math' for Americans but not for RP speakers. Membership is partly lexical, not fully predictable. |
| Intervocalic /t/ (and /d/) — flapping | `[ɾ]` alveolar tap (voiced flap) | `[t]` full stop, or `[ʔ]` glottal stop | water: GA `[ˈwɑɾɚ]` — RP `/ˈwɔːtə/`; butter: GA `[ˈbʌɾɚ]` — RP `/ˈbʌtə/` ~ `[ˈbʌʔə]`; city: GA `/ˈsɪɾi/` — RP `/ˈsɪti/` | In GA, /t/ (and /d/) between vowels where the second is unstressed reduces to a quick voiced tap [ɾ], so 'latter' and 'ladder' often sound identical. RP retains a clear [t] in careful speech; in many contemporary RP-adjacent and Estuary speakers the same /t/ is realized as a glottal stop [ʔ] rather than a flap. |
| Yod-dropping after coronals | `/u/` (no /j/ glide after t, d, n, s, l) | `/juː/` (yod retained) | tune: GA `/tun/` — RP `/tjuːn/`; new: GA `/nu/` — RP `/njuː/`; duke: GA `/duk/` — RP `/djuːk/`; Tuesday: GA `/ˈtuzdeɪ/` — RP `/ˈtjuːzdeɪ/` | After alveolar/coronal consonants (/t d n s l/), GA typically deletes the historical palatal glide /j/, giving plain /u/. RP preserves the glide /juː/ (or coalesces it, as in 'Tuesday' → [ˈtʃuːzdeɪ] for some speakers). Both accents keep the yod after non-coronals ('cue' /kjuː/, 'few' /fjuː/). |
| GOAT vowel | `/oʊ/` (back rounded onset) | `/əʊ/` (central/schwa onset) | goat: GA `/ɡoʊt/` — RP `/ɡəʊt/`; go: GA `/ɡoʊ/` — RP `/ɡəʊ/`; no: GA `/noʊ/` — RP `/nəʊ/` | The vowel of 'go, goat, home' begins farther back and rounded in GA ([oʊ]) but with a central, unrounded schwa-like onset in RP ([əʊ]). The RP onset has fronted considerably over the twentieth century; this is one of the most reliable cues distinguishing the two accents on a single word. |
| CLOTH vowel | `/ɔ/` (raised; groups with THOUGHT for many) — or `/ɑ/` where cot-caught merged | `/ɒ/` (short, groups with LOT) | cloth: GA `/klɔθ/` — RP `/klɒθ/`; off: GA `/ɔf/` — RP `/ɒf/`; cost: GA `/kɔst/` — RP `/kɒst/` | Historically CLOTH words (/ɒ/ before voiceless fricatives) raised to /ɔː/ in conservative GA, joining the THOUGHT set, so 'cloth' and 'cough' could pattern with 'thought'. In RP the lengthening was undone, and CLOTH rejoined LOT as short /ɒ/. In cot-caught-merged GA, CLOTH instead falls together with LOT as /ɑ/. |
| THOUGHT vowel and the cot-caught merger | `/ɔ/` distinct, OR merged with LOT/PALM as `/ɑ/` (merger widespread in GA) | `/ɔː/` — always distinct from LOT `/ɒ/` | caught: GA `/kɔt/` or merged `/kɑt/` — RP `/kɔːt/`; cot: GA `/kɑt/` — RP `/kɒt/`; thought: GA `/θɔt/` ~ `/θɑt/` — RP `/θɔːt/` | RP maintains a robust contrast between short rounded LOT /ɒ/ ('cot') and long THOUGHT /ɔː/ ('caught'). A large and growing share of GA speakers (especially Western and Canadian) have merged these into a single vowel, usually /ɑ/, so that 'cot' and 'caught', 'Don' and 'dawn' are homophones. Where unmerged (e.g. parts of the East and South), GA THOUGHT is /ɔ/. |
| NURSE vowel (r-coloring) | `/ɝ/` (rhotacized, r-colored vowel) | `/ɜː/` (long, no r-coloring) | nurse: GA `/nɝs/` — RP `/nɜːs/`; bird: GA `/bɝd/` — RP `/bɜːd/`; work: GA `/wɝk/` — RP `/wɜːk/` | Because GA is rhotic, the NURSE vowel carries r-coloring throughout and is transcribed as the single rhotacized vowel /ɝ/ (or [ɚ] when unstressed, as in lettER). RP, being non-rhotic, has a plain long central vowel /ɜː/ with no rhoticity. The same split governs lettER: GA /ɚ/ vs RP /ə/. |
| START / NORTH / FORCE (r-colored vowels) | vowel + `[ɹ]`: START `/ɑɹ/`, NORTH/FORCE `/ɔɹ/` (or `/oɹ/`) | long vowel, no [r]: START `/ɑː/`, NORTH/FORCE `/ɔː/` | start: GA `/stɑɹt/` — RP `/stɑːt/`; north: GA `/nɔɹθ/` — RP `/nɔːθ/`; force: GA `/foɹs/` ~ `/fɔɹs/` — RP `/fɔːs/` | In rhotic GA these sets keep an audible /r/ closing the syllable. In non-rhotic RP the /r/ is lost and the preceding vowel is lengthened: START → /ɑː/ (merging with PALM and BATH), NORTH and FORCE → /ɔː/ (merging with THOUGHT). The historical NORTH-FORCE distinction ('horse' vs 'hoarse') is lost in both modern accents, surviving only in conservative varieties. |
| happY vowel (final unstressed -y) | `[i]` tense (happy-tensing) | `[i]` tense in modern RP; conservative RP `[ɪ]` lax | happy: GA `/ˈhæpi/` — RP `/ˈhæpi/` (conservative `/ˈhæpɪ/`); city: GA `[ˈsɪɾi]` — RP `/ˈsɪti/`; coffee: GA `/ˈkɔfi/` ~ `/ˈkɑfi/` — RP `/ˈkɒfi/` | The final vowel of 'happy, city, money' is realized as a tense [i] (happy-tensing) in GA and in present-day mainstream RP. Older/conservative RP used a lax [ɪ], so 'happy' ended like the KIT vowel. This is one feature where the two reference accents have largely converged, though dictionaries often transcribe it with the neutral symbol /i/ to cover both values. |
| Dark /l/ distribution and L-vocalization | `[ɫ]` velarized (dark) in most positions | `[l]` clear before vowels, `[ɫ]` dark in codas; coda `[ɫ]` → `[o]`/`[ʊ]` for many (L-vocalization) | feel: GA `/fiɫ/` — RP `/fiːɫ/` ~ `/fiːo/`; milk: GA `/mɪɫk/` — RP `/mɪɫk/` ~ `/mɪok/`; leaf: GA `/lif/` — RP `/liːf/` (clear [l] in both, onset position) | GA tends toward a dark, velarized [ɫ] in all environments, including before vowels. RP maintains the classic clear-vs-dark allophony (clear [l] in onsets, dark [ɫ] in codas). A widespread innovation in Southern British (Estuary and younger RP) vocalizes coda dark-l to a back vowel [o]/[ʊ], so 'milk' approaches [mɪok] — a change not characteristic of GA. |

GA and RP differ most audibly in (1) rhoticity, which cascades through NURSE, lettER, START, NORTH, FORCE, CURE and the entire system of r-colored vowels; (2) the back vowel space, where the LOT/CLOTH/THOUGHT/PALM relationships diverge and GA shows the cot-caught merger; and (3) the TRAP-BATH split present only in RP. Allophonic processes — GA t-flapping, GA yod-dropping, and Southern British glottalling and L-vocalization — further separate the two traditions.

## Orthography: Grapheme–Phoneme Correspondences

English orthography is morphophonemic and historically deep rather than transparently phonemic. The Latin alphabet of 26 letters is mapped onto roughly 44 phonemes (24 consonants + ~20 vowels/diphthongs), so grapheme-to-phoneme correspondences are heavily one-to-many (a single grapheme has several pronunciations, e.g. 'a' in cat/face/father/about; 'gh' in ghost/laugh/night) and many-to-one (several graphemes spell one phoneme, e.g. /f/ = f, ff, ph, gh; /iː/ = ee, ea, ie, e_e, ei). The spelling system fossilises earlier stages of the language: the Great Vowel Shift (c. 1400-1700) raised and diphthongised the Middle English long vowels while their spellings stayed fixed, which is why 'i' in 'bite' is `/aɪ/` not `/iː/` and 'a' in 'name' is `/eɪ/` not `/aː/`. Other layers include Norman French spellings (qu, gu, ch), Latinate and Greek borrowings (ph, ch=/k/, rh, ps), the silent magic-e (VCe) lengthening convention, silent letters left by sound changes (k in 'knife', gh in 'night', l in 'walk', w in 'write'), and a tendency to preserve morphemic identity across pronunciation changes (sign~signal, nation~native, heal~health). Both reference accents share the same spelling system; differences below note GA (General American) vs RP (Received Pronunciation), chiefly rhoticity (GA pronounces post-vocalic r, RP does not) and a few lexical-set splits.

**Reference accents:**

| Label | Accent |
|---|---|
| GA | General American (rhotic) |
| RP | Received Pronunciation / Standard Southern British English (non-rhotic) |

### General Principles

Four organising principles govern how letters map to sounds.

- **One-to-many:** A single grapheme maps to multiple phonemes depending on position, etymology, and following letters.
  - c -> `/k/` (cat), `/s/` (city)
  - g -> `/ɡ/` (go), `/dʒ/` (gem)
  - a -> `/æ/` (cat), `/eɪ/` (face), `/ɑː/`~`/ɒ/` (father/want), `/ə/` (about)
  - ough -> `/ɔː/` (thought), `/ʌf/` (rough), `/oʊ/`~`/əʊ/` (though), `/uː/` (through), `/aʊ/` (bough), `/ɒf/`~`/ɔːf/` (cough)
- **Many-to-one:** Several distinct graphemes spell a single phoneme.
  - `/f/` <- f (fan), ff (off), ph (phone), gh (laugh)
  - `/iː/` <- ee (see), ea (eat), e_e (these), ie (field), ei (receive), ey (key), i (machine)
  - `/eɪ/` <- a_e (cake), ai (rain), ay (day), ei (vein), ey (they), ea (great)
  - `/k/` <- c (cat), k (kit), ck (back), q(u) (quick), ch (chord), cc (account)
- **Positional conditioning:** Pronunciation is conditioned by surrounding graphemes.
  - Soft c/g before e, i, y (cent, gym) vs hard before a, o, u (cat, gum)
  - Magic-e (VCe) signals a 'long'/free vowel: hat -> hate, hop -> hope
  - Vowel + r yields an r-controlled vowel distinct from the plain vowel: ca-t vs car
- **Morphophonemic stability:** Spelling preserves morpheme identity across alternating pronunciations, prioritising the visual word over phonemic transparency.
  - sign `/saɪn/` ~ signal `/ˈsɪɡnəl/` (silent g surfaces in derivative)
  - nation `/ˈneɪʃ(ə)n/` ~ native `/ˈneɪtɪv/` (t spells `/ʃ/` vs `/t/`)
  - electric `/k/` ~ electricity `/s/` ~ electrician `/ʃ/`
  - heal `/iː/` ~ health `/ɛ/`

### Consonant Graphemes

Consonant letters and digraphs and their phoneme mappings. Single consonant letters are mostly regular; the system's complexity lies in digraphs (sh, ch, th, ng, ph, wh, gh), the soft/hard alternation of c and g, doubled consonants, and the cluster letters x and qu. (`∅` denotes a silent/null realisation.)

#### Single Letters

| Grapheme | IPA | Examples | Note |
|---|---|---|---|
| b | `/b/` | bat; rob | Silent in mb (comb, lamb) and bt (doubt, debt). |
| c | `/k/`, `/s/` | cat /k/; city /s/ | Hard `/k/` before a, o, u and consonants; soft `/s/` before e, i, y. See soft/hard alternation. |
| d | `/d/`, `/dʒ/` | dog /d/; soldier /dʒ/; educate /dʒ/ (casual) | `/dʒ/` by yod-coalescence before `/juː/` in some words. |
| f | `/f/` | fan; leaf | Exception: of `/ɒv/`~`/əv/` where f = `/v/`. |
| g | `/ɡ/`, `/dʒ/` | go /ɡ/; gem /dʒ/ | Hard `/ɡ/` before a, o, u; soft `/dʒ/` often before e, i, y (but many exceptions: get, give, girl = `/ɡ/`). See soft/hard alternation. |
| h | `/h/`, `∅` | hat /h/; hour ∅; honest ∅ | Silent in some Romance loans and after some consonants (digraphs). |
| j | `/dʒ/` | jam; major | Rarely `/j/` (hallelujah) or `/h/` (Spanish loans, jalapeño). |
| k | `/k/`, `∅` | kite /k/; knee ∅ | Silent in word-initial kn. |
| l | `/l/`, `∅` | leaf /l/; walk ∅; calm ∅ | Clear [l] before vowels, dark [ɫ] in codas; silent in alk, alf, alm, ould. |
| m | `/m/` | man; ham | Syllabic [m̩] in some unstressed endings (rhythm). |
| n | `/n/`, `/ŋ/` | net /n/; ink /ŋ/ (n before k/g) | Realised [ŋ] before velars; silent after m word-finally (hymn, autumn). |
| p | `/p/`, `∅` | pen /p/; psalm ∅; receipt ∅ | Silent in initial ps, pt, pn (Greek) and a few others. |
| q | `/k/` | queen; quit | Almost always written qu = `/kw/`; see qu entry. |
| r | `/r/` | red; car (GA) | Phonetically [ɹ]. GA rhotic: pronounced in all positions. RP non-rhotic: silent in codas (car [kɑː]) unless linking to a following vowel. |
| s | `/s/`, `/z/`, `/ʃ/`, `/ʒ/` | sun /s/; dogs /z/; sure /ʃ/; vision /ʒ/ | `/z/` intervocalically and in voiced plurals; `/ʃ/`~`/ʒ/` before `/j/` glide (sugar, measure). |
| t | `/t/`, `/ʃ/`, `/tʃ/` | top /t/; nation /ʃ/ (tion); nature /tʃ/ | `/ʃ/` in -tion/-tial; `/tʃ/` by coalescence before `/juː/`. GA flaps intervocalic `/t/` to [ɾ] (water). |
| v | `/v/` | van; love | Very regular; English words avoid final v, hence silent e (love, give). |
| w | `/w/`, `∅` | win /w/; write ∅; sword ∅; two ∅ | Silent in initial wr and a few clusters; part of digraphs wh, aw, ow, ew. |
| x | `/ks/`, `/ɡz/`, `/z/` | box /ks/; exam /ɡz/; xylophone /z/ | `/ks/` default; `/ɡz/` when before a stressed vowel; `/z/` word-initially (Greek). |
| y | `/j/`, `/ɪ/`, `/iː/`~`/i/`, `/aɪ/` | yes /j/; gym /ɪ/; happy /i/; my /aɪ/; type /aɪ/ | Consonant `/j/` word-initially; otherwise a vowel grapheme. See Vowel Graphemes. |
| z | `/z/`, `/ts/`, `/ʒ/` | zoo /z/; pizza /ts/; seizure /ʒ/ | `/z/` default; `/ts/` in some loans; `/ʒ/` before yod glide. |

#### Digraphs

| Grapheme | IPA | Examples | Note |
|---|---|---|---|
| sh | `/ʃ/` | ship; wash | Stable digraph for the voiceless postalveolar fricative; no single Latin letter for `/ʃ/`. |
| ch | `/tʃ/`, `/k/`, `/ʃ/` | chair /tʃ/; chorus /k/; chef /ʃ/ | `/tʃ/` native default; `/k/` in Greek-origin words (chaos, school); `/ʃ/` in French loans (machine, brochure). |
| tch | `/tʃ/` | catch; watch; kitchen | Spelling of `/tʃ/` after a short (checked) vowel; cf. 'rich', 'much' without t. |
| th | `/θ/`, `/ð/` | thin /θ/; this /ð/; bath /θ/; bathe /ð/ | Voiceless `/θ/` vs voiced `/ð/` are not distinguished in spelling; `/ð/` typical in grammatical/function words (the, this, that, then) and medial position, `/θ/` in content words and finally. Sometimes `/t/` in names (Thomas, Thames). |
| ng | `/ŋ/`, `/ŋɡ/` | sing /ŋ/; finger /ŋɡ/; longer /ŋɡ/ | Word-final and before suffixes `/ŋ/`; `/ŋɡ/` in the middle of morpheme-internal words and comparatives. `/ndʒ/` when followed by soft-g spelling (danger, hinge). |
| ph | `/f/`, `/v/` | phone /f/; graph /f/; Stephen /v/ | Greek-origin spelling of `/f/`; `/v/` exceptionally in 'Stephen', 'nephew' (older RP). |
| wh | `/w/`, `/h/` | what /w/; who /h/ | Usually `/w/` in modern GA/RP (wine-whine merger); conservative/Scottish/Irish and some GA speakers keep `/ʍ/` (voiceless [w̥]). `/h/` before back rounded vowel (who, whole, whose). |
| gh | `/f/`, `/ɡ/`, `∅` | laugh /f/; ghost /ɡ/; night ∅; though ∅ | Once `/x/` (velar fricative); now `/f/` in some codas (rough, cough), `/ɡ/` initially (ghost, ghetto), and silent after a vowel (high, weigh, daughter), often leaving the preceding vowel 'long'. |
| rh | `/r/` | rhyme; rhythm; rhino | Greek-origin spelling; h is silent. |
| gn | `/n/`, `/ɡn/` | gnaw /n/ (initial); sign /n/ (final); signal /ɡn/ | Silent g word-initially and word-finally; both pronounced when split across a morpheme/syllable boundary (sig-nal, ig-nore). |
| kn | `/n/` | knee; knife; know | Word-initial; k is silent (formerly `/kn/`). |
| wr | `/r/` | write; wrong; wrist | Word-initial; w is silent (formerly `/wr/`). |
| ck | `/k/` | back; sick; rocket | Spelling of `/k/` after a short (checked) vowel; doubled-consonant analogue of single c/k. |
| dg(e) | `/dʒ/` | bridge; judge; badger | Spelling of `/dʒ/` after a short vowel; the d marks the preceding vowel as short. |
| qu | `/kw/`, `/k/` | queen /kw/; quick /kw/; antique /k/; quiche /k/ | `/kw/` native default; `/k/` in French loans where the vowel after qu is silent or final (-que = `/k/`: unique, plaque). |
| ti/ci/si (+ vowel) | `/ʃ/`, `/ʒ/` | nation /ʃ/; special /ʃ/; vision /ʒ/; occasion /ʒ/ | Palatalisation of t/c/s before an unstressed front vowel + vowel in Latinate suffixes (-tion, -cial, -sion). The parallel 'su' palatalisation (measure, pleasure, sure) is a separate pattern not covered here. |
| ps/pt/pn | `/s/`, `/t/`, `/n/` | psalm /s/; ptarmigan /t/; pneumonia /n/ | Word-initial Greek clusters with silent p. |

#### Doubled Consonants

A doubled consonant letter spells a single consonant phoneme; its primary function is orthographic, marking the preceding vowel as 'short' (checked) and blocking the magic-e 'long' reading.

**Rule:** `<CC>` -> single `/C/`

| Word | IPA | Contrast | Note |
|---|---|---|---|
| hopping | `/ˈhɒpɪŋ/` (RP), `/ˈhɑːpɪŋ/` (GA) | hoping `/ˈhoʊpɪŋ/`~`/ˈhəʊpɪŋ/` | pp keeps the `/ɒ/`~`/ɑː/` short; single p triggers GOAT. |
| diner vs dinner | `/ˈdaɪnər/` vs `/ˈdɪnər/` |  | Single n -> PRICE; double nn -> KIT. |
| comma | `/ˈkɒmə/`~`/ˈkɑːmə/` |  | mm = single `/m/`. |

Exceptions, where a doubled letter does more than spell a single consonant:

| Grapheme | IPA | Examples | Note |
|---|---|---|---|
| ss | `/s/`, `/z/`, `/ʃ/`, `/ʒ/` | miss /s/; scissors /z/; issue /ʃ/; pleasure-type spellings; dessert (s+s) /z/ | ss usually `/s/` but `/z/` in 'dessert', 'possess', `/ʃ/` in 'issue', 'tissue'. |
| cc | `/k/`, `/ks/` | account /k/; accept /ks/; accident /ks/ | `/ks/` when the second c is soft (before e, i). |
| gg | `/ɡ/`, `/dʒ/` | egg /ɡ/; suggest /dʒ/ (one g soft) | Mostly `/ɡ/`; `/dʒ/` in 'suggest', 'exaggerate'. |

#### Soft/Hard Alternation of c and g

Inherited from Romance: the letters c and g have a 'hard' (velar/plosive) value before back vowels a, o, u and consonants, and a 'soft' (sibilant/affricate) value before the front vowels e, i, y. A silent 'u' or 'e' is often inserted to preserve or block a value.

| Letter | Value | IPA | Environment | Examples |
|---|---|---|---|---|
| c | hard | `/k/` | before a, o, u, consonant, word-finally | cat; cot; cut; clip; panic |
| c | soft | `/s/` | before e, i, y | cent; city; cycle; race |
| g | hard | `/ɡ/` | before a, o, u, consonant; many native words before e/i | gap; got; gut; glad; get; give; girl |
| g | soft | `/dʒ/` | frequently before e, i, y (esp. Latinate) | gem; giant; gym; age; magic |

*g is less predictable than c: many high-frequency Germanic words keep hard g before front vowels (get, give, gift, gear, geese, girl, begin).*

Preservation devices that keep or block a value:

| Device | Function | Examples |
|---|---|---|
| silent u after g | keeps g hard before e/i | guess; guitar; guard; vague |
| silent u after q | etymological; qu = `/kw/` | quick; quiet |
| e to soften c/g word-finally | shows soft value and marks long vowel | page `/peɪdʒ/`; ice `/aɪs/`; change `/tʃeɪndʒ/` |
| k or ck after hard c | keeps `/k/` before e/i in derivatives | picnic -> picnicking; panic -> panicky |

### Vowel Graphemes

The five (six with y) vowel letters a, e, i, o, u (y) each spell several vowel phonemes. The core English convention distinguishes a 'short'/CHECKED value (in a closed syllable, often before a doubled consonant), a 'long'/FREE value (typically the Great-Vowel-Shifted reflex, signalled by magic-e or an open syllable), and a REDUCED value `/ə/`~`/ɪ/` in unstressed syllables. Lexical-set labels follow Wells (1982). GA/RP differences are noted; the most pervasive is r-control (GA rhotic vs RP non-rhotic).

#### Single Vowel Letters

The table gives, for each vowel letter, its short/checked value, its long/free value, and its reduced (unstressed) value, each with the Wells lexical set.

| Grapheme | Short/checked (set) | Long/free (set) | Reduced (set) |
|---|---|---|---|
| a | `/æ/` — TRAP (cat, man, happy) | `/eɪ/` — FACE (table, apron, name [magic-e]) | `/ə/` — commA (about, sofa, comma) |
| e | `/ɛ/` — DRESS (bed, pen, met) | `/iː/` — FLEECE (be, these [magic-e], even) | `/ə/`, `/ɪ/` — commA / KIT (taken /ə/, wanted /ɪ/~/ə/, roses /ɪ/) |
| i | `/ɪ/` — KIT (sit, big, fish) | `/aɪ/` — PRICE (time [magic-e], find, child, I) | `/ɪ/`~`/ə/` (pencil, animal, possible) |
| o | `/ɒ/` (RP) ~ `/ɑː/` (GA) — LOT (hot, dog, box) | `/oʊ/` (GA), `/əʊ/` (RP) — GOAT (go, note [magic-e], open, old) | `/ə/` (lemon, second, method) |
| u | `/ʌ/` — STRUT (cup, but, sun) | `/juː/`, `/uː/` — GOOSE with/without yod (cube /juː/, use /juː/, rule /uː/, tune /tjuːn/[RP]~/tuːn/[GA]) | `/ə/` (circus, album, support) |
| y | `/ɪ/` — KIT (gym, myth, system) | `/aɪ/` — PRICE (my, type [magic-e], cry, fly) | `/i/`~`/ɪ/` (happy, rhythm [syllabic]) |

Additional ("other") values of each vowel letter:

| Grapheme | IPA | Lexical set | Examples | Note |
|---|---|---|---|---|
| a | `/ɑː/` (RP) ~ `/æ/` (GA) | BATH | path; grass; dance | TRAP-BATH split: RP has long back `/ɑː/`, GA keeps `/æ/`. |
| a | `/ɒ/` (RP) ~ `/ɑː/` (GA) | LOT | want; wash; swan | After `/w/`, a -> LOT vowel. |
| a | `/ɔː/` | THOUGHT | all; talk; water | Before l and in 'water', 'all'. |
| e | `∅` |  | the silent final e of name, here, love | Word-final e is usually silent; functions as magic-e or to soften c/g/avoid final v/s. |
| i | `/iː/` | FLEECE | machine; ski; pizza; police | Retains continental value in some loans. |
| i | `/j/` |  | onion; million | Before a vowel in some words, i = glide `/j/`. |
| o | `/ʌ/` | STRUT | son; love; come; month | 'o' spelling of `/ʌ/`, often where a written u was avoided next to m/n/v. |
| o | `/uː/` | GOOSE | do; who; move; lose |  |
| o | `/ʊ/` | FOOT | wolf; woman; bosom |  |
| o | `/ɒ/` (RP) ~ `/ɔ/`~`/ɔː/` (GA) | CLOTH | off; cross; dog (some GA) | LOT-CLOTH split: the LOT-CLOTH split raises these to `/ɔ/` (merging with THOUGHT) for many GA speakers, while modern RP keeps LOT `/ɒ/`. The older `/ɔː/` ('orf', 'crorss') CLOTH pronunciation is now archaic/conservative RP and no longer Standard Southern British English. |
| o | `/wʌ/` |  | one /wʌn/; once /wʌns/ | Idiosyncratic; o spells `/wʌ/`. |
| u | `/ʊ/` | FOOT | put; full; push; bull | FOOT-STRUT split: northern English lacks this contrast. |
| u | `∅` |  | guess; guitar; build | Silent u keeping g hard or as etymological filler. |
| u | `/w/` |  | quick (qu=/kw/); language; persuade | u = glide `/w/` after g/q/s. |
| y | `/j/` |  | yes; yard | Word-initial consonant glide. |
| y | `/i/` (happY) | happY | happy; city; money | Word-final unstressed; tense [i] in GA and modern RP (happy-tensing), traditionally `/ɪ/`. |

#### Magic-e (VCe)

The 'magic-e' / split-digraph / VCe convention: a silent final e signals that the preceding single vowel grapheme takes its 'long'/free (Great-Vowel-Shifted) value, with one consonant between them (Vowel-Consonant-e). The e is itself unpronounced.

**Pattern:** V + C + silent e

| Checked | Free | Vowel |
|---|---|---|
| cap `/kæp/` | cape `/keɪp/` | a -> FACE `/eɪ/` |
| pet `/pɛt/` | Pete `/piːt/` | e -> FLEECE `/iː/` |
| bit `/bɪt/` | bite `/baɪt/` | i -> PRICE `/aɪ/` |
| hop `/hɒp/`~`/hɑːp/` | hope `/hoʊp/`~`/həʊp/` | o -> GOAT `/oʊ/`~`/əʊ/` |
| cub `/kʌb/` | cube `/kjuːb/` | u -> GOOSE `/juː/` |
| tub `/tʌb/` | tube `/tjuːb/`~`/tuːb/` | u -> GOOSE |

- The e also commonly serves to soften a preceding c or g (ice, page) and to avoid a word ending in v, u, or single s (have, love, blue, house).
- When a vowel-suffix is added, the silent e is dropped but its lengthening effect is taken over by the syllable structure (hope -> hoping, not hopping).

#### Vowel Digraphs

| Grapheme | IPA | Lexical set | Examples | Note |
|---|---|---|---|---|
| ai | `/eɪ/` | FACE | rain; train; wait | Mid-word; word-final equivalent is 'ay'. |
| ay | `/eɪ/` | FACE | day; play; stay | Word-final spelling of `/eɪ/`. |
| ea | `/iː/`, `/ɛ/`, `/eɪ/` | FLEECE / DRESS / FACE | eat /iː/; bread /ɛ/; great /eɪ/ | Classic one-to-many digraph; `/iː/` most common, `/ɛ/` in a closed set (head, dead, health), `/eɪ/` in great/break/steak. |
| ee | `/iː/` | FLEECE | see; tree; free | Very regular spelling of `/iː/`. |
| ie | `/iː/`, `/aɪ/`, `/ɪ/`, `/ɛ/` | FLEECE / PRICE / KIT / DRESS | field /iː/; pie /aɪ/; sieve /ɪ/; friend /ɛ/ | `/iː/` mid-word (i before e), `/aɪ/` word-finally (pie, tie, die); `/ɛ/` exceptionally in 'friend'. |
| ei | `/iː/`, `/eɪ/`, `/aɪ/` | FLEECE / FACE / PRICE | receive /iː/; vein /eɪ/; height /aɪ/ | 'i before e except after c' rule covers receive/ceiling vs believe. |
| oa | `/oʊ/`, `/əʊ/` | GOAT | boat; road; coat | Regular spelling of GOAT; before r -> FORCE (board, soar). |
| oo | `/uː/`, `/ʊ/`, `/ʌ/` | GOOSE / FOOT / STRUT | moon /uː/; book /ʊ/; blood /ʌ/ | `/uː/` default; `/ʊ/` in a set (book, good, foot, wood); `/ʌ/` exceptionally (blood, flood). |
| ou | `/aʊ/`, `/uː/`, `/ʌ/`, `/oʊ/`~`/əʊ/`, `/ʊ/`, `/ɔː/` | MOUTH / GOOSE / STRUT / GOAT / FOOT / THOUGHT | out /aʊ/; soup /uː/; touch /ʌ/; soul /oʊ/; could /ʊ/; bought /ɔː/ | One of the most overloaded digraphs; the 'ough' string is especially irregular. |
| ow | `/aʊ/`, `/oʊ/`~`/əʊ/` | MOUTH / GOAT | cow /aʊ/; now /aʊ/; snow /oʊ/; low /oʊ/ | Two readings unpredictable from spelling (bow the ship's front /aʊ/ vs bow with a ribbon /oʊ/). |
| oy | `/ɔɪ/` | CHOICE | boy; toy; enjoy | Word-final spelling of `/ɔɪ/`; mid-word equivalent is 'oi'. |
| oi | `/ɔɪ/` | CHOICE | coin; voice; oil | Mid-word spelling of `/ɔɪ/`. |
| au | `/ɔː/`, `/ɒ/` (GA varies) | THOUGHT | caught; August; fault | `/ɔː/`; some GA speakers with the cot-caught merger have `/ɑː/`. Exceptions: aunt, laugh. |
| aw | `/ɔː/` | THOUGHT | saw; law; dawn | Word-final/pre-consonant spelling of `/ɔː/`. |
| ew | `/juː/`, `/uː/` | GOOSE | new /njuː/(RP)~/nuː/(GA); few /juː/; flew /uː/; blew /uː/ | With or without yod by the same yod-dropping rule as 'u'. |
| ey | `/eɪ/`, `/iː/` | FACE / FLEECE | they /eɪ/; grey /eɪ/; key /iː/; money /i/ | Word-final; `/eɪ/` stressed, `/i/` unstressed (happY-type), `/iː/` in 'key'. |
| ue | `/uː/`, `/juː/` | GOOSE | blue /uː/; true /uː/; cue /juː/ | Often the 'u' free value spread across a final cluster (-ue). |
| ui | `/uː/`, `/ɪ/` | GOOSE / KIT | fruit /uː/; suit /uː/; build /ɪ/; guitar /ɪ/ | `/uː/` in fruit/juice; `/ɪ/` where u is silent (build, guilt). |

#### r-Controlled (Rhotacised) Vowels

A vowel letter followed by r forms an r-controlled (rhotacised) vowel. In GA (rhotic) the r colours the vowel and is pronounced [ɚ]/[ɝ] or as a following [ɹ]. In RP (non-rhotic) the r is not pronounced before a consonant or pause; it leaves a long monophthong or a centring diphthong, and only surfaces as 'linking r' before a vowel. Lexical sets: NURSE, START, NORTH, FORCE, NEAR, SQUARE, CURE, lettER.

Stressed r-controlled vowels:

| Grapheme | IPA (GA) | IPA (RP) | Lexical set | Examples | Note |
|---|---|---|---|---|---|
| ar | `/ɑːr/` | `/ɑː/` | START | car; far; park | Some words: war/warm -> NORTH `/ɔːr/`~`/ɔː/` after w. |
| er | `/ɝː/` | `/ɜː/` | NURSE | her; term; serve | Merges with ir/ur in NURSE for most speakers. |
| ir | `/ɝː/` | `/ɜː/` | NURSE | bird; first; girl | NURSE merger. |
| or | `/ɔːr/` | `/ɔː/` | NORTH/FORCE | for; north; more; born | NORTH (for, born) and FORCE (more, four) merged in GA and RP. 'wor' -> NURSE (word, work). |
| ur | `/ɝː/` | `/ɜː/` | NURSE | fur; turn; burn | NURSE merger. |
| yr | `/ɝː/` | `/ɜː/` | NURSE | myrtle; myrrh | y in NURSE environment. |

Vowel + re / ear sequences:

| Grapheme | IPA (GA) | IPA (RP) | Lexical set | Examples | Note |
|---|---|---|---|---|---|
| are | `/ɛr/`~`/ɛər/` | `/ɛə/` | SQUARE | care; share; dare | SQUARE; a + r + e. |
| ear | `/ɪr/`, `/ɝː/`, `/ɛr/` | `/ɪə/`, `/ɜː/`, `/ɛə/` | NEAR / NURSE / SQUARE | near /ɪə/; earth /ɜː/; bear /ɛə/ | Three readings: NEAR (near, fear), NURSE (earth, learn), SQUARE (bear, pear, wear). |
| eer | `/ɪr/` | `/ɪə/` | NEAR | deer; cheer; beer | NEAR. |
| ere | `/ɪr/`, `/ɛr/` | `/ɪə/`, `/ɛə/` | NEAR / SQUARE | here /ɪə/; there /ɛə/; where /ɛə/ | NEAR in here/sphere; SQUARE in there/where. |
| air | `/ɛr/` | `/ɛə/` | SQUARE | air; hair; fair | SQUARE. |
| oor/our | `/ʊr/`, `/ɔːr/` | `/ʊə/`, `/ɔː/` | CURE / NORTH | poor /ʊə/~/ɔː/; tour /ʊə/; four /ɔː/; your /ɔː/ | CURE (poor, tour) increasingly merges into NORTH/THOUGHT in RP ('CURE-lowering'). |
| ure | `/jʊr/`~`/jɝ/` | `/jʊə/`~`/jɔː/` | CURE | cure; pure; secure | CURE with preceding yod; reduced -ure = `/ər/` (nature, picture). |

Unstressed lettER (the reduced r-coloured ending):

| Grapheme | IPA (GA) | IPA (RP) | Lexical set | Examples | Note |
|---|---|---|---|---|---|
| er/ar/or/ure/our | `/ɚ/` | `/ə/` | lettER | letter; dollar; doctor; measure /-ʒə(r)/; colour/color | Unstressed syllabic r-coloured schwa; GA [ɚ], RP [ə] with linking r before a vowel. |

### Silent Letters

Letters retained in spelling that are not pronounced in the modern standard accents, mostly fossils of historical sound changes or etymological re-spellings. The IPA column gives the modern pronunciation of the example word.

| Grapheme | Example | IPA | Note |
|---|---|---|---|
| k (initial kn) | knife | `/naɪf/` | Initial `/kn/` simplified; cf. knee, know, knock, knee. |
| k (initial kn) | knee | `/niː/` | Same change. |
| b (mb) | comb | `/koʊm/`, `/kəʊm/` | Silent b after m word-finally; cf. lamb, thumb, climb, bomb. |
| b (bt) | doubt | `/daʊt/` | Etymological b inserted (Latin dubitare); also debt, subtle. |
| w (initial wr) | write | `/raɪt/` | Initial `/wr/` simplified; cf. wrong, wrist, wrap, wreck. |
| w (cluster) | sword | `/sɔːrd/`, `/sɔːd/` | Silent w; also two `/tuː/`, answer `/ˈænsər/`. |
| gh (igh/eigh) | night | `/naɪt/` | gh once `/x/`; now silent, vowel diphthongised; cf. light, high, weigh, eight, daughter. |
| gh (ough silent) | though | `/ðoʊ/`, `/ðəʊ/` | Silent gh; cf. dough, through, bough. |
| l (alk) | walk | `/wɔːk/`, `/wɔːk/` | Silent l before k; cf. talk, chalk, folk, yolk. |
| l (alm/alf) | calm | `/kɑːm/`, `/kɑːm/` | Silent l; cf. palm, half, calf, salmon, would, could, should. |
| t (stl/ften) | castle | `/ˈkæsəl/`, `/ˈkɑːsəl/` | Silent t; cf. listen, whistle, often (variable), Christmas. |
| h (initial/Romance) | hour | `/aʊər/`, `/aʊə/` | Silent h; cf. honest, honour, heir. |
| h (after g/r) | ghost | `/ɡoʊst/`, `/ɡəʊst/` | h silent within digraphs gh-, rh-; cf. rhyme, rhythm. |
| g (gn) | sign | `/saɪn/` | Silent g in gn; surfaces in signal/signature; cf. gnaw, design, foreign, reign. |
| n (mn) | autumn | `/ˈɔːtəm/` | Silent n after m word-finally; surfaces in autumnal; cf. hymn, column, condemn. |
| p (initial ps/pt/pn) | psalm | `/sɑːm/`, `/sɑːm/` | Greek silent p; cf. pneumonia, pterodactyl, psychology, receipt. |
| c (sc) | scissors | `/ˈsɪzərz/`, `/ˈsɪzəz/` | Silent c in sci-; cf. science, scene, scent, muscle. |
| s (Romance) | island | `/ˈaɪlənd/` | Silent s (etymologically intrusive); cf. aisle, isle, debris. |
| u (gu/qu) | guess | `/ɡɛs/` | Silent u keeping g hard; cf. guitar, guard, tongue, league. |
| e (final magic-e) | name | `/neɪm/` | Final e silent; marks the long vowel and/or softens c/g. |
| d (dge/handsome) | Wednesday | `/ˈwɛnzdeɪ/`, `/ˈwɛnzdi/` | Silent d; cf. handkerchief, handsome (often). |

### Notes

- Estimates put fully regular grapheme-to-phoneme spellings at well under half of English vocabulary; high-frequency function words (the, of, one, two, said, are, was) are among the most irregular.
- English uses 26 letters for ~44 phonemes; the deficit is met by digraphs (sh, ch, th, ng, ph, wh) and by context-sensitive rules (soft/hard c/g, magic-e, doubling, r-control).
- The Great Vowel Shift (c. 1400-1700) explains why the 'long' values of the vowel letters are diphthongs or raised monophthongs (a=`/eɪ/`, i=`/aɪ/`, o=`/oʊ/`) that no longer match their continental-alphabet values, while the spellings were frozen by the printing press.
- Spelling tends to preserve morphemic identity over phonemic transparency: the same letters can spell different sounds across a word family (sign~signal, electric~electricity~electrician, photograph~photography) so the shared root stays visible.
- GA and RP share the orthography; the principal pronunciation differences read off the same spelling are rhoticity (post-vocalic r: pronounced in GA, vocalised in RP), the TRAP-BATH split (RP `/ɑː/` vs GA `/æ/` in path/dance), the LOT vowel (RP `/ɒ/` vs GA `/ɑː/`), and yod-dropping after coronals (GA tune `/tuːn/` vs RP `/tjuːn/`).
- The 'ough' string is the canonical example of orthographic opacity, spelling at least seven values: thought `/ɔː/`, though `/oʊ~əʊ/`, through `/uː/`, rough `/ʌf/`, cough `/ɒf~ɔːf/`, bough `/aʊ/`, hiccough `/ʌp/`.
- Doubled consonants and the magic-e are complementary length cues for the preceding vowel: hopping (short) vs hoping (long), dinner (short) vs diner (long).

## Weak Forms & Connected Speech

Weak forms (reduced pronunciations of function words) and the segmental processes of connected (running) speech in Modern English. This is the English analog to the Peshitta guide's reduced-vowel (shva) system extended to cover sandhi phenomena at word boundaries. In citation/isolation, function words carry a full "strong form"; in the unstressed flow of an utterance they typically reduce to a "weak form", most often centring on schwa `/ə/` or syllabic consonants. Connected speech then further reshapes word boundaries through linking, assimilation, coalescence, elision, and gemination.

**Applies to:** Spontaneous and fluent connected speech in both reference accents. Strong forms surface in citation, contrastive emphasis, utterance-final position, and after a preceding preposition for certain pronouns. Weak forms and the listed processes are variable and rate-dependent: they increase with speech tempo and informality, and decrease in careful or emphatic speech.

### Reference Accents

- **GA:** General American (rhotic; linking-r present, intrusive-r marginal/absent in conservative GA)
- **RP:** Received Pronunciation / Standard Southern British English (non-rhotic; linking-r and intrusive-r both productive)

**Schwa note:** The mid-central vowel `/ə/` (commA, lettER) is the principal vowel of English weak forms, exactly as it is the most frequent vowel of unstressed syllables generally. Weak forms may also reduce to `/ɪ/` (e.g. the prevocalic "the"), to a syllabic consonant `/n̩, l̩, m̩/`, or to zero (full elision of the vowel).

### Weak Forms

| Word | Category | Strong Form | Weak Form | Example in Context |
|---|---|---|---|---|
| a | indefinite article | `/eɪ/` | `/ə/` | have a try `/hæv ə ˈtraɪ/`; strong form only when citing the word itself: "the letter a" `/ðə ˈletər ˈeɪ/` |
| an | indefinite article (prevocalic) | `/æn/` | `/ən/` (rare fast-speech variant `/n̩/`) | an apple `/ən ˈæpl̩/`; standard weak form: "not an issue" `/ˌnɒt ən ˈɪʃuː/` (syllabic `/n̩/` for "an" is a marginal fast-speech variant only) |
| the | definite article | `/ðiː/` | `/ðə/` before a consonant, `/ði/` before a vowel | the cat `/ðə ˈkæt/`; the apple `/ði ˈæpl̩/`; strong `/ðiː/` for emphasis or hesitation: "THE place to go" `/ˈðiː ˌpleɪs/` |
| and | coordinating conjunction | `/ænd/` | `/ən/`, `/ənd/`, `/n̩/`, `/n/` | fish and chips `/ˌfɪʃ ən ˈtʃɪps/`; bread and butter `/ˌbred n̩ ˈbʌtər/` (syllabic n after the released `/d/` context) |
| but | coordinating conjunction | `/bʌt/` | `/bət/` | slow but steady `/ˌsloʊ bət ˈstedi/` |
| that | conjunction / relativiser (NOT the demonstrative) | `/ðæt/` | `/ðət/` | I think that he left `/aɪ ˌθɪŋk ðət i ˈleft/`; the demonstrative "that book" keeps the strong form `/ˈðæt ˌbʊk/` |
| than | comparative conjunction | `/ðæn/` | `/ðən/` ~ `/ðn̩/` | bigger than ever `/ˌbɪɡər ðən ˈevər/` |
| as | conjunction / particle | `/æz/` | `/əz/` | as soon as possible `/əz ˌsuːn əz ˈpɒsəbl̩/` |
| of | preposition | `/ɒv/` (RP) ~ `/ʌv/` (GA) | `/əv/`, and `/ə/` before a consonant | a cup of tea `/ə ˌkʌp əv ˈtiː/`; lots of money `/ˌlɒts ə ˈmʌni/` (reduced to `/ə/` before consonant) |
| to | preposition / infinitive marker | `/tuː/` | `/tə/` before a consonant, `/tu/` ~ `/tʊ/` before a vowel | going to school `/ˌɡoʊɪŋ tə ˈskuːl/`; want to eat `/ˌwɒnt tu ˈiːt/` |
| from | preposition | `/frɒm/` (RP) ~ `/frʌm/` (GA) | `/frəm/` | back from work `/ˌbæk frəm ˈwɜːrk/` |
| for | preposition / conjunction | `/fɔːr/` (GA) ~ `/fɔː/` (RP) | `/fər/` (GA) ~ `/fə/` (RP); linking `/fər/` before a vowel in RP | waiting for you `/ˌweɪtɪŋ fər ˈjuː/`; thanks for asking `/ˌθæŋks fər ˈɑːskɪŋ/` (RP uses linking r before the vowel) |
| at | preposition | `/æt/` | `/ət/` | look at this `/ˌlʊk ət ˈðɪs/` |
| some | determiner (partitive/indefinite quantity) | `/sʌm/` | `/səm/` ~ `/sm̩/` | have some water `/ˌhæv səm ˈwɔːtər/`; strong `/sʌm/` when meaning "a certain": "SOME people think..." `/ˈsʌm ˌpiːpl̩/` |
| was | auxiliary / copula (BE, past sg.) | `/wɒz/` (RP) ~ `/wʌz/` (GA) | `/wəz/` | he was here `/hi wəz ˈhɪər/`; strong in negatives/finals: "Yes he was" `/ˈjes hi ˈwɒz/` |
| were | auxiliary / copula (BE, past pl.) | `/wɜːr/` (GA) ~ `/wɜː/` (RP) | `/wər/` (GA) ~ `/wə/` (RP) | they were waiting `/ðeɪ wər ˈweɪtɪŋ/` |
| is | copula / auxiliary (BE, 3sg.) | `/ɪz/` | `/z/` after a voiced sound, `/s/` after a voiceless sound (clitic), `/ɪz/` after a sibilant | she's ready `/ʃiz ˈredi/`; Jack's coming `/ˈdʒæks ˌkʌmɪŋ/`; the bus is full `/ðə ˈbʌs ɪz ˈfʊl/` (no clitic after sibilant) |
| are | copula / auxiliary (BE, pl.) | `/ɑːr/` (GA) ~ `/ɑː/` (RP) | `/ər/` (GA) ~ `/ə/` (RP); clitic `/r/` ~ ∅ | we are leaving `/wi ər ˈliːvɪŋ/`; we're off `/wɪər ˈɒf/` |
| am | copula / auxiliary (BE, 1sg.) | `/æm/` | `/əm/` ~ `/m/` (clitic in "I'm") | I am sure `/aɪ əm ˈʃʊər/`; I'm late `/aɪm ˈleɪt/` |
| has | auxiliary / verb (HAVE, 3sg.) | `/hæz/` | `/həz/`, `/əz/` (h-dropped), clitic `/z/` ~ `/s/` | she has gone `/ʃi həz ˈɡɒn/`; the deal's collapsed `/ðə ˈdiːlz kəˈlæpst/` |
| have | auxiliary / verb (HAVE) | `/hæv/` | `/həv/`, `/əv/` (h-dropped), clitic `/v/` | they have left `/ðeɪ həv ˈleft/`; should've known `/ˈʃʊdəv ˈnoʊn/` (note: "of"-sounding `/əv/`) |
| had | auxiliary / verb (HAVE, past) | `/hæd/` | `/həd/`, `/əd/` (h-dropped), clitic `/d/` | if I had known `/ɪf aɪ həd ˈnoʊn/`; I'd seen it `/aɪd ˈsiːn ɪt/` |
| do | auxiliary (DO) | `/duː/` | `/də/` before a consonant, `/du/` before a vowel | where do you live `/ˌweər də ju ˈlɪv/`; what do I do `/ˌwɒt du aɪ ˈduː/` (final lexical "do" stays strong) |
| does | auxiliary (DO, 3sg.) | `/dʌz/` | `/dəz/` | what does it mean `/ˌwɒt dəz ɪt ˈmiːn/` |
| can | modal auxiliary | `/kæn/` | `/kən/` ~ `/kn̩/` | I can swim `/aɪ kən ˈswɪm/`; contrast with stressed negative "can't" `/kɑːnt/` (RP) ~ `/kænt/` (GA), which is never reduced |
| could | modal auxiliary | `/kʊd/` | `/kəd/` | you could try `/ju kəd ˈtraɪ/` |
| shall | modal auxiliary | `/ʃæl/` | `/ʃəl/` ~ `/ʃl̩/` | shall we go `/ʃəl wi ˈɡoʊ/` |
| should | modal auxiliary | `/ʃʊd/` | `/ʃəd/` | you should rest `/ju ʃəd ˈrest/` |
| would | modal auxiliary | `/wʊd/` | `/wəd/`, `/əd/` (h-less-like reduction), clitic `/d/` | I would go `/aɪ wəd ˈɡoʊ/`; I'd go `/aɪd ˈɡoʊ/` |
| must | modal auxiliary | `/mʌst/` | `/məst/`, `/məs/` (with `/t/`-elision before a consonant) | you must come `/ju məs ˈkʌm/` (final `/t/` elided in the cluster before `/k/`) |
| you | personal pronoun (2nd person) | `/juː/` | `/ju/` ~ `/jə/` | see you later `/ˌsiː jə ˈleɪtər/`; coalesces after `/t d s z/`: "did you" → `/ˈdɪdʒu/` |
| he | personal pronoun (3sg. masc.) | `/hiː/` | `/hi/`, `/i/` (h-dropped after a word) | did he go `/ˌdɪd i ˈɡoʊ/` (h-dropped non-initially) |
| she | personal pronoun (3sg. fem.) | `/ʃiː/` | `/ʃi/` | is she here `/ɪz ʃi ˈhɪər/` (she has no h, so it reduces only in length/stress) |
| we | personal pronoun (1pl.) | `/wiː/` | `/wi/` | can we start `/kən wi ˈstɑːrt/` |
| them | personal pronoun (object, 3pl.) | `/ðem/` | `/ðəm/`, `/ðm̩/`, and colloquial `/əm/` ('em) | tell them now `/ˌtel ðəm ˈnaʊ/`; get 'em `/ˌɡet əm/` |
| his | possessive determiner (3sg. masc.) | `/hɪz/` | `/ɪz/` (h-dropped non-initially) | took his coat `/ˌtʊk ɪz ˈkoʊt/` |
| her | possessive determiner / object pronoun (3sg. fem.) | `/hɜːr/` (GA) ~ `/hɜː/` (RP) | `/ər/` (GA) ~ `/ə/` (RP), with h-dropping; `/hər/` utterance-initially | gave her a book `/ˌɡeɪv ər ə ˈbʊk/`; Her name is... `/ˈhɜː ˌneɪm/` (initial h kept) |
| your | possessive determiner (2nd person) | `/jɔːr/` (GA) ~ `/jɔː/` (RP) | `/jər/` (GA) ~ `/jə/` (RP); linking `/jər/` before a vowel | what's your name `/ˌwɒts jər ˈneɪm/` |
| there | existential "there" (NOT locative) | `/ðeər/` (GA) ~ `/ðeə/` (RP) | `/ðər/` (GA) ~ `/ðə/` (RP) | there is a problem `/ðər ɪz ə ˈprɒbləm/`; the locative adverb stays strong: "over THERE" `/ˌoʊvər ˈðeər/` |

### Weak-Form Rules

- **Strong form retained in citation and contrast** — Function words take their strong form when quoted in isolation, when contrastively stressed, or when contradicting an expectation. *Example:* "I said FROM Monday, not TO Monday" keeps both prepositions strong: `/frɒm/`, `/tuː/`
- **Strong form retained utterance-finally / stranded** — Prepositions and auxiliaries left at the end of a clause (stranded) cannot reduce and surface strong. *Example:* "Who are you waiting for?" → final "for" = `/fɔːr/` (GA) ~ `/fɔː/` (RP), never `/fər/`
- **H-dropping in pronominal/auxiliary weak forms** — Initial `/h/` of he, him, his, her, have, has, had drops when the word is unstressed and non-utterance-initial, leaving a schwa-onset weak form. *Example:* "tell him" `/ˈtel ɪm/`; "should have" `/ˈʃʊdəv/`. The `/h/` is retained when the word begins the utterance.
- **Syllabic-consonant weak forms** — After a homorganic or appropriate consonant, the schwa of and, can, than, them, shall may be absorbed into a syllabic nasal or lateral. *Example:* "rock and roll" `/ˌrɒk n̩ ˈroʊl/`; "shall we" `/ʃl̩ wi/`
- **Cliticisation of BE/HAVE auxiliaries** — is, has, are, am, have, had, would reduce beyond schwa to a single attached consonant (clitic), spelled with an apostrophe. *Example:* "it is" → it's `/ɪts/`; "they have" → they've `/ðeɪv/`; "I would/had" → I'd `/aɪd/`

### Connected-Speech Processes

#### Linking /r/ (liaison-r)

**Type:** linking

An orthographic but (in non-rhotic accents) otherwise-silent word-final `/r/` is pronounced when the next word begins with a vowel, bridging the two words. In rhotic GA the `/r/` is always present; the "linking" character is most salient in non-rhotic RP, where the same `/r/` is silent before a consonant or pause.

- **Notation:** `/r/` → `[ɹ]` / V_#V (realised; in RP also ∅ / _#C or _##)
- **Example:** "far away" RP `[ˌfɑːr əˈweɪ]` (r linked) vs "far behind" `[ˌfɑː bɪˈhaɪnd]` (r silent); "better off" `[ˌbetər ˈɒf]`

#### Intrusive /r/

**Type:** linking

A non-etymological `[ɹ]` inserted between a word ending in a non-high vowel (`/ə, ɑː, ɔː/`) and a following vowel, by analogy with linking-r. Productive in RP and other non-rhotic accents; generally absent or stigmatised in careful GA.

- **Notation:** ∅ → `[ɹ]` / {ə, ɑː, ɔː}_#V
- **Example:** "law and order" RP `[ˌlɔːr ən ˈɔːdə]`; "media event" `[ˌmiːdiə(r) ɪˈvent]`; "Asia and Africa" `[ˈeɪʒə(r) ən ˈæfrɪkə]`

#### Catenation / consonant-to-vowel liaison

**Type:** linking

A word-final consonant is re-syllabified as the onset of a following vowel-initial word, so the boundary is heard inside the second word rather than between them. The basic mechanism of smooth "joined-up" speech.

- **Notation:** ...C#V... → ...#CV... (C re-syllabified as onset)
- **Example:** "an apple" → `[ə.ˈnæ.pl̩]`; "pick it up" → `[ˌpɪ.kɪ.ˈtʌp]`; "find out" → `[ˌfaɪn.ˈdaʊt]`

#### Glide insertion (linking /j/ and /w/)

**Type:** linking

A predictable transitional glide bridges two vowels across a word boundary: `[j]` after a front/high-front vowel (`/iː, ɪ, eɪ, aɪ, ɔɪ/`) and `[w]` after a rounded/back-high vowel (`/uː, ʊ, oʊ/aʊ/`). The non-rhotic counterpart of linking-r for non-r vowels.

- **Notation:** ∅ → `[j]` / {iː,ɪ,eɪ,aɪ,ɔɪ}_#V ; ∅ → `[w]` / {uː,ʊ,oʊ,aʊ}_#V
- **Example:** "I agree" → `[aɪ‿j‿əˈɡriː]`; "go away" → `[ˌɡoʊ‿w‿əˈweɪ]`; "the end" (prevocalic "the") → `[ði‿j‿ˈend]`

#### Place assimilation (regressive, alveolar → labial/velar)

**Type:** assimilation

A word-final alveolar `/t, d, n/` adopts the place of articulation of a following consonant: → bilabial `[p, b, m]` before `/p, b, m/`, and → velar `[k, ɡ, ŋ]` before `/k, ɡ/`. Anticipatory (regressive) and very common at normal tempo. `/s, z/` may likewise become `[ʃ, ʒ]` before `/ʃ, j/`.

- **Notation:** `/t,d,n/` → `[p,b,m]` / _#{p,b,m}; `/t,d,n/` → `[k,ɡ,ŋ]` / _#{k,ɡ}
- **Example:** "ten boys" → `[tem ˈbɔɪz]`; "that man" → `[ðæp ˈmæn]`; "good girl" → `[ɡʊɡ ˈɡɜːl]`; "ten cups" → `[teŋ ˈkʌps]`; "this shop" → `[ðɪʃ ˈʃɒp]`

#### Voicing/manner assimilation

**Type:** assimilation

Secondary to place: a final voiced obstruent may partially devoice before a voiceless onset, and the function-word fricatives `/v, ð/` may assimilate. Generally weaker in English than place assimilation.

- **Notation:** `/z/` → `[s]` / _#C[-voice] (variable); `/ð/` → `[θ]` or geminate after voiceless
- **Example:** "have to" → `[ˈhæftə]` (lexicalised `/v/`→`[f]`); "used to" → `[ˈjuːstə]`

#### Coalescent assimilation (yod-coalescence / palatalisation)

**Type:** assimilation

A word-final alveolar `/t, d, s, z/` merges with a following `/j/` (usually the weak form of "you" or "your") into a single palato-alveolar affricate or fricative: `/t+j/` → `[tʃ]`, `/d+j/` → `[dʒ]`, `/s+j/` → `[ʃ]`, `/z+j/` → `[ʒ]`. Both segments are replaced by the coalesced one (mutual, not merely regressive).

- **Notation:** `/t,d,s,z/` + `/j/` → `[tʃ, dʒ, ʃ, ʒ]`
- **Example:** "don't you" → `/doʊntʃu/` `[ˈdoʊn.tʃə]`; "would you" → `/wʊdʒu/` `[ˈwʊ.dʒə]`; "miss you" → `[ˈmɪ.ʃə]`; "as you wish" → `[əˈʒə ˈwɪʃ]`

#### Elision of schwa (compression)

**Type:** elision

An unstressed `/ə/` in a weak syllable is deleted, often producing a syllabic consonant or compressing a syllable. Especially common in pretonic open syllables and the weak forms of function words.

- **Notation:** `/ə/` → ∅ / in unstressed syllables (with C becoming syllabic)
- **Example:** "police" → `[pəˈliːs]` ~ `[ˈpliːs]` (cluster as stressed-syllable onset); "tonight" → `[təˈnaɪt]` ~ `[ˈtnaɪt]`; "lots of" → `[ˈlɒts ə]` (the `/v/` of "of" also gone); "camera" → `[ˈkæm.rə]`

#### Elision of /t/ and /d/ (cluster simplification)

**Type:** elision

An alveolar stop `/t/` or `/d/` is deleted when it stands between two other consonants across a word boundary (or within a final cluster), typically when flanked by obstruents of the same voicing. The most frequent consonant elision in English.

- **Notation:** `/t,d/` → ∅ / C_#C (medial in a tri-consonantal sequence)
- **Example:** "last night" → `[ˌlɑːs ˈnaɪt]`; "next please" → `[ˌneks ˈpliːz]`; "old man" → `[ˌoʊl ˈmæn]`; "kept quiet" → `[ˌkep ˈkwaɪət]`; "must be" → `[ˌmʌs ˈbiː]`

#### Elision of /h/ (h-dropping in weak forms)

**Type:** elision

The `/h/` of unstressed pronouns and auxiliaries (he, him, his, her, have, has, had) is deleted in non-initial position. A connected-speech process distinct from accent-level h-dropping, since it applies even in standard accents that otherwise keep `/h/`.

- **Notation:** `/h/` → ∅ / [unstressed function word, non-utterance-initial]
- **Example:** "give him his book" → `[ˌɡɪv ɪm ɪz ˈbʊk]`; "what has he done" → `[ˌwɒt əz i ˈdʌn]`

#### Gemination across word boundaries (degemination/long hold)

**Type:** gemination

When a word ends in the same (or homorganic) consonant that the next word begins with, the two are not pronounced separately but realised as one long-held `[Cː]` with a single release. Length is the only cue to the boundary; failing to lengthen yields a perceived single word.

- **Notation:** C#C → `[Cː]` (single long consonant, one release)
- **Example:** "this Saturday" → `[ðɪsːˈætədeɪ]`; "big girl" → `[bɪɡːɜːl]`; "hot toast" → `[hɒtːoʊst]`; "ten names" → `[tenːeɪmz]`; "half full" → `[hɑːfːʊl]` (note: word-internal geminates such as "unknown" `/ʌnˈnoʊn/` → `[ʌnːoʊn]` are a related but distinct, non-boundary phenomenon)

#### /t/-glottalling and glottal reinforcement

**Type:** lenition

A word-final or pre-consonantal `/t/` is realised as a glottal stop `[ʔ]` (RP and many GA contexts before a consonant or pause). Common alongside elision and assimilation at boundaries.

- **Notation:** `/t/` → `[ʔ]` / _#C or _## (also `[ʔt]` reinforced)
- **Example:** "not now" → `[ˌnɒʔ ˈnaʊ]`; "that one" → `[ˌðæʔ ˈwʌn]`; "quite good" → `[ˌkwaɪʔ ˈɡʊd]`

#### /t, d/ flapping across word boundaries (GA)

**Type:** lenition

In General American, a word-final `/t/` or `/d/` becomes a voiced alveolar tap `[ɾ]` when followed by a vowel-initial word (catenation feeds flapping). Characteristic of GA; absent in conservative RP, which prefers glottalling.

- **Notation:** `/t,d/` → `[ɾ]` / V_#V (GA)
- **Example:** "get up" → GA `[ˌɡɛ.ˈɾʌp]`; "a lot of" → `[ə ˈlɑ.ɾə]`; "shut it" → `[ˌʃʌ.ˈɾɪt]`

### Interaction & Register

**Interaction note:** These processes feed one another and apply in cascade. A single phrase may show several at once: "don't you want to" → coalescence (`/t+j/`→`[tʃ]`) + `/t/`-elision in "want to" (→ "wanna" `/ˈwɒnə/`) + weak-form "to" → `[ˈdoʊn.tʃə ˈwɒ.nə]`. Likewise "last night" shows `/t/`-elision and may then feed place assimilation of the resulting `/s/`+`/n/`. Ordering generally: weak-form selection → assimilation/coalescence → elision → linking/catenation across the smoothed boundary.

**Rate and register note:** All weak forms and connected-speech processes are gradient and optional. Their frequency scales with speech rate and informality and drops sharply in slow, careful, or emphatic delivery, in which strong forms and full segments are restored. Citation forms in dictionaries list strong forms; the IPA of running speech requires these reductions to sound native.

**Cross-reference:** This section is the English counterpart to the Peshitta guide's "shva_system" (reduced vowel `/ə/`) and "phonological_rules" (assimilation, elision, gemination). Where the Peshitta documents Eastern vs Western traditions, the English guide documents GA vs RP; the principal divergence here is rhoticity, which governs linking-r, intrusive-r, flapping (GA) vs glottalling (RP), and the r-coloured vs schwa weak forms of for, your, her, there, are, were.

## Sample Words in IPA

37 illustrative English words transcribed in IPA for two reference accents — GA (General American) and RP (Received Pronunciation / Standard Southern British English), modeled on the Peshitta guide's parallel Eastern/Western tradition columns. The words are chosen to exercise the full segmental inventory (all 24 consonants and all monophthong and diphthong phonemes), every Wells (1982) Standard Lexical Set, a range of complex consonant clusters, and stress-placement contrasts (including stress-shift minimal pairs and word-internal vowel reduction). Each entry lists the phonemes it illustrates and the lexical sets it covers so the array as a whole forms a verifiable coverage matrix for the English phonological system.

*Words were selected illustratively (not corpus-sliced) to guarantee complete coverage: collectively they realize all 24 consonant phonemes, supply one keyword per monophthong lexical set, instantiate all closing and centring diphthongs, demonstrate marked onset and coda clusters (/sɪksθs/, /strɛŋkθs/), and contrast lexical stress and reduction (e.g. PHOtograph vs phoTOGraphy, COMFORTable, VEGetable). GA and RP transcriptions are given in parallel; where the two accents diverge (rhoticity, BATH/TRAP split, LOT rounding, GOAT/GOOSE quality, yod-dropping, /t/ allophony) both values are shown and the divergence is noted.*

*GA is rhotic: coda /r/ is pronounced as [ɹ] and is shown in transcriptions. RP is non-rhotic: historical coda /r/ is not pronounced except as a linking/intrusive [ɹ] before a following vowel; it surfaces instead as vowel length or a centring offglide. The NURSE, START, NORTH, FORCE, lettER, NEAR, SQUARE, and CURE entries make this contrast explicit.*

**Total sample words:** 37

| Word | GA | RP | Note | Lexical sets |
|---|---|---|---|---|
| thought | `/θɔt/` | `/θɔːt/` | THOUGHT keyword; voiceless dental fricative onset /θ/ + open-mid back rounded vowel + final /t/. GA THOUGHT is variably shorter and (in cot–caught merged speakers) merges with LOT; RP keeps a long rounded /ɔː/. | THOUGHT |
| measure | `/ˈmɛʒɚ/` | `/ˈmeʒə/` | Medial voiced postalveolar fricative /ʒ/ (rare except medially) + DRESS in the stressed syllable + reduced lettER ending. The coda /r/ surfaces only as GA rhoticity on the r-colored schwa [ɚ] and is entirely absent in RP (plain [ə]); it is therefore listed as 'ɚ' rather than as a /r/ consonant. | DRESS, lettER |
| sixths | `/sɪksθs/` | `/sɪksθs/` | Extreme four-consonant coda cluster /-ksθs/, a classic test of English syllable structure; KIT vowel. Often simplified in connected speech to [sɪksts] or [sɪks]. | KIT |
| strengths | `/strɛŋkθs/` | `/streŋkθs/` | Three-consonant /str-/ onset and a dense /-ŋkθs/ coda with epenthetic [k] between /ŋ/ and /θ/; velar nasal /ŋ/ and DRESS vowel. A maximal demonstration of English cluster phonotactics. | DRESS |
| rhythm | `/ˈrɪðm̩/` | `/ˈrɪðm̩/` | Approximant onset /r/ ([ɹ]), voiced dental fricative /ð/, and a syllabic bilabial nasal [m̩] forming the unstressed second syllable; KIT vowel. Minimal contrast of /ð/ (here) with /θ/ in 'thin'. | KIT |
| about | `/əˈbaʊt/` | `/əˈbaʊt/` | Initial unstressed commA schwa /ə/ + stressed MOUTH diphthong /aʊ/ + voiced /b/ onset. Demonstrates iambic stress and a word-initial reduced vowel. | commA, MOUTH |
| photograph | `/ˈfoʊtəˌɡræf/` | `/ˈfəʊtəɡrɑːf/` | Primary stress on syllable 1 (PHO-). GOAT diphthong differs by accent: GA [oʊ] vs RP [əʊ]. Final syllable shows the BATH/TRAP split — GA TRAP [ræf] vs RP BATH [rɑːf]. Voiceless labiodental /f/ twice. Contrast stress with 'photography' (next). | GOAT, commA, TRAP, BATH |
| photography | `/fəˈtɑɡrəfi/` | `/fəˈtɒɡrəfi/` | Stress shifts to syllable 2 (-TOG-) relative to 'photograph', triggering vowel reduction of syllables 1, 3, 4 to schwa. Stressed vowel is LOT: GA unrounded [ɑ] vs RP rounded [ɒ]. Final happY vowel /i/. The pair photograph~photography is a textbook stress-and-reduction alternation. | commA, LOT, happY |
| water | `/ˈwɔɾɚ/` | `/ˈwɔːtə/` | Labial-velar approximant /w/ onset; THOUGHT vowel; intervocalic /t/ realized in GA as a voiced alveolar tap [ɾ] (flapping) but as plain [t] in RP. lettER ending is rhotic [ɚ] in GA, schwa [ə] in RP — the coda /r/ is GA rhoticity only, so it is listed as 'ɚ' rather than as a /r/ consonant. | THOUGHT, lettER |
| tune | `/tun/` | `/tjuːn/` | GOOSE vowel. Yod contrast: RP retains the palatal glide /j/ after /t/ ([tjuːn], often coalesced to [tʃuːn]); GA drops the yod (yod-dropping) giving [tun]. Aspirated [tʰ] onset. | GOOSE |
| bath | `/bæθ/` | `/bɑːθ/` | The BATH lexical set itself: GA uses the short front TRAP vowel [æ], RP uses the long back PALM-like vowel [ɑː] (the BATH/TRAP split). Voiced /b/ onset, voiceless /θ/ coda. | BATH, TRAP, PALM |
| father | `/ˈfɑðɚ/` | `/ˈfɑːðə/` | PALM/START-quality open back unrounded vowel /ɑ(ː)/ in the stressed syllable + voiced dental fricative /ð/ + reduced lettER ending. GA is rhotic [ɚ]; RP non-rhotic [ə] — the coda /r/ is GA rhoticity only, so it is listed as 'ɚ' rather than as a /r/ consonant. Contrasts /ð/ with /θ/ of 'bath'. | PALM, lettER |
| going | `/ˈɡoʊɪŋ/` | `/ˈɡəʊɪŋ/` | Voiced velar plosive /ɡ/ onset; GOAT diphthong (GA [oʊ] / RP [əʊ]) in hiatus with KIT; velar nasal /ŋ/ in the -ing suffix (formal [ɪŋ], colloquial [ɪn]). | GOAT, KIT |
| square | `/skwɛr/` | `/skweə/` | Complex /skw-/ onset (fricative + plosive + approximant). SQUARE centring set: GA is rhotic with [ɛr]; RP is non-rhotic with a centring diphthong [ɛə] (monophthongizing to [ɛː] for many speakers). | SQUARE |
| cure | `/kjʊr/` | `/kjʊə/` | CURE centring set with preceding palatal glide /j/. GA rhotic [ʊr]; RP non-rhotic centring diphthong [ʊə], increasingly merged toward NORTH/THOUGHT [ɔː] in modern RP (the CURE–FORCE merger). Voiceless aspirated /k/ onset. | CURE |
| judge | `/dʒʌdʒ/` | `/dʒʌdʒ/` | Voiced postalveolar affricate /dʒ/ in both onset and coda; STRUT vowel /ʌ/. Pairs with 'church' to show the voiced/voiceless affricate contrast. | STRUT |
| church | `/tʃɝtʃ/` | `/tʃɜːtʃ/` | Voiceless postalveolar affricate /tʃ/ in onset and coda framing the NURSE vowel. GA has the rhotic mid-central vowel [ɝ] (which already encodes the rhoticity — there is no separate /r/ consonant segment); RP has non-rhotic long [ɜː] with no /r/ at all. Voiced counterpart in 'judge'. | NURSE |
| vision | `/ˈvɪʒən/` | `/ˈvɪʒn̩/` | Voiced labiodental fricative /v/ onset; medial /ʒ/ (from historic /zj/ coalescence); KIT vowel; final syllable a schwa+/n/ or syllabic [n̩]. Together with 'measure' and 'pleasure' it documents the limited distribution of /ʒ/. | KIT, commA |
| singer | `/ˈsɪŋɚ/` | `/ˈsɪŋə/` | Velar nasal /ŋ/ with NO following [ɡ] (morpheme boundary sing+er): [sɪŋ.ɚ]. Minimal pair with 'finger'. KIT vowel + reduced lettER ending (rhotic [ɚ] GA / [ə] RP) — the coda /r/ is GA rhoticity only, so it is listed as 'ɚ' rather than as a /r/ consonant. | KIT, lettER |
| finger | `/ˈfɪŋɡɚ/` | `/ˈfɪŋɡə/` | Velar nasal /ŋ/ FOLLOWED by [ɡ] (no morpheme boundary): [fɪŋ.ɡɚ]. The singer~finger pair shows that English /ŋ/+[ɡ] realization is morphologically conditioned. /f/ onset, KIT vowel, lettER ending — the coda /r/ is GA rhoticity only, so it is listed as 'ɚ' rather than as a /r/ consonant. | KIT, lettER |
| this | `/ðɪs/` | `/ðɪs/` | Voiced dental fricative /ð/ in word-initial position (typical of function words) contrasted with voiceless /θ/ of 'thin'; KIT vowel + voiceless /s/ coda. A near-minimal /ð/~/θ/ onset pair with 'thin'. | KIT |
| thin | `/θɪn/` | `/θɪn/` | Voiceless dental fricative /θ/ onset, the voiceless counterpart to /ð/ in 'this'; KIT vowel + alveolar nasal /n/ coda. Demonstrates the /θ/~/ð/ phonemic contrast that English orthography spells identically as 'th'. | KIT |
| pleasure | `/ˈplɛʒɚ/` | `/ˈpleʒə/` | /pl-/ onset cluster; DRESS vowel; medial /ʒ/; reduced lettER ending. With 'measure' and 'vision' it triangulates the distribution of /ʒ/. Aspiration of /p/ is suppressed after... here word-initial [pʰl]. | DRESS, lettER |
| schedule | `/ˈskɛdʒul/` | `/ˈʃedjuːl/` | A salient GA/RP lexical-incidence split: GA onset /sk-/ [ˈskɛdʒul] vs RP /ʃ-/ [ˈʃɛdjuːl]. Following the guide convention, GA GOOSE is written without a length mark (cf. 'tune' GA /tun/) while RP marks length [uː]. DRESS vowel in syllable 1, GOOSE vowel in syllable 2; illustrates voiceless postalveolar fricative /ʃ/ (RP) and the /skw/-free /sk/ cluster (GA). | DRESS, GOOSE |
| comfortable | `/ˈkʌmftɚbəl/` | `/ˈkʌmftəbl̩/` | Common syncope: orthographic four syllables reduce to three in casual speech ([ˈkʌmf.tɚ.bəl] / [ˈkʌmf.tə.bl̩]), with the second 'o' deleted. STRUT vowel + reduced syllables + final syllabic [l̩] (RP) / schwa+l (GA). A stress-and-reduction showpiece. The -or- /r/ is GA rhoticity only (the lettER syllable [ɚ]) and is absent in RP, so it is listed as 'ɚ' rather than as a /r/ consonant. | STRUT, lettER, commA |
| vegetable | `/ˈvɛdʒtəbəl/` | `/ˈvedʒtəbl̩/` | Like 'comfortable', a four-letter-syllable word reduced to three by deletion of the second 'e' ([ˈvɛdʒ.tə.bəl] / [ˈvɛdʒ.tə.bl̩]). /v/ onset, DRESS vowel, medial /dʒ/, final syllabic [l̩] (RP). Demonstrates lexicalized vowel syncope. | DRESS, commA |
| north | `/nɔrθ/` | `/nɔːθ/` | Supplies the NORTH keyword. /n/ onset, /θ/ coda. GA rhotic [ɔr]; RP non-rhotic long [ɔː]. NORTH and FORCE are historically distinct sets but are merged in GA and most RP; FORCE is exemplified independently by 'force' (next-but-one entry). | NORTH |
| force | `/fɔrs/` | `/fɔːs/` | FORCE keyword, historically distinct from NORTH ('force/four' vs 'north/horse') though merged in GA and most modern RP. /f/ onset + /s/ coda. GA rhotic [ɔr]; RP non-rhotic long [ɔː]. Provides FORCE with a proper keyword rather than relying on the NORTH–FORCE merger in 'north'. | FORCE |
| fleece | `/flis/` | `/fliːs/` | FLEECE keyword: the close front unrounded long vowel. /fl-/ onset cluster + /s/ coda. GA omits the length mark by guide convention (/flis/); RP marks length (/fliːs/). Distinct from the happY vowel of 'photography' (which is unstressed and lax-to-tense variable). | FLEECE |
| foot | `/fʊt/` | `/fʊt/` | FOOT keyword: the near-close near-back rounded lax vowel /ʊ/ (as in 'good', 'put'). /f/ onset, /t/ coda. This is the FOOT monophthong proper — distinct from the /ʊ/ that serves only as the onset of the CURE centring diphthong in 'cure'. GA and RP agree. | FOOT |
| cloth | `/klɔθ/` | `/klɒθ/` | CLOTH keyword, illustrating the GA/RP incidence split: GA assigns CLOTH to the THOUGHT vowel [ɔ] (the historical lot–cloth split / THOUGHT raising before voiceless fricatives), while RP keeps it in the short rounded LOT vowel [ɒ]. /kl-/ onset cluster + /θ/ coda. | CLOTH |
| face | `/feɪs/` | `/feɪs/` | FACE keyword: the closing front diphthong /eɪ/. /f/ onset, /s/ coda. GA and RP agree on the nucleus (RP may be slightly more open at onset [ɛɪ] for some speakers). One of the core closing diphthongs. | FACE |
| price | `/praɪs/` | `/praɪs/` | PRICE keyword: the closing diphthong /aɪ/. /pr-/ onset cluster + /s/ coda. GA and RP agree (GA may show Canadian-raising-style [ʌɪ] before the voiceless /s/ for some speakers). A core closing diphthong. | PRICE |
| choice | `/tʃɔɪs/` | `/tʃɔɪs/` | CHOICE keyword: the closing back-to-front diphthong /ɔɪ/. Voiceless postalveolar affricate /tʃ/ onset + /s/ coda. GA and RP agree. Completes the set of three core closing diphthongs (FACE, PRICE, CHOICE) alongside MOUTH and GOAT. | CHOICE |
| near | `/nɪr/` | `/nɪə/` | NEAR centring set. /n/ onset. GA is rhotic [ɪr]; RP is non-rhotic with a centring diphthong [ɪə] (monophthongizing to [ɪː] for many speakers). Completes the centring diphthongs alongside SQUARE and CURE. | NEAR |
| house | `/haʊs/` | `/haʊs/` | Supplies the voiceless glottal fricative /h/, which no other keyword realizes. Also gives a second MOUTH diphthong /aʊ/ (cf. 'about') and a /s/ coda. GA and RP agree. | MOUTH |
| zoo | `/zu/` | `/zuː/` | Supplies a surface /z/ (voiced alveolar fricative), which no other keyword realizes as a lexical onset. GOOSE vowel: GA omits the length mark by guide convention (/zu/); RP marks length (/zuː/). | GOOSE |

## Unicode Reference

Unicode codepoint reference for every IPA symbol, diacritic, and suprasegmental mark used throughout this English pronunciation guide. Each entry gives the symbol, its Unicode codepoint (U+XXXX), decimal value, official Unicode character name, and its IPA phonetic role in English (General American = GA, Received Pronunciation = RP). All codepoints follow the IPA 2015 revision conventions. Note that many IPA symbols are drawn from the Basic Latin block, but the specialized symbols live in the IPA Extensions, Spacing Modifier Letters, and Combining Diacritical Marks blocks.

### IPA Consonant Symbols

The 24 English consonant phonemes plus key allophonic symbols. Most plain consonants reuse Basic Latin letters; the affricates tʃ and dʒ are digraphs (no single codepoint); ʃ ʒ ɡ come from IPA Extensions, ŋ from Latin Extended-A, ð from Latin-1 Supplement, and θ is the Greek letter theta.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| p | `U+0070` | 112 | LATIN SMALL LETTER P | voiceless bilabial plosive `/p/` (PEN); aspirated `[pʰ]` word-initially in stressed onsets |
| b | `U+0062` | 98 | LATIN SMALL LETTER B | voiced bilabial plosive `/b/` (BAT) |
| t | `U+0074` | 116 | LATIN SMALL LETTER T | voiceless alveolar plosive `/t/` (TOP); aspirated `[tʰ]`, flapped `[ɾ]` intervocalically in GA, glottalized `[ʔ]` in RP |
| d | `U+0064` | 100 | LATIN SMALL LETTER D | voiced alveolar plosive `/d/` (DOG) |
| k | `U+006B` | 107 | LATIN SMALL LETTER K | voiceless velar plosive `/k/` (CAT); aspirated `[kʰ]` in stressed onsets |
| ɡ | `U+0261` | 609 | LATIN SMALL LETTER SCRIPT G | voiced velar plosive `/ɡ/` (GO); note: the single-story script g, distinct from Latin small letter g U+0067 |
| tʃ | — | — | LATIN SMALL LETTER T + LATIN SMALL LETTER ESH (digraph) | voiceless postalveolar affricate `/tʃ/` (CHURCH); the IPA tie-bar ligature t͡ʃ may also be written |
| dʒ | — | — | LATIN SMALL LETTER D + LATIN SMALL LETTER EZH (digraph) | voiced postalveolar affricate `/dʒ/` (JUDGE); the IPA tie-bar ligature d͡ʒ may also be written |
| f | `U+0066` | 102 | LATIN SMALL LETTER F | voiceless labiodental fricative `/f/` (FAN) |
| v | `U+0076` | 118 | LATIN SMALL LETTER V | voiced labiodental fricative `/v/` (VAN) |
| θ | `U+03B8` | 952 | GREEK SMALL LETTER THETA | voiceless dental fricative `/θ/` (THIN); borrowed Greek letter theta, NOT Latin |
| ð | `U+00F0` | 240 | LATIN SMALL LETTER ETH | voiced dental fricative `/ð/` (THIS); Latin letter eth, distinct from theta |
| s | `U+0073` | 115 | LATIN SMALL LETTER S | voiceless alveolar fricative `/s/` (SIP) |
| z | `U+007A` | 122 | LATIN SMALL LETTER Z | voiced alveolar fricative `/z/` (ZIP) |
| ʃ | `U+0283` | 643 | LATIN SMALL LETTER ESH | voiceless postalveolar fricative `/ʃ/` (SHIP) |
| ʒ | `U+0292` | 658 | LATIN SMALL LETTER EZH | voiced postalveolar fricative `/ʒ/` (VISION, BEIGE) |
| h | `U+0068` | 104 | LATIN SMALL LETTER H | voiceless glottal fricative `/h/` (HAT) |
| m | `U+006D` | 109 | LATIN SMALL LETTER M | voiced bilabial nasal `/m/` (MAN); syllabic `[m̩]` in e.g. rhythm |
| n | `U+006E` | 110 | LATIN SMALL LETTER N | voiced alveolar nasal `/n/` (NO); syllabic `[n̩]` in e.g. button |
| ŋ | `U+014B` | 331 | LATIN SMALL LETTER ENG | voiced velar nasal `/ŋ/` (SING); never occurs word-initially in English |
| l | `U+006C` | 108 | LATIN SMALL LETTER L | voiced alveolar lateral approximant `/l/` (LIP); clear `[l]` and dark/velarized `[ɫ]` allophones |
| r | `U+0072` | 114 | LATIN SMALL LETTER R | rhotic phoneme `/r/` (RUN); phonetically the postalveolar approximant `[ɹ]` in most English varieties |
| j | `U+006A` | 106 | LATIN SMALL LETTER J | voiced palatal approximant `/j/` (YES); NOT the affricate value of English orthographic 'j' |
| w | `U+0077` | 119 | LATIN SMALL LETTER W | voiced labial-velar approximant `/w/` (WET) |

### IPA Vowel Symbols

Vowel qualities used across the Wells (1982) Standard Lexical Sets (KIT, DRESS, TRAP, LOT, STRUT, FOOT, NURSE, FLEECE, GOOSE, etc.). The lax/quality-distinct vowels ɪ ɛ ɑ ɒ ɔ ʌ ə ʊ ɜ come from the IPA Extensions block (U+0250–U+02AF), plus æ from Latin-1 Supplement; the cardinal-quality monophthongs i u e o reuse Basic Latin letters.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| ɪ | `U+026A` | 618 | LATIN LETTER SMALL CAPITAL I | near-close near-front unrounded vowel `/ɪ/` (KIT lexical set) |
| ɛ | `U+025B` | 603 | LATIN SMALL LETTER OPEN E | open-mid front unrounded vowel `/ɛ/` (DRESS lexical set) |
| æ | `U+00E6` | 230 | LATIN SMALL LETTER AE | near-open front unrounded vowel `/æ/` (TRAP lexical set; also BATH in GA) |
| ɑ | `U+0251` | 593 | LATIN SMALL LETTER ALPHA | open back unrounded vowel `/ɑ/` (PALM/START; LOT in GA; BATH in RP) |
| ɒ | `U+0252` | 594 | LATIN SMALL LETTER TURNED ALPHA | open back rounded vowel `/ɒ/` (LOT/CLOTH in RP); not phonemic in GA |
| ɔ | `U+0254` | 596 | LATIN SMALL LETTER OPEN O | open-mid back rounded vowel `/ɔ/` (THOUGHT/NORTH/FORCE; CLOTH in GA) |
| ʌ | `U+028C` | 652 | LATIN SMALL LETTER TURNED V | open-mid back unrounded vowel `/ʌ/` (STRUT lexical set) |
| ə | `U+0259` | 601 | LATIN SMALL LETTER SCHWA | mid central unrounded vowel `/ə/` (commA; unstressed lettER in RP) |
| ʊ | `U+028A` | 650 | LATIN SMALL LETTER UPSILON | near-close near-back rounded vowel `/ʊ/` (FOOT lexical set) |
| ɜ | `U+025C` | 604 | LATIN SMALL LETTER REVERSED OPEN E | open-mid central unrounded vowel `/ɜ/`; element of NURSE `[ɜː]` in RP transcriptions; non-rhotic central vowel |
| i | `U+0069` | 105 | LATIN SMALL LETTER I | close front unrounded vowel `/i/` (FLEECE; happY); often written `/iː/` with length for FLEECE |
| u | `U+0075` | 117 | LATIN SMALL LETTER U | close back rounded vowel `/u/` (GOOSE); often written `/uː/` with length |
| e | `U+0065` | 101 | LATIN SMALL LETTER E | close-mid front unrounded vowel `/e/`; first element of FACE diphthong `/eɪ/`; monophthong `[eː]` in some accents |
| o | `U+006F` | 111 | LATIN SMALL LETTER O | close-mid back rounded vowel `/o/`; first element of GOAT diphthong `/oʊ/` (GA) — RP uses `/əʊ/` |

### Diacritics & Suprasegmentals

Stress, length, aspiration, syllabicity, nasalization, rhoticity, and the tap, approximant, dark-l, and glottal-stop symbols. Stress and length and aspiration marks (ˈ ˌ ː ʰ) are spacing characters from Spacing Modifier Letters (U+02B0–U+02FF); syllabicity ◌̩ and nasalization ◌̃ are non-spacing combining marks from Combining Diacritical Marks (U+0300–U+036F) that attach to a base glyph; ɚ ɝ ɾ ɹ ɫ ʔ are letter symbols from IPA Extensions.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| ˈ | `U+02C8` | 712 | MODIFIER LETTER VERTICAL LINE | primary stress mark ˈ; precedes the stressed syllable, e.g. `/ˈwɔːtə/` |
| ˌ | `U+02CC` | 716 | MODIFIER LETTER LOW VERTICAL LINE | secondary stress mark ˌ; precedes a syllable with secondary stress |
| ː | `U+02D0` | 720 | MODIFIER LETTER TRIANGULAR COLON | length mark ː; marks a long vowel, e.g. `/iː uː ɑː ɔː ɜː/` |
| ʰ | `U+02B0` | 688 | MODIFIER LETTER SMALL H | aspiration diacritic ʰ; voiceless plosive released with a puff of air, e.g. `[pʰ tʰ kʰ]` |
| ◌̩ | `U+0329` | 809 | COMBINING VERTICAL LINE BELOW | syllabicity diacritic ◌̩; marks a syllabic consonant, e.g. `[n̩]` in button, `[l̩]` in bottle (combining, attaches below base) |
| ◌̃ | `U+0303` | 771 | COMBINING TILDE | nasalization diacritic ◌̃; vowel nasalized adjacent to a nasal, e.g. `[æ̃]` in man (combining, attaches above base) |
| ɚ | `U+025A` | 602 | LATIN SMALL LETTER SCHWA WITH HOOK | rhotacized schwa ɚ (r-colored); unstressed lettER in GA, e.g. `/ˈbʌtɚ/` |
| ɝ | `U+025D` | 605 | LATIN SMALL LETTER REVERSED OPEN E WITH HOOK | rhotacized open-mid central vowel ɝ; stressed NURSE in GA, e.g. `/nɝz/` |
| ɾ | `U+027E` | 638 | LATIN SMALL LETTER R WITH FISHHOOK | alveolar tap/flap `[ɾ]`; allophone of `/t/` and `/d/` between vowels in GA, e.g. water `[ˈwɔɾɚ]` |
| ɹ | `U+0279` | 633 | LATIN SMALL LETTER TURNED R | postalveolar approximant `[ɹ]`; the usual phonetic realization of English `/r/` |
| ɫ | `U+026B` | 619 | LATIN SMALL LETTER L WITH MIDDLE TILDE | velarized (dark) alveolar lateral `[ɫ]`; coda allophone of `/l/`, e.g. feel `[fiːɫ]` |
| ʔ | `U+0294` | 660 | LATIN LETTER GLOTTAL STOP | glottal stop `[ʔ]`; allophone of `/t/` in RP (e.g. button `[ˈbʌʔn̩]`) and onset before stressed vowels |

### Unicode Blocks Used

Summary of the Unicode blocks from which every symbol in this guide is drawn. Verify rendering with a font that fully supports IPA Extensions and combining marks (e.g. Charis SIL, Doulos SIL, Gentium).

| Block | Range | Usage |
|---|---|---|
| Basic Latin | U+0000–U+007F | Plain consonant letters (p b t d k f v s z h m n l r j w) and the cardinal-quality vowel letters i u e o. |
| Latin-1 Supplement | U+0080–U+00FF | æ TRAP vowel (U+00E6) and ð voiced dental fricative (U+00F0). |
| Latin Extended-A | U+0100–U+017F | ŋ velar nasal eng (U+014B). |
| IPA Extensions | U+0250–U+02AF | Specialized IPA letters: ɡ ʃ ʒ vowels ɪ ɛ ɑ ɒ ɔ ʌ ə ʊ ɜ and rhotic/allophone symbols ɚ ɝ ɾ ɹ ɫ ʔ. |
| Spacing Modifier Letters | U+02B0–U+02FF | Spacing diacritics that occupy their own width: aspiration ʰ, primary stress ˈ, secondary stress ˌ, length ː. |
| Combining Diacritical Marks | U+0300–U+036F | Non-spacing marks that attach to a base glyph: nasalization ◌̃ (U+0303) and syllabicity ◌̩ (U+0329). |
| Greek and Coptic | U+0370–U+03FF | θ theta, borrowed for the voiceless dental fricative (U+03B8). |

## Cross-Reference to the Semitic Guides

Cross-reference relating this English IPA pronunciation guide to its three companion Semitic guides: Classical Syriac (Peshitta), Biblical Aramaic, and Biblical Hebrew. Where the Semitic guides cross-reference one another within a single language family, this section instead documents the typological and phonological GAP between English (an Indo-European, Germanic language) and the Semitic family, while noting the shared descriptive apparatus (IPA 2015, phonemic vs phonetic notation, articulatory place/manner classification) that lets all four guides be read against each other. It is a contrastive bridge, not a claim of genetic relationship: English and the Semitic languages are unrelated, but the IPA framework is shared.

### Shared Framework

All four guides (English, Peshitta, Biblical Aramaic, Biblical Hebrew) are built on the same descriptive linguistic apparatus, which makes their pronunciation data directly comparable despite the languages being unrelated.

- Primary and sole pronunciation system is the International Phonetic Alphabet (IPA), 2015 revision; spelling/orthography is never the authoritative record.
- Phonemic transcriptions are written between /slashes/; narrow phonetic transcriptions are written between [brackets].
- Consonants are classified by place of articulation, manner of articulation, and voicing (the IPA pulmonic consonant chart).
- Vowels are classified by height, backness, roundedness, and length/tenseness (the IPA vowel chart).
- Suprasegmental marks are shared: `ˈ` primary stress, `ˌ` secondary stress, `ː` length, `ʰ` aspiration, and the under-ring `◌̩` for syllabic consonants.
- Each guide documents two parallel reference traditions of one language: English uses General American (GA) and Received Pronunciation (RP/SSBE); the Semitic guides use Eastern/Western (Peshitta) or comparable reconstructed reading traditions (e.g. Tiberian for Hebrew and Biblical Aramaic).

Because the framework is identical, an IPA symbol means the same articulatory target in every guide. `/b/`, `/t/`, `/s/`, `/m/` denote the same sounds in English as in Syriac, Aramaic, or Hebrew; only the phoneme inventories, distributions, and phonological rules differ.

### Typological Contrasts

| Feature | English | Semitic |
|---|---|---|
| Language family | Indo-European > Germanic > West Germanic > Anglo-Frisian. English is genetically unrelated to the Semitic languages. | Afroasiatic > Semitic. Syriac and Biblical Aramaic are Northwest Semitic (Aramaic branch); Biblical Hebrew is Northwest Semitic (Canaanite branch). All three are closely related to one another. |
| Basic word order | Configurational SVO (Subject–Verb–Object) as the unmarked order; word order carries most grammatical relations because English has little case morphology. | Tendency toward VSO (Verb–Subject–Object) in Classical Syriac, Biblical Aramaic, and Biblical Hebrew narrative, though SVO and other orders occur; verb-initial clauses are characteristic, especially in Hebrew narrative wayyiqtol chains. |
| Morphological type | Predominantly concatenative and fusional with strong analytic/isolating tendencies: affixes are linearly added to stems (un-friend-li-ness), and grammar relies heavily on free function words and word order rather than rich inflection. | Root-and-pattern (templatic, nonconcatenative) morphology: meaning is built from a discontinuous triconsonantal root (e.g. k-t-b 'write') interleaved with vowel/consonant templates (binyanim/verbal stems), producing forms like katab, ktib, maktub. This interdigitation has no English equivalent. |
| Writing system and direction | Written left-to-right in the Latin (Roman) alphabet, a true alphabet that represents (deeply and opaquely) both consonants and vowels with separate letters. | Written right-to-left. Syriac uses the Syriac abjad; Biblical Aramaic and Biblical Hebrew use the Hebrew square abjad. An abjad encodes consonants as letters and marks vowels only optionally, with later pointing systems (Syriac dots; Tiberian niqqud). |
| Rhythm and timing | Traditionally classed as stress-timed: stressed syllables recur at roughly regular intervals and unstressed syllables are compressed, with pervasive vowel reduction to schwa `/ə/`. Lexical stress is contrastive (ˈrecord vs reˈcord). | Rhythm varies and is not strongly stress-timed in the English sense. Stress placement in the Semitic guides is largely predictable from word structure (e.g. typically final or penultimate), vowel reduction to schwa is far less pervasive, and reduced vowels (Hebrew/Aramaic shewa) behave differently from English schwa. |
| Consonant inventory — guttural region | Has NO pharyngeal or pharyngealized (emphatic) consonants and no contrastive uvulars. The only glottal/back consonant is `/h/` (plus non-phonemic glottal stop `[ʔ]`). The rhotic `/r/` is a postalveolar/retroflex approximant `[ɹ]` in most accents, not a trill. | Rich guttural and emphatic series. Pharyngeals `/ħ/` (Heth/Kheth) and `/ʕ/` (Ayin), glottals `/ʔ/` (Aleph/Alaph) and `/h/` (He), and emphatic (pharyngealized) consonants such as `/tˤ/` (Teth) and `/sˤ/` (Tsade) that can spread pharyngealization to neighboring vowels. Syriac and Biblical Aramaic Resh is an alveolar trill `/r/`; Tiberian Hebrew Resh is reconstructed as uvular `/ʁ/`. |
| Vowel inventory | Large vowel system: roughly 11–12 monophthongs plus a set of phonemic diphthongs (FACE `/eɪ/`, PRICE `/aɪ/`, CHOICE `/ɔɪ/`, MOUTH `/aʊ/`, GOAT `/oʊ~əʊ/`), keyed here to the Wells (1982) Standard Lexical Sets. Vowel quality (and, in RP, length) is heavily contrastive. | Smaller vowel systems (typically 5–7 vowel qualities, e.g. Peshitta Eastern 7 `/a ɑ ɛ e i o u/` or Western 5 `/a ɔ e i u/`; Tiberian Hebrew/Aramaic 7 `/a ɛ e i ɔ o u/`). Diphthongs are marginal or arise from vowel + glide sequences rather than forming a large phonemic diphthong set as in English. |

### Companion Guides

- **Peshitta** — `peshitta_pronunciation_guide.json`. Classical Syriac (Aramaic), the Peshitta reading tradition. Documents Eastern (Madnhaya) and Western (Serto) traditions in parallel, the Begadkephat spirantization rule, guttural and emphatic consonants, and the Syriac abjad (U+0700–U+074F). The cross_reference_to_aramaic_and_hebrew section there ties Syriac to its two Semitic siblings.
- **Biblical Aramaic** — `biblical_aramaic_pronunciation_guide.json`. Biblical Aramaic / Jewish Literary Aramaic, as preserved in the Tiberian pointing of the Aramaic portions of the Hebrew Bible (Daniel, Ezra). Northwest Semitic (Aramaic branch); uses the Hebrew square abjad with Tiberian niqqud. Shares emphatic/guttural consonants and triconsonantal root morphology with Syriac and Hebrew.
- **Biblical Hebrew** — `biblical_hebrew_pronunciation_guide.json`. Biblical (Classical) Hebrew in the Tiberian reading tradition. Northwest Semitic (Canaanite branch); uses the Hebrew square abjad with Tiberian niqqud. Notable for the prefixed definite article `/ha-/` with following gemination, the Tiberian uvular Resh `/ʁ/`, and a 7-vowel system.

### Shared IPA Symbols

IPA consonant symbols whose phonetic value is shared between English and one or more of the Semitic companion guides, allowing direct cross-reference. The symbol denotes the same articulatory target in every guide; the languages differ in how these phonemes pattern, not in what the symbols mean.

| IPA | Name | English | Semitic |
|---|---|---|---|
| `b` | voiced bilabial plosive | `/b/` (bee, cab) | Beth (hard/plosive allophone) in Syriac, Aramaic, Hebrew |
| `d` | voiced alveolar/dental plosive | `/d/` (do, bed) | Daleth (hard/plosive allophone) in all three |
| `k` | voiceless velar plosive | `/k/` (key, back); aspirated `[kʰ]` in stressed onset | Kaph (hard/plosive allophone) in all three |
| `ɡ` | voiced velar plosive | `/ɡ/` (go, bag) | Gimel (hard/plosive allophone) in all three |
| `p` | voiceless bilabial plosive | `/p/` (pea, cap); aspirated `[pʰ]` in stressed onset | Pe (hard/plosive allophone) in Syriac, Aramaic, Hebrew |
| `t` | voiceless alveolar/dental plosive | `/t/` (tea, cat); aspirated `[tʰ]` in onset, flapped `[ɾ]` intervocalically in GA | Taw (hard/plosive allophone) in all three (distinct from emphatic Teth `/tˤ/`) |
| `f` | voiceless labiodental fricative | `/f/` (fee, leaf) | Pe (soft/spirantized allophone, Begadkephat) in all three |
| `v` | voiced labiodental fricative | `/v/` (vee, leave) | Beth (soft/spirantized allophone) in Aramaic and Hebrew; spirantized Beth is `[v]` in Western Syriac (Eastern Syriac tends toward `[w]`) |
| `θ` | voiceless dental fricative | `/θ/` (thin, bath) | Taw (soft/spirantized allophone) in Syriac, Biblical Aramaic, and Tiberian Hebrew |
| `ð` | voiced dental fricative | `/ð/` (this, bathe) | Daleth (soft/spirantized allophone) in Syriac, Biblical Aramaic, and Tiberian Hebrew |
| `s` | voiceless alveolar fricative | `/s/` (see, bus) | Semkath / plain Samekh and Sin in all three (distinct from emphatic Tsade `/sˤ/`) |
| `z` | voiced alveolar fricative | `/z/` (zoo, buzz) | Zayin in all three |
| `ʃ` | voiceless postalveolar fricative | `/ʃ/` (she, fish) | Shin in all three (contrasts with `/s/`) |
| `h` | voiceless glottal fricative | `/h/` (he); English `/h/` occurs only in onset position (no coda `/h/`) | He in all three |
| `m` | voiced bilabial nasal | `/m/` (me, sum) | Mem / Mim in all three |
| `n` | voiced alveolar nasal | `/n/` (no, sun) | Nun in all three |
| `l` | voiced alveolar lateral approximant | `/l/` with clear `[l]` and dark `[ɫ]` allophones | Lamadh / Lamed in all three (clear lateral) |
| `r` | rhotic (English approximant vs Semitic trill/uvular) | `/r/` realized as postalveolar/retroflex approximant `[ɹ]` in most English accents | Resh = alveolar trill `/r/` in Syriac and Biblical Aramaic; uvular `/ʁ/` in Tiberian Hebrew. The phoneme corresponds, but the phonetic realization differs sharply. |
| `j` | voiced palatal approximant | `/j/` (yes) | Yodh / Yud in all three |
| `w` | voiced labial-velar approximant | `/w/` (we) | Waw / Vav (consonantal value) in all three; in some Hebrew traditions realized as `/v/` |

#### English-Only Consonants

English consonant phonemes with no direct counterpart in the Semitic companion inventories.

- `tʃ` (CHurch — affricate; arises only marginally/secondarily in the Semitic guides)
- `dʒ` (Judge — affricate; not a primary Semitic phoneme, though Gimel is `[dʒ]` in some modern/Yemenite traditions, not in the Tiberian/Classical reading traditions documented here)
- `ʒ` (meaSure — voiced postalveolar fricative; absent from the Semitic phoneme sets)
- `ŋ` (siNG — velar nasal; an allophone of `/n/` before velars, not an independent Semitic phoneme)

#### Semitic-Only Consonants

Semitic consonant phonemes with no counterpart in English; these are the principal articulatory targets an English speaker must learn anew.

- `ʔ` (Aleph/Alaph — glottal stop; non-phonemic `[ʔ]` only in English)
- `ħ` (Heth/Kheth — voiceless pharyngeal fricative; absent in English)
- `ʕ` (Ayin — voiced pharyngeal fricative; absent in English)
- `tˤ` (Teth — emphatic/pharyngealized t; absent in English)
- `sˤ` (Tsade/Tsadi — emphatic/pharyngealized s; absent in English)
- `q` (Qoph — voiceless uvular plosive; absent in English)
- `x` (spirantized Kaph in Hebrew/Syriac/Aramaic; absent as a phoneme in English)
- `ʁ` (Tiberian uvular Resh; absent in English)

> **Note:** Unlike the Semitic guides' cross_reference sections, which trace correspondences within a single language family, this section is fundamentally contrastive: English shares the IPA description framework with the companion guides but belongs to a different family (Indo-European/Germanic) with different word order (SVO), morphology (concatenative vs root-and-pattern), script (left-to-right alphabet vs right-to-left abjad), rhythm (stress-timed with schwa reduction), and a markedly different sound inventory (no pharyngeals or emphatics; a large vowel system with phonemic diphthongs).
