# Nomenclature — confession, probe_bind

**Compiled (UTC):** `2026-08-21T16:13:31Z`  
**Branch:** `cross-alias-reconciliation`

## Canonical structural pair

| Token | Status |
|-------|--------|
| `confession` | **canonical** |
| `probe_bind` | **canonical** |

## Legacy / corrected forms

| Form | Maps to |
|------|---------|
| `bind_probe` | `probe_bind` |
| confession binding (generic) | `confession` (+ pair with `probe_bind`) |
| `confession_binding` / `confession.bind` | `confession` |
| `probe.bind` | `probe_bind` |

## Secondary crawl counts (prefilter)

- confession: files=794 hits=26041
- probe_bind (literal): files=0 hits=0
- bind_probe (legacy): files=0 hits=0

## Rule

Emit protocol maps as **confession** + **probe_bind**. Do not use fused generic “confession_binding” as the structural name.
