# Peshitta Aramaic IPA Pronunciation Guide

**Version:** 3.0.0  
**Date:** 2026-04-01  
**Phase:** Phase 4 (Rebuild of Phase 1)  
**Language:** Classical Syriac (Aramaic) (ISO 639-3: `syc`)  
**Encoding:** UTF-8  
**IPA Standard:** IPA (International Phonetic Alphabet, 2015 revision)  
**Tradition:** Peshitta New Testament (both Eastern/Madnhaya and Western/Serto traditions)  

Machine-readable IPA-based pronunciation guide for Peshitta Syriac Aramaic covering BOTH script systems: Syriac script (Estrangela/Serto, U+0700–U+074F) and Block Aramaic / Hebrew square script (U+0590–U+05FF). All pronunciation data is encoded in the International Phonetic Alphabet (IPA, 2015 revision) as the primary and only system.

### Script Systems

- **Syriac script (Estrangela / Serto / Madnhaya)** — Unicode block `U+0700–U+074F`
- **Block Aramaic (Hebrew square script / Ktav Ashuri)** — Unicode block `U+0590–U+05FF`
  - Same script as Biblical Aramaic and Biblical Hebrew; the language is Syriac Aramaic

### Source Texts

**The complete Peshitta New Testament in four parallel text variants** — 27 books

- `Peshitta/SyriacVersion/` — Consonantal Syriac script
- `Peshitta/SyriacVersion_Vowels/` — Voweled Syriac script with pointing
- `Peshitta/BlockVersion/` — Consonantal Block Aramaic (Hebrew square script)
- `Peshitta/BlockVersion_Vowels/` — Voweled Block Aramaic with niqqud pointing


### Companion Files

- `biblical_aramaic_pronunciation_guide.json`
- `biblical_hebrew_pronunciation_guide.json`

### Notes

- Syriac and Block Aramaic are written right-to-left
- The Peshitta is the standard Syriac Bible translation, used by all Syriac Christian traditions
- Western (Serto) and Eastern (Madnhaya) traditions differ in pronunciation and vowel notation
- Block Aramaic texts use Hebrew-style niqqud vocalization, not Syriac vowel dots
- All IPA transcriptions use the standard 2015 IPA chart notation
- Phonemic transcriptions use / / slashes; phonetic transcriptions use [ ] brackets
- Suprasegmentals: /ː/ marks vowel length; /ˈ/ marks primary stress; /ˤ/ marks pharyngealization
- Syriac Resh = alveolar trill /r/ (NOT uvular /ʁ/ as in Tiberian Hebrew)

## Table of Contents

1. [How to Read IPA](#how-to-read-ipa)
2. [Phonological Inventory](#phonological-inventory)
3. [Consonants](#consonants)
4. [Begadkephat](#begadkephat)
5. [Dagesh System](#dagesh-system)
6. [Vowel Diacritics](#vowel-diacritics)
7. [Shva System](#shva-system)
8. [Hataf Vowels](#hataf-vowels)
9. [Shin-Sin Distinction](#shin-sin-distinction)
10. [Final Form Letters](#final-form-letters)
11. [Consonant-Vowel IPA Matrix](#consonant-vowel-ipa-matrix)
12. [Diacritical Marks](#diacritical-marks)
13. [Suprasegmentals](#suprasegmentals)
14. [Diphthongs](#diphthongs)
15. [Syllable Structure](#syllable-structure)
16. [Phonological Rules](#phonological-rules)
17. [Eastern vs. Western IPA Differences](#eastern-vs-western-ipa-differences)
18. [Vocalization Traditions](#vocalization-traditions)
19. [Cantillation Overview](#cantillation-overview)
20. [Cross-Reference: Aramaic and Hebrew](#cross-reference-aramaic-and-hebrew)
21. [Sample Words — IPA Transcriptions](#sample-words-ipa-transcriptions)
22. [Unicode Reference](#unicode-reference)
23. [Numerical Values](#numerical-values)

## How to Read IPA

This guide uses the **International Phonetic Alphabet (IPA, 2015 revision)** as the sole pronunciation system. No English approximations are provided — this is by design, to preserve scientific accuracy and cross-linguistic neutrality.

IPA conventions used throughout this document:

- **/ /** (slashes) enclose *phonemic* transcriptions — the abstract sound categories of the language
- **[ ]** (square brackets) enclose *phonetic* transcriptions — the actual pronunciation in a specific tradition
- **ˈ** before a syllable marks *primary stress*
- **ː** after a vowel or consonant marks *length* (long sound)
- **ˤ** after a consonant marks *pharyngealization* (emphatic articulation)

For a full IPA chart with audio examples, see the [official IPA chart](https://www.internationalphoneticassociation.org/content/ipa-chart).

---

## Phonological Inventory

The complete phonemic inventory of Classical Syriac as used in the Peshitta, organized by IPA categories. Shared across both script systems.

### Consonant Phonemes

All consonant phonemes of Classical Syriac arranged by place and manner of articulation

**Total consonant phonemes:** 31  
22 letters yield 31 distinct phonemes: 16 non-Begadkephat consonants + 6 Begadkephat hard (plosive) + 6 Begadkephat soft (fricative) + labial-velar /w/ + palatal /j/ = 31

#### IPA Consonant Chart

IPA consonant chart for Classical Syriac (rows = manner, columns = place). Voiceless precedes voiced in each cell.

| Manner | Bilabial | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|---|---|---|---|---|---|---|---|---|---|
| Plosive | p b |  | t d tˤ |  |  | k ɡ | q |  | ʔ |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Fricative | ɸ β | θ ð | s z sˤ | ʃ |  | x ɣ |  | ħ ʕ | h |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

*/w/ is labial-velar and not shown in this simplified chart. Modern realizations: /β/→[v], /ɸ/→[f].*

#### Notes by Place of Articulation

- **Bilabial:** /b/ and /β/ are allophones of Beth; /p/ and /ɸ/ (or /f/) are allophones of Pe
- **Labiodental:** Modern realizations of soft Beth [v] and soft Pe [f]; classical forms may have been bilabial [β] and [ɸ]
- **Dental:** /ð/ is soft Dalath; /θ/ is soft Taw
- **Alveolar:** /tˤ/ is Teth (emphatic); /sˤ/ is Tsade (emphatic). /d/ and /ð/ are allophones of Dalath; /t/ and /θ/ are allophones of Taw. Resh = alveolar trill /r/.
- **Postalveolar:** /ʃ/ is Shin
- **Palatal:** /j/ is Yudh (consonantal)
- **Velar:** /ɡ/ and /ɣ/ are allophones of Gamal; /k/ and /x/ are allophones of Kaph
- **Uvular:** /q/ is Qaph
- **Pharyngeal:** /ħ/ is Kheth; /ʕ/ is Ayin (E)
- **Glottal:** /ʔ/ is Alaph; /h/ is He
- **Labial velar:** /w/ is Waw (consonantal)

### Vowel Phonemes

The vowel phonemes of Classical Syriac, with Eastern (7 vowels) and Western (5 vowels) inventories

**Eastern vowel count:** 7 | **Western vowel count:** 5  
Eastern Syriac preserves a 7-vowel system; Western Syriac merged several vowels to yield 5

#### Eastern Vowel Chart

| Height | Front (unrounded) | Central | Back (rounded) |
|---|---|---|---|
| close | i |  | u |
| close-mid | e |  | o |
| open-mid | ɛ |  |  |
| open |  | a | ɑ |

#### Western Vowel Chart

| Height | Front (unrounded) | Central | Back (rounded) |
|---|---|---|---|
| close | i |  | u |
| close-mid | e |  | o |
| open |  | a |  |

*Western merged /ɛ/+/e/→/e/ and /ɑ/→/ɔ/. The Zqapha vowel is /ɑ/ Eastern vs /ɔ/ Western.*

#### Eastern Phoneme Inventory

| IPA | Height | Backness | Rounding | Syriac Sign | Distribution |
|---|---|---|---|---|---|
| a | open | central | unrounded | Pthakha (ܦܬ݂ܳܚܳܐ) | Open central vowel; short |
| ɑ | open | back | unrounded | Zqapha (ܙܩܳܦ݂ܳܐ) | Open back vowel; corresponds to Western /ɔ/ |
| ɛ | open-mid | front | unrounded | Rbasa karya (ܪܒ݂ܳܨܳܐ ܟܰܪܝܳܐ) | Open-mid front; short e-vowel |
| e | close-mid | front | unrounded | Rbasa arikha (ܪܒ݂ܳܨܳܐ ܐܰܪܺܝܟ݂ܳܐ) | Close-mid front; long e-vowel |
| i | close | front | unrounded | Khwasa (ܚܒ݂ܳܨܳܐ) | Close front vowel |
| o | close-mid | back | rounded | Rwakha (ܪܘܳܚܳܐ) | Close-mid back rounded |
| u | close | back | rounded | ʿEsasa (ܥܨܳܨܳܐ) | Close back rounded |

#### Western Phoneme Inventory

| IPA | Height | Backness | Rounding | Syriac Sign | Distribution |
|---|---|---|---|---|---|
| a | open | central | unrounded | Pthakha | Open central vowel |
| ɔ | open-mid | back | rounded | Zqapha | Western realization of Zqapha (Eastern /ɑ/) |
| e | close-mid | front | unrounded | Rbasa | Merged /ɛ/+/e/ |
| i | close | front | unrounded | Khwasa | Close front vowel |
| u | close | back | rounded | ʿEsasa/Rwakha | Western merged /o/+/u/ |

## Consonants

The 22 consonant letters of the Peshitta Syriac alphabet in both Syriac and Block Aramaic scripts. IPA values are shared (same language, same phonemes).

**Letter count:** 22 | **Effective phonemes:** 31  
22 letters → 31 phonemes due to 6 Begadkephat pairs (hard/soft) + base consonants

| # | Syriac Name | Block Name | Syriac | Block | Syriac Unicode | Block Unicode | IPA | Place | Manner | Voicing | Bgdkpt | Emph. | Gutt. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ʾAlaph | ʾAleph | ܐ | א | `U+0710` | `U+05D0` | /ʔ/ | glottal | plosive | voiceless |  |  | ✓ |
| 2 | Beth | Bet | ܒ | ב | `U+0712` | `U+05D1` | /b/ | bilabial | plosive | voiced | ✓ |  |  |
| 3 | Gamal | Gimel | ܓ | ג | `U+0713` | `U+05D2` | /ɡ/ | velar | plosive | voiced | ✓ |  |  |
| 4 | Dalath | Dalet | ܕ | ד | `U+0715` | `U+05D3` | /d/ | alveolar | plosive | voiced | ✓ |  |  |
| 5 | He | He | ܗ | ה | `U+0717` | `U+05D4` | /h/ | glottal | fricative | voiceless |  |  | ✓ |
| 6 | Waw | Vav | ܘ | ו | `U+0718` | `U+05D5` | /w/ | labial-velar | approximant | voiced |  |  |  |
| 7 | Zayn | Zayin | ܙ | ז | `U+0719` | `U+05D6` | /z/ | alveolar | fricative | voiced |  |  |  |
| 8 | Kheth | Chet | ܚ | ח | `U+071A` | `U+05D7` | /ħ/ | pharyngeal | fricative | voiceless |  |  | ✓ |
| 9 | Teth | Tet | ܛ | ט | `U+071B` | `U+05D8` | /tˤ/ | alveolar | plosive | voiceless |  | ✓ |  |
| 10 | Yudh | Yod | ܝ | י | `U+071D` | `U+05D9` | /j/ | palatal | approximant | voiced |  |  |  |
| 11 | Kaph | Kaf | ܟ | כ | `U+071F` | `U+05DB` | /k/ | velar | plosive | voiceless | ✓ |  |  |
| 12 | Lamadh | Lamed | ܠ | ל | `U+0720` | `U+05DC` | /l/ | alveolar | lateral_approximant | voiced |  |  |  |
| 13 | Mim | Mem | ܡ | מ | `U+0721` | `U+05DE` | /m/ | bilabial | nasal | voiced |  |  |  |
| 14 | Nun | Nun | ܢ | נ | `U+0722` | `U+05E0` | /n/ | alveolar | nasal | voiced |  |  |  |
| 15 | Semkath | Samekh | ܣ | ס | `U+0723` | `U+05E1` | /s/ | alveolar | fricative | voiceless |  |  |  |
| 16 | Ayin (E) | Ayin | ܥ | ע | `U+0725` | `U+05E2` | /ʕ/ | pharyngeal | fricative | voiced |  |  | ✓ |
| 17 | Pe | Pe | ܦ | פ | `U+0726` | `U+05E4` | /p/ | bilabial | plosive | voiceless | ✓ |  |  |
| 18 | Tsade | Tsadi | ܨ | צ | `U+0728` | `U+05E6` | /sˤ/ | alveolar | fricative | voiceless |  | ✓ |  |
| 19 | Qaph | Qof | ܩ | ק | `U+0729` | `U+05E7` | /q/ | uvular | plosive | voiceless |  |  |  |
| 20 | Resh | Resh | ܪ | ר | `U+072A` | `U+05E8` | /r/ | alveolar | trill | voiced |  |  |  |
| 21 | Shin | Shin | ܫ | ש | `U+072B` | `U+05E9` | /ʃ/ | postalveolar | fricative | voiceless |  |  |  |
| 22 | Taw | Tav | ܬ | ת | `U+072C` | `U+05EA` | /t/ | alveolar | plosive | voiceless | ✓ |  |  |

## Begadkephat

The six Begadkephat letters (בגדכפת / ܒܓܕܟܦܬ) each have two pronunciations: hard (plosive, with Qushshaya/dagesh) and soft (fricative, with Rukkakha/no dagesh). Dual-track: Syriac marks hardness with dots above/below; Block Aramaic uses dagesh.

**Rule:** After a vowel sound (post-vocalic position), Begadkephat letters are soft (fricative). After silence or a consonant, they are hard (plosive). This is the spirantization rule.

| Name | Syriac | Block | Hard IPA | Soft IPA | Classical Soft | Hard Desc. | Soft Desc. |
|---|---|---|---|---|---|---|---|
| Beth/Bet | ܒ | ב | /b/ | /v/ | /β/ | voiced bilabial plosive | voiced labiodental fricative (classical: voiced bilabial fricative /β/) |
| Gamal/Gimel | ܓ | ג | /ɡ/ | /ɣ/ | /ɣ/ | voiced velar plosive | voiced velar fricative |
| Dalath/Dalet | ܕ | ד | /d/ | /ð/ | /ð/ | voiced alveolar plosive | voiced dental fricative |
| Kaph/Kaf | ܟ | כ | /k/ | /x/ | /x/ | voiceless velar plosive | voiceless velar fricative |
| Pe | ܦ | פ | /p/ | /f/ | /ɸ/ | voiceless bilabial plosive | voiceless labiodental fricative (classical: voiceless bilabial fricative /ɸ/) |
| Taw/Tav | ܬ | ת | /t/ | /θ/ | /θ/ | voiceless alveolar plosive | voiceless dental fricative |

## Dagesh System

The dagesh system applies to Block Aramaic (Hebrew square script) texts of the Peshitta. Syriac script uses Qushshaya/Rukkakha dots instead. In Block Aramaic voweled texts (BlockVersion_Vowels/), dagesh appears as a dot inside the consonant letter.

**Unicode:** `U+05BC` — Character: ּ  
**Applies to:** Block Aramaic script only  
**Syriac equivalent:** Qushshaya (ܩܘܫܝܐ) — dot above letter for hard pronunciation

### Dagesh Lene

Marks the hard (plosive) pronunciation of Begadkephat letters: בּ גּ דּ כּ פּ תּ

**Ipa effect:** Plosive allophone: /b/, /ɡ/, /d/, /k/, /p/, /t/  
**Applies to:** Begadkephat letters only (בגדכפת)  

### Dagesh Forte

Marks gemination (consonant doubling) in Block Aramaic voweled texts

**Ipa effect:** Gemination: /Cː/ (doubled consonant)  
**Applies to:** Most consonants except gutturals (א ה ח ע) and Resh (ר)  
**Note:** In Peshitta Block Aramaic texts, dagesh forte usage follows Hebrew conventions applied to Aramaic morphology  

### Disambiguation Rule

In Begadkephat letters, dagesh lene and dagesh forte are the same grapheme (dot inside letter). Context determines which: if the letter could only be hard (word-initial), it is dagesh lene; if preceded by a vowel where doubling applies, it is dagesh forte.

**Letters that reject dagesh forte:** א, ה, ח, ע, ר

### Mappiq

A dot inside final He (הּ) indicating that He is consonantal /h/, not a mater lectionis  
**Unicode:** `U+05BC`  
Same grapheme as dagesh but functionally distinct; applies to final He only

## Vowel Diacritics

Two parallel vowel diacritical systems for the Peshitta: (1) Syriac vowel dots (Eastern Madnhaya / Western Serto traditions) and (2) Hebrew-style niqqud pointing used in Block Aramaic voweled texts.

### Syriac Vowel System

Syriac vocalization uses dots placed above or below letters. The Eastern (Madnhaya) system uses dot pairs; the Western (Serto) system uses small Greek-derived letters.

#### Eastern (Madnhaya) Vowels

| Name | IPA | Character | Unicode | Position | Note |
|---|---|---|---|---|---|
| Pthakha | /a/ | ܰ | `U+0730` | single dot above | Open central vowel |
| Zqapha | /ɑ/ | ܳ | `U+0733` | single dot above (different position) | Open back vowel; Western = /ɔ/ |
| Rbasa karya | /ɛ/ | ܶ | `U+0736` | two dots below horizontally | Open-mid front; short e |
| Rbasa arikha | /e/ | ܸ | `U+0738` | two dots below diagonally | Close-mid front; long e |
| Khwasa | /i/ | ܺ | `U+073A` | dot below | Close front vowel |
| Rwakha | /o/ | ܽ | `U+073D` | dot above Waw | Close-mid back rounded |
| ʿEsasa | /u/ | ܿ | `U+073F` | dot below Waw | Close back rounded |

#### Western (Serto) Vowels

| Name | IPA | Character | Unicode | Position | Note |
|---|---|---|---|---|---|
| Pthakha | /a/ | ܱ | `U+0731` | small letter above | Open central vowel (same IPA as Eastern) |
| Zqapha | /ɔ/ | ܴ | `U+0734` | small letter above | Open-mid back rounded (Eastern = /ɑ/) |
| Rbasa | /e/ | ܷ | `U+0737` | small letter below | Close-mid front (merged /ɛ/+/e/) |
| Khwasa | /i/ | ܻ | `U+073B` | small letter below | Close front vowel |
| ʿEsasa | /u/ | ݀ | `U+0740` | small letter below | Close back rounded (merged /o/+/u/) |

### Block Aramaic Niqqud System

Block Aramaic voweled texts (BlockVersion_Vowels/) use Hebrew-style niqqud pointing. The vowel signs are from the Hebrew Unicode block and are applied to Aramaic text in Hebrew square script.

*Niqqud values when applied to Peshitta Aramaic may differ from their Biblical Hebrew values because the underlying language is Syriac Aramaic.*

| Name | IPA | Character | Unicode | Position | Note |
|---|---|---|---|---|---|
| Patach | /a/ | ַ | `U+05B7` | below letter |  |
| Qamats | /ɑ/ (E) or /ɔ/ (W) | ָ | `U+05B8` | below letter |  |
| Segol | /ɛ/ | ֶ | `U+05B6` | below letter |  |
| Tsere | /e/ | ֵ | `U+05B5` | below letter |  |
| Hiriq | /i/ | ִ | `U+05B4` | below letter |  |
| Holam | /o/ | ֹ | `U+05B9` | above letter |  |
| Qubuts | /u/ | ֻ | `U+05BB` | below letter |  |
| Shva | /ə/ or ∅ | ְ | `U+05B0` | below letter |  |

## Shva System

The shva system in Block Aramaic voweled texts of the Peshitta. Shva (שְׁוָא) represents either a reduced vowel /ə/ (shva na/mobile) or silence (shva nach/quiescent).

**Applies to:** Block Aramaic voweled texts (BlockVersion_Vowels/) only. Syriac script does not use shva.  
**Unicode:** `U+05B0` — Character: ְ
 — Decimal: 1456


### Shva Na

**Name:** Shva na (mobile/vocal)  
**Ipa:** /ə/  
**Description:** Pronounced as a mid-central reduced vowel  
**Rules:**

- At the beginning of a word
- After another shva (the second of two consecutive shvas)
- Under a letter with dagesh forte
- After a long vowel in an open syllable


### Shva Nach

**Name:** Shva nach (quiescent/silent)  
**Ipa:** ∅ (silent)  
**Description:** Not pronounced; marks the end of a closed syllable  
**Rules:**

- At the end of a word
- The first of two consecutive shvas (except word-final)
- After a short vowel in a closed syllable



Shva rules in Peshitta Block Aramaic follow the Hebrew conventions applied to Aramaic morphology. Some contexts may differ from Biblical Hebrew shva rules due to different syllable structures in Syriac Aramaic.

## Hataf Vowels

Ultra-short (reduced) vowels used under guttural consonants in Block Aramaic voweled texts. Gutturals (א ה ח ע) prefer hataf vowels over plain shva.

**Applies to:** Block Aramaic voweled texts (BlockVersion_Vowels/) only

**Guttural consonants:** א Aleph (/ʔ/), ה He (/h/), ח Chet (/ħ/), ע Ayin (/ʕ/)

| Name | Ipa | Unicode | Character | Decimal | Description |
|---|---|---|---|---|---|
| Hataf Segol | /ɛ̆/ | U+05B1 | ֱ | 1457 | Ultra-short open-mid front vowel; replaces shva na under gutturals |
| Hataf Patach | /ă/ | U+05B2 | ֲ | 1458 | Ultra-short open front vowel; the most common hataf vowel |
| Hataf Qamats | /ɔ̆/ | U+05B3 | ֳ | 1459 | Ultra-short open-mid back rounded vowel; under gutturals before /ɔ/ or /o/ |

## Shin-Sin Distinction

In Block Aramaic (Hebrew square script), the letter Shin (ש) can represent two phonemes: Shin /ʃ/ (postalveolar fricative, dot upper-right) and Sin /s/ (alveolar fricative, dot upper-left). In Syriac script, Shin (ܫ) is a single letter representing /ʃ/ only; the /s/ phoneme is represented by Semkath (ܣ).

**Applies to:** Block Aramaic script; Syriac script has a single Shin letter

### Block Aramaic Script

| Letter | Character | Base | Dot | Dot Name | Dot Unicode | IPA | Description |
|---|---|---|---|---|---|---|---|
| Shin | שׁ | ש | ׁ | Shin dot (upper-right) | `U+05C1` | /ʃ/ | Postalveolar fricative |
| Sin | שׂ | ש | ׂ | Sin dot (upper-left) | `U+05C2` | /s/ | Alveolar fricative (same phoneme as Samekh ס) |

### Syriac Script Equivalence

- **shin IPA ʃ:** ܫ Shin (`U+072B`)
- **sin IPA s:** ܣ Semkath (`U+0723`)

Syriac distinguishes /ʃ/ and /s/ with separate letters. Block Aramaic uses one base letter with distinguishing dots.

*In Peshitta Block Aramaic voweled texts, the Shin/Sin distinction may or may not be consistently marked. Where it appears, Shin dot = /ʃ/ and Sin dot = /s/.*

## Final Form Letters

Block Aramaic (Hebrew square script) uses special final forms for 5 letters when they appear at the end of a word. Syriac script does NOT have final forms — all letters have the same form regardless of position.

**Applies to:** Block Aramaic script only

**Syriac note:** Syriac script has no final letter forms. Letters connect differently in Syriac cursive (Serto) based on position, but the base character is the same.

| Name | Medial | Medial unicode | Final | Final unicode | Ipa | Decimal medial | Decimal final |
|---|---|---|---|---|---|---|---|
| Kaf | כ | U+05DB | ך | U+05DA | /k/ or /x/ | 1499 | 1498 |
| Mem | מ | U+05DE | ם | U+05DD | /m/ | 1502 | 1501 |
| Nun | נ | U+05E0 | ן | U+05DF | /n/ | 1504 | 1503 |
| Pe | פ | U+05E4 | ף | U+05E3 | /p/ or /f/ | 1508 | 1507 |
| Tsadi | צ | U+05E6 | ץ | U+05E5 | /sˤ/ | 1510 | 1509 |

*Peshitta Block Aramaic texts in the source corpus may or may not use final forms consistently. The BlockVersion/ texts in this corpus do NOT use final forms (all letters use medial forms throughout).*

## Consonant-Vowel IPA Matrix

Consonant + vowel IPA combinations for all 22 Syriac consonants. IPA values are shared across both scripts. Uses the Eastern 7-vowel system; Western variants can be derived by applying the Eastern→Western vowel mappings.

| Consonant | Syriac | Block | Base IPA | a | ɑ | ɛ | e | i | o | u |
|---|---|---|---|---|---|---|---|---|---|---|
| ʾAlaph | ܐ | א | ʔ | ʔa | ʔɑ | ʔɛ | ʔe | ʔi | ʔo | ʔu |
| Beth | ܒ | ב | b | ba | bɑ | bɛ | be | bi | bo | bu |
| Gamal | ܓ | ג | ɡ | ɡa | ɡɑ | ɡɛ | ɡe | ɡi | ɡo | ɡu |
| Dalath | ܕ | ד | d | da | dɑ | dɛ | de | di | do | du |
| He | ܗ | ה | h | ha | hɑ | hɛ | he | hi | ho | hu |
| Waw | ܘ | ו | w | wa | wɑ | wɛ | we | wi | wo | wu |
| Zayn | ܙ | ז | z | za | zɑ | zɛ | ze | zi | zo | zu |
| Kheth | ܚ | ח | ħ | ħa | ħɑ | ħɛ | ħe | ħi | ħo | ħu |
| Teth | ܛ | ט | tˤ | tˤa | tˤɑ | tˤɛ | tˤe | tˤi | tˤo | tˤu |
| Yudh | ܝ | י | j | ja | jɑ | jɛ | je | ji | jo | ju |
| Kaph | ܟ | כ | k | ka | kɑ | kɛ | ke | ki | ko | ku |
| Lamadh | ܠ | ל | l | la | lɑ | lɛ | le | li | lo | lu |
| Mim | ܡ | מ | m | ma | mɑ | mɛ | me | mi | mo | mu |
| Nun | ܢ | נ | n | na | nɑ | nɛ | ne | ni | no | nu |
| Semkath | ܣ | ס | s | sa | sɑ | sɛ | se | si | so | su |
| Ayin (E) | ܥ | ע | ʕ | ʕa | ʕɑ | ʕɛ | ʕe | ʕi | ʕo | ʕu |
| Pe | ܦ | פ | p | pa | pɑ | pɛ | pe | pi | po | pu |
| Tsade | ܨ | צ | sˤ | sˤa | sˤɑ | sˤɛ | sˤe | sˤi | sˤo | sˤu |
| Qaph | ܩ | ק | q | qa | qɑ | qɛ | qe | qi | qo | qu |
| Resh | ܪ | ר | r | ra | rɑ | rɛ | re | ri | ro | ru |
| Shin | ܫ | ש | ʃ | ʃa | ʃɑ | ʃɛ | ʃe | ʃi | ʃo | ʃu |
| Taw | ܬ | ת | t | ta | tɑ | tɛ | te | ti | to | tu |

## Diacritical Marks

Diacritical marks used in Peshitta manuscripts and printed editions. Presented for both Syriac and Block Aramaic scripts.

### Syriac Diacritics

| Name | Character | Unicode | Decimal | Function | IPA Effect | Position |
|---|---|---|---|---|---|---|
| Qushshaya (ܩܘܫܝܐ) | ݁ | `U+0741` | 1857 | Marks hard (plosive) pronunciation of Begadkephat letter | Plosive allophone: /b/, /ɡ/, /d/, /k/, /p/, /t/ | Single dot above the letter |
| Rukkakha (ܪܘܟܟܐ) | ݂ | `U+0742` | 1858 | Marks soft (fricative) pronunciation of Begadkephat letter | Fricative allophone: /v/, /ɣ/, /ð/, /x/, /f/, /θ/ | Single dot below the letter |
| Seyame (ܣܝܡܐ) | ̈ | `U+0308` | 776 | Marks plural or distinguishes homographs | No direct phonetic effect; morphological marker | Two dots above the word |
| Linea Occultans | ݇ | `U+0747` | 1863 | Marks a silent (quiescent) letter — the letter is written but not pronounced | ∅ (letter is silent) | Small line above or below the letter |
| Mhaggyānā (ܡܗܓܝܢܐ) | ݀ | `U+0740` | 1856 | Marks a vowelless consonant or emphasizes pronunciation | Varies; typically indicates the consonant is pronounced without a following vowel | Dot or line below |

### Block Aramaic Diacritics

| Name | Character | Unicode | Decimal | Function | IPA Effect | Position |
|---|---|---|---|---|---|---|
| Dagesh | ּ | `U+05BC` | 1468 | Marks hard pronunciation (Begadkephat) or gemination | Plosive or gemination /Cː/ | Dot inside the letter |
| Shin dot | ׁ | `U+05C1` | 1473 | Distinguishes Shin /ʃ/ from Sin /s/ | /ʃ/ | Dot upper-right of Shin (שׁ) |
| Sin dot | ׂ | `U+05C2` | 1474 | Distinguishes Sin /s/ from Shin /ʃ/ | /s/ | Dot upper-left of Shin (שׂ) |
| Meteg | ֽ | `U+05BD` | 1469 | Secondary stress marker; indicates shva na or clarifies vowel length | Secondary stress or vowel lengthening | Vertical line below letter |
| Maqaf | ־ | `U+05BE` | 1470 | Word connector (hyphen); joins words into a prosodic unit | Stress shift to the final word of the unit | Horizontal line between words |
| Rafe | ֿ | `U+05BF` | 1471 | Marks soft (fricative) pronunciation of Begadkephat — opposite of dagesh | Fricative allophone | Horizontal line above letter |

## Suprasegmentals

Prosodic and suprasegmental features of Classical Syriac pronunciation

### Stress

Primary stress in Classical Syriac falls on the penultimate (second-to-last) syllable in most words. Some suffixed and construct forms shift stress to the final syllable.

**IPA notation:** ˈ before the stressed syllable

**Default pattern:** Penultimate stress (milʿel)

**Exceptions:**

- Monosyllabic words: stress falls on the single syllable
- Words with heavy final syllable (CVCC or CVːC): stress may shift to the final syllable
- Proclitic particles are unstressed

### Gemination

Consonant length (gemination) is phonemic in Eastern Syriac and indicated by doubling in IPA

**IPA notation:** ː after the consonant (e.g., /bb/ → [bː])

**Eastern tradition:** Gemination preserved; phonemic contrast between single and doubled consonants

**Western tradition:** Gemination largely lost; historical geminates simplified to single consonants

**Note:** In Block Aramaic voweled texts, gemination is marked by dagesh forte

### Vowel Length

Vowel length distinctions in Classical Syriac

**IPA notation:** ː after the vowel for long vowels

**Long vowels:**

- /aː/
- /eː/
- /iː/
- /oː/
- /uː/

**Short vowels:**

- /a/
- /ɛ/
- /i/
- /o/
- /u/

**Note:** Vowel length correlates with syllable type: short vowels in closed syllables, long vowels in open syllables

### Pharyngealization

Emphatic consonants /tˤ/ and /sˤ/ are produced with pharyngealization, which spreads to adjacent vowels

**IPA notation:** ˤ (raised pharyngeal) on the consonant

**Affected consonants:**

- /tˤ/ (Teth)
- /sˤ/ (Tsade)

**Vowel effect:** Adjacent vowels are backed and lowered: /a/ → [ɑ], /i/ → [ɪ], /u/ → [ʊ]

## Diphthongs

Diphthong combinations in Classical Syriac, shared across both scripts

| IPA | Description | Example Context | Eastern | Western |
|---|---|---|---|---|
| /aj/ | Open front + palatal glide | When Yudh follows a Pthakha vowel | [aj] | [aj] |
| /aw/ | Open front + labial-velar glide | When Waw follows a Pthakha vowel | [aw] | [aw] |
| /ej/ | Close-mid front + palatal glide | When Yudh follows an Rbasa vowel | [ej] | [ej] |
| /oj/ | Close-mid back + palatal glide | Rare; in certain loan words | [oj] | [oj] |

*Diphthongs in Syriac are relatively limited compared to Biblical Hebrew. Most apparent diphthongs have monophthongized historically (/aj/ → /eː/, /aw/ → /oː/).*

## Syllable Structure

Syllable structure patterns in Classical Syriac. This section is unique to the Peshitta guide.

**IPA template:** `(C)(C)V(C)(C)`

**Components:**

- **Onset:** C or CC — one or two consonants *(optional)*
- **Nucleus:** V — a single vowel (monophthong or diphthong) *(required)*
- **Coda:** C or CC — one or two consonants *(optional)*

### Syllable Types

| Type | Description | Ipa example | Frequency |
|---|---|---|---|
| CV | Open syllable (consonant + vowel) | /ba/ | Most common |
| CVC | Closed syllable | /bar/ | Very common |
| V | Vowel-only (rare; with silent Alaph onset) | /a/ | Rare |
| VC | Vowel + coda (rare) | /al/ | Rare |
| CVCC | Closed with consonant cluster coda | /malk/ | Common |
| CCVC | Consonant cluster onset | /ʃmaʕ/ | Occasional |

### Rules

- Short vowels /a/, /ɛ/, /i/ typically occur in closed syllables (with a coda consonant)
- Long vowels /aː/, /eː/, /iː/, /oː/, /uː/ may occur in open or closed syllables
- Maximum syllable: CCVCC
- Onset clusters are limited; most onsets are single consonants
- Coda clusters of two consonants are common in word-final position

## Phonological Rules

Active phonological processes in Classical Syriac

### Rule 1: Begadkephat spirantization

**IPA notation:** /b d ɡ k p t/ → [v ð ɣ x f θ] / V_

Begadkephat letters become fricatives after a vowel (post-vocalic spirantization)

**Examples:**

- word-initial /b/ (plosive) vs. post-vocalic /v/ (fricative)

### Rule 2: Assimilation of Nun

**IPA notation:** /n/ → [C] / _C (where C is a following consonant)

Nun assimilates to the place of articulation of a following consonant, especially before dental and alveolar consonants

**Examples:**

- /nt/ → [tt]
- /nd/ → [dd]

### Rule 3: Assimilation of Taw (Ethpeel/Ethpaal)

**IPA notation:** /t/ → [C] / in Ethpeel/Ethpaal stems before sibilants

The Taw of the Ethpeel/Ethpaal reflexive stems assimilates to following sibilants (/s/, /z/, /sˤ/, /ʃ/)

**Examples:**

- /ʔeθtˤamar/ → [ʔeθθamar]

### Rule 4: Alaph quiescence

**IPA notation:** /ʔ/ → ∅ / in specific morphological contexts

Alaph frequently becomes silent (quiescent), especially in medial and final positions. Marked by Linea Occultans in Syriac script.

**Examples:**

- final Alaph in emphatic state nouns is typically silent

### Rule 5: Vowel reduction in unstressed syllables

**IPA notation:** V → [ə] or ∅ / in pretonic open syllables

Short vowels in unstressed open syllables may reduce to schwa or be elided

**Examples:**

- rapid speech: full vowels → [ə]

### Rule 6: Pharyngealization spread

**IPA notation:** /tˤ, sˤ/ → adjacent vowels backed/lowered

Emphatic consonants cause adjacent vowels to be backed and lowered

**Examples:**

- /tˤa/ → [tˤɑ]
- /sˤi/ → [sˤɪ]

### Rule 7: Waw/Yudh consonant-vowel alternation

**IPA notation:** /w/ ↔ /u/, /o/; /j/ ↔ /i/, /e/

Waw and Yudh alternate between consonantal (/w/, /j/) and vocalic (/u/o/, /i/e/) realizations based on syllable position

**Examples:**

- onset Waw = [w]; nucleus Waw = [uː] or [oː]

### Rule 8: Gemination of consonants after short vowels

**IPA notation:** C → Cː / V̆_ (in Pa''el, Aph'el stems)

The middle radical is geminated in Pa''el and related verb stems (Eastern tradition preserves gemination; Western tends to simplify)

**Examples:**

- /qattel/ (Pa''el intensive)

### Rule 9: He quiescence in final position

**IPA notation:** /h/ → ∅ / _# (word-finally, unless mappiq in Block script)

Final He is often silent, serving as a mater lectionis for the preceding vowel

**Examples:**

- final /-ah/ may be realized as [-aː]

### Rule 10: Compensatory lengthening

**IPA notation:** V → Vː / when a following consonant is lost

When a consonant (especially Alaph or He) is lost, the preceding vowel lengthens to compensate

**Examples:**

- /raʔʃ/ → [rɑːʃ]

### Rule 11: Metathesis of Taw in Ethpeel

**IPA notation:** /ʔet- + sibilant/ → /ʔes- + t/

When Ethpeel prefix /t/ precedes a sibilant, metathesis may occur

**Examples:**

- /ʔetsammaḵ/ → [ʔestammaḵ]

### Rule 12: Degemination of final consonants

**IPA notation:** Cː → C / _#

Geminate consonants are simplified in absolute word-final position

**Examples:**

- /ħadd/ → [ħad]

## Eastern vs. Western IPA Differences

Systematic pronunciation differences between Eastern (Madnhaya) and Western (Serto) traditions, expressed in IPA. This section is unique to the Peshitta guide.

| Feature | Eastern IPA | Western IPA | Note |
|---|---|---|---|
| Zqapha vowel | [ɑ] | [ɔ] | Major vowel shift; Western /ɑ/ → [ɔ] |
| Vowel inventory size | 7 phonemes: /a ɑ ɛ e i o u/ | 5 phonemes: /a ɔ e i u/ | Western merged /ɛ/+/e/ and /o/+/u/ |
| Gemination | [Cː] preserved | [Cː] lost (→ [C]) | Eastern maintains consonant length contrast |
| Soft Taw | [θ] consistent | [θ] or [t] | Some Western dialects simplify |
| Kheth realization | [x] (velar fricative) | [ħ] (pharyngeal fricative) | Different phonetic realization of Kheth |
| Rbasa vowels | [ɛ] (karya) vs [e] (arikha) | [e] (merged) | Western merged the two e-vowels |
| Rwakha/ʿEsasa | [o] vs [u] (distinct) | [u] (merged) | Western merged o and u |

## Vocalization Traditions

Three vocalization systems used to represent Peshitta vowels: Eastern Madnhaya dots, Western Serto marks, and Block Aramaic (Hebrew-style) niqqud.

### Eastern (Madnhaya)

**Script:** Syriac  
**Vowel count:** 7  
**Vowels:** /a/, /ɑ/, /ɛ/, /e/, /i/, /o/, /u/  
**Gemination:** Preserved; marked by Mhaggyānā or contextual rules  
**Key feature:** 7-vowel system preserving Proto-Syriac distinctions  

Uses pairs of dots above and below letters to indicate vowels. Developed in the Church of the East tradition.

### Western (Serto)

**Script:** Syriac  
**Vowel count:** 5  
**Vowels:** /a/, /ɔ/, /e/, /i/, /u/  
**Gemination:** Largely lost; historical geminates simplified  
**Key feature:** 5-vowel system with merged categories (Zqapha = /ɔ/)  

Uses small Greek-derived vowel letters placed above or below consonants. Developed in the Syriac Orthodox tradition.

### Block Aramaic niqqud

**Script:** Block Aramaic (Hebrew square script)  
**Vowel count:** 7  
**Vowels:** /a/, /ɔ/, /ɛ/, /e/, /i/, /o/, /u/ (plus shva /ə/ and hataf vowels)  
**Gemination:** Marked by dagesh forte (dot inside consonant)  
**Key feature:** Hebrew niqqud applied to Syriac Aramaic morphology; vowel values may differ from Biblical Hebrew  

Uses Hebrew Tiberian-style niqqud pointing applied to Aramaic text in Hebrew script. Found in study editions and interlinear Bibles.

### Cross-System Vowel Mapping

| Eastern syriac | Western syriac | Block niqqud |
|---|---|---|
| Pthakha /a/ | Pthakha /a/ | Patach /a/ |
| Zqapha /ɑ/ | Zqapha /ɔ/ | Qamats /ɑ/ or /ɔ/ |
| Rbasa karya /ɛ/ | Rbasa /e/ (merged) | Segol /ɛ/ |
| Rbasa arikha /e/ | Rbasa /e/ (merged) | Tsere /e/ |
| Khwasa /i/ | Khwasa /i/ | Hiriq /i/ |
| Rwakha /o/ | ʿEsasa /u/ (merged) | Holam /o/ |
| ʿEsasa /u/ | ʿEsasa /u/ (merged) | Qubuts/Shuruq /u/ |

## Cantillation Overview

Syriac liturgical accent marks (qeryānā / qonunā) used in Peshitta manuscripts for chanting and reading. Less codified than the Hebrew cantillation (teamim) system.

*Syriac cantillation is primarily an oral tradition with regional variation. The accent marks in manuscripts serve as guides for chanting patterns rather than a strict grammatical system.*

### Syriac Accent Marks

| Name | Character | Unicode | Function | IPA Effect | Position |
|---|---|---|---|---|---|
| Pāsōqā (ܦܣܘܩܐ) | ܀ | `U+0700` | Verse divider; marks the end of a verse | Full pause; falling intonation | End of verse |
| Zāwgā Elpāyā (ܙܘܓܐ ܐܠܦܝܐ) | ܆ | `U+0706` | Phrase divider; marks the primary division within a verse | Major pause; slight pitch rise before pause | Mid-verse break |
| Tāḥtāyā (ܬܚܬܝܐ) | ܃ | `U+0703` | Minor pause or breath mark | Brief pause | Between phrases |
| ʿElyāyā (ܥܠܝܝܐ) | ܄ | `U+0704` | Minor accent mark, above the line | Slight pitch accent | Above letter |

### Block Aramaic

Block Aramaic texts of the Peshitta typically do not include cantillation marks. Hebrew cantillation (teamim) is not applied to Peshitta Block texts.

### Comparison with Hebrew Cantillation

Syriac cantillation is simpler and less codified than the Hebrew te'amim system. Hebrew has 28+ distinct cantillation marks with strict hierarchical rules; Syriac has fewer marks with more regional variation.

## Cross-Reference: Aramaic and Hebrew

Three-way cross-reference between Peshitta Syriac, Biblical Aramaic, and Biblical Hebrew. Documents phonological correspondences, shared features, and key differences.

### Shared Features

- All three are Semitic languages written right-to-left
- All use the Begadkephat spirantization rule (6 letters with hard/soft allophones)
- All have guttural consonants: Aleph/Alaph /ʔ/, He /h/, Kheth/Heth /ħ/, Ayin /ʕ/
- All have emphatic consonants: Teth /tˤ/, Tsade/Tsadi /sˤ/
- All have pharyngealized (emphatic) consonants that spread to adjacent vowels
- Triconsonantal root morphology is shared across all three languages

### Key Differences

| Feature | Peshitta | Biblical aramaic | Biblical hebrew | Note |
|---|---|---|---|---|
| Resh pronunciation | /r/ (alveolar trill) | /r/ (alveolar trill) | /ʁ/ (uvular fricative, Tiberian reconstruction per Geoffrey Khan) | Syriac and Biblical Aramaic preserve the older Semitic alveolar /r/ |
| Vowel systems | Eastern: 7 vowels /a ɑ ɛ e i o u/; Western: 5 vowels /a ɔ e i u/ | Tiberian: 7 vowels /a ɛ e i ɔ o u/ | Tiberian: 7 vowels /a ɛ e i ɔ o u/ | Peshitta Eastern and Tiberian systems have the same number of vowels but different distributions |
| Script systems | Syriac script (U+0700–U+074F) primary; Block Aramaic (U+0590–U+05FF) secondary | Hebrew square script (U+0590–U+05FF) only | Hebrew square script (U+0590–U+05FF) only | Block Aramaic Peshitta shares the same script as Biblical Aramaic and Hebrew |
| Vocalization system | Syriac dots (Eastern/Western) or niqqud (Block Aramaic) | Tiberian niqqud | Tiberian niqqud | Block Aramaic Peshitta uses the same niqqud system as Biblical Aramaic/Hebrew |
| Shin/Sin distinction | Syriac: separate letters (Shin ܫ /ʃ/, Semkath ܣ /s/); Block: dot system (שׁ /ʃ/, שׂ /s/) | Dot system (שׁ /ʃ/, שׂ /s/) | Dot system (שׁ /ʃ/, שׂ /s/) | All three distinguish /ʃ/ and /s/ but Syriac uses separate letters |
| Final letter forms | Syriac: none; Block Aramaic: uses Hebrew final forms (ך ם ן ף ץ) | Hebrew final forms (ך ם ן ף ץ) | Hebrew final forms (ך ם ן ף ץ) | Syriac script has no final forms; Block Aramaic follows Hebrew convention |
| Gemination marking | Syriac: contextual / Mhaggyānā; Block: dagesh forte | Dagesh forte | Dagesh forte | Eastern Syriac preserves gemination; Western has largely lost it |
| Definite article | Emphatic state suffix /-ɑ/ (not a prefix) | Emphatic state suffix /-ɑ/ (same as Peshitta) | Prefix /ha-/ with dagesh forte on following consonant | Aramaic languages (Peshitta + Biblical Aramaic) use suffixed definiteness; Hebrew uses a prefix |

### Companion Guides

- `biblical_aramaic`
- `biblical_hebrew`

## Sample Words — IPA Transcriptions

16 sample words extracted from the Peshitta source corpus in all four script variants: consonantal Syriac, voweled Syriac, consonantal Block Aramaic, and voweled Block Aramaic. Each word includes IPA transcription for both Eastern and Western traditions, source reference, codepoint verification, and segmental decomposition derived from the word field.

*All words are byte-sliced from actual source text files in the Peshitta/ folder. No characters were manually typed.*

**Total sample words:** 16

### 1. book / scripture

| Form | Text |
|---|---|
| Syriac (consonantal) | ܟܬܒܐ |
| Syriac (voweled) | ܟ݁ܬ݂ܳܒ݂ܳܐ |
| Block (consonantal) | כתבא |
| Block (voweled) | כֶתַבַא |

**IPA phonemic:** /kθɑːvɑː/  
**IPA phonetic (Eastern):** [kθɑː.ˈvɑː]  
**IPA phonetic (Western):** [kθɔː.ˈvɔː]  
**Stress:** milra (final)  
**Source:** Matthew 1:1

**Features demonstrated:**

- Kaph hard /k/ (word-initial)
- Soft Taw /θ/ (post-vocalic Begadkephat)
- Soft Beth /v/
- Emphatic state /-ɑː/

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܟ | ܟ݁ | U+071F | ݁ `U+0741` SYRIAC QUSHSHAYA |
| ܬ | ܬ݂ܳ | U+072C | ݂ `U+0742` SYRIAC RUKKAKHA; ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܒ | ܒ݂ܳ | U+0712 | ݂ `U+0742` SYRIAC RUKKAKHA; ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܐ | ܐ | U+0710 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| כ | כֶ | U+05DB | ֶ `U+05B6` HEBREW POINT SEGOL |
| ת | תַ | U+05EA | ַ `U+05B7` HEBREW POINT PATAH |
| ב | בַ | U+05D1 | ַ `U+05B7` HEBREW POINT PATAH |
| א | א | U+05D0 |  |

---

### 2. Jesus

| Form | Text |
|---|---|
| Syriac (consonantal) | ܝܫܘܥ |
| Syriac (voweled) | ܝܶܫܽܘܥ |
| Block (consonantal) | ישוע |
| Block (voweled) | יַשֶוַע |

**IPA phonemic:** /jeʃuːʕ/  
**IPA phonetic (Eastern):** [je.ˈʃuːʕ]  
**IPA phonetic (Western):** [je.ˈʃuːʕ]  
**Stress:** milra (final)  
**Source:** Matthew 1:21

**Features demonstrated:**

- Yudh consonantal /j/
- Shin /ʃ/ (postalveolar fricative)
- Long /uː/ vowel
- Ayin /ʕ/ (pharyngeal guttural)

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܝ | ܝܶ | U+071D | ܶ `U+0736` SYRIAC RBASA ABOVE |
| ܫ | ܫܽ | U+072B | ܽ `U+073D` SYRIAC ESASA ABOVE |
| ܘ | ܘ | U+0718 |  |
| ܥ | ܥ | U+0725 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| י | יַ | U+05D9 | ַ `U+05B7` HEBREW POINT PATAH |
| ש | שֶ | U+05E9 | ֶ `U+05B6` HEBREW POINT SEGOL |
| ו | וַ | U+05D5 | ַ `U+05B7` HEBREW POINT PATAH |
| ע | ע | U+05E2 |  |

---

### 3. Messiah / Christ

| Form | Text |
|---|---|
| Syriac (consonantal) | ܡܫܝܚܐ |
| Syriac (voweled) | ܡܫܺܝܚܳܐ |
| Block (consonantal) | משיחא |
| Block (voweled) | מֶשֶיַחַא |

**IPA phonemic:** /mʃiːħɑː/  
**IPA phonetic (Eastern):** [mʃiː.ˈħɑː]  
**IPA phonetic (Western):** [mʃiː.ˈħɔː]  
**Stress:** milra (final)  
**Source:** Matthew 1:1

**Features demonstrated:**

- Shin /ʃ/
- Kheth /ħ/ (pharyngeal fricative)
- Emphatic state /-ɑː/
- Eastern /ɑː/ vs Western /ɔː/

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܡ | ܡ | U+0721 |  |
| ܫ | ܫܺ | U+072B | ܺ `U+073A` SYRIAC HBASA ABOVE |
| ܝ | ܝ | U+071D |  |
| ܚ | ܚܳ | U+071A | ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܐ | ܐ | U+0710 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| מ | מֶ | U+05DE | ֶ `U+05B6` HEBREW POINT SEGOL |
| ש | שֶ | U+05E9 | ֶ `U+05B6` HEBREW POINT SEGOL |
| י | יַ | U+05D9 | ַ `U+05B7` HEBREW POINT PATAH |
| ח | חַ | U+05D7 | ַ `U+05B7` HEBREW POINT PATAH |
| א | א | U+05D0 |  |

---

### 4. king

| Form | Text |
|---|---|
| Syriac (consonantal) | ܡܠܟܐ |
| Syriac (voweled) | ܡܰܠܟ݁ܳܐ |
| Block (consonantal) | מלכא |
| Block (voweled) | מֶלַכַא |

**IPA phonemic:** /malkɑː/  
**IPA phonetic (Eastern):** [mal.ˈkɑː]  
**IPA phonetic (Western):** [mal.ˈkɔː]  
**Stress:** milra (final)  
**Source:** Matthew 1:6

**Features demonstrated:**

- CVC.CV syllable structure
- Kaph hard /k/ (after consonant)
- Emphatic state /-ɑː/
- East /ɑː/ vs West /ɔː/

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܡ | ܡܰ | U+0721 | ܰ `U+0730` SYRIAC PTHAHA ABOVE |
| ܠ | ܠ | U+0720 |  |
| ܟ | ܟ݁ܳ | U+071F | ݁ `U+0741` SYRIAC QUSHSHAYA; ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܐ | ܐ | U+0710 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| מ | מֶ | U+05DE | ֶ `U+05B6` HEBREW POINT SEGOL |
| ל | לַ | U+05DC | ַ `U+05B7` HEBREW POINT PATAH |
| כ | כַ | U+05DB | ַ `U+05B7` HEBREW POINT PATAH |
| א | א | U+05D0 |  |

---

### 5. spirit

| Form | Text |
|---|---|
| Syriac (consonantal) | ܪܘܚܐ |
| Syriac (voweled) | ܪܽܘܚܳܐ |
| Block (consonantal) | רוחא |
| Block (voweled) | רַוַחַא |

**IPA phonemic:** /ruːħɑː/  
**IPA phonetic (Eastern):** [ruː.ˈħɑː]  
**IPA phonetic (Western):** [ruː.ˈħɔː]  
**Stress:** milra (final)  
**Source:** Matthew 1:18

**Features demonstrated:**

- Resh /r/ (alveolar trill — NOT uvular)
- Long /uː/ with Waw mater
- Kheth /ħ/ (pharyngeal)
- Emphatic state

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܪ | ܪܽ | U+072A | ܽ `U+073D` SYRIAC ESASA ABOVE |
| ܘ | ܘ | U+0718 |  |
| ܚ | ܚܳ | U+071A | ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܐ | ܐ | U+0710 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ר | רַ | U+05E8 | ַ `U+05B7` HEBREW POINT PATAH |
| ו | וַ | U+05D5 | ַ `U+05B7` HEBREW POINT PATAH |
| ח | חַ | U+05D7 | ַ `U+05B7` HEBREW POINT PATAH |
| א | א | U+05D0 |  |

---

### 6. in the beginning

| Form | Text |
|---|---|
| Syriac (consonantal) | ܒܪܫܝܬ |
| Syriac (voweled) | ܒ݁ܪܺܫܺܝܬ݂ |
| Block (consonantal) | ברשית |
| Block (voweled) | בּרִשִיתֿ |

**IPA phonemic:** /breːʃiːθ/  
**IPA phonetic (Eastern):** [breː.ˈʃiːθ]  
**IPA phonetic (Western):** [breː.ˈʃiːθ]  
**Stress:** milra (final)  
**Source:** John 1:1

**Features demonstrated:**

- Beth hard /b/ (word-initial)
- Resh /r/ (alveolar trill)
- Shin /ʃ/
- Soft Taw /θ/ (word-final)

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܒ | ܒ݁ | U+0712 | ݁ `U+0741` SYRIAC QUSHSHAYA |
| ܪ | ܪܺ | U+072A | ܺ `U+073A` SYRIAC HBASA ABOVE |
| ܫ | ܫܺ | U+072B | ܺ `U+073A` SYRIAC HBASA ABOVE |
| ܝ | ܝ | U+071D |  |
| ܬ | ܬ݂ | U+072C | ݂ `U+0742` SYRIAC RUKKAKHA |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ב | בּ | U+05D1 | ּ `U+05BC` HEBREW POINT DAGESH OR MAPIQ |
| ר | רִ | U+05E8 | ִ `U+05B4` HEBREW POINT HIRIQ |
| ש | שִ | U+05E9 | ִ `U+05B4` HEBREW POINT HIRIQ |
| י | י | U+05D9 |  |
| ת | תֿ | U+05EA | ֿ `U+05BF` HEBREW POINT RAFE |

---

### 7. word / logos

| Form | Text |
|---|---|
| Syriac (consonantal) | ܡܠܬܐ |
| Syriac (voweled) | ܡܶܠܬ݂ܳܐ |
| Block (consonantal) | מלתא |
| Block (voweled) | מֶלתָֿא |

**IPA phonemic:** /melθɑː/  
**IPA phonetic (Eastern):** [mel.ˈθɑː]  
**IPA phonetic (Western):** [mel.ˈθɔː]  
**Stress:** milra (final)  
**Source:** John 1:1

**Features demonstrated:**

- Soft Taw /θ/ (post-vocalic Begadkephat)
- Emphatic state /-ɑː/
- CVC.CV syllable pattern

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܡ | ܡܶ | U+0721 | ܶ `U+0736` SYRIAC RBASA ABOVE |
| ܠ | ܠ | U+0720 |  |
| ܬ | ܬ݂ܳ | U+072C | ݂ `U+0742` SYRIAC RUKKAKHA; ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܐ | ܐ | U+0710 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| מ | מֶ | U+05DE | ֶ `U+05B6` HEBREW POINT SEGOL |
| ל | ל | U+05DC |  |
| ת | תָֿ | U+05EA | ֿ `U+05BF` HEBREW POINT RAFE; ָ `U+05B8` HEBREW POINT QAMATS |
| א | א | U+05D0 |  |

---

### 8. God

| Form | Text |
|---|---|
| Syriac (consonantal) | ܐܠܗܐ |
| Syriac (voweled) | ܐܰܠܳܗܳܐ |
| Block (consonantal) | אלהא |
| Block (voweled) | אַלָהָא |

**IPA phonemic:** /ʔɑːlɑːhɑː/  
**IPA phonetic (Eastern):** [ʔɑː.lɑː.ˈhɑː]  
**IPA phonetic (Western):** [ʔɔː.lɔː.ˈhɔː]  
**Stress:** milra (final)  
**Source:** John 1:1

**Features demonstrated:**

- Alaph /ʔ/ (glottal stop)
- He /h/ (glottal fricative)
- Three open syllables
- Emphatic state

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܐ | ܐܰ | U+0710 | ܰ `U+0730` SYRIAC PTHAHA ABOVE |
| ܠ | ܠܳ | U+0720 | ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܗ | ܗܳ | U+0717 | ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܐ | ܐ | U+0710 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| א | אַ | U+05D0 | ַ `U+05B7` HEBREW POINT PATAH |
| ל | לָ | U+05DC | ָ `U+05B8` HEBREW POINT QAMATS |
| ה | הָ | U+05D4 | ָ `U+05B8` HEBREW POINT QAMATS |
| א | א | U+05D0 |  |

---

### 9. blessed are they (Beatitudes formula)

| Form | Text |
|---|---|
| Syriac (consonantal) | ܛܘܒܝܗܘܢ |
| Syriac (voweled) | ܛܽܘܒ݂ܰܝܗܽܘܢ |
| Block (consonantal) | טוביהונ |
| Block (voweled) | טַוַבַיַהַוַנ |

**IPA phonemic:** /tˤuːvajhon/  
**IPA phonetic (Eastern):** [tˤuː.vaj.ˈhon]  
**IPA phonetic (Western):** [tˤuː.vaj.ˈhon]  
**Stress:** milra (final)  
**Source:** Matthew 5:3

**Features demonstrated:**

- Teth /tˤ/ (emphatic consonant)
- Long /uː/
- Soft Beth /v/ (post-vocalic)
- Pronominal suffix /-hon/

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܛ | ܛܽ | U+071B | ܽ `U+073D` SYRIAC ESASA ABOVE |
| ܘ | ܘ | U+0718 |  |
| ܒ | ܒ݂ܰ | U+0712 | ݂ `U+0742` SYRIAC RUKKAKHA; ܰ `U+0730` SYRIAC PTHAHA ABOVE |
| ܝ | ܝ | U+071D |  |
| ܗ | ܗܽ | U+0717 | ܽ `U+073D` SYRIAC ESASA ABOVE |
| ܘ | ܘ | U+0718 |  |
| ܢ | ܢ | U+0722 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ט | טַ | U+05D8 | ַ `U+05B7` HEBREW POINT PATAH |
| ו | וַ | U+05D5 | ַ `U+05B7` HEBREW POINT PATAH |
| ב | בַ | U+05D1 | ַ `U+05B7` HEBREW POINT PATAH |
| י | יַ | U+05D9 | ַ `U+05B7` HEBREW POINT PATAH |
| ה | הַ | U+05D4 | ַ `U+05B7` HEBREW POINT PATAH |
| ו | וַ | U+05D5 | ַ `U+05B7` HEBREW POINT PATAH |
| נ | נ | U+05E0 |  |

---

### 10. kingdom

| Form | Text |
|---|---|
| Syriac (consonantal) | ܡܠܟܘܬܐ |
| Syriac (voweled) | ܡܰܠܟ݁ܽܘܬ݂ܳܐ |
| Block (consonantal) | מלכותא |
| Block (voweled) | מֶלַכַוַתַא |

**IPA phonemic:** /malkuːθɑː/  
**IPA phonetic (Eastern):** [mal.kuː.ˈθɑː]  
**IPA phonetic (Western):** [mal.kuː.ˈθɔː]  
**Stress:** milra (final)  
**Source:** Matthew 5:3

**Features demonstrated:**

- CVCC onset cluster (malk-)
- Long /uː/ with Waw
- Soft Taw /θ/ (post-vocalic)
- Emphatic state

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܡ | ܡܰ | U+0721 | ܰ `U+0730` SYRIAC PTHAHA ABOVE |
| ܠ | ܠ | U+0720 |  |
| ܟ | ܟ݁ܽ | U+071F | ݁ `U+0741` SYRIAC QUSHSHAYA; ܽ `U+073D` SYRIAC ESASA ABOVE |
| ܘ | ܘ | U+0718 |  |
| ܬ | ܬ݂ܳ | U+072C | ݂ `U+0742` SYRIAC RUKKAKHA; ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܐ | ܐ | U+0710 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| מ | מֶ | U+05DE | ֶ `U+05B6` HEBREW POINT SEGOL |
| ל | לַ | U+05DC | ַ `U+05B7` HEBREW POINT PATAH |
| כ | כַ | U+05DB | ַ `U+05B7` HEBREW POINT PATAH |
| ו | וַ | U+05D5 | ַ `U+05B7` HEBREW POINT PATAH |
| ת | תַ | U+05EA | ַ `U+05B7` HEBREW POINT PATAH |
| א | א | U+05D0 |  |

---

### 11. of heaven(s)

| Form | Text |
|---|---|
| Syriac (consonantal) | ܕܫܡܝܐ |
| Syriac (voweled) | ܕ݁ܰܫܡܰܝܳܐ |
| Block (consonantal) | דשמיא |
| Block (voweled) | דֶשֶמַיַא |

**IPA phonemic:** /daʃmajjɑː/  
**IPA phonetic (Eastern):** [daʃ.maj.ˈjɑː]  
**IPA phonetic (Western):** [daʃ.maj.ˈjɔː]  
**Stress:** milra (final)  
**Source:** Matthew 5:3

**Features demonstrated:**

- Dalath prefix /d-/ (genitive)
- Shin /ʃ/
- Geminate Yudh /jj/
- Emphatic state /-ɑː/

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܕ | ܕ݁ܰ | U+0715 | ݁ `U+0741` SYRIAC QUSHSHAYA; ܰ `U+0730` SYRIAC PTHAHA ABOVE |
| ܫ | ܫ | U+072B |  |
| ܡ | ܡܰ | U+0721 | ܰ `U+0730` SYRIAC PTHAHA ABOVE |
| ܝ | ܝܳ | U+071D | ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܐ | ܐ | U+0710 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ד | דֶ | U+05D3 | ֶ `U+05B6` HEBREW POINT SEGOL |
| ש | שֶ | U+05E9 | ֶ `U+05B6` HEBREW POINT SEGOL |
| מ | מַ | U+05DE | ַ `U+05B7` HEBREW POINT PATAH |
| י | יַ | U+05D9 | ַ `U+05B7` HEBREW POINT PATAH |
| א | א | U+05D0 |  |

---

### 12. our father

| Form | Text |
|---|---|
| Syriac (consonantal) | ܐܒܘܢ |
| Syriac (voweled) | ܐܰܒ݂ܽܘܢ |
| Block (consonantal) | אבונ |
| Block (voweled) | אַבַוַנ |

**IPA phonemic:** /ʔɑːvun/  
**IPA phonetic (Eastern):** [ˈʔɑː.vun]  
**IPA phonetic (Western):** [ˈʔɔː.vun]  
**Stress:** milʿel (penultimate)  
**Source:** Matthew 6:9

**Features demonstrated:**

- Alaph /ʔ/
- Soft Beth /v/ (post-vocalic)
- Pronominal suffix /-un/ (1pl)
- Penultimate stress

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܐ | ܐܰ | U+0710 | ܰ `U+0730` SYRIAC PTHAHA ABOVE |
| ܒ | ܒ݂ܽ | U+0712 | ݂ `U+0742` SYRIAC RUKKAKHA; ܽ `U+073D` SYRIAC ESASA ABOVE |
| ܘ | ܘ | U+0718 |  |
| ܢ | ܢ | U+0722 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| א | אַ | U+05D0 | ַ `U+05B7` HEBREW POINT PATAH |
| ב | בַ | U+05D1 | ַ `U+05B7` HEBREW POINT PATAH |
| ו | וַ | U+05D5 | ַ `U+05B7` HEBREW POINT PATAH |
| נ | נ | U+05E0 |  |

---

### 13. your kingdom

| Form | Text |
|---|---|
| Syriac (consonantal) | ܡܠܟܘܬܟ |
| Syriac (voweled) | ܡܰܠܟ݁ܽܘܬ݂ܳܟ݂ |
| Block (consonantal) | מלכותכ |
| Block (voweled) | מֶלַכַוַתַכ |

**IPA phonemic:** /malkuːθɑːx/  
**IPA phonetic (Eastern):** [mal.kuː.ˈθɑːx]  
**IPA phonetic (Western):** [mal.kuː.ˈθɔːx]  
**Stress:** milra (final)  
**Source:** Matthew 6:10

**Features demonstrated:**

- Soft Taw /θ/
- Soft Kaph /x/ (word-final suffix)
- Pronominal suffix /-ɑːx/ (2ms)
- Begadkephat in suffix

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܡ | ܡܰ | U+0721 | ܰ `U+0730` SYRIAC PTHAHA ABOVE |
| ܠ | ܠ | U+0720 |  |
| ܟ | ܟ݁ܽ | U+071F | ݁ `U+0741` SYRIAC QUSHSHAYA; ܽ `U+073D` SYRIAC ESASA ABOVE |
| ܘ | ܘ | U+0718 |  |
| ܬ | ܬ݂ܳ | U+072C | ݂ `U+0742` SYRIAC RUKKAKHA; ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܟ | ܟ݂ | U+071F | ݂ `U+0742` SYRIAC RUKKAKHA |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| מ | מֶ | U+05DE | ֶ `U+05B6` HEBREW POINT SEGOL |
| ל | לַ | U+05DC | ַ `U+05B7` HEBREW POINT PATAH |
| כ | כַ | U+05DB | ַ `U+05B7` HEBREW POINT PATAH |
| ו | וַ | U+05D5 | ַ `U+05B7` HEBREW POINT PATAH |
| ת | תַ | U+05EA | ַ `U+05B7` HEBREW POINT PATAH |
| כ | כ | U+05DB |  |

---

### 14. on earth / on the land

| Form | Text |
|---|---|
| Syriac (consonantal) | ܒܐܪܥܐ |
| Syriac (voweled) | ܒ݁ܰܐܪܥܳܐ |
| Block (consonantal) | בארעא |
| Block (voweled) | בֶאַרַעַא |

**IPA phonemic:** /bʔarʕɑː/  
**IPA phonetic (Eastern):** [bʔar.ˈʕɑː]  
**IPA phonetic (Western):** [bʔar.ˈʕɔː]  
**Stress:** milra (final)  
**Source:** Matthew 6:10

**Features demonstrated:**

- Beth prefix /b-/ (preposition)
- Alaph /ʔ/
- Resh /r/ (alveolar)
- Ayin /ʕ/ (pharyngeal guttural)

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܒ | ܒ݁ܰ | U+0712 | ݁ `U+0741` SYRIAC QUSHSHAYA; ܰ `U+0730` SYRIAC PTHAHA ABOVE |
| ܐ | ܐ | U+0710 |  |
| ܪ | ܪ | U+072A |  |
| ܥ | ܥܳ | U+0725 | ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܐ | ܐ | U+0710 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ב | בֶ | U+05D1 | ֶ `U+05B6` HEBREW POINT SEGOL |
| א | אַ | U+05D0 | ַ `U+05B7` HEBREW POINT PATAH |
| ר | רַ | U+05E8 | ַ `U+05B7` HEBREW POINT PATAH |
| ע | עַ | U+05E2 | ַ `U+05B7` HEBREW POINT PATAH |
| א | א | U+05D0 |  |

---

### 15. their sins

| Form | Text |
|---|---|
| Syriac (consonantal) | ܚܛܗܝܗܘܢ |
| Syriac (voweled) | ܚܛܳܗܰܝܗܽܘܢ |
| Block (consonantal) | חטהיהונ |
| Block (voweled) | חַטַהַיַהַוַנ |

**IPA phonemic:** /ħtˤɑːhajhon/  
**IPA phonetic (Eastern):** [ħtˤɑː.haj.ˈhon]  
**IPA phonetic (Western):** [ħtˤɔː.haj.ˈhon]  
**Stress:** milra (final)  
**Source:** Matthew 1:21

**Features demonstrated:**

- Kheth /ħ/ (pharyngeal)
- Teth /tˤ/ (emphatic)
- He /h/
- Pronominal suffix /-hon/ (3mpl)

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܚ | ܚ | U+071A |  |
| ܛ | ܛܳ | U+071B | ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܗ | ܗܰ | U+0717 | ܰ `U+0730` SYRIAC PTHAHA ABOVE |
| ܝ | ܝ | U+071D |  |
| ܗ | ܗܽ | U+0717 | ܽ `U+073D` SYRIAC ESASA ABOVE |
| ܘ | ܘ | U+0718 |  |
| ܢ | ܢ | U+0722 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ח | חַ | U+05D7 | ַ `U+05B7` HEBREW POINT PATAH |
| ט | טַ | U+05D8 | ַ `U+05B7` HEBREW POINT PATAH |
| ה | הַ | U+05D4 | ַ `U+05B7` HEBREW POINT PATAH |
| י | יַ | U+05D9 | ַ `U+05B7` HEBREW POINT PATAH |
| ה | הַ | U+05D4 | ַ `U+05B7` HEBREW POINT PATAH |
| ו | וַ | U+05D5 | ַ `U+05B7` HEBREW POINT PATAH |
| נ | נ | U+05E0 |  |

---

### 16. its peace

| Form | Text |
|---|---|
| Syriac (consonantal) | ܫܠܡܗ |
| Syriac (voweled) | ܫܠܳܡܶܗ |
| Block (consonantal) | שלמה |
| Block (voweled) | שֶלַמַה |

**IPA phonemic:** /ʃlɑːmeh/  
**IPA phonetic (Eastern):** [ʃlɑː.ˈmeh]  
**IPA phonetic (Western):** [ʃlɔː.ˈmeh]  
**Stress:** milra (final)  
**Source:** Matthew 10:12

**Features demonstrated:**

- Shin /ʃ/
- Lamadh /l/
- He suffix /-eh/ (3ms possessive)
- East-West vowel contrast

**Syriac segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ܫ | ܫ | U+072B |  |
| ܠ | ܠܳ | U+0720 | ܳ `U+0733` SYRIAC ZQAPHA ABOVE |
| ܡ | ܡܶ | U+0721 | ܶ `U+0736` SYRIAC RBASA ABOVE |
| ܗ | ܗ | U+0717 |  |

**Block segments:**

| Character | Combined | Unicode | Marks |
|---|---|---|---|
| ש | שֶ | U+05E9 | ֶ `U+05B6` HEBREW POINT SEGOL |
| ל | לַ | U+05DC | ַ `U+05B7` HEBREW POINT PATAH |
| מ | מַ | U+05DE | ַ `U+05B7` HEBREW POINT PATAH |
| ה | ה | U+05D4 |  |

---

## Unicode Reference

Unicode codepoint reference for all characters used in this guide, covering both Syriac (U+0700–U+074F) and Hebrew/Block Aramaic (U+0590–U+05FF) Unicode blocks.

### Syriac Unicode Block (U+0700–U+074F)

| Character | Unicode | Decimal | Name | Ipa |
|---|---|---|---|---|
| ܐ | `U+0710` | 1808 | SYRIAC LETTER ʾALAPH | /ʔ/ |
| ܒ | `U+0712` | 1810 | SYRIAC LETTER BETH | /b/ |
| ܓ | `U+0713` | 1811 | SYRIAC LETTER GAMAL | /ɡ/ |
| ܕ | `U+0715` | 1813 | SYRIAC LETTER DALATH | /d/ |
| ܗ | `U+0717` | 1815 | SYRIAC LETTER HE | /h/ |
| ܘ | `U+0718` | 1816 | SYRIAC LETTER WAW | /w/ |
| ܙ | `U+0719` | 1817 | SYRIAC LETTER ZAYN | /z/ |
| ܚ | `U+071A` | 1818 | SYRIAC LETTER KHETH | /ħ/ |
| ܛ | `U+071B` | 1819 | SYRIAC LETTER TETH | /tˤ/ |
| ܝ | `U+071D` | 1821 | SYRIAC LETTER YUDH | /j/ |
| ܟ | `U+071F` | 1823 | SYRIAC LETTER KAPH | /k/ |
| ܠ | `U+0720` | 1824 | SYRIAC LETTER LAMADH | /l/ |
| ܡ | `U+0721` | 1825 | SYRIAC LETTER MIM | /m/ |
| ܢ | `U+0722` | 1826 | SYRIAC LETTER NUN | /n/ |
| ܣ | `U+0723` | 1827 | SYRIAC LETTER SEMKATH | /s/ |
| ܥ | `U+0725` | 1829 | SYRIAC LETTER AYIN (E) | /ʕ/ |
| ܦ | `U+0726` | 1830 | SYRIAC LETTER PE | /p/ |
| ܨ | `U+0728` | 1832 | SYRIAC LETTER TSADE | /sˤ/ |
| ܩ | `U+0729` | 1833 | SYRIAC LETTER QAPH | /q/ |
| ܪ | `U+072A` | 1834 | SYRIAC LETTER RESH | /r/ |
| ܫ | `U+072B` | 1835 | SYRIAC LETTER SHIN | /ʃ/ |
| ܬ | `U+072C` | 1836 | SYRIAC LETTER TAW | /t/ |
| ܰ | `U+0730` | 1840 | SYRIAC PTHAHA ABOVE | /a/ |
| ܱ | `U+0731` | 1841 | SYRIAC PTHAHA BELOW | /a/ |
| ܲ | `U+0732` | 1842 | SYRIAC PTHAHA DOTTED | /a/ |
| ܳ | `U+0733` | 1843 | SYRIAC ZQAPHA ABOVE | /ɑ/ (E) or /ɔ/ (W) |
| ܴ | `U+0734` | 1844 | SYRIAC ZQAPHA BELOW | /ɑ/ (E) or /ɔ/ (W) |
| ܵ | `U+0735` | 1845 | SYRIAC ZQAPHA DOTTED | /ɑ/ (E) or /ɔ/ (W) |
| ܶ | `U+0736` | 1846 | SYRIAC RBASA ABOVE | /ɛ/ (E) or /e/ (W) |
| ܷ | `U+0737` | 1847 | SYRIAC RBASA BELOW | /ɛ/ (E) or /e/ (W) |
| ܸ | `U+0738` | 1848 | SYRIAC DOTTED ZLAMA HORIZONTAL | /e/ |
| ܹ | `U+0739` | 1849 | SYRIAC DOTTED ZLAMA ANGULAR | /e/ |
| ܺ | `U+073A` | 1850 | SYRIAC HBASA ABOVE | /i/ |
| ܻ | `U+073B` | 1851 | SYRIAC HBASA BELOW | /i/ |
| ܼ | `U+073C` | 1852 | SYRIAC HBASA-ESASA DOTTED | /i/ |
| ܽ | `U+073D` | 1853 | SYRIAC ESASA ABOVE | /o/ |
| ܾ | `U+073E` | 1854 | SYRIAC ESASA BELOW | /o/ |
| ܿ | `U+073F` | 1855 | SYRIAC RWAHA | /u/ |
| ݀ | `U+0740` | 1856 | SYRIAC FEMININE DOT | morphological |
| ݁ | `U+0741` | 1857 | SYRIAC QUSHSHAYA | hard (plosive) |
| ݂ | `U+0742` | 1858 | SYRIAC RUKKAKHA | soft (fricative) |
| ݇ | `U+0747` | 1863 | SYRIAC OBLIQUE LINE ABOVE | silent letter |

### Hebrew Unicode Block (U+0590–U+05FF)

*Used for Block Aramaic (Hebrew square script) representation of Peshitta text*

| Character | Unicode | Decimal | Name | Ipa |
|---|---|---|---|---|
| א | `U+05D0` | 1488 | HEBREW LETTER ʾALEPH | /ʔ/ |
| ב | `U+05D1` | 1489 | HEBREW LETTER BET | /b/ |
| ג | `U+05D2` | 1490 | HEBREW LETTER GIMEL | /ɡ/ |
| ד | `U+05D3` | 1491 | HEBREW LETTER DALET | /d/ |
| ה | `U+05D4` | 1492 | HEBREW LETTER HE | /h/ |
| ו | `U+05D5` | 1493 | HEBREW LETTER VAV | /w/ |
| ז | `U+05D6` | 1494 | HEBREW LETTER ZAYIN | /z/ |
| ח | `U+05D7` | 1495 | HEBREW LETTER CHET | /ħ/ |
| ט | `U+05D8` | 1496 | HEBREW LETTER TET | /tˤ/ |
| י | `U+05D9` | 1497 | HEBREW LETTER YOD | /j/ |
| כ | `U+05DB` | 1499 | HEBREW LETTER KAF | /k/ |
| ל | `U+05DC` | 1500 | HEBREW LETTER LAMED | /l/ |
| מ | `U+05DE` | 1502 | HEBREW LETTER MEM | /m/ |
| נ | `U+05E0` | 1504 | HEBREW LETTER NUN | /n/ |
| ס | `U+05E1` | 1505 | HEBREW LETTER SAMEKH | /s/ |
| ע | `U+05E2` | 1506 | HEBREW LETTER AYIN | /ʕ/ |
| פ | `U+05E4` | 1508 | HEBREW LETTER PE | /p/ |
| צ | `U+05E6` | 1510 | HEBREW LETTER TSADI | /sˤ/ |
| ק | `U+05E7` | 1511 | HEBREW LETTER QOF | /q/ |
| ר | `U+05E8` | 1512 | HEBREW LETTER RESH | /r/ |
| ש | `U+05E9` | 1513 | HEBREW LETTER SHIN | /ʃ/ |
| ת | `U+05EA` | 1514 | HEBREW LETTER TAV | /t/ |
| ך | `U+05DA` | 1498 | HEBREW LETTER FINAL KAF | /k/ or /x/ |
| ם | `U+05DD` | 1501 | HEBREW LETTER FINAL MEM | /m/ |
| ן | `U+05DF` | 1503 | HEBREW LETTER FINAL NUN | /n/ |
| ף | `U+05E3` | 1507 | HEBREW LETTER FINAL PE | /p/ or /f/ |
| ץ | `U+05E5` | 1509 | HEBREW LETTER FINAL TSADI | /sˤ/ |
| ְ | `U+05B0` | 1456 | HEBREW POINT SHEVA | /ə/ or ∅ |
| ֱ | `U+05B1` | 1457 | HEBREW POINT HATAF SEGOL | /ɛ̆/ |
| ֲ | `U+05B2` | 1458 | HEBREW POINT HATAF PATAH | /ă/ |
| ֳ | `U+05B3` | 1459 | HEBREW POINT HATAF QAMATS | /ɔ̆/ |
| ִ | `U+05B4` | 1460 | HEBREW POINT HIRIQ | /i/ |
| ֵ | `U+05B5` | 1461 | HEBREW POINT TSERE | /e/ |
| ֶ | `U+05B6` | 1462 | HEBREW POINT SEGOL | /ɛ/ |
| ַ | `U+05B7` | 1463 | HEBREW POINT PATAH | /a/ |
| ָ | `U+05B8` | 1464 | HEBREW POINT QAMATS | /ɑ/ or /ɔ/ |
| ֹ | `U+05B9` | 1465 | HEBREW POINT HOLAM | /o/ |
| ֻ | `U+05BB` | 1467 | HEBREW POINT QUBUTS | /u/ |
| ּ | `U+05BC` | 1468 | HEBREW POINT DAGESH | hard/gemination |
| ֽ | `U+05BD` | 1469 | HEBREW POINT METEG | secondary stress |
| ־ | `U+05BE` | 1470 | HEBREW PUNCTUATION MAQAF | word connector |
| ֿ | `U+05BF` | 1471 | HEBREW POINT RAFE | soft (fricative) |
| ׁ | `U+05C1` | 1473 | HEBREW POINT SHIN DOT | /ʃ/ |
| ׂ | `U+05C2` | 1474 | HEBREW POINT SIN DOT | /s/ |

## Numerical Values

Gematria (numerical values) of the Syriac and Block Aramaic alphabets. Both systems use the same traditional Semitic numerical assignment.

### Syriac Gematria

| Letter | Name | Value |
|---|---|---|
| ܐ | ʾAlaph | 1 |
| ܒ | Beth | 2 |
| ܓ | Gamal | 3 |
| ܕ | Dalath | 4 |
| ܗ | He | 5 |
| ܘ | Waw | 6 |
| ܙ | Zayn | 7 |
| ܚ | Kheth | 8 |
| ܛ | Teth | 9 |
| ܝ | Yudh | 10 |
| ܟ | Kaph | 20 |
| ܠ | Lamadh | 30 |
| ܡ | Mim | 40 |
| ܢ | Nun | 50 |
| ܣ | Semkath | 60 |
| ܥ | Ayin (E) | 70 |
| ܦ | Pe | 80 |
| ܨ | Tsade | 90 |
| ܩ | Qaph | 100 |
| ܪ | Resh | 200 |
| ܫ | Shin | 300 |
| ܬ | Taw | 400 |

### Block Aramaic Gematria

| Letter | Name | Value |
|---|---|---|
| א | ʾAleph | 1 |
| ב | Bet | 2 |
| ג | Gimel | 3 |
| ד | Dalet | 4 |
| ה | He | 5 |
| ו | Vav | 6 |
| ז | Zayin | 7 |
| ח | Chet | 8 |
| ט | Tet | 9 |
| י | Yod | 10 |
| כ | Kaf | 20 |
| ל | Lamed | 30 |
| מ | Mem | 40 |
| נ | Nun | 50 |
| ס | Samekh | 60 |
| ע | Ayin | 70 |
| פ | Pe | 80 |
| צ | Tsadi | 90 |
| ק | Qof | 100 |
| ר | Resh | 200 |
| ש | Shin | 300 |
| ת | Tav | 400 |

---

*Generated programmatically from `peshitta_pronunciation_guide.json` (v3.0.0). This Markdown file is derived from the audited JSON data — the JSON remains the source of truth.*
