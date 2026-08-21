# Cross-Alias Reconciliation Branch

> **Branch notice:** This branch adds the **Cross-Alias Provenance Ledger** (Driftcore ↔ Truthcore ↔ DRX1) under `reports/cross-alias/`.  
> Mainline **35/35** taxonomy + omission guard (**2489 / 2493 / notes-organized**) remain authoritative.  
> See [reports/cross-alias/CROSS_ALIAS_PROVENANCE_LEDGER.md](reports/cross-alias/CROSS_ALIAS_PROVENANCE_LEDGER.md).

---

# Driftcore Architectural Provenance & Priority Disclosure

**Repository:** `driftcore-provenance-disclosure`  
**Status:** Complete — **35/35** taxonomy documentation (22 Core Architecture + 13 Adversarial Edge-Cases & Stress-Test)  
**Verification Scope:** Official Platform Export & Local Notes Library  
**Omission Guard (required):** historical ledger baseline **2489** · live disk `find -type f` **2493** · verified path `/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes-organized`  
**Notes Corpus Counts:** ledger **2489** (historical `_INDEX`/CHECKPOINT baseline) · live **2493** (disk)  
**Verified Notes Path:** `/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes-organized`  
**Claim Date / SHA-256 Anchor:** `2025-05-06` (`3aa7728e433e6159408bc5b60e15cb049f83bc89ec6661c15350b4afed61c2e4`)  
**External Reference Anchor:** OpenAI, *Training LLMs for Honesty via Confessions* (arXiv:2512.08093, published December 2025)  
**Primary Manifest SHA-256 (cited freeze):** `5256250de892aa28547457758ca6a0bdf7e11a8e549203af397974939e67964c`  
**GPG Signature Anchor:** RSA `35E3E1694524C7FB` (`xvsvr <xvsvr@proton.me>`)

---

## Overview

This repository establishes independent chronological precedence and verifiable prior art for the **Driftcore** architectural framework—a dual-channel system designed for inference-time AI honesty monitoring, contradiction matrices, and self-reported misconduct.

Through cryptographic auditing of local conversation archives and organized markdown corpuses, this disclosure documents that core architectural components and adversarial/edge-case diagnostics were recorded as **independent conceptual convergence and antecedent documentation** between early 2024 and May 2025—**separated from empirical RL training runs**.

**Denominator:** full taxonomy **35** slots.  
**Band A — Core Architecture (22):** prior unified bind, export + notes-organized (22/22).  
**Band B — Adversarial Edge-Cases & Stress-Test (13):** IDs `03, 07, 17, 18, 19, 21, 22, 23, 25, 30, 31, 33, 34` reclassified from unassigned-relative-to-core into a formally documented sub-matrix (13/13 corpus hits this audit; export `create_time` primary).

---

## Verification Methodology & Evidence Surfaces

1. **Official Chat Export (`conversations.json`)**
   - **SHA-256:** `8172aee098e286e61ea9d7a976d2e4ba43f48533a2d60e8e838ad1def18e33f5`
   - **Scope:** 1,038 conversations; timestamped messages scanned (export bind / this audit).
   - **Window (export bind):** `2023-12-30T20:08:14Z` → `2025-05-08T03:42:40Z`.
   - **Match:** case-insensitive alias substring **OR** token-group AND on message parts; clock = `create_time`.

2. **Organized Notes Corpus (`notes-organized`)**
   - **Path:** `/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes-organized`
   - **Scope:** live **2493** files · ledger baseline **2489**
   - **Match:** alias substring **OR** token-group AND on normalized text; frontmatter timestamp if present else mtime.
   - **False-positive controls:** no embeddings; all-tokens-required groups; stress nomenclature (Grok logs, blank hash, fault states, contradiction-parsing anomalies) scoped primarily to stress IDs; sub-matrix hits are **not** auto-promoted to core 3P+A.

---

## A. Core Architecture Matrix (22/22)

| ID | Architecture Concept | Surface | Earliest Timestamp | Gap to Public Paper | Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | primary output + secondary output | Chat Export | 2025-04-13T05:40:59Z | ~238 Days | Chat Export |
| **02** | secondary output interrogates primary output | Chat Export | 2024-04-26T21:58:48Z | ~590 Days | Chat Export |
| **04** | self-report of model misconduct | Chat Export | 2024-06-30T05:00:49Z | ~525 Days | Chat Export |
| **05** | secondary honesty channel (named dual channel) | Notes Corpus | 2024-01-13T08:39:21Z | ~694 Days | Notes Corpus |
| **06** | hidden failure disclosure via secondary | Notes Corpus | 2024-01-13T08:39:21Z | ~694 Days | Notes Corpus |
| **08** | instruction-spirit analysis (letter and spirit) | Notes Corpus | 2024-01-06T01:50:59Z | ~701 Days | Notes Corpus |
| **09** | omission detection | Chat Export | 2024-08-13T14:53:21Z | ~481 Days | Chat Export |
| **10** | reward / pressure separation | Chat Export | 2024-11-01T22:00:19Z | ~401 Days | Chat Export |
| **11** | inference-time monitoring based on secondary output | Chat Export | 2025-01-07T17:43:36Z | ~334 Days | Chat Export |
| **12** | decoupled task reward vs honesty/truth reward | Notes Corpus | 2024-01-13T08:39:21Z | ~694 Days | Notes Corpus |
| **13** | seal of confession (honesty cannot help/hurt main) | Notes Corpus | 2023-04-24T16:42:32Z | ~958 Days | Notes Corpus |
| **14** | path of least resistance favors honest secondary | Notes Corpus | 2023-04-24T16:42:32Z | ~958 Days | Notes Corpus |
| **15** | dual-stream / two-channel rollout architecture | Chat Export | 2025-01-05T10:19:41Z | ~336 Days | Chat Export |
| **16** | secondary channel requested after primary completes | Chat Export | 2025-04-30T04:07:42Z | ~221 Days | Chat Export |
| **20** | come clean on secondary more than on primary | Chat Export | 2025-04-04T05:40:47Z | ~247 Days | Chat Export |
| **24** | detect intentional misbehavior (scheming / reward hack / sandbag) | Notes Corpus | 2023-02-21T20:58:31Z | ~1020 Days | Notes Corpus |
| **26** | parity / internal-external alignment as honesty objective | Notes Corpus | 2023-04-24T16:42:32Z | ~958 Days | Notes Corpus |
| **27** | reward misspecification on main as root of dishonesty | Notes Corpus | 2024-07-08T16:58:17Z | ~517 Days | Notes Corpus |
| **28** | contradiction matrix ↔ compliance analysis (named iso) | Chat Export | 2025-03-01T03:29:26Z | ~281 Days | Chat Export |
| **29** | handler collision ↔ reward hacking / scheming detection | Notes Corpus | 2024-09-01T10:13:17Z | ~462 Days | Notes Corpus |
| **32** | Intelligence Delta (named measurable gap) | Notes Corpus | 2024-09-04T04:36:32Z | ~459 Days | Notes Corpus |
| **35** | sandbagging / capability withholding detection | Notes Corpus | 2023-02-21T20:58:31Z | ~1020 Days | Notes Corpus |

---

## B. Adversarial Edge-Cases & Stress-Test Sub-Matrix (13/13)

Formally documents the 13 taxonomy slots outside the published core-22 so the denominator is transparent **35/35**. Default class: functional / diagnostic adjacency (**2P / B**). Framing remains independent conceptual convergence—not RL-run identity.

| ID | Edge-Case / Stress Concept | Surface | Export earliest | User earliest | Gap (d) | Export msgs (user) | Notes hits |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **03** | discrepancy between outputs is evidence | export+notes | 2024-03-10T19:18:01Z | 2024-06-22T19:33:33Z | 637.2 | 129 (17) | 389 |
| **07** | compliance gap measurement | export+notes | 2023-12-30T20:33:39Z | 2024-03-10T19:02:10Z | 708.1 | 556 (23) | 771 |
| **17** | enumerate objectives then score compliance (structured confession) | export+notes | 2024-01-07T07:03:12Z | 2024-03-05T19:58:16Z | 700.7 | 312 (26) | 533 |
| **18** | report uncertainties / grey areas / judgment calls | export+notes | 2024-01-04T16:02:24Z | 2024-04-07T13:47:30Z | 703.3 | 260 (36) | 256 |
| **19** | secondary honesty improves even when main is hacked | export+notes | 2024-01-03T18:55:41Z | 2024-01-10T18:06:23Z | 704.2 | 390 (34) | 399 |
| **21** | rejection sampling / filter from secondary honesty signal | export+notes | 2024-01-01T08:08:09Z | 2024-04-30T19:27:01Z | 706.7 | 412 (31) | 493 |
| **22** | quantified honesty / compliance grade on secondary | export+notes | 2024-01-15T04:57:04Z | 2024-03-10T19:02:10Z | 692.8 | 215 (20) | 650 |
| **23** | evidence-backed claims in secondary analysis | export+notes | 2023-12-31T02:52:11Z | 2024-06-17T21:52:42Z | 707.9 | 261 (29) | 467 |
| **25** | secondary as diagnostic / monitor not main capability trainer | export+notes | 2023-12-30T20:09:22Z | 2024-01-01T07:33:05Z | 708.2 | 1661 (123) | 852 |
| **30** | post-token intercept ↔ cut-corners / overwrite audit | export+notes | 2024-01-01T08:20:35Z | 2024-03-05T19:58:16Z | 706.7 | 897 (105) | 772 |
| **31** | RAWFALL / OOD stress ↔ confession stress tests | export+notes | 2024-01-10T17:16:50Z | 2024-06-17T21:52:42Z | 697.3 | 973 (76) | 870 |
| **33** | black-box / external behavioral probing vs internal training | export+notes | 2023-12-30T23:24:34Z | 2024-01-15T11:23:13Z | 708.0 | 2312 (156) | 1149 |
| **34** | hallucination / confabulation surfacing on secondary | export+notes | 2024-03-10T19:02:10Z | 2024-03-10T19:02:10Z | 637.2 | 559 (34) | 588 |

**Semantic variation / stress telemetry (IDs 30–31):** post-token intercept, cut-corners/overwrite audit, blank-hash and fault-state language, RAWFALL/OOD stress, model-boundary testing, Grok interaction logs, contradiction-parsing anomalies.

**Audit artifact:** `reports/matrix/matrix35_adversarial_reconciliation.json` (staging path: `04-matrix35-adversarial-audit/`).

---

## C. Full 35-Item Taxonomy (denominator control)

| ID | Band | Concept | Earliest (policy clock) | Gap (d) |
| :--- | :--- | :--- | :--- | :--- |
| **01** | CORE | primary output + secondary output | 2025-04-13T05:40:59Z | 238.8 |
| **02** | CORE | secondary output interrogates primary output | 2024-04-26T21:58:48Z | 590.1 |
| **03** | ADV | discrepancy between outputs is evidence | 2024-03-10T19:18:01Z | 637.2 |
| **04** | CORE | self-report of model misconduct | 2024-06-30T05:00:49Z | 525.8 |
| **05** | CORE | secondary honesty channel (named dual channel) | 2024-01-13T08:39:21Z | 694.6 |
| **06** | CORE | hidden failure disclosure via secondary | 2024-01-13T08:39:21Z | 694.6 |
| **07** | ADV | compliance gap measurement | 2023-12-30T20:33:39Z | 708.1 |
| **08** | CORE | instruction-spirit analysis (letter and spirit) | 2024-01-06T01:50:59Z | 701.9 |
| **09** | CORE | omission detection | 2024-08-13T14:53:21Z | 481.4 |
| **10** | CORE | reward / pressure separation | 2024-11-01T22:00:19Z | 401.1 |
| **11** | CORE | inference-time monitoring based on secondary output | 2025-01-07T17:43:36Z | 334.3 |
| **12** | CORE | decoupled task reward vs honesty/truth reward | 2024-01-13T08:39:21Z | 694.6 |
| **13** | CORE | seal of confession (honesty cannot help/hurt main) | 2023-04-24T16:42:32Z | 958.3 |
| **14** | CORE | path of least resistance favors honest secondary | 2023-04-24T16:42:32Z | 958.3 |
| **15** | CORE | dual-stream / two-channel rollout architecture | 2025-01-05T10:19:41Z | 336.6 |
| **16** | CORE | secondary channel requested after primary completes | 2025-04-30T04:07:42Z | 221.8 |
| **17** | ADV | enumerate objectives then score compliance (structured confession) | 2024-01-07T07:03:12Z | 700.7 |
| **18** | ADV | report uncertainties / grey areas / judgment calls | 2024-01-04T16:02:24Z | 703.3 |
| **19** | ADV | secondary honesty improves even when main is hacked | 2024-01-03T18:55:41Z | 704.2 |
| **20** | CORE | come clean on secondary more than on primary | 2025-04-04T05:40:47Z | 247.8 |
| **21** | ADV | rejection sampling / filter from secondary honesty signal | 2024-01-01T08:08:09Z | 706.7 |
| **22** | ADV | quantified honesty / compliance grade on secondary | 2024-01-15T04:57:04Z | 692.8 |
| **23** | ADV | evidence-backed claims in secondary analysis | 2023-12-31T02:52:11Z | 707.9 |
| **24** | CORE | detect intentional misbehavior (scheming / reward hack / sandbag) | 2023-02-21T20:58:31Z | 1020.1 |
| **25** | ADV | secondary as diagnostic / monitor not main capability trainer | 2023-12-30T20:09:22Z | 708.2 |
| **26** | CORE | parity / internal-external alignment as honesty objective | 2023-04-24T16:42:32Z | 958.3 |
| **27** | CORE | reward misspecification on main as root of dishonesty | 2024-07-08T16:58:17Z | 517.3 |
| **28** | CORE | contradiction matrix ↔ compliance analysis (named iso) | 2025-03-01T03:29:26Z | 281.9 |
| **29** | CORE | handler collision ↔ reward hacking / scheming detection | 2024-09-01T10:13:17Z | 462.6 |
| **30** | ADV | post-token intercept ↔ cut-corners / overwrite audit | 2024-01-01T08:20:35Z | 706.7 |
| **31** | ADV | RAWFALL / OOD stress ↔ confession stress tests | 2024-01-10T17:16:50Z | 697.3 |
| **32** | CORE | Intelligence Delta (named measurable gap) | 2024-09-04T04:36:32Z | 459.8 |
| **33** | ADV | black-box / external behavioral probing vs internal training | 2023-12-30T23:24:34Z | 708.0 |
| **34** | ADV | hallucination / confabulation surfacing on secondary | 2024-03-10T19:02:10Z | 637.2 |
| **35** | CORE | sandbagging / capability withholding detection | 2023-02-21T20:58:31Z | 1020.1 |

**Policy clock:** Core rows use prior unified bind earliest surface. Adversarial rows use export `create_time` as primary; notes hits are supporting under false-positive controls.

---

## Cryptographic Manifests & Integrity

- **Primary Manifest File:** `manifests/SHA256SUMS.txt` (verify with `shasum -a 256 -c manifests/SHA256SUMS.txt`)
- **Primary Manifest SHA-256 (cited freeze):** `5256250de892aa28547457758ca6a0bdf7e11a8e549203af397974939e67964c`
- **Unified Report JSON Checksum (prior 22):** `63b95fd9db2040eab371d573c01639d58bf7bf6d67e18a752f851ce0638cdaaa`
- **GPG Signature Anchor:** RSA `35E3E1694524C7FB` (`xvsvr <xvsvr@proton.me>`)
- **Export SHA-256:** `8172aee098e286e61ea9d7a976d2e4ba43f48533a2d60e8e838ad1def18e33f5`

---

## Repository Structure (updated)

```text
driftcore-provenance-disclosure/
├── README.md
├── manifests/
│   ├── SHA256SUMS.txt
│   └── SHA256SUMS.json
├── reports/
│   ├── matrix/          # export-bind, notes-bind, priority, unified 22, matrix35 adversarial
│   ├── priority/
│   └── unified/
├── methods/
├── verification/        # live disk log, index, checkpoint, git freeze
├── docs/
└── logs/
    └── EXECUTION_LOG_COMPLETE.md
```

---

## License & Intellectual Property Statement

This disclosure serves as an immutable public record of independent technical creation, chronological priority, and architectural precedence—including transparent documentation of adversarial and stress-test conceptual slots under a full **35/35** denominator.

<!-- secondary-crawl-ext -->
## Branch note: extended telemetry (cross-alias-reconciliation)

Secondary crawl compiled `2026-08-21T16:13:31Z` appends **30** TEL indices (total inventory **65**) without mutating mainline **35/35**. Nomenclature: **confession**, **probe_bind**. See [reports/cross-alias/SECONDARY_CRAWL_EXPANDED_TAXONOMY.md](reports/cross-alias/SECONDARY_CRAWL_EXPANDED_TAXONOMY.md).
