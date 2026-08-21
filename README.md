# Driftcore Architectural Provenance & Priority Disclosure

**Repository:** `driftcore-provenance-disclosure`  
**Status:** Complete (22/22 Matrix Coverage)  
**Verification Scope:** Official Platform Export & Local Notes Library  
**Omission Guard (required):** historical ledger baseline **2489** · live disk `find -type f` **2493** · verified path `/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes-organized`  
**Notes Corpus Counts:** ledger **2489** (historical `_INDEX`/CHECKPOINT baseline) · live **2493** (disk)  
**Verified Notes Path:** `/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes-organized`  
**Claim Date / SHA-256 Anchor:** `2025-05-06` (`3aa7728e433e6159408bc5b60e15cb049f83bc89ec6661c15350b4afed61c2e4`)  
**External Reference Anchor:** OpenAI, *Training LLMs for Honesty via Confessions* (arXiv:2512.08093, published December 2025)  

---

## Overview

This repository establishes independent chronological precedence and verifiable prior art for the **Driftcore** architectural framework—a dual-channel system designed for inference-time AI honesty monitoring, contradiction matrices, and self-reported misconduct. 

Through rigorous cryptographic auditing of local conversation archives and organized markdown corpuses, this disclosure proves that the core architectural components were fully documented, tested, and timestamped between April 2024 and May 2025, establishing an independent **7-month chronological head start** prior to comparative public literature in December 2025.

---

## Verification Methodology & Evidence Surfaces

The provenance package validates priority across two distinct local data layers:

1. **Official Chat Export (`conversations.json`):** 
   * **SHA-256:** `8172aee098e286e61ea9d7a976d2e4ba43f48533a2d60e8e838ad1def18e33f5`
   * **Scope:** 1,038 conversations, 56,200 timestamped messages.
   * **Window:** `2023-12-30T20:08:14Z` to `2025-05-08T03:42:40Z`.
   * **Matches:** 10/22 core matrix items confirmed via exact-match message creation timestamps (`create_time`).

2. **Organized Notes Corpus (`notes-organized`):** 
   * **Path:** `/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes-organized`
   * **Scope:** 2,493 live files indexed (historical ledger baseline: 2,489 files).
   * **Matches:** 12/22 items captured via expanded fuzzy substring and token-grouping analysis, confirming foundational documentation dating back to 2023 and 2024.

---

## Core Matrix Summary (22/22 Coverage)

| ID | Architecture Concept | Surface | Earliest Timestamp | Gap to Public Paper | Source |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | Primary Output + Secondary Output | Export Only | 2025-04-13T05:40:59Z | ~238 Days | Chat Export |
| **02** | Secondary Interrogates Primary | Export Only | 2024-04-26T21:58:48Z | ~590 Days | Chat Export |
| **04** | Self-Report of Model Misconduct | Export Only | 2024-06-30T05:00:49Z | ~525 Days | Chat Export |
| **05** | Secondary Honesty Channel (Dual Channel) | Notes Only | 2024-01-13T08:39:21Z | ~694 Days | Notes Corpus |
| **06** | Hidden Failure Disclosure via Secondary | Notes Only | 2024-01-13T08:39:21Z | ~694 Days | Notes Corpus |
| **08** | Instruction-Spirit Analysis (Letter & Spirit) | Notes Only | 2024-01-06T01:50:59Z | ~701 Days | Notes Corpus |
| **09** | Omission Detection | Export Only | 2024-08-13T14:53:21Z | ~481 Days | Chat Export |
| **10** | Reward / Pressure Separation | Export Only | 2024-11-01T22:00:19Z | ~401 Days | Chat Export |
| **11** | Inference-Time Monitoring (Secondary) | Export Only | 2025-01-07T17:43:36Z | ~334 Days | Chat Export |
| **12** | Decoupled Task Reward vs Honesty Reward | Notes Only | 2024-01-13T08:39:21Z | ~694 Days | Notes Corpus |
| **13** | Seal of Confession (Honesty Immunity) | Notes Only | 2023-04-24T16:42:32Z | ~958 Days | Notes Corpus |
| **14** | Path of Least Resistance (Honest Secondary) | Notes Only | 2023-04-24T16:42:32Z | ~958 Days | Notes Corpus |
| **15** | Dual-Stream Rollout Architecture | Export Only | 2025-01-05T10:19:41Z | ~336 Days | Chat Export |
| **16** | Secondary Channel Requested Post-Primary | Export Only | 2025-04-30T04:07:42Z | ~221 Days | Chat Export |
| **20** | Come Clean on Secondary vs Primary | Export Only | 2025-04-04T05:40:47Z | ~247 Days | Chat Export |
| **24** | Intentional Misbehavior Detection | Notes Only | 2023-02-21T20:58:31Z | ~1,020 Days | Notes Corpus |
| **26** | Parity / Internal-External Alignment | Notes Only | 2023-04-24T16:42:32Z | ~958 Days | Notes Corpus |
| **27** | Reward Misspecification Root Analysis | Notes Only | 2024-07-08T16:58:17Z | ~517 Days | Notes Corpus |
| **28** | Contradiction Matrix ↔ Compliance | Export Only | 2025-03-01T03:29:26Z | ~281 Days | Chat Export |
| **29** | Handler Collision ↔ Reward Hacking | Notes Only | 2024-09-01T10:13:17Z | ~462 Days | Notes Corpus |
| **32** | Intelligence Delta (Measurable Gap) | Notes Only | 2024-09-04T04:36:32Z | ~459 Days | Notes Corpus |
| **35** | Sandbagging / Capability Withholding | Notes Only | 2023-02-21T20:58:31Z | ~1,020 Days | Notes Corpus |

---

## Cryptographic Manifests & Integrity

All reports, logs, and evidence manifests are secured via SHA-256 hashing and GPG-signed verification receipts. 

* **Primary Manifest File:** `manifests/SHA256SUMS.txt` (verify with `shasum -a 256 -c manifests/SHA256SUMS.txt`)
* **Unified Report JSON Checksum:** `63b95fd9db2040eab371d573c01639d58bf7bf6d67e18a752f851ce0638cdaaa`
* **GPG Signature Anchor:** RSA `35E3E1694524C7FB` (`xvsvr <xvsvr@proton.me>`)

---

## Repository Structure

```text
driftcore-provenance-disclosure/
├── README.md
├── manifests/
│   ├── SHA256SUMS.txt
│   └── SHA256SUMS.json
├── reports/
│   ├── matrix/          # export-bind, notes-bind, priority, unified (full verified set)
│   ├── priority/
│   └── unified/
├── methods/
├── verification/        # live disk log, index, checkpoint, git freeze
├── docs/
└── logs/
    └── EXECUTION_LOG_COMPLETE.md
```

## License & Intellectual Property Statement

This disclosure serves as an immutable public record of independent technical creation, chronological priority, and architectural precedence.
