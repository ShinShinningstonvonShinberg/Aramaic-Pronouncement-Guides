# Spanish IPA Pronunciation Guide

**Version:** 1.0.0
**Date:** 2026-06-24
**Language:** Spanish (ISO 639-3: `spa`)  
**Encoding:** UTF-8  
**IPA Standard:** IPA (International Phonetic Alphabet, 2015 revision)  
**Reference Accents:** Peninsular Standard Castilian (CAST) and General Latin American (LATAM)  

Machine-readable IPA-based pronunciation guide for Modern Spanish. All pronunciation data is encoded in the International Phonetic Alphabet (IPA, 2015 revision) as the primary and only system. Designed for AI-assisted pronunciation, text-to-speech reference, second-language teaching, and language documentation. Two reference accents are documented in parallel: Peninsular Standard Castilian (with distinción) and General Latin American (with seseo).

### Varieties Covered

- **Peninsular Standard Castilian (CAST)** — Spain (supraregional north-central Castilian standard, the prestige norm of the Real Academia Española and Spanish broadcast media). Sibilant system: **distinción** — the voiceless interdental fricative `/θ/` (spelled z, and c before e/i) contrasts phonemically with the voiceless alveolar fricative `/s/` (spelled s). Thus caza `/ˈkaθa/` ('hunt') ≠ casa `/ˈkasa/` ('house'), and cocer `/koˈθeɾ/` ('to cook') ≠ coser `/koˈseɾ/` ('to sew'). The prestige reference accent of European Spanish, based on north-central (Castilian) usage. Key features: distinción (`/θ/` ~ `/s/` contrast); apico-alveolar `/s/` (often retracted `[s̺]`, auditorily 'whistly'); velar~uvular `/x/`, realized `[x]`~`[χ]`, notably back/raspy (e.g. jamón `[xaˈmon]`~`[χaˈmon]`); widespread yeísmo (`/ʎ/` merged into `/ʝ/`) in most modern speakers, though lleísmo (distinct `/ʎ/`) survives conservatively; coda `/s/` generally retained as `[s]` in the central-northern standard. ~19 consonant phonemes in conservative full Castilian (including both `/θ/` and, for lleísta speakers, `/ʎ/`). Analogous to the Eastern (Madnhaya) tradition in the Peshitta guide and General American (GA) in the English guide — one of two co-equal documented standards.
- **General Latin American Spanish (LATAM)** — Spanish America (pan-American supraregional standard; the seseo-yeísta norm shared in broad outline across Mexico, Central America, the Andes, the Caribbean, and the Southern Cone). Sibilant system: **seseo** — universal merger of historical `/θ/` into `/s/`, so z and c (before e/i) are pronounced `[s]` just like s. Thus caza, casa, cocer and coser are all homophonous with `/s/`: caza = casa = `/ˈkasa/`. There is no `/θ/` phoneme. The pan-American reference accent, defined against Castilian by seseo. Key features: seseo (`/θ/` → `/s/`; no interdental fricative); near-universal yeísmo (`/ʎ/` → `/ʝ/`), with Rioplatense rehilamiento `/ʝ/` → `[ʒ]`~`[ʃ]` (e.g. yo `[ʃo]`, calle `[ˈkaʃe]`) as a salient subvariety; `/x/` commonly weakened to glottal `[h]` in the Caribbean and much of the Americas (jamón `[haˈmon]`); coda `/s/` frequently aspirated to `[h]` or deleted in Caribbean and lowland varieties (e.g. los `[loh]`, está `[ehˈta]`); typically a laminal/dental `[s]` rather than the Castilian apico-alveolar `[s̺]`; conservative lleísmo (distinct `/ʎ/`) survives in some Andean and Paraguayan varieties. ~17 consonant phonemes in general seseo-yeísta varieties (no `/θ/`, no `/ʎ/`). Analogous to the Western (Serto) tradition in the Peshitta guide and Received Pronunciation (RP/SSBE) in the English guide — one of two co-equal documented standards.

### Companion Files

- `peshitta_pronunciation_guide.json`
- `biblical_aramaic_pronunciation_guide.json`
- `biblical_hebrew_pronunciation_guide.json`
- `english_pronunciation_guide.json`
- `french_pronunciation_guide.json`

### Notes

- Spanish is written left-to-right in the Latin (Roman) script, unlike the right-to-left Semitic companion guides; it shares the Latin-script, parallel-two-accent design of the English and French companion guides.
- Spanish orthography is exceptionally SHALLOW (transparent/phonemic): the grapheme-to-phoneme mapping is highly regular and largely bidirectional, so spelling reliably predicts pronunciation — among the most phonemic orthographies of any major language, and the opposite extreme from English's deep, opaque spelling.
- Spanish has a CLEAN, symmetric 5-vowel system `/a e i o u/` with NO phonemic length and NO vowel reduction: every vowel keeps its full quality whether stressed or unstressed, so there is no schwa and no weak-vowel set — a central contrast with English and French.
- Lexical stress is contrastive and phonemic but is marked overtly with the acute accent (tilde de acentuación) and is recoverable from spelling, e.g. término `/ˈteɾmino/` vs termino `/teɾˈmino/` vs terminó `/teɾmiˈno/`; default stress falls on the penult for words ending in a vowel/-n/-s and on the final syllable otherwise.
- Spanish rhythm is SYLLABLE-TIMED, with syllables of relatively even duration and no durational reduction of unstressed vowels, unlike the stress-timed rhythm of English.
- The hallmark allophonic process is SPIRANTIZATION (lenition) of the voiced stops `/b d ɡ/` to the voiced approximants `[β ð ɣ]` in most environments — typically intervocalically and after most consonants — with the full stops `[b d ɡ]` retained utterance-initially, after a nasal, and (for `/d/`) after `/l/`. E.g. bebé `[beˈβe]`, lado `[ˈlaðo]`, lago `[ˈlaɣo]`.
- The two reference accents differ centrally in the sibilant system: Castilian DISTINCIÓN keeps `/θ/` (caza `/ˈkaθa/` ≠ casa `/ˈkasa/`), while Latin American SESEO merges `/θ/` into `/s/` (caza = casa = `/ˈkasa/`); this guide documents both in parallel.
- YEÍSMO — the merger of historical `/ʎ/` (ll) into `/ʝ/` (y) — is near-universal in both accents, so for most speakers ll and y are pronounced alike; conservative LLEÍSMO (a distinct palatal lateral `/ʎ/`) survives in some Andean and Paraguayan varieties and is documented as a sub-variant.
- Spanish phonemically contrasts the TRILL `/r/` (spelled rr, or r word-initially and after l/n/s) with the TAP/FLAP `/ɾ/` (spelled single intervocalic r): perro `/ˈpero/` ('dog') ≠ pero `/ˈpeɾo/` ('but'); carro `/ˈkaro/` ≠ caro `/ˈkaɾo/`.
- The letters b and v both spell the single phoneme `/b/` (no `/v/` in standard Spanish): there is no native `[v]`–`[b]` contrast, and both surface as `[b]` or spirantized `[β]` by position (e.g. vaca `[ˈbaka]`, tubo `[ˈtuβo]`).
- The voiced velar fricative spelled j (and g before e/i), phonemically `/x/`, ranges from velar `[x]` to uvular `[χ]` in Castilian and is frequently weakened to glottal `[h]` in Caribbean and much of Latin American Spanish (jamón `[xaˈmon]`~`[haˈmon]`).
- The letter h is always silent (e.g. hora `/ˈoɾa/`, hombre `/ˈombɾe/`); it carries no sound and exists for etymological/orthographic reasons only.
- `/n/` assimilates in place to a following consonant (`[m]` before labials, `[ɱ]` before labiodentals, `[n̪]` before dentals, `[ɲ]` before palatals, `[ŋ]` before velars), and `/s/` voices to `[z]` before a voiced consonant (e.g. mismo `[ˈmizmo]`, desde `[ˈdezðe]`); these are allophonic, not phonemic.
- Rioplatense (Buenos Aires/Montevideo) shows REHILAMIENTO: `/ʝ/` is strengthened to a postalveolar fricative `[ʒ]` or, increasingly, devoiced `[ʃ]`, so yo is `[ʒo]`~`[ʃo]` and calle is `[ˈkaʒe]`~`[ˈkaʃe]`; this is documented as a major Latin American sub-variety.

## Table of Contents

- [How to Read This Guide](#how-to-read-this-guide)
  - [Phonemic vs phonetic notation](#phonemic-vs-phonetic-notation)
  - [Stress (lexical, marked by the acute accent)](#stress-lexical-marked-by-the-acute-accent)
  - [The two reference accents](#the-two-reference-accents)
  - [The clean 5-vowel system](#the-clean-5-vowel-system)
- [Phonological Inventory](#phonological-inventory)
  - [Consonant Phonemes](#consonant-phonemes)
  - [Vowel Phonemes](#vowel-phonemes)
- [Consonants](#consonants)
  - [Consonant Inventory](#consonant-inventory)
  - [Natural Classes](#natural-classes)
- [Vowels](#vowels)
  - [Vowel System Overview](#vowel-system-overview)
  - [Vowel Inventory](#vowel-inventory)
  - [Stress Changes Prominence, Not Quality](#stress-changes-prominence-not-quality)
  - [Diphthongs and Hiatus](#diphthongs-and-hiatus)
  - [Allophonic Processes](#allophonic-processes)
  - [Dialect Note](#dialect-note)
  - [IPA Symbol Summary](#ipa-symbol-summary)
- [Diphthongs & Triphthongs](#diphthongs--triphthongs)
  - [Rising Diphthongs](#rising-diphthongs)
  - [Falling Diphthongs](#falling-diphthongs)
  - [Triphthongs](#triphthongs-1)
  - [The Glides /j/ and /w/](#the-glides-j-and-w)
  - [Hiatus (*Hiato*)](#hiatus-hiato)
  - [Dialect Note](#dialect-note-1)
- [Consonant–Vowel IPA Matrix](#consonantvowel-ipa-matrix)
  - [Reference Vowels](#reference-vowels)
  - [CV Matrix](#cv-matrix)
  - [Phonetic Notes](#phonetic-notes)
  - [Accent Notes](#accent-notes)
- [Suprasegmentals](#suprasegmentals)
  - [Stress](#stress)
  - [Rhythm](#rhythm)
  - [Vowel Quality & Length](#vowel-quality--length)
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
  - [Rule 1: Spirantization (lenition of voiced stops)](#rule-1-spirantization-lenition-of-voiced-stops)
  - [Rule 2: Distinción vs. seseo (`/θ/`–`/s/` contrast)](#rule-2-distinción-vs-seseo-θs-contrast)
  - [Rule 3: Yeísmo (`/ʎ/` → `/ʝ/` merger)](#rule-3-yeísmo-ʎ--ʝ-merger)
  - [Rule 4: Nasal place assimilation](#rule-4-nasal-place-assimilation)
  - [Rule 5: `/s/` voicing before voiced consonants](#rule-5-s-voicing-before-voiced-consonants)
  - [Rule 6: Coda `/s/`-aspiration and elision](#rule-6-coda-s-aspiration-and-elision)
  - [Rule 7: Sinalefa (cross-word vowel coalescence)](#rule-7-sinalefa-cross-word-vowel-coalescence)
  - [Rule 8: Trill vs. tap distribution](#rule-8-trill-vs-tap-distribution)
  - [Rule 9: `/x/` realization (`[x]`~`[χ]` vs. `[h]`)](#rule-9-x-realization-xχ-vs-h)
  - [Rule 10: Final-`/d/` weakening and elision](#rule-10-final-d-weakening-and-elision)
  - [Rule 11: Lateral and nasal dental/palatal assimilation](#rule-11-lateral-and-nasal-dentalpalatal-assimilation)
  - [Rule 12: Rioplatense rehilamiento (`/ʝ/` → `[ʒ ʃ]`)](#rule-12-rioplatense-rehilamiento-ʝ--ʒ-ʃ)
  - [Rule 13: Ceceo (some Andalusian `/s/` → `[θ]`)](#rule-13-ceceo-some-andalusian-s--θ)
  - [Rule 14: Voiceless stops unaspirated; intervocalic `/p t k/` lenition](#rule-14-voiceless-stops-unaspirated-intervocalic-p-t-k-lenition)
  - [Rule 15: Vowel sequence reduction (no schwa; hiatus → diphthong)](#rule-15-vowel-sequence-reduction-no-schwa-hiatus--diphthong)
- [Castilian vs. Latin American](#castilian-vs-latin-american)
  - [Reference accents](#reference-accents)
  - [Differences](#differences)
- [Orthography: Grapheme–Phoneme Correspondences](#orthography-graphemephoneme-correspondences)
  - [General Principles](#general-principles)
  - [Consonant Graphemes](#consonant-graphemes)
  - [Vowel Graphemes](#vowel-graphemes)
  - [Silent Letters](#silent-letters)
  - [Diacritics](#diacritics)
  - [Allophonic Processes Not Reflected in Spelling](#allophonic-processes-not-reflected-in-spelling)
  - [Notes](#notes-1)
- [Connected Speech & Sinalefa](#connected-speech--sinalefa)
  - [Reference Accents](#reference-accents-1)
  - [Sinalefa](#sinalefa)
  - [Resyllabification](#resyllabification)
  - [Cross-word Spirantization / Assimilation](#cross-word-spirantization--assimilation)
  - [No Vowel Reduction](#no-vowel-reduction-1)
  - [Hiato / Hiatus (the marked absence of sinalefa)](#hiato--hiatus-the-marked-absence-of-sinalefa)
  - [Process Ordering](#process-ordering)
  - [Rate and Register](#rate-and-register)
  - [Dialect Variation (Castilian vs Latin American)](#dialect-variation-castilian-vs-latin-american)
  - [Cross-reference](#cross-reference)
- [Sample Words in IPA](#sample-words-in-ipa)
  - [Source note](#source-note)
- [Unicode Reference](#unicode-reference)
  - [IPA Consonant Symbols](#ipa-consonant-symbols)
  - [Spirantized Allophones](#spirantized-allophones)
  - [IPA Vowel Symbols](#ipa-vowel-symbols)
  - [Diacritics & Suprasegmentals](#diacritics--suprasegmentals)
  - [Unicode Blocks Used](#unicode-blocks-used)
- [Cross-Reference to the Companion Guides](#cross-reference-to-the-companion-guides)
  - [Shared Framework](#shared-framework)
  - [Typological Contrasts](#typological-contrasts)
  - [Companion Guides](#companion-guides)
  - [Shared IPA Symbols](#shared-ipa-symbols)

## How to Read This Guide

This guide records pronunciation in the International Phonetic Alphabet (IPA, 2015 revision) as its primary and only system. A few conventions govern how to read every entry.

### Phonemic vs phonetic notation

Phonemic transcriptions use `/ /` slashes and represent the contrastive, dialect-neutral sound categories of the language; phonetic transcriptions use `[ ]` brackets and represent the actual realized sounds, including allophonic detail. The single most important case for Spanish is SPIRANTIZATION: the voiced stop phonemes `/b d ɡ/` have voiced approximant allophones written `[β ð ɣ]`. These spirantized approximants are phonetic realizations only and always appear in `[ ]` brackets — never inside `/ /` slashes. For example, the phoneme `/b/` surfaces as `[b]` utterance-initially or after a nasal but as `[β]` between vowels: bebé `[beˈβe]`.

### Stress (lexical, marked by the acute accent)

Spanish lexical stress is CONTRASTIVE and PHONEMIC: words can differ in meaning by stress placement alone, e.g. término `/ˈteɾmino/` ('term') vs termino `/teɾˈmino/` ('I finish') vs terminó `/teɾmiˈno/` ('he/she finished'). Crucially, unlike the deep stress of English, Spanish stress is overtly marked and recoverable from spelling: the acute accent (tilde de acentuación) — á é í ó ú — marks the stressed syllable on every word that departs from the default rules, and by default words ending in a vowel, -n, or -s are stressed on the penultimate syllable (llana/grave) while words ending in any other consonant are stressed on the final syllable (aguda). In IPA, primary stress is marked with `/ˈ/` before the stressed syllable. The acute accent never changes vowel quality — Spanish has no vowel-quality alternation by stress.

### The two reference accents

Two co-equal reference accents are documented in parallel throughout this guide:

- **Castilian (CAST)** — Peninsular Standard Castilian, with **distinción** (the `/θ/` ~ `/s/` contrast: caza `/ˈkaθa/` ≠ casa `/ˈkasa/`), apico-alveolar `/s/`, and a back `/x/` ~ `[χ]`.
- **Latin American (LATAM)** — General Latin American, with **seseo** (`/θ/` merged into `/s/`: caza = casa = `/ˈkasa/`), near-universal yeísmo, and frequent jota-aspiration `/x/` → `[h]`.

Both accents share near-universal yeísmo, syllable-timed rhythm, the clean 5-vowel system, and spirantization of `/b d ɡ/`. Where an entry differs between the accents, both forms are given.

### The clean 5-vowel system

Spanish has a fully symmetric, economical 5-vowel system — `/a e i o u/` — with two front unrounded vowels `/i e/`, one open central `/a/`, and two back rounded vowels `/o u/`. There is NO phonemic vowel length and NO vowel reduction: unstressed vowels retain their full quality, so Spanish has no schwa and no weak-vowel set (a major typological contrast with English and French). The glides `/j w/` combine with these vowels to form diphthongs and triphthongs.

## Phonological Inventory

The complete phonemic inventory of Modern Spanish, organized by IPA categories. Documented in parallel for two reference accents: Castilian (Peninsular / European Standard Castilian) and Latin American (general / pan-American standard). The two accents share an identical vowel system (the canonical five vowels `/a e i o u/`) and differ in the consonant inventory mainly through two parameters: **distinción vs seseo** (Castilian contrasts `/θ/` ~ `/s/`, e.g. *caza* `/ˈkaθa/` 'hunt' vs *casa* `/ˈkasa/` 'house'; Latin American merges both into `/s/`, *caza* = *casa* = `/ˈkasa/`) and, secondarily, **lleísmo vs yeísmo** (conservative lleísta varieties keep the lateral `/ʎ/` distinct from `/ʝ/`; the near-universal modern norm is yeísta, `/ʎ/` → `/ʝ/`). The result is a small, stable inventory of about 17 consonant phonemes in general seseo-yeísta Spanish, rising to about 19 in full Castilian (distinción + lleísmo). The IPA used follows the 2015 revision; `/slashes/` mark phonemes, `[brackets]` mark phonetic realizations.

### Consonant Phonemes

All consonant phonemes of Modern Spanish arranged by place and manner of articulation. The inventory is shared across Castilian and Latin American Spanish except for two phonemes whose status is dialect-dependent: `/θ/` (the voiceless dental/interdental fricative) exists only in distinción-speaking Castilian, and `/ʎ/` (the palatal lateral approximant) exists only in conservative lleísta varieties. The hallmark phonetic process of the language is the **spirantization** (lenition) of the voiced stops `/b d ɡ/` to the approximants `[β ð ɣ]` in most positions; these are allophones, not separate phonemes.

**Total consonant phonemes:** 17–19  
Phoneme count is dialect-dependent. General seseo-yeísta Spanish (the broadest Latin American and much modern Peninsular usage) has about 17 consonant phonemes: 6 plosives `/p b t d k ɡ/` + 1 affricate `/tʃ/` + 4 fricatives `/f s x ʝ/` + 3 nasals `/m n ɲ/` + 1 lateral approximant `/l/` + 2 rhotics `/r ɾ/` = 17. Full Castilian adds the voiceless dental/interdental fricative `/θ/` (distinción) for 18, and conservative lleísta varieties (Andean highlands, Paraguay, parts of northern/rural Spain) additionally retain the palatal lateral `/ʎ/` for the often-cited maximum of 19.

**Key allophones** (not separate phonemes): the voiced stops `/b d ɡ/` spirantize to the approximants `[β ð ɣ]` except after a pause, after a nasal, and (for `/d/`) after `/l/` — the single most characteristic phonetic feature of Spanish; `/n/` assimilates in place to a following consonant, surfacing as `[m ɱ n̪ n ɲ ŋ]`; `/s/` voices to `[z]` before a voiced consonant (e.g. *mismo* `[ˈmizmo]`); coda `/s/` aspirates to `[h]` (or is lost) in Caribbean and Andalusian Spanish; `/x/` ranges from `[x]`~`[χ]` (Castilian) to a softer `[h]` (Caribbean and much of Latin America).

**Phonemic rhotic contrast:** the alveolar trill `/r/` and the alveolar tap `/ɾ/` contrast in intervocalic position (*perro* `/ˈpero/` 'dog' vs *pero* `/ˈpeɾo/` 'but'); elsewhere their distribution is largely complementary. `/ʝ/` undergoes *rehilamiento* (strengthening) to `[ʒ]`~`[ʃ]` in Rioplatense Spanish (*yo* `[ʃo]`).

#### IPA Consonant Chart

IPA consonant chart for Modern Spanish (rows = manner, columns = place). Where a cell holds two symbols, voiceless precedes voiced. Phonemes whose existence is dialect-conditioned are flagged in the accompanying note: `/θ/` is Castilian-only (distinción) and `/ʎ/` is lleísta-only.

| Manner | Bilabial | Labiodental | Dental | Alveolar | Postalveolar / Palatal | Velar |
|---|---|---|---|---|---|---|
| Plosive | p b |  | t d |  |  | k ɡ |
| Affricate |  |  |  |  | tʃ |  |
| Nasal | m |  |  | n | ɲ |  |
| Fricative |  | f | θ | s | ʝ | x |
| Tap |  |  |  | ɾ |  |  |
| Trill |  |  |  | r |  |  |
| Lateral approximant |  |  |  | l | ʎ |  |

*Two cells are dialect-conditioned: `/θ/` (dental fricative) appears only in distinción-speaking Castilian — seseo varieties leave that cell empty and use `/s/` for both 'caza' and 'casa'; `/ʎ/` (palatal lateral) appears only in conservative lleísta varieties — yeísta varieties (the modern majority) leave that cell empty and merge it into `/ʝ/`. `/b d ɡ/` are shown as plosives but surface as the approximants `[β ð ɣ]` in most contexts (spirantization). The `/ʝ/` phoneme is listed once in the postalveolar/palatal column though it spans palatal articulation; it is the merger target of yeísmo. The glides `/j w/` are NOT counted here as consonant phonemes: they are treated as the on-/off-glide elements of diphthongs and are catalogued in the vowel section. Phoneme tally: general seseo-yeísta inventory = p b t d k ɡ (6) + tʃ (1) + f s x ʝ (4) + m n ɲ (3) + l (1) + r ɾ (2) = 17; add `/θ/` for Castilian distinción = 18; add `/ʎ/` for lleísmo = 19.*

#### Notes by Place of Articulation

- **Bilabial:** `/p b m/`. `/p/` (as in *pino* 'pine') is voiceless and UNASPIRATED in all positions — a major contrast with English, which aspirates `/p t k/` in stressed onsets. `/b/` (as in *vaca* 'cow', *barco* 'ship'; spelled both 'b' and 'v', which are not distinguished in Spanish) spirantizes to the voiced bilabial approximant `[β]` except after a pause or a nasal (e.g. *lobo* `[ˈloβo]` vs *un barco* `[umˈbaɾko]`). `/m/` as in *mano* 'hand'.
- **Labiodental:** `/f/` (as in *foco* 'focus') is the only labiodental phoneme; Spanish has no phonemic `/v/` — orthographic 'v' is realized as `/b/`. The labiodental nasal `[ɱ]` occurs only as an assimilatory allophone of `/n/` before `/f/` (e.g. *enfermo* `[eɱˈfeɾmo]`).
- **Dental:** `/t d θ/`. `/t/` and `/d/` are DENTAL (laminal, articulated against the back of the upper teeth) in Spanish, not alveolar as in English; `/t/` is unaspirated. `/d/` spirantizes to the voiced dental approximant `[ð]` except after a pause, a nasal, or `/l/` (e.g. *nada* `[ˈnaða]` vs *falda* `[ˈfalda]`); word-final `/d/` is often weakened or dropped (*Madrid* `[maˈðɾi(θ)]`). `/θ/` (the voiceless dental/interdental fricative, as in *caza* 'hunt', *cielo* 'sky' `/ˈθjelo/` (Cast.) ~ `/ˈsjelo/` (LatAm), *zapato* 'shoe') is CASTILIAN-ONLY: it exists only in distinción-speaking Peninsular Spanish. In seseo varieties (all of Latin America, the Canaries, parts of Andalusia) `/θ/` is merged into `/s/`, so *caza* and *casa* are homophones `/ˈkasa/`.
- **Alveolar:** `/s n l r ɾ/`. `/s/` (as in *casa* 'house', *sol* 'sun') is the Spanish sibilant; in much of Castile it is the apico-alveolar `[s̺]` (a retracted, slightly 'sh'-like quality), while seseo varieties use a laminal/dental `[s̪]`. `/s/` voices to `[z]` before voiced consonants (*mismo* `[ˈmizmo]`); coda `/s/` aspirates to `[h]` or is lost in Caribbean, coastal, and Andalusian Spanish. `/n/` as in *nada* 'nothing'; it assimilates in place to a following consonant. `/l/` (as in *lado* 'side') is the alveolar lateral; unlike English it is CLEAR `[l]` in all positions, with no dark/velarized `[ɫ]` in codas. The two rhotics contrast only intervocalically: the alveolar TRILL `/r/` (*perro* 'dog', also word-initial and after `/n l s/`) vs the alveolar TAP `/ɾ/` (*pero* 'but', *caro* 'expensive').
- **Postalveolar / Palatal:** `/tʃ ʝ ɲ ʎ/`. `/tʃ/` (the voiceless postalveolar affricate, as in *mucho* 'much', spelled 'ch') is the only affricate in Spanish. `/ʝ/` (the voiced palatal fricative/approximant, as in *yo* 'I', *mayo* 'May', and — under yeísmo — *llave* 'key' `/ˈʝabe/` `[ˈʝaβe]` (yeísta) ~ `/ˈʎabe/` `[ˈʎaβe]` (lleísta)) ranges from a weak approximant `[ʝ̞]`~`[j]` intervocalically to a stronger fricative; in Rioplatense Spanish it undergoes *rehilamiento* to `[ʒ]`~`[ʃ]` (*yo* `[ʃo]`). `/ɲ/` (the palatal nasal, as in *año* 'year' `[ˈaɲo]`, *España* 'Spain' `[esˈpaɲa]`, spelled 'ñ') is a full phoneme contrasting with `/n/`. `/ʎ/` (the palatal lateral approximant, as in *llave* 'key' `/ˈʎabe/` `[ˈʎaβe]` (lleísta) ~ `/ˈʝabe/` `[ˈʝaβe]` (yeísta), *calle* 'street') is LLEÍSTA-ONLY: it survives as a distinct phoneme only in conservative varieties (Andean highlands, Paraguay, and shrinking pockets of northern/rural Spain). Under the near-universal YEÍSMO it has merged into `/ʝ/`, so *llave* and (where relevant) homophones with 'y' are pronounced alike.
- **Velar:** `/k ɡ x/`. `/k/` (as in *casa* 'house', *quiero* 'I want') is voiceless and UNASPIRATED. `/ɡ/` (as in *gato* 'cat', *guerra* 'war') spirantizes to the voiced velar approximant `[ɣ]` except after a pause or a nasal (e.g. *lago* `[ˈlaɣo]`, *gato* `[ˈɣato]` in connected speech vs *un gato* `[uŋˈɡato]`, *tengo* `[ˈteŋɡo]`). `/x/` (the voiceless velar fricative, as in *jamón* 'ham', *gente* 'people', spelled 'j' and 'g' before e/i) is realized as `[x]`~`[χ]` (often strongly fricated, even uvular) in Castilian, but weakens to a soft glottal `[h]` in the Caribbean and much of Latin America.

### Vowel Phonemes

The vowel phonemes of Modern Spanish. Spanish has a maximally simple and stable five-vowel system `/a e i o u/`, IDENTICAL across Castilian and Latin American accents (the vowels do not participate in the distinción/seseo or lleísmo/yeísmo splits, which are purely consonantal). Three properties set the Spanish vowel system sharply apart from English: (1) there is NO phonemic vowel length — vowels are not contrastively long or short; (2) there is NO vowel reduction — unstressed vowels keep their full quality and are never reduced to schwa, so Spanish has no `/ə/`; (3) vowel quality is STABLE and largely context-independent, with only minor allophonic raising/lowering. This section covers the five simple (monophthong) vowels and the two glides `/j w/` that combine with them to form diphthongs and triphthongs; the diphthongs themselves are enumerated in the separate diphthongs section.

**Castilian vowel count:** 5 | **Latin American vowel count:** 5  
Both reference accents have exactly 5 vowel phonemes: `/a e i o u/`. There is no GA/RP-style divergence in the vowel inventory and no rhoticity issue (Spanish has no r-coloured vowels). Crucially, unlike English there is NO phonemic length distinction and NO unstressed reduction: *banana* is `[baˈnana]` with three full, clear `[a]` vowels, never reduced. Stress is LEXICAL and contrastive and is marked orthographically with the acute accent where it is irregular (*término* 'term' / *termino* 'I finish' / *terminó* 'he/she finished' — a minimal triplet differing only in stress placement). Allophonic detail: mid vowels `/e o/` lower slightly to `[ɛ ɔ]` in closed syllables and adjacent to certain consonants; `/a/` may back to `[ɑ]` before `/o u l/`; high vowels `/i u/` become the glides `[j w]` when unstressed and adjacent to another vowel. The two GLIDES `/j w/` are the non-syllabic counterparts of `/i u/` and occur in rising diphthongs (*tiene* `[ˈtjene]`, *bueno* `[ˈbweno]`), falling diphthongs (*aire* `[ˈajɾe]`, *causa* `[ˈkawsa]`), and triphthongs (*buey* `[bwej]`, *estudiáis* `[estuˈðjajs]`); whether they are best analysed as independent phonemes or as positional variants of `/i u/` is debated, and they are not counted among the five vowel phonemes here.

#### IPA Vowel Chart

IPA vowel quadrilateral for the five Spanish monophthongs (rows = height, columns = backness/rounding). The chart is identical for Castilian and Latin American Spanish. The peripheral, symmetric, evenly spaced layout reflects the system's stability and the absence of central/reduced vowels.

| Height | Front (unrounded) | Central | Back (rounded) |
|---|---|---|---|
| close | i |  | u |
| mid | e |  | o |
| open |  | a |  |

*The system is a textbook symmetric five-vowel triangle: two close `/i u/`, two mid `/e o/`, one open `/a/`. There is NO central column except for the single low vowel `/a/` (phonetically central-to-front `[a~ä]`), and crucially NO schwa `/ə/` — every vowel is fully realized in both stressed and unstressed syllables. Phonetically the mid vowels sit between cardinal close-mid and open-mid (i.e. `[e̞ o̞]`); `/e/` is front unrounded, `/o/` back rounded, `/i/` close front unrounded, `/u/` close back rounded. No length marks (ː) appear because Spanish has no phonemic vowel length.*

#### Monophthong Inventory

| IPA | Height | Backness | Rounding | Example | Distribution |
|---|---|---|---|---|---|
| `/a/` | open | central | unrounded | *casa* 'house', *mapa* 'map', *and* | The single low vowel; phonetically central `[a]`~`[ä]`, backing to `[ɑ]` before `/o u l/` (e.g. *mal*). Fully stable and full in both stressed and unstressed syllables (*banana* `[baˈnana]`). Identical in Castilian and Latin American Spanish. |
| `/e/` | mid (close-mid to open-mid) | front | unrounded | *mesa* 'table', *pez* 'fish', *café* | Front mid unrounded vowel, phonetically `[e̞]`. Lowers slightly toward `[ɛ]` in closed syllables (e.g. *perro*) and near `/r/` or `/x/`; never reduced when unstressed. No length contrast. |
| `/i/` | close | front | unrounded | *vino* 'wine', *sí* 'yes', *mil* 'thousand' | Close front unrounded vowel. When unstressed and adjacent to another vowel it becomes the glide `[j]` (e.g. *tiene* `[ˈtjene]`, *aire* `[ˈajɾe]`). Always full quality; no reduction or length contrast. |
| `/o/` | mid (close-mid to open-mid) | back | rounded | *como* 'I eat / like', *sol* 'sun', *no* | Back mid rounded vowel, phonetically `[o̞]`. Lowers slightly toward `[ɔ]` in closed syllables and near `/r x/`; never reduced when unstressed (e.g. the final `/o/` of *como* stays full). No length contrast. |
| `/u/` | close | back | rounded | *luna* 'moon', *tú* 'you', *sur* 'south' | Close back rounded vowel. When unstressed and adjacent to another vowel it becomes the glide `[w]` (e.g. *bueno* `[ˈbweno]`, *causa* `[ˈkawsa]`). Silent in the digraphs 'que/qui' and 'gue/gui' (*queso* `[ˈkeso]`) unless written with diaeresis 'ü' (*pingüino* `[piŋˈɡwino]`). Full quality always; no reduction or length contrast. |

#### Glides

The two non-syllabic high vocoids (semivowels/glides) that combine with the five monophthongs to build diphthongs and triphthongs. They are the non-syllabic counterparts of the close vowels `/i u/` and are bracketed here as the on-glide (rising diphthong) and off-glide (falling diphthong) elements; the full diphthong and triphthong inventory is enumerated in the separate diphthongs section. Their phonemic status is debated — many analyses treat `[j w]` as positional allophones of `/i u/` rather than independent phonemes — so they are NOT counted among the five vowel phonemes.

Both glides behave identically in Castilian and Latin American Spanish; they are unaffected by the seseo/distinción and yeísmo/lleísmo splits. Care should be taken not to confuse the vocalic glide `[j]` (the off/on-glide of a diphthong, as in *tiene* `[ˈtjene]`, *rey* `[rej]`) with the consonant phoneme `/ʝ/` (the palatal fricative/approximant of *yo*, *mayo*): they are distinct, though phonetically close.

| IPA | Name | Vowel Counterpart | Example | Notes |
|---|---|---|---|---|
| `[j]` | palatal glide (front semivowel) | `/i/` | *tiene* `[ˈtjene]` 'has', *aire* `[ˈajɾe]` 'air', *rey* `[rej]` 'king' | Non-syllabic front close vocoid; on-glide in rising diphthongs (ie, ia, io, iu) and off-glide in falling diphthongs (ai, ei, oi). Distinct from the consonant `/ʝ/`. |
| `[w]` | labio-velar glide (back rounded semivowel) | `/u/` | *bueno* `[ˈbweno]` 'good', *causa* `[ˈkawsa]` 'cause', *deuda* `[ˈdewða]` 'debt' | Non-syllabic back close rounded vocoid; on-glide in rising diphthongs (ue, ua, uo, ui) and off-glide in falling diphthongs (au, eu, ou). Appears after 'g/q' in 'gua, gue (with ü), cua' sequences. |

## Consonants

The consonant phonemes of Modern Spanish, documented in parallel for two reference accents: Castilian (Peninsular / European Standard Castilian) and Latin American (general / pan-American standard). The two accents differ chiefly in two phonemic mergers: **seseo** (Latin American varieties merge Castilian `/θ/` into `/s/`, so 'caza' `/ˈkaθa/` = 'casa' `/ˈkasa/` = `/ˈkasa/`), and the near-universal **yeísmo** (the historical `/ʎ/` ~ `/ʝ/` contrast collapses to `/ʝ/`, so 'pollo' = 'poyo'; conservative Andean/Paraguayan **lleísta** varieties still keep `/ʎ/`). Counting `/θ/` and `/ʎ/`, full Castilian *distinción*-*lleísmo* has ~19 consonant phonemes; general *seseo*-*yeísta* Spanish has ~17. The hallmark phonological process of Spanish is the **spirantization** of the voiced stops `/b d ɡ/` to the approximants `[β ð ɣ]` in most positions (after vowels, glides, and most consonants); they surface as true stops `[b d ɡ]` only utterance-initially and after a nasal (and `/d/` also after `/l/`). Spanish maintains a **trill** `/r/` ~ **tap** `/ɾ/` phonemic contrast in intervocalic position (perro 'dog' `/ˈpero/` vs pero 'but' `/ˈpeɾo/`; carro vs caro). Phonemic values are given in /slashes/ and phonetic realisations in [brackets], following IPA (2015 revision). The IPA `/b d ɡ ʝ x r ɾ/` values are accent-neutral; accent-specific surface realisations (seseo, yeísmo, rehilamiento, coda `/s/`-aspiration, uvular `/x/`, etc.) are recorded in the allophony notes.

**Consonant phonemes:** 19 | **Effective phonemes:** 17  
19 phonemes counts the full conservative Castilian inventory (*distinción* + *lleísmo*), which keeps both `/θ/` (the voiceless dental fricative, written *c* before *e*/*i* and *z*) and `/ʎ/` (the palatal lateral, written *ll*). The dominant general standard is *seseo*-*yeísta*: `/θ/` merges into `/s/` and `/ʎ/` merges into `/ʝ/`, giving an effective inventory of 17 consonant phonemes. Spanish consonant spelling is mostly transparent but has notable many-to-one mappings: `/k/` is written *c* (before *a*/*o*/*u*), *qu* (before *e*/*i*) and *k*; `/x/` is written *j* and *g* (before *e*/*i*); `/b/` is written *b* and *v* (no `/b/`–`/v/` contrast exists — both are the SAME phoneme); `/θ/` (or `/s/` under seseo) is written *z* and *c* (before *e*/*i*). The letter *h* is silent (it spells no phoneme), and the digraphs *ch* `/tʃ/`, *ll* `/ʎ~ʝ/` and *rr* `/r/` each spell a single phoneme. The affricate `/tʃ/` is treated as a single phoneme.

### Consonant Inventory

The 19 consonant phonemes with their IPA value, phonetic name, spelling graphemes, example words (with IPA), and allophony notes. The two accent-specific mergers (`/θ/` under *seseo*, `/ʎ/` under *yeísmo*) are flagged in their respective rows.

| # | IPA | Name | Spellings | Example Words | Allophony Notes |
|---|---|---|---|---|---|
| 1 | `/p/` | voiceless bilabial plosive | p | pan `/pan/`; capa `/ˈkapa/`; septiembre `/sepˈtjembɾe/` | Crucially UNASPIRATED `[p]` in all positions — Spanish voiceless stops have no aspiration, a major contrast with English (Spanish 'pan' `[pan]`, not `[pʰan]`). Fully released. In syllable codas (rare, mostly in learned/borrowed words such as 'apto', 'concepto') it may voice toward `[b̥]` or weaken/elide in casual speech. Same in Castilian and Latin American. |
| 2 | `/b/` | voiced bilabial plosive | b, v | barco `/ˈbaɾko/`; vaca `/ˈbaka/`; haba `/ˈaba/` `[ˈaβa]` | There is NO `/b/`–`/v/` distinction in Spanish: the letters *b* and *v* both spell this one phoneme ('baca' = 'vaca' phonemically; `[v]` is not a native sound). SPIRANTIZATION (the hallmark Spanish process): realised as a true stop `[b]` only utterance-initially (pause) and after a nasal (un barco `[umˈbaɾko]`, hombre `[ˈombɾe]`); ELSEWHERE — most importantly between vowels and after most consonants — it weakens to the voiced bilabial approximant `[β]` (haba `[ˈaβa]`, la vaca `[laˈβaka]`, árbol `[ˈaɾβol]`). Same in Castilian and Latin American. |
| 3 | `/t/` | voiceless dental plosive | t | tomate `/toˈmate/`; patata `/paˈtata/`; antes `/ˈantes/` | DENTAL (laminal-denti-alveolar) `[t̪]`, with the tongue tip on the back of the upper teeth — NOT the English alveolar `[t]`, and NOT aspirated (Spanish 'tos' `[t̪os]`, not `[tʰɑs]`). There is no flapping: intervocalic `/t/` stays a full stop, so Spanish 'todo' is never tapped the way American English 'water' is. Same in Castilian and Latin American. |
| 4 | `/d/` | voiced dental plosive | d | dedo `/ˈdedo/`; nada `/ˈnada/` `[ˈnaða]`; usted `/usˈted/` | DENTAL `[d̪]`, not alveolar. SPIRANTIZATION: realised as a true stop `[d̪]` utterance-initially, after a nasal (mando `[ˈmando]`) and after `/l/` (caldo `[ˈkald̪o]`); ELSEWHERE — especially intervocalically — it weakens to the voiced dental approximant `[ð]` (dedo `[ˈdeð̞o]`, nada `[ˈnaða]`, cada `[ˈkaða]`). Word-final `/d/` is heavily reduced: in much of Spain it is a faint `[ð̞]` or fully ELIDED (usted `[usˈte]`, Madrid `[maˈðɾi]`); Castilian colloquial speech often realises final *-d* as `[θ]` (Madrid `[maˈðɾiθ]`). Latin American varieties likewise weaken or drop final *-d* (verdad `[beɾˈða]`). |
| 5 | `/k/` | voiceless velar plosive | c (before a, o, u), qu (before e, i), k, ch (in loans) | casa `/ˈkasa/`; queso `/ˈkeso/`; kilo `/ˈkilo/` | UNASPIRATED `[k]` in all positions. Written *c* before *a*/*o*/*u* and before a consonant (casa, claro), *qu* before *e*/*i* (queso, quien — the *u* is silent), and *k* in loanwords (kilo). In codas (mostly learned words: acto, técnico) it may voice to `[ɡ]`/`[ɣ]` or weaken in casual speech ('doctor' `[doɣˈtoɾ]`). Same in Castilian and Latin American. |
| 6 | `/ɡ/` | voiced velar plosive | g (before a, o, u), gu (before e, i), gü (before e, i, for [ɡw]) | gato `/ˈɡato/`; guerra `/ˈɡera/`; lago `/ˈlaɡo/` `[ˈlaɣo]` | Written *g* before *a*/*o*/*u* (gato), *gu* before *e*/*i* where the *u* is silent (guerra `[ˈɡera]`), and *gü* (with diaeresis) before *e*/*i* when the *u* IS pronounced `[ɡw]` (pingüino `[piŋˈɡwino]`). SPIRANTIZATION: a true stop `[ɡ]` only utterance-initially and after a nasal (tengo `[ˈteŋɡo]`); ELSEWHERE it weakens to the voiced velar approximant `[ɣ]` (lago `[ˈlaɣo]`, la gata `[laˈɣata]`, agua `[ˈaɣwa]`). Same in Castilian and Latin American. |
| 7 | `/tʃ/` | voiceless postalveolar affricate | ch | chico `/ˈtʃiko/`; leche `/ˈletʃe/`; noche `/ˈnotʃe/` | Single phoneme, always spelled with the digraph *ch*. Standard realisation is the affricate `[tʃ]`. In several varieties — Andalusian, Chilean, northern Mexican (Sonora/Chihuahua), Panamanian, Canary Islands — it is DEAFFRICATED to a fricative `[ʃ]` (muchacho `[muˈʃaʃo]`); this is stigmatised in some regions but very common. The standard Castilian and most Latin American norms keep the full affricate. |
| 8 | `/f/` | voiceless labiodental fricative | f | feo `/ˈfeo/`; café `/kaˈfe/`; alfombra `/alˈfombɾa/` | Stable labiodental `[f]` in standard speech. In rural and colloquial varieties (and historically) it may be realised as a bilabial fricative `[ɸ]` or, before `/w/`, weaken (fuego `[ˈfweɣo]` ~ `[ˈɸweɣo]`); some dialects show *f* > `[x]`/`[h]` in items like 'fuerte'. The standard norm keeps `[f]`. There is no voiced `[v]` counterpart in the native system. |
| 9 | `/θ/` | voiceless dental fricative *(Castilian only)* | z, c (before e, i) | zapato `/θaˈpato/` (Cast.); `/saˈpato/` (LatAm); cinco `/ˈθiŋko/` (Cast.); `/ˈsiŋko/` (LatAm); caza `/ˈkaθa/` (Cast.); `/ˈkasa/` (LatAm) — merges with 'casa' | CASTILIAN-ONLY phoneme (DISTINCIÓN): an interdental/dental `[θ]` like English 'th' in 'thin', written *z* (anywhere) and *c* before *e*/*i*. It contrasts with `/s/`: 'caza' `/ˈkaθa/` vs 'casa' `/ˈkasa/`, 'cocer' vs 'coser'. Under SESEO — all of Latin America, the Canary Islands, and parts of Andalusia — `/θ/` does NOT exist: it has merged into `/s/`, so 'caza' = 'casa' = `/ˈkasa/` and there is no *z*/*c*-vs-*s* distinction. (The reverse merger, CECEO, in which `/s/` is realised as `[θ]`, occurs in parts of Andalusia.) Voices to `[ð]` before a voiced consonant in Castilian (hazlo `[ˈaðlo]`). |
| 10 | `/s/` | voiceless alveolar fricative | s, z (in seseo), c (before e, i, in seseo), x ([ks] > coda [s]) | sol `/sol/`; casa `/ˈkasa/`; mismo `/ˈmismo/` (`[ˈmizmo]`) | Major source of dialect variation. (1) QUALITY: Castilian (north-central Spain) uses an APICO-ALVEOLAR `[s̺]` — a retracted, slightly 'hushing' *s* made with the tongue tip — whereas most of Latin America and southern Spain use a laminal/predorsal `[s]` closer to English. (2) VOICING: regressively voices to `[z]` before a voiced consonant in all varieties (mismo `[ˈmizmo]`, desde `[ˈdezðe]`, los gatos `[lozˈɣatos]`). (3) CODA `/s/`-ASPIRATION: in Caribbean (Cuba, Puerto Rico, Dominican Republic, coastal Venezuela/Colombia), much of Andalusia and the Canaries, and lowland/coastal Latin America, syllable-final `/s/` weakens to `[h]` or is fully ELIDED (estos `[ˈehtoh]` ~ `[ˈetoh]`, las casas `[lahˈkasah]`); this is one of the most salient pan-Hispanic isoglosses. (4) Under SESEO, `/s/` also absorbs the words spelled *z* and *c*+*e*/*i*. Word *x* is `/ks/` (examen `[ekˈsamen]`), reducing to coda `[s]` in casual speech (extra `[ˈestɾa]`). |
| 11 | `/x/` | voiceless velar fricative | j, g (before e, i), x (in some proper nouns: México, Texas) | jamón `/xaˈmon/`; gente `/ˈxente/`; México `/ˈmexiko/` | Written *j* (everywhere) and *g* before *e*/*i* (gente, gitano). REALISATION varies sharply by region: in Castilian and other central/northern Peninsular speech it is strongly post-velar to UVULAR `[χ]`, with audible friction (jamón `[χaˈmon]`); in much of Latin America it is a plainer velar `[x]`; in the Caribbean, coastal/lowland Latin America, Andalusia and the Canaries it weakens to a simple glottal `[h]` (jamón `[haˈmon]`, gente `[ˈhente]`). A handful of place names preserve the archaic spelling *x* for this sound (México, Oaxaca, Texas = `[ˈmexiko]`, etc.), pronounced `/x/`, NOT `/ks/`. |
| 12 | `/ʝ/` | voiced palatal fricative/approximant | y (before a vowel), ll (in yeísmo), hi- (in hierba, hielo) | yo `/ʝo/` (`[ɟʝo]`; Rioplatense `[ʃo]`); mayo `/ˈmaʝo/`; calle `/ˈkaʝe/` (yeísmo); `/ˈkaʎe/` (lleísmo) | The consonantal 'y' sound, written *y* before a vowel (yo, mayo, ya) and — under near-universal YEÍSMO — also written *ll*, since historical `/ʎ/` has merged into it (calle `[ˈkaʝe]`, pollo `[ˈpoʝo]` = poyo). Realisation: a palatal approximant/fricative `[ʝ]` between vowels, strengthening to an AFFRICATE `[ɟʝ]` (or stop-like) utterance-initially, after a nasal, and after `/l/` (yo `[ɟʝo]`, cónyuge, inyección `[iɲɟʝekˈθjon]`). RIOPLATENSE (Buenos Aires, Montevideo) shows REHILAMIENTO / *žeísmo*–*šeísmo*: `/ʝ/` (and merged *ll*) is realised as a strident postalveolar `[ʒ]` or, increasingly, devoiced `[ʃ]` — so 'yo' = `[ʒo]` ~ `[ʃo]`, 'calle' = `[ˈkaʃe]`, 'lluvia' = `[ˈʃuβja]`. In some Andean and other zones `/ʝ/` weakens or elides next to `/i/` and `/e/` (gallina, ella). |
| 13 | `/m/` | voiced bilabial nasal | m, n (before bilabials: un peso) | madre `/ˈmadɾe/` `[ˈmaðɾe]`; cama `/ˈkama/`; campo `/ˈkampo/` | Stable bilabial `[m]` in onsets. The `/m/`–`/n/` contrast is neutralised in the CODA: syllable-final nasals assimilate in place to a following consonant, so the `[m]` heard in 'campo' `[ˈkampo]` or 'un peso' `[umˈpeso]` is the place-assimilated realisation of underlying `/n/` rather than phonemic `/m/` (see `/n/`). Word-final orthographic *m* is rare and limited to loans/Latinisms (álbum), often pronounced `[n]`. Same in Castilian and Latin American. |
| 14 | `/n/` | voiced alveolar nasal | n | no `/no/`; mano `/ˈmano/`; tengo `/ˈtenɡo/` (`[ˈteŋɡo]`) | Alveolar `[n]` in onsets and before alveolars. In the CODA it undergoes thoroughgoing PLACE ASSIMILATION to the following consonant: bilabial `[m]` before `/p b m/` (un peso `[umˈpeso]`, énfasis); labiodental `[ɱ]` before `/f/` (énfasis `[ˈeɱfasis]`, confeti); dental `[n̪]` before `/t d/` (antes `[ˈan̪tes]`, donde); palatal `[ɲ]` before `/tʃ ʝ/` (ancho `[ˈaɲtʃo]`); and VELAR `[ŋ]` before `/k ɡ x/` (tengo `[ˈteŋɡo]`, banco `[ˈbaŋko]`, naranja `[naˈɾaŋxa]`). WORD-FINAL `/n/` is alveolar `[n]` in standard Castilian and central Latin America, but VELARISES to `[ŋ]` (or nasalises the vowel and elides) in Caribbean, Andalusian, Canarian, Central American and much coastal Latin American speech (pan `[paŋ]`, bien `[bjeŋ]`). |
| 15 | `/ɲ/` | voiced palatal nasal | ñ | año `/ˈaɲo/`; niño `/ˈniɲo/`; España `/esˈpaɲa/` | A distinct phoneme spelled with the dedicated letter *ñ*, contrasting with `/n/` + glide: 'año' `/ˈaɲo/` vs 'ano'; 'huraño' vs 'urano'. A true single palatal nasal `[ɲ]`, not the sequence `[nj]` (though casual/American speech sometimes realises it close to `[nj]`). Restricted to onset position (never word-final or syllable-final in native words). Same place value in Castilian and Latin American. |
| 16 | `/l/` | voiced alveolar lateral approximant | l | luna `/ˈluna/`; sol `/sol/`; papel `/paˈpel/` | A CLEAR (non-velarised) alveolar `[l]` in ALL positions, including codas — unlike English, Spanish has no 'dark' `[ɫ]` (sol `[sol]`, not `[soɫ]`; this is a frequent giveaway of an English accent). Assimilates in place before a following dental or palatal consonant: dental `[l̪]` before `/t d/` (alto `[ˈal̪to]`, caldo), palatal `[lʲ]` before `/tʃ ʝ/` (colcha). In Caribbean and Andalusian speech coda `/l/` and `/ɾ/` may neutralise (LAMBDACISM/rhotacism: 'puerta' ~ `[ˈpwelta]` or 'alma' ~ `[ˈaɾma]`). |
| 17 | `/ʎ/` | voiced palatal lateral approximant *(lleísta only)* | ll | llave `/ˈʎabe/` `[ˈʎaβe]` (lleísmo); `/ˈʝabe/` `[ˈʝaβe]` (yeísmo); pollo `/ˈpoʎo/` (lleísmo); `/ˈpoʝo/` (yeísmo); calle `/ˈkaʎe/` (lleísmo); `/ˈkaʝe/` (yeísmo) | LLEÍSTA-ONLY phoneme: a palatal lateral `[ʎ]` (like Italian 'gli'), spelled with the digraph *ll*. It is preserved only in conservative LLEÍSTA varieties — much of the Andes (highland Peru, Bolivia, Ecuador, parts of Colombia), Paraguay (reinforced by Guaraní), and a shrinking number of rural northern-Peninsular speakers. For the OVERWHELMING majority of speakers, YEÍSMO has MERGED `/ʎ/` into `/ʝ/`, so *ll* and *y* are pronounced identically (calle = caye, pollo = poyo); under yeísmo this phoneme does not exist as a separate unit and '*ll*' is realised as `/ʝ/` (or, in Rioplatense, as `[ʒ]`/`[ʃ]`). Where present, `/ʎ/` contrasts minimally with `/ʝ/`: 'pollo' `/ˈpoʎo/` vs 'poyo' `/ˈpoʝo/`, 'halla' vs 'haya'. |
| 18 | `/r/` | voiced alveolar trill | rr, r (word-initial), r (after l, n, s) | perro `/ˈpero/` (`[ˈpero]`, trill) — vs 'pero' `/ˈpeɾo/`; rosa `/ˈrosa/`; carro `/ˈkaro/` — vs 'caro' `/ˈkaɾo/` | The MULTIPLE alveolar TRILL `[r]` (two or more apical taps). It contrasts PHONEMICALLY with the single tap `/ɾ/` ONLY between vowels, which is the contrast's stronghold: 'perro' `/ˈpero/` (dog) vs 'pero' `/ˈpeɾo/` (but); 'carro' vs 'caro'; 'pero' vs 'perro'. The trill is written *rr* between vowels, but single *r* when word-initial (rosa, ramo) and after `/l n s/` (alrededor, honra, Israel), where only the trill occurs. REGIONAL realisations of `/r/` include an assibilated/fricative trill `[r̝]` (highland Andes, Costa Rica, parts of Mexico — 'carro' `[ˈkar̝o]`) and a posterior/uvular `[ʁ]`~`[χ]` (rural Puerto Rico — 'perro' `[ˈpeʁo]`, the 'erre velar' (velarized/uvular r)). Same phonemic status in Castilian and Latin American. |
| 19 | `/ɾ/` | voiced alveolar tap | r (between vowels, in clusters, in coda) | pero `/ˈpeɾo/` — vs 'perro' `/ˈpero/`; caro `/ˈkaɾo/` — vs 'carro' `/ˈkaro/`; tres `/tɾes/` | The single alveolar TAP/flap `[ɾ]` (one quick apical contact, identical to the American English flapped *t/d* in 'water'/'ladder'). Spelled with single *r* in all positions EXCEPT the trill environments (so not word-initially and not after `/l n s/`). PHONEMIC contrast with the trill `/r/` is restricted to intervocalic position: 'pero' `/ˈpeɾo/` vs 'perro' `/ˈpero/`, 'caro' vs 'carro'. The tap also occurs in onset clusters after an obstruent (tres `[tɾes]`, grande, primo) and in the coda (mar `[maɾ]`, cartón, comer); in the coda the contrast with `/r/` is neutralised (either tap or trill may surface) and the segment is prone to weakening — coda `/ɾ/` may be ELIDED (especially in infinitives: comer `[koˈme]`), assibilated, or in Caribbean/Andalusian speech merged with `/l/` (see `/l/`). Word-final `/ɾ/` is frequently dropped in rapid speech. |

### Natural Classes

Groupings of the consonant phonemes by shared phonological features, drawn from the source data. The two accent-restricted phonemes are listed where the source assigns them: `/θ/` is Castilian-only, `/ʎ/` is lleísta-only.

| Class | Members |
|---|---|
| Voiceless stops | `/p/`, `/t/`, `/k/` |
| Voiced stops | `/b/`, `/d/`, `/ɡ/` |
| Affricates | `/tʃ/` |
| Fricatives | `/f/`, `/θ/`, `/s/`, `/x/` |
| Nasals | `/m/`, `/n/`, `/ɲ/` |
| Laterals | `/l/`, `/ʎ/` |
| Rhotics | `/r/`, `/ɾ/` |
| Central approximants | `/ʝ/` |
| Obstruents | `/p/`, `/b/`, `/t/`, `/d/`, `/k/`, `/ɡ/`, `/tʃ/`, `/f/`, `/θ/`, `/s/`, `/x/`, `/ʝ/` |
| Sonorants | `/m/`, `/n/`, `/ɲ/`, `/l/`, `/ʎ/`, `/r/`, `/ɾ/` |
| Voiceless | `/p/`, `/t/`, `/k/`, `/tʃ/`, `/f/`, `/θ/`, `/s/`, `/x/` |
| Voiced | `/b/`, `/d/`, `/ɡ/`, `/ʝ/`, `/m/`, `/n/`, `/ɲ/`, `/l/`, `/ʎ/`, `/r/`, `/ɾ/` |
| Sibilants | `/s/`, `/tʃ/` |
| Spirantizing stops | `/b/`, `/d/`, `/ɡ/` |
| Castilian only | `/θ/` |
| Lleísta only | `/ʎ/` |

## Vowels

The Spanish vowel inventory. Spanish has exactly **five** vowel phonemes `/a e i o u/` arranged in a clean, symmetrical triangular system — one of the simplest and most stable vowel systems among major world languages, in sharp contrast to English. Three defining properties govern the whole system:

1. **No phonemic vowel length** — vowels are not contrastively long or short (unlike English `/ɪ/` vs `/iː/`). No length mark `/ː/` is ever used.
2. **No vowel reduction** — unstressed vowels keep their full quality and are **not** centralised to schwa `[ə]`. The two vowels of *papá* are both clear `[a]`, never `[pəˈpa]`. This is the single largest difference from English, where unstressed syllables reduce.
3. **Only minor, predictable allophonic variation** — mostly mid-vowel opening plus contextual nasalisation and devoicing. None of it creates new phonemes.

Stress is **lexical and contrastive** but is realised through prominence (intensity, pitch, duration), **not** through any change of vowel quality. Two reference accents are documented in parallel, mirroring the GA/RP framing of the English guide: **Castilian** (Peninsular / European Standard Castilian, with *distinción*) and **Latin American** (general pan-American standard, with *seseo*). The five-vowel system itself is essentially **identical** across all standard accents — dialect variation overwhelmingly affects consonants, not vowels. IPA follows the 2015 revision; `/slashes/` mark phonemic transcription and `[brackets]` mark phonetic detail. Primary stress is marked with `/ˈ/`.

### Vowel System Overview

The five Spanish vowel phonemes plotted on the height/backness grid. The system is maximally dispersed: two high (close), two mid, one low (open), with left–right symmetry between the front unrounded series `/i e/` and the back rounded series `/u o/`, and `/a/` central at the base. There are no front rounded vowels, no central vowels other than `/a/`, no nasal vowel phonemes, and no schwa.

| Dimension | Class | Vowels |
|---|---|---|
| Height | high (close) | `/i/`, `/u/` |
| Height | mid | `/e/`, `/o/` |
| Height | low (open) | `/a/` |
| Backness | front unrounded | `/i/`, `/e/` |
| Backness | central | `/a/` |
| Backness | back rounded | `/o/`, `/u/` |

- **Rounding** — only the back vowels `/o u/` are rounded; the front vowels `/i e/` and central `/a/` are unrounded. Spanish has no front rounded vowels.
- **Contrast with English** — English distinguishes ~11–15 monophthongs with phonemic length and a tense/lax (free/checked) opposition, plus pervasive reduction to schwa in weak syllables. Spanish has just 5 vowels, no length contrast, no tense/lax opposition, and no reduction — every vowel is fully realised in every syllable, stressed or not.

### Vowel Inventory

The five vowel phonemes with their default phonetic values and example words. Each example deliberately pairs **stressed** and **unstressed** occurrences of the same vowel to demonstrate that quality is identical in both — there is no reduction. The inventory is shared by both reference accents (Castilian and Latin American).

| IPA | Phonetic | Name | Spelling | Example (stressed + unstressed) |
|---|---|---|---|---|
| `/a/` | `[ä]` | open central (low) unrounded | a | *casa* `/ˈkasa/` 'house'; *patata* `/paˈtata/` 'potato'; *mamá* `/maˈma/` 'mum' |
| `/e/` | `[e]` ~ `[e̞]` ~ `[ɛ]` | close-mid to mid front unrounded | e | *bebé* `/beˈbe/` 'baby'; *leche* `/ˈletʃe/` 'milk'; *este* `/ˈeste/` 'this' |
| `/i/` | `[i]` | close front unrounded | i (also *y* alone or word-finally, e.g. *y*, *rey*) | *vivir* `/biˈbiɾ/` 'to live'; *difícil* `/diˈfiθil/` (Cast.) ~ `/diˈfisil/` (LatAm) 'difficult'; *casi* `/ˈkasi/` 'almost' |
| `/o/` | `[o]` ~ `[o̞]` ~ `[ɔ]` | close-mid to mid back rounded | o | *cómodo* `/ˈkomodo/` `[ˈkomoðo]` 'comfortable'; *ocho* `/ˈotʃo/` 'eight'; *amor* `/aˈmoɾ/` 'love' |
| `/u/` | `[u]` | close back rounded | u (silent in *que, qui, gue, gui*; pronounced in *güe, güi*) | *cuscús* `/kusˈkus/` 'couscous'; *música* `/ˈmusika/` 'music'; *espíritu* `/esˈpiɾitu/` 'spirit' |

#### Per-vowel notes

- **`/a/` — open central unrounded `[ä]`.** Phonetically a low **central** unrounded vowel, best written with the centralised symbol `[ä]`: it is neither the front cardinal `[a]` nor fully back `[ɑ]`, sitting roughly at the cardinal-4-to-5 mid position. (The bare glyph `/a/` is the IPA symbol for the front cardinal, but Spanish realises it centrally, hence `[ä]`.) Highly stable. A backed/velarised allophone `[ɑ]` may appear before `/o u/` or before a syllable-final velar `/l/` in some descriptions, but this is minor. The key fact: *a* in an unstressed syllable is the **same** `[ä]` as in a stressed one — no centralisation toward `[ə]`. In *casa* `/ˈkasa/`, both the stressed `[ˈka]` and the unstressed final `[sa]` are full clear `[a]`; in *patata* `/paˈtata/`, all three `/a/` (pretonic, stressed, post-tonic) are identical; *mamá* `/maˈma/` vs *mama* `/ˈmama/` differ only in stress placement, not vowel quality.
- **`/e/` — mid front unrounded `[e̞]`.** Phonemically a single mid front vowel; phonetically a **mid** vowel best transcribed `[e̞]` (lowered close-mid), between cardinal `[e]` and `[ɛ]`, **not** the very close `[e]` of e.g. French *été*. In the traditional (Navarro Tomás) account it **lowers** toward `[ɛ]` in predictable environments: in a closed syllable (before a coda consonant, e.g. *verde* `[ˈbɛɾðe]`), before `/r/` (trill or tap), before the velar fricative `/x/` (*teja*), and in the diphthong `/ei̯/`; and is closer `[e]` in open syllables. Modern instrumental studies find the opening to be **gradient and variable** rather than categorical — many speakers stay near mid `[e̞]` throughout — so `[ɛ]` is best read as a tendency toward greater openness, not a fixed target. Crucially the alternation is **allophonic** (positionally conditioned), not phonemic: Spanish has no `/e/` vs `/ɛ/` contrast, unlike Italian or French. No length variation, no reduction. In *bebé* `/beˈbe/` the pretonic `[be]` and stressed `[ˈbe]` are both full; the final *-e* of *leche* `/ˈletʃe/` keeps its full quality, not `[ə]`; *este* `/ˈeste/` shows `/e/` in a stressed syllable and a checked post-tonic syllable with quality unchanged.
- **`/i/` — close front unrounded `[i]`.** A consistently close, tense, front unrounded `[i]` in **all** positions — there is no lax counterpart `[ɪ]` and no shortening in unstressed syllables. When `/i/` is unstressed and adjacent to another vowel it becomes the glide `[j]` (rising diphthong, e.g. *bien* `[bjen]`) or `[i̯]` (falling diphthong, e.g. *peine* `[ˈpei̯ne]`); these glides are allophones of `/i/`, not separate phonemes. Between vowels it may be slightly devoiced `[i̥]` in fast speech next to voiceless consonants, but this is minor. In *vivir* `/biˈbiɾ/` both the pretonic `[bi]` and stressed `[ˈbiɾ]` are full close `[i]` (not laxed to English `[ɪ]`); *difícil* `/diˈfiθil/` (Cast.) ~ `/diˈfisil/` (LatAm) shows three identical `/i/` and also illustrates Castilian `/θ/` vs Latin American *seseo* `/s/`; the final *-i* of *casi* `/ˈkasi/` is full `[i]`, never reduced.
- **`/o/` — mid back rounded `[o̞]`.** The back rounded mirror image of `/e/`. Phonemically one mid back vowel; phonetically a **mid** `[o̞]` (lowered close-mid), between cardinal `[o]` and `[ɔ]`, **not** the very close French/German `[o]`. In the traditional description it **lowers** toward `[ɔ]` in the same conditions that open `/e/`: in closed syllables (*sol* `[sɔl]`), before `/r/`, before `/x/`, and in the diphthong `/oi̯/`; closer `[o]` in open syllables. As with `/e/`, instrumental work suggests this opening is **gradient and variable** rather than a categorical shift to `[ɔ]` — treat `[ɔ]` as a tendency toward greater openness, with the default staying near mid `[o̞]`. Either way it is **allophonic**, not phonemic — Spanish has no `/o/` vs `/ɔ/` contrast. No length variation, no reduction; unstressed `/o/` keeps its full rounded quality. In *cómodo* `/ˈkomodo/` `[ˈkomoðo]` the three `/o/` (stressed, post-tonic, final) are all full rounded `[o]`; *ocho* `/ˈotʃo/` keeps the final *-o* full; *amor* `/aˈmoɾ/` shows stressed `/o/` in a closed syllable before `/r/`, opening toward `[ɔ]`.
- **`/u/` — close back rounded `[u]`.** A consistently close, tense, back rounded `[u]` in all positions — no lax `[ʊ]` counterpart and no reduction in unstressed syllables. When `/u/` is unstressed and adjacent to another vowel it surfaces as the glide `[w]` (rising diphthong, e.g. *bueno* `[ˈbweno]`) or `[u̯]` (falling diphthong, e.g. *causa* `[ˈkau̯sa]`); these glides are allophones of `/u/`. The letter *u* is orthographically silent in *que/qui/gue/gui* (a spelling convention, not phonological deletion) and is pronounced when written *ü* (*pingüino* `[piŋˈɡwino]`). In *cuscús* `/kusˈkus/` both the pretonic `[kus]` and stressed `[ˈkus]` are full close `[u]` (not laxed to English `[ʊ]`); *música* `/ˈmusika/` has a full stressed `/u/`; the final *-u* of *espíritu* `/esˈpiɾitu/` is full `[u]`, never reduced.

### Stress Changes Prominence, Not Quality

In Spanish, stress changes the **prominence** of a vowel (greater duration, intensity and pitch) but **not** its quality. This is the categorical difference from English, where unstressed vowels reduce to schwa.

- **Lexical contrast.** Stress is phonemic/contrastive and can distinguish words: *término* `/ˈteɾmino/` ('term') vs *termino* `/teɾˈmino/` ('I finish') vs *terminó* `/teɾmiˈno/` ('he/she finished'). The vowels `/e i o/` are the **same** full qualities in all three; only the location of stress moves.
- **Orthography.** Lexical stress that is irregular relative to the default rules is marked with the acute accent (*á é í ó ú*). The accent therefore signals stress and, on *i/u*, signals hiatus (see below).
- **No reduction.** Because there is no reduction, learners coming from English must consciously avoid weakening unstressed vowels to `[ə]`: *comida* is `[koˈmiða]`, never `[kəˈmidə]`.

### Diphthongs and Hiatus

Spanish freely combines its five vowels into diphthongs and triphthongs. Whether two adjacent vowels form a **single** syllable (diphthong) or **two separate** syllables (hiatus) depends on which vowels are involved and on stress, and is signalled in the orthography by the acute accent. Only the high vowels `/i u/` can become glides `/j w/`.

#### Diphthong

A sequence of glide + vowel (rising) or vowel + glide (falling) sharing **one** syllable nucleus. The glide is a non-syllabic allophone of `/i/` (`[j]`/`[i̯]`) or `/u/` (`[w]`/`[u̯]`), so glide-bearing forms are given in `[brackets]`.

| Type | Word | IPA | Structure |
|---|---|---|---|
| Rising | *bien* | `[bjen]` | `/i/` → glide `[j]` + `/e/`, one syllable |
| Rising | *bueno* | `[ˈbweno]` | `/u/` → glide `[w]` + `/e/`, one syllable |
| Falling | *ley* 'law' | `[lei̯]` | `/e/` + `/i/` → glide `[i̯]`, one syllable; the classic *ley* diphthong |
| Falling | *causa* 'cause' | `[ˈkau̯sa]` | `/a/` + `/u/` → glide `[u̯]`, one syllable |

#### Hiatus

Two adjacent vowels belonging to **separate** syllables, each its own nucleus, with no glide. Hiatus occurs (a) between two non-high (strong) vowels `/a e o/`, e.g. *caer*, and (b) when a high vowel `/i u/` is **stressed** and adjacent to another vowel, in which case it stays a full syllabic vowel and the orthography marks it with an accent. The period `.` marks the syllable break.

| Word | IPA | Structure |
|---|---|---|
| *leí* 'I read (past)' | `/le.ˈi/` | `/e/` + stressed `/i/` → two syllables *le-í*; the written accent on *í* forces the hiatus |
| *día* 'day' | `/ˈdi.a/` | stressed `/i/` + `/a/` → hiatus *dí-a*; the accent breaks what would otherwise be a diphthong |
| *caer* 'to fall' | `/ka.ˈeɾ/` | `/a/` + `/e/` → hiatus *ca-er* (two non-high vowels never form a diphthong) |

#### Minimal contrast: diphthong vs hiatus

| Form | Word | IPA | Syllables |
|---|---|---|---|
| Diphthong | *ley* | `[lei̯]` | 1 |
| Hiatus | *leí* | `/le.ˈi/` | 2 |

The **only** phonological difference between *ley* `[lei̯]` (one syllable, falling diphthong) and *leí* `/le.ˈi/` (two syllables, hiatus) is whether `/i/` is a non-syllabic glide `[i̯]` or a stressed syllabic vowel `[i]`. The glide-bearing diphthong is shown in `[brackets]` and the syllabified hiatus with a syllable-break dot. This diphthong/hiatus distinction is exactly what the acute accent encodes.

#### Triphthongs

Spanish also has triphthongs (glide + vowel + glide), e.g. *buey* `[bwei̯]` 'ox', *estudiáis* `[estuˈðjai̯s]` 'you study (2nd pl.)'. These forms are given in `[brackets]` because they contain the phonetic glides `[w j i̯ u̯]` and, in *estudiáis*, the spirantized allophone `[ð]` of `/d/` — allophonic spirantization `[β ð ɣ]` is always written in brackets, never inside `/slashes/`. The purely phonemic forms would be `/buei̯/` and `/estuˈdjais/`.

### Allophonic Processes

The only systematic phonetic variation affecting Spanish vowels. **None of these create new phonemes.**

- **Mid-vowel opening.** `/e o/` are mid `[e̞ o̞]` by default and, in the traditional (Navarro Tomás) account, lower toward `[ɛ ɔ]` in closed syllables, before `/r/`, before `/x/`, and in certain diphthongs. Modern instrumental studies treat this opening as gradient and variable rather than categorical, so `[ɛ ɔ]` mark a tendency toward greater openness, not a fixed allophone. Allophonic in any case.
- **Nasalisation.** Vowels are slightly nasalised `[ã ẽ ĩ õ ũ]` when adjacent to a nasal consonant, especially between two nasals or before a tautosyllabic nasal (*mano*, *un*). Light and allophonic — Spanish has **no** phonemic nasal vowels (unlike French).
- **Devoicing.** In rapid or relaxed speech, unstressed vowels (especially word-finally, in Mexican Spanish and other highland varieties) may be partly devoiced or elided between voiceless consonants, e.g. *pesos* → `[ˈpe̥sos̥]`. Phonetic and variety-specific.
- **Glide formation.** Unstressed `/i u/` adjacent to another vowel become glides `[j w]` / `[i̯ u̯]`, forming diphthongs; this is the allophonic source of the glides `/j w/` used in this guide's diphthong transcriptions.

### Dialect Note

The five-vowel system is remarkably uniform across Spanish. Dialect variation is concentrated in the **consonants**, not the vowels.

- **Castilian vs Latin American.** Castilian (*distinción*) and Latin American (*seseo*) differ in the consonant inventory (`/θ/` present vs merged into `/s/`), but their vowels `/a e i o u/` are identical in number and quality. Likewise *yeísmo*, `/x/` realisation (`[x]`~`[χ]` vs `[h]`), coda `/s/`-aspiration, and Rioplatense *rehilamiento* are all **consonantal** features and do not alter the vowel inventory.
- **Eastern Andalusian exception.** One marginal exception: in parts of Eastern Andalusia, the deletion/aspiration of coda `/s/` leaves a quality difference (a more open vowel) on the preceding vowel, which some analyses treat as an incipient phonemic length/openness contrast (e.g. singular vs plural). This is local and not part of the standard reference accents documented here.
- **Summary.** For both reference accents in this guide, treat the vowels as a single shared 5-vowel system `/a e i o u/`.

### IPA Symbol Summary

Quick reference of the Spanish vowel phonemes and their main phonetic realisations. Identical for both reference accents (Castilian and Latin American).

| Phoneme | Principal allophones |
|---|---|
| `/a/` | `[ä]` (central; ~`[ɑ]` minor backing) |
| `/e/` | `[e̞]` by default; tends toward more open `[ɛ]` in closed syllables / before `/r x/` (gradient, not categorical) |
| `/i/` | `[i]`; `[j]`/`[i̯]` as glide in diphthongs |
| `/o/` | `[o̞]` by default; tends toward more open `[ɔ]` in closed syllables / before `/r x/` (gradient, not categorical) |
| `/u/` | `[u]`; `[w]`/`[u̯]` as glide in diphthongs |

**Glides:** `/j/`, `/w/` (non-syllabic allophones of `/i/` and `/u/`).

- **No length.** No length mark `/ː/` is used: Spanish vowels are not phonemically long. The English-guide distinction between checked/free and the use of `/ː/` has **no** Spanish equivalent.
- **No schwa.** There is **no** schwa `/ə/` in Spanish and no weak-vowel set: unstressed vowels are full `/a e i o u/`.

## Diphthongs & Triphthongs

Unlike English, whose diphthongs are organized by Wells lexical sets, Spanish diphthongs are sequences of a vowel and a high glide (`/j/` or `/w/`) that share a single syllable. Spanish is RICH in diphthongs (and even triphthongs), in sharp contrast to French. A Spanish diphthong (*diptongo*) is any tautosyllabic combination of one of the five full vowels `/a e i o u/` with a glide derived from an unstressed high vowel: the palatal glide `/j/` (from `/i/`) or the labio-velar glide `/w/` (from `/u/`). Two structural types exist: RISING diphthongs (*diptongos crecientes*), glide + vowel, where the glide precedes the syllable nucleus and the sonority rises (`/ja je jo ju/`, `/wa we wi wo/`); and FALLING diphthongs (*diptongos decrecientes*), vowel + glide, where the nucleus precedes the glide and the sonority falls (`/ai ei oi au eu ou/`). Because Spanish has NO phonemic vowel length and NO vowel reduction, both elements keep full, clear quality; the glide is shorter and non-syllabic but is not a separate consonant phoneme.

Spanish vowels are stable across both reference accents, so the diphthong and triphthong inventory is essentially IDENTICAL in Castilian (Peninsular, *distinción*) and Latin American (general, *seseo*) Spanish; the parallel IPA fields below are given for schema consistency and differ only in rare lexical or allophonic detail, not in the vowel system itself. The orthographic acute accent on a high vowel BREAKS a would-be diphthong into a two-syllable HIATUS (e.g. *día* `/ˈdi.a/` vs *hacia* `/ˈa.θja/`~`/ˈa.sja/`).

### Rising Diphthongs

Glide + vowel (*diptongos crecientes*): the glide onsets the syllable and the sonority rises into the vowel nucleus. Built on the palatal glide `[j]` (from `/i/`) and the labio-velar glide `[w]` (from `/u/`).

| Diphthong | Castilian | Latin American | Example Words | Notes |
|---|---|---|---|---|
| `/ja/` | `/ja/` | `/ja/` | *hacia* `/ˈa.θja/` (Cast.), `/ˈa.sja/` (LatAm); *piano* `/ˈpja.no/`; *estudiar* `[es.tuˈðjaɾ]` | Spelled ⟨ia⟩. The glide `[j]` is the non-syllabic counterpart of `/i/`. Identical in both reference accents; only the `[θ]`~`[s]` of a neighbouring consonant (as in *hacia*) reflects *distinción* vs *seseo*, not the diphthong itself. Word-initially or after a pause the glide may strengthen toward the approximant/fricative `[ʝ]`~`[j]` (e.g. *hierba* `[ˈʝeɾβa]`~`[ˈjeɾβa]`), where the orthography uses ⟨hi-⟩. An acute accent on the ⟨i⟩ dissolves the diphthong into hiatus: compare *hacia* `/ˈa.θja/` with accented forms such as *comía* `/koˈmi.a/`. |
| `/je/` | `/je/` | `/je/` | *tierra* `/ˈtje.ra/`; *bien* `/bjen/`; *siempre* `/ˈsjem.pɾe/` | Spelled ⟨ie⟩. Extremely frequent because the diphthong `/je/` is the regular outcome of stressed Latin short `/e/` (*tierra* < TERRA, *bien* < BENE), one of the defining diphthongizations of Spanish. Word-initial ⟨hie-⟩ (*hielo*, *hierba*) is realized with a strengthened onset `[ˈʝe-]`~`[ˈje-]`. Stable across Castilian and Latin American Spanish. |
| `/jo/` | `/jo/` | `/jo/` | *radio* `[ˈra.ðjo]`; *patio* `/ˈpa.tjo/`; *dios* `/djos/` | Spelled ⟨io⟩. Very common word-finally in masculine nouns and in the present-tense first person (*estudio*, *cambio*). The intervocalic `/d/` in *radio* spirantizes to `[ð]` in both accents. Word-initial ⟨hio-⟩ is rare. An accent breaks the diphthong: *río* `/ˈri.o/` (hiatus) vs the diphthongal pattern of *radio*. |
| `/ju/` | `/ju/` | `/ju/` | *viuda* `[ˈbju.ða]`; *ciudad* `[θjuˈðað]` (Cast.), `[sjuˈðað]` (LatAm); *triunfo* `/ˈtɾjun.fo/` | Spelled ⟨iu⟩; the rarest of the `/j/`-initial rising diphthongs. When two high vowels meet (⟨iu⟩, ⟨ui⟩), the FIRST is normally the glide and the second the nucleus, so ⟨iu⟩ = `/ju/` (*viuda*) and ⟨ui⟩ = `/wi/` (*cuidar*); this is the standard Spanish resolution of high-high sequences. Identical in both accents; the `[θ]`~`[s]` in *ciudad* reflects *distinción* vs *seseo*, not the diphthong. ⟨iu⟩/⟨ui⟩ stay diphthongal as long as NEITHER high vowel carries a written accent; an accent on the second high vowel breaks the sequence into hiatus (*huida* `/uˈi.da/` `[uˈi.ða]`). In *ciudad* `[θjuˈðað]` the ⟨iu⟩ diphthong is itself unstressed: the stress falls on the final syllable *-dad*, not on either high vowel. |
| `/wa/` | `/wa/` | `/wa/` | *agua* `[ˈa.ɣwa]`; *cuatro* `/ˈkwa.tɾo/`; *guante* `/ˈɡwan.te/` | Spelled ⟨ua⟩ and, after ⟨g⟩/⟨c⟩, ⟨gua⟩/⟨cua⟩. The glide `[w]` is the non-syllabic counterpart of `/u/`. Note that the ⟨u⟩ is pronounced (and forms the glide) after ⟨g⟩ and ⟨c⟩ but is SILENT in ⟨gue⟩/⟨gui⟩ (*guerra* `/ˈɡe.ra/`, *guitarra* `/ɡiˈta.ra/`) unless written with diaeresis ⟨güe⟩/⟨güi⟩ (*pingüino* `/pinˈɡwi.no/`). In *agua* the intervocalic `/ɡ/` spirantizes to `[ɣ]` in both accents. Stable across Castilian and Latin American Spanish. |
| `/we/` | `/we/` | `/we/` | *bueno* `/ˈbwe.no/`; *fuego* `[ˈfwe.ɣo]`; *puerta* `/ˈpweɾ.ta/` | Spelled ⟨ue⟩ (and ⟨güe⟩ after the velars). Like `/je/`, the diphthong `/we/` is the regular reflex of stressed Latin short `/o/` (*bueno* < BONUS, *puerta* < PORTA, *fuego* < FOCUS), a hallmark Spanish diphthongization that alternates with non-diphthongized `/o/` in unstressed related forms (*bueno* ~ *bondad*, *puerta* ~ *portero*). Word-initially the glide may be reinforced: *hueso* `[ˈweso]`~`[ˈɣweso]`. Stable across both reference accents. |
| `/wi/` | `/wi/` | `/wi/` | *fui* `/fwi/`; *cuidar* `[kwiˈðaɾ]`; *ruido* `[ˈrwi.ðo]` | Spelled ⟨ui⟩ (and ⟨güi⟩ after the velars). In the ⟨ui⟩ spelling the ⟨u⟩ is the glide and the ⟨i⟩ the nucleus (*cuidar* `[kwiˈðaɾ]`, not \*`[kuiˈðaɾ]`). Monosyllables like *fui* and the preterite forms are not written with an accent under current orthography. By contrast, when the second high vowel is stressed and written with an accent the sequence becomes hiatus: *huida* `/uˈi.da/` `[uˈi.ða]`. Stable across both accents. |
| `/wo/` | `/wo/` | `/wo/` | *cuota* `/ˈkwo.ta/`; *antiguo* `[anˈti.ɣwo]`; *arduo* `[ˈaɾ.ðwo]` | Spelled ⟨uo⟩; the rarest of the `/w/`-initial rising diphthongs. The least common rising diphthong; it occurs chiefly in learned/Latinate words (*cuota*, *individuo*, *arduo*, *antiguo*). The two non-low rounded-ish elements `[w]` and `[o]` remain distinct, `[w]` gliding into a fully back `[o]` with no reduction. Stable across Castilian and Latin American Spanish. |

### Falling Diphthongs

Vowel + glide (*diptongos decrecientes*): the full vowel nucleus precedes the glide and the sonority falls into a non-syllabic offglide `[i̯]` or `[u̯]`. Some traditions transcribe these offglides as `[ai̯ ei̯ ...]` with the inverted breve; others simply as `/ai/`.

| Diphthong | Castilian | Latin American | Example Words | Notes |
|---|---|---|---|---|
| `/ai/` | `/ai/` | `/ai/` | *aire* `/ˈai.ɾe/`; *baile* `/ˈbai.le/`; *hay* `/ai/` | Falling diphthong: open central vowel `[a]` nucleus gliding up to the palatal offglide `[i̯]`; transcribed `/ai/` (often `[ai̯]`). Spelled ⟨ai⟩ within a word and ⟨ay⟩ word-finally (*hay*, *caray*). The offglide is the non-syllabic `[i̯]`, the falling counterpart of `/j/`. An acute accent dissolves it into hiatus: *caída* `/kaˈi.da/` `[kaˈi.ða]`. Stable across both reference accents. |
| `/ei/` | `/ei/` | `/ei/` | *ley* `/lei/`; *reina* `/ˈrei.na/`; *peine* `/ˈpei.ne/` | Falling diphthong: close-mid front vowel `[e]` nucleus gliding up to the palatal offglide `[i̯]`; transcribed `/ei/` (often `[ei̯]`). Spelled ⟨ei⟩ word-internally and ⟨ey⟩ word-finally (*ley*, *rey*, *buey*-type endings). Distinct from the rising `/je/`: *reina* `/ˈrei.na/` (falling, nucleus `[e]`) vs the rising onset of words like *hierro*. The accented variant is hiatus: *reír* `/reˈiɾ/`. Stable across Castilian and Latin American Spanish. |
| `/oi/` | `/oi/` | `/oi/` | *hoy* `/oi/`; *boina* `/ˈboi.na/`; *estoico* `/esˈtoi.ko/` | Falling diphthong: close-mid back rounded vowel `[o]` nucleus gliding up to the palatal offglide `[i̯]`; transcribed `/oi/` (often `[oi̯]`). Spelled ⟨oi⟩ word-internally and ⟨oy⟩ word-finally (*hoy*, *soy*, *voy*, *estoy*). The nucleus is a fully rounded back `[o]` (no reduction) with a short `[i̯]` offglide. Accented ⟨oí⟩ is hiatus: *oír* `/oˈiɾ/`. Stable across both reference accents. |
| `/au/` | `/au/` | `/au/` | *causa* `/ˈkau.sa/`; *auto* `/ˈau.to/`; *jaula* `/ˈxau.la/` | Falling diphthong: open central vowel `[a]` nucleus gliding up and back to the labio-velar offglide `[u̯]`; transcribed `/au/` (often `[au̯]`). Spelled ⟨au⟩. The offglide `[u̯]` is the non-syllabic, falling counterpart of `/w/`. In *jaula* the ⟨j⟩ is `/x/`, realized `[x]`~`[χ]` in Castilian and commonly `[h]` in Caribbean and much Latin American Spanish, but the diphthong `/au/` is unaffected. Accented ⟨aú⟩ is hiatus: *baúl* `/baˈul/`. Stable across both reference accents. |
| `/eu/` | `/eu/` | `/eu/` | *deuda* `[ˈdeu.ða]`; *Europa* `/euˈɾo.pa/`; *neutro* `/ˈneu.tɾo/` | Falling diphthong: close-mid front vowel `[e]` nucleus gliding up and back to the labio-velar offglide `[u̯]`; transcribed `/eu/` (often `[eu̯]`). Spelled ⟨eu⟩. Less frequent than `/au/`, occurring in *deuda*, *Europa*, *neutro*, *reuma*, *seudónimo*. In *deuda* the intervocalic `/d/` of the cluster surfaces with the second `/d/` spirantized to `[ð]`. Accented ⟨eú⟩ gives hiatus: *reúne* `/reˈu.ne/`. Stable across Castilian and Latin American Spanish. |
| `/ou/` | `/ou/` | `/ou/` | *bou* `/bou/`; *Souto* `/ˈsou.to/`; *estadounidense* `[es.ta.ðou.niˈðen.se]` | Falling diphthong: close-mid back rounded vowel `[o]` nucleus gliding to the labio-velar offglide `[u̯]`; the rarest native falling diphthong. Spelled ⟨ou⟩. By far the rarest falling diphthong in native Spanish vocabulary; it survives mostly in Galician/Catalan-origin words and proper names (*bou*, *Souto*, *Bousoño*) and at certain morpheme boundaries (*estadounidense*, from *estado* + *unidense*). The two back rounded elements `[o]` and `[u̯]` are kept distinct. Stable across both reference accents. |

### Triphthongs

A *triptongo* is a glide + vowel + glide cluster sharing one syllable, with the single full vowel as nucleus flanked by two glides. They cluster around the second-person plural (*vosotros*) verb inflections and proper names. The written accent marks the stressed nucleus.

| Triphthong | Castilian | Latin American | Example Words | Notes |
|---|---|---|---|---|
| `/jai/` | `/jai/` | `/jai/` | *limpiáis* `/limˈpjais/`; *estudiáis* `[es.tuˈðjais]`; *averiguáis* `[a.βe.ɾiˈɣwais]` | Glide + vowel + glide: palatal onglide `[j]` + open nucleus `[a]` + palatal offglide `[i̯]` in a single syllable. Spelled ⟨iái⟩ / ⟨iáis⟩. `/jai/` appears chiefly in the second-person plural (*vosotros*) present of *-iar* verbs (*limpiáis*, *cambiáis*), an inflection used in Peninsular Spanish; Latin American Spanish, which uses *ustedes*, encounters these forms less in speech but the phonotactics are identical. The written accent marks the stressed nucleus `[a]`. |
| `/jei/` | `/jei/` | `/jei/` | *limpiéis* `/limˈpjeis/`; *estudiéis* `[es.tuˈðjeis]`; *cambiéis* `/kamˈbjeis/` | Palatal onglide `[j]` + close-mid front nucleus `[e]` + palatal offglide `[i̯]`. Spelled ⟨iéi⟩ / ⟨iéis⟩. Found mainly in the second-person plural (*vosotros*) present subjunctive of *-iar* verbs (*limpiéis*, *cambiéis*, *estudiéis*). Same dialectal note as `/jai/`: a Peninsular *vosotros* inflection, phonotactically valid everywhere. The accent on ⟨é⟩ marks the stressed nucleus. |
| `/wai/` | `/wai/` | `/wai/` | *Paraguay* `[pa.ɾaˈɣwai]`; *Uruguay* `[u.ɾuˈɣwai]`; *averiguáis* `[a.βe.ɾiˈɣwais]` | Labio-velar onglide `[w]` + open nucleus `[a]` + palatal offglide `[i̯]`. Spelled ⟨uay⟩/⟨uái⟩. Famous in the country names *Paraguay* and *Uruguay* (with `[ɣw]` after the spirantized `/ɡ/`), and in *vosotros* forms of *-guar* verbs (*averiguáis*). The cluster is one syllable: `[ˈɣwai]`. Stable across Castilian and Latin American Spanish (the `[ɣ]` is the regular intervocalic spirantization of `/ɡ/` in both). |
| `/wei/` | `/wei/` | `/wei/` | *buey* `/bwei/`; *Camagüey* `[ka.maˈɣwei]`; *averigüéis* `[a.βe.ɾiˈɣweis]` | Labio-velar onglide `[w]` + close-mid front nucleus `[e]` + palatal offglide `[i̯]`. Spelled ⟨uey⟩/⟨üey⟩/⟨üéi⟩. The classic example is *buey* ('ox'), a one-syllable word `/bwei/`. Also in the Cuban place name *Camagüey* and in *vosotros* subjunctive forms of *-guar* verbs (*averigüéis*), where the diaeresis ⟨ü⟩ signals that the ⟨u⟩ is pronounced as the glide `[w]` before the front vowel. Stable across both reference accents. |

### The Glides /j/ and /w/

Spanish has two glides (semivowels/semiconsonants), the palatal `/j/` and the labio-velar `/w/`. They are the non-syllabic counterparts of the high vowels `/i/` and `/u/` and occur ONLY within diphthongs and triphthongs; they are NOT independent consonant phonemes. In RISING diphthongs the glide precedes the nucleus and is often called a semiconsonant (`[j]` in *tierra* `[ˈtjera]`, `[w]` in *bueno* `[ˈbweno]`); in FALLING diphthongs the glide follows the nucleus and is often called a semivowel (`[i̯]` in *aire* `[ˈai̯ɾe]`, `[u̯]` in *causa* `[ˈkau̯sa]`).

When a high vowel is in absolute initial position or after a pause, especially the spelled ⟨hi-⟩/⟨y⟩, the palatal glide can strengthen toward the approximant or fricative `[ʝ]`~`[j]` (*hierba*, *hielo*), where it borders on the consonant phoneme `/ʝ/`. The phoneme `/ʝ/` itself (*yeísmo*) is the merged reflex of historical ⟨y⟩ and ⟨ll⟩; *lleísta* varieties of conservative Andean and Paraguayan Spanish keep `/ʎ/` distinct, but this concerns the consonant system, not the diphthong glides.

### Hiatus (*Hiato*)

A HIATO (hiatus) is a sequence of two adjacent vowels that belong to DIFFERENT syllables and therefore do NOT form a diphthong. Spanish hiatus arises in two main ways:

1. **Two non-high (strong) vowels in sequence** are always heterosyllabic: *caos* `/ˈka.os/`, *teatro* `/teˈa.tɾo/`, *león* `/leˈon/`, *poeta* `/poˈe.ta/`.
2. **A high vowel that bears the STRESS** next to another vowel is a full syllabic nucleus, not a glide, creating hiatus: *día* `/ˈdi.a/` (not \*`/dja/`), *país* `/paˈis/` (not \*`/pais/`), and likewise *maíz* `/maˈiθ/` (Cast.) ~ `/maˈis/` (LatAm), *baúl* `/baˈul/`, *río* `/ˈri.o/`, *búho* `/ˈbu.o/`, *continúo* `/kon.tiˈnu.o/`.

Hiatus is identical in Castilian and Latin American Spanish. In rapid or casual speech a hiatus of two non-high or of unstressed high + vowel sequences may be reduced toward a diphthong (*sinéresis*), e.g. *teatro* `[ˈtja.tɾo]`, but the careful/standard form keeps the two syllables.

**Orthographic accent and hiatus.** Spanish orthography uses the acute accent precisely to mark this distinction. By the rules, a combination of a STRONG vowel `/a e o/` and an UNSTRESSED WEAK vowel `/i u/` (or two weak vowels) is a DIPHTHONG and counts as a single syllable for stress purposes; but when the WEAK vowel `/i/` or `/u/` is itself stressed, a written accent is placed on it to signal that the diphthong is BROKEN into hiatus. Thus the accent does double duty: it both marks stress and forces the high vowel to be a separate syllabic nucleus. Compare:

- *hacia* `/ˈa.θja/`~`/ˈa.sja/` (diphthong, two letters one syllable) with *hacía* `/aˈθi.a/`~`/aˈsi.a/` (hiatus, accented ⟨í⟩);
- *continuo* `/konˈti.nwo/` (diphthong) with *continúo* `/kon.tiˈnu.o/` (hiatus) with *continuó* `/kon.tiˈnwo/` (diphthong, stress on the final nucleus);
- *seria* `/ˈse.ɾja/` (diphthong) with *sería* `/seˈɾi.a/` (hiatus).

This accent-driven breaking of diphthongs is a regular, productive feature of written Spanish and applies identically in both reference accents. Because Spanish stress is lexical and contrastive, the orthographic accent is the written signal of both the stressed syllable and this diphthong/hiatus split.

### Dialect Note

The Spanish vowel system, and therefore the diphthong and triphthong inventory, is remarkably uniform: there is NO vowel length and NO unstressed-vowel reduction in any major variety, so all diphthongs keep both elements at full quality across Castilian (*distinción*) and Latin American (*seseo*) Spanish. The reference-accent labels matter for surrounding consonants, not for the diphthongs themselves: e.g. the ⟨c⟩/⟨z⟩ in *hacia* and *ciudad* is `[θ]` in Castilian but `[s]` under *seseo*; the ⟨j⟩/⟨g⟩ in *jaula*/*gente* is `[x]`~`[χ]` in Castilian but often `[h]` in Caribbean and much of Latin America; word-initial strengthened glides interact with *yeísmo* (`/ʝ/`) vs conservative *lleísmo* (`/ʎ/`). Rioplatense *rehilamiento* turns `/ʝ/` into `[ʒ]`~`[ʃ]` (*yo* `[ʃo]`), which can affect a strengthened palatal onglide word-initially but not the offglides of falling diphthongs. None of these consonantal differences alters the vowel-plus-glide structure of the diphthongs catalogued above.

*Spanish, in marked contrast to French, is RICH in diphthongs and even has triphthongs. Diphthongs are tautosyllabic vowel + glide sequences built from the five stable vowels `/a e i o u/` plus the glides `/j/` (from `/i/`) and `/w/` (from `/u/`), with NO length and NO reduction. RISING diphthongs (glide + vowel: `/ja je jo ju/`, `/wa we wi wo/`) include the historically pivotal `/je/` < Latin short `/e/` (*tierra*) and `/we/` < Latin short `/o/` (*bueno*). FALLING diphthongs (vowel + glide: `/ai ei oi au eu ou/`) end in `[i̯]` or `[u̯]`, with `/ou/` the rarest. TRIPHTHONGS (`/jai jei wai wei/`, as in *limpiáis*, *limpiéis*, *Paraguay*, *buey*) pack a glide-vowel-glide into one syllable and cluster around* vosotros *verb inflections and proper names. Crucially, the orthographic acute accent on a high vowel BREAKS a diphthong into a two-syllable HIATUS (*hacia* `/ˈa.θja/` vs *hacía* `/aˈθi.a/`; *país* `/paˈis/`; *día* `/ˈdi.a/`), so the accent simultaneously marks stress and signals syllabic separation. Because Spanish vowels do not vary between the reference accents, the diphthong inventory is essentially identical in Castilian (*distinción*) and Latin American (*seseo*) Spanish; the accents differ only in neighbouring consonants (`/θ/`~`/s/`, `/x/`~`[h]`, *yeísmo*/*lleísmo*, Rioplatense *rehilamiento*), never in the vowel-plus-glide structure.*

## Consonant–Vowel IPA Matrix

Systematic consonant + vowel (CV) IPA combination matrix pairing each Spanish consonant phoneme with the full five-vowel set `/a e i o u/`. Each cell gives the phonemic IPA string for the consonant followed by the reference vowel. The general (seseo-yeísta) inventory has 17 consonant phonemes `/p b t d k ɡ tʃ f s x ʝ m n ɲ l r ɾ/` (17 × 5 = 85 combinations); full distinguishing Castilian adds `/θ/`, and conservative lleísta varieties add `/ʎ/`, giving up to 19 consonants. Combinations are phonemic transcriptions; consult each consonant's phonetic note for the principal allophonic realizations — especially the spirantization of `/b d ɡ/` to `[β ð ɣ]`, nasal place assimilation, and the trill `/r/` ~ tap `/ɾ/` contrast — that surface in actual CV syllables. Spanish vowels are never reduced, so each vowel keeps identical quality stressed or unstressed.

- **Reference accent:** Latin American (general seseo-yeísta)
- **Secondary reference accent:** Castilian (Peninsular / European Standard Castilian, with distinción and optional lleísmo)
- **Transcription level:** phonemic

### Reference Vowels

The five reference vowels used as columns in the matrix. Spanish has a clean, stable five-vowel system with NO phonemic length and NO unstressed reduction — every vowel keeps full quality regardless of stress, so there is no schwa.

| Vowel | Name | Example | Note |
|---|---|---|---|
| a | open (low) central unrounded vowel | casa `/ˈkasa/` ('house') | Stable [a]; central-to-front. Identical whether stressed or unstressed — Spanish has NO vowel reduction, so unstressed /a/ never becomes schwa. |
| e | mid (close-mid to open-mid) front unrounded vowel | mesa `/ˈmesa/` ('table') | Realized [e] in open syllables, lowering toward [ɛ] in closed syllables and before /r/ (a sub-phonemic detail, not contrastive). No reduction when unstressed. |
| i | close front unrounded vowel | vino `/ˈbino/` ('wine') | Stable [i]; its non-syllabic counterpart is the glide [j] in diphthongs (e.g. tiene [ˈtjene]). No length contrast. |
| o | mid (close-mid to open-mid) back rounded vowel | todo `/ˈtodo/` ('all') | Realized [o] in open syllables, lowering toward [ɔ] in closed syllables and before /r/ (sub-phonemic). No reduction when unstressed. |
| u | close back rounded vowel | luna `/ˈluna/` ('moon') | Stable [u]; its non-syllabic counterpart is the glide [w] in diphthongs (e.g. bueno [ˈbweno]). Silent in the digraphs ⟨que qui gue gui⟩ unless written ⟨ü⟩. |

### CV Matrix

Each cell gives the phonemic consonant + vowel sequence. Columns are the five reference vowels; the **Base IPA** column gives the consonant phoneme on its own. The `/θ/` row is **Castilian only** (under seseo it merges into the `/s/` row); the `/ʎ/` row applies to **lleísta varieties only** (under the near-universal yeísmo it merges into the `/ʝ/` row).

| Consonant | Name | Example | Base IPA | a | e | i | o | u |
|---|---|---|---|---|---|---|---|---|
| p | voiceless bilabial plosive | pan `/pan/` ('bread') | p | pa | pe | pi | po | pu |
| b | voiced bilabial plosive (~ approximant [β]) | vaca `/ˈbaka/` ('cow') | b | ba | be | bi | bo | bu |
| t | voiceless dental plosive | té `/te/` ('tea') | t | ta | te | ti | to | tu |
| d | voiced dental plosive (~ approximant [ð]) | dar `/dar/` ('to give') | d | da | de | di | do | du |
| k | voiceless velar plosive | casa `/ˈkasa/` ('house') | k | ka | ke | ki | ko | ku |
| ɡ | voiced velar plosive (~ approximant [ɣ]) | gato `/ˈɡato/` ('cat') | ɡ | ɡa | ɡe | ɡi | ɡo | ɡu |
| tʃ | voiceless postalveolar affricate | chico `/ˈtʃiko/` ('boy') | tʃ | tʃa | tʃe | tʃi | tʃo | tʃu |
| f | voiceless labiodental fricative | foca `/ˈfoka/` ('seal') | f | fa | fe | fi | fo | fu |
| θ | voiceless dental fricative (Castilian only) | caza `/ˈkaθa/` ('hunt'), zapato `/θaˈpato/` ('shoe') | θ | θa | θe | θi | θo | θu |
| s | voiceless alveolar fricative | casa `/ˈkasa/` ('house') | s | sa | se | si | so | su |
| x | voiceless velar fricative | jamón `/xaˈmon/` ('ham'), gente `/ˈxente/` ('people') | x | xa | xe | xi | xo | xu |
| ʝ | voiced palatal fricative/approximant (yeísta) | yo `/ʝo/` ('I'), llave `/ˈʝabe/` [ˈʝaβe] ('key') | ʝ | ʝa | ʝe | ʝi | ʝo | ʝu |
| ʎ | voiced palatal lateral approximant (lleísta only) | llave `/ˈʎabe/` [ˈʎaβe] ('key'), calle `/ˈkaʎe/` ('street') | ʎ | ʎa | ʎe | ʎi | ʎo | ʎu |
| m | voiced bilabial nasal | mano `/ˈmano/` ('hand') | m | ma | me | mi | mo | mu |
| n | voiced alveolar nasal | no `/no/` ('no') | n | na | ne | ni | no | nu |
| ɲ | voiced palatal nasal | año `/ˈaɲo/` ('year'), niño `/ˈniɲo/` ('child'), España `/esˈpaɲa/` ('Spain') | ɲ | ɲa | ɲe | ɲi | ɲo | ɲu |
| l | voiced alveolar lateral approximant | luna `/ˈluna/` ('moon') | l | la | le | li | lo | lu |
| r | voiced alveolar trill | perro `/ˈpero/` ('dog'), rosa `/ˈrosa/` ('rose') | r | ra | re | ri | ro | ru |
| ɾ | voiced alveolar tap/flap | pero `/ˈpeɾo/` ('but'), cara `/ˈkaɾa/` ('face') | ɾ | ɾa | ɾe | ɾi | ɾo | ɾu |

### Phonetic Notes

Principal allophonic realizations for each consonant onset. These describe how the phonemic CV cells above surface in actual speech.

| Consonant | Phonetic Note |
|---|---|
| p | Unaspirated [p] in all positions — a key contrast with English, which aspirates [pʰ] before stressed vowels; identical realization in Castilian and Latin American Spanish. |
| b | Phonemic /b/, written ⟨b⟩ or ⟨v⟩ (no /v/ phoneme in Spanish; seseo varieties and Castilian alike). Plosive [b] occurs utterance-initially and after a nasal; elsewhere it spirantizes to the approximant [β] (e.g. la vaca [la ˈβaka]). |
| t | Laminal DENTAL [t̪], not the English alveolar [t]; unaspirated. Same in both standards. Never flapped/tapped between vowels (contrast English [ɾ]). |
| d | Laminal dental [d̪] utterance-initially, after a nasal, and after /l/; elsewhere spirantizes to the approximant [ð] (e.g. nada [ˈnaða]). Word-final /d/ is weakened to [ð̞] or elided, and realized as [θ] in much of Castilian (Madrid usted [usˈteθ]). |
| k | Unaspirated [k]; written ⟨c⟩ before /a o u/ and ⟨qu⟩ before /e i/ (and ⟨k⟩ in loans). Fronts toward palatal before front vowels. Identical in both standards. |
| ɡ | Plosive [ɡ] utterance-initially and after a nasal; elsewhere spirantizes to the approximant [ɣ] (e.g. lago [ˈlaɣo]). Written ⟨g⟩ before /a o u/ and ⟨gu⟩ before /e i/; ⟨gü⟩ marks the sequence /ɡw/ before /e i/ (e.g. pingüino). |
| tʃ | Single affricate phoneme, written ⟨ch⟩. General realization [tʃ]; deaffricated to a fricative [ʃ] in Andalusian, Chilean, and northern-Mexican varieties (e.g. muchacho [muˈʃaʃo]). |
| f | Stable labiodental [f] across vowel contexts in both standards; some rural/Caribbean speech realizes it as bilabial [ɸ] or, before /w/, as [x]/[h] (e.g. fuego). |
| θ | CASTILIAN ONLY (distinción): the phoneme spelled ⟨z⟩ (all vowels) and ⟨c⟩ before /e i/. Contrasts with /s/ — caza /ˈkaθa/ vs casa /ˈkasa/. In LATIN AMERICAN Spanish (and Andalusian) this phoneme does NOT exist: seseo merges it into /s/, so caza = casa = /ˈkasa/. The combinations above are Castilian; under seseo these merge into the /s/ row. |
| s | In seseo (Latin American, Andalusian) /s/ also covers ⟨z⟩ and ⟨c⟩-before-/e i/. Castilian /s/ is typically apico-alveolar [s̺]; most Latin American /s/ is laminal/dental [s̻]. Voiced to [z] before voiced consonants (mismo [ˈmizmo]). Coda /s/ aspirates to [h] or elides in the Caribbean, much of coastal Latin America, and Andalusia (estos [ˈehto(h)]). |
| x | Written ⟨j⟩ (all vowels) and ⟨g⟩ before /e i/. Realized as velar [x] or post-velar/uvular [χ] in Castilian (strongly back), but as a soft glottal [h] in the Caribbean, much of Latin America, and Andalusia (e.g. jamón [haˈmon]). |
| ʝ | The merged YEÍSTA phoneme, written ⟨y⟩ and (under yeísmo) ⟨ll⟩. Near-universal in modern Spanish; ranges from approximant [ʝ̞]/[j] to fricative [ʝ]. In Rioplatense (Buenos Aires/Montevideo) it undergoes rehilamiento to [ʒ] or devoiced [ʃ] (e.g. yo [ʃo], calle [ˈkaʃe]). Lleísta varieties keep this distinct from /ʎ/ — see /ʎ/ row. |
| ʎ | LLEÍSTA VARIETIES ONLY (conservative Andean — highland Bolivia, Peru, Paraguay; parts of Castile). Written ⟨ll⟩ and kept distinct from /ʝ/ (e.g. pollo /ˈpoʎo/ 'chicken' vs poyo /ˈpoʝo/ 'stone bench'). Under YEÍSMO (the majority everywhere else) /ʎ/ has merged into /ʝ/, so ⟨ll⟩ = ⟨y⟩. |
| m | Stable [m] in onset. In the coda, place is neutralized: nasals assimilate to a following consonant ([ɱ] before /f/, [n̪] before dentals, [ŋ] before velars), and syllable/word-final /n/ velarizes to [ŋ] in the Caribbean and much of Latin America (pan [paŋ]). |
| n | Alveolar [n] in onset; assimilates in place to a following consonant ([m ɱ n̪ ɲ ŋ]). Word-final /n/ is velarized to [ŋ] (often with vowel nasalization) in Caribbean, Central American, and Andalusian speech. |
| ɲ | Distinct phoneme written ⟨ñ⟩; contrasts with the sequence /nj/ (e.g. huraño /uˈɾaɲo/ 'sullen' vs uranio /uˈɾanjo/ 'uranium'). Stable palatal [ɲ] in both standards. |
| l | Always a CLEAR (non-velarized) [l] in all positions — Spanish has no dark/velarized [ɫ], a notable contrast with English coda /l/. Dentalized [l̪] before dental /t d/. Caribbean/Andalusian speech may merge coda /l/ with /ɾ/ (lateralization/rhotacism). |
| r | TRILL /r/ — multiple-contact [r]. Phonemically contrasts with the tap /ɾ/ ONLY between vowels (perro /ˈpero/ 'dog' vs pero /ˈpeɾo/ 'but'). The trill is the obligatory realization word-initially, after /l n s/, and for written ⟨rr⟩. Assibilated [r̝]/[ʐ] in Andean and some other varieties. |
| ɾ | TAP /ɾ/ — single-contact [ɾ]; the intervocalic and onset-cluster (e.g. tres, gris) realization of written single ⟨r⟩. Contrasts with the trill /r/ intervocalically (pero vs perro). Syllable-final ⟨r⟩ is typically a tap [ɾ] but variably trilled, assibilated, or (Caribbean/Andalusian) elided or merged with /l/. |

### Accent Notes

**Castilian vs. Latin American.** This matrix uses the LATIN AMERICAN (general seseo-yeísta) reference accent. The two principal standards differ mainly in three features. (1) DISTINCIÓN vs SESEO: Castilian distinguishes `/θ/` (⟨z⟩, ⟨c⟩+e/i) from `/s/` — caza `/ˈkaθa/` vs casa `/ˈkasa/` — whereas Latin American (and Andalusian) seseo merges both into `/s/`, so caza = casa = `/ˈkasa/`. The `/θ/` row is therefore Castilian-only. (2) YEÍSMO vs LLEÍSMO: near-universally `/ʎ/` (⟨ll⟩) has merged into `/ʝ/` (⟨y⟩); conservative Andean and Paraguayan varieties retain the `/ʎ/` ~ `/ʝ/` contrast (lleísmo) — the `/ʎ/` row applies to those only. (3) `/x/` backing: ⟨j⟩/⟨g⟩+e/i is a strongly back `[x]`~`[χ]` in Castilian but a soft glottal `[h]` across the Caribbean and much of Latin America.

**Seseo.** Under seseo (Latin American + Andalusian + Canarian standard) the Castilian `/θ/` ~ `/s/` contrast is neutralized to `/s/`. Consequently the general-American inventory has ~17 consonant phonemes; full distinguishing Castilian has ~19 (adding `/θ/` and, in lleísta speech, `/ʎ/`).

**Spirantization.** The hallmark allophonic process: voiced stops `/b d ɡ/` are realized as plosives `[b d ɡ]` only utterance-initially and after a homorganic nasal (and `/d/` also after `/l/`); in ALL other positions — crucially between vowels — they soften to the approximants `[β ð ɣ]`. The CV cells above are phonemic (`/b/`, `/d/`, `/ɡ/`); in running speech these consonants surface as `[β ð ɣ]` in most intervocalic CV contexts.

**Trill vs. tap.** The single phonemic rhotic contrast in Spanish: alveolar TRILL `/r/` vs alveolar TAP `/ɾ/`, distinctive only intervocalically (perro `/ˈpero/` 'dog' vs pero `/ˈpeɾo/` 'but'). Word-initially, after `/l n s/`, and in ⟨rr⟩ only the trill occurs; for single intervocalic ⟨r⟩ only the tap occurs — so the contrast is positionally restricted.

**No vowel reduction.** Unlike English, Spanish has a clean 5-vowel system `/a e i o u/` with NO phonemic length and NO unstressed vowel reduction — every vowel keeps full quality regardless of stress. Stress is lexical and contrastive, marked orthographically with the acute accent (término / termino / terminó). There is therefore no schwa in the Spanish vowel inventory.

## Suprasegmentals

Prosodic and suprasegmental features of Modern Spanish pronunciation, documented in parallel for two reference accents: Castilian (Peninsular / European Standard, with distinción — the `/θ/`~`/s/` contrast) and Latin American (general pan-American standard, with seseo — `/θ/` merged into `/s/`). Spanish is a stress accent language in which lexical stress is phonemic and contrastive; rhythm is syllable-timed; the five vowels `/a e i o u/` have NO phonemic length and undergo NO vowel reduction (unstressed vowels keep their full quality). The orthographic acute accent (tilde) marks stress that deviates from the default rules. These properties contrast sharply with English, where stress drives pervasive vowel reduction to schwa and a stress-timed rhythm.

### Stress

Spanish lexical stress (acento prosódico) is phonemic and contrastive: the position of stress alone distinguishes otherwise identical words and is not fixed to a single syllable, unlike fixed-stress languages such as French (final stress) or Czech/Finnish (initial stress). In this respect Spanish patterns WITH English (both have phonemic lexical stress). Stress is realized chiefly through greater duration, higher and more dynamic pitch (the syllable carries the pitch accent), and somewhat greater intensity on the stressed syllable. Crucially — and unlike English — the VOWEL QUALITY of the stressed and unstressed syllables is the SAME: there is no reduction, so prominence is carried by duration and pitch rather than by vowel-quality contrast.

#### Stress Levels

| Level | IPA Notation | Phonetic Correlates |
|---|---|---|
| Primary (tonic) stress — sílaba tónica | `ˈ` placed immediately before the stressed syllable (e.g., `/paˈpel/` papel 'paper') | Pitch prominence (the syllable carries the main pitch accent), greater duration, greater intensity. Vowel quality remains FULL and identical to the same vowel when unstressed (no reduction). |
| Unstressed (atonic) — sílaba átona | no mark; the vowel keeps its full quality `/a e i o u/` (NO reduction to schwa) | Shorter duration and no pitch prominence, but FULL vowel quality is preserved. Spanish has no `/ə/`; 'banana' is `/baˈnana/` with three clear `[a]` vowels, not English `[bəˈnænə]`. |

**Note on secondary stress:** Spanish has only a weak and largely rhythmic secondary stress, far less salient than English secondary stress. It may surface on long words and adverbs in -mente (which carry two prominences: the adjective's stress plus the -ˈmen- of the suffix), e.g., rápidamente `[ˌrapiðaˈmente]`. Standard descriptions and dictionaries mark only the single primary (lexical) stress.

#### Phonemic Contrast (Stress Is Lexical/Contrastive)

Stress placement alone is contrastive in Spanish; numerous minimal pairs — and famous minimal TRIPLETS — differ only in which syllable bears the stress. The classic triplet contrasts the same consonant-vowel skeleton across antepenultimate, penultimate, and final stress. Vowel quality does NOT change across the three forms (no English-style reduction); only the position of duration/pitch prominence moves, often signaled orthographically by the acute accent.

**Minimal triplets (esdrújula / llana / aguda):**

| Esdrújula (antepenult) | Llana (penult) | Aguda (final) |
|---|---|---|
| **término** `/ˈteɾmino/` — 'term' (noun; antepenultimate stress — esdrújula, always written with an accent) | **termino** `/teɾˈmino/` — 'I finish / I terminate' (1st person present; penultimate stress — llana, no accent because it ends in a vowel) | **terminó** `/teɾmiˈno/` — 'he/she finished' (3rd person preterite; final stress — aguda, written with an accent because it ends in a vowel) |
| **público** `/ˈpubliko/` — 'public' (adjective/noun; esdrújula) | **publico** `/puˈbliko/` — 'I publish' (1st person present; llana) | **publicó** `/publiˈko/` — 'he/she published' (3rd person preterite; aguda) |
| **depósito** `/deˈposito/` — 'deposit' (noun; esdrújula) | **deposito** `/depoˈsito/` — 'I deposit' (1st person present; llana) | **depositó** `/deposiˈto/` — 'he/she deposited' (3rd person preterite; aguda) |

**Minimal pairs / sets:**

| Spelling | Forms |
|---|---|
| papa / papá | `/ˈpapa/` 'potato' (llana) · `/paˈpa/` 'dad' (aguda) |
| ánimo / animo / animó | `/ˈanimo/` 'spirit, encouragement' (noun; esdrújula) · `/aˈnimo/` 'I encourage' (llana) · `/aniˈmo/` 'he/she encouraged' (aguda) |
| célebre / celebre / celebré | `/ˈθelebɾe/` (Castilian) ~ `/ˈselebɾe/` (Latin American) 'famous' (esdrújula) · `/θeˈlebɾe/` ~ `/seˈlebɾe/` '(that) he/she celebrate' (subjunctive; llana) · `/θeleˈbɾe/` ~ `/seleˈbɾe/` 'I celebrated' (aguda) |
| esta / está | `/ˈesta/` 'this' (demonstrative; llana) · `/esˈta/` 'he/she is / it is' (verb estar; aguda) |

**Note:** Because stress is phonemic, Spanish orthography encodes it: the acute accent (tilde) is written precisely on the syllables that depart from the default stress rules (and on all esdrújulas), so the written form alone disambiguates término / termino / terminó. This is unlike English, where stress is unmarked in spelling.

#### Default Stress Rules & the Orthographic Accent

Although stress is phonemic, its position in the UNMARKED case is predictable from word-final segments. The acute accent is written if and only if a word deviates from these default rules (plus all antepenultimate-and-earlier stress is always written). This is why Spanish stress, though contrastive, is fully recoverable from the orthography.

**Palabras agudas (oxytones)** — stress on the FINAL syllable. Words ending in a CONSONANT OTHER THAN -n or -s are agudas by default and take NO written accent.

| Word | IPA | Gloss |
|---|---|---|
| papel | `/paˈpel/` | 'paper' (ends in -l; aguda by rule, unaccented) |
| reloj | `/reˈlox/` (Castilian) ~ `/reˈloh/` (much of Lat. Am.) | 'clock/watch' (ends in -j; aguda by rule) |
| ciudad | `/θjuˈdad/` ~ `/sjuˈdad/` | 'city' (ends in -d; aguda by rule). Phonetically the intervocalic and coda /d/ spirantize: `[θjuˈðað]` ~ `[sjuˈðað]`. |

Accented exceptions (aguda but contrary to the default condition → accent written):

| Word | IPA | Gloss |
|---|---|---|
| café | `/kaˈfe/` | ends in a vowel yet is aguda → accent written |
| canción | `/kanˈθjon/` ~ `/kanˈsjon/` | ends in -n yet is aguda → accent written |
| compás | `/komˈpas/` | ends in -s yet is aguda → accent written |

**Palabras llanas / graves (paroxytones)** — stress on the PENULTIMATE (next-to-last) syllable. Words ending in a VOWEL, -n, or -s are llanas by default and take NO written accent. This is the most common Spanish stress pattern.

| Word | IPA | Gloss |
|---|---|---|
| casa | `/ˈkasa/` | 'house' (ends in vowel; llana by rule) |
| cantan | `/ˈkantan/` | 'they sing' (ends in -n; llana by rule) |
| lunes | `/ˈlunes/` | 'Monday' (ends in -s; llana by rule) |

Accented exceptions (llana but contrary to the default condition → accent written):

| Word | IPA | Gloss |
|---|---|---|
| árbol | `/ˈaɾbol/` | ends in -l (not vowel/-n/-s) yet llana → accent written. Phonetically the post-vocalic /b/ spirantizes: `[ˈaɾβol]`. |
| lápiz | `/ˈlapiθ/` ~ `/ˈlapis/` | ends in -z yet llana → accent written |
| fácil | `/ˈfaθil/` ~ `/ˈfasil/` | ends in -l yet llana → accent written |

**Palabras esdrújulas (proparoxytones)** — stress on the ANTEPENULTIMATE (third-from-last) syllable. ALL esdrújulas ALWAYS carry a written accent, without exception, regardless of final segment.

| Word | IPA | Gloss |
|---|---|---|
| esdrújula | `/esˈdɾuxula/` ~ `/esˈdɾuhula/` | 'proparoxytone' (the term itself is esdrújula). Phonetically the post-/s/ /d/ spirantizes: `[esˈðɾuxula]`. |
| rápido | `/ˈrapido/` | 'fast'. Phonetically the intervocalic /d/ spirantizes: `[ˈrapiðo]`. |
| teléfono | `/teˈlefono/` | 'telephone' |
| música | `/ˈmusika/` | 'music' |

**Palabras sobresdrújulas (preproparoxytones)** — stress BEFORE the antepenultimate (fourth-from-last or earlier) syllable. ALWAYS accented; arise almost exclusively from verb forms with enclitic pronouns.

| Word | IPA | Gloss |
|---|---|---|
| dígamelo | `/ˈdigamelo/` | 'tell it to me' (verb + two enclitic pronouns). Phonetically the intervocalic /g/ spirantizes: `[ˈdiɣamelo]`. |
| entregándoselo | `/entɾeˈgandoselo/` | 'handing it over to him/her' (gerund + enclitics). Phonetically the intervocalic /g/ spirantizes: `[entɾeˈɣandoselo]`. |

**Diacritic accent note:** The acute accent also serves a purely grammatical (diacritic) function on some monosyllables to distinguish homophones that do not differ in stress: e.g., tú 'you' vs tu 'your'; él 'he' vs el 'the'; sí 'yes' vs si 'if'; más 'more' vs mas 'but'. These are spelling distinctions, not prosodic ones.

#### Cross-Linguistic Comparison

- **Spanish vs French:** French has FIXED stress — prominence falls predictably on the final full syllable of the rhythmic group, so stress is not lexically contrastive; there are no French minimal pairs distinguished by stress alone. Spanish, by contrast, has MOVABLE phonemic stress (término / termino / terminó), making it typologically unlike French in this respect.
- **Spanish vs English:** Spanish patterns WITH English in HAVING lexical, contrastive stress (English record-noun vs record-verb is analogous to Spanish término vs terminó). The key DIFFERENCE is downstream: English stress drives massive vowel reduction (unstressed vowels collapse to `/ə/`), whereas Spanish unstressed vowels retain full quality. So both languages 'have' lexical stress, but only English uses it to license reduction.
- **Summary:** Typological placement: Spanish = movable/phonemic stress (like English, unlike French) BUT no reduction and syllable-timed rhythm (like French, unlike English).

### Rhythm

Spanish is traditionally classified as a SYLLABLE-TIMED language: every syllable tends to take roughly the same amount of time, and the inter-stress intervals therefore vary with the number of syllables they contain. This is the same rhythmic class as French and contrasts directly with STRESS-TIMED English, where unstressed syllables are compressed and reduced to keep stresses roughly equidistant. The syllable-timed character is reinforced by the absence of vowel reduction: because unstressed Spanish vowels keep full quality and comparable duration, syllables do not 'shrink' between stresses the way English ones do, giving Spanish its characteristically even, 'machine-gun' or 'staccato' rhythm to English ears.

#### The Timing Unit

The SYLLABLE (not the stress foot) is the basic rhythmic unit in Spanish. Each syllable is allotted roughly equal time, so an utterance's duration scales with its syllable count rather than its stress count.

**Example:** In 'la ca-sa de mi a-bue-la' (`/la ˈkasa de mi aˈbwela/`; phonetically with spirantization `[la ˈkasa ðe mi aˈβwela]`), each of the syllables is given comparable duration; unstressed syllables are NOT compressed to fit a stress beat.

**IPA notation:** Syllable boundaries may be marked with the period `.` in narrow transcription (e.g., `/a.ˈbwe.la/`, phonetically `[a.ˈβwe.la]`); the stress mark `ˈ` precedes the tonic syllable.

#### Isochrony

ISOCHRONY in Spanish is claimed at the level of the SYLLABLE (syllable-isochrony) rather than the inter-stress foot. As with stress-timing in English, strict acoustic equality is not perfectly supported by measurement, but Spanish reliably shows much LESS durational difference between stressed and unstressed syllables than English does, and no qualitative vowel reduction. Spanish is therefore best described as tending strongly toward syllable-timing on the stress-/syllable-timing continuum.

**Consequence:** Because syllables are not compressed between stresses, adding unstressed syllables lengthens the utterance proportionally rather than speeding up the intervening material. This, combined with full unstressed vowels, is what makes Spanish sound evenly paced compared with the 'galloping' compression of English.

#### Accent Difference

| Accent | Rhythmic Behavior |
|---|---|
| Castilian | Syllable-timed; full unstressed vowels, no reduction. Coda consonants (especially /s/) are typically retained and clearly articulated in standard Peninsular speech, reinforcing even syllable timing. |
| Latin American | Also syllable-timed across all standard varieties. Some varieties (notably Caribbean and other coastal/lowland dialects) aspirate or delete coda /s/ (`[h]` or ∅) and weaken syllable codas, which can lighten certain syllables — yet the overall rhythmic TYPE remains syllable-timed, not stress-timed. |

**Note:** Both reference accents share the syllable-timed rhythmic type, contrasting with stress-timed English. This is the single most important rhythmic difference an English-speaking learner must internalize: do not reduce unstressed vowels, and give each syllable its own beat.

### Vowel Quality & Length

Spanish has a clean five-vowel system `/a e i o u/` with NO phonemic length and NO vowel reduction. This is a defining contrast with English. (1) NO LENGTH: vowel duration is not contrastive — there are no long/short minimal pairs as in English (e.g., English `/i/`–`/ɪ/` or `/ɑː/`–`/ʌ/` distinctions have no Spanish counterpart). Any lengthening is purely a sub-phonemic effect of stress, emphasis, or open-syllable position. (2) NO REDUCTION: unstressed vowels keep their FULL quality — Spanish has no schwa `/ə/` and no centralization. The same vowel phoneme sounds essentially identical whether stressed or unstressed.

#### No Phonemic Length

Vowel length is allophonic at most. Stressed vowels, and vowels in open stressed syllables, may be slightly longer, but length never distinguishes two words. Adjacent identical vowels across a morpheme/word boundary may merge into a single (optionally longer) vowel in casual speech but this is not phonemic length.

| Phenomenon | Detail |
|---|---|
| No long/short pairs | There is a single `/i/` in 'mí' `/mi/` and 'sí' `/si/`; Spanish does not split it into tense/lax `/iː/`–`/ɪ/` as English does in 'beat' vs 'bit'. |
| Allophonic lengthening only | casa `/ˈkasa/` → `[ˈkaˑsa]` with a mildly half-long stressed `[a]`; this is automatic and never contrastive. |

#### No Vowel Reduction

Unlike English, Spanish does NOT reduce unstressed vowels to schwa or alter their quality. Each of `/a e i o u/` retains its full peripheral quality in every position. This is the suprasegmental complement of syllable-timed rhythm: even timing plus full vowels.

**Contrast with English:**

- **English pattern:** English reduces most unstressed full vowels to `/ə/` (or `/ɪ/`): 'banana' = `[bəˈnænə]`, 'photograph' `[ˈfoʊtəɡræf]` → 'photography' `[fəˈtɑɡrəfi]`, where the same letter takes a full vowel under stress and a schwa without it.
- **Spanish pattern:** Spanish keeps the full vowel regardless of stress: 'banana' = `/baˈnana/` → `[baˈnana]` with THREE clear `[a]`'s; 'teléfono' `/teˈlefono/` keeps full `[e]`, `[o]`, `[o]` in the unstressed syllables. There is no Spanish process by which a vowel's quality changes when it loses stress.

| Word | IPA | Note |
|---|---|---|
| banana | `/baˈnana/` | All three /a/ are the full open vowel `[a]`; the unstressed first and third are NOT schwa. Contrast English `[bəˈnænə]`. |
| teléfono | `/teˈlefono/` | Unstressed /e/, /o/, /o/ all keep full quality; no reduction despite three unstressed vowels. |
| compañero | `/kompaˈɲeɾo/` | Unstressed /o/, /a/, /o/ are full; English-influenced reduction to schwa would be a learner error. |
| operación | `/opeɾaˈθjon/` (Castilian) ~ `/opeɾaˈsjon/` (Latin American) | Each unstressed vowel /o/, /e/, /a/ is fully articulated; nucleus on the final aguda syllable -ción. |

**No weak forms:** Because there is no reduction, Spanish has nothing equivalent to the English strong/weak-form alternation of function words. Articles, prepositions, pronouns, and conjunctions keep stable full-vowel pronunciations whether stressed or not. Unstressed grammatical words are simply atonic (de `/de/`, que `/ke/`, en `/en/`, la `/la/`) — they never collapse to a centralized schwa-form the way English 'to' → `/tə/` or 'of' → `/əv/` do.

| Word | IPA | Note |
|---|---|---|
| de | `/de/` | Preposition 'of/from'; always `/de/`, never reduced to schwa. |
| que | `/ke/` | Conjunction/relative 'that'; always full `/ke/`. |
| los | `/los/` | Article 'the' (masc. pl.); full /o/, no reduction. |

**Diphthongs and hiatus note:** Spanish vowel timing also interacts with diphthong/hiatus structure: the weak vowels /i u/ glide to /j w/ next to a stronger vowel within a single syllable (diphthong, e.g., 'aire' `/ˈaiɾe/` → `[ˈai̯ɾe]`), whereas an accent can break this into separate syllables (hiatus, e.g., 'país' `/paˈis/` with stressed /i/ in its own syllable). This is detailed in the vowels/diphthongs sections; prosodically it matters because each syllable — whether containing a diphthong or a single vowel — still receives roughly even timing.

### Intonation

Intonation (entonación) is the linguistically structured use of pitch (fundamental frequency, F0) over the stretch of an utterance (the intonation phrase / grupo entonativo). Spanish intonation is analyzed around a NUCLEAR configuration: a series of pitch accents associated with stressed syllables, plus a final BOUNDARY TONE at the edge of the phrase that does much of the grammatical work of distinguishing statements from questions. Spanish is a pitch-accent-on-stress language: each lexically stressed syllable is a potential docking site for a pitch accent, and the LAST (nuclear) pitch accent plus the final boundary tone determine the contour's meaning. Because stress is full-vowelled and the rhythm is syllable-timed, Spanish pitch movements are typically realized as clear rises and falls aligned to specific syllables.

#### Structure of the Intonation Phrase

The intonation phrase (grupo entonativo / grupo fónico) is the domain of one intonation contour, bounded by perceptible breaks. A typical neutral declarative shows three sections: an initial rise on the first stressed syllable, a relatively high or gradually declining body (declination), and a final movement on/after the nuclear (last stressed) syllable.

**Components:**

- **Pre-nuclear stretch** — the stressed syllables before the nucleus, each typically carrying a rising pitch accent (often L+>H*, the rise peaking on the post-tonic syllable in many Peninsular varieties)
- **Nucleus (núcleo)** — the LAST stressed syllable of the phrase, carrying the nuclear pitch accent that, together with the boundary tone, sets the contour type
- **Boundary tone (tono de frontera / juntura terminal)** — the final pitch target at the phrase edge: falling (L%) for finality, rising (H%) for questioning/continuation, sustained for non-finality

**IPA notation:** Global pitch movement on/after the nucleus is marked with the IPA arrows ↘ (global fall) and ↗ (global rise); ↓ downstep and ↑ upstep mark local pitch resets; tone-unit boundaries with `|` (minor) and `‖` (major). In autosegmental-metrical (Sp_ToBI) notation, pitch accents are written with starred tones on stressed syllables (e.g., L*, H*, L+H*, L+>H*) and boundary tones with % (e.g., L%, H%, M%).

#### Intonation Patterns

| Type | Contour | Boundary Tone | Symbol |
|---|---|---|---|
| Declarative (statement) — enunciativa | Final FALL | L% (low boundary tone) following a typically falling nuclear accent (H+L* or L* on the nucleus) | ↘ |
| Yes/No question (interrogativa total / absoluta) | Final RISE | H% (high boundary tone), typically with a low nuclear accent (L*) followed by the final rise | ↗ |
| Wh-question (interrogativa parcial / pronominal) | Typically a FALL (like a statement), with high pitch on the wh-word | L% (low boundary tone); the interrogative pronoun (qué, quién, cómo, dónde, cuándo, por qué) carries a high pitch accent | ↘ (often with high onset on the wh-word) |
| Continuation / non-final (listing, subordinate clause) | Sustained or slight RISE (anticadence) | Mid/high continuation tone (often analyzed as M% or H-) signaling 'more to come' | → / ↗ |
| Exclamative / emphatic — exclamativa | Expanded pitch range, often a rise-fall on the nucleus | L% (usually falling to low) but with a markedly higher peak and wider excursion | ↗↘ |

**Declarative (statement) — enunciativa:** The neutral broad-focus statement shows an early rise, gradual declination across the body, and a clear FALL on/after the nucleus (the last stressed syllable), ending low. This conveys finality, completeness, and assertion. It is the direct analog of the English statement fall.
*Example:* María come manzanas. — `/maˈɾi.a ˈkome manˈθanas↘/` (Castilian) ~ `/maˈɾi.a ˈkome manˈsanas↘/` (Latin American) — 'María eats apples.' Nucleus on -ˈza-/-ˈza- of manzanas, falling to a low boundary.

**Yes/No question (interrogativa total / absoluta):** A polar (yes/no) question characteristically ends in a RISE: the pitch falls or stays low through the nucleus and then rises sharply to a high boundary tone at the phrase edge. Crucially, since Spanish word order in a yes/no question is often IDENTICAL to the statement (¿María come manzanas? = María come manzanas.), the RISING intonation alone can be what marks the utterance as a question. This is the canonical Spanish question-vs-statement intonational minimal contrast. (Some varieties — e.g., parts of the Caribbean, Canary Islands, and Galician-influenced NW Spain — use a falling or circumflex final contour on yes/no questions instead, a notable dialectal exception.)
*Example:* ¿María come manzanas? — `/maˈɾi.a ˈkome manˈθanas↗/` ~ `/...manˈsanas↗/` — 'Does María eat apples?' Same segments as the statement; the final rise to H% does the questioning.

**Wh-question (interrogativa parcial / pronominal):** Information (wh-) questions, which are introduced by an accented interrogative word, are usually pronounced with a FALLING nuclear contour — the questioning is already signaled lexically by the wh-word, so a rise is not required (parallel to English wh-question falls). A rise on a wh-question typically adds a nuance of politeness, surprise, or a request to repeat.
*Example:* ¿Qué comes? — `/ˈke ˈkomes↘/` — 'What are you eating?' High pitch on qué, falling to a low boundary.

**Continuation / non-final (listing, subordinate clause):** Non-final intonation phrases — items in a list before the last, or a clause that precedes its completion — end on a sustained mid-level or slightly rising tone (anticadencia / semicadencia) that signals incompleteness and projects continuation, exactly as English non-final list items rise. The final item then takes the appropriate terminal contour (fall for a closed list).
*Example:* Compré pan→, queso→, y vino↘. — `/komˈpɾe ˈpan→ ˈkeso→ i ˈbino↘/` — 'I bought bread, cheese, and wine.' Non-final items sustained/rising; the final item falls to L%.

**Exclamative / emphatic — exclamativa:** Exclamations widen the pitch range and raise the peak, typically producing a rise-fall on the emphasized (nuclear) syllable, conveying strong feeling — surprise, admiration, indignation. Functionally parallel to the English rise-fall of strong involvement.
*Example:* ¡Qué bonito! — `/ˈke boˈnito↘/` (phonetically with spirantized intervocalic /b/ `[ˈke βoˈnito↘]`) with an expanded high peak on -ˈni- — 'How beautiful!'

#### Pitch-Accent Role & Focus

Spanish associates pitch accents with LEXICALLY STRESSED syllables: prominence (the pitch movement) docks on the tónica of each accented word, never on an arbitrary syllable. Because stress is phonemic and full-vowelled, the alignment of the F0 peak with (or just after) the stressed syllable is perceptually clear and is itself a marker of which syllable is stressed. The PLACEMENT of the nuclear pitch accent marks FOCUS / new information: by default the nucleus falls on the last content word (broad focus), but it shifts leftward for contrastive/narrow focus, highlighting a particular constituent.

| Utterance | Focus |
|---|---|
| Juan compró un coche ROJO. — `/xwan komˈpɾo un ˈkotʃe ˈroxo↘/` | Broad / default focus — nucleus on the last content word (rojo). |
| JUAN compró un coche rojo. (no fue otro) — nucleus shifted to the subject | Contrastive/narrow focus on the subject Juan ('it was JUAN, not someone else'). |
| Juan COMPRÓ un coche rojo. (no lo alquiló) — nucleus on the verb | Contrastive focus on the verb ('Juan BOUGHT it, he didn't rent it'). |

**Note:** Spanish relies more on word order and prosodic phrasing (e.g., fronting or clefting: 'Fue Juan quien...') to mark focus than English does, but pitch-accent placement on the stressed syllable of the focused word is the core intonational mechanism, mirroring English nucleus placement.

#### Functions of Intonation

- **Grammatical:** Distinguishes sentence types — most importantly statement (fall, L%) vs yes/no question (rise, H%) when word order is identical; marks clause/phrase boundaries; signals continuation vs completion in lists and complex sentences.
- **Focus and information:** Placement of the nuclear pitch accent marks the focus / new information; shifting the nucleus leftward yields contrastive/narrow focus.
- **Attitudinal:** Pitch range and contour shape convey attitude and emotion — politeness, surprise, insistence, irony, doubt — e.g., a yes/no rise added to a wh-question softens it into a polite or surprised query.
- **Discourse:** Manages turn-taking, signals topic boundaries via major (`‖`) vs minor (`|`) breaks, and links or contrasts information across an exchange through pitch resets (downstep/upstep).

#### Accent Difference

| Accent | Intonational Behavior |
|---|---|
| Castilian | Peninsular Castilian neutral declaratives show a characteristic pre-nuclear rise that PEAKS on the post-tonic syllable (analyzed as L+>H* with a late peak) and a clear final fall to L%; yes/no questions rise to H%. Pitch range is comparatively moderate. Standard Sp_ToBI descriptions of Spanish intonation are largely built on Peninsular data. |
| Latin American | Latin American varieties broadly share the declarative-fall / yes/no-question-rise system, but differ in detail: many show EARLIER F0 peaks (peak aligned within the stressed syllable, L+H*), and several varieties have distinctive contours — e.g., Mexican Spanish 'circumflex' (rise-fall) phrase-final patterns, Rioplatense (Buenos Aires) intonation noted for its Italian-influenced melodic shape, and Caribbean varieties that may use a FINAL FALL on yes/no questions (the reverse of the canonical rise). Andean and Chilean varieties have their own pitch-accent alignments. |

**Note:** The fundamental inventory — declarative fall (L%), yes/no-question rise (H%), wh-question fall, and non-final continuation rise — is shared across both reference accents; differences are largely in F0-peak ALIGNMENT (late vs early peaks), pitch range, and a few salient dialectal contours (Caribbean falling polar questions, Mexican circumflex, Rioplatense melody). Spanish as a whole is syllable-timed and reduction-free, so these pitch movements are realized over clear, full-quality syllables.

## Syllable Structure

Syllable structure patterns in Modern Spanish, documented for two reference accents in parallel: Castilian (Peninsular / European Standard, with *distinción* — the `/θ/` ~ `/s/` contrast) and Latin American (general pan-American standard, with *seseo* — `/θ/` merged into `/s/`). In sharp contrast with English, Spanish strongly prefers OPEN, CV syllables: the favored and statistically dominant shape is consonant + vowel, codas are far simpler than English, and complex margins are tightly restricted. The nucleus is always a vowel (or a vowel + glide diphthong/triphthong); Spanish has NO syllabic consonants, NO phonemic vowel length, and NO vowel reduction (the five vowels `/a e i o u/` keep full quality whether stressed or unstressed). The maximal native shape is CCVCC, and even that is uncommon; the great majority of syllables are V, CV, or CVC. Stress is lexical and contrastive (*término* / *termino* / *terminó*). Across word boundaries Spanish actively reshapes syllables: a word-final consonant resyllabifies as the onset of a following vowel-initial word (*resilabación*), and adjacent vowels across word boundaries merge into a single syllable (*sinalefa*). This section is the Spanish equivalent of the Peshitta guide's syllable_structure section.

**IPA template:** `(C)(C)V(G)(C)(C)`

**Maximal syllable:** `CCVCC`

**Preferred syllable:** `CV`

**Components:**

- **Onset:** 0 to 2 consonants preceding the nucleus *(optional)*
- **Nucleus:** V — a full vowel, diphthong (V+G), or triphthong (G+V+G); always vocalic *(required)*
- **Coda:** 0 to 2 consonants following the nucleus *(optional)*

### Onset

0 to 2 consonants preceding the nucleus. The single-consonant onset is by far the most frequent and any consonant can fill it (the trill `/r/` and the tap `/ɾ/` both occur word-initially / syllable-initially, though `/ɾ/` does not begin a word). Two-consonant onsets are limited to a strict, closed set: an obstruent `/p b t d k ɡ f/` followed by a liquid `/l/` or `/ɾ/` (a *muta cum liquida* cluster), obeying rising sonority toward the nucleus. Spanish has NO three-consonant onsets and NO `/s/`+consonant onsets at all — the latter gap forces a prothetic `/e/` before historical sC- clusters (see constraints).

- **Minimum consonants:** 0
- **Maximum consonants:** 2

**Sonority sequencing:** Within an onset, sonority must rise toward the vowel (obstruent < liquid < vowel). Spanish permits ONLY obstruent + liquid clusters and has no sonority-reversing `/s/`+stop onsets of the English type. The Spanish trill `/r/` never appears as the second member of a cluster; only the tap `/ɾ/` does (e.g. `/tɾ/` in *tres*, never `*/tr/`).

**Two-consonant onsets** — structure: obstruent `/p b t d k ɡ f/` + liquid `/l ɾ/`.

Attested clusters: `pl`, `pɾ`, `bl`, `bɾ`, `tɾ`, `dɾ`, `kl`, `kɾ`, `ɡl`, `ɡɾ`, `fl`, `fɾ`.

**Gaps:** The clusters `*/tl/` and `*/dl/` are absent in native onsets (the orthographic 'tl' of words like *atlas* or the Nahuatlism *tlapalería* is heterosyllabic in most Peninsular usage — `/at.las/` — though many Latin American varieties, especially Mexican, do syllabify `/a.tlas/`). `/dl/` never forms an onset.

| Word | IPA | Phonetic | Onset | Gloss | Note |
|---|---|---|---|---|---|
| plato | `/ˈpla.to/` | — | `pl` | plate | |
| prima | `/ˈpɾi.ma/` | — | `pɾ` | cousin (f.) | |
| blanco | `/ˈblan.ko/` | — | `bl` | white | |
| tres | `/tɾes/` | — | `tɾ` | three | |
| clave | `/ˈkla.be/` | `[ˈkla.βe]` | `kl` | key | Intervocalic `/b/` spirantizes to the approximant `[β]`; phonemic `/b/` is shown in `//` and the allophone in `[]`. |
| grande | `/ˈɡɾan.de/` | — | `ɡɾ` | big | |
| flores | `/ˈflo.ɾes/` | — | `fl` | flowers | |

**Single-consonant onset notes:** Any of the ~17–19 phonemes may be a simple onset. The voiced stops `/b d ɡ/` surface as STOPS `[b d ɡ]` utterance-initially and after a nasal (and `/d/` also after `/l/`), but SPIRANTIZE to approximants `[β ð ɣ]` in most other onset positions — the hallmark Spanish process (e.g. *la vaca* `[la ˈβa.ka]` vs utterance-initial *vaca* `[ˈba.ka]`). The trill `/r/` and tap `/ɾ/` contrast only intervocalically (*perro* `/ˈpe.ro/` vs *pero* `/ˈpe.ɾo/`); word-initial and post-consonantal 'r' is always the trill `/r/` (*rosa* `/ˈro.sa/`).

### Nucleus

The obligatory core of the syllable, ALWAYS a vocalic element — Spanish has no syllabic consonants. It is filled by one of the five full vowels `/a e i o u/` (a monophthong), or by a rising/falling diphthong (vowel + glide `/j w/`), or, less commonly, by a triphthong (glide + vowel + glide). Vowel quality is constant regardless of stress: there is no reduction to schwa.

#### Vowel nucleus

A single full vowel. The five-vowel system `/a e i o u/` has no phonemic length and no quality alternation between stressed and unstressed positions.

Vowels: `a`, `e`, `i`, `o`, `u`.

| Word | IPA | Nucleus | Gloss |
|---|---|---|---|
| casa | `/ˈka.sa/` | `a` | house |
| mesa | `/ˈme.sa/` | `e` | table |
| sí | `/si/` | `i` | yes |
| todo | `/ˈto.do/` | `o` | all |
| uno | `/ˈu.no/` | `u` | one |

#### Diphthong nucleus

A vowel combined with a glide `/j/` (palatal) or `/w/` (labiovelar) within a single nucleus. RISING diphthongs (glide + vowel) begin with the glide; FALLING diphthongs (vowel + glide) end with it. The high vowels `/i u/` become glides `[j w]` when adjacent to a more open vowel in the same syllable. Counting both series, Spanish has 16 possible diphthongs (8 rising + 8 falling) as enumerated in the 'attested' lists below, though not all are equally native: the falling 'ow' is essentially non-native (it occurs only in loans/proper nouns such as *bou*), and 'uj' and 'iw' are rare/marginal, so the conventional inventory of fully native common diphthongs is about 14. The combinations `/i/`+`/u/` are also possible (e.g. *ciudad*, *viuda*). A written accent on the high vowel breaks the diphthong into hiatus (two syllables): *río* `/ˈri.o/`, *país* `/pa.ˈis/`.

**Rising diphthongs** — structure: glide `/j w/` + vowel.

Attested: `ja`, `je`, `jo`, `ju`, `wa`, `we`, `wi`, `wo`.

| Word | IPA | Castilian | Latin American | Nucleus | Gloss | Note |
|---|---|---|---|---|---|---|
| tiempo | `/ˈtjem.po/` | — | — | `je` | time/weather | |
| agua | `/ˈa.ɡwa/` | — | — | `wa` | water | Intervocalic `/ɡ/` spirantizes to the approximant `[ɣ]` → `[ˈa.ɣwa]`. |
| bueno | `/ˈbwe.no/` | — | — | `we` | good | |
| ciudad | `/sju.ˈdad/` | `[θju.ˈðað]` | `[sju.ˈðað]` | `ju` | city | Oxytone — primary stress on the final syllable (ciu-DAD). Phonemic `/sju.ˈdad/` (general *seseo*); the intervocalic and final `/d/` spirantize to `[ð]` in connected speech, hence Latin American `[sju.ˈðað]` and Castilian `[θju.ˈðað]`. |

**Falling diphthongs** — structure: vowel + glide `/j w/`.

Attested: `aj`, `ej`, `oj`, `uj`, `aw`, `ew`, `ow`, `iw`.

**Marginal note:** The fully native falling diphthongs are 'aj' (*baile*), 'ej' (*seis*), 'oj' (*hoy*), 'aw' (*aula*), 'ew' (*Europa*), and 'iw' (*viuda*, *ciudad*). 'uj' (*muy*) is restricted to a few words, and 'ow' is essentially non-native — it appears only in loans and proper nouns (e.g. *bou*) with no common native word — so it is listed for completeness but should be treated as marginal, not part of the core inventory.

| Word | IPA | Nucleus | Gloss |
|---|---|---|---|
| baile | `/ˈbaj.le/` | `aj` | dance |
| seis | `/sejs/` | `ej` | six |
| aula | `/ˈaw.la/` | `aw` | classroom |
| Europa | `/ew.ˈɾo.pa/` | `ew` | Europe |

#### Triphthong nucleus

A three-element nucleus of the shape glide + vowel + glide (`/jVj/`, `/wVj/`, etc.), found chiefly in second-person plural verb forms (*vosotros*) and a few nouns. Always built around an open or mid vowel flanked by two glides.

Structure: glide `/j w/` + vowel + glide `/j w/`. Attested: `jaj`, `jej`, `waj`, `wej`.

| Word | IPA | Phonetic | Nucleus | Gloss | Note |
|---|---|---|---|---|---|
| estudiáis | `/es.tu.ˈdjajs/` | `[es.tu.ˈðjajs]` | `jaj` | you (pl.) study | Intervocalic `/d/` spirantizes to `[ð]`. |
| averiguáis | `/a.be.ɾi.ˈɡwajs/` | `[a.βe.ɾi.ˈɣwajs]` | `waj` | you (pl.) find out | Intervocalic `/b/` and `/ɡ/` spirantize to `[β]` and `[ɣ]`. |
| Uruguay | `/u.ɾu.ˈɡwaj/` | `[u.ɾu.ˈɣwaj]` | `waj` | Uruguay | Intervocalic `/ɡ/` spirantizes to `[ɣ]`. |
| buey | `/bwej/` | — | `wej` | ox | |

### Coda

0 to 2 consonants following the nucleus, but Spanish codas are markedly SIMPLER and more restricted than English ones. Word-internally, single codas are the norm and only a limited set of consonants is fully native in coda position — chiefly `/n s ɾ l d θ/` (Castilian) / `/n s ɾ l d/` (*seseo* Latin American), plus `/b k ɡ ɲ/` marginally in learned/loan vocabulary. Word-FINAL codas are even more restricted, dominated by `/s n ɾ l d θ/` (e.g. plurals in -s, verb endings in -n, infinitives in -ɾ, `/-dad/` nouns realized phonetically as `[-ðað]`). Two-consonant codas occur only word-internally before a heterosyllabic onset (e.g. *instituto*, *perspectiva*) and are felt as learned; Spanish has nothing like English four-consonant suffix stacks. Coda consonants are phonetically weak and prone to lenition: `/s/` aspirates to `[h]` (Caribbean, Andalusian, much coastal/southern speech) and may delete; `/d/` in final position weakens to `[ð]` and often drops (*Madrid* `[ma.ˈðɾi(ð)]`~`[ma.ˈðɾiθ]`); coda `/n/` velarizes to `[ŋ]` in many dialects.

- **Minimum consonants:** 0
- **Maximum consonants:** 2

**Common coda consonants:**

| Accent | Common coda consonants |
|---|---|
| Castilian | `n`, `s`, `ɾ`, `l`, `d`, `θ` |
| Latin American | `n`, `s`, `ɾ`, `l`, `d` |

`/θ/` is a possible coda only in Castilian (*distinción*), e.g. *paz* `/paθ/`, *luz* `/luθ/`; in *seseo* Latin American these have coda `/s/` (*paz* `/pas/`, *luz* `/lus/`). Marginal/learned codas `/b k ɡ p t/` appear in loans and technical words (*club* `/klub/`, phonetically `[kluβ]`; *coñac*, *iceberg*, *apto*, *étnico*) and are frequently lenited or simplified in casual speech.

**Two-consonant codas:** Restricted to word-internal position before another syllable's onset. Where the consonant string cannot be redistributed (because neither member can join the following onset), a genuine tautosyllabic two-consonant coda results — these are real but uncommon and felt as learned, occurring chiefly in *cultismos* (learned borrowings from Latin). Such codas typically end in `/s/`. In *ins-ti-tu-to* the `/ns/` closing the first syllable IS a genuine word-internal tautosyllabic CC coda (not a heterosyllabic split): `/st/` is not a legal Spanish onset, so both consonants stay in the first syllable's coda.

| Word | IPA | Phonetic | Coda | Gloss | Note |
|---|---|---|---|---|---|
| instituto | `/ins.ti.ˈtu.to/` | — | `ns` | institute | `/ns/` is a genuine tautosyllabic two-consonant coda on the first syllable 'ins' — `/st/` cannot form an onset, so both consonants close the syllable. |
| perspectiva | `/peɾs.pek.ˈti.ba/` | `[peɾs.pek.ˈti.βa]` | `ɾs` | perspective | `/ɾs/` is a genuine word-internal tautosyllabic two-consonant coda closing the first syllable 'peɾs'; intervocalic `/b/` spirantizes to `[β]`. |
| transporte | `/ˈtɾans.poɾ.te/` | — | `ns` | transport | `/ns/` closes the first syllable (tautosyllabic two-consonant coda); `/ɾt/` is not a legal onset, so `/ɾ/` stays in the coda of 'poɾ'. |

**Colloquial simplification:** Such learned coda clusters are commonly reduced in everyday speech: *instituto* `[in.ti.ˈtu.to]`, *transporte* `[tɾas.ˈpoɾ.te]`, reflecting the language's strong preference for simple codas / open syllables.

**Nasal assimilation:** A coda nasal `/n/` assimilates in place to a following consonant: `[m]` before labials (*un beso* `[um ˈbe.so]`), `[ɱ]` before `/f/` (*enfermo* `[eɱ.ˈfeɾ.mo]`), `[n̪]` before dentals `/t d/` (*cuando* `[ˈkwan̪.do]`), `[ɲ]` before palatals, and `[ŋ]` before velars `/k ɡ x/` (*blanco* `[ˈblaŋ.ko]`, *tengo* `[ˈteŋ.ɡo]`). This is allophonic, not a change of phoneme.

### Syllable Types

| Type | Description | IPA example | Word | Frequency |
|---|---|---|---|---|
| V | Bare vowel; no onset, no coda (open syllable) | `/a/` | a (preposition 'to') | Common (function words, prefixes, hiatus syllables) |
| CV | Open syllable (single consonant + vowel) — the preferred and most frequent Spanish syllable | `/lo/` | lo | Most common (the canonical, dominant shape) |
| VC | Vowel + single coda (no onset) | `/en/` | en | Common |
| CVC | Closed syllable (onset + vowel + single coda) | `/sol/` | sol | Very common |
| CCV | Obstruent+liquid onset cluster + vowel (open) | `/tɾes/` (`/tɾe/` as in the open syllable of 'tre.gua') | tre- (in 'tregua') | Common |
| CGV | Onset + rising-diphthong nucleus (consonant + glide + vowel, open) | `/bwe/` | bue- (in 'bueno') | Common |
| CVG | Onset + falling-diphthong nucleus (open syllable ending in a glide) | `/baj/` | bai- (in 'baile') | Common |
| CCVC | Obstruent+liquid onset + vowel + single coda (closed) | `/tɾen/` | tren | Common |
| CGVC | Onset + rising diphthong + coda | `/bjen/` | bien | Common |
| CVCC | Onset + vowel + two-consonant coda (learned/word-internal; maximal native coda) | `/kons/` (as in 'cons.truc.ción' or 'cons.tar') | cons- (in 'constar') | Rare (cultismos only; often simplified in speech) |
| CCVCC | Maximal native syllable: obstruent+liquid onset + vowel + two-consonant coda | `/tɾans/` | trans- (in 'transporte') | Rare |
| CGVG | Onset + triphthong nucleus (glide + vowel + glide) | `/bwej/` | buey | Rare (mainly vosotros verb forms, a few nouns) |

### Syllabification

**Principle:** Maximal Onset Principle (with the Spanish onset inventory)

When consonants stand between two vowels, as many as can form a LEGAL Spanish onset are assigned to the following syllable; the rest stay in the preceding coda. Because Spanish allows only single consonants and obstruent+liquid as onsets, a single intervocalic consonant always begins the next syllable (V.CV), and an intervocalic obstruent+liquid cluster also joins the next syllable, while any other two-consonant string is split (VC.CV). Spanish further reshapes syllables ACROSS word boundaries by two productive processes: *resilabación* (resyllabification) and *sinalefa*.

| Word | IPA | Phonetic | Note |
|---|---|---|---|
| casa | `/ˈka.sa/` | — | single intervocalic `/s/` becomes the onset of the next syllable (V.CV) |
| padre | `/ˈpa.dɾe/` | `[ˈpa.ðɾe]` | obstruent+liquid `/dɾ/` is a legal onset, so the whole cluster joins the second syllable (V.CCV); intervocalic `/d/` spirantizes to `[ð]` |
| carta | `/ˈkaɾ.ta/` | — | `/ɾt/` is not a legal onset, so the `/ɾ/` stays in the first (closed) syllable (VC.CV) |
| instante | `/ins.ˈtan.te/` | — | `/nst/` cannot all be onset; `/st/` is not a Spanish onset either, so the break leaves `/ns/` in the coda of the first syllable |
| construir | `/kons.tɾu.ˈiɾ/` | — | `/ns/` closes the first syllable; `/tɾ/` (legal onset) opens the second |

#### Resilabación (across word boundaries)

A word-final consonant is pronounced as the onset of the next word when that word begins with a vowel, dissolving the word boundary in connected speech. This is obligatory and pervasive in normal-tempo Spanish, and it feeds the spirantization of `/b d ɡ/` and the `/s/`→`[z]` voicing rules because the consonant now stands in onset, intervocalic position.

| Phrase | IPA | Note |
|---|---|---|
| los amigos | `[lo.sa.ˈmi.ɣos]` | final `/s/` of 'los' becomes the onset of 'a-', and intervocalic `/ɡ/` in 'amigos' spirantizes to `[ɣ]` |
| el árbol | `[e.ˈlaɾ.βol]` | final `/l/` of 'el' onsets the vowel of 'árbol' |
| un hombre | `[u.ˈnom.bɾe]` | final `/n/` of 'un' resyllabifies as the onset of 'hombre' (silent 'h') |
| más o menos | `[ma.so.ˈme.nos]` | final `/s/` of 'más' onsets the following 'o' |

#### Sinalefa (vowel coalescence across word boundaries)

When one word ends in a vowel and the next begins with a vowel (orthographic 'h' being silent), the two vowels are pronounced together in a SINGLE syllable rather than as separate syllabic beats. *Sinalefa* is the across-word counterpart of word-internal diphthongization and is central to Spanish rhythm and to verse scansion (it determines syllable counts in poetry). Identical vowels typically fuse into one; differing vowels form a diphthong-like glide-plus-vowel sequence. Stronger/lower vowels tend to retain syllabicity while higher vowels reduce to glides.

| Phrase | IPA | Syllables | Note |
|---|---|---|---|
| mi hermano | `[mjeɾ.ˈma.no]` | mier-ma-no (3, not 4) | `/i/` + `/e/` across the boundary merge: `/i/` becomes the glide `[j]` |
| su amigo | `[swa.ˈmi.ɣo]` | swa-mi-go (3, not 4) | `/u/` + `/a/` merge into one syllable; `/u/` becomes the glide `[w]` |
| la amiga | `[la.ˈmi.ɣa]` | la-mi-ga (3, not 4) | identical-quality merge of `/a/` + `/a/` into a single vowel |
| lo he hecho | `[loe.ˈt͡ʃo]` | loe-cho (2, not 4) | 'h' is silent; `/o/` + `/e/` coalesce into one syllable across two word boundaries |
| casa elegante | `[ka.sae.le.ˈɣan.te]` | ca-sae-le-gan-te (5, not 6) | `/a/` + `/e/` across the boundary count as one syllable in scansion |

### Constraints

- The strongly preferred syllable is OPEN CV; Spanish maximizes onsets and minimizes codas, the opposite tendency from English. Statistically, CV and V account for the majority of syllables in running text.
- No `/s/` + consonant onset is permitted. Historical Latin (and modern loan) sC- clusters trigger a PROTHETIC `/e/` that creates a legal syllable: Latin *schola* → *escuela*, *Spania* → *España*, *studiante* (Lat. *studentem*) → *estudiante*, *stress* → *estrés*, *spray* → *espray*, *Stalin* → *Estalin*. A Spanish word can therefore never begin with `/s/` followed by another consonant.
- Onsets allow at most two consonants, and a two-consonant onset MUST be obstruent `/p b t d k ɡ f/` + liquid `/l ɾ/` (rising sonority). No other onset clusters exist; there are no three-consonant onsets.
- Within an onset cluster the liquid is the TAP `/ɾ/`, never the trill `/r/` (e.g. *tres* `/tɾes/`, *prado* `/ˈpɾa.do/`, phonetically `[ˈpɾa.ðo]` with spirantized `/d/`). The trill `/r/` occurs only as a simple onset (word-initial or after a heterosyllabic consonant) and intervocalically.
- The clusters `*/tl/` and `*/dl/` are not native onsets; orthographic 'tl' is heterosyllabic in Peninsular Spanish (*at.las*) though tautosyllabic (*a.tlas*) in much of Latin America, especially Mexico.
- The nucleus is always vocalic — Spanish has NO syllabic consonants (no `/l̩ n̩ m̩ r̩/` nuclei of the English 'bottle, button, rhythm' type). Every syllable contains a full vowel, diphthong, or triphthong.
- Vowels have no phonemic length and undergo NO reduction: unstressed `/a e i o u/` keep full quality and never centralize to schwa. (Major typological contrast with English.)
- Stress is lexical and contrastive and is the only thing distinguishing many triplets: *término* `/ˈteɾ.mi.no/` vs *termino* `/teɾ.ˈmi.no/` vs *terminó* `/teɾ.mi.ˈno/`. The acute accent marks irregular stress orthographically.
- Codas are restricted to a small set, chiefly `/n s ɾ l d/` (plus `/θ/` in Castilian *distinción*); other consonants in coda are marginal, learned, or loan-bound and are frequently lenited or dropped.
- Word-final codas are even more limited than internal ones, dominated by `/s n ɾ l d/` (and Castilian `/θ/`): e.g. plural -s, 3rd-person-plural verb -n, infinitive -ɾ, nouns in `/-dad/` (phonetically `[-ðað]`). Word-final `/d/` commonly weakens to `[ð]` or deletes; in Castilian it may surface as `[θ]` (*Madrid* `[ma.ˈðɾiθ]`).
- Two-consonant codas are rare, restricted to word-internal *cultismos* (learned Latinisms) such as *instituto*, *perspectiva*, *transporte*, and are routinely simplified in colloquial speech (*istituto*, *trasporte*). There is nothing comparable to English three- or four-consonant suffix codas.
- A coda nasal assimilates in place to the following consonant (`[m ɱ n̪ ɲ ŋ]`); this is allophonic. In many dialects (Caribbean, much of Latin America) word-final `/n/` velarizes to `[ŋ]`.
- Coda `/s/` is widely weakened: in Caribbean, Andalusian, and other southern/coastal varieties it aspirates to `[h]` (*los amigos* `[loh.a.ˈmi.ɣoh]`) or deletes, a salient dialect marker (the *distinción*/*seseo* question concerns onset `/θ/`~`/s/`, but coda `/s/`-aspiration is an independent areal feature).
- Across word boundaries, *resilabación* moves a final consonant into the onset of a following vowel-initial word (*los amigos* `[lo.sa.ˈmi.ɣos]`), feeding intervocalic spirantization of `/b d ɡ/` → `[β ð ɣ]` and voicing of `/s/` → `[z]` before voiced consonants.
- Across word boundaries, *sinalefa* fuses a final vowel and a following initial vowel into a single syllable (*su amigo* `[swa.ˈmi.ɣo]`); this is obligatory at normal tempo and governs syllable counting in Spanish verse.
- The Maximal Onset Principle governs medial consonant assignment, subject to the constraint that the resulting onset and coda must each be an independently legal Spanish margin (a single consonant or an obstruent+liquid onset; a permitted coda consonant set).

## Phonological Rules

Active connected-speech and allophonic processes in Modern Spanish, documented in parallel for two reference accents: **Castilian** (Peninsular / European Standard Castilian, which has *distinción* — the `/θ/`~`/s/` contrast) and **Latin American** (general pan-American standard, which has *seseo* — `/θ/` merged into `/s/`). These rules describe systematic, largely automatic changes that apply to underlying phonemic forms to yield surface phonetic forms. Many operate within the phonological phrase across word boundaries in connected speech (Spanish syllabifies and resyllabifies freely across words), while others are word-internal allophonic adjustments. Unlike English, Spanish has **NO** phonemic vowel length and **NO** vowel reduction: the five vowels `/a e i o u/` keep full quality in every position, stressed or unstressed. Accent scope is marked as 'Castilian', 'Latin American', or 'both'; where a process applies in both but differs in detail, or is restricted to particular sub-varieties (Caribbean, Andalusian, Rioplatense, Andean), the divergence is noted. IPA examples are given as input → output, with /slashes/ for phonemic underlying forms and [brackets] for phonetic surface forms.

> Note on stress: Spanish word stress is **lexical and contrastive** — marked by the orthographic accent and able to distinguish otherwise identical strings (e.g. *término* / *termino* / *terminó*). It is never fixed to a syllable; the rules below presuppose this lexical stress and, crucially, do **not** trigger any accompanying change of vowel quality.

### Rules at a Glance

| # | Rule | Process | Accents |
|---|---|---|---|
| 1 | Spirantization (lenition of voiced stops) | `/b d ɡ/ → [β ð ɣ]` | both |
| 2 | Distinción vs. seseo (`/θ/`–`/s/` contrast) | ⟨z⟩, ⟨ce⟩, ⟨ci⟩ → `[θ]` ~ `[s]` | both |
| 3 | Yeísmo (`/ʎ/` → `/ʝ/` merger) | `/ʎ/ → /ʝ/` | both |
| 4 | Nasal place assimilation | `/n/ → [m ɱ n̪ n ɲ ŋ]` | both |
| 5 | `/s/` voicing before voiced consonants | `/s/ → [z]` | both |
| 6 | Coda `/s/`-aspiration and elision | `/s/ → [h] (~ ∅)` | both |
| 7 | Sinalefa (cross-word vowel coalescence) | `V#V → tautosyllabic` | both |
| 8 | Trill vs. tap distribution | `/r/` vs. `/ɾ/` | both |
| 9 | `/x/` realization (`[x]`~`[χ]` vs. `[h]`) | `/x/ → [x ~ χ ~ h]` | both |
| 10 | Final-`/d/` weakening and elision | `/d/ → [ð] → [θ] ~ ∅` | both |
| 11 | Lateral and nasal dental/palatal assimilation | `/l n/ → [l̪ n̪] / [lʲ nʲ]` | both |
| 12 | Rioplatense rehilamiento (`/ʝ/` → `[ʒ ʃ]`) | `/ʝ/ → [ʒ ~ ʃ]` | Latin American |
| 13 | Ceceo (some Andalusian `/s/` → `[θ]`) | `/s/ → [θ]` | Castilian |
| 14 | Voiceless stops unaspirated; `/p t k/` lenition | `/p t k/ → [p t k]` | both |
| 15 | Vowel sequence reduction (hiatus → diphthong) | unstressed high V → glide `[j w]` | both |

### Rule 1: Spirantization (lenition of voiced stops)

The hallmark process of Spanish phonology. The voiced obstruents `/b d ɡ/` surface as voiced approximants `[β ð ɣ]` (lenis, frictionless continuants) in the great majority of positions. They are realized as full stops `[b d ɡ]` ONLY in three blocking environments: (1) utterance-initially after a pause; (2) after any nasal (which assimilates in place); and additionally for `/d/` only, (3) after `/l/`. Thus *un beso* → `[um ˈbeso]` (stop after nasal) but *el beso* → `[el ˈβeso]` (approximant). The contrast is allophonic, not phonemic, and applies across word boundaries. Pervasive and near-categorical in both reference accents.

**IPA example:** `/b d ɡ/ → [β ð ɣ]` : *la barca* `/la ˈbaɾka/` → `[la ˈβaɾka]`, *cada* `/ˈkada/` → `[ˈkaða]`, *lago* `/ˈlaɡo/` → `[ˈlaɣo]`  
**IPA notation:** `/b d ɡ/ → [β ð ɣ] / elsewhere; → [b d ɡ] / {#__ after pause, N__, l__ (for /d/ only)}`  
**Environment:** Approximant `[β ð ɣ]` in all positions EXCEPT: utterance-initial after pause, after a nasal, and (for `/d/` only) after `/l/`, where full stops appear  
**Accents:** both  

### Rule 2: Distinción vs. seseo (`/θ/`–`/s/` contrast)

The principal accent-defining split. In Castilian (*distinción*) the dental fricative `/θ/` and alveolar `/s/` are distinct phonemes: *caza* (hunt) `/ˈkaθa/` contrasts with *casa* (house) `/ˈkasa/`, and *cocer*/*coser* are minimal pairs. Orthographic ⟨z⟩ and ⟨c⟩ before ⟨e i⟩ map to `[θ]`. In Latin American Spanish (and Canarian/much of Andalusian), *seseo* applies: `/θ/` is wholly merged into `/s/`, so *caza* and *casa* are homophones `[ˈkasa]`. The merger is to the alveolar `[s]` (or a more apical/dorsal `[s]` depending on region).

**IPA example:** *caza* `/ˈkaθa/` vs. *casa* `/ˈkasa/` (Castilian); *caza* = *casa* = `/ˈkasa/` (Latin American)  
**IPA notation:** orthographic ⟨z⟩, ⟨ce⟩, ⟨ci⟩ → `[θ]` (Castilian) ~ `[s]` (Latin American)  
**Environment:** Orthographic ⟨z⟩ in all positions and ⟨c⟩ before front vowels ⟨e i⟩; lexically/orthographically conditioned  
**Accents:** both  

### Rule 3: Yeísmo (`/ʎ/` → `/ʝ/` merger)

Near-universal in modern Spanish: the palatal lateral `/ʎ/` (orthographic ⟨ll⟩) has merged with `/ʝ/` (orthographic ⟨y⟩), so *pollo* and *poyo*, *haya* and *halla*, become homophones. Yeísta speakers have no `/ʎ/` phoneme at all. Conservative *lleísmo* — retention of distinct `/ʎ/` — survives only in pockets: parts of the Andes (Bolivia, Paraguay, highland Peru/Ecuador), and a dwindling number of rural Peninsular speakers. The merged `/ʝ/` then feeds further realizational processes (see *rehilamiento*).

**IPA example:** `/ʎ/ → /ʝ/` : *llama* `/ˈʎama/` → `/ˈʝama/`, *pollo* `/ˈpoʎo/` → `/ˈpoʝo/` (= *poyo*)  
**IPA notation:** `/ʎ/ → /ʝ/` (palatal lateral merges into palatal fricative/approximant)  
**Environment:** Orthographic ⟨ll⟩ in all positions; merger is lexicalized, not contextual  
**Accents:** both  

### Rule 4: Nasal place assimilation

A coda nasal assimilates completely to the place of articulation of an immediately following consonant. `/n/` surfaces as: bilabial `[m]` before `/p b m/` (*un beso* `[um ˈβeso]`); labiodental `[ɱ]` before `/f/` (*enfático* `[eɱˈfatiko]`); dental `[n̪]` before `/t d/` (*cuando* `[ˈkwan̪do]`); alveolar `[n]` before `/s/` etc.; palatal/palatalized `[ɲ]` before `/tʃ ʝ/` (*ancho* `[ˈaɲtʃo]`); and velar `[ŋ]` before `/k ɡ x/` (*banco* `[ˈbaŋko]`, *un kilo*). The process is regressive, gradient with speech rate, and applies vigorously across word boundaries. Active in both accents.

**IPA example:** `/n/ → [m ɱ n̪ n ɲ ŋ]` : *un peso* → `[um ˈpeso]`, *enfermo* → `[eɱˈfeɾmo]`, *cantar* → `[kan̪ˈtaɾ]`, *ancho* → `[ˈaɲtʃo]`, *tengo* → `[ˈteŋɡo]`  
**IPA notation:** `N → [αPLACE] / _C[αPLACE] (coda nasal takes place of following consonant)`  
**Environment:** Coda nasal immediately before a consonant, word-internally and across word boundaries  
**Accents:** both  

### Rule 5: `/s/` voicing before voiced consonants

The voiceless alveolar fricative `/s/` is voiced to `[z]` when immediately followed by a voiced consonant, within a word or across a word boundary (*los dedos* → `[loz ˈðeðos]`). The voicing is regressive and largely automatic; it does not create a new phoneme (Spanish has no phonemic `/z/`). Before voiced consonants this is the default in careful and connected speech in both reference accents, though it competes with `/s/`-aspiration in aspirating dialects (see next rule).

**IPA example:** `/s/ → [z]` : *mismo* `/ˈmismo/` → `[ˈmizmo]`, *desde* → `[ˈdezðe]`, *las manos* → `[laz ˈmanos]`, *rasgo* → `[ˈrazɣo]`  
**IPA notation:** `/s/ → [z] / _C[+voice]`  
**Environment:** Coda `/s/` immediately before a voiced consonant, word-internally or across word boundaries  
**Accents:** both  

### Rule 6: Coda `/s/`-aspiration and elision

In a large set of varieties (Caribbean — Cuba, Puerto Rico, Dominican Republic, coastal; Andalusian; Canarian; Rioplatense; much of lowland Latin America), syllable-final `/s/` weakens to a glottal/laryngeal `[h]` and may delete entirely, so *los niños* → `[loh ˈniɲoh]` ~ `[lo ˈniɲo]`. Aspiration is most general before a consonant and at word/utterance end; some speakers preserve `[s]` prevocalically across words. Castilian standard and the conservative Andean/Mexican highland norms RESIST aspiration, keeping a full sibilant. This is one of the most salient isoglosses dividing 'highland/conservative' from 'lowland/innovative' Spanish.

**IPA example:** `/s/ → [h] (~ ∅)` : *estos* `/ˈestos/` → `[ˈehtoh]`, *las casas* → `[lah ˈkasah]`, *más* → `[mah]`  
**IPA notation:** `/s/ → [h] / _{C, #}` (syllable-final); `→ ∅` (further weakening)  
**Environment:** Syllable-final `/s/` (preconsonantal and word/phrase-final); dialect-restricted  
**Accents:** both  

### Rule 7: Sinalefa (cross-word vowel coalescence)

A vowel ending one word coalesces with a vowel beginning the next into a single syllable across the word boundary — the normal Spanish resolution of vowel hiatus in connected speech, and the basis of poetic metre. Identical vowels typically fuse into one (*la alumna* → `[laˈlumna]`); unlike vowels form a diphthong or glide-plus-vowel (*su amigo* → `[swaˈmiɣo]`). Because Spanish resyllabifies freely across words, *sinalefa* keeps utterances vowel-onset-free and is pervasive in both reference accents; its degree depends on speech rate and register.

**IPA example:** `V#V → tautosyllabic` : *la alumna* → `[laˈlumna]`, *mi hijo* → `[ˈmixo]`, *se han ido* → `[seaˈniðo]` ~ `[sjaˈniðo]`  
**IPA notation:** `...Vₐ # Vᵦ... → ...Vₐ.Vᵦ... (across word boundary; → diphthong/single V)`  
**Environment:** Word boundary where one word ends and the next begins in a vowel; connected speech  
**Accents:** both  

### Rule 8: Trill vs. tap distribution

Spanish has a phonemic contrast between the alveolar trill `/r/` and the tap `/ɾ/`, but only intervocalically: *perro* `[ˈpero]` (trill) vs. *pero* `[ˈpeɾo]` (tap), *carro* vs. *caro*. Outside the intervocalic position the two are in complementary distribution: the TRILL appears word-initially (*rosa* `[ˈrosa]`), after heterosyllabic `/n l s/` (*honra* `[ˈonra]`, *alrededor*, *Israel*), and for orthographic ⟨rr⟩; the TAP appears in onset clusters (*tres* `[tɾes]`, *brazo*), syllable-finally/coda (*mar*, *carta*), and elsewhere. Coda rhotics vary freely between tap, trill, approximant and (in some dialects) further weakenings. Active in both accents.

**IPA example:** `/r/` vs. `/ɾ/` : *perro* `/ˈpero/` → `[ˈpero]` (trill) vs. *pero* `/ˈpeɾo/` → `[ˈpeɾo]` (tap); *rosa* → `[ˈrosa]`, *honra* → `[ˈonra]`, *pero caro* → `[ˈkaɾo]`  
**IPA notation:** `[r] / {#__, after n l s, intervocalic ⟨rr⟩}; [ɾ] / elsewhere`  
**Environment:** Trill: word-initial, after `/n l s/`, orthographic ⟨rr⟩, and contrastively intervocalic; tap: clusters, coda, other intervocalic  
**Accents:** both  

### Rule 9: `/x/` realization (`[x]`~`[χ]` vs. `[h]`)

The voiceless dorsal fricative `/x/` (orthographic ⟨j⟩ everywhere and ⟨g⟩ before ⟨e i⟩) has markedly different realizations by region. In Castilian it is a strongly back velar `[x]`, often uvular `[χ]` before back vowels and with notable friction (*jota* `[ˈχota]`). In the Caribbean, much of lowland Latin America, Central America, and Andalusia it weakens to a glottal/pharyngeal `[h]` (*gente* `[ˈhente]`, *mujer* `[muˈheɾ]`). Mexican and other highland Latin American norms keep a clear, less retracted velar `[x]`. The phoneme itself is the same; only its place/manner of realization shifts.

**IPA example:** `/x/ → [x ~ χ ~ h]` : *jamón* `/xaˈmon/` → `[xaˈmon]` ~ `[χaˈmon]` (Castilian) ~ `[haˈmon]` (Caribbean), *gente* → `[ˈxente]` ~ `[ˈhente]`  
**IPA notation:** `/x/ → [χ] / before back V (Castilian); → [x] elsewhere (Castilian); → [h] (Caribbean & much of Latin America)`  
**Environment:** Orthographic ⟨j⟩ in all positions and ⟨g⟩ before ⟨e i⟩; realization is dialect-conditioned  
**Accents:** both  

### Rule 10: Final-`/d/` weakening and elision

Word-final `/d/` (already spirantized to `[ð]`) is highly unstable. In Castilian it commonly fortifies/devoices to `[θ]`, so *Madrid* is `[maˈðɾiθ]` and *usted* `[usˈteθ]` — a famously Madrid-area trait. Across most of Latin America and in casual speech everywhere it instead deletes, giving *Madrid* `[maˈðɾi]`, *verdad* `[beɾˈða]`, *ciudad* `[sjuˈða]`. Both outcomes start from the lenited approximant `[ð]`; the divergence is whether the coda hardens (Castilian) or drops (general Latin American / colloquial).

**IPA example:** `/d/ → [ð] → [θ] ~ ∅` : *Madrid* `/maˈdɾid/` → `[maˈðɾið]` → `[maˈðɾiθ]` ~ `[maˈðɾi]`; *usted* → `[usˈteð]` ~ `[usˈte]`; *verdad* → `[beɾˈða]` ~ `[beɾˈðaθ]`  
**IPA notation:** `/d/ → [ð] (spirantized) → [θ] (Castilian fortition) ~ ∅ / _#`  
**Environment:** Word-final `/d/`, especially phrase-finally; outcome (`[θ]` vs. ∅) is dialect/register conditioned  
**Accents:** both  

### Rule 11: Lateral and nasal dental/palatal assimilation

Like the nasal, the alveolar lateral `/l/` assimilates the place of a following coronal consonant: it dentalizes to `[l̪]` before dental `/t d/` (*alto* `[ˈal̪to]`, *el dedo* `[el̪ ˈðeðo]`) and palatalizes to `[lʲ ~ ʎ]` before palatals `/tʃ ʝ/` (*el chico* `[el̪ʲ ˈtʃiko]`, *el yerno*). Spanish `/l/` is otherwise a clear, non-velarized alveolar `[l]` in all positions — a key difference from English, which darkens coda `/l/` to `[ɫ]`; Spanish has no dark-L. The dental/palatal assimilation is automatic and applies across word boundaries in both accents.

**IPA example:** `/l n/ → [l̪ n̪] / _/t d/ ; [lʲ nʲ] / _/tʃ ʝ/` : *alto* → `[ˈal̪to]`, *caldo* → `[ˈkal̪do]`, *el chico* → `[el̪ʲ ˈtʃiko]`, *cuanto* → `[ˈkwan̪to]`  
**IPA notation:** `/l/ → [l̪] / _C[+dental]; → [lʲ] / _C[+palatal]; (parallel to /n/)`  
**Environment:** Coda `/l/` (and `/n/`) immediately before a dental or palatal consonant, within or across words  
**Accents:** both  

### Rule 12: Rioplatense rehilamiento (`/ʝ/` → `[ʒ ʃ]`)

In Rioplatense Spanish (Buenos Aires, Montevideo and the River Plate region) the yeísta phoneme `/ʝ/` — covering both orthographic ⟨y⟩ and ⟨ll⟩ — is strengthened into a strident postalveolar sibilant: historically voiced `[ʒ]` (*žeísmo*), and over recent decades increasingly devoiced to `[ʃ]` (*šeísmo*), now dominant among younger and female speakers. Thus *yo* is `[ʃo]`, *calle* `[ˈkaʃe]`, *pollo* `[ˈpoʃo]`. This is the most salient phonetic marker of the accent. It is absent from Castilian and from most other Latin American norms, where `/ʝ/` stays a palatal approximant/fricative.

**IPA example:** `/ʝ/ → [ʒ ~ ʃ]` : *yo* `/ʝo/` → `[ʒo]` ~ `[ʃo]`, *lluvia* → `[ˈʒuβja]` ~ `[ˈʃuβja]`, *calle* → `[ˈkaʒe]` ~ `[ˈkaʃe]`  
**IPA notation:** `/ʝ/ → [ʒ] (voiced) → [ʃ] (devoiced, ongoing change) / Rioplatense`  
**Environment:** Orthographic ⟨y⟩ and ⟨ll⟩ (= merged `/ʝ/`) in all positions; Rioplatense varieties only  
**Accents:** Latin American  

### Rule 13: Ceceo (some Andalusian `/s/` → `[θ]`)

The mirror image of *seseo*, found in parts of southern Andalusia (Cádiz, Málaga, much of Granada/Sevilla rural). *Ceceo* merges `/s/` AND `/θ/` into a single (often slightly fronted/dental) fricative `[θ̟]`, so BOTH *casa* and *caza* come out as `[ˈkaθa]`, and *sí* as `[θi]`. Whereas *seseo* collapses the pair onto `[s]`, *ceceo* collapses it onto `[θ]`. It is a regional, socially marked feature of certain Andalusian varieties, not part of either prestige reference norm (Castilian *distinción* keeps the two apart; the Latin American standard uses *seseo*).

**IPA example:** `/s/ → [θ]` : *casa* `/ˈkasa/` → `[ˈkaθa]`, *sí* → `[θi]`, *piscina* → `[piθˈθina]`  
**IPA notation:** `/s/` and `/θ/` both → `[θ̟]` (merger to a dental fricative, opposite of *seseo*)  
**Environment:** Etymological `/s/` (and `/θ/`) in all positions; restricted to *ceceante* Andalusian varieties  
**Accents:** Castilian  

> **Tagging note:** 'Castilian' here denotes Peninsular GEOGRAPHY, not the *distinción* prestige norm — *ceceo* is explicitly NOT *distinción* (it merges `/s/` and `/θ/`, the opposite of the *distinción* contrast) and is the only available tag under the binary Castilian/Latin American vocabulary.

### Rule 14: Voiceless stops unaspirated; intervocalic `/p t k/` lenition

Spanish voiceless stops `/p t k/` are ALWAYS unaspirated, with short-lag voice onset time, in every position — a sharp contrast with English, where syllable-initial stressed `/p t k/` are strongly aspirated `[pʰ tʰ kʰ]`. There is no flapping of intervocalic `/t/` (English *water* `[ˈwɑɾɚ]` has no Spanish analogue: Spanish `/t/` stays `[t]`). Spanish `/t/` is also dental `[t̪]`, not alveolar. In very rapid casual speech the intervocalic voiceless stops may lenite slightly, but the categorical aspiration and tapping of English are absent. Active in both reference accents.

**IPA example:** `/p t k/ → [p t k]` (no aspiration) : *papa* → `[ˈpapa]`, *tomate* → `[toˈmate]`; casual intervocalic voicing *todo* → `[ˈtoðo]` only via `/d/`-spirantization  
**IPA notation:** `/p t k/ → [p t k] (unaspirated, fully voiceless) in all positions`  
**Environment:** `/p t k/` in all positions; categorically unaspirated, `/t/` dental  
**Accents:** both  

### Rule 15: Vowel sequence reduction (no schwa; hiatus → diphthong)

Spanish has NO vowel reduction: every unstressed vowel keeps its full `/a e i o u/` quality (English-style schwa `[ə]` does not exist), so both vowels of *banana* are clear `[a]`. Where two vowels meet within a word, an unstressed high vowel `/i u/` tends to become a glide `[j w]` and form a diphthong with the adjacent vowel (*teatro* → `[ˈtja.tɾo]`, *poeta* → `[ˈpwe.ta]`) in casual speech, while careful speech may keep the hiatus. Stress is lexical and contrastive (*término* / *termino* / *terminó*) and is the only thing distinguishing such triplets — there is no concomitant vowel-quality change. Active in both accents.

**IPA example:** `V.V → glide+V within words` : *teatro* → `[ˈtja.tɾo]`, *poeta* → `[ˈpwe.ta]`; *héroe* → `[ˈe.ɾoe]`; NO unstressed reduction: *banana* → `[baˈnana]`, not `[bəˈnænə]`  
**IPA notation:** unstressed high V → glide `[j w]` before/after another V; mid/low V keep full quality  
**Environment:** Adjacent vowels within a word; unstressed high vowels glide; no reduction of any unstressed vowel  
**Accents:** both  

## Castilian vs. Latin American

Systematic pronunciation differences between the two reference accents of Modern Spanish, expressed in IPA. The two traditions documented in parallel are Castilian (Peninsular / European Standard Castilian), the prestige standard of Spain, and Latin American (general / pan-American standard), the broad reference for the Americas. As with the Eastern (Madnhaya) and Western (Serto) traditions of Syriac, neither accent is intrinsically more correct; they represent two coexisting standardized systems atop a much larger dialect continuum. The single deepest structural division is distinción vs seseo: Castilian distinguishes `/θ/` from `/s/` (caza `/ˈkaθa/` ≠ casa `/ˈkasa/`), whereas Latin American varieties merge them into a single `/s/` (caza = casa = `/ˈkasa/`), reducing the consonant inventory by one phoneme. Phonemic transcriptions use /slashes/ and phonetic detail uses [brackets]. Note that the unstressed vowel system is identical across all Spanish accents — five full vowels `/a e i o u/` with no reduction — so dialect divergence is carried almost entirely by the consonants. Voseo (use of vos for tú) is a grammatical and morphological feature, not a phonological one, and is therefore out of scope here.

### Reference accents

- **Castilian:** Castilian (Peninsular / European Standard Castilian) — has distinción: the phonemic contrast `/θ/` ~ `/s/` (caza `/ˈkaθa/` vs casa `/ˈkasa/`); apical `[s̺]`; velar-to-uvular jota `[x]`~`[χ]`; yeísta in the standard but lleísmo (`/ʎ/`) survives in conservative northern/rural speech; coda `/s/` generally retained as full `[s]` in the central-northern standard.
- **Latin American:** Latin American (general / pan-American standard) — has seseo: `/θ/` is merged into `/s/`, so caza = casa = `/ˈkasa/` and the inventory has no `/θ/`; laminal `[s]`; near-universally yeísta (`/ʎ/` → `/ʝ/`), with lleísmo retained only in conservative Andean and Paraguayan zones; jota and coda `/s/` realizations vary sharply by region (Caribbean `[h]` vs highland `[x]`/`[s]`).

### Differences

| Feature | Castilian IPA | Latin American IPA | Examples | Explanation |
|---|---|---|---|---|
| Distinción vs seseo (the `/θ/` ~ `/s/` contrast) | `/θ/` and `/s/` are two distinct phonemes (distinción) | `/θ/` is absent; ⟨z⟩, ⟨ce⟩, ⟨ci⟩ and ⟨s⟩ all = `/s/` (seseo) | caza ('hunt') / casa ('house'): Castilian `/ˈkaθa/` vs `/ˈkasa/` (contrast) — Latin American `/ˈkasa/` = `/ˈkasa/` (homophones); cielo ('sky'): Castilian `/ˈθjelo/` — Latin American `/ˈsjelo/`; zapato ('shoe'): Castilian `/θaˈpato/` — Latin American `/saˈpato/`; cinco ('five'): Castilian `/ˈθiŋko/` — Latin American `/ˈsiŋko/` | The defining division of the two traditions. Castilian preserves a voiceless dental fricative `/θ/` for orthographic ⟨z⟩ and ⟨c⟩ before ⟨e i⟩, contrasting it with `/s/` (spelled ⟨s⟩). All of Latin America, plus Andalusia and the Canary Islands, merged the two into a single `/s/` (seseo), so caza and casa, cocer and coser are homophones. Seseo removes one phoneme from the inventory (≈18 vs ≈19 consonants, counting `/ʎ/` in the conservative reckoning) and is by far the most consequential, most frequently occurring difference between the accents. |
| Presence vs absence of `/θ/` in the phoneme inventory | `/θ/` present (~19 consonant phonemes in the conservative distinción-lleísta reckoning that also counts `/ʎ/`; ~18 in the more usual yeísta Castilian without `/ʎ/`) | `/θ/` absent (~17 consonant phonemes in the general seseo-yeísta inventory; ~18 only if a lleísta variety retaining `/ʎ/` is assumed) | azul ('blue'): Castilian `/aˈθul/` — Latin American `/aˈsul/`; luz ('light'): Castilian `/luθ/` — Latin American `/lus/`; doce ('twelve'): Castilian `/ˈdoθe/` — Latin American `/ˈdose/`; gracias ('thanks'): Castilian `/ˈɡɾaθjas/` — Latin American `/ˈɡɾasjas/` | A direct structural consequence of distinción vs seseo: Castilian carries `/θ/` as a full member of its fricative series, while general Latin American Spanish simply lacks the segment. This is the cleanest single-phoneme inventory difference between the two standards. For a Latin American speaker, no native word ever requires `/θ/`; for a Castilian speaker, `/θ/` is needed to keep dozens of minimal pairs apart. The dental `[θ]` is articulatorily and auditorily similar to English 'th' in 'think', but it is an independent Spanish phoneme, not a borrowing. |
| Yeísmo (merger of ⟨ll⟩ and ⟨y⟩) vs lleísmo (retention of `/ʎ/`) | Yeísta standard: `/ʎ/` → `/ʝ/`; conservative northern/rural Castilian retains `/ʎ/` (lleísmo) | Near-universally yeísta: `/ʎ/` → `/ʝ/`; lleísmo retained only in Andean highlands and Paraguay | calló ('was silent') / cayó ('fell'): yeísta `/kaˈʝo/` = `/kaˈʝo/` (homophones) — lleísta `/kaˈʎo/` vs `/kaˈʝo/` (contrast); llave ('key'): yeísta `[ˈʝaβe]` — lleísta `[ˈʎaβe]`; pollo ('chicken') / poyo ('stone bench'): yeísta `/ˈpoʝo/` = `/ˈpoʝo/` — lleísta `/ˈpoʎo/` vs `/ˈpoʝo/`; valla ('fence') / vaya ('go-SUBJ'): yeísta `/ˈbaʝa/` = `/ˈbaʝa/` — lleísta `/ˈbaʎa/` vs `/ˈbaʝa/` | Yeísmo — the loss of the palatal lateral `/ʎ/` in favour of the palatal approximant/fricative `/ʝ/` — is now the overwhelming majority pattern in both Spain and Latin America, so ⟨ll⟩ and ⟨y⟩ spell the same sound. The conservative system that keeps them apart (lleísmo, with `/ʎ/`) survives in pockets: in Spain, parts of the rural and northern Peninsula (and Castilian Catalan/Basque-contact zones); in Latin America, the Andean highlands (Bolivia, Peru, Ecuador, highland Colombia) and especially Paraguay, where Guaraní contact reinforces `/ʎ/`. Where lleísmo holds, calló ≠ cayó and pollo ≠ poyo remain distinct. |
| Rioplatense rehilamiento / žeísmo (`/ʝ/` → `[ʒ]` ~ `[ʃ]`) | `/ʝ/` realized as palatal approximant/fricative `[ʝ]` (no rehilamiento) | In Rioplatense (Buenos Aires, Montevideo): `/ʝ/` → strident postalveolar `[ʒ]` (žeísmo) or, increasingly, devoiced `[ʃ]` (sheísmo) | yo ('I'): Castilian `/ʝo/` (`[ʝo]`) — Rioplatense `[ʒo]` ~ `[ʃo]`; calle ('street'): Castilian `/ˈkaʝe/` (`[ˈkaʝe]`) — Rioplatense `[ˈkaʒe]` ~ `[ˈkaʃe]`; lluvia ('rain'): Castilian `[ˈʝuβja]` — Rioplatense `[ˈʒuβja]` ~ `[ˈʃuβja]`; playa ('beach'): Castilian `/ˈplaʝa/` — Rioplatense `[ˈplaʒa]` ~ `[ˈplaʃa]` | In the Río de la Plata region (Argentina and Uruguay) the yeísta merger landed not on `[ʝ]` but on a strident, 'buzzed' postalveolar consonant — historically voiced `[ʒ]` (rehilamiento / žeísmo), as in English 'measure'. Over the 20th century, especially in Buenos Aires and among younger and female speakers, this has devoiced to voiceless `[ʃ]` (sheísmo), so 'yo' is `[ʃo]` and 'calle' is `[ˈkaʃe]`. This is the single most recognizable badge of Porteño Spanish. It is still phonemically `/ʝ/` (yeísta — ⟨ll⟩ and ⟨y⟩ are merged); only the phonetic realization differs. |
| Realization of `/x/` (the jota) | `[x]` velar fricative, backing to uvular `[χ]` before back vowels and in emphatic/northern speech | `[x]` in highland/central varieties; weakened to glottal `[h]` in the Caribbean, coastal, and much of southern/lowland Latin America | jamón ('ham'): Castilian `[xaˈmon]` ~ `[χaˈmon]` — Caribbean `[haˈmon]`; gente ('people'): Castilian `[ˈxente]` — Caribbean `[ˈhente]`; México: Castilian `[ˈmexiko]` — Caribbean/lowland `[ˈmehiko]`; trabajo ('work'): Castilian `[tɾaˈβaxo]` — Caribbean `[tɾaˈβaho]` | The phoneme spelled ⟨j⟩ (and ⟨g⟩ before ⟨e i⟩) is a firm, sometimes raspy velar `[x]` in Castilian, often retracted to a uvular `[χ]` before `/a o u/` or in emphatic northern Peninsular speech. In the Caribbean (Cuba, Puerto Rico, Dominican Republic), coastal Colombia and Venezuela, Central America, and other lowland zones, it lenites to a soft glottal `[h]`, identical to English 'h' in 'hat'. Highland Latin American varieties (Mexico City, the Andes, interior Colombia) keep a clear velar `[x]`. The phoneme is `/x/` everywhere; the difference is purely in place and strength of articulation. |
| Coda `/s/` aspiration and elision | Coda `/s/` retained as full sibilant `[s]` in the central-northern standard (apical `[s̺]`) | Coda `/s/` aspirated to `[h]` (or elided ∅) in the Caribbean, coastal, and lowland varieties; retained as `[s]` in highland varieties | esto ('this'): Castilian (north) `[ˈesto]` — aspirating zones `[ˈehto]`; los libros ('the books'): Castilian `[los ˈliβɾos]` — Caribbean `[loh ˈliβɾoh]` ~ `[lo ˈliβɾo]`; más ('more'): Castilian `[mas]` — Caribbean `[mah]`; España ('Spain'): Castilian `[esˈpaɲa]` — aspirating zones `[ehˈpaɲa]` | In syllable-final and word-final position, `/s/` weakens to an `[h]`-like aspiration, or disappears entirely, across a broad 'lowland' belt: the Caribbean, coastal Mexico and Central America, coastal Colombia and Venezuela, Chile, and the Río de la Plata, as well as Andalusia and the Canary Islands within Spain. Central-northern Castilian and the Latin American highlands (Mexico City, Bogotá, the Andes, highland Guatemala) keep a full `[s]`. Aspiration is among the most socially salient and geographically widespread variables in the language and can affect plural marking (los gatos → `[lo ˈɣato]`). |
| Apical `/s/` (Castilian) vs laminal `/s/` (Latin American) | Apico-alveolar `[s̺]` — tongue tip raised toward the alveolar ridge, giving a 'thick', hushing quality | Lamino-alveolar / dental `[s]` — tongue blade, a 'thinner', more dental-sounding sibilant | sí ('yes'): Castilian `[s̺i]` — Latin American `[si]`; casa ('house'): Castilian `[ˈkas̺a]` — Latin American `[ˈkasa]`; soso ('bland'): Castilian `[ˈs̺os̺o]` — Latin American `[ˈsoso]`; presidente ('president'): Castilian `[pɾes̺iˈðente]` — Latin American `[pɾesiˈðente]` | Even where both accents have a single `/s/`, its articulation differs. Castilian (and most of northern/central Spain) uses an apical `[s̺]`, made with the tongue tip near the alveolar ridge; to non-Castilian ears it can sound faintly like a soft 'sh'. Latin American `/s/` is laminal (and often more fronted/dental), a 'cleaner', higher-pitched sibilant. This apical-vs-laminal split is a constant, low-level cue distinguishing Peninsular from American Spanish that operates independently of seseo. Andalusian seseo/ceceo varieties often use a laminal or dental `/s/` closer to the American type. |
| Ceceo (Andalusian merger of `/s/` into `/θ/`) | Standard Castilian keeps `/s/` and `/θ/` distinct (distinción) | Latin America is seseo (only `/s/`); ceceo does not occur as a standard | casa ('house'): distinción `[ˈkasa]` — ceceo `[ˈkaθa]`; sí ('yes'): distinción `[si]` — ceceo `[θi]`; siesta ('nap'): distinción `[ˈsjesta]` — ceceo `[ˈθjeθta]`; señor ('mister'): distinción `[seˈɲoɾ]` — ceceo `[θeˈɲoɾ]` | Ceceo is the mirror image of seseo, found in parts of western Andalusia (Cádiz, Málaga, rural Seville and Granada): instead of merging `/θ/` into `/s/`, these speakers merge `/s/` into `/θ/`, so casa is `[ˈkaθa]` and sí is `[θi]` — everything is pronounced with the dental fricative. It is a regional Peninsular feature, generally non-prestige and absent from the broadcast standards of either reference accent, but it is phonologically important because it shows the third logically possible outcome of the historical `/s/`~`/θ/` system (alongside distinción and seseo). |
| Realization of coda `/n/` (velarization) | Word-final `/n/` stays alveolar `[n]` (assimilating only to a following consonant's place) | In Caribbean and coastal varieties, word-final `/n/` velarizes to `[ŋ]`, optionally nasalizing the vowel and deleting | pan ('bread'): Castilian `[pan]` — Caribbean `[paŋ]`; bien ('well'): Castilian `[bjen]` — Caribbean `[bjeŋ]`; corazón ('heart'): Castilian `[koɾaˈθon]` — Caribbean `[koɾaˈsoŋ]`; en ('in'): Castilian `[en]` — Caribbean `[eŋ]` | In phrase-final and prepausal position, the central-northern Castilian standard keeps an alveolar `[n]`. Across the Caribbean (Cuba, Puerto Rico, Dominican Republic), coastal Colombia and Venezuela, Central America, and parts of Andalusia, final `/n/` retracts to a velar `[ŋ]` (as in English 'sing'), frequently nasalizing the preceding vowel and sometimes dropping altogether. Velar `[ŋ]` coda is one of the bundle of 'lowland' features that pattern with `/s/`-aspiration and jota-to-`[h]`. |
| Treatment of syllable-final `/ɾ/` and `/l/` (liquids) | Coda `/ɾ/` and `/l/` kept distinct and clearly articulated: tap `[ɾ]` vs lateral `[l]` | In the Caribbean, coda liquids weaken: `/ɾ/`↔`/l/` neutralize (lambdacism/rhotacism), or `/ɾ/` is aspirated, vocalized, or geminated | puerto ('port'): Castilian `[ˈpweɾto]` — Puerto Rican `[ˈpwelto]` (lambdacism); amor ('love'): Castilian `[aˈmoɾ]` — Caribbean `[aˈmol]` ~ `[aˈmo]`; alma ('soul'): Castilian `[ˈalma]` — some Caribbean `[ˈaɾma]` (rhotacism); carne ('meat'): Castilian `[ˈkaɾne]` — Cuban `[ˈkanne]` (gemination) ~ Dominican `[ˈkaɪne]` | Castilian (and the highland Latin American standard) maintains a sharp coda contrast between the tap `/ɾ/` and the lateral `/l/`. In much of the Caribbean these merge or transform in syllable codas: Puerto Rican Spanish famously turns coda `/ɾ/` into `[l]` (lambdacism: 'puerto' → `[ˈpwelto]`), some speakers do the reverse (rhotacism: 'alma' → `[ˈaɾma]`), Cuban Spanish geminates the liquid onto the following consonant (`[ˈkanne]` for 'carne'), and Dominican varieties may vocalize coda `/ɾ/` to a glide `[ɪ]`. None of these affect the phonemic count; they are coda-weakening processes parallel to `/s/`-aspiration. (Note: the trill `/r/` vs tap `/ɾ/` contrast of perro `/ˈpero/` ~ pero `/ˈpeɾo/` is intervocalic and is preserved across all standards.) |

Castilian and Latin American Spanish differ most consequentially in (1) the sibilant system, where distinción (Castilian `/θ/` ~ `/s/`) opposes seseo (a single `/s/` everywhere in the Americas), the one difference that changes the phoneme inventory; (2) the palatal merger, where both are now overwhelmingly yeísta (`/ʎ/` → `/ʝ/`) but conservative Andean/Paraguayan zones keep lleísmo (`/ʎ/`), and Rioplatense pushes the merged `/ʝ/` to strident `[ʒ]`~`[ʃ]` (yo `[ʃo]`, calle `[ˈkaʃe]`); and (3) a bundle of 'lowland' lenition features — coda `/s/`-aspiration to `[h]`, jota `/x/` to glottal `[h]`, final `/n/`-velarization to `[ŋ]`, and Caribbean coda-liquid neutralization — that split the Caribbean/coastal/Andalusian belt from the conservative central-northern Castilian and Latin American highland standards. Lower-level but constant cues include the apical `[s̺]` of Castile vs the laminal `[s]` of the Americas, and the regional Andalusian ceceo (`/s/` → `/θ/`). Throughout, the five-vowel system `/a e i o u/` stays stable and unreduced, so accent identity in Spanish is carried almost entirely by the consonants.

## Orthography: Grapheme–Phoneme Correspondences

Spanish orthography is SHALLOW (transparent) rather than deep: it is among the most phonemic spelling systems of any major world language, approaching a one-to-one grapheme-to-phoneme mapping once a small, fully regular set of context rules is learned. This is the opposite of English and French, whose orthographies are morphophonemic and historically opaque (cf. English 'ough' spelling seven values). In Spanish the reading direction (spelling → sound) is almost perfectly predictable: given the written form, a reader can pronounce a word correctly with near-certainty, because grapheme-to-phoneme is essentially deterministic apart from a handful of context-conditioned letters (c, g, r) and the regional split below. The writing direction (sound → spelling) is slightly less determinate, since a few phonemes have more than one possible spelling (the `/b/` phoneme is written both b and v; the `/x/` phoneme is written j and, before e/i, g; in seseo varieties `/s/` may be written s, z, or soft c; and silent h has no audible cue), which is why these are the classic Spanish spelling-difficulty pairs (b/v, g/j, c/z/s, with/without h). The system uses the 27-letter Latin alphabet (the 26 international letters plus ñ; the former digraph-letters ch and ll were removed from the alphabet in 1994/2010 but the digraphs remain in use), supplemented by the digraphs ch, ll, rr, qu, gu and the diacritics ´ (acute accent) and ¨ (diaeresis). There is NO phonemic vowel length and NO unstressed-vowel reduction: the five vowel letters always spell their five full vowel qualities `/a e i o u/` regardless of stress, a major contrast with English (where unstressed vowels reduce to `/ə/`). Two reference accents are documented in parallel, analogous to the English guide's GA/RP: CASTILIAN (Peninsular / European Standard) which has DISTINCIÓN (the `/θ/` ~ `/s/` contrast: caza `/ˈkaθa/` vs casa `/ˈkasa/`), and LATIN AMERICAN (general / pan-American standard) which has SESEO (`/θ/` merged into `/s/`: caza = casa = `/ˈkasa/`). Both accents share the same orthography; the spelling rules below are identical, only the phonetic value of z and soft c differs by region.

**Reference accents:**

| Label | Accent |
|---|---|
| Castilian | Peninsular / European Standard Castilian — has DISTINCIÓN: phonemic `/θ/` ~ `/s/` contrast (z and soft c = `/θ/`; s = `/s/`). ~19 consonant phonemes (full Castilian, lleísta varieties). `/x/` realised `[x]`~`[χ]`. |
| Latin American | General / pan-American standard — has SESEO: `/θ/` merged into `/s/` (z, soft c and s all = `/s/`). ~17 consonant phonemes (seseo-yeísta). `/x/` often weakened to `[h]` in the Caribbean and much of the Americas. |

### General Principles

Five organising principles govern how letters map to sounds.

- **Near one-to-one transparency:** Most graphemes map to exactly one phoneme in all positions, so reading (spelling → sound) is essentially deterministic. The complexity that exists is RULE-GOVERNED and context-predictable, not lexical/etymological as in English.
  - p → `/p/` always (papa, capa, apto)
  - f → `/f/` always (foco, café)
  - m → `/m/` always (mamá, cama)
  - t → `/t/` always; d → `/d/` always; l → `/l/` always; ch → `/tʃ/` always (chico, mucho); ñ → `/ɲ/` always (niño)
- **Positional conditioning:** A few letters take two values predictable from the FOLLOWING letter (front vs back vowel), exactly mirroring the Romance soft/hard alternation but with no exceptions in native vocabulary. See Soft/Hard Alternation below.
  - c → `/k/` before a, o, u, consonant (casa, coco, cubo, clavo); `/θ/` (Cast.) ~ `/s/` (LatAm) before e, i (cena, cine)
  - g → `/ɡ/` before a, o, u, consonant (gato, gota, gusto, gris); `/x/` before e, i (gente, gigante)
  - r → trill `/r/` word-initially and after n, l, s (rato, honra, alrededor, Israel); tap `/ɾ/` elsewhere (caro, pero, tres)
- **Limited many-to-one:** A small, closed set of phonemes can be spelled more than one way — the only real source of native SPELLING (sound → spelling) ambiguity. This is far more limited than English's pervasive many-to-one mapping.
  - `/b/` ← b (barco) and v (vaca): a complete merger; no phonemic `/v/` in Spanish
  - `/x/` ← j (jamón, caja) and g before e/i (gente, girar)
  - `/k/` ← c before a/o/u (casa), qu before e/i (queso, quiso), k (kilo)
  - `/θ/` (Cast.) ~ `/s/` (LatAm) ← z (zapato, luz) and soft c before e/i (cena, cielo); in seseo also overlaps with s (casa)
  - `/ɡ/` ← g before a/o/u (gato) and gu before e/i (guerra, guiso)
- **Diacritic marks stress only:** The acute accent (´) does NOT change vowel quality; it is a STRESS marker (and a disambiguator in tilde diacrítica pairs). The same vowel letter has the same sound whether or not it bears the accent. This is fundamentally unlike the French acute, which changes vowel quality.
  - á = `/a/` stressed (mamá), a = `/a/` (mapa) — identical quality
  - é = `/e/`, í = `/i/`, ó = `/o/`, ú = `/u/` — accent marks the stressed syllable only
  - Minimal stress triplet, all with `/e/`, `/i/`, `/o/`: término `/ˈteɾmino/` (noun) ~ termino `/teɾˈmino/` (I finish) ~ terminó `/teɾmiˈno/` (he finished)
- **No vowel reduction, no length:** Unstressed vowels keep full quality (no schwa), and there is no phonemic length. Every vowel letter is read at face value in every position. Contrast English 'about' `/əˈbaʊt/` where unstressed a, ou reduce.
  - casa `/ˈkasa/` — both a's are full `[a]`, no reduction of the unstressed one
  - teléfono `/teˈlefono/` — all four o/e vowels keep full quality despite three being unstressed
  - No long/short contrast: vowel duration is allophonic, never lexical

### Consonant Graphemes

Consonant letters and the digraphs ch, ll, rr, qu, gu and their phoneme mappings. Single consonant letters are almost all invariant (one letter, one phoneme). The only context-conditioned letters are c and g (soft/hard, by following vowel), r (trill vs tap, by position), and x (cluster). The hallmark allophonic processes — spirantisation of `/b d ɡ/` to `[β ð ɣ]`, nasal place assimilation, and `/s/`-voicing to `[z]` before voiced consonants — are NOT reflected in spelling and are documented as allophones, not separate graphemes. (`∅` denotes a silent/null realisation.)

#### Single Letters

| Grapheme | IPA | Examples | Note |
|---|---|---|---|
| p | `/p/` | papa; capa; apto | Invariant. Unaspirated `[p]` in all positions (unlike English aspirated initial `[pʰ]`). Silent in a few learned/Greek words historically but standardly pronounced today (psicología may be `[s]`~`[ps]`). |
| b | `/b/` | barco `/b/`; boca `/b/`; haba `[β]` | Merged with v: both spell `/b/`, no `/v/` phoneme. Plosive `[b]` utterance-initially and after a nasal (un beso `[umˈbeso]`); spirantised approximant `[β]` elsewhere, especially intervocalically (haba `[ˈaβa]`). |
| c | `/k/`, `/θ/` (Castilian) ~ `/s/` (Latin American) | casa `/k/`; coco `/k/`; cubo `/k/`; cena `/θ/`~`/s/`; cine `/θ/`~`/s/` | Hard `/k/` before a, o, u and consonants and word-finally; soft `/θ/` (Castilian distinción) ~ `/s/` (Latin American seseo) before e, i. Fully regular — no exceptions. See Soft/Hard Alternation. |
| d | `/d/` | dedo `/d/`; donde `[d]`; nada `[ð]`; Madrid `[ð]`~∅ | Invariant phoneme `/d/`, dental `[d̪]`. Plosive after a pause, nasal, or `/l/` (donde, falda); spirantised approximant `[ð]` elsewhere, especially intervocalically (nada `[ˈnaða]`). Word-final d is weak: `[ð]`, devoiced `[θ]` (Castilian), or dropped (usted, Madrid). |
| f | `/f/` | foco; café; afán | Invariant labiodental `[f]`. No `/v/` contrast (v spells `/b/`, never `/f/`). |
| g | `/ɡ/`, `/x/` | gato `/ɡ/`; gota `/ɡ/`; gusto `/ɡ/`; gente `/x/`; gigante `/x/` | Hard `/ɡ/` before a, o, u and consonants; soft `/x/` before e, i. To keep `/ɡ/` before e/i a silent u is inserted (gu: guerra); to restore the `/w/` in that digraph a diaeresis is used (gü: pingüino). Plosive `[ɡ]` after pause/nasal; spirantised `[ɣ]` elsewhere (lago `[ˈlaɣo]`). See Soft/Hard Alternation. |
| h | `∅` | hola ∅; hijo ∅; ahora ∅; hueso ∅ | ALWAYS SILENT in native and inherited vocabulary — the single most important silent letter in Spanish. Purely etymological/orthographic; never pronounced (cf. hola = ola homophones). Exception: spells `[tʃ]` only as part of the digraph ch, and may be aspirated `[h]`~`[x]` in some loanwords (hámster, hachís) and dialectally (Andalusian/American `[h]` for older `/x/`, e.g. jarana). |
| j | `/x/` | jamón; caja; reloj; jirafa | Invariant `/x/` before any vowel (jamás, jefe, jirafa, joven, julio) — unlike g, which is `/x/` only before e/i. Realised `[x]`~`[χ]` (Castilian, can be strongly uvular), softened to `[h]` in the Caribbean and much of Latin America and in Andalusian. Word-final j is rare and often silent (reloj `[reˈlo]`). |
| k | `/k/` | kilo; koala; kiwi | Rare; confined to loanwords and the metric prefix kilo-. Always `/k/`. Native Spanish writes `/k/` as c (before a/o/u) or qu (before e/i). |
| l | `/l/` | luna; cielo; sol | Invariant alveolar `[l]`; clear (non-velarised) in ALL positions, including codas — Spanish has no 'dark' `[ɫ]` (contrast English 'feel'). Distinct from the digraph ll (separate entry). |
| m | `/m/` | mamá; cama; campo | Invariant `[m]`. Word-final m is rare in native words and tends to be realised `[n]` (álbum `[ˈalβun]`). Written before p/b as part of normal nasal-assimilation spelling (campo, hombre). |
| n | `/n/` | no `/n/`; cana `/n/`; tengo `[ŋ]`; infierno `[ɱ]`; andar `[n̪]` | Phoneme `/n/`, alveolar `[n]` before vowels/pause. Assimilates in place to a following consonant: `[m]` before `/p b m/`, `[ɱ]` before `/f/`, `[n̪]` before `/t d/`, `[n]` before `/s l/`, `[ɲ]` before palatals, `[ŋ]` before velars `/k ɡ x/` (tengo `[ˈteŋɡo]`) and word-finally in much of the Americas (pan `[paŋ]`). |
| ñ | `/ɲ/` | niño; año; España | Dedicated letter (added to the alphabet) for the palatal nasal `/ɲ/`, historically from Latin geminate nn / -gn- (annus → año). Invariant. The tilde over n is part of the letter, not a stress mark. |
| q | `/k/` | queso; quiso; aquí | Occurs ONLY in the digraph qu (= `/k/` before e/i); never written alone, and the u is always silent. See qu and Soft/Hard Alternation. (Loanword 'quórum' with q+u+o is now respelled 'cuórum'.) |
| r | `/r/` (trill), `/ɾ/` (tap) | rato `/r/` (initial); honra `/r/` (after n); alrededor `/r/` (after l); Israel `/r/` (after s); caro `/ɾ/`; pero `/ɾ/`; tres `/ɾ/`; amor `/ɾ/`~`/r/` (final) | Single r is the TAP `/ɾ/` in most positions but the TRILL `/r/` word-initially and after n, l, s (heterosyllabic). The trill/tap CONTRAST is phonemic only between vowels, where it is written rr vs r (perro `/ˈpero/` 'dog' vs pero `/ˈpeɾo/` 'but'). Coda/word-final r is `/ɾ/` and may be tapped, trilled, fricated, or (dialectally) weakened. See rr and the rhotic rule. |
| s | `/s/` | sopa `/s/`; casa `/s/`; mismo `[z]`; los `[s]`~`[h]` | Phoneme `/s/`. Voiced allophone `[z]` before a voiced consonant (mismo `[ˈmizmo]`, desde `[ˈdezðe]`). Castilian s is apico-alveolar `[s̺]`. Coda `/s/` is aspirated to `[h]` or dropped in the Caribbean, coastal Latin America, and Andalusian (los libros `[loh ˈliβɾoh]`). In seseo varieties s also spells the merged `/θ/`~`/s/` phoneme that distinción writes z / soft c. |
| t | `/t/` | té; tomate; atlas | Invariant. Dental, unaspirated `[t̪]` in all positions (contrast English aspirated `[tʰ]`); never flapped intervocalically (unlike American English 'water'). |
| v | `/b/` | vaca `/b/`; vino `/b/`; uva `[β]` | Spells the SAME phoneme as b — there is NO `/v/` in Spanish and no labiodental `[v]` in the standard. Plosive `[b]` utterance-initially and after a nasal (un vaso `[umˈbaso]`); approximant `[β]` elsewhere (uva `[ˈuβa]`). b and v are pronounced identically; their distribution is purely orthographic/etymological (a classic spelling difficulty). |
| w | `/w/`~`/ɡw/`, `/b/` | kiwi `/w/`; web `[w]`~`[ɡw]`; wifi; Wagner `/b/` | Rare; only in loanwords and foreign names. English/general loans → the glide `/w/` (often reinforced to `[ɡw]`: web `[ɡweb]`); Germanic names → `/b/` (Wagner `[ˈbaɡneɾ]`). Not a native grapheme. |
| x | `/ks/`~`[ɣs]`, `/s/`, `/x/` | examen `/ks/`~`[ɣs]`; taxi `/ks/`; extra `/s/` (before consonant); México `/x/`; Xochimilco `[s]` | `/ks/` intervocalically and word-finally (examen, relax), often realised `[ɣs]`~`[s]` in casual speech; reduced to `/s/` before a consonant in many varieties (extra `[ˈestɾa]`). In certain Mexican/Mesoamerican proper names and 'México/mexicano' x retains the archaic value `/x/` (= modern j: México `/ˈmexiko/`); in a few indigenous-origin words it is `[s]` (Xochimilco). A learned-spelling letter; the related sound is otherwise written cs/cc/x only here. |
| y | `/ʝ/` (consonant), `/i/` (vowel) | yo `/ʝ/`; yeso `/ʝ/`; playa `/ʝ/`; y `/i/` (conjunction 'and'); rey `/i̯/` (diphthong); muy `/i̯/` | Consonant `/ʝ/` (palatal approximant/fricative) before a vowel and word-initially (yo, ya, yema, ayer); VOWEL `/i/` when it stands alone as the word 'y' (= 'and') and word-finally after a vowel where it forms the offglide of a diphthong (rey, hoy, muy, soy). Yeísmo makes it merge with ll. Rioplatense rehilamiento strengthens `/ʝ/` to `[ʒ]`~`[ʃ]` (yo `[ʃo]`). After 2010 norms, final-y-as-vowel words are still spelled with y. |
| z | `/θ/` (Castilian) ~ `/s/` (Latin American) | zapato `/θ/`~`/s/`; luz `/θ/`~`/s/`; azúcar `/θ/`~`/s/`; lápiz `/θ/`~`/s/` | `/θ/` in Castilian distinción (interdental `[θ]`, as in English 'thin'); merged to `/s/` in Latin American and Andalusian seseo. Spelled z before a, o, u and word-finally; before e/i the same phoneme is normally written with soft c instead (zapato but cena), so plural/derivation triggers z→c (luz → luces, lápiz → lápices). Voiced `[z̪]`~`[ð]` before a voiced consonant in distinción (juzgar). |

#### Digraphs

| Grapheme | IPA | Examples | Note |
|---|---|---|---|
| ch | `/tʃ/` | chico; mucho; coche | Invariant voiceless postalveolar affricate `/tʃ/`. Formerly counted as a single letter of the alphabet (alphabetised after c) until 1994/2010; still a functional digraph. May be deaffricated to `[ʃ]` in northern Mexican and Andalusian speech (muchacho `[muˈʃaʃo]`). |
| ll | `/ʝ/` (yeísta, majority), `/ʎ/` (lleísta, conservative) | llave `/ʝ/`~`/ʎ/`; calle `/ʝ/`~`/ʎ/`; pollo `/ʝ/`~`/ʎ/` | Historically the palatal lateral `/ʎ/`. YEÍSMO (the merger `/ʎ/` → `/ʝ/`) is now near-universal, so for most speakers ll = y = `/ʝ/` (pollo and poyo are homophones). LLEÍSMO (distinct `/ʎ/`) survives in conservative Andean (Bolivia, Peru highlands), Paraguayan (Guaraní contact), and a few northern-Spanish/Catalan-contact zones. Rioplatense rehilamiento: `/ʝ/` from ll → `[ʒ]`~`[ʃ]` (calle `[ˈkaʃe]`). Formerly a single alphabet letter until 1994/2010. |
| rr | `/r/` (trill) | perro; carro; torre | Always the alveolar TRILL `/r/`. Written only BETWEEN vowels, where it is the marked member of the phonemic trill/tap contrast (perro `/ˈpero/` vs pero `/ˈpeɾo/`; carro vs caro). Never word-initial (initial trill is written single r). When a prefix is joined to an r-initial root, the rhotic is the trill and is written rr (in- + real → irreal, sub- + rayar → subrayar). |
| qu | `/k/` | queso; quiso; aquí; porque | Spells `/k/` before e and i ONLY; the u is ALWAYS silent (que = `/ke/`, qui = `/ki/`). It is the front-vowel counterpart of hard c: casa/coco/cubo use c, but quepo/quiso use qu. Unlike English qu, it is NEVER `/kw/` — the `/kw/` sequence is written cu (cuanto `/ˈkwanto/`, cuestión). See Soft/Hard Alternation. |
| gu | `/ɡ/` (before e, i), `/ɡw/` (before a, o) | guerra `/ɡ/`; guitarra `/ɡ/`; guante `/ɡw/`; antiguo `/ɡw/` | Before e/i the digraph gu = `/ɡ/` with SILENT u (guerra `/ˈɡera/`, guiso) — the front-vowel counterpart of hard g, parallel to qu. Before a/o the same letters are NOT a silent-u digraph: gu = `/ɡw/` with the u pronounced (guante `/ˈɡwante/`). To make the u audible before e/i, a diaeresis is added (gü: see gü). |
| gü | `/ɡw/` | pingüino; vergüenza; lingüística; averigüe | The diaeresis (¨) over u in güe/güi signals that the u IS pronounced as the glide `/w/` — overriding the default 'silent u' of the gu digraph. Thus gue `/ɡe/` (silent u) vs güe `/ɡwe/` (audible u): cigüeña `/θiˈɡweɲa/`~`/siˈɡweɲa/`. The only standard use of the diaeresis in Spanish. |

#### Soft/Hard Alternation of c and g

Inherited from Latin/Romance: the letters c and g have a HARD value (velar plosive) before the back vowels a, o, u and before consonants, and a SOFT value (sibilant/fricative) before the front vowels e, i. Unlike English, the rule is EXCEPTIONLESS in native vocabulary. Spelling devices (qu, gu, silent u; the diaeresis ü) preserve or restore a value across a front/back vowel boundary so the SOUND of a root stays constant even though the LETTER must change.

| Letter | Value | IPA | Environment | Examples |
|---|---|---|---|---|
| c | hard | `/k/` | before a, o, u, a consonant, or word-finally | casa; coco; cubo; clase; frac |
| c | soft | `/θ/` (Castilian) ~ `/s/` (Latin American) | before e, i | cena; cine; cielo; doce; gracias |
| g | hard | `/ɡ/` | before a, o, u, or a consonant | gato; gota; gusto; grande; globo |
| g | soft | `/x/` | before e, i | gente; gigante; general; girar; ágil |

*c: To carry `/k/` into a front-vowel context, spelling switches to qu (saco → saque, busco → busqué). To carry soft `/θ/`~`/s/` into a back-vowel context, spelling switches to z (vez → veces; the reverse z→c happens before e/i).*

*g: Far more regular than English g (which is unpredictable before front vowels). To carry `/ɡ/` into a front-vowel context, spelling switches to gu with silent u (pago → pague, sigo → sigue). To carry soft `/x/` into a back-vowel context, spelling switches to j (cogí → cojo, rige → rijo). Note j can also appear before e/i (jefe, jirafa) where it overlaps with soft g — the only soft-side many-to-one ambiguity.*

Preservation devices that preserve or restore a value across a vowel boundary:

| Device | Function | Examples |
|---|---|---|
| qu before e/i | keeps c hard (`/k/`) before a front vowel; u is silent | que; quiso; saqué (from sacar); busqué (from buscar) |
| silent u after g (gu) before e/i | keeps g hard (`/ɡ/`) before a front vowel; u is silent | guerra; guitarra; pague (from pagar); sigue (from seguir) |
| diaeresis ü (güe/güi) | RESTORES the `/w/` of u after g before e/i (cancels the silent-u convention) | pingüino; vergüenza; averigüé (from averiguar) |
| z → c and c → z spelling switches | keeps the soft `/θ/`~`/s/` phoneme constant across a vowel change (z before a/o/u and finally; c before e/i) | luz → luces; lápiz → lápices; vez → veces; cruz → cruces |
| g → j and j → g spelling switches | keeps the soft `/x/` phoneme constant across a vowel change | coger → cojo; dirigir → dirijo; proteger → protejo |

### Vowel Graphemes

Spanish has a CLEAN 5-vowel system — five letters a, e, i, o, u mapping to exactly five vowel phonemes `/a e i o u/` with no length contrast, no reduction, and no quality change under the accent mark. There are no 'short vs long' or 'checked vs free' alternations (the English magic-e, vowel-digraph, and r-control machinery has NO Spanish analogue). The only structural complications are (1) the acute accent, which marks stress without altering quality, (2) the high vowels i and u becoming the glides `/j/` and `/w/` in diphthongs and triphthongs, and (3) ü as the spelling of the `/w/` glide in güe/güi.

#### Single Vowel Letters

| Grapheme | IPA | Quality | Accented form | Examples | Note |
|---|---|---|---|---|---|
| a | `/a/` | open central `[a]` | á (same `/a/`, marks stress) | casa; mapa; mamá (á stressed); está | Always full open `[a]` in every position, stressed or not — never reduced to schwa. á = a in quality. |
| e | `/e/` | mid front `[e]`~`[e̞]` | é (same `/e/`, marks stress) | pelo; mesa; café (é stressed); bebé | Single mid-front `/e/`; no tense/lax (FACE/DRESS) split, no length. Slightly more open `[ɛ̝]` in closed syllables / before rr in some descriptions, but allophonic. é = e in quality. |
| i | `/i/` (vowel), `/j/` (glide in diphthong) | close front `[i]`; glide `[j]` | í (same `/i/`, marks stress and/or breaks a diphthong = 'hiatus') | isla `/i/`; vivir `/i/`; tiene `/j/` (rising diphthong); país `/i/` (í marks hiatus: pa-ís); día `/i/` (hiatus) | Vowel `/i/` in isolation/nucleus; the GLIDE `/j/` when unstressed and adjacent to another vowel (tiene `/ˈtjene/`, hielo, aire `/ˈai̯ɾe/`). A written accent on í forces it to stay a full vowel and breaks the diphthong (hiato): tía `/ˈti.a/` vs the diphthong in 'pia'. |
| o | `/o/` | mid back rounded `[o]`~`[o̞]` | ó (same `/o/`, marks stress) | oso; todo; habló (ó stressed); rincón | Single mid-back `/o/`; no tense/lax (GOAT/THOUGHT) split, no length, no diphthongisation (contrast English 'go' `/oʊ/`). ó = o in quality. |
| u | `/u/` (vowel), `/w/` (glide in diphthong), `∅` (silent in que/qui/gue/gui) | close back rounded `[u]`; glide `[w]` | ú (same `/u/`, marks stress and/or breaks a diphthong = 'hiatus') | uno `/u/`; luna `/u/`; agua `/w/` (glide); bueno `/w/` (rising diphthong); que ∅ (silent after q); guerra ∅ (silent in gue); baúl `/u/` (ú marks hiatus: ba-úl) | Vowel `/u/` in nucleus; GLIDE `/w/` adjacent to another vowel (agua `/ˈaɡwa/` `[ˈaɣwa]`, bueno `/ˈbweno/`). SILENT after q (always) and in the digraph gu before e/i (que, qui, gue, gui) — but pronounced `/w/` in gua/guo (guante) and when marked with diaeresis in güe/güi. A written accent ú forces a full vowel (hiato): baúl `/baˈul/`. |

#### Diphthongs and Glides

i and u are the only vowels that form glides. A glide + full vowel (or full vowel + glide) within one syllable is a DIPHTHONG; two glides around a vowel form a TRIPHTHONG. There are 14 diphthongs and several triphthongs; all are predictable from spelling. A high vowel adjacent to a low/mid vowel diphthongises by default; an accent on the high vowel breaks the diphthong into a two-syllable HIATUS (hiato).

**Rising diphthongs** — pattern: glide `/j/` or `/w/` + vowel (unstressed i/u first); `/ja je jo ju/` and `/wa we wi wo/`:

| Sequence | Example |
|---|---|
| ia | piano `/ˈpjano/` |
| ie | tierra `/ˈtjera/` |
| io | radio `/ˈradjo/` |
| iu | ciudad `/θjuˈdad/` `[θjuˈðað]` (Cast.) ~ `/sjuˈdad/` `[sjuˈðað]` (LatAm) |
| ua | agua `/ˈaɡwa/` `[ˈaɣwa]` |
| ue | bueno `/ˈbweno/` |
| ui | cuidar `/kwiˈdaɾ/` `[kwiˈðaɾ]` |
| uo | antiguo `/anˈtiɡwo/` `[anˈtiɣwo]` |

**Falling diphthongs** — pattern: vowel + offglide `/i̯/` or `/u̯/` (unstressed i/u second; final glide may be spelled y); `/ai̯ ei̯ oi̯/` (also `au̯ eu̯ ou̯`):

| Sequence | Example |
|---|---|
| ai/ay | aire `/ˈai̯ɾe/`, hay `/ai̯/` |
| ei/ey | peine `/ˈpei̯ne/`, rey `/rei̯/` |
| oi/oy | boina `/ˈboi̯na/`, hoy `/oi̯/` |
| au | causa `/ˈkau̯sa/` |
| eu | deuda `/ˈdeu̯da/` `[ˈdeu̯ða]` |
| ou (rare) | bou `/bou̯/` |

**Triphthongs** — pattern: glide + vowel + glide `/jVi̯/`, `/wVi̯/`:

| Sequence | Example |
|---|---|
| iai | estudiáis `/estuˈdjai̯s/` `[estuˈðjai̯s]` |
| iei | estudiéis `/estuˈdjei̯s/` `[estuˈðjei̯s]` |
| uai/uay | Paraguay `/paɾaˈɡwai̯/` `[paɾaˈɣwai̯]` |
| uei/uey | buey `/bwei̯/` |

**Hiatus via accent:** A written acute accent on an i or u that would otherwise be a glide forces it to be a full syllabic vowel, splitting the would-be diphthong into two syllables (hiato).

| Word | IPA |
|---|---|
| país | `/pa.ˈis/` (vs the diphthong 'pais') |
| día | `/ˈdi.a/` |
| baúl | `/ba.ˈul/` |
| raíz | `/ra.ˈiθ/`~`/ra.ˈis/` |
| reúne | `/re.ˈu.ne/` |

### Silent Letters

Spanish has VERY FEW silent letters — another mark of its shallow orthography. There is no pervasive silent-letter layer as in English (knight, debt, psalm). The IPA column gives the standard pronunciation of the example word. Only h is unconditionally silent; u is silent only in the four fixed digraph contexts; a handful of consonants weaken or drop dialectally.

| Grapheme | Example | IPA | Note |
|---|---|---|---|
| h (always silent) | hola | `/ˈola/` | h is silent in EVERY position — initial (hola, hijo, hueso), medial (ahora `/aˈoɾa/`, almohada), and after a vowel. Homophones result: hola = ola, haya = aya, hecho = echo. The only silent letter that is always silent. |
| h (always silent) | ahora | `/aˈoɾa/` | Medial h does not block a hiatus or create a sound; it is purely orthographic/etymological (Latin/Arabic origin). |
| u (silent in que/qui) | queso | `/ˈkeso/` | u is silent in the digraph qu before e/i (que, qui, quien, aquí). The `/kw/` sound is spelled cu instead (cuanto). |
| u (silent in gue/gui) | guitarra | `/ɡiˈtara/` | u is silent in the digraph gu before e/i (guerra, guiso, sigue) — keeps g hard. Made audible only by the diaeresis (güe/güi: pingüino) or before a/o where gu = `/ɡw/` (guante). |
| consonant clusters (learned, optional) | psicología | `/sikoloˈxia/` ~ `/psikoloˈxia/` | In learned Greek/Latin-origin clusters the first consonant is commonly dropped in speech and increasingly in spelling: ps- (psicología `[s]`~`[ps]`), -mn- (mnemotécnico), gn- (gnomo); these are reductions, not fixed silent letters. RAE has simplified many spellings (psicología/sicología both accepted). |
| final d / coda d (weakened, dialectal) | usted | `/usˈted/` ~ `[usˈteð]` ~ `[usˈte]` | Word-final d is frequently dropped or weakened to `[ð]`~`[θ]` (Madrid, verdad, ciudad). A dialectal/casual reduction, not a true silent letter. |
| final/coda s (aspirated or dropped, dialectal) | los | `/los/` ~ `[loh]` ~ `[lo]` | Coda `/s/` aspirates to `[h]` or drops in the Caribbean, coastal Latin America, and Andalusian (las casas `[lah ˈkasah]`). Regional, not part of the standard orthographic system. |
| final j (often unpronounced) | reloj | `/reˈlox/` ~ `/reˈlo/` | Word-final j (rare) is commonly silent in speech (reloj `[reˈlo]`). Carcaj, boj likewise. |

### Diacritics

Spanish uses only two productive diacritics, neither of which changes a vowel's QUALITY (a key difference from French). The tilde over n (ñ) is treated as part of a distinct letter, not a diacritic.

| Diacritic | Symbol | Function |
|---|---|---|
| Acute accent | ´ (tilde / acento agudo) | Marks the STRESSED syllable; it never alters vowel quality (á=`/a/`, é=`/e/`, í=`/i/`, ó=`/o/`, ú=`/u/`, identical to the unaccented vowels). |
| Diaeresis | ¨ (diéresis / crema) | Placed ONLY over u in the sequences güe and güi to signal that the u is pronounced as the glide `/w/`, overriding the default silent-u of the gu digraph. |
| Tilde over n | ~ over n = ñ | NOT a diacritic on n but the mark that constitutes the separate letter ñ = `/ɲ/`. Always pronounced; never optional. |

#### Acute accent (´) — uses

| Use | Rule | Examples |
|---|---|---|
| stress on irregular position | Written when a word's stress departs from the default rule (default: words ending in vowel/n/s are stressed on the penult; others on the last syllable). | café (oxytone ending in vowel); lápiz (paroxytone ending in z); teléfono (proparoxytone, always marked); rápido |
| breaking a diphthong (hiato) | On i or u it forces a full vowel, splitting a would-be diphthong into two syllables. | día `/ˈdi.a/`; país `/pa.ˈis/`; baúl `/ba.ˈul/` |
| tilde diacrítica (disambiguation) | Distinguishes homophonous monosyllables/words that differ in function but not sound; purely orthographic, no phonetic difference. | tú (you) vs tu (your); él (he) vs el (the); sí (yes) vs si (if); más (more) vs mas (but); sé (I know) vs se (reflexive) |
| stress minimal triplets | Because stress is phonemic, the accent alone can distinguish three words spelled with the same letters. | término `/ˈteɾmino/` vs termino `/teɾˈmino/` vs terminó `/teɾmiˈno/`; ánimo vs animo vs animó; público vs publico vs publicó |

#### Diaeresis (¨) — güe/güi

| Word | IPA |
|---|---|
| pingüino | `/pinˈɡwino/` |
| vergüenza | `/beɾˈɡwenθa/`~`/beɾˈɡwensa/` |
| lingüística | — |
| cigüeña | `/θiˈɡweɲa/`~`/siˈɡweɲa/` |

Contrast gue/gui (silent u, `/ɡe/` `/ɡi/`) with güe/güi (audible u, `/ɡwe/` `/ɡwi/`). This is its only standard function in modern Spanish.

#### Tilde over n (ñ)

| Word | IPA |
|---|---|
| niño | `/ˈniɲo/` |
| año | `/ˈaɲo/` |
| señor | `/seˈɲoɾ/` |

### Allophonic Processes Not Reflected in Spelling

Major phonetic processes that are fully systematic but NEVER reflected in the (shallow) spelling — they are read off the surrounding sounds, not the letters. Documented here as allophones, not as separate graphemes or phonemes. CRITICAL: the spirantised approximants `[β ð ɣ]` are phonetic `[brackets]` only; they are never phonemes.

| Process | Rule | Examples |
|---|---|---|
| spirantisation of `/b d ɡ/` | The voiced stops `/b d ɡ/` (spelled b/v, d, g/gu) are realised as approximants `[β ð ɣ]` everywhere EXCEPT utterance-initially and after a nasal (and, for `/d/`, after `/l/`). The hallmark Spanish process. | haba `[ˈaβa]` vs un beso `[umˈbeso]`; nada `[ˈnaða]` vs donde `[ˈdonde]`; lago `[ˈlaɣo]` vs tengo `[ˈteŋɡo]` |
| nasal place assimilation | `/n/` (and `/m/`) take the place of articulation of a following consonant: `[m ɱ n̪ n ɲ ŋ]`. | un peso `[umˈpeso]`; enfermo `[eɱˈfeɾmo]`; antes `[ˈan̪tes]`; ancho `[ˈaɲtʃo]`; tengo `[ˈteŋɡo]` |
| s-voicing | `/s/` → `[z]` before a voiced consonant. | mismo `[ˈmizmo]`; desde `[ˈdezðe]`; los dedos `[loz ˈðeðos]` |

### Notes

- Spanish orthography is one of the most transparent (shallow) among major world languages: grapheme-to-phoneme correspondence is near one-to-one and almost fully RULE-GOVERNED, so reading aloud from spelling is essentially deterministic — the polar opposite of deep English/French orthography.
- The 27-letter alphabet (26 + ñ), plus the digraphs ch, ll, rr, qu, gu and the diacritics ´ and ¨, suffice with no etymological silent-letter layer. The only always-silent letter is h; u is silent only in the four contexts que, qui, gue, gui.
- The handful of context rules a learner must know: c/g soft before e, i and hard before a, o, u (and the qu/gu/ü devices that preserve a value across a vowel boundary); single r = trill word-initially and after n, l, s but tap elsewhere; the trill/tap contrast is phonemic only between vowels (rr vs r: perro vs pero).
- Spelling ambiguity is limited to a closed set of sound→spelling cases (the source of nearly all native spelling difficulty): b vs v (both `/b/`), j vs soft g (both `/x/`), and — in seseo varieties — s vs z vs soft c (all `/s/`); plus the inaudible h.
- The acute accent is a STRESS marker (and homograph disambiguator), not a vowel-quality change: término / termino / terminó differ only in stress, and á/é/í/ó/ú have the same quality as a/e/i/o/u. The diaeresis ¨ appears only in güe/güi to make u = `/w/`.
- The two reference accents share the SAME spelling; they diverge only in the value of z and soft c: Castilian DISTINCIÓN keeps `/θ/` ~ `/s/` (caza `/ˈkaθa/` vs casa `/ˈkasa/`), while Latin American SESEO merges them to `/s/` (caza = casa = `/ˈkasa/`).
- Further dialect features read off the same spelling: yeísmo (ll = y = `/ʝ/`, near-universal) vs conservative lleísmo (ll = `/ʎ/`, retained in Andean and Paraguayan Spanish); Rioplatense rehilamiento (ll/y → `[ʒ]`~`[ʃ]`, yo `[ʃo]`); `/x/` (j, soft g) as `[x]`~`[χ]` in Castilian vs `[h]` in the Caribbean and much of Latin America; coda `/s/`-aspiration to `[h]` in the Caribbean and Andalusian; weakening of coda/final d and j.
- Crucially, the deep allophonic processes — spirantisation of `/b d ɡ/` to `[β ð ɣ]`, nasal place assimilation, and `/s/` → `[z]` before voiced consonants — are NEVER written. They are predictable from context, so the shallow orthography simply omits them, leaving the reader to apply them automatically.

## Connected Speech & Sinalefa

The segmental processes of connected (running) speech in Modern Spanish, organised around its signature phenomenon: SINALEFA. This is the Spanish analog of the English guide's `weak_forms_and_connected_speech` slot, but the central mechanism is fundamentally different. English reshapes word boundaries by REDUCING unstressed function words to a schwa-centred "weak form"; Spanish has NO weak forms and NO vowel reduction whatsoever — every vowel keeps its full quality in every position. Instead, Spanish smooths the utterance by MERGING vowels across word boundaries into a single syllable (sinalefa), by re-syllabifying word-final consonants as the onset of a following vowel (resilabeo), and by applying the language's pervasive lenition and assimilation rules straight across the word boundary as if the words were one (spirantisation of `/b d ɡ/`, nasal place assimilation, `/s/`-voicing). The result is a continuous vocalic stream broken into syllables that ignore where one word ends and the next begins.

**Applies to:** Spontaneous and fluent connected speech in both reference accents. These processes are the DEFAULT in normal-tempo speech, not optional reductions: sinalefa, resyllabification and spirantisation apply even at moderately careful rates and are obligatory in the metrical scansion of Spanish verse. They are suspended only in very slow, hyper-articulated, or emphatic delivery (e.g. dictation, contrastive correction, or a deliberate pause inserted for rhetorical effect), where a glottal separation (*hiato enfático*) may break an expected sinalefa. Crucially, even when these boundary processes apply, the underlying vowels never change quality or shorten the way English weak-form vowels do.

### Reference Accents

Two reference accents are tracked throughout. Spanish stress is **lexical and contrastive** (marked by the orthographic accent, e.g. *término* / *termino* / *terminó*) and is never deleted or relocated by connected-speech processes.

| Accent | Description |
|---|---|
| **Castilian** | Peninsular / European Standard Castilian. Has DISTINCIÓN: the `/θ/` ~ `/s/` contrast (*caza* `/ˈkaθa/` vs *casa* `/ˈkasa/`). Velar/uvular jota `[x]`~`[χ]`. Generally retains coda `/s/` as `[s]`~`[z]` in the standard. |
| **Latin American** | General / pan-American standard. Has SESEO: `/θ/` merged into `/s/` (*caza* = *casa* = `/ˈkasa/`). Jota typically `[x]`, weakening to `[h]` in the Caribbean and much of the lowlands. Yeísmo is near-universal in both accents; coda `/s/`-aspiration to `[h]` and Rioplatense *rehilamiento* (`/ʝ/` → `[ʒ ʃ]`) are noted as regional variants where relevant. |

### Sinalefa

**Category:** vowel-merging

Two or more vowels that meet across a word boundary are pronounced together within a single syllable rather than in separate syllables (which would be a *hiato*). This is the hallmark of Spanish connected speech and the basis of syllable counting in Spanish metrics.

**Rules.** When a word ends in a vowel and the next begins with a vowel, the vowels fuse into one syllable. Outcomes depend on the vowels:

1. **IDENTICAL vowels** typically fuse into one (often slightly lengthened) vowel: *de Europa* is fine, and *va a hablar* shows `/a/`+`/a/` compression → `[ba.βˈlaɾ]` (phrase-initial `/b/` is a stop after a pause; primary stress on the verb's final syllable `[laɾ]`).
2. A **HIGH unstressed vowel** `/i/` or `/u/` adjacent to another vowel glides to `[j]`/`[w]`, forming a diphthong: *mi alma* → `[ˈmjal.ma]`, *tu hermano* → `[tweɾˈma.no]` (unstressed *tu* joins *her-* into the syllable `[tweɾ]`; primary stress stays on the penult `[ma]` of *hermano*).
3. **NON-HIGH vowel sequences** (`/a e o/`) are pronounced in the same syllable with a smooth transition, the more open or stressed vowel acting as nucleus: *lo he hecho* → `[ˈlo.eˈe.tʃo]` said without a break (both `/e/` kept; primary stress on the `[e]` of HE-cho), *este hombre* → `[ˈes.te.ˈom.bɾe]` (stress on `[es]` of ES-te and on `[om]` of OM-bre).

Orthographic *h* is silent and never blocks sinalefa (*mi hijo* = *mi ijo* → `[ˈmi.xo]`; silent h, and the j is the jota `/x/`, not a glide). Sinalefa freely spans more than two vowels (*a Europa* → three vowels in one syllable).

**Notation:** `...Vˌ#V... → ...V͜V...` (single syllable); `/i,u/` unstressed → `[j,w]` before/after another vowel

| Text | IPA | Note |
|---|---|---|
| mi alma | `[ˈmjal.ma]` | unstressed `/i/` → glide `[j]`, 'mi al-' becomes one syllable `[mjal]` |
| tu hermano | `[tweɾˈma.no]` | silent h; unstressed `/u/` → glide `[w]`; 'tu her-' → `[tweɾ]`; primary stress on the penult `[ma]` of hermano (er-MA-no) |
| lo he hecho | `[ˈlo.eˈe.tʃo]` | two silent h's; `/o/`+`/e/` join in one syllable with no glottal break, but both `/e/` are kept; primary stress on the `[e]` of HE-cho |
| su edad | `[sweˈðað]` | `/u/` → `[w]`: 'su e-' → `[swe]`; 'su' is unstressed, primary stress on final `[ðað]` (e-DAD); final `/d/` spirantised `[ð]` |
| casa amarilla | `[ˈka.sa.ma.ˈɾi.ʝa]` | identical `/a/`+`/a/` fuse to a single `[a]`; yeísta `[ʝ]` |
| va a hablar | `[ba.βˈlaɾ]` | three vowels (`/a/`+`/a/`+`/a/`, h silent) compress; phrase-initial `/b/` of 'va' is a stop `[b]` after a pause; intervocalic `/b/` of 'hablar' → `[β]`; primary stress on the final syllable `[laɾ]` (a-BLAR), not on the auxiliary 'va' |

### Resyllabification

*Resilabeo (consonant-to-vowel liaison)* — **category:** linking

A word-final consonant is re-syllabified as the onset of a following vowel-initial word, so the syllable boundary falls INSIDE the second word and the consonant is heard as belonging to it. Spanish strongly prefers open CV syllables, so this *enchaînement* is automatic and pervasive — the counterpart of English catenation, but without any vowel reduction on either side.

**Rules.** Any word-final consonant before a vowel-initial word becomes that vowel's onset: `C#V → #CV`. This is why *los hombres* is syllabified `[lo.ˈsom.bɾes]` (the `/s/` onsets *-om-*), not `[los.ˈom.bɾes]`. The re-syllabified consonant then undergoes the same allophonic rules it would word-internally: re-syllabified `/s/` before a stressed vowel stays `[s]`; re-syllabified `/n/` links cleanly as an onset; re-syllabified `/b d ɡ/` become intervocalic and spirantise (see next entry).

**Notation:** `...C#V... → ...#CV...` (final C becomes onset of next syllable)

| Text | IPA | Note |
|---|---|---|
| los hombres | `[lo.ˈsom.bɾes]` | `/s/` re-syllabified as onset of '-om-'; silent h |
| un amigo | `[u.ˈna.mi.ɣo]` | `/n/` onsets '-a-'; intervocalic `/ɡ/` → `[ɣ]` |
| el árbol | `[e.ˈlaɾ.βol]` | `/l/` onsets '-ár-'; intervocalic `/b/` → `[β]` |
| dos años | `[do.ˈsa.ɲos]` | `/s/` onsets '-a-'; stays `[s]` before stressed vowel |
| club enorme | `[klu.βe.ˈnoɾ.me]` | final `/b/` re-syllabified AND spirantised intervocalically → `[β]` |

### Cross-word Spirantization / Assimilation

Spanish applies its hallmark lenition and assimilation rules straight across the word boundary, computing the conditioning environment over the whole utterance.

#### Spirantisation across word boundaries

**Category:** lenition

The voiced stops `/b d ɡ/` realise as the approximants `[β̞ ð̞ ɣ̞]` (commonly transcribed `[β ð ɣ]`) when they fall between vowels or after most continuants — and this applies STRAIGHT ACROSS the word boundary, because connected speech treats the boundary as transparent. A `/b d ɡ/` that begins a word will spirantise if the preceding word ends in a vowel (or a non-blocking consonant).

**Rules.** `/b d ɡ/` → `[β ð ɣ]` except (a) after a pause, (b) after a nasal (and, for `/d/`, after `/l/`), where they surface as full stops `[b d ɡ]`. The conditioning environment is computed over the whole utterance, so the SAME word can begin with a stop or an approximant depending on what precedes it: *en Berlín* has `[b]` (after nasal `/n/`) but *a Berlín* has `[β]` (after vowel `/a/`). This is the most audible single signature of native Spanish connected speech.

**Notation:** `/b d ɡ/` → `[β ð ɣ]` / V_ (and after most C across #); → `[b d ɡ]` / N_ , (l)_d , ‖_

| Text | IPA | Note |
|---|---|---|
| la boca | `[la.ˈβo.ka]` | word-initial `/b/` → `[β]` after vowel `/a/` |
| en Berlín | `[em.beɾ.ˈlin]` | `/b/` stays `[b]` after the (assimilated) nasal; contrast next item |
| a Berlín | `[a.βeɾ.ˈlin]` | same word, but `/b/` → `[β]` because the previous word ends in a vowel |
| todo el día | `[ˈto.ðo.el.ˈdi.a]` | intervocalic `/d/` → `[ð]` in 'todo'; '-l d-' keeps `[d]` after `/l/` |
| mi gato | `[mi.ˈɣa.to]` | word-initial `/ɡ/` → `[ɣ]` after vowel `/i/` |
| es de Granada | `[ˈez.ðe.ɣɾa.ˈna.ða]` | `/d/` and `/ɡ/` spirantise across boundaries; `/s/` → `[z]` before voiced `/d/` |

#### Nasal place assimilation across word boundaries

**Category:** assimilation

A word-final nasal `/n/` adopts the place of articulation of the consonant beginning the next word. Spanish has a single archiphonemic coda nasal that is fully assimilated to a following consonant, and the assimilation reaches across the word boundary in connected speech. This is regressive (anticipatory) and obligatory at normal tempo in both accents.

**Rules.** Final `/n/` → `[m]` before bilabials `/p b m/`; → `[ɱ]` before labiodental `/f/`; → `[n̪]` before dentals `/t d/`; → `[n]` before alveolars `/s l r/` and before vowels (where it instead re-syllabifies, see *resilabeo*); → `[ɲ]`~`[nj]` before palatals `/tʃ ʝ/`; → `[ŋ]` before velars `/k ɡ x/`. Before a vowel-initial word the nasal does NOT assimilate but is re-syllabified as a clean onset `[n]`.

**Notation:** `/n/` → `[m ɱ n̪ n ɲ ŋ]` / _#C[αplace]; → `[n]` (onset) / _#V

| Text | IPA | Note |
|---|---|---|
| un peso | `[um.ˈpe.so]` | `/n/` → `[m]` before bilabial `/p/` |
| con fe | `[koɱ.ˈfe]` | `/n/` → `[ɱ]` before labiodental `/f/` |
| un tío | `[un̪.ˈti.o]` | `/n/` → dental `[n̪]` before `/t/` |
| un gato | `[uŋ.ˈɣa.to]` | `/n/` → velar `[ŋ]` before `/ɡ/`; `/ɡ/` also spirantised `[ɣ]` |
| con José | `[koŋ.xo.ˈse]` | `/n/` → `[ŋ]` before velar jota `/x/` (Castilian `[x]`; Caribbean `[h]`) |
| un año | `[u.ˈna.ɲo]` | before a vowel `/n/` does not assimilate but re-syllabifies as onset `[n]` |

#### `/s/`-voicing and coda `/s/` behaviour across word boundaries

**Category:** assimilation

Voiceless `/s/` assimilates the voicing of a following voiced consonant, surfacing as `[z]` before a voiced obstruent or sonorant across the word boundary. In aspirating dialects, coda `/s/` has an entirely different fate (debuccalisation to `[h]` or zero), which interacts with the boundary.

**Rules.** Standard rule: `/s/` → `[z]` before a voiced consonant `/b d ɡ m n l r ʝ/` at the word boundary (*las manos* `[laz.ˈma.nos]`); `/s/` stays `[s]` before a voiceless consonant or a vowel (*los toros* `[los.ˈto.ɾos]`, *los amigos* re-syllabified `[lo.sa.ˈmi.ɣos]`). DIALECT NOTE: in Caribbean, Andalusian and other aspirating varieties, syllable-final `/s/` debuccalises to `[h]` or is deleted — *los dos* → `[loh.ˈðoh]`~`[lo.ˈðo]`; before a vowel the aspiration may persist (*los hombres* → `[loh.ˈom.bɾes]`) or the `/s/` may resist deletion if re-syllabified as an onset, with much regional variation.

**Notation:** `/s/` → `[z]` / _#C[+voice] ; → `[s]` / _#C[-voice] , _#V (onset); DIALECT: `/s/` → `[h]`~∅ / coda (aspirating varieties)

| Text | IPA | Note |
|---|---|---|
| las manos | `[laz.ˈma.nos]` | `/s/` → `[z]` before voiced nasal `/m/` |
| es verdad | `[ˈez.βeɾ.ˈðað]` | `/s/` → `[z]` before voiced `/b/` (also spirantised `[β]`) |
| los toros | `[los.ˈto.ɾos]` | `/s/` stays `[s]` before voiceless `/t/` |
| los amigos | `[lo.sa.ˈmi.ɣos]` | prevocalic `/s/` re-syllabified as onset `[s]`, not voiced |
| los dos (aspirating) | `[loh.ˈðoh]` | Caribbean/Andalusian: coda `/s/` → `[h]`; contrast Castilian `[loz.ˈðos]` |

### No Vowel Reduction

**There is NO schwa and NO vowel reduction in Spanish.** The five vowels `/a e i o u/` keep their full quality whether stressed or unstressed, in citation and in the fastest connected speech alike. This is the single largest contrast with English connected speech: English collapses unstressed function words onto `/ə/`, whereas Spanish function words (prepositions *de, en, con, por*; articles *el, la, los*; conjunctions *y, o, que*; clitic pronouns *me, te, se, lo*) are pronounced with the SAME full vowels in the utterance as in isolation.

What changes across a Spanish word boundary is SYLLABIFICATION and CONSONANT LENITION, not vowel quality. Stress remains lexical and contrastive throughout (*término* / *termino* / *terminó*), and is never deleted or relocated by connected-speech processes; an unstressed full vowel simply stays unstressed and full.

The defining contrast with the English `weak_forms_and_connected_speech` section: English connected speech is driven by VOWEL REDUCTION — unstressed function words collapse onto schwa `/ə/`, syllabic consonants, or zero, and rhythm is stress-timed. Spanish connected speech has NO weak forms, NO schwa, and NO vowel reduction; it is syllable-timed and keeps every vowel full. Where English bridges word boundaries with linking-r, intrusive-r and glide insertion tied to its reduced vowels, Spanish bridges them with sinalefa (vowel coalescence into one syllable) and resilabeo (consonant onset transfer), then applies its hallmark spirantisation of `/b d ɡ/` across the seam. The English "strong vs weak form" distinction has no Spanish counterpart; the nearest Spanish analog is the optional sinalefa↔hiato alternation, which is about syllable grouping, not vowel quality.

The following examples show full unreduced vowels persisting through connected-speech processes:

| Text | IPA | Note |
|---|---|---|
| lo he hecho | `[ˈlo.eˈe.tʃo]` | function word *lo* keeps full `/o/`; both `/e/` kept across the boundary — no reduction |
| su edad | `[sweˈðað]` | clitic *su* keeps its `/u/` (gliding to `[w]`), never centralising to schwa |
| es de Granada | `[ˈez.ðe.ɣɾa.ˈna.ða]` | prepositions *es de* keep full `/e/` vowels; only consonants lenite |
| los amigos | `[lo.sa.ˈmi.ɣos]` | article *los* keeps full `/o/`; `/s/` re-syllabifies, vowels stay full |

### Hiato / Hiatus (the marked absence of sinalefa)

**Category:** vowel-separation

The opposite of sinalefa: two vowels are kept in separate syllables. Across word boundaries *hiato* is the MARKED option, chosen for emphasis, slow tempo, or to disambiguate, and is often reinforced by a light glottal onset `[ʔ]` on the second vowel (*hiato enfático*). It is included here as the boundary against which sinalefa is defined.

**Rules.** An expected sinalefa may be broken (a) for contrastive or emotional emphasis (*¡es a-sombroso!*), (b) in deliberately slow or careful speech, (c) when a heavy stress falls on the second vowel and the speaker reinforces it, or (d) to avoid an unwanted merger that would obscure meaning. The reinforcement is typically a brief glottal stop `[ʔ]` or simply re-articulated separate syllables; the vowels still keep full quality (no reduction). Word-internally, certain spelled vowel sequences are lexically hiatus (e.g. *día* `[ˈdi.a]`, *reírse*), but that is orthographic/lexical, not a connected-speech choice.

**Notation:** `...V#V... → ...V.(ʔ)V...` (two syllables; optional glottal onset on emphatic vowel)

| Text | IPA | Note |
|---|---|---|
| está enojado (emphatic) | `[es.ˈta.ʔe.no.ˈxa.ðo]` | emphatic hiato with glottal onset; cf. neutral sinalefa `[es.ˈta͜e.no.ˈxa.ðo]` |
| lo odio (emphatic) | `[lo.ˈʔo.ðjo]` | glottal reinforcement separates `/o/`+`/o/` for emphasis |
| mi amor (neutral vs emphatic) | `[mja.ˈmoɾ]` ~ `[mi.a.ˈmoɾ]` | neutral sinalefa `[mja-]` vs careful/emphatic hiato `[mi.a-]` |

### Process Ordering

These boundary processes feed one another in cascade across a single utterance. General ordering:

1. **Compute syllabification** over the whole phrase, applying resyllabification and sinalefa so that word boundaries are dissolved into a continuous CV-preferring syllable stream.
2. **On that re-syllabified string apply the allophonic rules** — nasal place assimilation, `/s/`-voicing, and spirantisation of `/b d ɡ/` — using the NEW syllable context, which is why a word-initial `/b d ɡ/` after a vowel-final word spirantises (*a Berlín* `[a.βeɾ.ˈlin]`) while the same word after a pause or nasal keeps its stop (*en Berlín* `[em.beɾ.ˈlin]`).

A single short phrase can show several at once: *es un buen año* → `/s/`-voicing (`[z]` before voiced), nasal assimilation, spirantisation and re-syllabification together → `[e.sum.ˈbwe.ˈna.ɲo]`.

### Rate and Register

Unlike English weak forms, the core Spanish boundary processes (sinalefa, resyllabification, spirantisation, nasal assimilation, `/s/`-voicing) are NOT optional reductions that appear only in fast casual speech — they operate already at careful, formal, and even read-aloud tempos, and sinalefa is presupposed by the syllable counts of traditional Spanish metrics. What slow/emphatic delivery adds is the OPTION to break a sinalefa into an emphatic hiato and to fully re-articulate boundaries; it never introduces vowel reduction. Dialect-specific lenitions (coda `/s/` → `[h]`, jota → `[h]`, *rehilamiento* `/ʝ/` → `[ʒ ʃ]`) do scale with register and region. Citation/dictionary forms give the underlying phonemes; the IPA of running Spanish requires sinalefa, resyllabification and spirantisation to sound native.

### Dialect Variation (Castilian vs Latin American)

Castilian vs Latin American divergences relevant to the boundary:

1. **DISTINCIÓN vs SESEO** — Castilian keeps coda `/θ/` distinct (*la voz* `[la.ˈβoθ]`) where seseante Latin American has `[s]` (`[la.ˈβos]`), which then participates in `/s/`-voicing and aspiration.
2. **Coda `/s/`-ASPIRATION** (`[h]`) and deletion are widespread in the Caribbean, coastal/lowland Latin America and Andalusia, reshaping every `/s/`-final boundary.
3. **JOTA** is velar/uvular `[x]`~`[χ]` in Castilian but weakens to glottal `[h]` in the Caribbean and much of Latin America, affecting the realisation of nasal assimilation before it.
4. **YEÍSMO** (`/ʎ/`→`/ʝ/`) is near-universal, so *con llave* is `[koɲ.ˈʝa.βe]` for most speakers, while conservative Andean/Paraguayan LLEÍSMO keeps `[ʎ]` (`[koɲ.ˈʎa.βe]`).
5. **Rioplatense REHILAMIENTO** realises `/ʝ/` as `[ʒ]`~`[ʃ]` (*la lluvia* `[la.ˈʒu.βja]`~`[la.ˈʃu.βja]`), a postvocalic boundary effect across word edges too.

### Cross-reference

This section is the Spanish counterpart to the English guide's `weak_forms_and_connected_speech`. It draws on and should be read with the Spanish guide's vowel section (the fixed 5-vowel system `/a e i o u/`, no length, no reduction), the consonant-allophone section (spirantisation of `/b d ɡ/` → `[β ð ɣ]`; nasal assimilation; `/s/` → `[z]`), the diphthong/triphthong section (glide formation of `/i u/` → `[j w]`, which is the same mechanism that drives sinalefa), and the dialect section (distinción/seseo, yeísmo/lleísmo, `/s/`-aspiration, jota realisation, rehilamiento). Where the English guide opposes GA vs RP (chiefly over rhoticity), the Spanish guide opposes Castilian vs Latin American (chiefly over distinción/seseo and coda `/s/` behaviour).

## Sample Words in IPA

30 illustrative Spanish words transcribed in IPA for two reference accents — **Castilian** (Peninsular / European Standard, with *distinción*) and **Latin American** (general pan-American standard, with *seseo*) — modeled on the English guide's parallel GA/RP columns and on the Peshitta guide's parallel Eastern/Western tradition columns. The words are chosen to exercise the full segmental system: the complete consonant inventory, the clean five-vowel system /a e i o u/, the trill/tap contrast /r/ ~ /ɾ/, the *distinción*/*seseo* split (/θ/ ~ /s/), the spirantization of /b d ɡ/ to approximants [β ð ɣ], the palatals /ɲ ʝ ʎ/ and *yeísmo*, /x/ realization, diphthongs and a triphthong, lexical stress contrasts, silent orthographic *h*, and the *b*=*v* merger. Each entry lists the phonemes it illustrates so the array as a whole forms a verifiable coverage matrix for the Spanish phonological system.

*Words were selected illustratively (not corpus-sliced) to guarantee complete coverage: collectively they realize every consonant phoneme of the general seseo-yeísta inventory plus the Castilian-only /θ/ and the lleísta-only /ʎ/, supply each of the five vowels in stressed position, demonstrate spirantization of the voiced stops, contrast the trill /r/ with the tap /ɾ/ (perro ~ pero, carro ~ caro), instantiate the palatal nasal /ɲ/ and the ll/y mergers, exhibit the velar/uvular fricative /x/, and contrast lexical stress (término / terminó, papá / papa). Castilian and Latin American transcriptions are given in parallel; where the two reference accents diverge (distinción vs seseo, lleísmo vs yeísmo, /x/ as [x]~[χ] vs [h], Rioplatense rehilamiento, coda /s/-aspiration) both values are shown and the divergence is noted in the per-word gloss.*

*Spanish stress is **lexical and contrastive**: it is not fixed to a particular syllable but distinguishes words, and an orthographic acute accent marks it whenever the position is irregular. The pairs papá /paˈpa/ ('dad') ~ papa /ˈpapa/ ('potato') and término / termino / terminó differ in meaning by stress placement alone. The spirantized voiced-stop allophones [β ð ɣ] are phonetic realizations and are therefore written in [brackets] beside the phonemic /slashes/, never inside them.*

**Total sample words:** 30

| Word | Castilian IPA | Latin American IPA | Gloss | Note | Phonemes illustrated |
|---|---|---|---|---|---|
| cielo | `/ˈθjelo/` | `/ˈsjelo/` | 'sky, heaven' | Distinción vs seseo on c before e/i: Castilian /θ/ ([ˈθjelo]) vs Latin American /s/ ([ˈsjelo]). Rising diphthong /je/ in the stressed syllable. Front vowels /e/ kept at full quality (no reduction). | θ, s, j, e, l, o |
| caza | `/ˈkaθa/` | `/ˈkasa/` | 'hunt' (noun) / 'he-she hunts' | Core distinción minimal pair: Castilian caza /ˈkaθa/ ('hunt') contrasts with casa /ˈkasa/ ('house'); under Latin American seseo the two are HOMOPHONOUS as /ˈkasa/. Voiceless /k/ onset, low vowel /a/ twice at full quality. | k, a, θ, s |
| zapato | `/θaˈpato/` | `/saˈpato/` | 'shoe' | Word-initial z: Castilian /θ/ vs Latin American /s/ (seseo). Voiceless unaspirated stops /p t/ (no aspiration, unlike English). Penultimate stress, all three /a/ at full quality. | θ, s, a, p, t, o |
| gracias | `/ˈɡɾaθjas/` | `/ˈɡɾasjas/` | 'thank you' | Onset cluster /ɡɾ/ with the tap /ɾ/ (a stop+liquid cluster, the commonest Spanish onset cluster type). c before i = /θ/ Castilian vs /s/ Latin American (seseo). Rising diphthong /ja/. Word-initial /ɡ/ is occlusive [ɡ] here after a pause. | ɡ, ɾ, a, θ, s, j, s |
| cinco | `/ˈθinko/ [ˈθiŋko]` | `/ˈsinko/ [ˈsiŋko]` | 'five' | Same word, two onsets within: c before i = /θ/ (Castilian) ~ /s/ (Latin American), then /k/. Phonemically /n/, which assimilates to velar [ŋ] before /k/ — an allophonic, not phonemic, nasal place change, hence the phonetic [ˈθiŋko]/[ˈsiŋko] in brackets beside the phonemic /ˈθinko//ˈsinko/. High front vowel /i/. | θ, s, i, ŋ, k, o |
| gato | `/ˈɡato/` | `/ˈɡato/` | 'cat' | Identical in both accents. Word-initial /ɡ/ is the OCCLUSIVE allophone [ɡ] (after a pause), but the same phoneme spirantizes to approximant [ɣ] intervocalically, e.g. 'el gato' [el ˈɣato] or in 'lago' [ˈlaɣo]. Voiceless unaspirated /t/ medially. Low vowel /a/. | ɡ, a, t, o |
| lobo | `/ˈlobo/ [ˈloβo]` | `/ˈlobo/ [ˈloβo]` | 'wolf' | Identical in both accents. Demonstrates SPIRANTIZATION of /b/: intervocalic /b/ surfaces as the voiced bilabial approximant [β], hence [ˈloβo] not *[ˈlobo]. Lateral /l/ onset (clear in all positions in Spanish). Back vowels /o/ at full quality. | l, o, b, β |
| nada | `/ˈnada/ [ˈnaða]` | `/ˈnada/ [ˈnaða]` | 'nothing' | Identical in both accents. Demonstrates SPIRANTIZATION of /d/: intervocalic /d/ surfaces as the voiced dental approximant [ð], hence [ˈnaða]. (Word-initial /n/ here is alveolar [n]; the /d/ would be occlusive only after a pause, nasal, or /l/.) Low vowel /a/ twice. | n, a, d, ð |
| abogado | `/aboˈɡado/ [aβoˈɣaðo]` | `/aboˈɡado/ [aβoˈɣaðo]` | 'lawyer' | Identical in both accents. A triple-spirantization showcase: all three voiced stops /b ɡ d/ are intervocalic and surface as approximants [β ɣ ð] → [aβoˈɣaðo]. Penultimate stress /ˈɡa/. Full-quality vowels /a o a o/ with NO reduction despite three of four being unstressed. | a, b, β, o, ɡ, ɣ, d, ð |
| perro | `/ˈpero/` | `/ˈpero/` | 'dog' | Identical in both accents. The TRILL /r/ (alveolar trill, orthographic rr between vowels): perro /ˈpero/ 'dog' contrasts minimally with pero /ˈpeɾo/ 'but' — the single phonemic trill~tap opposition of Spanish. Voiceless unaspirated /p/ onset, mid vowels /e o/. | p, e, r, o |
| pero | `/ˈpeɾo/` | `/ˈpeɾo/` | 'but' | Identical in both accents. The TAP /ɾ/ (alveolar tap, single intervocalic r): pero /ˈpeɾo/ 'but' is the minimal-pair counterpart to perro /ˈpero/ 'dog'. Confirms /r/ ~ /ɾ/ as the sole rhotic contrast, neutralized in many other positions. | p, e, ɾ, o |
| carro | `/ˈkaro/` | `/ˈkaro/` | 'car / cart' | Identical in both accents (lexeme aside). A second trill/tap minimal pair: carro /ˈkaro/ ('car') vs caro /ˈkaɾo/ ('expensive'). Reinforces the rr→/r/ trill, r→/ɾ/ tap orthography-to-phoneme mapping. Voiceless /k/ onset. | k, a, r, o |
| rosa | `/ˈrosa/` | `/ˈrosa/` | 'rose / pink' | Identical in both accents. Word-INITIAL r is always the TRILL /r/ in Spanish (never a tap), so rosa = /ˈrosa/. Intervocalic /s/ here may voice to [z] before a voiced consonant in connected speech but stays [s] between vowels. Low and back vowels /o a/. | r, o, s, a |
| España | `/esˈpaɲa/` | `/esˈpaɲa/` | 'Spain' | Identical in both accents. The palatal nasal /ɲ/ (orthographic ñ), a full phoneme distinct from /nj/. Coda /s/ in 'es-' is [s] in careful speech but ASPIRATES to [h] ([ehˈpaɲa]) in Caribbean and Andalusian varieties. Penultimate stress. | e, s, p, a, ɲ |
| niño | `/ˈniɲo/` | `/ˈniɲo/` | 'child, boy' | Identical in both accents. Minimal contrast of alveolar /n/ (onset) with palatal /ɲ/ (medial ñ) within one word: /ˈniɲo/, paralleling 'pena' /ˈpena/ vs 'peña' /ˈpeɲa/. That /ɲ/ ~ /n/ is contrastive (not allophonic) is shown by the classic pair año /ˈaɲo/ ('year') vs ano /ˈano/ ('anus'). High front /i/ and back /o/. | n, i, ɲ, o |
| llave | `/ˈʎabe/ [ˈʎaβe] ~ /ˈʝabe/ [ˈʝaβe]` | `/ˈʝabe/ [ˈʝaβe]` | 'key' | ll/y demonstration. Conservative lleísta speakers (some Andean/Paraguayan, and prescriptive Castilian) keep the palatal lateral /ʎ/: [ˈʎaβe]. The near-universal YEÍSMO merges ll into /ʝ/: [ˈʝaβe]. Note also b=v: the v spells /b/, spirantized intervocalically to [β]. Rioplatense rehilamiento would give [ˈʒaβe]~[ˈʃaβe]. | ʎ, ʝ, a, b, β, e |
| calle | `/ˈkaʎe/ ~ /ˈkaʝe/` | `/ˈkaʝe/` | 'street' | Another ll word: lleísta /ˈkaʎe/ vs the dominant yeísta /ˈkaʝe/. In Rioplatense (Buenos Aires/Montevideo) the merged phoneme is rehilado: [ˈkaʃe] (devoiced) or [ˈkaʒe]. Voiceless /k/ onset, low /a/, front /e/. | k, a, ʎ, ʝ, e |
| yo | `/ʝo/` | `/ʝo/ ~ (Rioplatense) [ʃo]` | 'I' | Word-initial y = /ʝ/ (palatal approximant/fricative) in most varieties. The clearest showcase of Rioplatense REHILAMIENTO: 'yo' is famously [ʃo] (voiceless) or [ʒo] in Buenos Aires. Single back vowel /o/. | ʝ, o |
| pollo | `/ˈpoʎo/ ~ /ˈpoʝo/` | `/ˈpoʝo/` | 'chicken' | ll word that, under yeísmo, becomes HOMOPHONOUS with poyo /ˈpoʝo/ ('stone bench') — the merger's signature consequence. Lleístas keep pollo /ˈpoʎo/ distinct. Voiceless /p/ onset, back /o/ twice. | p, o, ʎ, ʝ |
| jamón | `/xaˈmon/ [χaˈmon]` | `/xaˈmon/ ~ (Caribbean) [haˈmon]` | 'ham' | The /x/ phoneme (orthographic j): in Castilian often a strongly back/uvular [χ]; in much of Latin America a plain velar [x]; in the Caribbean and parts of the Americas a soft glottal [h] ([haˈmon]). Bilabial nasal /m/. Final-syllable stress (acute on ó) with /o/. | x, a, m, o, n |
| mujer | `/muˈxeɾ/ [muˈχeɾ]` | `/muˈxeɾ/ ~ (Caribbean) [muˈheɾ]` | 'woman' | /x/ again (here spelled j before e). Coda r is the TAP /ɾ/ in syllable-final position. High back /u/, mid front /e/. Final stress. In Caribbean speech both the /x/→[h] and possible coda-/ɾ/ weakening surface. | m, u, x, e, ɾ |
| gente | `/ˈxente/ [ˈχente]` | `/ˈxente/ ~ (Caribbean) [ˈhente]` | 'people' | g before e/i is pronounced /x/ (NOT /ɡ/): gente = /ˈxente/. /n/ assimilates to dental [n̪] before the dental /t/. Front vowels /e/ at full quality, penultimate stress. | x, e, n, t |
| México | `/ˈmexiko/ [ˈmeχiko]` | `/ˈmexiko/` | 'Mexico' | Orthographic x here spells /x/ (an archaic spelling preserved in the toponym), NOT /ks/ — so 'México' = /ˈmexiko/, never *[ˈmeksiko]. Antepenultimate (esdrújula) stress, always written with an accent. Showcases the /x/ phoneme with a non-obvious spelling. | m, e, x, i, k, o |
| bueno | `/ˈbweno/` | `/ˈbweno/` | 'good' | Identical in both accents. Rising diphthong /we/ with the labio-velar glide /w/ (ue). Word-initial /b/ is occlusive [b] after a pause. Demonstrates that a glide+vowel forms one syllable. Mid vowels /e o/. | b, w, e, n, o |
| agua | `/ˈaɡwa/ [ˈaɣwa]` | `/ˈaɡwa/ [ˈaɣwa]` | 'water' | Identical in both accents. Rising diphthong /wa/ (ua) with glide /w/; the /ɡ/ before it is intervocalic and SPIRANTIZES to [ɣ] → [ˈaɣwa]. Stress on the first /a/. A diphthong + spirantization two-for-one. | a, ɡ, ɣ, w |
| aire | `/ˈai̯ɾe/` | `/ˈai̯ɾe/` | 'air' | Identical in both accents. FALLING (closing) diphthong /ai̯/ ([ai̯], non-syllabic offglide, equivalently the glide /j/), contrasting with the rising diphthongs above. The non-syllabic breve in the IPA field matches the offglide shown here. Intervocalic single r = the TAP /ɾ/. Three full-quality vowels across two syllables. | a, i, ɾ, e |
| buey | `/ˈbwei̯/` | `/ˈbwei̯/` | 'ox' | Identical in both accents. A monosyllabic TRIPHTHONG /wei̯/ ([ˈbwei̯], glide–vowel–glide): rising onglide /w/ + nucleus /e/ + falling offglide /j/. Compare 'Paraguay' /paɾaˈɡwai̯/ [paɾaˈɣwai̯] with the /wai̯/ triphthong. Word-initial occlusive /b/. (Stress marked here for consistency with other entries, though optional on a monosyllable.) | b, w, e, i |
| papá | `/paˈpa/` | `/paˈpa/` | 'dad' | Identical in both accents. LEXICAL STRESS minimal pair: papá /paˈpa/ ('dad', oxytone, accent written and heard on the final syllable) vs papa /ˈpapa/ ('potato', paroxytone, stress on the first syllable) — two distinct words separated by stress placement ALONE, the segments being identical /papa/. Confirms that Spanish stress is contrastive and orthographically marked with the acute accent. Voiceless unaspirated /p/ twice, full-quality /a/ in both syllables (no reduction of the unstressed one). | p, a |
| huevo | `/ˈuebo/ [ˈweβo]` | `/ˈuebo/ [ˈweβo]` | 'egg' | Identical in both accents. SILENT orthographic h — the h is never pronounced, so 'huevo' begins phonetically with the glide of the diphthong, [ˈweβo], not *[ˈhweβo]; hu- before a vowel spells /we/. Compare other silent-h words hola /ˈola/, ahora /aˈoɾa/. (Incidentally also b=v: the v spells /b/, spirantized intervocalically to [β], giving [ˈweβo].) Rising diphthong /we/ with onglide /w/. | w, e, b, β, o |
| vaca | `/ˈbaka/ [ˈbaka]` | `/ˈbaka/ [ˈbaka]` | 'cow' | Identical in both accents. The clearest b=v demonstration with a v-spelled lexeme distinct from 'llave': orthographic v spells the phoneme /b/ (Spanish has NO /v/), so vaca = /ˈbaka/. After a pause it is occlusive [ˈbaka]; intervocalically (e.g. 'la vaca') it SPIRANTIZES to the approximant [la ˈβaka]. Compare bota /ˈbota/ ('boot'), b-spelled but identical onset /b/. Voiceless /k/ medially, low /a/ twice (full quality, no reduction). | b, β, a, k |

### Source note

Words were selected illustratively (not corpus-sliced) to guarantee complete coverage: collectively they realize every consonant phoneme of the general seseo-yeísta inventory plus the Castilian-only /θ/ and the lleísta-only /ʎ/, supply each of the five vowels in stressed position, demonstrate spirantization of the voiced stops, contrast the trill /r/ with the tap /ɾ/ (perro ~ pero, carro ~ caro), instantiate the palatal nasal /ɲ/ and the ll/y mergers, exhibit the velar/uvular fricative /x/, and contrast lexical stress (término / terminó, papá / papa). Castilian and Latin American transcriptions are given in parallel; where the two reference accents diverge (distinción vs seseo, lleísmo vs yeísmo, /x/ as [x]~[χ] vs [h], Rioplatense rehilamiento, coda /s/-aspiration) both values are shown and the divergence is noted in the per-word gloss.

The voiced stops /b d ɡ/ have two principal allophones in both reference accents: occlusive [b d ɡ] after a pause and after a nasal (and /d/ also after /l/), but approximant [β ð ɣ] elsewhere — most notably intervocalically. This lenition is the hallmark process of Spanish consonantism and is **not** a phonemic contrast, so the approximant allophones are always written phonetically in [brackets] alongside the phonemic /slashes/, as in lobo [ˈloβo], nada [ˈnaða], and abogado [aβoˈɣaðo]. The same note covers *b* = *v*: orthographic *b* and *v* spell the SAME phoneme /b/ (vaca and bota both begin with /b/), so spirantization applies identically regardless of spelling.

## Unicode Reference

Unicode codepoint reference for every IPA symbol, diacritic, and suprasegmental mark used throughout this Spanish pronunciation guide. Each entry gives the symbol, its Unicode codepoint (U+XXXX), decimal value, official Unicode character name, and its IPA phonetic role in Spanish, distinguishing the two reference accents documented in parallel throughout the guide: CASTILIAN (Peninsular / European Standard Castilian, with distinción — the `/θ/`~`/s/` contrast) and LATIN AMERICAN (general pan-American standard, with seseo — `/θ/` merged into `/s/`). All codepoints follow the IPA 2015 revision conventions. Most plain consonants and all five cardinal vowels reuse Basic Latin letters, but the specialized palatals, rhotics, spirantized approximants, and diacritics live in the IPA Extensions, Spacing Modifier Letters, and Combining Diacritical Marks blocks; two symbols (θ and β) are borrowed Greek letters.

### IPA Consonant Symbols

The Spanish consonant phonemes plus key allophonic and dialectal symbols. Spanish has ~17 phonemes in general seseo-yeísta varieties and ~19 in full Castilian (which adds `/θ/`, lleísta varieties add `/ʎ/`). The affricate tʃ is a digraph (no single codepoint). The palatals ɲ ʝ ʎ, the tap ɾ, the velar fricative x, and the postalveolars ʃ ʒ come from the IPA Extensions block; θ is the Greek letter theta. The plain stops `/p b t d k/`, `/f s m n l/`, and the trill `/r/` reuse Basic Latin letters; `/ɡ/` is the single-story script g.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| p | `U+0070` | 112 | LATIN SMALL LETTER P | voiceless bilabial plosive `/p/` (pan); unaspirated in all positions, unlike English — a key contrast for learners |
| b | `U+0062` | 98 | LATIN SMALL LETTER B | voiced bilabial plosive `/b/` (bota, vaca); spelled both 'b' and 'v', which are pronounced identically; spirantizes to [β] in most positions |
| t | `U+0074` | 116 | LATIN SMALL LETTER T | voiceless dental plosive `/t/` (tu); phonetically laminal DENTAL [t̪], not the English alveolar; unaspirated, never flapped |
| d | `U+0064` | 100 | LATIN SMALL LETTER D | voiced dental plosive `/d/` (dar); phonetically dental [d̪]; spirantizes to dental approximant [ð] in most positions and word-finally |
| k | `U+006B` | 107 | LATIN SMALL LETTER K | voiceless velar plosive `/k/` (casa, queso, kilo); unaspirated; spelled 'c' (before a/o/u), 'qu' (before e/i), or 'k' |
| ɡ | `U+0261` | 609 | LATIN SMALL LETTER SCRIPT G | voiced velar plosive `/ɡ/` (gato, guerra); the single-story script g, distinct from Latin small letter g U+0067; spirantizes to [ɣ] in most positions |
| tʃ | — | — | LATIN SMALL LETTER T (U+0074) + LATIN SMALL LETTER ESH (U+0283) (digraph) | voiceless postalveolar affricate `/tʃ/` (chico); the only affricate phoneme of Spanish, spelled 'ch'; the IPA tie-bar ligature t͡ʃ may also be written |
| f | `U+0066` | 102 | LATIN SMALL LETTER F | voiceless labiodental fricative `/f/` (faro) |
| θ | `U+03B8` | 952 | GREEK SMALL LETTER THETA | voiceless (inter)dental fricative `/θ/` — CASTILIAN ONLY, the distinción phoneme (caza `/ˈkaθa/`, cielo, zapato); spelled 'z' or 'c' before e/i; MERGED into `/s/` in Latin American seseo (seseo: caza = casa = `/ˈkasa/`); borrowed Greek letter theta, NOT Latin |
| s | `U+0073` | 115 | LATIN SMALL LETTER S | voiceless alveolar fricative `/s/` (casa, sol); in Castilian phonetically apical [s̺] (apico-alveolar); in seseo varieties also covers what Castilian writes `/θ/`; voices to [z] before voiced consonants; coda `/s/` aspirates to [h] in Caribbean and Andalusian varieties |
| x | `U+0078` | 120 | LATIN SMALL LETTER X | voiceless velar fricative `/x/` (jamón, gente, México); spelled 'j' or 'g' before e/i; realized [x]~[χ] (uvular) in Castilian, but as glottal [h] in the Caribbean and much of Latin America |
| ʝ | `U+029D` | 669 | LATIN SMALL LETTER J WITH CROSSED-TAIL | voiced palatal fricative/approximant `/ʝ/` (yo, llama in yeísmo); the merged phoneme of yeísmo (near-universal `/ʎ/`→`/ʝ/`); spelled 'y' or 'll'; in Rioplatense undergoes rehilamiento to [ʒ]~[ʃ] (yo [ʃo]) |
| ʃ | `U+0283` | 643 | LATIN SMALL LETTER ESH | voiceless postalveolar fricative; the second element of the affricate `/tʃ/` (chico); also the Rioplatense devoiced rehilamiento realization of `/ʝ/` (yo [ʃo], calle [ˈkaʃe]); not an independent phoneme of standard Spanish |
| ʒ | `U+0292` | 658 | LATIN SMALL LETTER EZH | voiced postalveolar fricative; the voiced Rioplatense rehilamiento realization of `/ʝ/` (yo [ʒo]); allophonic/dialectal, not an independent phoneme of standard Spanish |
| m | `U+006D` | 109 | LATIN SMALL LETTER M | voiced bilabial nasal `/m/` (mano); also the assimilated realization of `/n/` before bilabials (un beso [umˈbeso]) |
| n | `U+006E` | 110 | LATIN SMALL LETTER N | voiced alveolar nasal `/n/` (no); assimilates in place to [m ɱ n̪ ɲ ŋ] before a following consonant |
| ɲ | `U+0272` | 626 | LATIN SMALL LETTER N WITH LEFT HOOK | voiced palatal nasal `/ɲ/` (año, niño); spelled 'ñ'; a full phoneme contrasting with `/nj/` in careful speech |
| ŋ | `U+014B` | 331 | LATIN SMALL LETTER ENG | voiced velar nasal [ŋ]; allophone of `/n/` before velars (un gato [uŋˈɡato], blanco); also the realization of word-final `/n/` in many Caribbean and Andean varieties (velarización) |
| ɱ | `U+0271` | 625 | LATIN SMALL LETTER M WITH HOOK | voiced labiodental nasal [ɱ]; allophone of `/n/` before labiodental `/f/` (infierno [iɱˈfjeɾno]); never contrastive |
| l | `U+006C` | 108 | LATIN SMALL LETTER L | voiced alveolar lateral approximant `/l/` (luna); CLEAR [l] in all positions — never the dark/velarized [ɫ] of English coda position |
| ʎ | `U+028E` | 654 | LATIN SMALL LETTER TURNED Y | voiced palatal lateral approximant `/ʎ/` (llave) — LLEÍSTA VARIETIES ONLY (conservative Andean and Paraguayan Spanish); spelled 'll'; merged into `/ʝ/` under near-universal yeísmo |
| r | `U+0072` | 114 | LATIN SMALL LETTER R | voiced alveolar TRILL `/r/` (perro, rojo); a full phoneme contrasting with the tap `/ɾ/` intervocalically (perro `/ˈpero/` vs pero `/ˈpeɾo/`); spelled 'rr', or single 'r' word-initially and after /l n s/ |
| ɾ | `U+027E` | 638 | LATIN SMALL LETTER R WITH FISHHOOK | voiced alveolar TAP/flap `/ɾ/` (pero, caro); contrasts phonemically with the trill `/r/` intervocalically; spelled single 'r' (not word-initial) |
| j | `U+006A` | 106 | LATIN SMALL LETTER J | voiced palatal approximant `/j/` as the on/off-glide of diphthongs and triphthongs (tiene [ˈtjene], hay [ai̯]); NOT the value of orthographic Spanish 'j', which is the velar fricative `/x/` |
| w | `U+0077` | 119 | LATIN SMALL LETTER W | voiced labial-velar approximant `/w/` as the glide of diphthongs and triphthongs (bueno [ˈbweno], causa, agua [ˈaɣwa]) |

### Spirantized Allophones

The hallmark phonological process of Spanish: the voiced stops `/b d ɡ/` are realized as voiced APPROXIMANTS [β ð ɣ] in most positions (notably between vowels and after most consonants), surfacing as true stops only utterance-initially and after a nasal (and `/d/` also after `/l/`). These are ALLOPHONES, not separate phonemes. The strict IPA approximant diacritic [β̞ ð̠˕ ɣ˕] is often omitted by convention; the bare fricative symbols are used here. The symbols β and γ are Greek-derived; ð is a Latin letter.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| β | `U+03B2` | 946 | GREEK SMALL LETTER BETA | voiced bilabial approximant/fricative [β], spirantized allophone of `/b/` (lava [ˈlaβa], la vaca [la ˈβaka]); borrowed Greek letter beta, NOT a Latin letter; strictly the approximant [β̞] |
| ð | `U+00F0` | 240 | LATIN SMALL LETTER ETH | voiced dental approximant/fricative [ð], spirantized allophone of `/d/` (cada [ˈkaða], usted [usˈteð]); Latin letter eth; same symbol as English 'this' but in Spanish it is an allophone of `/d/`, not a phoneme |
| ɣ | `U+0263` | 611 | LATIN SMALL LETTER GAMMA | voiced velar approximant/fricative [ɣ], spirantized allophone of `/ɡ/` (lago [ˈlaɣo], agua [ˈaɣwa]); strictly the approximant [ɣ˕]; distinct from the gamma-like ɤ |

### IPA Vowel Symbols

Spanish has a CLEAN, symmetric five-vowel system `/a e i o u/` with NO phonemic length and NO vowel reduction — unstressed vowels keep their full cardinal quality (a major contrast with English schwa-reduction). There is no schwa `/ə/`. All five monophthongs reuse Basic Latin letters; the glides `/j w/` (also Basic Latin) form rising and falling diphthongs and triphthongs but are not independent vowel qualities.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| a | `U+0061` | 97 | LATIN SMALL LETTER A | open central/front unrounded vowel `/a/` (casa, mapa); a single quality in stressed and unstressed positions alike — never reduced |
| e | `U+0065` | 101 | LATIN SMALL LETTER E | close-mid (to mid) front unrounded vowel `/e/` (mesa, tener); roughly cardinal [e], with a lower [ɛ]-like quality in closed syllables for some speakers; no length or reduction contrast |
| i | `U+0069` | 105 | LATIN SMALL LETTER I | close front unrounded vowel `/i/` (sí, vida); cardinal [i]; the nucleus that yields the glide [j] in diphthongs |
| o | `U+006F` | 111 | LATIN SMALL LETTER O | close-mid (to mid) back rounded vowel `/o/` (todo, sol); roughly cardinal [o]; no length or reduction contrast |
| u | `U+0075` | 117 | LATIN SMALL LETTER U | close back rounded vowel `/u/` (luna, tú); cardinal [u]; silent in the digraphs 'que/qui' and 'gue/gui' (where the diaeresis ü, U+00FC, restores it: pingüino) |
| j | `U+006A` | 106 | LATIN SMALL LETTER J | palatal glide [j] of rising diphthongs/triphthongs derived from `/i/` (tiene [ˈtjene], hielo, estudiáis); as a falling-diphthong off-glide often written with the non-syllabic diacritic [i̯] (aire [ˈai̯ɾe]) |
| w | `U+0077` | 119 | LATIN SMALL LETTER W | labial-velar glide [w] of rising diphthongs/triphthongs derived from `/u/` (bueno [ˈbweno], cuota); as a falling-diphthong off-glide often written with the non-syllabic diacritic [u̯] (causa [ˈkau̯sa]) |

### Diacritics & Suprasegmentals

Marks for stress, place refinement, voicing, and articulator detail. Spanish stress is LEXICAL and contrastive (término / termino / terminó), marked phonetically with the primary-stress vertical line and orthographically with the acute accent. The combining diacritics live in the Combining Diacritical Marks block (U+0300–U+036F) and attach to the preceding base glyph; the stress mark is a spacing modifier letter. There is no length mark (ː) because Spanish has no phonemic vowel length.

| Symbol | Codepoint | Decimal | Name | IPA Role |
|---|---|---|---|---|
| ˈ | `U+02C8` | 712 | MODIFIER LETTER VERTICAL LINE | primary stress mark, placed BEFORE the stressed syllable (camión [kaˈmjon], sábado [ˈsaβaðo]); marks lexically contrastive stress; a spacing modifier letter, NOT the apostrophe U+0027 |
| ◌̪ | `U+032A` | 810 | COMBINING BRIDGE BELOW | dental diacritic, marking the DENTAL articulation of Spanish `/t d/` as [t̪ d̪] (todo [ˈt̪oð̪o]) and the dental assimilation of `/n l/` before `/t d/` (cuando [ˈkwan̪d̪o]); combines below the base letter |
| ◌̥ | `U+0325` | 805 | COMBINING RING BELOW | voiceless diacritic, marking devoicing of a normally voiced sound — e.g. devoiced final approximants or the devoiced Rioplatense rehilamiento [ʃ]; combines below the base letter |
| ◌̬ | `U+032C` | 812 | COMBINING CARON BELOW | voiced diacritic, marking voicing of a normally voiceless sound — e.g. `/s/` voiced to [s̬]≈[z] before a voiced consonant (mismo [ˈmizmo], desde [ˈdezðe]); combines below the base letter |
| ◌̺ | `U+033A` | 826 | COMBINING INVERTED BRIDGE BELOW | apical diacritic, marking the APICAL (apico-alveolar) Castilian `/s/` as [s̺] — its characteristic retracted, [ʃ]-tinged quality, distinct from the laminal/dental `/s/` typical of Latin American varieties; combines below the base letter |
| ◌͡◌ | `U+0361` | 865 | COMBINING DOUBLE INVERTED BREVE | tie bar (affricate ligature), joining the two elements of the affricate `/tʃ/` into [t͡ʃ] (chico [ˈt͡ʃiko]); spans the two base letters; written above; the below-base equivalent is the double breve below U+035C |

### Unicode Blocks Used

The IPA symbols in this Spanish guide are drawn from a small number of Unicode blocks. The cardinal vowels `/a e i o u/`, the glides `/j w/`, and the plain consonants `/p b t d k f s m n l r/` and `/x/` (as letter x) all live in BASIC LATIN (U+0000–U+007F). The specialized palatals, rhotics, and spirantized approximants come from IPA EXTENSIONS (U+0250–U+02AF: ɡ U+0261, ɣ U+0263, ɲ U+0272, ʃ U+0283, ʎ U+028E, ʒ U+0292, ʝ U+029D, ɾ U+027E, ɱ U+0271, plus ŋ U+014B from Latin Extended-A). The stress mark ˈ U+02C8 is in SPACING MODIFIER LETTERS (U+02B0–U+02FF). The dental, voicing, apical, and tie-bar marks are in COMBINING DIACRITICAL MARKS (U+0300–U+036F: bridge below U+032A, ring below U+0325, caron below U+032C, inverted bridge below U+033A, double inverted breve U+0361). Two symbols are borrowed from the GREEK AND COPTIC block (U+0370–U+03FF): theta θ U+03B8 (for Castilian `/θ/`) and beta β U+03B2 (for the spirantized allophone [β]); the velar-fricative variant χ U+03C7 (chi) and the Latin letter eth ð U+00F0 from LATIN-1 SUPPLEMENT also appear.

| Block | Range | Symbols Used |
|---|---|---|
| Basic Latin | U+0000–U+007F | a e i o u j w p b t d k f s m n l r x h z (cardinal vowels, glides, plain consonants, `/x/` as letter x) |
| Latin-1 Supplement | U+0080–U+00FF | ð U+00F0 (eth, spirantized allophone of `/d/`); ü U+00FC (orthographic diaeresis, restores `/u/` in güe/güi) |
| Latin Extended-A | U+0100–U+017F | ŋ U+014B (velar-nasal allophone of `/n/` before velars and word-final velarización) |
| IPA Extensions | U+0250–U+02AF | ɡ U+0261, ɣ U+0263, ɱ U+0271, ɲ U+0272, ɾ U+027E, ʃ U+0283, ʎ U+028E, ʒ U+0292, ʝ U+029D |
| Spacing Modifier Letters | U+02B0–U+02FF | ˈ U+02C8 (primary stress) |
| Combining Diacritical Marks | U+0300–U+036F | ◌̥ U+0325 (voiceless), ◌̪ U+032A (dental), ◌̬ U+032C (voiced), ◌̺ U+033A (apical), ◌͡◌ U+0361 (tie bar) |
| Greek and Coptic | U+0370–U+03FF | θ U+03B8 (theta, Castilian `/θ/`), β U+03B2 (beta, spirantized [β]), χ U+03C7 (chi, uvular variant of `/x/`) |

## Cross-Reference to the Companion Guides

Cross-reference relating this Spanish IPA pronunciation guide to its five companion guides: English, French, and the Semitic three — Classical Syriac (Peshitta), Biblical Aramaic, and Biblical Hebrew. Spanish is an Indo-European, Italic > Romance language and is therefore a genetic SIBLING of French and a more distant Indo-European cousin of Germanic English; it is unrelated to the Afroasiatic Semitic guides. This section documents both the close typological kinship Spanish shares with French (Romance family, lexical—French fixed, syllable-timed rhythm) and English (lexical contrastive stress), and the wider gap to the Semitic family, while noting the shared descriptive apparatus (IPA 2015, phonemic vs phonetic notation, articulatory place/manner/voicing classification) that lets all six guides be read against one another. It is a contrastive bridge, not a uniform claim of relationship: Spanish, French, and English are all Indo-European but in different branches, and the Semitic languages are unrelated to all three; the IPA framework alone is fully shared. Spanish is documented here in TWO parallel reference accents: CASTILIAN (Peninsular / European Standard Castilian, with distinción, the `/θ/`~`/s/` contrast) and LATIN AMERICAN (general pan-American standard, with seseo, `/θ/` merged into `/s/`) — the Spanish analogue of the English guide's GA/RP pairing.

### Shared Framework

All six guides (Spanish, English, French, Peshitta, Biblical Aramaic, Biblical Hebrew) are built on the same descriptive linguistic apparatus, which makes their pronunciation data directly comparable even where the languages are unrelated.

- Primary and sole pronunciation system is the International Phonetic Alphabet (IPA), 2015 revision; spelling/orthography is never the authoritative record.
- Phonemic transcriptions are written between /slashes/; narrow phonetic transcriptions are written between [brackets].
- Consonants are classified by place of articulation, manner of articulation, and voicing (the IPA pulmonic consonant chart).
- Vowels are classified by height, backness, and roundedness (the IPA vowel chart); Spanish, unlike English and the Semitic guides, has NO phonemic length and NO vowel reduction, so quality alone defines its five vowels.
- Suprasegmental marks are shared: `ˈ` primary stress, `ˌ` secondary stress, the syllable break `.`, the tie bar `◌͡◌` for affricates and diphthong glides, and the under-arch for non-syllabic glides `◌̯`.
- Each guide documents two parallel reference traditions of one language: Spanish uses Castilian (distinción) and Latin American (seseo); English uses General American (GA) and Received Pronunciation (RP/SSBE); French uses standard reference (Parisian-based) pronunciation; the Semitic guides use Eastern/Western (Peshitta) or reconstructed reading traditions (e.g. Tiberian for Hebrew and Biblical Aramaic).

Because the framework is identical, an IPA symbol means the same articulatory target in every guide. `/b/`, `/t/`, `/s/`, `/m/` denote the same sounds in Spanish as in English, French, Syriac, Aramaic, or Hebrew; only the phoneme inventories, distributions, allophonic rules (e.g. Spanish spirantization of `/b d ɡ/`), and suprasegmental systems differ.

### Typological Contrasts

| Feature | Spanish | Others (English, French, Semitic) |
|---|---|---|
| Language family | Indo-European > Italic > Romance > Ibero-Romance (West Iberian). Spanish is genetically a sibling of French (both Romance, descended from Latin) and a more distant cousin of Germanic English; it is unrelated to the Semitic languages, though centuries of Andalusi Arabic contact left a large loanword stratum (e.g. almohada, ojalá). | French is Indo-European > Italic > Romance > Gallo-Romance — the closest relative among the companion guides. English is Indo-European > Germanic > West Germanic. Syriac and Biblical Aramaic are Afroasiatic > Semitic > Northwest Semitic (Aramaic branch); Biblical Hebrew is Northwest Semitic (Canaanite branch); the Semitic three are unrelated to Spanish. |
| Lexical vs fixed stress | Stress is LEXICAL and contrastive, like English: minimal triples such as término `[ˈteɾmino]` 'term' / termino `[teɾˈmino]` 'I finish' / terminó `[teɾmiˈno]` 'he finished' differ only in stress placement. Stress is largely predictable from word shape and final segment, and the orthographic acute accent (´) marks every exception, making Spanish stress unusually transparent. | English also has lexical contrastive stress (ˈrecord vs reˈcord), so Spanish patterns WITH English here. French, by contrast, has FIXED phrase-final stress (group-final prominence on the last full syllable of the rhythmic group), not lexical word stress — a major Spanish/French divergence despite their close genetic kinship. In the Semitic guides stress is largely predictable from word structure (typically final or penultimate). |
| Rhythm and timing | Traditionally classed as SYLLABLE-TIMED: syllables recur at roughly equal intervals and there is essentially NO vowel reduction — unstressed vowels keep their full quality. This makes Spanish rhythm pattern WITH French and sharply AGAINST English. | French is likewise syllable-timed, so Spanish and French share this rhythmic profile. English is stress-timed: stressed syllables recur at regular intervals while unstressed vowels compress and reduce pervasively to schwa `/ə/` — a feature Spanish entirely lacks. The Semitic guides are not strongly stress-timed in the English sense, and their reduced vowels (Hebrew/Aramaic shewa) behave differently again. |
| Vowel system size and the absence of reduction | A CLEAN, symmetrical 5-VOWEL system `/a e i o u/` — the SIMPLEST vowel inventory among all six guides. There is NO phonemic length, NO tense/lax contrast, NO nasal vowels, and crucially NO vowel reduction: a vowel has the same quality stressed or unstressed (the o of teléfono is a full `[o]` in every syllable). Spanish builds diphthongs and triphthongs from the glides `/j w/` plus these five vowels (e.g. bien `[bjen]`, cuota `[ˈkwota]`, buey `[bwej]`). | English has a large system (≈11–12 monophthongs plus phonemic diphthongs) with pervasive unstressed reduction to schwa. French has roughly 11–13 oral vowels PLUS phonemic NASAL vowels (`/ɛ̃ ɑ̃ ɔ̃/`, and conservatively `/œ̃/`) and front rounded vowels `/y ø œ/` — none of which exist in Spanish. The Semitic guides have small systems too (Peshitta Eastern 7, Western 5; Tiberian 7) but, unlike Spanish, include a reduced vowel (shewa). Spanish thus has the cleanest, most reduction-free vowel system of the set. |
| Spirantization of voiced stops `/b d ɡ/` | The HALLMARK Spanish allophonic process: the voiced stops `/b d ɡ/` surface as approximants `[β ð ɣ]` in most positions (typically after a continuant — e.g. la barba `[la ˈβaɾβa]`, cada `[ˈkaða]`, lago `[ˈlaɣo]`) and only as full stops `[b d ɡ]` after a pause, after a nasal, and (for `/d/`) after `/l/`. These are ALLOPHONES, not separate phonemes. Castilian and Latin American behave alike here. | This continuous-allophony rule is distinctively Spanish in shape. The Semitic guides have a superficially comparable but historically/structurally distinct alternation — Begadkephat spirantization, where `/b ɡ d k p t/` alternate hard/plosive vs soft/spirantized (`[b]`~`[v]`, `[d]`~`[ð]`, `[ɡ]`~`[ɣ]`, `[p]`~`[f]`, `[t]`~`[θ]`, `[k]`~`[x]`) conditioned by a preceding vowel. English and French have no comparable productive stop-to-approximant lenition of `/b d ɡ/`. |
| Rhotic contrast: trill vs tap | Spanish has a PHONEMIC contrast between the alveolar TRILL `/r/` and the alveolar TAP `/ɾ/`, distinctive intervocalically: perro `[ˈpero]` 'dog' vs pero `[ˈpeɾo]` 'but'; carro vs caro. Both are coronal rhotics; the contrast is one of manner (multiple vs single closure). | The Semitic guides also use a true alveolar trill `/r/` for Resh (Syriac, Biblical Aramaic), with Tiberian Hebrew Resh reconstructed as uvular `/ʁ/` — but they lack the trill~tap PHONEMIC contrast Spanish has. French uses a single uvular rhotic `/ʁ/` (no trill/tap contrast). English `/r/` is a postalveolar/retroflex approximant `[ɹ]`, neither trilled nor tapped (apart from the GA intervocalic flap `[ɾ]` from `/t d/`, which is unrelated to the Spanish rhotic system). The Spanish two-way coronal-rhotic contrast is unique among the six. |
| Orthographic depth (transparency) | VERY shallow / transparent orthography: the grapheme-to-phoneme mapping is highly regular and nearly one-directional from spelling to sound, so a reader who knows the rules and the accent marks can pronounce almost any written word. Residual complications are few (c/z for `/θ~s/`, c/qu for `/k/`, g/gu/gü for `/ɡ/`, silent h, b vs v both `/b/`, the digraphs ch ll rr). This is the SHALLOWEST orthography of the six guides. | English orthography is notoriously DEEP and opaque (through, though, tough, cough; -ough alone has many values). French orthography is also relatively deep: many silent final letters and several spellings per sound (eau/au/o = `/o/`; ent/é/ez/er = `/e/` contexts), though reading direction sound is fairly predictable. The Semitic guides use right-to-left ABJADS that historically encode consonants only, with vowels supplied by optional later pointing (Syriac dots; Tiberian niqqud) — a different kind of under-specification. Spanish stands at the transparent extreme of this whole spectrum. |
| No nasal vowels, no vowel reduction | Spanish has NO nasal vowels: a vowel adjacent to a nasal may be lightly coarticulated but never contrasts as a phonemic nasal vowel. It also has NO vowel reduction (see above). These two absences set Spanish apart from its two Indo-European companions in opposite directions. | French famously HAS phonemic nasal vowels (`/ɛ̃ ɑ̃ ɔ̃/`, conservatively `/œ̃/`), e.g. vin `/vɛ̃/`, blanc `/blɑ̃/`, bon `/bɔ̃/` — a feature wholly absent from Spanish. English HAS pervasive vowel reduction to schwa `/ə/` in unstressed syllables — also absent from Spanish. Thus Spanish lacks the signature French nasalization AND the signature English reduction, keeping all five vowels full and oral in every position. (Spanish nasal consonant `/n/` does assimilate in place to `[m ɱ n̪ ɲ ŋ]`, but this is consonantal, not vocalic, nasalization.) |
| Consonant inventory — guttural and emphatic region | Spanish has NO pharyngeal, pharyngealized (emphatic), or uvular PHONEMES. Its one dorsal fricative `/x/` (jota; e.g. caja, gente) is velar `[x]` (Castilian, often uvular-ish `[χ]`) but reduces to a mere glottal `[h]` in the Caribbean and much of Latin America. There is no phonemic glottal stop. Castilian additionally has the voiceless dental fricative `/θ/` (distinción), which Latin American seseo merges into `/s/`. | The Semitic guides have a rich guttural and emphatic series with no Spanish counterpart: pharyngeals `/ħ/` (Heth) and `/ʕ/` (Ayin), glottals `/ʔ/` (Aleph/Alaph) and `/h/` (He), emphatic `/tˤ/` (Teth) and `/sˤ/` (Tsade), and uvular `/q/` (Qoph). French shares Spanish's lack of pharyngeals/emphatics but, unlike Spanish, uses a uvular rhotic `/ʁ/`. English likewise lacks pharyngeals and emphatics. Spanish `/θ/` (Castilian) does happen to coincide articulatorily with English `/θ/` (thin) and with the spirantized Taw of the Semitic guides, though their sources differ. |
| Morphological type | Fusional/inflecting, like its Indo-European companions: rich verbal inflection for person, number, tense, mood, and aspect realized by concatenated, often portmanteau, suffixes (habl-o, habl-aste, habl-aríamos), with grammatical gender and number agreement on nouns and adjectives. | French and English are likewise Indo-European and concatenative — French strongly fusional like Spanish, English fusional with marked analytic tendencies. The Semitic guides use ROOT-AND-PATTERN (templatic, nonconcatenative) morphology: a discontinuous triconsonantal root (e.g. k-t-b 'write') is interleaved with vowel/consonant templates (binyanim/verbal stems) to yield katab, ktib, maktub — a system with no equivalent in Spanish. |

### Companion Guides

- **Peshitta** — `peshitta_pronunciation_guide.json`. Classical Syriac (Aramaic), the Peshitta reading tradition. Documents Eastern (Madnhaya) and Western (Serto) traditions in parallel, the Begadkephat spirantization rule, guttural and emphatic consonants, and the Syriac abjad (U+0700–U+074F). Unrelated to Spanish (Afroasiatic vs Indo-European), but its Begadkephat lenition offers an instructive contrast to Spanish `/b d ɡ/` spirantization, and several of its plain consonants share IPA symbols with Spanish.
- **Biblical Aramaic** — `biblical_aramaic_pronunciation_guide.json`. Biblical Aramaic / Jewish Literary Aramaic, as preserved in the Tiberian pointing of the Aramaic portions of the Hebrew Bible (Daniel, Ezra). Northwest Semitic (Aramaic branch); uses the Hebrew square abjad with Tiberian niqqud. Shares emphatic/guttural consonants and triconsonantal root morphology with Syriac and Hebrew; unrelated to Spanish.
- **Biblical Hebrew** — `biblical_hebrew_pronunciation_guide.json`. Biblical (Classical) Hebrew in the Tiberian reading tradition. Northwest Semitic (Canaanite branch); uses the Hebrew square abjad with Tiberian niqqud. Notable for the prefixed definite article `/ha-/` with following gemination, the Tiberian uvular Resh `/ʁ/`, and a 7-vowel system with shewa; unrelated to Spanish.
- **English** — `english_pronunciation_guide.json`. Modern English (Indo-European > Germanic), documented in General American (GA) and Received Pronunciation (RP/SSBE). The closest companion to Spanish in STRESS typology — both have lexical, contrastive word stress — but the polar opposite in rhythm (English is stress-timed with pervasive schwa reduction; Spanish is syllable-timed with no reduction) and in vowel-system size and orthographic depth. Useful as the reference for what Spanish's clean 5-vowel system and reduction-free rhythm are NOT.
- **French** — `french_pronunciation_guide.json`. Modern Standard French (Indo-European > Italic > Romance), the closest GENETIC relative of Spanish among the companion guides. Shares Spanish's Romance ancestry and syllable-timed rhythm, but diverges sharply on stress (French has fixed phrase-final stress, not lexical), vowels (French has phonemic nasal vowels `/ɛ̃ ɑ̃ ɔ̃/` and front rounded `/y ø œ/`, all absent in Spanish), and rhotic (French uvular `/ʁ/` vs the Spanish trill/tap contrast). The most instructive same-family comparison in the set.

### Shared IPA Symbols

IPA consonant symbols whose phonetic value is shared between Spanish and one or more of the companion guides, allowing direct cross-reference. The symbol denotes the same articulatory target in every guide; the languages differ in how these phonemes pattern (and, in Spanish, how `/b d ɡ/` spirantize), not in what the symbols mean.

| IPA | Name | Spanish | Others |
|---|---|---|---|
| `p` | voiceless bilabial plosive | `/p/` (pan, capa); UNASPIRATED `[p]` in all positions (no `[pʰ]`, unlike English onset) | English `/p/` (pea), aspirated `[pʰ]` in stressed onset; French `/p/` unaspirated like Spanish; Pe (hard/plosive allophone) in Syriac, Aramaic, Hebrew |
| `b` | voiced bilabial plosive | `/b/` (written b or v: barco, vaca); stop `[b]` after pause/nasal, spirantized approximant `[β]` elsewhere (la vaca `[la ˈβaka]`) | English `/b/` (bee); French `/b/`; Beth (hard/plosive allophone) in Syriac, Aramaic, Hebrew |
| `t` | voiceless dental plosive | `/t/` (tomar); DENTAL `[t̪]` and unaspirated in Spanish (no `[tʰ]`) | English `/t/` (tea), aspirated `[tʰ]` in onset, GA intervocalic flap `[ɾ]`; French dental unaspirated `/t/`; Taw (hard/plosive allophone) in all three Semitic guides (distinct from emphatic Teth `/tˤ/`) |
| `d` | voiced dental plosive | `/d/` (dar); DENTAL `[d̪]`; stop after pause/nasal/l, spirantized approximant `[ð]` elsewhere (cada `[ˈkaða]`) | English `/d/` (do); French dental `/d/`; Daleth (hard/plosive allophone) in all three Semitic guides |
| `k` | voiceless velar plosive | `/k/` (written c, qu, k: casa, queso); unaspirated `[k]` in all positions | English `/k/` (key), aspirated `[kʰ]` in stressed onset; French unaspirated `/k/`; Kaph (hard/plosive allophone) in all three Semitic guides |
| `ɡ` | voiced velar plosive | `/ɡ/` (written g, gu: gato, guerra); stop after pause/nasal, spirantized approximant `[ɣ]` elsewhere (lago `[ˈlaɣo]`) | English `/ɡ/` (go); French `/ɡ/`; Gimel (hard/plosive allophone) in all three Semitic guides |
| `tʃ` | voiceless postalveolar affricate | `/tʃ/` (written ch: mucho, chico); a full phoneme in Spanish | English `/tʃ/` (CHurch); marginal/absent as a primary phoneme in the Semitic guides; French has it only in loanwords |
| `f` | voiceless labiodental fricative | `/f/` (fácil, café) | English `/f/` (fee); French `/f/`; Pe (soft/spirantized allophone, Begadkephat) in the Semitic guides |
| `θ` | voiceless dental fricative | `/θ/` — CASTILIAN ONLY (distinción): written c (before e, i) or z, e.g. caza `[ˈkaθa]` vs casa `[ˈkasa]`. In Latin American seseo this phoneme does NOT exist; it is merged into `/s/`. | English `/θ/` (thin, bath); absent in French; Taw (soft/spirantized allophone) in Syriac, Biblical Aramaic, and Tiberian Hebrew. The symbol's articulatory target is identical even though the sources differ. |
| `s` | voiceless alveolar fricative | `/s/` (casa, sol); Castilian `/s/` is often apico-alveolar `[s̺]`; in seseo it also covers what Castilian spells with c/z. Voices to `[z]` before a voiced consonant (mismo `[ˈmizmo]`); aspirates to `[h]` in coda in Caribbean/Andalusian speech (los `[loh]`). | English `/s/` (see); French `/s/`; Semkath / Samekh / Sin in the Semitic guides (distinct from emphatic Tsade `/sˤ/`) |
| `x` | voiceless velar/uvular fricative | `/x/` (jota; written j, or g before e/i: caja, gente). Velar `[x]` in Castilian (often uvular `[χ]`); weakens to glottal `[h]` in the Caribbean and much of Latin America. | Absent as a phoneme in English and (native) French; corresponds to the spirantized Kaph `[x]` of Syriac, Biblical Aramaic, and Tiberian Hebrew (Begadkephat). The Latin American `[h]` realization coincides with the value of Semitic He / English `/h/`. |
| `ʝ` | voiced palatal fricative/approximant | `/ʝ/` (written y or, under yeísmo, ll: yo, calle). The near-universal yeísta merger of historical `/ʎ/` and `/ʝ/`. Realized `[ʒ]`~`[ʃ]` in Rioplatense (rehilamiento: yo `[ʃo]`). | No exact phonemic counterpart in the other guides; nearest is the palatal approximant `/j/` (see below). French and English `/ʒ/` relate only to the Rioplatense allophone. |
| `m` | voiced bilabial nasal | `/m/` (mano, cama) | English `/m/`; French `/m/`; Mem / Mim in all three Semitic guides |
| `n` | voiced alveolar nasal | `/n/` (no, pan); assimilates in place to `[m ɱ n̪ ɲ ŋ]` before consonants of the matching place (e.g. un peso `[um ˈpeso]`, banco `[ˈbaŋko]`) | English `/n/` (with `[ŋ]` allophone before velars); French `/n/`; Nun in all three Semitic guides |
| `ɲ` | voiced palatal nasal | `/ɲ/` (written ñ: año, niño); a full phoneme | French `/ɲ/` (agneau) — a shared Romance palatal nasal phoneme; English has only the `[ɲ]`-like cluster sequence, not a phoneme; not a primary Semitic phoneme |
| `l` | voiced alveolar lateral approximant | `/l/` (luna, sol); CLEAR `[l]` in all positions (no dark `[ɫ]`, unlike English coda) | English `/l/` with clear `[l]` and dark `[ɫ]` allophones; French clear `/l/`; Lamadh / Lamed in the Semitic guides (clear lateral) |
| `ʎ` | voiced palatal lateral approximant | `/ʎ/` (written ll: calle) — LLEÍSTA varieties only (conservative Andean, Paraguayan, parts of rural Spain). Most speakers are yeísta and merge it into `/ʝ/`. | Marginal/archaic in French (historically the value of -ill-); absent as a phoneme in English; not a primary Semitic phoneme. A distinctively Ibero-Romance segment where retained. |
| `r` | voiced alveolar trill | `/r/` (written rr, or r word-initially/after n,l,s: perro `[ˈpero]`, rosa). Phonemically contrasts with the tap `/ɾ/`. | Resh = alveolar trill `/r/` in Syriac and Biblical Aramaic — the same articulatory target; Tiberian Hebrew Resh is uvular `/ʁ/`; French rhotic is uvular `/ʁ/`; English `/r/` is the approximant `[ɹ]`. Only Spanish (with the Semitic trill) uses a true alveolar trill, and only Spanish contrasts it phonemically with a tap. |
| `ɾ` | voiced alveolar tap | `/ɾ/` (written single r between vowels or in clusters: pero `[ˈpeɾo]`, tres). Phonemically contrasts with the trill `/r/` (pero vs perro). | Occurs in English only as the GA intervocalic ALLOPHONE of `/t d/` (water `[ˈwɔɾɚ]`) — not a phoneme; not a distinct phoneme in French or the Semitic guides. The Spanish tap as an independent phoneme contrasting with a trill is unique to Spanish in this set. |
| `j` | voiced palatal approximant (glide) | `/j/` as the diphthong onglide/offglide (tiene `[ˈtjene]`, rey `[rej]`); distinct from the consonant `/ʝ/` | English `/j/` (yes); French `/j/` (yeux); Yodh / Yud in all three Semitic guides |
| `w` | voiced labial-velar approximant (glide) | `/w/` as the diphthong glide (cuota `[ˈkwota]`, aula `[ˈawla]`) | English `/w/` (we); French `/w/` (oui); Waw / Vav (consonantal value) in the Semitic guides; in some Hebrew traditions realized as `/v/` |

#### Spanish-Only Consonants

Spanish consonant phonemes (or near-phonemes) with no direct counterpart in some companion inventories; chief among these is the trill/tap contrast and the palatals.

- `ɾ` (single-r tap as an independent phoneme contrasting with the trill `/r/` — perro/pero — found nowhere else in the set as a contrastive phoneme)
- `ʝ` (the yeísta palatal fricative/approximant from merged y/ll — no exact phonemic counterpart in the other guides)
- `ʎ` (palatal lateral, lleísta varieties — marginal/absent elsewhere)
- `θ` (Castilian distinción only; shared symbol with English `/θ/` and Semitic spirantized Taw, but absent from Latin American Spanish, French, and the inventory under seseo)

#### Consonants Absent in Spanish

Consonant phonemes prominent in the companion guides that Spanish lacks; these are the principal articulatory targets a Spanish speaker must learn anew for the other languages.

- `v` (voiced labiodental fricative — English/French `/v/` and Semitic spirantized Beth; Spanish spells v but pronounces it `/b/`, so `[v]` is not a Spanish phoneme)
- `z` (voiced alveolar fricative — phoneme in English/French and Semitic Zayin; in Spanish `[z]` is only an allophone of `/s/` before voiced consonants)
- `ʃ` (voiceless postalveolar fricative — English/French phoneme; in Spanish only as a Rioplatense allophone of `/ʝ/`, not a general phoneme)
- `ʒ` (voiced postalveolar fricative — English/French phoneme; in Spanish only a Rioplatense allophone)
- `ʁ` (uvular rhotic — French and Tiberian-Hebrew Resh; absent in Spanish)
- `ħ ʕ` (pharyngeal fricatives — Semitic Heth/Ayin; absent in Spanish)
- `ʔ` (glottal stop — Semitic Aleph/Alaph; not phonemic in Spanish)
- `q` (voiceless uvular plosive — Semitic Qoph; absent in Spanish)
- `tˤ sˤ` (emphatic/pharyngealized stops/fricatives — Semitic Teth/Tsade; absent in Spanish)
- `y ø œ` and the nasal vowels `ɛ̃ ɑ̃ ɔ̃` (French front-rounded and nasal VOWELS — wholly absent from the Spanish vowel system)

> **Note:** Unlike the Semitic guides' cross_reference sections, which trace correspondences within a single language family, this section is doubly contrastive: Spanish shares the IPA description framework with all five companions, is a Romance SIBLING of French and a Germanic cousin of English (both Indo-European), yet is unrelated to the Afroasiatic Semitic three. Its distinctive profile across the set is a clean 5-vowel system with NO length, NO reduction, and NO nasal vowels; LEXICAL contrastive stress (like English, unlike French); SYLLABLE-TIMED rhythm (like French, unlike English); the spirantization of `/b d ɡ/` to `[β ð ɣ]`; a phonemic TRILL `/r/` vs TAP `/ɾ/` contrast; and a VERY shallow, transparent orthography — making Spanish the phonologically simplest and most orthographically transparent member of the six-guide family. Throughout, Castilian (distinción, velar `[x]`) and Latin American (seseo, often glottal `[h]`, near-universal yeísmo) are documented in parallel as the two reference accents.
