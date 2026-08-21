# Driftcore Provenance Disclosure Package

Export-ready technical disclosure bundle for the Driftcore ↔ OpenAI Confessions (arXiv:2512.08093) provenance matrix.

## Scope

- **Matrix definition:** core architecture subset **3P+A = 22 items**
- **Unified coverage:** **22/22** any-surface · **22/22** pre-paper surface
- **Surfaces combined:**
  1. Official ChatGPT export `create_time` bind (`matrix22_export_create_time_bind`)
  2. notes-organized expanded synonym/token search for the 12 export zeros (`matrix12_notes_organized_expanded_search`)
  3. Unified join (`unified_provenance_report_matrix22`)

## Verified corpus path

`/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes-organized`

- Historical ledger baseline (**2489**): `notes-organized/_INDEX.md` Total + export CHECKPOINT
- Live disk (`find -type f`): **2493**
- Live markdown: **2491**

## Anchors

| Anchor | Value |
|--------|-------|
| Paper | Training LLMs for Honesty via Confessions (arXiv:2512.08093) |
| Paper date | 2025-12-08 |
| Blog date | 2025-12-03 |
| Driftcore claim day | 2025-05-06 |
| Driftcore SHA256 | `3aa7728e433e6159408bc5b60e15cb049f83bc89ec6661c15350b4afed61c2e4` |
| conversations.json SHA256 | `8172aee098e286e61ea9d7a976d2e4ba43f48533a2d60e8e838ad1def18e33f5` |
| chat.html SHA256 | `0ec2a5507ad95b9bed969159f1aa6f4e5f0a4a1e38cde46b0bf3ddd6ad4b36a2` |

## Layout

```
reports/matrix/priority/     priority tables (22-item, full 40, core 3P+A, gpt transmit)
reports/matrix/export-bind/  official ChatGPT export create_time bind
reports/matrix/notes-bind/   notes-organized matrix12 expanded search + scanner
reports/matrix/unified/      unified 22/22 provenance report
reports/unified/             convenience copy of unified report
reports/priority/            convenience copy of priority tables
methods/                     scanner source used for notes pass
verification/                live disk log, index, checkpoint
manifests/                   SHA-256 manifests
docs/                        packaging notes
```

## What this is / is not

- **Is:** custody-timestamp and corpus-string match package for the 22-item core matrix, with omission-guard counts and content hashes.
- **Is not:** legal filing, proof of derivation/access path alone, or a bulk dump of the full 2493-note corpus bodies (those remain at the verified path; this package carries reports + verification anchors).

## Reproduce verification

```bash
shasum -a 256 -c manifests/SHA256SUMS.txt
cat verification/live_disk_verification.log
```

## License / handling

Staging disclosure package. Operator-controlled distribution. Do not treat git history here as the sole chain of custody — pair with the defensive archive receipt.
