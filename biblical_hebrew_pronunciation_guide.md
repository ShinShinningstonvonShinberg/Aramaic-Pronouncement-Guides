# Biblical Hebrew IPA Pronunciation Guide

**Version:** 1.0.0  
**Date:** 2026-04-01  
**Language:** Biblical Hebrew (Classical Hebrew) (ISO 639-3: `hbo`)  
**Encoding:** UTF-8  
**IPA Standard:** IPA (International Phonetic Alphabet, 2015 revision)  

Machine-readable IPA-based pronunciation guide for Biblical Hebrew (Tiberian tradition). All pronunciation data is encoded in the International Phonetic Alphabet (IPA) as the primary system, ensuring cross-linguistic accuracy and universality for AI-assisted language preservation.

**Script:** Hebrew square script (Ktav Merubah)

### Source Texts

**The Hebrew portions of the Hebrew Bible (Tanakh), encompassing Torah, Nevi'im, and Ketuvim**

- **Torah (Pentateuch):** Genesis, Exodus, Leviticus, Numbers, Deuteronomy
- **Nevi'im (Prophets):** Joshua, Judges, Samuel, Kings, Isaiah, Jeremiah, Ezekiel, The Twelve
- **Ketuvim (Writings):** Psalms, Proverbs, Job, Song of Songs, Ruth, Lamentations, Ecclesiastes, Esther, Daniel, Ezra-Nehemiah, Chronicles

*Excluded Aramaic portions:*

- Daniel 2:4b–7:28
- Ezra 4:8–6:18, 7:12–26
- Jeremiah 10:11
- Genesis 31:47


### Companion Files

- `peshitta_pronunciation_guide.json`
- `biblical_aramaic_pronunciation_guide.json`

### Notes

- Biblical Hebrew is written right-to-left in Hebrew square script
- The Tiberian niqqud system is the primary vocalization documented here
- All IPA transcriptions use the standard 2015 IPA chart notation
- Phonemic transcriptions use / / slashes; phonetic transcriptions use [ ] brackets
- Suprasegmentals: /ː/ marks vowel length; /ˈ/ marks primary stress; /ˤ/ marks pharyngealization
- This guide covers the same script and vocalization system as the Biblical Aramaic companion guide; the differences are primarily linguistic (morphology, phonological rules, stress patterns)

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
15. [Pausal Forms](#pausal-forms)
16. [Definite Article](#definite-article)
17. [Phonological Rules](#phonological-rules)
18. [Vocalization Traditions](#vocalization-traditions)
19. [Cantillation Overview](#cantillation-overview)
20. [Cross-Reference: Biblical Aramaic](#cross-reference-biblical-aramaic)
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

The complete phonemic inventory of Biblical Hebrew as vocalized in the Tiberian tradition, organized by IPA categories

### Consonant Phonemes

All consonant phonemes of Biblical Hebrew arranged by place and manner of articulation (IPA standard layout)

**Total consonant phonemes:** 29  
22 letters yield 29 distinct consonant phonemes: 16 non-Begadkephat consonants (including both Shin /ʃ/ and Sin /s/) + 6 Begadkephat hard (plosive) + 6 Begadkephat soft (fricative) + labial-velar /w/ = 29

#### IPA Consonant Chart

IPA consonant chart for Biblical Hebrew (rows = manner, columns = place). Voiceless precedes voiced in each cell (IPA convention).

| Manner | Bilabial | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|---|---|---|---|---|---|---|---|---|---|
| Plosive | p b |  | t d tˤ |  |  | k ɡ | q |  | ʔ |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill/fricative |  |  |  |  |  |  | ʁ |  |  |
| Fricative | f v | θ ð | s z sˤ | ʃ |  | x ɣ |  | ħ ʕ | h |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

*/w/ is labial-velar and not shown in this simplified chart.*

#### Notes by Place of Articulation

- **Bilabial:** /b/ and /v/ are allophones of Bet; /p/ and /f/ are allophones of Pe.
- **Dental:** /ð/ is soft Dalet; /θ/ is soft Tav
- **Alveolar:** /tˤ/ is Tet (emphatic); /sˤ/ is Tsadi (emphatic). /d/ and /ð/ are allophones of Dalet; /t/ and /θ/ are allophones of Tav.
- **Postalveolar:** /ʃ/ is Shin (שׁ). Sin (שׂ) = /s/ is classified under alveolar.
- **Palatal:** /j/ is Yod (consonantal)
- **Velar:** /ɡ/ and /ɣ/ are allophones of Gimel; /k/ and /x/ are allophones of Kaf
- **Uvular:** /q/ is Qof
- **Pharyngeal:** /ħ/ is Chet; /ʕ/ is Ayin
- **Glottal:** /ʔ/ is Alef; /h/ is He
- **Labial velar:** /w/ is Vav (consonantal)

### Vowel Phonemes

The vowel phonemes of Biblical Hebrew in the Tiberian tradition, arranged by the IPA vowel quadrilateral (height × backness × rounding)

**Tiberian vowel count:** 7  
7 primary vowel qualities plus 3 hataf (ultra-short) variants and schwa

#### IPA Vowel Chart

IPA vowel quadrilateral for Biblical Hebrew (Tiberian tradition)

| Height | Front unrounded | Central | Back rounded |
|---|---|---|---|
| close | i |  | u |
| close-mid | e |  | o |
| open-mid | ɛ |  | ɔ |
| open | a |  |  |

#### Vowel Phoneme Inventory

| Ipa | Height | Backness | Rounding | Tiberian sign | Distribution |
|---|---|---|---|---|---|
| i | close | front | unrounded | Hiriq | Short /i/ or long /iː/ (Hiriq gadol with Yod) |
| e | close-mid | front | unrounded | Tsere | Close-mid front vowel; long when written plene with Yod |
| ɛ | open-mid | front | unrounded | Segol | Open-mid front vowel; short |
| a | open | front | unrounded | Patach | Open front unrounded vowel; short |
| ɔ | open-mid | back | rounded | Qamats | Qamats gadol = /ɔ/; Qamats qatan = /ɔ/ in closed unaccented syllable |
| o | close-mid | back | rounded | Holam | Close-mid back rounded vowel; long when written plene with Vav |
| u | close | back | rounded | Qubuts/Shuruq | Close back rounded vowel; Shuruq (Vav+dagesh) for plene writing |

#### Reduced Vowels

| Ipa | Name | Description |
|---|---|---|
| ə | Shva (mobile) | Mid-central vowel; occurs as shva na (mobile) in specific contexts |
| ɛ̆ | Hataf Segol | Ultra-short open-mid front vowel; under guttural consonants |
| ă | Hataf Patach | Ultra-short open front vowel; under guttural consonants |
| ɔ̆ | Hataf Qamats | Ultra-short open-mid back rounded vowel; under guttural consonants |

## Consonants

The 22 consonant letters of the Hebrew square script used for Biblical Hebrew, with full IPA phonological descriptions. Each letter includes place of articulation, manner of articulation, voicing, and all allophonic variants.

**Letter count:** 22 | **Effective phonemes:** 23  
22 letters produce 23 base consonant phonemes because Shin (ש) has two values: /ʃ/ (shin) and /s/ (sin)

| # | Hebrew Name | Transliteration | Character | Unicode | IPA Phoneme | IPA Phonetic | Place | Manner | Voicing | Bgdkpt | Emph. | Gutt. | Final |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | אָלֶף | ʾAlef | א | `U+05D0` | /ʔ/ | [ʔ] | glottal | plosive | voiceless |  |  | ✓ |  |
| 2 | בֵּית | Bet | ב | `U+05D1` | /b/ |  | bilabial | plosive (hard) / fricative (soft) | voiced | ✓ |  |  |  |
| 3 | גִּימֶל | Gimel | ג | `U+05D2` | /ɡ/ |  | velar | plosive (hard) / fricative (soft) | voiced | ✓ |  |  |  |
| 4 | דָּלֶת | Dalet | ד | `U+05D3` | /d/ |  |  | plosive (hard) / fricative (soft) | voiced | ✓ |  |  |  |
| 5 | הֵא | He | ה | `U+05D4` | /h/ | [h] | glottal | fricative | voiceless |  |  | ✓ |  |
| 6 | וָו | Vav | ו | `U+05D5` | /w/ | [w] | labial-velar | approximant | voiced |  |  |  |  |
| 7 | זַיִן | Zayin | ז | `U+05D6` | /z/ | [z] | alveolar | fricative | voiced |  |  |  |  |
| 8 | חֵית | Chet | ח | `U+05D7` | /ħ/ | [ħ] | pharyngeal | fricative | voiceless |  |  | ✓ |  |
| 9 | טֵית | Tet | ט | `U+05D8` | /tˤ/ | [tˤ] | alveolar | plosive (emphatic) | voiceless |  | ✓ |  |  |
| 10 | יוֹד | Yod | י | `U+05D9` | /j/ | [j] | palatal | approximant | voiced |  |  |  |  |
| 11 | כָּף | Kaf | כ | `U+05DB` | /k/ |  | velar | plosive (hard) / fricative (soft) | voiceless | ✓ |  |  | ✓ |
| 12 | לָמֶד | Lamed | ל | `U+05DC` | /l/ | [l] | alveolar | lateral_approximant | voiced |  |  |  |  |
| 13 | מֵים | Mem | מ | `U+05DE` | /m/ | [m] | bilabial | nasal | voiced |  |  |  | ✓ |
| 14 | נוּן | Nun | נ | `U+05E0` | /n/ | [n] | alveolar | nasal | voiced |  |  |  | ✓ |
| 15 | סָמֶךְ | Samekh | ס | `U+05E1` | /s/ | [s] | alveolar | fricative | voiceless |  |  |  |  |
| 16 | עַיִן | Ayin | ע | `U+05E2` | /ʕ/ | [ʕ] | pharyngeal | fricative | voiced |  |  | ✓ |  |
| 17 | פֵּא | Pe | פ | `U+05E4` | /p/ |  | bilabial (hard) / labiodental (soft) | plosive (hard) / fricative (soft) | voiceless | ✓ |  |  | ✓ |
| 18 | צָדֵי | Tsadi | צ | `U+05E6` | /sˤ/ | [sˤ] | alveolar | fricative (emphatic) | voiceless |  | ✓ |  | ✓ |
| 19 | קוֹף | Qof | ק | `U+05E7` | /q/ | [q] | uvular | plosive | voiceless |  |  |  |  |
| 20 | רֵישׁ | Resh | ר | `U+05E8` | /ʁ/ | [ʁ] | uvular | fricative | voiced |  |  |  |  |
| 21 | שִׁין | Shin | ש | `U+05E9` |  |  |  | fricative | voiceless |  |  |  |  |
| 22 | תָּו | Tav | ת | `U+05EA` | /t/ |  |  | plosive (hard) / fricative (soft) | voiceless | ✓ |  |  |  |

## Begadkephat

The six Begadkephat consonants (בגדכפת) that alternate between plosive (stop) and fricative pronunciation. In Biblical Hebrew, the plosive form is marked by Dagesh lene (U+05BC); the fricative form occurs without dagesh, typically after a vowel.

**Marking system:**

- **Hard marker:** Dagesh lene (U+05BC) — dot inside letter
- **Soft marker:** Absence of dagesh (or Rafe U+05BF in some manuscripts)
- **Contrast with peshitta:** Peshitta Syriac uses two separate marks: Qushaya (U+0741) for hard and Rukkakha (U+0742) for soft. Biblical Hebrew uses presence/absence of a single dagesh dot.

**Spirantization rule:** A Begadkephat letter is realized as a fricative (soft) when it immediately follows a vowel sound and does not carry dagesh forte (gemination). It is realized as a plosive (hard) word-initially, after a consonant, or when carrying dagesh.

| Letter | Name | Hard ipa | Soft ipa | Hard place | Soft place | Hard manner | Soft manner | Voicing | Hard features | Soft features |
|---|---|---|---|---|---|---|---|---|---|---|
| ב | Bet | [b] | [v] | bilabial | labiodental | plosive | fricative | voiced | +voiced, +bilabial, +plosive, -continuant | +voiced, +labiodental, +fricative, +continuant |
| ג | Gimel | [ɡ] | [ɣ] | velar | velar | plosive | fricative | voiced | +voiced, +velar, +plosive, -continuant | +voiced, +velar, +fricative, +continuant |
| ד | Dalet | [d] | [ð] | alveolar | dental | plosive | fricative | voiced | +voiced, +alveolar, +plosive, -continuant | +voiced, +dental, +fricative, +continuant |
| כ | Kaf | [k] | [x] | velar | velar | plosive | fricative | voiceless | -voiced, +velar, +plosive, -continuant | -voiced, +velar, +fricative, +continuant |
| פ | Pe | [p] | [f] | bilabial | labiodental | plosive | fricative | voiceless | -voiced, +bilabial, +plosive, -continuant | -voiced, +labiodental, +fricative, +continuant |
| ת | Tav | [t] | [θ] | alveolar | dental | plosive | fricative | voiceless | -voiced, +alveolar, +plosive, -continuant | -voiced, +dental, +fricative, +continuant |

## Dagesh System

The dagesh is a single dot placed inside a Hebrew letter (U+05BC). It serves two entirely different phonological functions depending on context. This dual function is unique to the Hebrew/Aramaic script and has no parallel in Syriac.

**Unicode:** `U+05BC` — Character: ּ  

### Dagesh Lene

Marks the plosive (hard/stop) pronunciation of a Begadkephat letter

**Phonological effect:** Blocks spirantization; letter is realized as plosive rather than fricative  
**Applies to:** Only the 6 Begadkephat letters: ב ג ד כ פ ת  

**Conditions:**

- Word-initial position
- After a consonant (including silent shva)
- After a major disjunctive cantillation accent (pause)


**Examples:**

- בּ [b] — Bet with dagesh lene = plosive
- כּ [k] — Kaf with dagesh lene = plosive


### Dagesh Forte

Indicates gemination (consonant doubling/lengthening)

**Phonological effect:** The consonant is phonologically doubled: the coda of the preceding syllable and the onset of the following syllable  
**Applies to:** Almost any consonant letter (except gutturals אהחע and usually ר)  

**Conditions:**

- Always preceded by a vowel (never word-initial)
- The preceding syllable is closed by the first half of the geminate


**Examples:**

- הַמֶּלֶךְ /ham.mɛlɛx/ — Definite article causes dagesh forte in Mem: the king
- דִּבֵּר /dib.bɛr/ — Piel verb stem: dagesh forte in second root letter


**Subtypes:**

- **Conjunctive:** Compensates for assimilated Nun: מִנְ + ד → מִדּ (min + d → mid.d-)
- **Compensatory:** After short vowel when expected gemination occurs
- **Characteristic:** Inherent in certain morphological patterns (e.g., Piel verb stem)
- **Article dagesh:** The Hebrew definite article הַ causes dagesh forte on the following consonant


### Disambiguation Rule

If the letter is a Begadkephat letter and the dagesh could be either lene or forte, determine by context: dagesh lene occurs only when no vowel precedes (word-initial or post-consonantal); dagesh forte always has a preceding vowel. In a Begadkephat letter with dagesh forte, BOTH effects apply: the letter is geminated AND realized as a plosive.

### Mappiq

A dagesh-like dot inside final He (הּ) that indicates He is a true consonant /h/ rather than a silent mater lectionis  
**Unicode:** `U+05BC (same codepoint as dagesh)`  

## Vowel Diacritics

The complete Tiberian niqqud vowel system used to vocalize Biblical Hebrew texts. All vowel points are placed below or above the consonant they follow.

**System:** Tiberian (sublinear, developed by Masoretes of Tiberias c. 750–950 CE)  
**Total vowel signs:** 13

*13 vowel signs: 7 primary vowels + 1 shva + 3 hataf vowels + Holam Haser + Shuruq (composite)*

| Name | Unicode | Character | Ipa | Type | Position | Length | Height | Backness | Rounding | Note |
|---|---|---|---|---|---|---|---|---|---|---|
| Shva | U+05B0 | ְ | /ə/ or ∅ | reduced/silent | below | ultra-short or silent | mid | central | unrounded | Mobile shva = [ə]; quiescent shva = silent. See shva_system section. |
| Hataf Segol | U+05B1 | ֱ | /ɛ̆/ | reduced (hataf) | below | ultra-short | open-mid | front | unrounded | Ultra-short /ɛ/; used under guttural consonants (אהחע) |
| Hataf Patach | U+05B2 | ֲ | /ă/ | reduced (hataf) | below | ultra-short | open | front | unrounded | Ultra-short /a/; most common hataf vowel under gutturals |
| Hataf Qamats | U+05B3 | ֳ | /ɔ̆/ | reduced (hataf) | below | ultra-short | open-mid | back | rounded | Ultra-short /ɔ/; used under guttural consonants |
| Hiriq | U+05B4 | ִ | /i/ | short | below | short (or long with Yod) | close | front | unrounded | Hiriq qatan (short) alone; Hiriq gadol (long /iː/) when followed by Yod as mater lectionis |
| Tsere | U+05B5 | ֵ | /e/ | long | below | long | close-mid | front | unrounded | Close-mid front vowel; often long, especially with Yod mater lectionis |
| Segol | U+05B6 | ֶ | /ɛ/ | short | below | short | open-mid | front | unrounded | Open-mid front vowel; characteristic of segholate nouns |
| Patach | U+05B7 | ַ | /a/ | short | below | short | open | front | unrounded | Open front unrounded vowel; furtive patach occurs under final guttural |
| Qamats | U+05B8 | ָ | /ɔ/ | long | below | long | open-mid | back | rounded | Qamats gadol = /ɔ/ (long, in open or accented syllables). Qamats qatan = /ɔ/ in closed unaccented syllables. |
| Holam | U+05B9 | ֹ | /o/ | long | above | long | close-mid | back | rounded | Close-mid back rounded vowel; Holam male (with Vav) = /oː/ |
| Holam Haser | U+05BA | ֺ | /o/ | long | above | long | close-mid | back | rounded | Holam written without Vav carrier; used when Vav would be ambiguous |
| Qubuts | U+05BB | ֻ | /u/ | short | below | short | close | back | rounded | Close back rounded vowel; short /u/ |
| Shuruq | composite |  | /u/ | long | inline | long | close | back | rounded | Long /uː/ written as Vav (U+05D5) with dagesh (U+05BC). No separate codepoint. |

## Shva System

The shva (ְ, U+05B0) system is a critical feature of the Tiberian vocalization. Shva can be either mobile (na, pronounced as /ə/) or quiescent (nach, silent). Correct identification determines syllable structure and pronunciation.

**Unicode:** `U+05B0` — Character: ְ


### Shva Na

**Name:** Shva Na (Mobile Shva)  
**Ipa:** /ə/  
**Description:** Pronounced as a short mid-central vowel [ə]; opens a new syllable  
**Rules:**

- **Word-initial shva:** Shva under the first consonant of a word is always mobile
- **Second of two consecutive shvas (non-final):** When two shvas appear in sequence within a word, the second is mobile
- **After a long vowel:** Shva following a long vowel is mobile
- **Under a letter with dagesh forte:** Shva under a geminated consonant is mobile (it follows the second half of the geminate)
- **Under the first of two identical consonants:** To prevent ambiguity, the shva is mobile


### Shva Nach

**Name:** Shva Nach (Quiescent Shva)  
**Ipa:** ∅ (silent)  
**Description:** Silent; closes the preceding syllable. Does not represent any vowel sound.  
**Rules:**

- **Word-final shva:** Shva at the end of a word is always quiescent (silent)
- **First of two consecutive shvas (non-final):** When two shvas appear in sequence, the first is quiescent (closes syllable)
- **After a short vowel in a closed syllable:** Shva after a short vowel closes that syllable



## Hataf Vowels

Three ultra-short (reduced) vowels unique to the Tiberian vocalization system. They replace simple shva under guttural consonants (אהחע), which cannot take ordinary shva. Each hataf vowel preserves the quality of its corresponding full vowel but in ultra-short duration.

**Guttural consonants:**  Alef (/ʔ/),  He (/h/),  Chet (/ħ/),  Ayin (/ʕ/)

| Name | Unicode | Character | Ipa | Corresponding full vowel | Height | Backness | Rounding | Duration | Typical contexts | Example |
|---|---|---|---|---|---|---|---|---|---|---|
| Hataf Segol | U+05B1 | ֱ | /ɛ̆/ | Segol /ɛ/ | open-mid | front | unrounded | ultra-short | Under א and ה most commonly | אֱלֹהִים /ʔɛ̆.lo.him/ (God) |
| Hataf Patach | U+05B2 | ֲ | /ă/ | Patach /a/ | open | front | unrounded | ultra-short | Most common hataf vowel; used under all four gutturals | חֲלוֹם /ħă.lom/ (dream) |
| Hataf Qamats | U+05B3 | ֳ | /ɔ̆/ | Qamats /ɔ/ | open-mid | back | rounded | ultra-short | Under gutturals, especially in specific morphological patterns | חֳלִי /ħɔ̆.li/ (my sickness) |

## Shin-Sin Distinction

The Hebrew letter Shin (ש, U+05E9) represents two distinct phonemes in Biblical Hebrew, distinguished by a diacritical dot. Sin is more common in Hebrew roots than in Biblical Aramaic.

### Base Letter

- **Character:** ש
- **Unicode:** U+05E9
- **Name:** Shin/Sin

## Final Form Letters

Five Hebrew letters have distinct glyph forms when they appear at the end of a word. These final (sofit) forms represent the SAME phoneme as their medial counterparts — the difference is purely orthographic, not phonological.

| Name | Medial | Medial unicode | Final | Final unicode | Ipa | Note |
|---|---|---|---|---|---|---|
| Kaf sofit | כ | U+05DB | ך | U+05DA | /k/ or /x/ | Final Kaf is typically spirantized [x] as it follows a vowel |
| Mem sofit | מ | U+05DE | ם | U+05DD | /m/ | Closed rectangular form in final position |
| Nun sofit | נ | U+05E0 | ן | U+05DF | /n/ | Extended descender form in final position |
| Pe sofit | פ | U+05E4 | ף | U+05E3 | /p/ or /f/ | Final Pe is typically spirantized [f] as it follows a vowel |
| Tsadi sofit | צ | U+05E6 | ץ | U+05E5 | /sˤ/ | Extended descender form in final position |

## Consonant-Vowel IPA Matrix

IPA matrix for all consonant-vowel combinations in Biblical Hebrew. 29 consonant sounds × 11 vowels.

**Consonants:** 29 | **Vowels:** 11 | **Total combinations:** 319

The full matrix maps each consonant against the vowel set. Each cell shows the IPA of the consonant + vowel combination.

| Consonant | IPA | Hiriq | Tsere | Segol | Patach | Qamats | Holam | Qubuts | Shva (mobile) | Hataf Segol | Hataf Patach | Hataf Qamats |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alef | ʔ | ʔi | ʔe | ʔɛ | ʔa | ʔɔ | ʔo | ʔu | ʔə | ʔɛ̆ | ʔă | ʔɔ̆ |
| Bet (hard) | b | bi | be | bɛ | ba | bɔ | bo | bu | bə | bɛ̆ | bă | bɔ̆ |
| Bet (soft) | v | vi | ve | vɛ | va | vɔ | vo | vu | və | vɛ̆ | vă | vɔ̆ |
| Gimel (hard) | ɡ | ɡi | ɡe | ɡɛ | ɡa | ɡɔ | ɡo | ɡu | ɡə | ɡɛ̆ | ɡă | ɡɔ̆ |
| Gimel (soft) | ɣ | ɣi | ɣe | ɣɛ | ɣa | ɣɔ | ɣo | ɣu | ɣə | ɣɛ̆ | ɣă | ɣɔ̆ |
| Dalet (hard) | d | di | de | dɛ | da | dɔ | do | du | də | dɛ̆ | dă | dɔ̆ |
| Dalet (soft) | ð | ði | ðe | ðɛ | ða | ðɔ | ðo | ðu | ðə | ðɛ̆ | ðă | ðɔ̆ |
| He | h | hi | he | hɛ | ha | hɔ | ho | hu | hə | hɛ̆ | hă | hɔ̆ |
| Vav | w | wi | we | wɛ | wa | wɔ | wo | wu | wə | wɛ̆ | wă | wɔ̆ |
| Zayin | z | zi | ze | zɛ | za | zɔ | zo | zu | zə | zɛ̆ | ză | zɔ̆ |
| Chet | ħ | ħi | ħe | ħɛ | ħa | ħɔ | ħo | ħu | ħə | ħɛ̆ | ħă | ħɔ̆ |
| Tet | tˤ | tˤi | tˤe | tˤɛ | tˤa | tˤɔ | tˤo | tˤu | tˤə | tˤɛ̆ | tˤă | tˤɔ̆ |
| Yod | j | ji | je | jɛ | ja | jɔ | jo | ju | jə | jɛ̆ | jă | jɔ̆ |
| Kaf (hard) | k | ki | ke | kɛ | ka | kɔ | ko | ku | kə | kɛ̆ | kă | kɔ̆ |
| Kaf (soft) | x | xi | xe | xɛ | xa | xɔ | xo | xu | xə | xɛ̆ | xă | xɔ̆ |
| Lamed | l | li | le | lɛ | la | lɔ | lo | lu | lə | lɛ̆ | lă | lɔ̆ |
| Mem | m | mi | me | mɛ | ma | mɔ | mo | mu | mə | mɛ̆ | mă | mɔ̆ |
| Nun | n | ni | ne | nɛ | na | nɔ | no | nu | nə | nɛ̆ | nă | nɔ̆ |
| Samekh | s | si | se | sɛ | sa | sɔ | so | su | sə | sɛ̆ | să | sɔ̆ |
| Ayin | ʕ | ʕi | ʕe | ʕɛ | ʕa | ʕɔ | ʕo | ʕu | ʕə | ʕɛ̆ | ʕă | ʕɔ̆ |
| Pe (hard) | p | pi | pe | pɛ | pa | pɔ | po | pu | pə | pɛ̆ | pă | pɔ̆ |
| Pe (soft) | f | fi | fe | fɛ | fa | fɔ | fo | fu | fə | fɛ̆ | fă | fɔ̆ |
| Tsadi | sˤ | sˤi | sˤe | sˤɛ | sˤa | sˤɔ | sˤo | sˤu | sˤə | sˤɛ̆ | sˤă | sˤɔ̆ |
| Qof | q | qi | qe | qɛ | qa | qɔ | qo | qu | qə | qɛ̆ | qă | qɔ̆ |
| Resh | ʁ | ʁi | ʁe | ʁɛ | ʁa | ʁɔ | ʁo | ʁu | ʁə | ʁɛ̆ | ʁă | ʁɔ̆ |
| Shin | ʃ | ʃi | ʃe | ʃɛ | ʃa | ʃɔ | ʃo | ʃu | ʃə | ʃɛ̆ | ʃă | ʃɔ̆ |
| Sin | s | si | se | sɛ | sa | sɔ | so | su | sə | sɛ̆ | să | sɔ̆ |
| Tav (hard) | t | ti | te | tɛ | ta | tɔ | to | tu | tə | tɛ̆ | tă | tɔ̆ |
| Tav (soft) | θ | θi | θe | θɛ | θa | θɔ | θo | θu | θə | θɛ̆ | θă | θɔ̆ |

## Diacritical Marks

Non-vowel diacritical marks used in Biblical Hebrew texts with their Unicode codepoints and phonological functions.

| Name | Character | Unicode | Position | Functions |
|---|---|---|---|---|
| Dagesh / Mappiq | ּ | `U+05BC` | inside letter | Dagesh lene: marks plosive pronunciation in Begadkephat letters; Dagesh forte: marks gemination (doubling) in any eligible letter; Mappiq: in final He (הּ), marks consonantal /h/ |
| Rafe | ֿ | `U+05BF` | above letter | Horizontal bar indicating soft (fricative) pronunciation of Begadkephat letter; explicitly marks absence of dagesh. Rare in printed texts but found in some manuscripts. |
| Shin dot | ׁ | `U+05C1` | upper-right of Shin | Distinguishes Shin /ʃ/ from Sin /s/. Placed upper-right on ש. |
| Sin dot | ׂ | `U+05C2` | upper-left of Shin | Distinguishes Sin /s/ from Shin /ʃ/. Placed upper-left on ש. |
| Meteg (Siluq) | ֽ | `U+05BD` | below letter, left side | Marks secondary stress; prevents vowel reduction in its syllable. Also indicates that a following shva is mobile. |
| Maqaf | ־ | `U+05BE` | between words (inline) | Hyphen joining two or more words into a single phonological unit. The joined words share one primary stress (on the last word); preceding words lose their independent stress. |
| Paseq | ׀ | `U+05C0` | between words (inline) | Vertical bar indicating a pause or separation between words. Prevents phonological merging. |
| Sof Pasuq | ׃ | `U+05C3` | end of verse | Colon-like mark at the end of a verse. Marks the strongest disjunctive break. |

## Suprasegmentals

Prosodic features that extend beyond individual segments (consonants and vowels) in Biblical Hebrew.

### Stress

Biblical Hebrew has a phonologically significant stress system indicated by cantillation marks. Hebrew stress patterns are more complex and better documented than Biblical Aramaic.

**IPA notation:** /ˈ/ = primary stress (before stressed syllable); /ˌ/ = secondary stress

**Primary patterns:**

- **Milra:** Ultimate (final syllable) stress — the default and most common pattern in Biblical Hebrew
  - דָּבָר /dɔˈvɔr/ (word/thing)
  - שָׁלוֹם /ʃɔˈlom/ (peace)
- **Milel:** Penultimate stress — occurs in specific morphological patterns
  - **Segholate nouns:** Bisyllabic nouns of the pattern CeCeC — מֶלֶךְ /ˈmɛlɛx/ (king)
  - **Certain verb forms:** Some perfect 2ms and 1cs forms — כָּתַבְתָּ /kɔˈθav.tɔ/ (you wrote)
  - **Feminine nouns in -ֶת:** Segholate feminine forms — דַּעַת /ˈdaʕaθ/ (knowledge)

**Nasog achor:**

- **Definition:** Stress retraction to avoid consecutive stressed syllables (stress clash avoidance)
- **Mechanism:** When two words are closely connected (conjunctive accent) and both would have adjacent stresses, the first word retracts its stress to the penultimate syllable
- **Ipa effect:** Primary stress mark /ˈ/ moves one syllable earlier in the first word

**Waw consecutive stress:**

- **Wayyiqtol:** Waw-consecutive with imperfect (wayyiqtol): stress typically retracts to penultimate syllable
- **Weqatal:** Waw-consecutive with perfect (weqatal): stress may advance to final syllable

**Meteg effect:** Meteg (U+05BD) marks secondary stress and prevents vowel reduction

**Maqaf effect:** Words joined by maqaf (U+05BE) form a single stress unit; only the last word retains primary stress

### Gemination

Consonant doubling/lengthening, marked by dagesh forte (U+05BC)

**IPA notation:** Geminate consonants are written as two identical IPA symbols: /bb/, /kk/, /ll/, etc.

**Phonological effect:** The geminate consonant closes the preceding syllable (as coda) and opens the following syllable (as onset)

**Restrictions:** Guttural consonants (אהחע) and Resh (ר) typically resist gemination

### Vowel Length

Tiberian vocalization distinguishes long and short vowels, though length is not always contrastive.

**IPA notation:** /ː/ marks long vowels

**Long vowels:**

- Qamats /ɔː/
- Tsere /eː/
- Holam /oː/
- Hiriq gadol /iː/ (with Yod)
- Shuruq /uː/ (Vav+dagesh)

**Short vowels:**

- Patach /a/
- Segol /ɛ/
- Hiriq qatan /i/
- Qubuts /u/
- Qamats qatan /ɔ/

**Note:** In open accented syllables, vowels tend to be long; in closed unaccented syllables, vowels tend to be short.

### Syllable Structure

Biblical Hebrew syllable structure

**Pattern:** (C)V(C)

**Rules:**

- Every syllable must begin with a consonant (onset is obligatory)
- Open syllables (CV) typically contain long vowels
- Closed syllables (CVC) typically contain short vowels
- No syllable begins with a vowel; word-initial vowels have a glottal stop onset [ʔ]
- Complex onsets (CC-) are resolved by epenthetic shva

## Diphthongs

Diphthongs in Biblical Hebrew — vowel sequences that function as single phonological units within a syllable.

| IPA | Spelling | Tiberian Realization | Example Context | Note |
|---|---|---|---|---|
| /aj/ | Patach + Yod | [aj] | Plural masculine construct | May monophthongize to /eː/ in some environments |
| /aw/ | Patach/Qamats + Vav | [aw] | Found in some noun patterns | Frequently monophthongizes to /oː/ |
| /ej/ | Tsere + Yod | [ej] | Plural construct and pronominal suffixes | Common in demonstratives and plural endings |

*Diphthongs are identical across Biblical Hebrew, Biblical Aramaic, and Peshitta Syriac, with similar monophthongization patterns.*

## Pausal Forms

Biblical Hebrew has a systematic pattern of vowel changes at major pausal positions in the text. These pausal forms affect pronunciation significantly and have no direct parallel in Biblical Aramaic.

### Triggering Accents

Cantillation accents that trigger pausal vowel changes

**Primary:**

- **Silluq (סִלּוּק)** — End of verse (with Sof Pasuq)
- **Atnah (אַתְנָח)** — Major midverse division

**Secondary:**

- **Zaqef Qaton** — Occasionally triggers pausal forms when it marks a major syntactic break
- **Zaqef Gadol** — Occasionally triggers pausal forms
- **Segolta** — Rarely triggers pausal forms; generally weaker

**Poetic System:** Ole ve-Yored (עוֹלֶה וְיוֹרֵד) — In the poetic cantillation system (Psalms, Proverbs, Job), Ole ve-Yored functions as the strongest midverse disjunctive and triggers pausal forms


### Vowel Shifts

| Context vowel | Pausal vowel | Ipa shift | Description | Example context | Example pausal | Meaning |
|---|---|---|---|---|---|---|
| Patach /a/ | Qamats /ɔː/ | /a/ → /ɔː/ | Short open /a/ lengthens to long back /ɔː/ in pause | כָּתַב /kɔˈθav/ | כָּתָב /kɔˈθɔv/ | he wrote |
| Segol /ɛ/ | Tsere /eː/ | /ɛ/ → /eː/ | Short open-mid /ɛ/ raises to long close-mid /eː/ in pause | אֶרֶץ /ˈʔɛrɛsˤ/ | אָרֶץ /ˈʔɔːrɛsˤ/ | earth/land |
| Hiriq /i/ (in some forms) | Tsere /eː/ | /i/ → /eː/ | Short /i/ may lower to /eː/ in certain verb forms in pause | וַתֵּשְׁבִּי /vat.teːʃˈbi/ | וַתֵּשֶׁבִּי /vat.teːˈʃeːvi/ | and you sat (Ruth 3:18) |
| Shva (quiescent) /∅/ | Full vowel restored | ∅ → /ɔː/ or /a/ | In pause, reduced vowels may be restored to their original full quality | קָדְשׁוֹ /qɔðˈʃoː/ | קָדָשׁוֹ /qɔːðɔːˈʃoː/ | his holiness |

### Morphological Patterns

- Segholate nouns undergo regular pausal lengthening in the stressed syllable
- Strong verb forms: qal perfect 3ms shows /a/ → /ɔː/ in final syllable
- Pronominal suffixes may show pausal lengthening
- Nouns with doubly-closed syllables typically do NOT have separate pausal forms

*Pausal forms are a defining feature of Biblical Hebrew prosody. When extracting sample words from verse-final or atnah positions, the vowels may differ from their contextual (non-pausal) forms.*

## Definite Article

Biblical Hebrew uses a prefixed definite article הַ (ha-) that assimilates with the following consonant via dagesh forte. This is a Hebrew-specific feature; Biblical Aramaic uses a suffixed emphatic state (-א) instead.

### Basic Form

- **Prefix:** הַ
- **Ipa:** /ha/
- **Rule:** The article prefix הַ is added to the noun, and dagesh forte is placed in the following consonant to indicate gemination

### Rules

- **Default rule:** Before non-guttural, non-Resh consonants
  - Vowel: Patach /a/
  - IPA pattern: /haC.C.../
  - Example: הַמֶּלֶךְ /ham.mɛlɛx/ (the king)
- **Before gutturals (א ע) and Resh (ר):** These letters cannot take dagesh forte
  - Vowel: Qamats /ɔː/ (compensatory lengthening)
  - IPA pattern: /hɔːC.../
  - הָאִישׁ /hɔːʔiʃ/ (the man)
  - הָעִיר /hɔːʕir/ (the city)
  - הָרֹאשׁ /hɔːroʃ/ (the head)
- **Before ה and unaccented ח/ע with qamats:** Before He, or before Chet/Ayin when unaccented and followed by qamats
  - Vowel: Patach /a/ (no compensatory lengthening)
  - IPA pattern: /haC.../
  - הֶחָכָם /hɛħɔˈxɔm/ (the wise man)
  - הֶעָפָר /hɛʕɔˈfɔr/ (the dust)
- **Before accented ח and ה:** Before Chet or He when accented
  - Vowel: Patach /a/ (like default, but no dagesh)
  - IPA pattern: /haC.../
  - Example: הַחַג /haˈħaɡ/ (the festival)

### Contrast with Aramaic

Biblical Aramaic expresses definiteness through the emphatic state suffix /-ɔː/ (written -א), e.g., מַלְכָּא /mal.kɔː/ (the king). Hebrew uses a prefix; Aramaic uses a suffix.

## Phonological Rules

Systematic phonological processes that apply in Biblical Hebrew pronunciation.

### Rule 1: /b d g k p t/ → [v ð ɣ x f θ] after a vowel (when no dagesh is present)

**Formal:** `[-sonorant, +Begadkephat] → [+continuant] / V __`

**Note:** The most important allophonic rule. Does not apply word-initially or after a consonant.

### Rule 2: /n/ → ∅ / __ C (with gemination of following consonant)

**Formal:** `/n/ → Ci / __ Ci (where Ci = following consonant, which geminates)`

**Example:** input: /min.də/; output: /mid.də/; note: Nun assimilates to following consonant, shown by dagesh forte: מִדְּ

### Rule 3: Full vowels reduce to /ə/ in pretonic open syllables under certain morphological conditions

**Note:** This is a morphophonological process tied to word formation.

### Rule 4: Gutturals prefer /a/-colored vowels and take hataf vowels instead of simple shva

**Formal:** `/ə/ → /ă/ (or /ɛ̆/ or /ɔ̆/) / [+guttural] __`

**Note:** Guttural consonants also resist gemination (dagesh forte).

### Rule 5: A short /a/ (patach) is inserted BEFORE a final guttural (ח ע הּ) when preceded by a non-/a/ vowel

**Formal:** `∅ → [a] / V[-low] __ [+guttural]#`

**Note:** Written after the guttural in the script but pronounced BEFORE it: רוּחַ = /ruː.aħ/ not */ruː.ħa/

### Rule 6: Emphatic (pharyngealized) consonants spread their [+RTR] (retracted tongue root) feature to adjacent vowels

**Note:** Vowels adjacent to /tˤ/, /sˤ/, /q/ may be backed or lowered phonetically.

### Rule 7: A Begadkephat letter at the start of a word following a vowel-final word (without intervening pause) may spirantize

**Exception:** A strong disjunctive cantillation accent on the preceding word creates a pause, blocking cross-word spirantization.

### Rule 8: When a guttural rejects dagesh forte (gemination), the preceding vowel may lengthen to compensate

**Example:** Definite article before guttural: הַ + אִישׁ → הָאִישׁ /hɔːʔiʃ/

### Rule 9: At major pausal positions (silluq, atnah), certain vowels undergo systematic lengthening

**Note:** See pausal_forms section for full details.

**Vowel shifts:**

- /a/ → /ɔː/ (patach → qamats)
- /ɛ/ → /eː/ (segol → tsere)

### Rule 10: The article prefix הַ causes dagesh forte on the following consonant, with compensatory lengthening before gutturals and Resh

**Note:** See definite_article section for full rules.

### Rule 11: When two consecutive words would have adjacent stresses, the first word's stress retracts to avoid clash

**Formal:** `ˈσˈσ → ˈσσ + ˈσ (stress moves left in first word)`

**Note:** More productive in Hebrew than in Aramaic.

### Rule 12: Waw-consecutive wayyiqtol causes dagesh forte in the following consonant and may retract stress; weqatal may advance stress to final syllable

**Note:** Hebrew-specific; no Aramaic parallel.

### Rule 13: Qamats in a closed, unaccented syllable is qamats qatan /ɔ/ rather than qamats gadol /ɔː/

**Key patterns:**

- כָּל /kɔl/ (all) — closed syllable, qamats qatan
- חָכְמָה /ħɔx.mɔː/ — first syllable closed by shva nach = qamats qatan
- Qal infinitive construct patterns

## Vocalization Traditions

Three distinct vocalization traditions developed for marking vowels in Hebrew texts. This guide primarily documents the Tiberian tradition (standard), with comparative notes on the Babylonian and Palestinian systems. The Tiberian tradition is most thoroughly studied and documented for Biblical Hebrew.

### Tiberian

**Origin:** Tiberias, Galilee  
**Period:** c. 750–950 CE  
**Developers:** Ben Asher and Ben Naphtali Masoretic families  
**Mark position:** Sublinear (below consonants, with Holam above)  
**Vowel distinctions:** 7  
**Vowel inventory ipa:** /i/, /e/, /ɛ/, /a/, /ɔ/, /o/, /u/  
**Additional features:** 3 hataf vowels, Shva (mobile/quiescent), Dagesh (lene/forte), Full cantillation system (prose and poetic), Meteg for secondary stress  
**Status:** Canonical standard. All modern printed Hebrew Bibles use this system. The Aleppo Codex and Leningrad Codex represent the Ben Asher tradition.  



### Babylonian

**Origin:** Babylonia (Iraq)  
**Period:** c. 700–900 CE  
**Mark position:** Supralinear (above consonants)  
**Vowel distinctions:** 6  
**Vowel inventory ipa:** /i/, /e/, /a/, /ɔ/ or /o/, /u/, /ə/  
**Status:** Supplanted by Tiberian system. Preserved in some Yemenite traditions and early manuscript fragments.  



### Palestinian

**Origin:** Palestine (Land of Israel)  
**Period:** c. 700–900 CE  
**Mark position:** Supralinear (above consonants)  
**Vowel distinctions:** 5  
**Vowel inventory ipa:** /i/, /e/, /a/, /o/, /u/  
**Status:** Most communities followed Palestinian pronunciation while writing Tiberian signs.  



*The IPA values in this guide follow the Tiberian tradition as the standard reference. Users working with Babylonian or Palestinian vocalization manuscripts should apply the simplified vowel inventories listed above.*

## Cantillation Overview

Overview of the te'amim (cantillation marks) and their prosodic effects on pronunciation. Biblical Hebrew has TWO cantillation systems: one for the 21 prose books and one for the 3 poetic books (Psalms, Proverbs, Job — the 'emet' books).

*A full cantillation guide is beyond the scope of this pronunciation reference. This section documents only the prosodic/phonological effects relevant to pronunciation.*

**Relevance to pronunciation:** Cantillation marks indicate: (1) which syllable receives primary stress, (2) where pauses occur (affecting Begadkephat spirantization and pausal forms), (3) phrase grouping (affecting connected speech).

### Prose cantillation (21 books)

**Applies to:** All books of the Hebrew Bible except Psalms, Proverbs, and Job

**Disjunctive accents (Melakhim / Mafsikim):**

Create pauses/breaks of varying strength between phrases

- **Level 1: Silluq + Sof Pasuq / Atnah** — Verse division: Silluq marks the last stressed word; Atnah divides the verse into two halves
- **Level 2: Zaqef Qaton / Zaqef Gadol / Tiphcha** — Secondary phrase divisions
- **Level 3: Segolta / Shalshelet / Revia** — Tertiary phrase divisions
- **Level 4: Pashta / Yetiv / Tevir / Geresh / Gershayim** — Quaternary (weakest) divisions

**Phonological effect:** After a strong disjunctive pause, the next word's initial Begadkephat letter is realized as a plosive (as if word-initial), because the pause breaks the vowel-to-consonant connection.

**Conjunctive accents (Meshartim):**

Link words together within a phrase

**Accent marks:** Munach, Mercha, Mahpach, Darga, Azla/Qadma

**Phonological effect:** Words connected by conjunctive accents form a tight phonological unit; spirantization applies across word boundaries.

### Poetic cantillation (3 books: Psalms, Proverbs, Job)

**Applies to:** The three 'emet' (אמת) books: Psalms (תהלים), Proverbs (משׁלי), Job (איוב)

A distinct cantillation system with different accent names, different hierarchical structure, and different melodic traditions from the prose system.

**Disjunctive accents (Poetic):**

- **Level 1: Silluq + Sof Pasuq / Ole ve-Yored / Atnah** — Primary verse divisions. Ole ve-Yored is the highest-ranking midverse disjunctive in the poetic system.
- **Level 2: Revia Mugrash / Revia Gadol / Zaqef Qaton** — Secondary phrase divisions
- **Level 3: Tiphcha / Pazer / Mehuppakh Legarmeh** — Tertiary phrase divisions

**Phonological effect:** Same as prose: disjunctive pauses affect spirantization and may trigger pausal forms.

**Conjunctive accents (Poetic):**

**Accent marks:** Mercha, Munach, Illuj/Mehuppakh, Azla Legarmeh, Sinnorit

**Phonological effect:** Same as prose: connected words form phonological units.

**Key differences from prose system:**

- Ole ve-Yored replaces Zaqef as the primary midverse disjunctive
- Revia Mugrash is unique to the poetic system
- The hierarchy of disjunctive strength differs from the prose order
- Fewer distinct accent marks overall but more flexible phrase structure
- Atnah appears less frequently; some verses lack it entirely

## Cross-Reference: Biblical Aramaic

Systematic three-way mapping of phonological correspondences between Biblical Hebrew (this guide), Biblical Aramaic, and Peshitta Syriac. All three represent closely related Semitic languages sharing the same consonant inventory.

### Shared Features

- Same 22-consonant inventory with identical IPA values across all three
- Same Begadkephat spirantization pattern (same 6 consonant pairs, same IPA values)
- Same emphatic consonants: /tˤ/ (Tet), /sˤ/ (Tsadi/Sadhe), /q/ (Qof)
- Same guttural consonants: /ʔ/ (Alef/Alaph), /h/ (He), /ħ/ (Chet/Kheth), /ʕ/ (Ayin/E)
- Same basic syllable structure: (C)V(C)
- Same diphthongs: /aj/, /aw/

### Key Differences

| Feature | Biblical hebrew | Biblical aramaic | Peshitta syriac |
|---|---|---|---|
| Script | Hebrew square script (U+05D0–U+05EA) | Hebrew square script (identical) | Syriac script: Estrangela, Serto, Madnhaya (U+0700–U+074F) |
| Vowel system | Tiberian niqqud: 7 primary vowels + shva + 3 hataf = 11 vowel signs | Tiberian niqqud (identical system) | Eastern (7 vowels, dot-based) or Western (5 vowels, Greek-derived) |
| Shin/Sin distinction | שׁ /ʃ/ vs שׂ /s/ — Sin more common in Hebrew roots | שׁ /ʃ/ vs שׂ /s/ (identical) | ܨ /ʃ/ only — Syriac Sin is separate letter Semkath ܣ /s/ |
| Spirantization marking | Dagesh (U+05BC) = single mark; presence = plosive, absence = fricative | Dagesh (U+05BC) (identical) | Qushaya (U+0741) = hard; Rukkakha (U+0742) = soft; two explicit marks |
| Definite article | Prefix הַ (ha-) with dagesh forte on following consonant | Emphatic state suffix -א /-ɔː/ | Emphatic state suffix (similar to Aramaic) |
| Pausal forms | Systematic vowel changes at silluq/atnah positions | Less systematic pausal changes | No pausal form system |
| Stress patterns | Complex: milra (default), mil'el (segholates, etc.), nasog achor | Predominantly milra with fewer mil'el exceptions | Penultimate stress in Eastern; final stress in Western |
| Cantillation systems | Two systems: prose (21 books) + poetic (Psalms, Proverbs, Job) | Prose system only (Aramaic portions are in prose books) | No cantillation system |
| Waw-consecutive | Wayyiqtol/weqatal with stress shifts and dagesh forte | No waw-consecutive system | No waw-consecutive system |
| Qamats vowel | Tiberian Qamats = /ɔ/ (gadol and qatan) | Tiberian Qamats = /ɔ/ (identical) | Eastern Zqapha = /ɑ/; Western Zqapha = /ɔ/ |

### Consonant IPA Correspondence

The following table confirms that all 22 consonant IPA values are IDENTICAL across Biblical Hebrew, Biblical Aramaic, and Peshitta Syriac.

| Phoneme | Biblical hebrew | Biblical aramaic | Peshitta |
|---|---|---|---|
| /ʔ/ | א Alef | א Alef | ܐ Alaph |
| /b/~/v/ | ב Bet | ב Bet | ܒ Beth |
| /ɡ/~/ɣ/ | ג Gimel | ג Gimel | ܓ Gamal |
| /d/~/ð/ | ד Dalet | ד Dalet | ܕ Dalath |
| /h/ | ה He | ה He | ܗ He |
| /w/ | ו Vav | ו Vav | ܘ Waw |
| /z/ | ז Zayin | ז Zayin | ܙ Zayn |
| /ħ/ | ח Chet | ח Chet | ܚ Kheth |
| /tˤ/ | ט Tet | ט Tet | ܛ Teth |
| /j/ | י Yod | י Yod | ܝ Yudh |
| /k/~/x/ | כ Kaf | כ Kaf | ܟ Kaph |
| /l/ | ל Lamed | ל Lamed | ܠ Lamadh |
| /m/ | מ Mem | מ Mem | ܡ Mim |
| /n/ | נ Nun | נ Nun | ܢ Nun |
| /s/ | ס Samekh | ס Samekh | ܣ Semkath |
| /ʕ/ | ע Ayin | ע Ayin | ܥ E |
| /p/~/f/ | פ Pe | פ Pe | ܦ Pe |
| /sˤ/ | צ Tsadi | צ Tsadi | ܨ Sadhe |
| /q/ | ק Qof | ק Qof | ܩ Qaph |
| /ʁ/ | ר Resh | ר Resh | ܪ Rish |
| /ʃ/ | שׁ Shin | שׁ Shin | ܫ Shin |
| /t/~/θ/ | ת Tav | ת Tav | ܬ Taw |

## Sample Words — IPA Transcriptions

Sample words drawn from ACTUAL Biblical Hebrew texts with full IPA transcription, segmental breakdown, and syllabification. Each word is byte-identical to its source file. Segments are derived by slicing the actual word codepoints, not independently typed.

*All sample words are taken from the Hebrew portions of the Hebrew Bible as preserved in the workspace Niqqud/ folder. Words were chosen to showcase diverse phonological features: Begadkephat alternation, shva mobile/quiescent, hataf vowels, shin vs sin, dagesh lene vs forte, pausal forms, definite article, qamats qatan vs gadol.*

**Total sample words:** 15

### בְּרֵאשִׁית — In the beginning

**Word:** בְּרֵאשִׁית  
**Source:** Genesis 1:1  
**Source file:** `Niqqud/Genesis-Bereshit/genesis1_hebrew_verses.txt`  
**IPA transcription:** /bəʁeːˈʃiːθ/  
**Syllabification:** bə.ʁeː.ˈʃiːθ  
**Stress:** milra (final)

**Features demonstrated:**

- Begadkephat: Bet with dagesh lene → plosive /b/
- Shva mobile (after initial consonant) → /ə/
- Tsere → /eː/
- Shin (with shin dot) → /ʃ/
- Hiriq male (hiriq + yod) → /iː/
- Tav without dagesh → fricative /θ/

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| ב | Yes | שְׁוָא | bə | בְּ |
| ר | No | צֵירֵי | ʁeː | רֵ |
| א | No | — |  | א |
| שׁ | No | חִירִיק | ʃiː | שִׁ |
| ית | No | — | θ | ית |

---

### הַשָּׁמַיִם — the heavens

**Word:** הַשָּׁמַיִם  
**Source:** Genesis 1:1  
**Source file:** `Niqqud/Genesis-Bereshit/genesis1_hebrew_verses.txt`  
**IPA transcription:** /haʃʃɔːˈmajim/  
**Syllabification:** haʃ.ʃɔː.ˈma.jim  
**Stress:** milra (final)

**Features demonstrated:**

- Definite article הַ with dagesh forte on following consonant
- Dagesh forte in shin → gemination /ʃʃ/
- Shin (with shin dot) → /ʃ/
- Qamats gadol → /ɔː/
- Patach → /a/
- Hiriq + Yod → /jim/

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| ה | No | פַּתָח | ha | הַ |
| שׁ | Yes | קָמָץ | ʃʃɔː | שָּׁ |
| מ | No | פַּתָח | ma | מַ |
| ים | No | חִירִיק | jim | יִם |

---

### תֹהוּ — formless / void

**Word:** תֹהוּ  
**Source:** Genesis 1:2  
**Source file:** `Niqqud/Genesis-Bereshit/genesis1_hebrew_verses.txt`  
**IPA transcription:** /ˈθoːhuː/  
**Syllabification:** ˈθoː.huː  
**Stress:** mil'el (penultimate)

**Features demonstrated:**

- Tav without dagesh → fricative /θ/
- Holam → /oː/
- Shuruq (vav + dagesh) → /uː/
- Final He as mater lectionis (silent)

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| ת | No | חוֹלָם | θoː | תֹ |
| הו | No | שׁוּרוּק | huː | הוּ |

---

### עֶרֶב — evening

**Word:** עֶרֶב  
**Source:** Genesis 1:5  
**Source file:** `Niqqud/Genesis-Bereshit/genesis1_hebrew_verses.txt`  
**IPA transcription:** /ˈʕɛʁɛv/  
**Syllabification:** ˈʕɛ.ʁɛv  
**Stress:** mil'el (penultimate)

**Features demonstrated:**

- Ayin → pharyngeal fricative /ʕ/
- Segol → /ɛ/ (appears twice)
- Resh → uvular /ʁ/
- Bet without dagesh (after vowel) → fricative /v/ (Begadkephat spirantization)

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| ע | No | סֶגּוֹל | ʕɛ | עֶ |
| ר | No | סֶגּוֹל | ʁɛ | רֶ |
| ב | No | — | v | ב |

---

### וְאָהַבְתָּ — And you shall love

**Word:** וְאָהַבְתָּ  
**Source:** Deuteronomy 6:5  
**Source file:** `Niqqud/Deuteronomy-Devarim-Words/deuteronomy6_hebrew_verses.txt`  
**IPA transcription:** /vəʔɔːhavˈtɔː/  
**Syllabification:** və.ʔɔː.hav.ˈtɔː  
**Stress:** milra (final)

**Features demonstrated:**

- Conjunctive vav with shva → /və/
- Alef as glottal stop → /ʔ/
- Qamats gadol → /ɔː/
- He with patach → /ha/
- Bet without dagesh → fricative /v/ (Begadkephat)
- Tav with dagesh lene → plosive /t/
- Final qamats → /ɔː/

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| ו | No | שְׁוָא | və | וְ |
| א | No | קָמָץ | ʔɔː | אָ |
| ה | No | פַּתָח | ha | הַ |
| ב | No | שְׁוָא נָח | v | בְ |
| ת | Yes | קָמָץ | tɔː | תָּ |

---

### מִזְמוֹר — A psalm

**Word:** מִזְמוֹר  
**Source:** Psalm 23:1  
**Source file:** `Niqqud/Pslams-Tehillim-Praises/psalms23_hebrew_verses.txt`  
**IPA transcription:** /mizˈmoːʁ/  
**Syllabification:** miz.ˈmoːʁ  
**Stress:** milra (final)

**Features demonstrated:**

- Hiriq → /i/
- Shva nach (quiescent, closing syllable) → ∅
- Holam male (holam + vav) → /oː/
- Resh → /ʁ/

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| מ | No | חִירִיק | mi | מִ |
| ז | No | שְׁוָא נָח | z | זְ |
| מו | No | חוֹלָם מָלֵא | moː | מוֹ |
| ר | No | — | ʁ | ר |

---

### צַלְמָוֶת — shadow of death / deep darkness

**Word:** צַלְמָוֶת  
**Source:** Psalm 23:4  
**Source file:** `Niqqud/Pslams-Tehillim-Praises/psalms23_hebrew_verses.txt`  
**IPA transcription:** /sˤalˈmɔːvɛθ/  
**Syllabification:** sˤal.ˈmɔː.vɛθ  
**Stress:** milra (final)

**Features demonstrated:**

- Emphatic Tsadi → /sˤ/
- Patach → /a/
- Shva nach (closing syllable) → ∅
- Qamats gadol → /ɔː/
- Vav without dagesh (after vowel) → /v/ (Begadkephat spirantization)
- Segol → /ɛ/
- Tav without dagesh → fricative /θ/

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| צ | No | פַּתָח | sˤa | צַ |
| ל | No | שְׁוָא נָח | l | לְ |
| מ | No | קָמָץ | mɔː | מָ |
| ו | No | סֶגּוֹל | vɛ | וֶ |
| ת | No | — | θ | ת |

---

### קָדוֹשׁ — holy

**Word:** קָדוֹשׁ  
**Source:** Isaiah 6:3  
**Source file:** `Niqqud/Isaiah-Yeshayahu/isaiah6_hebrew_verses.txt`  
**IPA transcription:** /qɔːˈðoːʃ/  
**Syllabification:** qɔː.ˈðoːʃ  
**Stress:** milra (final)

**Features demonstrated:**

- Qof → uvular plosive /q/
- Qamats gadol → /ɔː/
- Dalet without dagesh → fricative /ð/ (Begadkephat)
- Holam male (holam + vav) → /oː/
- Shin → /ʃ/

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| ק | No | קָמָץ | qɔː | קָ |
| דו | No | חוֹלָם מָלֵא | ðoː | דוֹ |
| שׁ | No | — | ʃ | שׁ |

---

### זָכוֹר — Remember!

**Word:** זָכוֹר  
**Source:** Exodus 20:8  
**Source file:** `Niqqud/Exodus-Sh’mot-Names/exodus20_hebrew_verses.txt`  
**IPA transcription:** /zɔːˈxoːʁ/  
**Syllabification:** zɔː.ˈxoːʁ  
**Stress:** milra (final)

**Features demonstrated:**

- Zayin → /z/
- Qamats gadol → /ɔː/
- Kaf without dagesh → fricative /x/ (Begadkephat)
- Holam male → /oː/
- Resh → /ʁ/

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| ז | No | קָמָץ | zɔː | זָ |
| כו | No | חוֹלָם מָלֵא | xoː | כוֹ |
| ר | No | — | ʁ | ר |

---

### שְׂרָפִים — Seraphim (fiery ones)

**Word:** שְׂרָפִים  
**Source:** Isaiah 6:2  
**Source file:** `Niqqud/Isaiah-Yeshayahu/isaiah6_hebrew_verses.txt`  
**IPA transcription:** /səʁɔːˈfiːm/  
**Syllabification:** sə.ʁɔː.ˈfiːm  
**Stress:** milra (final)

**Features demonstrated:**

- Sin (with sin dot) → /s/ (contrast with shin /ʃ/)
- Shva mobile (word-initial) → /ə/
- Resh → /ʁ/
- Qamats gadol → /ɔː/
- Pe without dagesh → fricative /f/ (Begadkephat)
- Hiriq male (hiriq + yod) → /iː/
- Mem sofit (final mem) → /m/

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| שׂ | No | שְׁוָא | sə | שְׂ |
| ר | No | קָמָץ | ʁɔː | רָ |
| פ | No | חִירִיק | fiː | פִ |
| ים | No | — | m | ים |

---

### הָאָֽרֶץ — the earth

**Word:** הָאָֽרֶץ  
**Source:** Genesis 1:1  
**Source file:** `Niqqud/Genesis-Bereshit/genesis1_hebrew_verses.txt`  
**IPA transcription:** /hɔːˈʔɔːʁɛsˤ/  
**Syllabification:** hɔː.ˈʔɔː.ʁɛsˤ  
**Stress:** milra (final)

**Features demonstrated:**

- Definite article before Alef (guttural) → compensatory lengthening: patach→qamats
- Alef as glottal stop → /ʔ/
- Qamats gadol → /ɔː/
- Meteg (secondary stress marker)
- Segol → /ɛ/
- Resh → /ʁ/
- Tsadi (emphatic) → /sˤ/

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| ה | No | קָמָץ | hɔː | הָ |
| א | No | קָמָץ | ʔɔː | אָ |
| ר | No | סֶגּוֹל+מֶתֶג | ʁɛ | ֽרֶ |
| ץ | No | — | sˤ | ץ |

---

### כַּבֵּד — Honor!

**Word:** כַּבֵּד  
**Source:** Exodus 20:12  
**Source file:** `Niqqud/Exodus-Sh’mot-Names/exodus20_hebrew_verses.txt`  
**IPA transcription:** /kabˈbeːð/  
**Syllabification:** kab.ˈbeːð  
**Stress:** milra (final)

**Features demonstrated:**

- Kaf with dagesh lene → plosive /k/ (Begadkephat)
- Patach → /a/
- Bet with dagesh forte → gemination /bb/ (doubled consonant)
- Tsere → /eː/
- Dalet without dagesh → fricative /ð/ (Begadkephat)

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| כ | Yes | פַּתָח | ka | כַּ |
| ב | Yes | צֵירֵי | bbeː | בֵּ |
| ד | No | — | ð | ד |

---

### הִנְנִי — Here I am!

**Word:** הִנְנִי  
**Source:** Isaiah 6:8  
**Source file:** `Niqqud/Isaiah-Yeshayahu/isaiah6_hebrew_verses.txt`  
**IPA transcription:** /hinˈniː/  
**Syllabification:** hin.ˈniː  
**Stress:** milra (final)

**Features demonstrated:**

- He → /h/
- Hiriq → /i/
- Nun with shva nach → /n/ (closing syllable)
- Nun with hiriq → /niː/
- Final yod as mater lectionis (silent, extends /i/)

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| ה | No | חִירִיק | hi | הִ |
| נ | No | שְׁוָא נָח | n | נְ |
| ני | No | חִירִיק מָלֵא | niː | נִי |

---

### בְּכָל — with all

**Word:** בְּכָל  
**Source:** Deuteronomy 6:5  
**Source file:** `Niqqud/Deuteronomy-Devarim-Words/deuteronomy6_hebrew_verses.txt`  
**IPA transcription:** /bəˈxɔl/  
**Syllabification:** bə.ˈxɔl  
**Stress:** milra (final)

**Features demonstrated:**

- Bet with dagesh lene (after prefix shva) → plosive /b/ (Begadkephat)
- Shva mobile → /ə/
- Kaf without dagesh → fricative /x/ (Begadkephat)
- Qamats qatan → /ɔ/ (NOT gadol /ɔː/; in closed unaccented syllable before /l/)
- Lamed → /l/

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| ב | Yes | שְׁוָא | bə | בְּ |
| כ | No | קָמָץ קָטָן | xɔ | כָ |
| ל | No | — | l | ל |

---

### אֱלֹהִים — God

**Word:** אֱלֹהִים  
**Source:** Genesis 1:1  
**Source file:** `Niqqud/Genesis-Bereshit/genesis1_hebrew_verses.txt`  
**IPA transcription:** /ʔɛ̆loːˈhiːm/  
**Syllabification:** ʔɛ̆.loː.ˈhiːm  
**Stress:** milra (final)

**Features demonstrated:**

- Alef with hataf segol → /ʔɛ̆/ (ultra-short, guttural preference)
- Lamed with holam → /loː/
- He with hiriq → /hiː/
- Hiriq male (hiriq + yod) → /iː/
- Mem sofit → /m/

**Segments:**

| Consonant | Dagesh | Vowel sign | Ipa | Hebrew |
|---|---|---|---|---|
| א | No | חֲטַף סֶגּוֹל | ʔɛ̆ | אֱ |
| ל | No | חוֹלָם | loː | לֹ |
| ה | No | חִירִיק | hiː | הִ |
| ים | No | — | m | ים |

---

## Unicode Reference

Complete Unicode reference for the Hebrew block (U+0590–U+05FF) as used in Biblical Hebrew texts.

| Name | Character | Unicode | Hex | Decimal | Category | Ipa |
|---|---|---|---|---|---|---|
| ʾAlef | א | `U+05D0` | 05D0 | 1488 | consonant | /ʔ/ |
| Bet | ב | `U+05D1` | 05D1 | 1489 | consonant | /b/~/v/ |
| Gimel | ג | `U+05D2` | 05D2 | 1490 | consonant | /ɡ/~/ɣ/ |
| Dalet | ד | `U+05D3` | 05D3 | 1491 | consonant | /d/~/ð/ |
| He | ה | `U+05D4` | 05D4 | 1492 | consonant | /h/ |
| Vav | ו | `U+05D5` | 05D5 | 1493 | consonant | /w/ |
| Zayin | ז | `U+05D6` | 05D6 | 1494 | consonant | /z/ |
| Chet | ח | `U+05D7` | 05D7 | 1495 | consonant | /ħ/ |
| Tet | ט | `U+05D8` | 05D8 | 1496 | consonant | /tˤ/ |
| Yod | י | `U+05D9` | 05D9 | 1497 | consonant | /j/ |
| Kaf | כ | `U+05DB` | 05DB | 1499 | consonant | /k/~/x/ |
| Lamed | ל | `U+05DC` | 05DC | 1500 | consonant | /l/ |
| Mem | מ | `U+05DE` | 05DE | 1502 | consonant | /m/ |
| Nun | נ | `U+05E0` | 05E0 | 1504 | consonant | /n/ |
| Samekh | ס | `U+05E1` | 05E1 | 1505 | consonant | /s/ |
| Ayin | ע | `U+05E2` | 05E2 | 1506 | consonant | /ʕ/ |
| Pe | פ | `U+05E4` | 05E4 | 1508 | consonant | /p/~/f/ |
| Tsadi | צ | `U+05E6` | 05E6 | 1510 | consonant | /sˤ/ |
| Qof | ק | `U+05E7` | 05E7 | 1511 | consonant | /q/ |
| Resh | ר | `U+05E8` | 05E8 | 1512 | consonant | /ʁ/ |
| Shin | ש | `U+05E9` | 05E9 | 1513 | consonant | /ʃ/ or /s/ |
| Tav | ת | `U+05EA` | 05EA | 1514 | consonant | /t/~/θ/ |
| Kaf sofit | ך | `U+05DA` | 05DA | 1498 | final_form | /k/~/x/ |
| Mem sofit | ם | `U+05DD` | 05DD | 1501 | final_form | /m/ |
| Nun sofit | ן | `U+05DF` | 05DF | 1503 | final_form | /n/ |
| Pe sofit | ף | `U+05E3` | 05E3 | 1507 | final_form | /p/~/f/ |
| Tsadi sofit | ץ | `U+05E5` | 05E5 | 1509 | final_form | /sˤ/ |
| Shva | ְ | `U+05B0` | 05B0 | 1456 | vowel_point | /ə/ or ∅ |
| Hataf Segol | ֱ | `U+05B1` | 05B1 | 1457 | vowel_point | /ɛ̆/ |
| Hataf Patach | ֲ | `U+05B2` | 05B2 | 1458 | vowel_point | /ă/ |
| Hataf Qamats | ֳ | `U+05B3` | 05B3 | 1459 | vowel_point | /ɔ̆/ |
| Hiriq | ִ | `U+05B4` | 05B4 | 1460 | vowel_point | /i/ |
| Tsere | ֵ | `U+05B5` | 05B5 | 1461 | vowel_point | /e/ |
| Segol | ֶ | `U+05B6` | 05B6 | 1462 | vowel_point | /ɛ/ |
| Patach | ַ | `U+05B7` | 05B7 | 1463 | vowel_point | /a/ |
| Qamats | ָ | `U+05B8` | 05B8 | 1464 | vowel_point | /ɔ/ |
| Holam | ֹ | `U+05B9` | 05B9 | 1465 | vowel_point | /o/ |
| Holam Haser | ֺ | `U+05BA` | 05BA | 1466 | vowel_point | /o/ |
| Qubuts | ֻ | `U+05BB` | 05BB | 1467 | vowel_point | /u/ |
| Shuruq (composite) | וּ | `U+05D5 + U+05BC` | 05D5+05BC | 1493+1468 | vowel_composite | /u/ |
| Dagesh/Mappiq | ּ | `U+05BC` | 05BC | 1468 | diacritical |  |
| Meteg | ֽ | `U+05BD` | 05BD | 1469 | diacritical |  |
| Rafe | ֿ | `U+05BF` | 05BF | 1471 | diacritical |  |
| Shin Dot | ׁ | `U+05C1` | 05C1 | 1473 | diacritical |  |
| Sin Dot | ׂ | `U+05C2` | 05C2 | 1474 | diacritical |  |
| Maqaf | ־ | `U+05BE` | 05BE | 1470 | punctuation |  |
| Paseq | ׀ | `U+05C0` | 05C0 | 1472 | punctuation |  |
| Sof Pasuq | ׃ | `U+05C3` | 05C3 | 1475 | punctuation |  |

## Numerical Values

Gematria — the traditional numerical values assigned to each Hebrew letter. Values are identical across Biblical Hebrew, Biblical Aramaic, and Peshitta Syriac.

**System:** Units (1–9), Tens (10–90), Hundreds (100–400)

| Letter | Name | Value |
|---|---|---|
| א | Alef | 1 |
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

*Generated programmatically from `biblical_hebrew_pronunciation_guide.json` (v1.0.0). This Markdown file is derived from the audited JSON data — the JSON remains the source of truth.*
