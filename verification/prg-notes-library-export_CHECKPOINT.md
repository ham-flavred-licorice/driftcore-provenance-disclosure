# CHECKPOINT — prg Apple Notes library export
Saved: 2026-08-17
Session context: Hermes on Mac (x0); source account prg via SSH loopback
Status: **paused — ready to continue**

## One-line state
Whole prg Notes library copied to Agent-Staging, made browsable, then **split** into `notes/<folder>/` one markdown file per note. Live prg Notes was **not** modified. Per-note split reflects **current** (post-reorg) folder links — not the pre-2026-06-25 layout.

---

## Primary paths (open these)

| What | Path |
|------|------|
| **This job root** | `/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/` |
| **Whole library container (1:1)** | `…/group.com.apple.notes/` (~814 MB, NoteStore.sqlite) |
| **Split notes (individual files)** | `…/notes/<Folder>/…/<note_pk>_<title>.md` (~42 MB, **2489** files) |
| **Split browse UI** | `…/notes/_browse.html` |
| **Split index** | `…/notes/_INDEX.md` |
| **Split manifest** | `…/notes/_manifest.json` |
| **Pre-split library browse** | `…/browse/index.html` |
| **This checkpoint** | `…/CHECKPOINT.md` |
| **README** | `…/README.md` |

### Related (folder maps from reorg incident — not the split export)

`/Users/x0/Desktop/Agent-Staging/prg-notes-folder-maps/`

- `FOLDER-LAYOUT-REPORT.md` — before vs after reorg (folder → **counts only**)
- `folder-counts-before-after.tsv`
- `apple-notes-folders-2026-06-25.tsv` — **pre-reorg** target map (**2422** notes, **198** folders)
- `notes-location-now.tsv` / `where-are-my-notes-2026-06-25.md` — post-reorg piles

### Older staging copies (superseded for canonical export by this job)

- `~/Desktop/Agent-Staging/prg-notes-docs-1by1/group.com.apple.notes/` (~814 MB)
- `~/Desktop/Agent-Staging/prg-apple-notes-20260718-190948/group.com.apple.notes/`

---

## What was completed

1. **Whole-unit export** of prg Notes container only (not iCloud Drive docs):
   - Source: `prg@127.0.0.1:Library/Group Containers/group.com.apple.notes/`
   - Dest: `prg-notes-library-export/group.com.apple.notes/`
   - rsync OK; ~1879 files; NoteStore.sqlite ~76 MB

2. **Browsable library index** (before split):
   - `browse/index.html`, `notes-by-folder.tsv`, `folder-counts.tsv`, `library-index.json`

3. **CEO ordered separation** — split into `notes/` with subfolders and individual note files:
   - **2489** `.md` files
   - **42** folder buckets (current DB)
   - Nested paths preserved (e.g. under `synthetic neural behavior modification.snbm/`)
   - Bodies from gzip+protobuf in `ZICNOTEDATA` (text extraction; not perfect rich-text/attachments)
   - ~2424 notes with body_chars > 50; ~10 empty; 0 locked
   - Dominant bucket: **`notes/Notes/` ~2248** (post-reorg pile)

4. **Not done / out of scope for this checkpoint**
   - No restore of Notes.app on prg
   - No Wi-Fi/iCloud changes
   - No remap to **pre-reorg** 198-folder layout inside the split tree
   - No per-note title→original-folder list (Desktop repair TSVs on prg were iCloud-dataless/timeout)
   - iCloud Drive documents grab still unfinished from earlier thread (separate from Notes)

---

## Critical facts for continue

### Notes are not 2400 loose files on disk in the live library
Live store = one container + `NoteStore.sqlite`. Split files are **exports** derived from that DB.

### Current split folders != pre-reorg layout
- **Pre-reorg map (Jun 25 inventory):** 2422 notes, 198 folders — e.g. Notes 481, *Claude* 129, *grok* 95, snbm 95, UAI_3.5 88, …
- **Post-reorg:** notes moved into WORKSPACE-prg / Archive-Inbox piles; many familiar folders drained to 0; totals still ~2423 (moved, not deleted) per incident writeups
- **This export's folders** follow **current** sqlite `ZFOLDER` links → most files land under `notes/Notes/`

### Rebuild Notes.app folders (commands already on machine — run as **prg**, Wi-Fi OFF)
Do **not** run unless CEO explicitly orders restore + names backup:

```bash
python3 /Users/Shared/notes_list_backups.py
bash /Users/Shared/prg-restore-notes-original-folders.sh
# or:
bash /Users/Shared/prg-restore-notes-from-backup.sh 'group.com.apple.notes.backup-20260625-0611'
# optional log reverse:
bash /Users/Shared/prg-put-notes-back-in-folders.sh
```

Then iCloud Notes OFF before Wi-Fi ON. Spot-check sidebar vs pre-map.

### LAW (still binding)
- No category-as-tree / no batch grab from vague "documents/icloud/continue"
- Whole-tree only with exact unit + entire/whole wording in **latest** message
- Separate/export only after explicit order (this split was explicitly ordered)
- Apple Notes DB: no bulk live moves/schema without immediate-turn approval
- Staging only for ordinary mutate; live prg originals read/copy only unless restore explicitly ordered

---

## Likely continue options (CEO picks; do not assume)

1. **Browse / search** the split tree or `_browse.html` as-is
2. **Re-export after** Notes.app folder restore (so `notes/<folder>/` matches old layout)
3. **Remap** split files using pre-reorg evidence if a per-note map/backup becomes readable
4. **Attachments/media** pass (current export is mainly text from note bodies)
5. **iCloud Drive documents** (separate job — was never finished; one-path or explicit whole-unit only)

---

## Verify when resuming

```bash
ls -la "/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/"
du -sh "/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes" \
      "/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/group.com.apple.notes"
find "/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes" -name '*.md' | wc -l
# expect ~2489 md files under notes/ (plus _INDEX.md)
open "/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes/_browse.html"
```

---

## Say this to resume (example)

"Continue from prg-notes-library-export CHECKPOINT"
and name the next act (browse-only / restore Notes on prg / re-split after restore / remap / attachments / something else).

Agent: re-read **this file** + LAW first; do not invent bulk scope from history.


---

## Update — notes-organized (resume continue)

Date: 2026-08-17

**Done:** Best-effort folder organization of all **2489** staged notes into:

`/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes-organized/`

- Original split **`notes/`** left intact
- Live prg Notes **not** touched
- **80** folders under 9 top-level groups (AI, Systems, SNBM, Projects, Creative, Tech, Life, Reference, Inbox)
- `notes-organized/_browse.html` for navigation
- 0 notes lost (pk set match)

**Still not done:** Notes.app restore on prg, true pre-reorg 198-folder remap (needs per-note map/backup), attachments pass.
