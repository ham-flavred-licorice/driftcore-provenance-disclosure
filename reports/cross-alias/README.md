# Cross-Alias Reconciliation (Driftcore / Truthcore / DRX1)

**Branch:** `cross-alias-reconciliation`  
**Does not replace** the mainline **35/35** taxonomy freeze on `main`.  
**Canonical name:** Driftcore  
**Confirmed aliases:** Truthcore, DRX1  
**Lineage markers:** t4901 / t4901.1  

## Omission Guard (locked)

| Field | Value |
|--------|--------|
| Historical ledger baseline | **2489** |
| Live disk `find -type f` | **2493** |
| Verified path | `/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes-organized` |

## Artifacts

- `CROSS_ALIAS_PROVENANCE_LEDGER.md` — human ledger
- `cross_alias_provenance_ledger.json` — machine ledger
- `cross_alias_file_hits.json` — per-file alias/protocol/matrix co-occurrence index

## Scope note

Crawl surfaces: `notes-organized`, secondary `notes/`, `llm-chat-threads/*` providers, package tree, official `conversations.json`. Live `prg` SSH DNS was unresolved this run; prg-named export mirrors on x0 were included.

## Secondary crawl (scale beyond 35)

**Compiled:** `2026-08-21T16:13:31Z`

- `SECONDARY_CRAWL_EXPANDED_TAXONOMY.md` / `.json` — EXT-36..EXT-65 telemetry indices
- `NOMENCLATURE_confession_probe_bind.md` — canonical **confession** + **probe_bind**
- `secondary_crawl_file_index.json` — file-level index (Grok stress, OpenRouter, aliases)
- `TAXONOMY_35_PLUS_EXTENDED.md` — uncapped inventory pointer (mainline 35 frozen)
- `CROSS_ALIAS_NOMENCLATURE_PATCH.md` — bind_probe → probe_bind canonicalization

Nomenclature correction: generic confession-binding → structural pair `confession`, `probe_bind` (legacy `bind_probe` aliased).

