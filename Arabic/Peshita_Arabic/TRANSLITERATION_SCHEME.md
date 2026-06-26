# Peshitta Arabic Transliteration Scheme

## Overview

This folder contains a **4-tier transliteration of the Peshitta**, generated
**deterministically** from the project's IPA pronunciation guides
(`IPA/Peshitta/**/<name>_ipa.txt`).

Every output character is produced by a single, rule-based converter
(`transliterate_ar.py`). There is no hand-editing and no machine-learning step: the
same IPA input always yields exactly the same output. The IPA guides are the single
source of truth; the four tiers are mechanical re-encodings of that phonetic data for
four different audiences.

The converter operates on the **phonetic** representation only. It splits text on
ASCII spaces (preserving them verbatim), segments each token using a longest-match
rule, and renders each segment through one of the tier tables. Any character not
covered by the tables is reported, so the corpus can never silently lose information
(the Latin tiers pass uncovered characters through unchanged; the Arabic tiers drop
them only after recording).

## The Semitic-sibling framing — the most faithful reader tier in the project

Arabic is the program's **first Semitic-sibling target**, and that single fact makes
this the most faithful, most nearly-reversible reader tier in the whole project — **a
"cousin-script" transcription that sits closer to Scholarly than to a folk
respelling.**

Every prior reader tier had to *lose* information: the CJK targets collapsed the
Semitic consonant inventory wholesale onto a syllabary or onto Pinyin/Zhuyin; the
Indo-European targets approximated it. Arabic does the opposite. As the third great
Semitic abjad — the same Proto-Semitic phonemes in the same abjad order as Syriac
(ܐܒܓܕ) and Hebrew (אבגד) — it natively hosts almost the entire Syriac/Aramaic
consonant inventory, **pharyngeals, emphatics, and interdentals included.** Of the 28
source consonants, **about 25 map 1:1 to a dedicated Arabic letter with zero loss**,
including the four classes that vanished in every prior target:

- **pharyngeals:** `ħ → ح`, `ʕ → ع`
- **emphatics:** `tˤ → ط`, `sˤ → ص`
- **interdentals:** `θ → ث`, `ð → ذ`
- **uvular / velars:** `q → ق`, `x → خ`, `ɣ → غ`

…plus `ʃ → ش` and `ʔ → ء`.

The Vocalized Arabic abjad is therefore best understood not as a respelling but as a
**fourth Semitic-script representation of the same phonology** — a near-scholarly,
near-reversible rendering that is **the inverse of the CJK collapse.** The complete
loss list is just **five merges** (documented in full below), and even vowel *length*
is preserved structurally via the matres lectionis.

## The Four Tiers

| Tier | Script | Audience | Philosophy |
|------|--------|----------|------------|
| **Scholarly** | Latin (language-neutral) | Semiticists, students of Syriac/Aramaic, anyone comparing against academic editions | Maximum fidelity. Standard scholarly diacritics (macrons for long vowels; underlined/dotted letters for spirantized and emphatic consonants; `ʾ` for *alaph* and `ʿ` for *ayin*). Nothing collapsed or dropped. **Byte-for-byte identical to the English Peshitta Scholarly tier.** |
| **Pretty** | Latin (language-neutral) | General readers who want accuracy and the look of the original | A readable middle ground. Long vowels keep their macrons; spirantized consonants use familiar digraphs (`sh`, `th`, `dh`, `kh`, `gh`, `v`); *ayin* `ʿ` is kept; *alaph* is dropped word-initially and written `'` elsewhere. **Byte-for-byte identical to the English Peshitta Pretty tier.** |
| **Vocalized** | Arabic abjad (native) | Readers of Arabic; teaching/Quranic pointed register | The **primary native-script reader tier.** Full harakat (fatḥa/kasra/ḍamma), sukun on coda consonants, shadda on geminates, long vowels carried by the matres lectionis (ا/و/ي) bearing their short haraka, and a deterministic bare-hamza policy. The pointed, fully-vowelled form. |
| **Unvocalized** | Arabic abjad (native) | Readers of Arabic; the everyday written register | Mechanically `Vocalized − harakat`: strip U+064B–U+0652 (and tatweel). The consonant skeleton plus matres exactly as Arabic is normally written. Derived from the primary tier, so the two abjad tiers are guaranteed mutually consistent. |

**Scholarly and Pretty are language-neutral Latin tiers reused verbatim** from the
English transducer (`English/Peshita_English/transliterate.py`); their byte-identity
across language folders is a deliberate invariant. **Vocalized and Unvocalized are the
two native-script reader tiers** — a native abjad plus its harakat-stripped
projection, mirroring the project's established "native-script + trivially-derived
sibling" cadence (Japanese kana, Chinese Simplified/Traditional, Korean Hangul/RR).

> **No romanization tier is shipped.** A romanized readback of the Arabic skeleton
> would be strictly dominated by — and lossier than — Scholarly, which already
> romanizes the same source *more* faithfully (it keeps the begadkephat values
> ṯ/ḏ/ḵ/ḇ and the e/o vowel qualities the Arabic mapping collapses). Materializing it
> would also risk advertising the Arabic merges as source features. The merges are
> documented here instead.

---

## Segmentation

Identical in spirit to every other transducer in the project: split on ASCII space
`" "` only (spaces preserved verbatim), then within each token apply a left-to-right
**longest match**:

1. consonant + `ˤ` (U+02E4) → **emphatic** segment (2 chars)
2. vowel (`a ɑ e i o u`) + `ː` (U+02D0) → **long-vowel** segment (2 chars)
3. otherwise → single char

The same segmentation feeds all four tiers.

---

## Mapping Tables (Latin tiers)

Tier order in every row below: **Scholarly | Pretty**. These reproduce the English
Peshitta transducer exactly.

### Plain Consonants

| IPA | Scholarly | Pretty |
|-----|-----------|--------|
| `b` | b | b |
| `ɡ` | g | g |
| `d` | d | d |
| `h` | h | h |
| `w` | w | w |
| `z` | z | z |
| `k` | k | k |
| `l` | l | l |
| `m` | m | m |
| `n` | n | n |
| `s` | s | s |
| `p` | p | p |
| `q` | q | q |
| `r` | r | r |
| `t` | t | t |
| `f` | f | f |
| `j` | y | y |

### Spirantized (begadkepat) Consonants

| IPA | Scholarly | Pretty |
|-----|-----------|--------|
| `v` | ḇ | v |
| `ʃ` | š | sh |
| `θ` | ṯ | th |
| `ð` | ḏ | dh |
| `x` | ḵ | kh |
| `ɣ` | ḡ | gh |
| `ħ` | ḥ | ḥ |

### Glottal / Pharyngeal

| IPA | Name | Scholarly | Pretty |
|-----|------|-----------|--------|
| `ʔ` | *alaph* | `ʾ` (always) | dropped word-initial, else `'` |
| `ʕ` | *ayin* | `ʿ` | `ʿ` |

### Emphatics (consonant + `ˤ`)

| IPA | Scholarly | Pretty |
|-----|-----------|--------|
| `tˤ` | ṭ | ṭ |
| `sˤ` | ṣ | ṣ |
| *any other* `Cˤ` | tier(C) + combining dot below ( ̣ ) | tier(C) + combining dot below ( ̣ ) |

### Short Vowels (no length mark)

| IPA | Scholarly | Pretty |
|-----|-----------|--------|
| `a` | a | a |
| `ɑ` | a | a |
| `e` | e | e |
| `i` | i | i |
| `o` | o | o |
| `u` | u | u |

### Long Vowels (vowel + `ː`)

| IPA | Scholarly | Pretty |
|-----|-----------|--------|
| `aː` | ā | ā |
| `ɑː` | ā | ā |
| `eː` | ē | ē |
| `iː` | ī | ī |
| `oː` | ō | ō |
| `uː` | ū | ū |

---

## Mapping Tables (Arabic tiers)

These are the **finalized** tables actually implemented in `transliterate_ar.py`.
Codepoints were validated against `unicodedata`; all output lies in the Arabic block
U+0600–U+06FF (harakat U+064B–U+0652, hamza U+0621, alif U+0627). The Vocalized and
Unvocalized tiers share these tables — Unvocalized is simply Vocalized with the
harakat stripped.

### The 1:1 sibling core (no loss)

| IPA | Letter | Codepoint | Name | IPA | Letter | Codepoint | Name |
|-----|:------:|:---------:|------|-----|:------:|:---------:|------|
| `ʔ` | ء | U+0621 | hamza | `s` | س | U+0633 | sīn |
| `b` | ب | U+0628 | bāʾ | `ʕ` | ع | U+0639 | ʿayn |
| `t` | ت | U+062A | tāʾ | `ɣ` | غ | U+063A | ghayn |
| `θ` | ث | U+062B | thāʾ | `f` | ف | U+0641 | fāʾ |
| `d` | د | U+062F | dāl | `q` | ق | U+0642 | qāf |
| `ð` | ذ | U+0630 | dhāl | `k` | ك | U+0643 | kāf |
| `r` | ر | U+0631 | rāʾ | `l` | ل | U+0644 | lām |
| `z` | ز | U+0632 | zāy | `m` | م | U+0645 | mīm |
| `ʃ` | ش | U+0634 | shīn | `n` | ن | U+0646 | nūn |
| `ħ` | ح | U+062D | ḥāʾ | `h` | ه | U+0647 | hāʾ |
| `x` | خ | U+062E | khāʾ | `w` | و | U+0648 | wāw (consonant) |
|     |     |         |      | `j` | ي | U+064A | yāʾ (consonant) |

### Emphatics (consonant + `ˤ`)

| IPA | Letter | Codepoint | Name |
|-----|:------:|:---------:|------|
| `tˤ` | ط | U+0637 | ṭāʾ |
| `sˤ` | ص | U+0635 | ṣād |

*ض (ḍād) and ظ (ẓāʾ) are unused: the source inventory has `/tˤ/` and `/sˤ/` but no
`/dˤ/` or `/ðˤ/`.*

### The three gaps — native gap policy (the only consonant non-1:1 mappings)

| IPA | Letter | Codepoint | Name | Effect |
|-----|:------:|:---------:|------|--------|
| `v` | ف | U+0641 | fāʾ | v/f merge (native Arabic lacks `/v/`) |
| `p` | ب | U+0628 | bāʾ | p/b merge (native Arabic lacks `/p/`) |
| `ɡ` | ج | U+062C | jīm | none — `ɡ` is the *sole* source of ج, so reversible in-corpus; `[dʒ]` in MSA, `[ɡ]` in Egyptian/Classical is a realization note only |

This follows MSA-pure orthography (and is exactly the probe's behavior). The
v/p/ɡ policy is the one genuine judgment call, and the native default is chosen for
maximum nativeness; a fully-reversible loan-letter variant (ڤ veh U+06A4 / پ peh
U+067E / گ gaf U+06AF) is documented as an optional switch in the design study.

### Vowels + harakat (3-quality collapse; length preserved via matres)

| IPA | Short (haraka) | Codepoint | Long (`Vː`) = haraka + mater | Codepoints | Note |
|-----|:--------------:|:---------:|:----------------------------:|:----------:|------|
| `a` | fatḥa ـَ | U+064E | fatḥa + alif → ـَا | U+064E U+0627 | exact |
| `ɑ` | fatḥa ـَ | U+064E | fatḥa + alif → ـَا | U+064E U+0627 | ɑ/a merge (already upstream) |
| `e` | kasra ـِ | U+0650 | kasra + yāʾ → ـِي | U+0650 U+064A | **e→i collapse** |
| `i` | kasra ـِ | U+0650 | kasra + yāʾ → ـِي | U+0650 U+064A | exact |
| `o` | ḍamma ـُ | U+064F | ḍamma + wāw → ـُو | U+064F U+0648 | **o→u collapse** |
| `u` | ḍamma ـُ | U+064F | ḍamma + wāw → ـُو | U+064F U+0648 | exact |

Vowels collapse deterministically onto Arabic's three qualities. **Vowel length is not
lost** — a long vowel is the short haraka *plus* the mater letter (ا/و/ي), so length
survives even into the bare Unvocalized tier (matres lie outside the stripped
U+064B–U+0652 range).

### Harakat / mark codepoints

| Mark | Glyph | Codepoint |
|------|:-----:|:---------:|
| fatḥa | ـَ | U+064E |
| kasra | ـِ | U+0650 |
| ḍamma | ـُ | U+064F |
| sukun | ـْ | U+0652 |
| shadda | ـّ | U+0651 |
| alif (mater) | ا | U+0627 |
| alif madda | آ | U+0622 |
| wāw (mater) | و | U+0648 |
| yāʾ (mater) | ي | U+064A |

### Structural rules

- **Hamza:** `ʔ → ء` bare hamza (U+0621) everywhere — one input, one codepoint;
  trivially deterministic, perfectly reversible, never produces an illegal seat.
- **Sukun (U+0652):** any coda consonant (no following vowel) takes sukun — making
  syllable structure explicit and the pointed output teachable (the `l` in
  `mel·θɑː`, the onset cluster `b` in `breːʃiːθ`).
- **Shadda (U+0651):** two adjacent identical consonants with no vowel between them
  fuse to one letter + shadda. Canonical per-letter order is `base + shadda +
  vowel-haraka`; the geminate carries the vowel of the segment after the twin
  (e.g. the `jj` in `…elijjɑːwn` → one ي + shadda).
- **Long vowel:** short haraka on the carrier **then** the mater letter — never a bare
  mater without its haraka in the Vocalized tier.
- **Bare initial vowel:** a word-initial vowel with no consonant carrier is seated on
  a carrier alif (U+0627). A *long* `a/ɑ` would otherwise be carrier-alif + fatḥa +
  alif-mater (two consecutive alifs, malformed), so it is written as a single **alif
  madda آ** (U+0622). (No gold verse triggers this — they all begin with `ʔ`.)
- **Hyphen:** ASCII `-` (U+002D) is emitted verbatim inside the isolate (e.g.
  `bar-ʔaba`); never converted to tatweel (which is cosmetic elongation, not a
  separator).
- **Unvocalized:** Vocalized with harakat (U+064B–U+0652) and tatweel (U+0640)
  stripped; matres and hamza survive.

---

## RTL / Bidi Handling

RTL layout is **entirely the renderer's job.** The transducer's responsibility is to
emit correct *content* in correct *logical order*; the renderer (UAX #9 + the font)
handles right-to-left presentation and contextual joining.

1. **Logical-order emission — no reordering, no shaping.** Base codepoints + harakat
   are emitted in reading order, exactly as the IPA tiers do. **Never** emit Arabic
   presentation forms (U+FE70–U+FEFF); **never** reverse bytes; **never** emit tatweel
   (U+0640). Contextual joining (initial/medial/final/isolated) is the renderer's job.
2. **Line format unchanged:** `<verse#>\t<text>\n`, UTF-8, no BOM, LF. Parsers split
   on the first TAB; the TAB (U+0009) is kept (not replaced with spaces).
3. **Verse-prefix bidi isolates.** `transliterate_line()` wraps **only** the Arabic
   body in bidi isolates: **RLI (U+2067)** before the text and **PDI (U+2069)** after,
   producing `<verse#>\t<U+2067>…<U+2069>\n`. The LTR ASCII verse-number gutter stays
   a left-anchored gutter, the Arabic body flows RTL, and the two never interfere —
   robust in terminals, editors, browsers, and Git diffs. These are the modern
   isolates, not the deprecated RLE/PDF (U+202B/U+202C).
4. **Scholarly / Pretty are Latin and are NOT wrapped** — preserving their byte
   identity with the English Peshitta.

**Unicode blocks/codepoints used:** Arabic U+0600–U+06FF (letters + harakat
U+064B–U+0652, hamza U+0621, alif U+0627); ASCII space U+0020, hyphen-minus U+002D,
TAB U+0009; bidi isolates U+2067 / U+2069.

---

## Documented Limitations

Honest but minimal. Arabic is a Semitic sibling of the source, so the reader tier is
**near-reversible — the inverse of the lossy CJK collapse.** The *complete, exhaustive*
loss list is **exactly five merges**, all forced by genuine inventory gaps:

| # | Merge | Type | Note |
|---|-------|------|------|
| 1 | `p / b → ب` | consonant | Native Arabic lacks `/p/`; p merges to b. Eliminated entirely under the optional loan-letter variant (پ). |
| 2 | `v / f → ف` | consonant | Native Arabic lacks `/v/`; v merges to f. Eliminated entirely under the optional loan-letter variant (ڤ). |
| 3 | `ɡ → ج` | realization | **Not a true collision** — the source has no `/dʒ/`, so every ج came from `ɡ` and is reversible in-corpus. Only a reading note: `[dʒ]` in MSA, `[ɡ]` in Egyptian/Classical. |
| 4 | `e → i` | vowel quality | Both share kasra. Identical to attested **Western (Serto) Syriac** vocalism. |
| 5 | `o → u` | vowel quality | Both share ḍamma. Identical to attested **Western (Serto) Syriac** vocalism. |

What is **preserved** (and was lost in every prior reader tier): all pharyngeals,
emphatics, and interdentals; the uvular/velars; and — crucially — **vowel length**,
carried structurally by the ا/و/ي matres so that it survives even into the bare
Unvocalized tier.

Net: from the Vocalized tier the source IPA round-trips exactly except at those five
points. The two consonant merges vanish under the loan-letter variant, leaving only
the e→i and o→u vowel-quality merges — and even those merely render the attested
Western Syriac vocalism rather than introducing an arbitrary approximation. This is
the most faithful, most nearly-reversible reader tier in the project — a different
category from CJK entirely.

### Reference standards

The realization rulings behind the mapping follow **MSA (الفصحى) as the primary
standard and Classical/Quranic as the secondary** (the high-fidelity "tightening"
pair, analogous to the GA/RP pairing elsewhere in the project):

- **MSA** — the unmarked, pan-regional, prescriptive standard that retains the full
  consonant inventory the source needs (interdentals, qāf, pharyngeals, emphatics).
- **Classical / Quranic** — the genre-appropriate sibling for *scripture* (the careful
  *tajwīd* recitation register), preserving every contrast MSA does plus finer detail;
  mirrors the Hebrew/Aramaic guides' Tiberian-liturgical default.
- **Levantine — documented-only, NOT a shipped standard.** Geographically apt (the
  Peshitta's Syrian homeland) but phonologically the *least* apt: urban Levantine
  collapses qāf → `[ʔ]` and the interdentals ث/ذ → stops, destroying exactly the
  mappings that justify an Arabic tier. Recorded as deliberate dissent, not buried.

Key rulings carried into the guide: keep literary `[q]` for ق (matches Syriac Qoph),
Classical interdental values for ث/ذ, Classical pharyngealized `[tˤ]/[sˤ]` for ط/ص,
and declare **ج = source `/ɡ/`, read `[ɡ]`** (with `[dʒ]` noted as an acceptable MSA
surface variant). Case vowels (iʿrāb) and tajwīd features are descriptive only and are
never emitted — the source IPA is caseless.

---

## Worked Example

The six embedded gold cases used by `--selftest`, shown in source IPA followed by all
four tiers. These are guaranteed to match the shipped converter exactly (all 24
checks — 6 refs × 4 tiers — PASS). The Vocalized/Unvocalized strings are shown in
logical order; the renderer applies RTL. (The RLI…PDI isolate wrapping is added by
`transliterate_line()` around each verse body and is omitted here for readability.)

### John 1:1

```
IPA          breːʃiːθ ʔiːθawj wɑː melθɑː whuː melθɑː ʔiːθawj wɑː lwɑːθ ʔɑːlɑːhɑː waʔlɑːhɑː ʔiːθawj wɑː huː melθɑː
Scholarly    brēšīṯ ʾīṯawy wā melṯā whū melṯā ʾīṯawy wā lwāṯ ʾālāhā waʾlāhā ʾīṯawy wā hū melṯā
Pretty       brēshīth īthawy wā melthā whū melthā īthawy wā lwāth ālāhā wa'lāhā īthawy wā hū melthā
Vocalized    بْرِيشِيثْ ءِيثَوْيْ وَا مِلْثَا وْهُو مِلْثَا ءِيثَوْيْ وَا لْوَاثْ ءَالَاهَا وَءْلَاهَا ءِيثَوْيْ وَا هُو مِلْثَا
Unvocalized  بريشيث ءيثوي وا ملثا وهو ملثا ءيثوي وا لواث ءالاها وءلاها ءيثوي وا هو ملثا
```

Note the **e→i collapse** visible in `melθɑː → مِلْثَا` (`mel` read as `[mil]`); the
**long vowels** carried by ي/ا (`breːʃiːθ → بْرِيشِيثْ`); **sukun** on the onset `b`
and coda `θ`.

### John 1:2

```
IPA          hɑːnɑː ʔiːθawj wɑː breːʃiːθ lwɑːθ ʔɑːlɑːhɑː
Scholarly    hānā ʾīṯawy wā brēšīṯ lwāṯ ʾālāhā
Pretty       hānā īthawy wā brēshīth lwāth ālāhā
Vocalized    هَانَا ءِيثَوْيْ وَا بْرِيشِيثْ لْوَاثْ ءَالَاهَا
Unvocalized  هانا ءيثوي وا بريشيث لواث ءالاها
```

### John 1:3

```
IPA          kul bʔijðeh hwɑː wvelʕɑːðawj ʔɑːflɑː ħðɑː hwɑːθ medem dahwɑː
Scholarly    kul bʾiyḏeh hwā wḇelʿāḏawy ʾāflā ḥḏā hwāṯ medem dahwā
Pretty       kul b'iydheh hwā wvelʿādhawy āflā ḥdhā hwāth medem dahwā
Vocalized    كُلْ بْءِيْذِهْ هْوَا وْفِلْعَاذَوْيْ ءَافْلَا حْذَا هْوَاثْ مِدِمْ دَهْوَا
Unvocalized  كل بءيذه هوا وفلعاذوي ءافلا حذا هواث مدم دهوا
```

Note the **v/f merge** (`wvel… → وْفِلْ…`, `v` rendered with ف) and the pharyngeal
`ʕ → ع` (`…ʕɑːðawj → …عَاذَوْيْ`) and `ħ → ح` (`ħðɑː → حْذَا`).

### Matthew 1:1

```
IPA          kθɑːvɑː diːliːðuːθeh djeʃuːʕ mʃiːħɑː breh dðawiːð breh dʔavrɑːhɑːm
Scholarly    kṯāḇā dīlīḏūṯeh dyešūʿ mšīḥā breh dḏawīḏ breh dʾaḇrāhām
Pretty       kthāvā dīlīdhūtheh dyeshūʿ mshīḥā breh ddhawīdh breh d'avrāhām
Vocalized    كْثَافَا دِيلِيذُوثِهْ دْيِشُوعْ مْشِيحَا بْرِهْ دْذَوِيذْ بْرِهْ دْءَفْرَاهَامْ
Unvocalized  كثافا ديليذوثه ديشوع مشيحا بره دذويذ بره دءفراهام
```

### Romans 1:1

```
IPA          pawlɑːws ʕavdɑː djeʃuːʕ mʃiːħɑː qarjɑː waʃliːħɑː dʔeθpreʃ leʔwanɡelijjɑːwn dʔɑːlɑːhɑː
Scholarly    pawlāws ʿaḇdā dyešūʿ mšīḥā qaryā wašlīḥā dʾeṯpreš leʾwangeliyyāwn dʾālāhā
Pretty       pawlāws ʿavdā dyeshūʿ mshīḥā qaryā washlīḥā d'ethpresh le'wangeliyyāwn d'ālāhā
Vocalized    بَوْلَاوْسْ عَفْدَا دْيِشُوعْ مْشِيحَا قَرْيَا وَشْلِيحَا دْءِثْبْرِشْ لِءْوَنْجِلِيَّاوْنْ دْءَالَاهَا
Unvocalized  بولاوس عفدا ديشوع مشيحا قريا وشليحا دءثبرش لءونجلياون دءالاها
```

Note the **p→b merge** (`pawl… → بَوْل…`), the `ɡ → ج` (`…ɡeli… → …جِلِ…`), and the
**geminate** in `leʔwanɡelijjɑːwn`: the `jj` fuses to one ي + **shadda** →
`لِءْوَنْجِلِيَّاوْنْ`.

### Matthew 27:16 (Barabbas)

```
IPA          dmeθqre bar-ʔaba lvar-ʔaba lvar-ʔava
Scholarly    dmeṯqre bar-ʾaba lḇar-ʾaba lḇar-ʾaḇa
Pretty       dmethqre bar-'aba lvar-'aba lvar-'ava
Vocalized    دْمِثْقْرِ بَرْ-ءَبَ لْفَرْ-ءَبَ لْفَرْ-ءَفَ
Unvocalized  دمثقر بر-ءب لفر-ءب لفر-ءف
```

Note the literal **hyphen** emitted verbatim (`bar-ʔaba → بَرْ-ءَبَ`), and the bare
**hamza ء** for every `ʔ`.

---

## Folder Layout

Everything lives under the repository path `Arabic/Peshita_Arabic/` (relative to the
repo root):

```
Arabic/Peshita_Arabic/
├── TRANSLITERATION_SCHEME.md         # this document
├── transliterate_ar.py               # the deterministic converter (authoritative)
├── transliteration_mapping_ar.json   # machine-readable mirror of the mapping tables
├── Scholarly/                        # tier 1 output (Latin; byte-identical to English)
│   ├── Matthew-Matityahu/
│   │   ├── matthewmatityahu1_scholarly.txt
│   │   ├── matthewmatityahu2_scholarly.txt
│   │   └── ...
│   ├── 1stCorinthians/
│   └── ...                           # 27 book folders
├── Pretty/                           # tier 2 output (Latin; *_pretty.txt)
│   └── ...
├── Vocalized/                        # tier 3 output (Arabic abjad + harakat; *_vocalized.txt)
│   └── ...
└── Unvocalized/                      # tier 4 output (Vocalized − harakat; *_unvocalized.txt)
    └── ...
```

Each tier directory mirrors the book/chapter structure of `IPA/Peshitta/`. For every
source file `IPA/Peshitta/<Book>/<name>_ipa.txt` the build produces one file per tier
at `Arabic/Peshita_Arabic/<Tier>/<Book>/<name>_<tier>.txt`. Each output line keeps its
`<verse#>\t` prefix verbatim; for the Arabic tiers the verse body is additionally
wrapped in RLI…PDI isolates.

The current corpus is **260 IPA source files** across **27 books**, yielding
**1040 transliterated files** (260 × 4 tiers — 260 per tier).

---

## Reproducing

The whole corpus can be regenerated from scratch with one command, run from this
folder:

```sh
python3 transliterate_ar.py --build
```

This walks every `*_ipa.txt` under `IPA/Peshitta/`, transliterates each into all four
tiers, and writes the `Scholarly/`, `Pretty/`, `Vocalized/`, and `Unvocalized/` trees
described above. It reports the number of files written and any unmapped characters
(there should be none).

Other useful entry points:

```sh
python3 transliterate_ar.py --selftest        # run the embedded gold cases (24 checks: 6 refs × 4 tiers)
python3 transliterate_ar.py --coverage        # scan the corpus for unmapped IPA + non-Arabic-block leaks
python3 transliterate_ar.py --write-mapping   # (re)write transliteration_mapping_ar.json from the tables
```

Verified current status: `--selftest` reports **ALL PASS** (24/24); `--coverage`
reports **0 unmapped IPA segments and 0 non-Arabic-block characters** in the Vocalized
tier across all 260 files.

`transliterate_ar.py` is authoritative: `transliteration_mapping_ar.json` is a
machine-readable mirror of its hard-coded tables, regenerated by `--write-mapping`.

---

*Prepared and signed by **Shin**.*
