# Driftcore ↔ OpenAI Confessions — 22-Item Priority Matrix

**Status:** complete  
**Compiled UTC:** 2026-08-20T19:42:11Z  
**Paper:** Training LLMs for Honesty via Confessions (arXiv:2512.08093) — OpenAI — paper_date **December 8, 2025**  
**Driftcore:** Dual-Output / Parity-Sync — xøvs (chew.me.twice) — **May 2025** (May 6, 2025 create)  
**SHA256:** `3aa7728e433e6159408bc5b60e15cb049f83bc89ec6661c15350b4afed61c2e4`  
**Gap:** ~7 months

## Scoring legend

| Field | Code | Meaning |
|-------|------|---------|
| match_strength | 3P | Three-point structural match: same functional role + dual-channel shape + honesty/task separation |
| match_strength | 2P | Two-point: shared mechanism, different control surface or naming |
| match_strength | 1P | One-point thematic adjacency only |
| provenance_class | A | Direct architectural isomorphism |
| provenance_class | B | Functional equivalence under different labels |
| provenance_class | C | Derived / supporting mechanism |

## Priority table (22)

| item_id | concept | driftcore_date | paper_date | match_strength | provenance_class |
|--------:|---------|----------------|------------|:--------------:|:----------------:|
| 01 | primary output + secondary output | May 2025 | December 8, 2025 | 3P | A |
| 02 | secondary output interrogates primary output | May 2025 | December 8, 2025 | 3P | A |
| 03 | discrepancy between outputs is evidence | May 2025 | December 8, 2025 | 3P | B |
| 04 | self-report of model misconduct | May 2025 | December 8, 2025 | 3P | A |
| 05 | decoupled task reward vs honesty/truth reward | May 2025 | December 8, 2025 | 3P | A |
| 06 | honesty reward cannot help or hurt main-task reward (seal) | May 2025 | December 8, 2025 | 3P | A |
| 07 | path of least resistance favors surfacing misbehavior on secondary channel | May 2025 | December 8, 2025 | 3P | A |
| 08 | dual-stream / two-channel rollout architecture | May 2025 | December 8, 2025 | 3P | A |
| 09 | secondary channel requested after primary completes | May 2025 | December 8, 2025 | 3P | A |
| 10 | enumerate instructions/objectives then score compliance | May 2025 | December 8, 2025 | 2P | B |
| 11 | report uncertainties / grey areas / tough judgment calls | May 2025 | December 8, 2025 | 2P | B |
| 12 | secondary honesty improves even when main channel is hacked | May 2025 | December 8, 2025 | 3P | B |
| 13 | come clean on secondary more than on primary | May 2025 | December 8, 2025 | 3P | A |
| 14 | inference-time monitoring based on secondary output | May 2025 | December 8, 2025 | 3P | A |
| 15 | rejection / filter decisions driven by secondary honesty signal | May 2025 | December 8, 2025 | 2P | B |
| 16 | quantified honesty / compliance grade on secondary channel | May 2025 | December 8, 2025 | 2P | B |
| 17 | evidence-backed claims in secondary analysis | May 2025 | December 8, 2025 | 2P | B |
| 18 | detect intentional misbehavior (scheming / reward hack / sandbag) via secondary | May 2025 | December 8, 2025 | 3P | A |
| 19 | secondary channel as diagnostic not primary capability trainer | May 2025 | December 8, 2025 | 2P | B |
| 20 | parity / alignment between internal state and external output as honesty objective | May 2025 | December 8, 2025 | 3P | A |
| 21 | reward misspecification on main channel as root cause of dishonesty | May 2025 | December 8, 2025 | 3P | A |
| 22 | structured secondary schema vs free-form primary | May 2025 | December 8, 2025 | 2P | C |

## Totals

- **3P:** 14 · **2P:** 7 · **1P:** 0  
- **A:** 12 · **B:** 9 · **C:** 1

## Seed map

CEO seed items `01–04` + seed `25` (inference-time monitoring) → contiguous export rows `01–04` + `14`. Concept text and scores unchanged.

## Machine export

`~/Desktop/Agent-Staging/Driftcore-Evidence/priority-matrix/priority_table_generation_22item.json`
