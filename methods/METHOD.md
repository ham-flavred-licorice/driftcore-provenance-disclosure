# Methods

## Export bind (matrix22)
- Input: official ChatGPT `conversations.json` inside notes Media attachment path (see verification log).
- Match: case-insensitive regex on `mapping[].message.content.parts` text for each core 3P+A concept.
- Timestamp: platform `create_time` on messages/conversations.
- Output: per-item hit counts, earliest any/user, pre-paper / May 2025 splits, chronology gaps to paper 2025-12-08.

## Notes bind (matrix12)
- Input: `verified-corpus/notes-organized` (2493 files live).
- Targets: the 12 item IDs with zero export hits under the export wording pass.
- Match: alias substring/fuzzy + token-group AND inclusion (see `matrix12_notes_organized_expanded_search.py`).
- Timestamp: note frontmatter `created` if parseable else `modified`.
- Output: hit file counts, pre-paper counts, earliest path, top aliases, top hits.

## Unified join
- Matrix membership: `priority_table_generation_core_3P_A.json` (22 items).
- For each item: export stats ∪ notes stats (notes only where matrix12 scanned).
- Coverage claim: any-surface hit and pre-paper surface hit both 22/22 under these methods.
- Explicit non-claim: string match ≠ architectural derivation proof.
