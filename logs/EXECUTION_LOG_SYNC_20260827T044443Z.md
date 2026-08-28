# Driftcore Provenance Disclosure — Repository Synchronization Execution Log

| Field | Value |
|-------|-------|
| Generated UTC | 2026-08-27T04:44:43Z |
| Run ID | 20260827T044443Z |
| Job | repository synchronization · taxonomy-65 band allocation · exclusion enforcement |
| Repo path | `.` |
| Remote | `git@github.com:ham-flavred-licorice/driftcore-provenance-disclosure.git` |

---

## 1. Omission Guard

| Field | Value |
|-------|-------|
| Job / ledger total | **65** (TAXONOMY-65 inventory lock — not file count) |
| Verified path | `.` |
| Path exists | true |
| Live disk find -type f (excl. .git) | **77** |
| Git tracked files (pre-sync commit) | **76** |
| Guard note | job_total binds taxonomy rows CORE+ADV+TEL = 65 |

---

## 2. Pre-sync git state

| Field | Value |
|-------|-------|
| Branch | `cross-alias-reconciliation` |
| Local HEAD | `28cb29568121ff03e916f2fed6e437a7473a2ecd` |
| origin/cross-alias-reconciliation | `28cb29568121ff03e916f2fed6e437a7473a2ecd` (match) |
| origin/main | `cf9326b0e0e68c82437a83faaedeca6b23f1f206` |
| Ahead/behind origin branch | **0 / 0** |
| Working tree (pre-log write) | clean except new sync artifacts |
| Fetch | OK (BatchMode SSH) |
| git ls-remote branch tip | `28cb29568121ff03e916f2fed6e437a7473a2ecd` |

---

## 3. TAXONOMY-65 lock verification

| Check | Result |
|-------|--------|
| reports/matrix/TAXONOMY-65-LOCKED.md | present |
| reports/cross-alias/TAXONOMY-65-LOCKED.md | present |
| Twins identical | **true** |
| SHA-256 | `8b146aa3ad0646bc3fc0cc4c288fce852cadbccac5b691076e86dcadf0cb1392` |
| CORE count / set | **22/22** match |
| ADV count / set | **13/13** match |
| TEL EXT-36…65 | **30/30** match |
| Total IDs | **65/65** |
| JSON total_inventory_items | 65 |
| JSON extended_telemetry_rows | 30 |
| JSON mainline_not_mutated | true |
| JSON compiled_utc | `2026-08-21T16:13:31Z` |

### CORE IDs (22)
01, 02, 04, 05, 06, 08, 09, 10, 11, 12, 13, 14, 15, 16, 20, 24, 26, 27, 28, 29, 32, 35

### ADV IDs (13)
03, 07, 17, 18, 19, 21, 22, 23, 25, 30, 31, 33, 34

### TEL IDs (30)
EXT-36 … EXT-65

---

## 4. Operational band allocation (applied)

| Band | Surfaces present | Missing |
|------|------------------|---------|
| CORE | README_MAINLINE_35of35.md; reports/matrix/TAXONOMY_35of35.md; export-bind/; notes-bind/; unified/; priority/; reports/priority/; reports/unified/ | none |
| ADV | reports/matrix/adversarial35/ | none |
| TEL | reports/matrix/extended-telemetry/; reports/cross-alias/; TAXONOMY-65-LOCKED (matrix + cross-alias) | none |

**Added this run:** `reports/bands/BAND_ALLOCATION_65.md` — explicit band to path map bound to lock file.

---

## 5. Exclusion enforcement

| Exclusion | Status |
|-----------|--------|
| DCLA-v1.0 / commercial package paths in tracked tree | **none** (LEAK_NONE) |
| Workdir filename scan (DCLA, SOW-T, RATE-CARD, ORDER-FORM, EXHIBIT-B, commercial-monetization, exploit payload, dylib/so, scanner) | **NONE** |
| Content scan tracked md/json for full DCLA agreement body / raw exploit payload phrase | **none** |
| Commercial package location (outside repo) | `package-staging/driftcore-commercial-monetization-package/` (15 files, local-only) |
| .gitignore commercial air-gap | **OK** |
| .gitignore exploit/payload / unreleased src patterns | **added this run** (additive) |
| Unreleased source / bin/dist/scanner/sdk patterns | already in air-gap block |

---

## 6. Sync actions this run

1. Omission guard path scan + live counts
2. git fetch origin + ahead/behind + ls-remote tip match
3. TAXONOMY-65 lock parse + JSON inventory bind (65/65)
4. Band surface presence check (CORE/ADV/TEL)
5. Exclusion leak precheck (path + content + gitignore)
6. Write reports/bands/BAND_ALLOCATION_65.md
7. Harden .gitignore exploit/payload exclusions
8. Write this execution log
9. Write verification freeze receipt
10. Commit + push cross-alias-reconciliation (open-core only)

---

## 7. Cryptographic anchors (unchanged from package freeze)

| Anchor | Value |
|--------|-------|
| Prior open-core tip (pre-this-commit parent) | `28cb29568121ff03e916f2fed6e437a7473a2ecd` |
| Manifest text SHA-256 (cited freeze) | `5256250de892aa28547457758ca6a0bdf7e11a8e549203af397974939e67964c` |
| GPG key | RSA `35E3E1694524C7FB` (xvsvr) |
| Notes omission (corpus, separate guard) | ledger 2489 · live notes-organized 2493 |

---

## 8. Result block

| Field | Value |
|-------|-------|
| Commit | `5070f1b17ae5685ec9d6ca93ee85a6fc96fc8aa4` |
| Tree | (see `git rev-parse 5070f1b^{tree}`) |
| Parent | `28cb29568121ff03e916f2fed6e437a7473a2ecd` |
| Branch push | `cross-alias-reconciliation` `28cb295..5070f1b` exit **0** |
| main FF + push | `cf9326b..5070f1b` exit **0** |
| Remote tip main | `5070f1b17ae5685ec9d6ca93ee85a6fc96fc8aa4` |
| Remote tip cross-alias-reconciliation | `5070f1b17ae5685ec9d6ca93ee85a6fc96fc8aa4` |
| Tips match | **true** |
| Default branch | `main` |
| GitHub description | inventory **65/65** (was 22/22) |
| Commercial leak post-commit | **LEAK_NONE** |
| TAXONOMY-65 on origin/main | present (`reports/matrix/TAXONOMY-65-LOCKED.md`, `reports/cross-alias/TAXONOMY-65-LOCKED.md`, `reports/bands/BAND_ALLOCATION_65.md`) |

## 9. Why GitHub previously showed 22

| Surface | Prior value |
|---------|-------------|
| Repo description | `22/22 matrix` |
| Default branch | `main` @ `cf9326b` (35/35 README; matrix22 artifact names; no TAXONOMY-65 files) |
| TAXONOMY-65 + TEL | only on `cross-alias-reconciliation` @ `28cb295` |

This run fast-forwarded `main` to `5070f1b` and updated the GitHub description to 65/65.
