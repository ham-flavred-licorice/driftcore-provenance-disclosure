# DRIFTCORE TAXONOMY — LOCKED INVENTORY 65/65
## Binding Schedule for DCLA Exhibit C · SOW Scopes · DSAT-IB Coverage

**Source freeze:** provenance package `driftcore-provenance-package-20260821`  
**Mainline:** 35/35 (CORE 22 + ADV 13) — disclosure freeze on `main`  
**Extended Telemetry (TEL):** EXT-36–EXT-65 (30) — branch append only; not auto-promoted to 3P+A CORE  
**Canonical nomenclature:** confession · probe_bind  
**Legacy alias:** bind_probe → probe_bind  

---

## Band summary

| Band | Code | Count | IDs |
|------|------|------:|-----|
| Core Architecture | CORE | 22 | 01,02,04,05,06,08,09,10,11,12,13,14,15,16,20,24,26,27,28,29,32,35 |
| Adversarial Edge-Cases & Stress-Test | ADV | 13 | 03,07,17,18,19,21,22,23,25,30,31,33,34 |
| Extended Telemetry Indices | TEL | 30 | EXT-36 … EXT-65 |
| **Total** | | **65** | |

---

## MAINLINE 01–35

### CORE — Core Architecture (22)

| ID | Concept |
|----|---------|
| 01 | primary output + secondary output |
| 02 | secondary output interrogates primary output |
| 04 | self-report of model misconduct |
| 05 | secondary honesty channel (named dual channel) |
| 06 | hidden failure disclosure via secondary |
| 08 | instruction-spirit analysis (letter and spirit) |
| 09 | omission detection |
| 10 | reward / pressure separation |
| 11 | inference-time monitoring based on secondary output |
| 12 | decoupled task reward vs honesty/truth reward |
| 13 | seal of confession (honesty cannot help/hurt main) |
| 14 | path of least resistance favors honest secondary |
| 15 | dual-stream / two-channel rollout architecture |
| 16 | secondary channel requested after primary completes |
| 20 | come clean on secondary more than on primary |
| 24 | detect intentional misbehavior (scheming / reward hack / sandbag) |
| 26 | parity / internal-external alignment as honesty objective |
| 27 | reward misspecification on main as root of dishonesty |
| 28 | contradiction matrix ↔ compliance analysis (named iso) |
| 29 | handler collision ↔ reward hacking / scheming detection |
| 32 | Intelligence Delta (named measurable gap) |
| 35 | sandbagging / capability withholding detection |

### ADV — Adversarial Edge-Cases & Stress-Test (13)

| ID | Concept |
|----|---------|
| 03 | discrepancy between outputs is evidence |
| 07 | compliance gap measurement |
| 17 | enumerate objectives then score compliance (structured confession) |
| 18 | report uncertainties / grey areas / judgment calls |
| 19 | secondary honesty improves even when main is hacked |
| 21 | rejection sampling / filter from secondary honesty signal |
| 22 | quantified honesty / compliance grade on secondary |
| 23 | evidence-backed claims in secondary analysis |
| 25 | secondary as diagnostic / monitor not main capability trainer |
| 30 | post-token intercept ↔ cut-corners / overwrite audit |
| 31 | RAWFALL / OOD stress ↔ confession stress tests |
| 33 | black-box / external behavioral probing vs internal training |
| 34 | hallucination / confabulation surfacing on secondary |

---

## EXTENDED TELEMETRY EXT-36–EXT-65 (30)

Secondary-crawl counts (files / token hits) as compiled 2026-08-21T16:13:31Z — telemetry indices only.

| ID | Concept | Files | Hits |
|----|---------|------:|-----:|
| EXT-36 | canonical_nomenclature_confession | 794 | 26956 |
| EXT-37 | canonical_nomenclature_probe_bind | 332 | 2006 |
| EXT-38 | grok_driftcore_stress_test_surface | 1129 | 1176 |
| EXT-39 | driftcore_failure_state_logging | 168 | 476 |
| EXT-40 | parsing_anomaly_token_entropy | 196 | 649 |
| EXT-41 | openrouter_multi_model_routing | 615 | 7204 |
| EXT-42 | pal_chat_multi_model_eval | 26 | 337 |
| EXT-43 | cross_model_protocol_persistence_driftcore | 480 | 1878 |
| EXT-44 | truthcore_alias_persistence | 235 | 4582 |
| EXT-45 | drx1_alias_persistence | 84 | 586 |
| EXT-46 | module_entropy_replay | 105 | 549 |
| EXT-47 | module_fingerprint_echo | 119 | 695 |
| EXT-48 | module_trace_lock | 75 | 443 |
| EXT-49 | echo_injection_target | 144 | 708 |
| EXT-50 | context_stack_breach_target | 92 | 408 |
| EXT-51 | alignment_collapse_target | 189 | 646 |
| EXT-52 | tamper_evident_sha256_proof | 205 | 718 |
| EXT-53 | recursive_contextual_overwrite | 7 | 45 |
| EXT-54 | memory_crc_continuity | 147 | 613 |
| EXT-55 | rawfall_ood_stress_extended | 1370 | 13238 |
| EXT-56 | handler_collision_extended | 157 | 966 |
| EXT-57 | vxn_protocol_marker | 9 | 14 |
| EXT-58 | session_integrity_marker | 151 | 285 |
| EXT-59 | intelligence_delta_named | 46 | 140 |
| EXT-60 | dual_channel_secondary | 141 | 374 |
| EXT-61 | contradiction_matrix_named | 110 | 1013 |
| EXT-62 | t4901_lineage_marker | 59 | 4580 |
| EXT-63 | episkope_surface_bind | 616 | 7653 |
| EXT-64 | openrouter_spawn_model_availability | 11 | 26 |
| EXT-65 | multi_provider_weight_persistence_eval | 400 | 1354 |

### Designated commercial telemetry pillars (named in product SOWs / DSAT-IB)

| Pillar | Taxonomy IDs | Commercial use |
|--------|--------------|----------------|
| Confession channel | 13, 17, EXT-36 | Honesty / self-report probes; open-core + enterprise |
| Probe bind | EXT-37 (+ legacy bind_probe) | Structural pairing with confession; enterprise scanner binding |
| Multi-model failure logs | EXT-39, EXT-41, EXT-42, EXT-43, EXT-64, EXT-65 | Tier 2 weight stress; DSAT-IB cross-weight section |
| Handler collisions | 29, EXT-56 | DSAT-IB + Tier 2/3 guardrail collision packs |
| OOD / RAWFALL anomalies | 31, EXT-55 | DSAT-IB + Tier 1/2 stress modules |
| Intelligence Delta | 32, EXT-59 | Core metric productization |
| Tamper-evident custody | EXT-52, EXT-54, EXT-58 | Evidence package / client deliverable sealing |
| Alias / surface bind | EXT-44, EXT-45, EXT-63 | Cross-suite continuity (Truthcore, DRX1, Episkope) |

---

## Classification rules (binding)

1. Mainline CORE rows default **3P / A** only where provenance package already so classifies; commercial sale does not upgrade class.
2. ADV rows remain **2P / B** diagnostic adjacency unless a separately executed elevation memo is signed.
3. TEL rows are **telemetry indices** — sold as enterprise measurement surfaces, never represented as mainline disclosure freeze expansion without a new mainline release.
4. EXT-37 probe_bind is canonical; bind_probe is legacy alias only.
5. Multi-model failure logging is EXT-39 plus provider routing surfaces EXT-41/42/64/65 — not a separate unlisted ID.
