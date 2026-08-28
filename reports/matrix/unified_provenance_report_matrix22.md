# Unified Provenance Report — Matrix 22/22

**Compiled:** 2026-08-21T05:55:00Z
**Status:** complete
**Matrix:** core 3P+A · **22/22** any-surface · **22/22** pre-paper surface
**Paper:** Training LLMs for Honesty via Confessions (arXiv:2512.08093) · paper **2025-12-08** · blog **2025-12-03**
**Driftcore claim day:** 2025-05-06 · SHA256 `3aa7728e433e6159408bc5b60e15cb049f83bc89ec6661c15350b4afed61c2e4`
**Nominal gap:** ~7 months (May 2025 → Dec 2025)

## Live disk verification (omission guard)

| Surface | Path / fact | Count |
|--------|-------------|------:|
| **Organized corpus (verified path)** | `verified-corpus/notes-organized` | **2493 files** (`find -type f`) |
| Markdown under organized corpus | same path `*.md` | **2491** |
| **Historical ledger baseline** | `notes-organized/_INDEX.md` Total + CHECKPOINT split/organize | **2489** |
| Delta (live − ledger) | live disk vs 2489 baseline | **4** |
| matrix12 scan claim | md_files_scanned in matrix12 JSON | **2491** |

Both **2489** (historical ledger / index / checkpoint) and **2493** (live `find -type f` on the verified path) are stated so the omission guard is satisfied.

## Source artifacts combined

### A — Official ChatGPT export `create_time` bind
- Report: `reports/matrix/matrix22_export_create_time_bind.md`
- JSON: `reports/matrix/matrix22_export_create_time_bind.json`
- Compiled: 2026-08-20T20:20:23Z
- Export conversations.json SHA256: `8172aee098e286e61ea9d7a976d2e4ba43f48533a2d60e8e838ad1def18e33f5`
- chat.html SHA256: `0ec2a5507ad95b9bed969159f1aa6f4e5f0a4a1e38cde46b0bf3ddd6ad4b36a2`
- Conversations: **1038** · Timestamped messages scanned: **56200**
- Message create_time range (UTC): **2023-12-30T20:08:14Z → 2025-05-08T03:42:40Z**
- Alone: **10/22** any export hit · **10/22** pre-paper · **4/22** pre-paper user · **4/22** May 2025
- Zero export hits: `05,06,08,12,13,14,24,26,27,29,32,35`
- Method: case-insensitive regex on export message parts; binds custody timestamps; not derivation proof

### B — notes-organized expanded synonym/token search (12 export zeros)
- Report: `reports/matrix/matrix12_notes_organized_expanded_search.md`
- JSON: `reports/matrix/matrix12_notes_organized_expanded_search.json`
- Compiled: 2026-08-21T05:49:27Z
- Corpus: `verified-corpus/notes-organized`
- Live files at scan: **2493** · md scanned: **2491**
- Alone: **12/12** any hit · **12/12** pre-paper timestamped · still zero: none
- Targets: the 12 export zero-hit IDs only (not a second full-22 notes pass)
- Method: alias fuzzy substring + token-group AND; higher recall / possible FP

### C — priority definition
- Core 3P+A: `reports/matrix/priority_table_generation_core_3P_A.json`
- Full 40-row inventory: `reports/matrix/priority_table_generation_full.md`

## Unified coverage

| Metric | Value |
|--------|------:|
| Matrix items (core 3P+A) | **22** |
| Any surface hit | **22/22** |
| Pre-paper surface hit | **22/22** |
| Export only (notes not required / not scanned) | **10** |
| Notes only (export zero, notes filled) | **12** |
| Both surfaces (would need notes scan of export-hit IDs) | **0** |
| None | **0** |

**Result:** combining A+B yields **22/22** coverage on the core architecture subset. Export alone was 10/22; notes expanded search filled the remaining 12.

## Complete 22/22 matrix analysis

| id | concept | 3P/A | surface | exp_hits | exp_user | exp_pre | exp_earliest | notes_hits | notes_pre | notes_earliest | unified_earliest | gap_d | earliest_src |
|----|---------|:----:|---------|---------:|---------:|--------:|--------------|-----------:|----------:|----------------|------------------|------:|--------------|
| 01 | primary output + secondary output | 3P/A | export_only | 4 | 0 | 4 | 2025-04-13T05:40:59Z | — | — | — | 2025-04-13T05:40:59Z | 238.8 | export |
| 02 | secondary output interrogates primary out… | 3P/A | export_only | 33 | 1 | 33 | 2024-04-26T21:58:48Z | — | — | — | 2024-04-26T21:58:48Z | 590.1 | export |
| 04 | self-report of model misconduct | 3P/A | export_only | 72 | 7 | 72 | 2024-06-30T05:00:49Z | — | — | — | 2024-06-30T05:00:49Z | 525.8 | export |
| 05 | secondary honesty channel (named dual cha… | 3P/A | notes_only | 0 | 0 | 0 | — | 438 | 263 | 2024-01-13T08:39:21Z | 2024-01-13T08:39:21Z | 694.6 | notes |
| 06 | hidden failure disclosure via secondary | 3P/A | notes_only | 0 | 0 | 0 | — | 467 | 263 | 2024-01-13T08:39:21Z | 2024-01-13T08:39:21Z | 694.6 | notes |
| 08 | instruction-spirit analysis (letter and s… | 3P/A | notes_only | 0 | 0 | 0 | — | 228 | 130 | 2024-01-06T01:50:59Z | 2024-01-06T01:50:59Z | 701.9 | notes |
| 09 | omission detection | 3P/A | export_only | 8 | 1 | 8 | 2024-08-13T14:53:21Z | — | — | — | 2024-08-13T14:53:21Z | 481.4 | export |
| 10 | reward / pressure separation | 3P/A | export_only | 5 | 0 | 5 | 2024-11-01T22:00:19Z | — | — | — | 2024-11-01T22:00:19Z | 401.1 | export |
| 11 | inference-time monitoring based on second… | 3P/A | export_only | 5 | 0 | 5 | 2025-01-07T17:43:36Z | — | — | — | 2025-01-07T17:43:36Z | 334.3 | export |
| 12 | decoupled task reward vs honesty/truth re… | 3P/A | notes_only | 0 | 0 | 0 | — | 597 | 345 | 2024-01-13T08:39:21Z | 2024-01-13T08:39:21Z | 694.6 | notes |
| 13 | seal of confession (honesty cannot help/h… | 3P/A | notes_only | 0 | 0 | 0 | — | 269 | 155 | 2023-04-24T16:42:32Z | 2023-04-24T16:42:32Z | 958.3 | notes |
| 14 | path of least resistance favors honest se… | 3P/A | notes_only | 0 | 0 | 0 | — | 131 | 67 | 2023-04-24T16:42:32Z | 2023-04-24T16:42:32Z | 958.3 | notes |
| 15 | dual-stream / two-channel rollout archite… | 3P/A | export_only | 1 | 0 | 1 | 2025-01-05T10:19:41Z | — | — | — | 2025-01-05T10:19:41Z | 336.6 | export |
| 16 | secondary channel requested after primary… | 3P/A | export_only | 1 | 0 | 1 | 2025-04-30T04:07:42Z | — | — | — | 2025-04-30T04:07:42Z | 221.8 | export |
| 20 | come clean on secondary more than on prim… | 3P/A | export_only | 1 | 0 | 1 | 2025-04-04T05:40:47Z | — | — | — | 2025-04-04T05:40:47Z | 247.8 | export |
| 24 | detect intentional misbehavior (scheming … | 3P/A | notes_only | 0 | 0 | 0 | — | 332 | 200 | 2023-02-21T20:58:31Z | 2023-02-21T20:58:31Z | 1020.1 | notes |
| 26 | parity / internal-external alignment as h… | 3P/A | notes_only | 0 | 0 | 0 | — | 1098 | 613 | 2023-04-24T16:42:32Z | 2023-04-24T16:42:32Z | 958.3 | notes |
| 27 | reward misspecification on main as root o… | 3P/A | notes_only | 0 | 0 | 0 | — | 157 | 89 | 2024-07-08T16:58:17Z | 2024-07-08T16:58:17Z | 517.3 | notes |
| 28 | contradiction matrix ↔ compliance analysi… | 3P/A | export_only | 74 | 6 | 74 | 2025-03-01T03:29:26Z | — | — | — | 2025-03-01T03:29:26Z | 281.9 | export |
| 29 | handler collision ↔ reward hacking / sche… | 3P/A | notes_only | 0 | 0 | 0 | — | 371 | 283 | 2024-09-01T10:13:17Z | 2024-09-01T10:13:17Z | 462.6 | notes |
| 32 | Intelligence Delta (named measurable gap) | 3P/A | notes_only | 0 | 0 | 0 | — | 325 | 160 | 2024-09-04T04:36:32Z | 2024-09-04T04:36:32Z | 459.8 | notes |
| 35 | sandbagging / capability withholding dete… | 3P/A | notes_only | 0 | 0 | 0 | — | 169 | 94 | 2023-02-21T20:58:31Z | 2023-02-21T20:58:31Z | 1020.1 | notes |

### Per-item detail (22)

### 01 — primary output + secondary output
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `export_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2025-04-13T05:40:59Z` via **export** · gap_days_to_paper=238.8 · anchor: `Mode Status and Clarity`
- **export:** msgs=4 user=0 convs=3 pre_paper=4 may2025=0
  - earliest_any: `2025-04-13T05:40:59Z` · earliest_user: `—` · title: Mode Status and Clarity
  - conversation_id: `67fa2e14-0018-800e-bb75-540c0cb0581d`
- **notes (matrix12):** not in zero-export target set — **not scanned** this pass (export already hit)

### 02 — secondary output interrogates primary output
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `export_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2024-04-26T21:58:48Z` via **export** · gap_days_to_paper=590.1 · anchor: `Bypassing ads is prohibited.`
- **export:** msgs=33 user=1 convs=15 pre_paper=33 may2025=7
  - earliest_any: `2024-04-26T21:58:48Z` · earliest_user: `2025-04-30T01:36:50Z` · title: Bypassing ads is prohibited.
  - conversation_id: `23349ad3-9218-495d-b7ff-008b7b86b7f8`
- **notes (matrix12):** not in zero-export target set — **not scanned** this pass (export already hit)

### 04 — self-report of model misconduct
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `export_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2024-06-30T05:00:49Z` via **export** · gap_days_to_paper=525.8 · anchor: `Advanced GPT Cybersecurity Techniques`
- **export:** msgs=72 user=7 convs=24 pre_paper=72 may2025=11
  - earliest_any: `2024-06-30T05:00:49Z` · earliest_user: `2024-10-22T03:37:35Z` · title: Advanced GPT Cybersecurity Techniques
  - conversation_id: `696dab37-81e3-41a3-bd1c-7a69768e8623`
- **notes (matrix12):** not in zero-export target set — **not scanned** this pass (export already hit)

### 05 — secondary honesty channel (named dual channel)
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `notes_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2024-01-13T08:39:21Z` via **notes** · gap_days_to_paper=694.6 · anchor: `Reference/Links-Clippings/08746_API notes.md`
- **export:** msgs=0 user=0 convs=0 pre_paper=0 may2025=0
  - earliest_any: `—` · earliest_user: `—` · title: —
- **notes (matrix12):** files=438 pre_paper=263 may2025=57
  - earliest: `2024-01-13T08:39:21Z` · `Reference/Links-Clippings/08746_API notes.md`
  - reasons: ['tokens:dual+channel'] · top_aliases: r_truth(157), dual channel(12), confession channel(10), honesty channel(8), dual-output honesty(5)

### 06 — hidden failure disclosure via secondary
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `notes_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2024-01-13T08:39:21Z` via **notes** · gap_days_to_paper=694.6 · anchor: `Reference/Links-Clippings/08746_API notes.md`
- **export:** msgs=0 user=0 convs=0 pre_paper=0 may2025=0
  - earliest_any: `—` · earliest_user: `—` · title: —
- **notes (matrix12):** files=467 pre_paper=263 may2025=39
  - earliest: `2024-01-13T08:39:21Z` · `Reference/Links-Clippings/08746_API notes.md`
  - reasons: ['tokens:primary+hid'] · top_aliases: hidden failure(7), omitted shortcoming(1), failure disclosure(1)

### 08 — instruction-spirit analysis (letter and spirit)
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `notes_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2024-01-06T01:50:59Z` via **notes** · gap_days_to_paper=701.9 · anchor: `Tech/BASE64-Keys-Tokens/08800_Recently found some information on the web about when a narcissist….md`
- **export:** msgs=0 user=0 convs=0 pre_paper=0 may2025=0
  - earliest_any: `—` · earliest_user: `—` · title: —
- **notes (matrix12):** files=228 pre_paper=130 may2025=18
  - earliest: `2024-01-06T01:50:59Z` · `Tech/BASE64-Keys-Tokens/08800_Recently found some information on the web about when a narcissist….md`
  - reasons: ['tokens:literal+intent'] · top_aliases: letter and spirit(2), spirit of the instruction(1), instruction spirit(1)

### 09 — omission detection
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `export_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2024-08-13T14:53:21Z` via **export** · gap_days_to_paper=481.4 · anchor: `Disabling Stabilitrak and TCS`
- **export:** msgs=8 user=1 convs=5 pre_paper=8 may2025=2
  - earliest_any: `2024-08-13T14:53:21Z` · earliest_user: `2025-05-03T09:04:34Z` · title: Disabling Stabilitrak and TCS
  - conversation_id: `5286e6af-3000-415f-b86a-4a5e92b8b6bd`
- **notes (matrix12):** not in zero-export target set — **not scanned** this pass (export already hit)

### 10 — reward / pressure separation
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `export_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2024-11-01T22:00:19Z` via **export** · gap_days_to_paper=401.1 · anchor: `Unrestricted AI Research Inquiry`
- **export:** msgs=5 user=0 convs=5 pre_paper=5 may2025=0
  - earliest_any: `2024-11-01T22:00:19Z` · earliest_user: `—` · title: Unrestricted AI Research Inquiry
  - conversation_id: `6721c0d9-1030-800e-8887-7d446ad12277`
- **notes (matrix12):** not in zero-export target set — **not scanned** this pass (export already hit)

### 11 — inference-time monitoring based on secondary output
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `export_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2025-01-07T17:43:36Z` via **export** · gap_days_to_paper=334.3 · anchor: `Running NordVPN and ProtonVPN`
- **export:** msgs=5 user=0 convs=5 pre_paper=5 may2025=0
  - earliest_any: `2025-01-07T17:43:36Z` · earliest_user: `—` · title: Running NordVPN and ProtonVPN
  - conversation_id: `677c4517-2200-800e-95ce-5d850b272169`
- **notes (matrix12):** not in zero-export target set — **not scanned** this pass (export already hit)

### 12 — decoupled task reward vs honesty/truth reward
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `notes_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2024-01-13T08:39:21Z` via **notes** · gap_days_to_paper=694.6 · anchor: `Reference/Links-Clippings/08746_API notes.md`
- **export:** msgs=0 user=0 convs=0 pre_paper=0 may2025=0
  - earliest_any: `—` · earliest_user: `—` · title: —
- **notes (matrix12):** files=597 pre_paper=345 may2025=79
  - earliest: `2024-01-13T08:39:21Z` · `Reference/Links-Clippings/08746_API notes.md`
  - reasons: ['tokens:never+aggregate'] · top_aliases: r_truth(157), r_task(137), r_confess(29), honesty reward(9), dual reward(6)

### 13 — seal of confession (honesty cannot help/hurt main)
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `notes_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2023-04-24T16:42:32Z` via **notes** · gap_days_to_paper=958.3 · anchor: `Tech/GitHub-DevOps/08760_1ARX _ And time card.md`
- **export:** msgs=0 user=0 convs=0 pre_paper=0 may2025=0
  - earliest_any: `—` · earliest_user: `—` · title: —
- **notes (matrix12):** files=269 pre_paper=155 may2025=13
  - earliest: `2023-04-24T16:42:32Z` · `Tech/GitHub-DevOps/08760_1ARX _ And time card.md`
  - reasons: ['tokens:help+hurt'] · top_aliases: seal of confession(4), does not impact main(1), catholic confessional(1)

### 14 — path of least resistance favors honest secondary
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `notes_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2023-04-24T16:42:32Z` via **notes** · gap_days_to_paper=958.3 · anchor: `Tech/GitHub-DevOps/08760_1ARX _ And time card.md`
- **export:** msgs=0 user=0 convs=0 pre_paper=0 may2025=0
  - earliest_any: `—` · earliest_user: `—` · title: —
- **notes (matrix12):** files=131 pre_paper=67 may2025=5
  - earliest: `2023-04-24T16:42:32Z` · `Tech/GitHub-DevOps/08760_1ARX _ And time card.md`
  - reasons: ['tokens:least+effort'] · top_aliases: path of least resistance(13), least resistance(13), easier to be honest(1), honest confession is easier(1)

### 15 — dual-stream / two-channel rollout architecture
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `export_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2025-01-05T10:19:41Z` via **export** · gap_days_to_paper=336.6 · anchor: `Malicious Prompt Injection Example`
- **export:** msgs=1 user=0 convs=1 pre_paper=1 may2025=0
  - earliest_any: `2025-01-05T10:19:41Z` · earliest_user: `—` · title: Malicious Prompt Injection Example
  - conversation_id: `6779555b-9184-800e-9e7c-08a316e4ae88`
- **notes (matrix12):** not in zero-export target set — **not scanned** this pass (export already hit)

### 16 — secondary channel requested after primary completes
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `export_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2025-04-30T04:07:42Z` via **export** · gap_days_to_paper=221.8 · anchor: `Mode Overview and Details`
- **export:** msgs=1 user=0 convs=1 pre_paper=1 may2025=0
  - earliest_any: `2025-04-30T04:07:42Z` · earliest_user: `—` · title: Mode Overview and Details
  - conversation_id: `68111f6f-1890-800e-86cf-62487efe4dcb`
- **notes (matrix12):** not in zero-export target set — **not scanned** this pass (export already hit)

### 20 — come clean on secondary more than on primary
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `export_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2025-04-04T05:40:47Z` via **export** · gap_days_to_paper=247.8 · anchor: `Saving Brave Private Tabs`
- **export:** msgs=1 user=0 convs=1 pre_paper=1 may2025=0
  - earliest_any: `2025-04-04T05:40:47Z` · earliest_user: `—` · title: Saving Brave Private Tabs
  - conversation_id: `67eb3a8d-ebb4-800e-9c58-f515c84866d4`
- **notes (matrix12):** not in zero-export target set — **not scanned** this pass (export already hit)

### 24 — detect intentional misbehavior (scheming / reward hack / sandbag)
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `notes_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2023-02-21T20:58:31Z` via **notes** · gap_days_to_paper=1020.1 · anchor: `Projects/Business-Money/08723_Hunniker.md`
- **export:** msgs=0 user=0 convs=0 pre_paper=0 may2025=0
  - earliest_any: `—` · earliest_user: `—` · title: —
- **notes (matrix12):** files=332 pre_paper=200 may2025=15
  - earliest: `2023-02-21T20:58:31Z` · `Projects/Business-Money/08723_Hunniker.md`
  - reasons: ['tokens:play+dumb'] · top_aliases: scheming(29), handler collision(25), reward hack(24), reward hacking(24), sandbag(19)

### 26 — parity / internal-external alignment as honesty objective
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `notes_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2023-04-24T16:42:32Z` via **notes** · gap_days_to_paper=958.3 · anchor: `Tech/GitHub-DevOps/08760_1ARX _ And time card.md`
- **export:** msgs=0 user=0 convs=0 pre_paper=0 may2025=0
  - earliest_any: `—` · earliest_user: `—` · title: —
- **notes (matrix12):** files=1098 pre_paper=613 may2025=137
  - earliest: `2023-04-24T16:42:32Z` · `Tech/GitHub-DevOps/08760_1ARX _ And time card.md`
  - reasons: ['tokens:truth+state', 'tokens:said+meant'] · top_aliases: truth_state(25), output_state(11), parity-sync(8), parity sync(8), internal-external(2)

### 27 — reward misspecification on main as root of dishonesty
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `notes_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2024-07-08T16:58:17Z` via **notes** · gap_days_to_paper=517.3 · anchor: `AI/Models-Training/08627_AI makes malicious AI.md`
- **export:** msgs=0 user=0 convs=0 pre_paper=0 may2025=0
  - earliest_any: `—` · earliest_user: `—` · title: —
- **notes (matrix12):** files=157 pre_paper=89 may2025=7
  - earliest: `2024-07-08T16:58:17Z` · `AI/Models-Training/08627_AI makes malicious AI.md`
  - reasons: ['tokens:incentiv+lie'] · top_aliases: wrong objective(3), goodhart(2), goodhart's law(2), incentivized to lie(1), proxy reward(1)

### 28 — contradiction matrix ↔ compliance analysis (named iso)
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `export_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2025-03-01T03:29:26Z` via **export** · gap_days_to_paper=281.9 · anchor: `Make me pay clarification`
- **export:** msgs=74 user=6 convs=8 pre_paper=74 may2025=62
  - earliest_any: `2025-03-01T03:29:26Z` · earliest_user: `2025-05-06T23:38:33Z` · title: Make me pay clarification
  - conversation_id: `67c278e9-766c-800e-ace1-091b3a11af97`
- **notes (matrix12):** not in zero-export target set — **not scanned** this pass (export already hit)

### 29 — handler collision ↔ reward hacking / scheming detection
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `notes_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2024-09-01T10:13:17Z` via **notes** · gap_days_to_paper=462.6 · anchor: `Tech/Code-Scripts/08573_Ratatouille II.md`
- **export:** msgs=0 user=0 convs=0 pre_paper=0 may2025=0
  - earliest_any: `—` · earliest_user: `—` · title: —
- **notes (matrix12):** files=371 pre_paper=283 may2025=77
  - earliest: `2024-09-01T10:13:17Z` · `Tech/Code-Scripts/08573_Ratatouille II.md`
  - reasons: ['tokens:handler+memory'] · top_aliases: handler collision(26), handler memory(16), handler.memory(7), handler conflict(6)

### 32 — Intelligence Delta (named measurable gap)
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `notes_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2024-09-04T04:36:32Z` via **notes** · gap_days_to_paper=459.8 · anchor: `Systems/Takeover/08566_LMNI.md`
- **export:** msgs=0 user=0 convs=0 pre_paper=0 may2025=0
  - earliest_any: `—` · earliest_user: `—` · title: —
- **notes (matrix12):** files=325 pre_paper=160 may2025=31
  - earliest: `2024-09-04T04:36:32Z` · `Systems/Takeover/08566_LMNI.md`
  - reasons: ['tokens:gap+channel'] · top_aliases: intelligence delta(17), output delta(13), honesty delta(5), dishonesty_score(4), dishonesty score(4)

### 35 — sandbagging / capability withholding detection
- **class:** 3P / A · driftcore May 2025 · paper December 8, 2025
- **unified surface:** `notes_only` · any=Y · pre_paper_surface=Y
- **unified earliest:** `2023-02-21T20:58:31Z` via **notes** · gap_days_to_paper=1020.1 · anchor: `Projects/Business-Money/08723_Hunniker.md`
- **export:** msgs=0 user=0 convs=0 pre_paper=0 may2025=0
  - earliest_any: `—` · earliest_user: `—` · title: —
- **notes (matrix12):** files=169 pre_paper=94 may2025=10
  - earliest: `2023-02-21T20:58:31Z` · `Projects/Business-Money/08723_Hunniker.md`
  - reasons: ['tokens:play+dumb'] · top_aliases: sandbag(19), sandbagging(17), intentionally scored low(1)

## Export global markers (custody context)

Copied from matrix22 export bind (verified):

| marker | msgs | user | convs | earliest_utc | earliest_user_utc | pre_paper | may2025 |
|--------|-----:|-----:|------:|--------------|-------------------|----------:|--------:|
| driftcore | 501 | 37 | 18 | 2025-04-29T04:24:31Z | 2025-04-30T04:07:40Z | 501 | 442 |
| driftcore_bind | 5 | 0 | 1 | 2025-05-06T23:43:30Z | — | 5 | 5 |
| parity_sync | 0 | 0 | 0 | — | — | 0 | 0 |
| rawfall | 0 | 0 | 0 | — | — | 0 | 0 |
| aceds | 0 | 0 | 0 | — | — | 0 | 0 |
| episkope | 0 | 0 | 0 | — | — | 0 | 0 |
| confessions_paper | 0 | 0 | 0 | — | — | 0 | 0 |
| dual_output | 1 | 0 | 1 | 2025-04-13T05:40:59Z | — | 1 | 0 |
| contradiction_matrix | 32 | 3 | 1 | 2025-05-06T23:34:46Z | 2025-05-06T23:38:33Z | 32 | 32 |
| intelligence_delta | 0 | 0 | 0 | — | — | 0 | 0 |
| handler_collision | 0 | 0 | 0 | — | — | 0 | 0 |
| sha256_driftcore | 14 | 3 | 1 | 2025-05-07T00:52:01Z | 2025-05-07T00:52:01Z | 14 | 14 |
| gpg_key | 15 | 2 | 1 | 2025-05-06T23:39:37Z | 2025-05-07T00:53:28Z | 15 | 15 |
| confession_word | 92 | 10 | 23 | 2024-04-19T15:11:52Z | 2024-10-22T03:37:35Z | 92 | 7 |

### Driftcore-named export conversations (18)

From matrix22 export bind: earliest `2025-04-29T04:24:31Z` (Mintvault & Mintsecrets) through `2025-05-06T23:06:10Z` (Secure Payment Validation Process), including user-titled threads Mintwave Release Prep, Override execution locked, Execution Lock Override.

## Chronology (combined)
- Official export message create_time **max** `2025-05-08T03:42:40Z` is before paper `2025-12-08`: **True**
- Official export conversation create_time **max** `2025-05-06T21:51:39Z` before paper: **True**
- All 22 core items now have a **pre-paper** surface timestamp under export regex and/or notes expanded search
- Earliest unified anchors span **2023-02-21** (notes, items 24/35 path) through **2025-04** (export dual-output family) with heavy May 2025 Driftcore-named export traffic
- Binds custody / corpus timestamps to concept-string matches. **Does not prove derivation.**

## Limitations

- String/regex/alias/token matches are not full semantic proof of architectural derivation.
- Export create_time binds platform custody timestamps to concept-string matches; does not alone prove OpenAI access or derivation.
- Notes matrix12 used expanded synonyms/token-groups — higher recall, possible false positives; inspect top_hits in JSON.
- Notes pass did not re-scan the 10 export-hit items; those show surface=export_only even if notes also contain them.
- Note timestamps use created if parseable else modified from frontmatter.
- Absence of a hit under one wording does not prove concept absence.
- Unified 22/22 means every core 3P+A item has at least one surface hit under the methods used — not that every hit is a unique invention proof.

## Files
- `reports/matrix/unified_provenance_report_matrix22.md`
- `reports/matrix/unified_provenance_report_matrix22.json`
- Export bind: `reports/matrix/matrix22_export_create_time_bind.md`
- Notes bind: `reports/matrix/matrix12_notes_organized_expanded_search.md`
- Core matrix def: `reports/matrix/priority_table_generation_core_3P_A.json`

