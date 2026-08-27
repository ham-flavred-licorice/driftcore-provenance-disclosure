# TAXONOMY-65 Operational Band Allocation

**Compiled UTC:** 2026-08-27T04:44:00Z  
**Source lock:** `reports/matrix/TAXONOMY-65-LOCKED.md` · `reports/cross-alias/TAXONOMY-65-LOCKED.md`  
**SHA-256 (twins identical):** `8b146aa3ad0646bc3fc0cc4c288fce852cadbccac5b691076e86dcadf0cb1392`  
**Inventory:** 65/65 (CORE 22 + ADV 13 + TEL 30)

## Band to repository surfaces

| Band | Code | Count | IDs | Designated paths |
|------|------|------:|-----|------------------|
| Core Architecture | CORE | 22 | 01,02,04,05,06,08,09,10,11,12,13,14,15,16,20,24,26,27,28,29,32,35 | `README_MAINLINE_35of35.md`; `reports/matrix/TAXONOMY_35of35.md`; `reports/matrix/export-bind/`; `reports/matrix/notes-bind/`; `reports/matrix/unified/`; `reports/matrix/priority/`; `reports/priority/`; `reports/unified/` |
| Adversarial Edge-Cases and Stress-Test | ADV | 13 | 03,07,17,18,19,21,22,23,25,30,31,33,34 | `reports/matrix/adversarial35/` |
| Extended Telemetry Indices | TEL | 30 | EXT-36 … EXT-65 | `reports/matrix/extended-telemetry/`; `reports/cross-alias/`; `reports/matrix/TAXONOMY-65-LOCKED.md`; `reports/cross-alias/TAXONOMY-65-LOCKED.md` |

## JSON inventory bind

- Path: `reports/cross-alias/secondary_crawl_expanded_taxonomy.json`
- Twin under matrix: `reports/matrix/extended-telemetry/secondary_crawl_expanded_taxonomy.json`
- `total_inventory_items`: 65
- `matrix_mainline_count`: 35
- `telemetry_ext_count`: 30
- `mainline_not_mutated`: true
- `extended_telemetry_rows`: 30
- Nomenclature canonical: confession · probe_bind

## Exclusions (not allocated / not staged)

- DCLA-v1.0 legal agreements and commercial package (`driftcore-commercial-monetization-package`, `01-DCLA`, `02-SOW`, `03-DSAT-IB`, `05-schedules`)
- Raw exploit payloads
- Unreleased source / scanner binaries / ingest SDKs
- Enforced via `.gitignore` commercial air-gap plus exploit/payload patterns

## Classification rules (from TAXONOMY-65-LOCKED)

1. CORE: 3P/A only where provenance package already classifies; commercial sale does not upgrade class.
2. ADV: 2P/B diagnostic adjacency unless elevation memo signed.
3. TEL: telemetry indices only; not auto-promoted to mainline 35 freeze.
4. EXT-37 probe_bind canonical; bind_probe legacy alias.
5. Multi-model failure logging = EXT-39 + EXT-41/42/64/65.
