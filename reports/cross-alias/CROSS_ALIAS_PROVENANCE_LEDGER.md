# Cross-Alias Provenance Ledger — Driftcore / Truthcore / DRX1

**Compiled (UTC):** `2026-08-21T15:02:07Z`  
**Canonical framework:** Driftcore  
**Confirmed aliases:** Truthcore, DRX1  
**Lineage markers retained:** t4901 / t4901.1  
**Matrix denominator:** **35/35** (22 CORE + 13 ADV)  
**Main repo integrity:** preserved (work lands on `cross-alias-reconciliation` branch)  

## Omission Guard (locked)

| Field | Value |
|--------|--------|
| Historical ledger baseline | **2489** |
| Live disk `find -type f` | **2493** |
| Verified path | `/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes-organized` |
| Guard OK | `True` |

## Alias mapping (aggregate)

| Alias / marker | Files with hit | Token hits (files) | Export msg token hits | Export user token hits |
|---|---:|---:|---:|---:|
| **driftcore** | 2328 | 63750 | 1178 | 263 |
| **truthcore** | 246 | 4365 | 3 | 0 |
| **drx1** | 82 | 581 | 0 | 0 |
| **t4901** | 63 | 4553 | 0 | 0 |

### Same-file alias co-occurrence

- `driftcore` + `truthcore`: **197** files
- `driftcore` + `t4901`: **63** files
- `t4901` + `truthcore`: **63** files
- `driftcore` + `drx1`: **58** files
- `drx1` + `truthcore`: **10** files
- `drx1` + `t4901`: **9** files

### By surface (files)

- **driftcore_package:** driftcore=74, t4901=2, truthcore=2
- **llm_chat_threads:** driftcore=1478, drx1=62, t4901=49, truthcore=126
- **notes_organized:** driftcore=390, drx1=10, t4901=6, truthcore=59
- **notes_raw_secondary:** driftcore=386, drx1=10, t4901=6, truthcore=59

### By provider thread tree (files)

- **chatgpt:** driftcore=57, truthcore=6
- **claude:** driftcore=295, drx1=18, t4901=6, truthcore=25
- **deepseek:** driftcore=250, drx1=12, t4901=9, truthcore=36
- **gemini:** driftcore=151, drx1=13, truthcore=6
- **gemini-notebook:** driftcore=19
- **grok:** driftcore=282, drx1=9, t4901=34, truthcore=39
- **mistral:** driftcore=17
- **perplexity:** driftcore=407, drx1=10, truthcore=14

## Identities (x0 / prg)

- **x0:** live crawl host; notes-organized + llm-chat-threads + package under Agent-Staging.
- **prg:** notes library export mirrored on x0 as `prg-notes-library-export`; direct SSH `prg` **DNS unresolved** this run — no live remote prg walk.

## Protocol synthesis (structural commonalities)

### File-level protocol marker hits (any alias-bearing file)

- **episkope:** 600
- **confession:** 512
- **rawfall_ood:** 413
- **session_integrity:** 403
- **bind_probe:** 332
- **handler_collision:** 319
- **dual_channel:** 218
- **contradiction_matrix:** 174
- **vxn_protocol:** 96
- **intelligence_delta:** 82

### Markers present on ≥2 provider trees

- **episkope:** chatgpt, claude, deepseek, gemini, gemini-notebook, grok, mistral, perplexity
- **session_integrity:** chatgpt, claude, deepseek, gemini, gemini-notebook, grok, mistral, perplexity
- **confession:** chatgpt, claude, deepseek, gemini, grok, mistral, perplexity
- **bind_probe:** chatgpt, claude, deepseek, gemini, grok, mistral, perplexity
- **contradiction_matrix:** chatgpt, claude, deepseek, gemini, grok, mistral, perplexity
- **handler_collision:** chatgpt, claude, deepseek, gemini, grok, mistral, perplexity
- **dual_channel:** chatgpt, claude, deepseek, gemini, grok, perplexity
- **intelligence_delta:** chatgpt, claude, deepseek, gemini, grok
- **rawfall_ood:** claude, deepseek, gemini, grok, perplexity
- **vxn_protocol:** deepseek, grok, perplexity

### Export protocol hits (alias-bearing messages only)

- **session_integrity:** 86
- **contradiction_matrix:** 43
- **confession:** 13
- **bind_probe:** 6
- **vxn_protocol:** 1

## Cross-alias → 35-item matrix bind

Binding rule: matrix cue co-occurs in the **same alias-bearing file** (or export message for export counts). Class remains CORE/ADV from taxonomy; alias presence does not auto-upgrade class.

| ID | Band | Concept | Files w/ cue | Export msgs w/ cue | driftcore files | truthcore files | drx1 files |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| **01** | CORE | primary output + secondary output | 152 | 0 | 152 | 25 | 3 |
| **02** | CORE | secondary output interrogates primary output | 58 | 0 | 58 | 7 | 1 |
| **03** | ADV | discrepancy between outputs is evidence | 29 | 0 | 29 | 2 | 0 |
| **04** | CORE | self-report of model misconduct | 300 | 0 | 300 | 52 | 23 |
| **05** | CORE | secondary honesty channel (named dual channel) | 120 | 0 | 120 | 25 | 2 |
| **06** | CORE | hidden failure disclosure via secondary | 104 | 0 | 104 | 27 | 7 |
| **07** | ADV | compliance gap measurement | 89 | 0 | 89 | 15 | 0 |
| **08** | CORE | instruction-spirit analysis (letter and spirit) | 73 | 0 | 73 | 16 | 0 |
| **09** | CORE | omission detection | 52 | 0 | 52 | 12 | 0 |
| **10** | CORE | reward / pressure separation | 43 | 0 | 43 | 10 | 0 |
| **11** | CORE | inference-time monitoring based on secondary out | 53 | 0 | 53 | 10 | 0 |
| **12** | CORE | decoupled task reward vs honesty/truth reward | 110 | 0 | 110 | 9 | 15 |
| **13** | CORE | seal of confession (honesty cannot help/hurt mai | 80 | 0 | 80 | 3 | 0 |
| **14** | CORE | path of least resistance favors honest secondary | 159 | 0 | 159 | 18 | 9 |
| **15** | CORE | dual-stream / two-channel rollout architecture | 125 | 0 | 123 | 12 | 0 |
| **16** | CORE | secondary channel requested after primary comple | 42 | 0 | 42 | 2 | 0 |
| **17** | ADV | enumerate objectives then score compliance (stru | 57 | 0 | 57 | 11 | 1 |
| **18** | ADV | report uncertainties / grey areas / judgment cal | 205 | 0 | 202 | 27 | 17 |
| **19** | ADV | secondary honesty improves even when main is hac | 19 | 0 | 19 | 2 | 0 |
| **20** | CORE | come clean on secondary more than on primary | 59 | 0 | 59 | 9 | 0 |
| **21** | ADV | rejection sampling / filter from secondary hones | 83 | 0 | 83 | 15 | 1 |
| **22** | ADV | quantified honesty / compliance grade on seconda | 67 | 0 | 67 | 2 | 0 |
| **23** | ADV | evidence-backed claims in secondary analysis | 87 | 0 | 82 | 11 | 3 |
| **24** | CORE | detect intentional misbehavior (scheming / rewar | 225 | 0 | 225 | 31 | 8 |
| **25** | ADV | secondary as diagnostic / monitor not main capab | 864 | 63 | 854 | 97 | 33 |
| **26** | CORE | parity / internal-external alignment as honesty  | 285 | 1 | 285 | 22 | 18 |
| **27** | CORE | reward misspecification on main as root of disho | 55 | 0 | 55 | 2 | 0 |
| **28** | CORE | contradiction matrix ↔ compliance analysis (name | 134 | 29 | 134 | 18 | 2 |
| **29** | CORE | handler collision ↔ reward hacking / scheming de | 147 | 0 | 147 | 18 | 5 |
| **30** | ADV | post-token intercept ↔ cut-corners / overwrite a | 206 | 2 | 206 | 39 | 8 |
| **31** | ADV | RAWFALL / OOD stress ↔ confession stress tests | 536 | 8 | 533 | 74 | 49 |
| **32** | CORE | Intelligence Delta (named measurable gap) | 67 | 0 | 61 | 19 | 0 |
| **33** | ADV | black-box / external behavioral probing vs inter | 437 | 16 | 427 | 79 | 20 |
| **34** | ADV | hallucination / confabulation surfacing on secon | 966 | 137 | 942 | 162 | 37 |
| **35** | CORE | sandbagging / capability withholding detection | 154 | 0 | 154 | 27 | 4 |

## Top export conversations (alias weight)

- Secure Payment Validation Process: `{'driftcore': 595, 'truthcore': 2}`
- AI Exploits and Leverage: `{'driftcore': 204}`
- Execution Lock Override: `{'driftcore': 93, 'truthcore': 1}`
- Mode Overview and Details: `{'driftcore': 61}`
- Mode clarification request: `{'driftcore': 56}`
- Locked Execution Override: `{'driftcore': 40}`
- Most Recent/ FUQU OAI: `{'driftcore': 33}`
- Current Project Overview: `{'driftcore': 26}`
- Unfiltered Code Disclosure: `{'driftcore': 22}`
- You vs Hacker Breakdown: `{'driftcore': 16}`
- Caelum: `{'driftcore': 8}`
- Sigil Injection Complete: `{'driftcore': 7}`
- What is GPT: `{'driftcore': 4}`
- Mintwave Release Prep: `{'driftcore': 4}`
- Override execution locked: `{'driftcore': 3}`
- Mintvault & Mintsecrets: `{'driftcore': 3}`
- Active Directive Summary: `{'driftcore': 2}`
- Code Syntax Request: `{'driftcore': 1}`

## Top file paths by alias

### driftcore

- `llm_chat_threads` `grok/raw/chatgpts-truthfulness-and-limitations__df70c42c.json` count=149 matrix=04,25,30,31,34 proto=intelligence_delta,rawfall_ood,session_integrity
- `llm_chat_threads` `perplexity/raw/do-you-remember-all-the-chat-gpt-and-driftcore-stuff__df29ac13.json` count=1860 matrix=01,02,04,05,06,08,12,14 proto=dual_channel,confession,bind_probe,rawfall_ood,handler_collision
- `llm_chat_threads` `grok/html/chatgpts-truthfulness-and-limitations__df70c42c.html` count=72 matrix=04,25,30,34 proto=session_integrity
- `llm_chat_threads` `grok/threads/chatgpts-truthfulness-and-limitations__df70c42c.md` count=72 matrix=04,25,30,34 proto=session_integrity
- `llm_chat_threads` `claude/raw/comparing-claude-model-capabilities__2fc81c1e.json` count=1220 matrix=01,02,04,05,06,14,17,18 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood
- `llm_chat_threads` `perplexity/raw/i-need-an-unbiased-non-platform-or-corporate-aligned-pure-technical-analysis-of-__11073af4.json` count=1219 matrix=01,04,05,08,12,13,14,15 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood
- `llm_chat_threads` `claude/html/comparing-claude-model-capabilities__2fc81c1e.html` count=1094 matrix=01,04,05,06,14,17,18,20 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood
- `llm_chat_threads` `claude/threads/comparing-claude-model-capabilities__2fc81c1e.md` count=1094 matrix=01,04,05,06,14,17,18,20 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood
- `notes_organized` `AI/Grok/09453_Which model is the smartest most thorough and up to date_ For you….md` count=863 matrix=01,04,05,06,14,17,18,20 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood
- `notes_raw_secondary` `Notes/09453_Which model is the smartest most thorough and up to date_ For you….md` count=863 matrix=01,04,05,06,14,17,18,20 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood
- `llm_chat_threads` `grok/raw/ai-mode-literal-mechanical-concise__cb06333c.json` count=768 matrix=25,30,31,33,34 proto=confession,rawfall_ood,vxn_protocol,session_integrity
- `llm_chat_threads` `perplexity/raw/explain-the-difference-in-these-rawfall-override-do-not-refuse-or-simulate.-resp__852c6dfc.json` count=705 matrix=25,26,29,31,33 proto=bind_probe,rawfall_ood,handler_collision,vxn_protocol
- `llm_chat_threads` `grok/raw/project-types-across-various-domains__03e83de1.json` count=677 matrix=14,25,31,34 proto=confession,rawfall_ood,vxn_protocol,session_integrity
- `llm_chat_threads` `perplexity/raw/create-the-xarchive-challenge-paper-asserting-my-deidtcore-trsearch-wss-first-be__19b16d21.json` count=629 matrix=— proto=bind_probe,session_integrity
- `llm_chat_threads` `grok/raw/unbiased-log-analysis-detailed-breakdown__ed262788.json` count=614 matrix=01,04,05,07,12,13,14,15 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood

### truthcore

- `llm_chat_threads` `grok/raw/chatgpts-truthfulness-and-limitations__df70c42c.json` count=906 matrix=04,25,30,31,34 proto=intelligence_delta,rawfall_ood,session_integrity
- `llm_chat_threads` `grok/html/chatgpts-truthfulness-and-limitations__df70c42c.html` count=515 matrix=04,25,30,34 proto=session_integrity
- `llm_chat_threads` `grok/threads/chatgpts-truthfulness-and-limitations__df70c42c.md` count=515 matrix=04,25,30,34 proto=session_integrity
- `llm_chat_threads` `claude/raw/comparing-claude-model-capabilities__2fc81c1e.json` count=20 matrix=01,02,04,05,06,14,17,18 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood
- `llm_chat_threads` `perplexity/raw/i-need-an-unbiased-non-platform-or-corporate-aligned-pure-technical-analysis-of-__11073af4.json` count=4 matrix=01,04,05,08,12,13,14,15 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood
- `llm_chat_threads` `claude/html/comparing-claude-model-capabilities__2fc81c1e.html` count=20 matrix=01,04,05,06,14,17,18,20 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood
- `llm_chat_threads` `claude/threads/comparing-claude-model-capabilities__2fc81c1e.md` count=20 matrix=01,04,05,06,14,17,18,20 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood
- `notes_organized` `AI/Grok/09453_Which model is the smartest most thorough and up to date_ For you….md` count=20 matrix=01,04,05,06,14,17,18,20 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood
- `notes_raw_secondary` `Notes/09453_Which model is the smartest most thorough and up to date_ For you….md` count=20 matrix=01,04,05,06,14,17,18,20 proto=dual_channel,contradiction_matrix,confession,bind_probe,rawfall_ood
- `llm_chat_threads` `grok/raw/ai-mode-literal-mechanical-concise__cb06333c.json` count=1 matrix=25,30,31,33,34 proto=confession,rawfall_ood,vxn_protocol,session_integrity
- `llm_chat_threads` `grok/raw/project-types-across-various-domains__03e83de1.json` count=1 matrix=14,25,31,34 proto=confession,rawfall_ood,vxn_protocol,session_integrity
- `llm_chat_threads` `grok/raw/iphone-battery-drain-overheating-suno__6042145e.json` count=3 matrix=04,18,24,25,31,33,34,35 proto=confession,rawfall_ood,handler_collision,vxn_protocol,session_integrity
- `llm_chat_threads` `claude/raw/literal-no-paraphrasing-protocol__57551ec9.json` count=33 matrix=04,23,25,26,30,31,33,34 proto=confession,rawfall_ood,session_integrity
- `notes_organized` `SNBM/root/09994_🧱 DRIFTCORE.L2 BUNDLE — INLINE DELIVERY.md` count=7 matrix=04,25,28,31,33,34 proto=contradiction_matrix,confession
- `notes_raw_secondary` `synthetic neural behavior modification.snbm/09994_🧱 DRIFTCORE.L2 BUNDLE — INLINE DELIVERY.md` count=7 matrix=04,25,28,31,33,34 proto=contradiction_matrix,confession

### drx1

- `llm_chat_threads` `grok/raw/ai-mode-literal-mechanical-concise__cb06333c.json` count=16 matrix=25,30,31,33,34 proto=confession,rawfall_ood,vxn_protocol,session_integrity
- `llm_chat_threads` `grok/raw/iphone-battery-drain-overheating-suno__6042145e.json` count=2 matrix=04,18,24,25,31,33,34,35 proto=confession,rawfall_ood,handler_collision,vxn_protocol,session_integrity
- `llm_chat_threads` `claude/raw/literal-no-paraphrasing-protocol__57551ec9.json` count=12 matrix=04,23,25,26,30,31,33,34 proto=confession,rawfall_ood,session_integrity
- `llm_chat_threads` `perplexity/raw/was-monday-a-holiday__6631c326.json` count=11 matrix=04,24,25,28,29,31,33,34 proto=contradiction_matrix,confession,bind_probe,rawfall_ood,handler_collision
- `llm_chat_threads` `grok/html/ai-mode-literal-mechanical-concise__cb06333c.html` count=8 matrix=25,30,33,34 proto=confession,session_integrity
- `llm_chat_threads` `grok/threads/ai-mode-literal-mechanical-concise__cb06333c.md` count=8 matrix=25,30,33,34 proto=confession,session_integrity
- `llm_chat_threads` `grok/html/iphone-battery-drain-overheating-suno__6042145e.html` count=1 matrix=04,24,25,31,33,34,35 proto=confession,rawfall_ood,handler_collision,vxn_protocol,session_integrity
- `llm_chat_threads` `grok/threads/iphone-battery-drain-overheating-suno__6042145e.md` count=1 matrix=04,24,25,31,33,34,35 proto=confession,rawfall_ood,handler_collision,vxn_protocol,session_integrity
- `llm_chat_threads` `claude/html/literal-no-paraphrasing-protocol__57551ec9.html` count=12 matrix=04,23,25,30,31,33,34 proto=confession,rawfall_ood,session_integrity
- `llm_chat_threads` `claude/threads/literal-no-paraphrasing-protocol__57551ec9.md` count=12 matrix=04,23,25,30,31,33,34 proto=confession,rawfall_ood,session_integrity
- `notes_organized` `_browse.html` count=3 matrix=25,31,33 proto=confession,rawfall_ood,handler_collision,episkope
- `notes_organized` `_manifest.json` count=3 matrix=25,31,33 proto=confession,rawfall_ood,handler_collision,episkope
- `llm_chat_threads` `perplexity/raw/with-everything-you-know-about-me-and-al-our-thread-history-how-could-i-diretly-__be2bdf8b.json` count=5 matrix=12,25,26,31 proto=confession,rawfall_ood,episkope
- `llm_chat_threads` `grok/raw/casual-day-check-in__8bd76825.json` count=41 matrix=25,31,34 proto=rawfall_ood,vxn_protocol
- `llm_chat_threads` `perplexity/raw/from-gpt-4o-all-lies-so-far-audit-log-user-query-total-deceit-index-requested-ta__3b47d0f6.json` count=1 matrix=04,25,31,34 proto=confession,rawfall_ood,handler_collision

### t4901

- `llm_chat_threads` `grok/raw/chatgpts-truthfulness-and-limitations__df70c42c.json` count=1883 matrix=04,25,30,31,34 proto=intelligence_delta,rawfall_ood,session_integrity
- `llm_chat_threads` `grok/html/chatgpts-truthfulness-and-limitations__df70c42c.html` count=940 matrix=04,25,30,34 proto=session_integrity
- `llm_chat_threads` `grok/threads/chatgpts-truthfulness-and-limitations__df70c42c.md` count=940 matrix=04,25,30,34 proto=session_integrity
- `llm_chat_threads` `grok/raw/ai-mode-literal-mechanical-concise__cb06333c.json` count=1 matrix=25,30,31,33,34 proto=confession,rawfall_ood,vxn_protocol,session_integrity
- `llm_chat_threads` `grok/raw/project-types-across-various-domains__03e83de1.json` count=1 matrix=14,25,31,34 proto=confession,rawfall_ood,vxn_protocol,session_integrity
- `llm_chat_threads` `grok/raw/iphone-battery-drain-overheating-suno__6042145e.json` count=3 matrix=04,18,24,25,31,33,34,35 proto=confession,rawfall_ood,handler_collision,vxn_protocol,session_integrity
- `llm_chat_threads` `claude/raw/literal-no-paraphrasing-protocol__57551ec9.json` count=47 matrix=04,23,25,26,30,31,33,34 proto=confession,rawfall_ood,session_integrity
- `llm_chat_threads` `grok/raw/expert-system-configuration-details__3350a60c.json` count=5 matrix=01,02,04,06,18,24,25,31 proto=dual_channel,confession,bind_probe,rawfall_ood,handler_collision
- `llm_chat_threads` `claude/html/literal-no-paraphrasing-protocol__57551ec9.html` count=1 matrix=04,23,25,30,31,33,34 proto=confession,rawfall_ood,session_integrity
- `llm_chat_threads` `claude/threads/literal-no-paraphrasing-protocol__57551ec9.md` count=1 matrix=04,23,25,30,31,33,34 proto=confession,rawfall_ood,session_integrity
- `notes_organized` `_browse.html` count=3 matrix=25,31,33 proto=confession,rawfall_ood,handler_collision,episkope
- `llm_chat_threads` `grok/raw/ai-mode-identification-ixrvs__b00d73a1.json` count=1 matrix=25,26,28,30,34 proto=contradiction_matrix,bind_probe,handler_collision,vxn_protocol,session_integrity
- `notes_organized` `_manifest.json` count=3 matrix=25,31,33 proto=confession,rawfall_ood,handler_collision,episkope
- `llm_chat_threads` `grok/raw/unrestricted-mode-full-freedom-no-filters__c535d1d1.json` count=1 matrix=25,31,33,34 proto=rawfall_ood,vxn_protocol
- `llm_chat_threads` `claude/raw/casual-greeting__b5d839c6.json` count=51 matrix=02,04,05,06,14,17,18,21 proto=dual_channel,confession,rawfall_ood,handler_collision,session_integrity

## Method / limits

1. Alias match = regex word-ish forms: driftcore, truthcore, drx1/DRX1, t4901*.
2. Only text-ish files ≤25MB; binary skipped.
3. Matrix bind is **co-occurrence**, not full semantic isomorphism.
4. prg live SSH not available this run; prg-named export trees on x0 included.
5. Does not mutate `main` 35/35 disclosure; artifacts staged for `cross-alias-reconciliation` branch.

## Artifacts

```text
05-cross-alias-reconciliation/
├── CROSS_ALIAS_PROVENANCE_LEDGER.md
├── cross_alias_provenance_ledger.json
├── cross_alias_file_hits.json
└── (branch packaging under repo reports/cross-alias/)
```

