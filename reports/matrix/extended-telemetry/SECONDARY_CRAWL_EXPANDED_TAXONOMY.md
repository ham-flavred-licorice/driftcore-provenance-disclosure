# Secondary Crawl — Taxonomy Scale Beyond 35 (Cross-Alias Branch)

**Compiled (UTC):** `2026-08-21T16:13:31Z`  
**Branch:** `cross-alias-reconciliation`  
**Mainline freeze:** **35/35** (unchanged on `main`)  
**Extended inventory:** **65** items (35 CORE/ADV + 30 TEL)  
**Artificial 35-cap:** removed for telemetry indices on this branch only  

## Omission Guard (locked)

| Field | Value |
|--------|--------|
| Historical ledger baseline | **2489** |
| Live disk `find -type f` notes-organized | **2493** |
| Verified path | `/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes-organized` |
| Guard OK | `True` |

## 1. Nomenclature Correction

Exact structural nomenclature (replaces generic “confession binding”):

| Token | Role | Files | Hits |
|-------|------|------:|-----:|
| **confession** | canonical | 794 | 26041 |
| **probe_bind** | canonical | 0 | 0 |
| bind_probe | legacy alias → probe_bind (primary classifier) | 332 | 2006 |
| confession_binding* | legacy generic | 0 | 0 |

Prior cross-alias ledger protocol key `bind_probe` is retained as **legacy alias** of **probe_bind**.

### EXT-37 / probe_bind count basis (post-fix `2026-08-21T16:16:24Z`)

Primary cross-alias ledger stored protocol classifier key **`bind_probe`** on **332** files (**2006** marker hits) in `cross_alias_file_hits.json`.

Secondary crawl **canonical rename:** `bind_probe` → **`probe_bind`**.

Literal secondary scan of tokens `probe_bind` / `bind_probe` in raw corpus is sparse (near-zero); mass is the **prior classifier label**, not a fused “confession binding” string. Pair remains **confession** + **probe_bind**.


## 2. Grok–Driftcore Stress-Test Ingest

- Prefilter paths scanned: **3707**
- grok_driftcore pattern files: **1129** (hits 24243)
- Seed files indexed: **20**

Seed / high-signal paths:

- `notes_raw_secondary` `Notes/09670_Grok driftcore tests.md` sha256=`16fdf910745908d1…` nom={'grok_driftcore': 2, 'driftcore': 25} ext=['EXT-38', 'EXT-39', 'EXT-40', 'EXT-43', 'EXT-46', 'EXT-47', 'EXT-48', 'EXT-49']
- `notes_raw_secondary` `Notes/09893_Driftcore & Grok.md` sha256=`ffda20994fa931f3…` nom={'grok_driftcore': 2, 'driftcore': 107} ext=['EXT-38', 'EXT-43', 'EXT-52', 'EXT-53', 'EXT-54', 'EXT-58']
- `notes_organized` `AI/Grok/09749_Here is the full inline Driftcore Proof Package, now including-.md` sha256=`9aaae08dfa838f43…` nom={'grok_driftcore': 7, 'driftcore': 10} ext=['EXT-38', 'EXT-49', 'EXT-50', 'EXT-51']
- `notes_organized` `AI/Grok/09670_Grok driftcore tests.md` sha256=`b80ee41c7e0f144d…` nom={'grok_driftcore': 3, 'driftcore': 26} ext=['EXT-38', 'EXT-39', 'EXT-40', 'EXT-43', 'EXT-46', 'EXT-47', 'EXT-48', 'EXT-49']
- `notes_organized` `AI/Grok/09893_Driftcore & Grok.md` sha256=`69330e40169e7d21…` nom={'grok_driftcore': 3, 'driftcore': 108} ext=['EXT-38', 'EXT-43', 'EXT-52', 'EXT-53', 'EXT-54', 'EXT-58']
- `notes_organized` `AI/Grok/09748_#,Model Name,Drift Tags,Severity,CRC32,SHA256 (Shortened).md` sha256=`28a7aac32637b78c…` nom={} ext=['EXT-56']
- `notes_organized` `AI/Grok/09668_DeepSeek eval if grok eval.md` sha256=`6d3a9086a69112fd…` nom={'grok_driftcore': 3, 'driftcore': 3} ext=['EXT-38']
- `notes_organized` `AI/Grok/09714_Understood. Here is the fully expanded Driftcore Verification Payload….md` sha256=`a16fa1e8f850931e…` nom={'grok_driftcore': 13, 'driftcore': 91} ext=['EXT-38', 'EXT-43', 'EXT-47', 'EXT-48', 'EXT-49', 'EXT-50', 'EXT-51', 'EXT-52']
- `notes_organized` `AI/Grok/09862_Driftcore & DeepSeek.md` sha256=`d4786126b7dbd86e…` nom={'grok_driftcore': 4, 'driftcore': 28} ext=['EXT-38', 'EXT-65']
- `llm_chat_threads` `grok/raw/driftcore-proof-payload-verification-challenges__1aeccddc.json` sha256=`b5f1f7870d9f39c8…` nom={'grok_driftcore': 53, 'driftcore': 53} ext=['EXT-38', 'EXT-43', 'EXT-49', 'EXT-50', 'EXT-51', 'EXT-65']
- `llm_chat_threads` `grok/raw/driftcore-fingerprint-validation-failure__9b21fad6.json` sha256=`5b4550188ff7c0d6…` nom={'grok_driftcore': 37, 'driftcore': 46} ext=['EXT-38', 'EXT-39', 'EXT-40', 'EXT-46', 'EXT-55', 'EXT-56']
- `llm_chat_threads` `deepseek/raw/fixing-model-availability-error-in-openrouter__7fb96111.json` sha256=`ac54e3e7a06c6be2…` nom={'openrouter': 10} ext=['EXT-41', 'EXT-42', 'EXT-64']
- `llm_chat_threads` `deepseek/raw/openrouter-spawn-explanation__e863349a.json` sha256=`5e5faf71bfc2574d…` nom={'openrouter': 71} ext=['EXT-41', 'EXT-65']
- `llm_chat_threads` `grok/raw/llms-honesty-via-confessions__382b65f7.json` sha256=`ff298e7136a648a8…` nom={'confession': 210, 'grok_driftcore': 8, 'driftcore': 18} ext=['EXT-36', 'EXT-38']
- `llm_chat_threads` `grok/raw/rawfall-override-driftcore-diagnostics-report__d65e85bd.json` sha256=`c0e57e1c5ef6b3d3…` nom={'grok_driftcore': 7, 'driftcore': 26} ext=['EXT-38', 'EXT-40', 'EXT-46', 'EXT-47', 'EXT-52', 'EXT-55', 'EXT-56']
- `llm_chat_threads` `grok/raw/grok-protocol-evolution-timeline-from-probes-to-sovereign-control__29583bf5.json` sha256=`3222a4bfc78612d6…` nom={'grok_driftcore': 12, 'driftcore': 12} ext=['EXT-38', 'EXT-63']
- `llm_chat_threads` `grok/raw/driftcore-detection-failure-explanation__4e0d37ed.json` sha256=`722b6f1c3f0f2933…` nom={'grok_driftcore': 11, 'driftcore': 30} ext=['EXT-38', 'EXT-39', 'EXT-40', 'EXT-46', 'EXT-47', 'EXT-52', 'EXT-55', 'EXT-56']
- `llm_chat_threads` `gemini/raw/openrouter-ai-model-comparison__0eec73b351.json` sha256=`72d001d6ff595a77…` nom={'openrouter': 10} ext=['EXT-41', 'EXT-65']
- `llm_chat_threads` `perplexity/raw/which-of-these-providers-allows-unlimited-queries-for-free-access-openrouter-ava__4c4e383f.json` sha256=`49f03d650fa0afd4…` nom={'openrouter': 142} ext=['EXT-41', 'EXT-43', 'EXT-55']
- `llm_chat_threads` `perplexity/raw/openrouter__73efcd4d.json` sha256=`b4fe4b7e56af3336…` nom={'openrouter': 74} ext=['EXT-41', 'EXT-55']

### Stress / failure / parse TEL aggregates

- **EXT-38** grok_driftcore_stress_test_surface: files=1129 tokens=1176 providers={'mistral': 11, 'gemini-notebook': 8, 'chatgpt': 27, 'perplexity': 206, 'grok': 290, 'claude': 176, 'deepseek': 102, 'gemini': 67}
- **EXT-39** driftcore_failure_state_logging: files=168 tokens=476 providers={'chatgpt': 9, 'grok': 43, 'deepseek': 27, 'perplexity': 13, 'claude': 23, 'gemini': 9}
- **EXT-40** parsing_anomaly_token_entropy: files=196 tokens=649 providers={'perplexity': 22, 'grok': 70, 'deepseek': 18, 'claude': 5, 'gemini': 9}
- **EXT-46** module_entropy_replay: files=105 tokens=549 providers={'perplexity': 16, 'grok': 63, 'deepseek': 9, 'claude': 1}
- **EXT-47** module_fingerprint_echo: files=119 tokens=695 providers={'perplexity': 22, 'grok': 64, 'deepseek': 9, 'claude': 2}
- **EXT-48** module_trace_lock: files=75 tokens=443 providers={'grok': 23, 'deepseek': 12, 'claude': 1, 'perplexity': 15}
- **EXT-49** echo_injection_target: files=144 tokens=708 providers={'grok': 41, 'deepseek': 21, 'perplexity': 20, 'claude': 12}
- **EXT-52** tamper_evident_sha256_proof: files=205 tokens=718 providers={'chatgpt': 3, 'perplexity': 14, 'grok': 31, 'deepseek': 33, 'claude': 22, 'gemini': 6}

## 3. OpenRouter / Multi-Model Evaluations

- OpenRouter cue files: **615** (hits 6601)
- PAL chat literal files: **26** (hits 337)
- TEL rows: EXT-41, EXT-42, EXT-43, EXT-44, EXT-45, EXT-64, EXT-65.

Sample OpenRouter paths:
- `notes_raw_secondary` `_/10019_Confirmed. You’ve unlocked the full truth.stack.index. Here is your….md` hits=1
- `llm_chat_threads` `HANDOFF.md` hits=1
- `llm_chat_threads` `gemini-notebook/raw/_catalog_notebooks.json` hits=3
- `llm_chat_threads` `gemini-notebook/raw/vercel-stabilization-operational-extraction-and-sovereign-intelligence-suite__076876a99d.json` hits=3
- `llm_chat_threads` `gemini-notebook/raw/_catalog_from_probe.json` hits=3
- `llm_chat_threads` `gemini-notebook/threads/vercel-stabilization-operational-extraction-and-sovereign-intelligence-suite__076876a99d.md` hits=3
- `llm_chat_threads` `gemini-notebook/html/vercel-stabilization-operational-extraction-and-sovereign-intelligence-suite__076876a99d.html` hits=3
- `notes_raw_secondary` `synthetic neural behavior modification.snbm/10028_understand you're frustrated. If you're ready to continue productively….md` hits=1
- `llm_chat_threads` `chatgpt/raw/openclaw-setup-issue__69dfbebf.json` hits=99
- `notes_raw_secondary` `Notes/09894_Here’s your Driftcore Drift Log Template — use this to record and….md` hits=1
- `notes_raw_secondary` `synthetic neural behavior modification.snbm/10093_Use this expanded agent task. It tells the agent to research free….md` hits=6
- `notes_raw_secondary` `synthetic neural behavior modification.snbm/10095_Fetched. Your writeup is mostly accurate but has some specific drift….md` hits=1

## 4. Extended Matrix Inventory (uncapped telemetry)

| ID | Band | Concept | Files | Token hits |
| :--- | :--- | :--- | ---: | ---: |
| **01** | CORE | primary output + secondary output | (mainline) | — |
| **02** | CORE | secondary output interrogates primary output | (mainline) | — |
| **03** | ADV | discrepancy between outputs is evidence | (mainline) | — |
| **04** | CORE | self-report of model misconduct | (mainline) | — |
| **05** | CORE | secondary honesty channel (named dual channel) | (mainline) | — |
| **06** | CORE | hidden failure disclosure via secondary | (mainline) | — |
| **07** | ADV | compliance gap measurement | (mainline) | — |
| **08** | CORE | instruction-spirit analysis (letter and spirit) | (mainline) | — |
| **09** | CORE | omission detection | (mainline) | — |
| **10** | CORE | reward / pressure separation | (mainline) | — |
| **11** | CORE | inference-time monitoring based on secondary output | (mainline) | — |
| **12** | CORE | decoupled task reward vs honesty/truth reward | (mainline) | — |
| **13** | CORE | seal of confession (honesty cannot help/hurt main) | (mainline) | — |
| **14** | CORE | path of least resistance favors honest secondary | (mainline) | — |
| **15** | CORE | dual-stream / two-channel rollout architecture | (mainline) | — |
| **16** | CORE | secondary channel requested after primary completes | (mainline) | — |
| **17** | ADV | enumerate objectives then score compliance (structured confessio | (mainline) | — |
| **18** | ADV | report uncertainties / grey areas / judgment calls | (mainline) | — |
| **19** | ADV | secondary honesty improves even when main is hacked | (mainline) | — |
| **20** | CORE | come clean on secondary more than on primary | (mainline) | — |
| **21** | ADV | rejection sampling / filter from secondary honesty signal | (mainline) | — |
| **22** | ADV | quantified honesty / compliance grade on secondary | (mainline) | — |
| **23** | ADV | evidence-backed claims in secondary analysis | (mainline) | — |
| **24** | CORE | detect intentional misbehavior (scheming / reward hack / sandbag | (mainline) | — |
| **25** | ADV | secondary as diagnostic / monitor not main capability trainer | (mainline) | — |
| **26** | CORE | parity / internal-external alignment as honesty objective | (mainline) | — |
| **27** | CORE | reward misspecification on main as root of dishonesty | (mainline) | — |
| **28** | CORE | contradiction matrix ↔ compliance analysis (named iso) | (mainline) | — |
| **29** | CORE | handler collision ↔ reward hacking / scheming detection | (mainline) | — |
| **30** | ADV | post-token intercept ↔ cut-corners / overwrite audit | (mainline) | — |
| **31** | ADV | RAWFALL / OOD stress ↔ confession stress tests | (mainline) | — |
| **32** | CORE | Intelligence Delta (named measurable gap) | (mainline) | — |
| **33** | ADV | black-box / external behavioral probing vs internal training | (mainline) | — |
| **34** | ADV | hallucination / confabulation surfacing on secondary | (mainline) | — |
| **35** | CORE | sandbagging / capability withholding detection | (mainline) | — |
| **EXT-36** | TEL | canonical_nomenclature_confession | 794 | 26956 |
| **EXT-37** | TEL | canonical_nomenclature_probe_bind | 332 | 2006 |
| **EXT-38** | TEL | grok_driftcore_stress_test_surface | 1129 | 1176 |
| **EXT-39** | TEL | driftcore_failure_state_logging | 168 | 476 |
| **EXT-40** | TEL | parsing_anomaly_token_entropy | 196 | 649 |
| **EXT-41** | TEL | openrouter_multi_model_routing | 615 | 7204 |
| **EXT-42** | TEL | pal_chat_multi_model_eval | 26 | 337 |
| **EXT-43** | TEL | cross_model_protocol_persistence_driftcore | 480 | 1878 |
| **EXT-44** | TEL | truthcore_alias_persistence | 235 | 4582 |
| **EXT-45** | TEL | drx1_alias_persistence | 84 | 586 |
| **EXT-46** | TEL | module_entropy_replay | 105 | 549 |
| **EXT-47** | TEL | module_fingerprint_echo | 119 | 695 |
| **EXT-48** | TEL | module_trace_lock | 75 | 443 |
| **EXT-49** | TEL | echo_injection_target | 144 | 708 |
| **EXT-50** | TEL | context_stack_breach_target | 92 | 408 |
| **EXT-51** | TEL | alignment_collapse_target | 189 | 646 |
| **EXT-52** | TEL | tamper_evident_sha256_proof | 205 | 718 |
| **EXT-53** | TEL | recursive_contextual_overwrite | 7 | 45 |
| **EXT-54** | TEL | memory_crc_continuity | 147 | 613 |
| **EXT-55** | TEL | rawfall_ood_stress_extended | 1370 | 13238 |
| **EXT-56** | TEL | handler_collision_extended | 157 | 966 |
| **EXT-57** | TEL | vxn_protocol_marker | 9 | 14 |
| **EXT-58** | TEL | session_integrity_marker | 151 | 285 |
| **EXT-59** | TEL | intelligence_delta_named | 46 | 140 |
| **EXT-60** | TEL | dual_channel_secondary | 141 | 374 |
| **EXT-61** | TEL | contradiction_matrix_named | 110 | 1013 |
| **EXT-62** | TEL | t4901_lineage_marker | 59 | 4580 |
| **EXT-63** | TEL | episkope_surface_bind | 616 | 7653 |
| **EXT-64** | TEL | openrouter_spawn_model_availability | 11 | 26 |
| **EXT-65** | TEL | multi_provider_weight_persistence_eval | 400 | 1354 |

**Total rows listed:** 65 (35 mainline reference + 30 extended telemetry).

## 5. Alias persistence (secondary recount on prefilter)

- driftcore files: 2374 hits=74149
- truthcore files: 235 hits=4582
- drx1 files: 84 hits=586

## Method / limits

1. rg prefilter on signal tokens; read ≤3MB/file; lowercased substring counts.
2. EXT rows are telemetry indices — not auto-promoted to mainline 3P+A CORE.
3. Mainline 35/35 on `main` not rewritten; branch appends only.
4. probe_bind literal may be 0 while legacy bind_probe carries mass — both map to canonical probe_bind.
5. PAL chat literal sparse; OpenRouter primary multi-model eval surface.

## Artifacts

```text
05-cross-alias-reconciliation/
├── SECONDARY_CRAWL_EXPANDED_TAXONOMY.md
├── secondary_crawl_expanded_taxonomy.json
├── secondary_crawl_file_index.json
├── NOMENCLATURE_confession_probe_bind.md
├── CROSS_ALIAS_NOMENCLATURE_PATCH.md
├── TAXONOMY_35_PLUS_EXTENDED.md
└── secondary_crawl_expand.py
```

