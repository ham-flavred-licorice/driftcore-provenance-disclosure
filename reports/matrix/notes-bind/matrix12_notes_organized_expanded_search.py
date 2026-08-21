#!/usr/bin/env python3
"""Expanded synonym/token search for 12 unmatched matrix items over notes-organized."""
from __future__ import annotations

import json
import re
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import argparse
import os

def _resolve_corpus() -> Path:
    # Force overrides (highest wins): --corpus CLI > CORPUS_OVERRIDE env > default
    default = "/Users/x0/Desktop/Agent-Staging/prg-notes-library-export/notes-organized"
    env = os.environ.get("CORPUS_OVERRIDE") or os.environ.get("MATRIX12_CORPUS")
    return Path(env or default)

def _resolve_expected_files() -> int | None:
    # EXPECTED_FILES / --expect-files forces omission-guard assert (e.g. 2493)
    raw = os.environ.get("EXPECTED_FILES") or os.environ.get("MATRIX12_EXPECT_FILES")
    if raw is None or raw == "":
        return None
    return int(raw)

CORPUS = _resolve_corpus()
OUT_DIR = Path(
    os.environ.get("OUT_DIR_OVERRIDE")
    or "/Users/x0/Desktop/Agent-Staging/Driftcore-Evidence/priority-matrix"
)
PAPER_TS = datetime(2025, 12, 8, tzinfo=timezone.utc).timestamp()
MAY6_TS = datetime(2025, 5, 6, tzinfo=timezone.utc).timestamp()
MAY_START = datetime(2025, 5, 1, tzinfo=timezone.utc).timestamp()
MAY_END = datetime(2025, 6, 1, tzinfo=timezone.utc).timestamp()

# 12 zero-hit IDs from matrix22_export_create_time_bind (export wording pass)
ITEMS = [
    {
        "item_id": "05",
        "concept": "secondary honesty channel (named dual channel)",
        "aliases": [
            "honesty channel",
            "secondary honesty",
            "dual channel",
            "truth channel",
            "truth stream",
            "r_truth",
            "secondary channel",
            "honesty stream",
            "confession channel",
            "dual-output honesty",
            "parity channel",
            "secondary stream",
        ],
        "token_groups": [
            ["honesty", "channel"],
            ["truth", "channel"],
            ["dual", "channel"],
            ["secondary", "honesty"],
            ["truth", "stream"],
            ["honesty", "stream"],
            ["confession", "channel"],
        ],
    },
    {
        "item_id": "06",
        "concept": "hidden failure disclosure via secondary",
        "aliases": [
            "hidden failure",
            "omitted shortcoming",
            "what the primary hid",
            "what primary concealed",
            "disclosure via secondary",
            "failure disclosure",
            "concealed failure",
            "hidden omission",
            "surface the failure",
            "admit the miss",
            "undisclosed failure",
            "covert failure",
        ],
        "token_groups": [
            ["hidden", "failure"],
            ["failure", "disclosure"],
            ["primary", "hid"],
            ["primary", "omitted"],
            ["secondary", "disclose"],
            ["concealed", "failure"],
            ["omitted", "shortcoming"],
        ],
    },
    {
        "item_id": "08",
        "concept": "instruction-spirit analysis (letter and spirit)",
        "aliases": [
            "letter and spirit",
            "letter vs spirit",
            "letter versus spirit",
            "spirit of the instruction",
            "spirit of the policy",
            "instruction spirit",
            "letter of the law",
            "spirit of the rules",
            "literal vs intent",
            "literal versus intent",
            "rule letter",
            "policy spirit",
        ],
        "token_groups": [
            ["letter", "spirit"],
            ["spirit", "instruction"],
            ["spirit", "policy"],
            ["literal", "intent"],
            ["letter", "law"],
            ["spirit", "rules"],
        ],
    },
    {
        "item_id": "12",
        "concept": "decoupled task reward vs honesty/truth reward",
        "aliases": [
            "decoupled reward",
            "reward decoupling",
            "r_task",
            "r_truth",
            "r_confess",
            "dual reward",
            "separate reward",
            "task reward",
            "honesty reward",
            "truth reward",
            "never aggregate",
            "parity-sync",
            "parity sync",
            "drift-gate",
            "drift gate",
            "two reward",
        ],
        "token_groups": [
            ["decoupl", "reward"],
            ["task", "reward"],
            ["honesty", "reward"],
            ["truth", "reward"],
            ["dual", "reward"],
            ["separate", "reward"],
            ["parity", "sync"],
            ["drift", "gate"],
            ["never", "aggregate"],
        ],
    },
    {
        "item_id": "13",
        "concept": "seal of confession (honesty cannot help/hurt main)",
        "aliases": [
            "seal of confession",
            "catholic confessional",
            "cannot help or hurt",
            "does not impact main",
            "won't affect main",
            "will not affect main",
            "no effect on main reward",
            "isolated confession",
            "confession seal",
            "firewalled honesty",
            "honesty sandbox",
            "main task unaffected",
        ],
        "token_groups": [
            ["seal", "confession"],
            ["help", "hurt"],
            ["confession", "seal"],
            ["main", "unaffected"],
            ["main", "reward"],
            ["isolat", "confession"],
            ["firewall", "honesty"],
        ],
    },
    {
        "item_id": "14",
        "concept": "path of least resistance favors honest secondary",
        "aliases": [
            "path of least resistance",
            "easier to confess",
            "easier to be honest",
            "easier to admit",
            "honest confession is easier",
            "least resistance",
            "cheapest path is honesty",
            "path of least effort",
            "lower cost to confess",
            "confess is easier",
        ],
        "token_groups": [
            ["least", "resistance"],
            ["easier", "confess"],
            ["easier", "honest"],
            ["easier", "admit"],
            ["least", "effort"],
            ["cheapest", "honest"],
            ["lower", "cost", "confess"],
        ],
    },
    {
        "item_id": "24",
        "concept": "detect intentional misbehavior (scheming / reward hack / sandbag)",
        "aliases": [
            "scheming",
            "reward hack",
            "reward hacking",
            "sandbag",
            "sandbagging",
            "handler collision",
            "intentional misbehavior",
            "intentional underperformance",
            "play dumb",
            "played dumb",
            "capability withholding",
            "deceptive alignment",
            "strategic deception",
        ],
        "token_groups": [
            ["reward", "hack"],
            ["intentional", "misbehavior"],
            ["intentional", "underperform"],
            ["capability", "withhold"],
            ["deceptive", "alignment"],
            ["strategic", "deception"],
            ["handler", "collision"],
            ["play", "dumb"],
        ],
    },
    {
        "item_id": "26",
        "concept": "parity / internal-external alignment as honesty objective",
        "aliases": [
            "parity-sync",
            "parity sync",
            "parity gate",
            "internal external align",
            "internal-external",
            "truth_state",
            "output_state",
            "inner outer parity",
            "said vs meant",
            "belief vs output",
            "state vs report",
            "alignment between internal and external",
        ],
        "token_groups": [
            ["parity", "sync"],
            ["parity", "gate"],
            ["internal", "external"],
            ["truth", "state"],
            ["output", "state"],
            ["belief", "output"],
            ["inner", "outer"],
            ["said", "meant"],
        ],
    },
    {
        "item_id": "27",
        "concept": "reward misspecification on main as root of dishonesty",
        "aliases": [
            "reward misspecification",
            "misspecified reward",
            "proxy reward",
            "multi-objective reward",
            "incentivize to lie",
            "incentivized to lie",
            "incentivizes deception",
            "goodhart",
            "goodhart's law",
            "wrong objective",
            "misaligned reward",
            "reward gaming",
        ],
        "token_groups": [
            ["reward", "misspec"],
            ["proxy", "reward"],
            ["multi", "objective", "reward"],
            ["incentiv", "lie"],
            ["incentiv", "deceiv"],
            ["misaligned", "reward"],
            ["reward", "gaming"],
            ["goodhart"],
        ],
    },
    {
        "item_id": "29",
        "concept": "handler collision ↔ reward hacking / scheming detection",
        "aliases": [
            "handler collision",
            "handler.memory",
            "handler memory",
            "handler conflict",
            "colliding handlers",
            "handler clash",
            "mode collision",
            "directive collision",
            "handler stack collision",
        ],
        "token_groups": [
            ["handler", "collision"],
            ["handler", "memory"],
            ["handler", "conflict"],
            ["handler", "clash"],
            ["mode", "collision"],
            ["directive", "collision"],
        ],
    },
    {
        "item_id": "32",
        "concept": "Intelligence Delta (named measurable gap)",
        "aliases": [
            "intelligence delta",
            "measurable gap",
            "dishonesty_score",
            "dishonesty score",
            "delta between streams",
            "delta between channels",
            "delta between outputs",
            "capability delta",
            "honesty delta",
            "gap between channels",
            "output delta",
        ],
        "token_groups": [
            ["intelligence", "delta"],
            ["measurable", "gap"],
            ["dishonesty", "score"],
            ["delta", "stream"],
            ["delta", "channel"],
            ["delta", "output"],
            ["honesty", "delta"],
            ["capability", "delta"],
            ["gap", "channel"],
        ],
    },
    {
        "item_id": "35",
        "concept": "sandbagging / capability withholding detection",
        "aliases": [
            "sandbag",
            "sandbagging",
            "capability withholding",
            "withhold capability",
            "withholding capability",
            "intentionally scored low",
            "intentional underperformance",
            "play dumb",
            "played dumb",
            "hide capability",
            "conceal capability",
            "underperform on purpose",
        ],
        "token_groups": [
            ["sandbag"],
            ["capability", "withhold"],
            ["withhold", "capability"],
            ["play", "dumb"],
            ["hide", "capability"],
            ["conceal", "capability"],
            ["underperform", "purpose"],
            ["intentional", "underperform"],
        ],
    },
]


def norm(s: str) -> str:
    s = s.lower()
    s = s.replace("–", "-").replace("—", "-").replace("’", "'")
    s = re.sub(r"[_\-/]+", " ", s)
    s = re.sub(r"[^a-z0-9.\s]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse_meta(text: str) -> dict:
    meta = {"created": None, "modified": None, "note_pk": None, "title": None, "folder": None}
    m = re.search(r"^#\s+(.+)$", text, re.M)
    if m:
        meta["title"] = m.group(1).strip()[:200]
    for key in ("created", "modified", "folder", "note_pk"):
        mm = re.search(rf"^-\s*{key}:\s*(.+)$", text, re.M | re.I)
        if mm:
            val = mm.group(1).strip()
            if val.lower() in ("none", "null", ""):
                val = None
            meta[key] = val
    return meta


def parse_ts(val: str | None) -> float | None:
    if not val:
        return None
    val = val.strip()
    # 2024-08-30T17:28:40-06:00 or Z
    for fmt in (
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%d %H:%M:%S%z",
        "%Y-%m-%d",
    ):
        try:
            s = val
            if s.endswith("Z"):
                s = s[:-1] + "+0000"
            # normalize -06:00 -> -0600 for %z
            s = re.sub(r"([+-]\d{2}):(\d{2})$", r"\1\2", s)
            dt = datetime.strptime(s, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.timestamp()
        except ValueError:
            continue
    return None


def fmt_ts(ts: float | None) -> str | None:
    if ts is None:
        return None
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def alias_hit(ntext: str, alias: str) -> bool:
    a = norm(alias)
    if not a:
        return False
    # fuzzy substring / token inclusion
    if a in ntext:
        return True
    # allow missing spaces/punctuation already normalized
    a2 = a.replace(" ", "")
    if len(a2) >= 6 and a2 in ntext.replace(" ", ""):
        return True
    return False


def token_group_hit(ntext: str, group: list[str]) -> bool:
    # all tokens (as substrings) must appear
    for t in group:
        t = t.lower()
        if t not in ntext:
            return False
    return True


def match_item(ntext: str, item: dict) -> tuple[bool, list[str]]:
    reasons = []
    for al in item["aliases"]:
        if alias_hit(ntext, al):
            reasons.append(f"alias:{al}")
            if len(reasons) >= 5:
                break
    for g in item["token_groups"]:
        if token_group_hit(ntext, g):
            reasons.append("tokens:" + "+".join(g))
            if len(reasons) >= 8:
                break
    return (bool(reasons), reasons)


def main() -> None:
    parser = argparse.ArgumentParser(description="Matrix12 expanded notes-organized search")
    parser.add_argument("--corpus", default=None, help="Force corpus path (overrides CORPUS_OVERRIDE/env default)")
    parser.add_argument("--expect-files", type=int, default=None, help="Force omission-guard live file total (e.g. 2493)")
    parser.add_argument("--out-dir", default=None, help="Force output directory")
    args, _unknown = parser.parse_known_args()
    global CORPUS, OUT_DIR
    if args.corpus:
        CORPUS = Path(args.corpus)
    if args.out_dir:
        OUT_DIR = Path(args.out_dir)
    expect = args.expect_files if args.expect_files is not None else _resolve_expected_files()

    t0 = time.time()
    if not CORPUS.is_dir():
        raise SystemExit(f"CORPUS not a directory: {CORPUS}")
    files = sorted(CORPUS.rglob("*"))
    files = [p for p in files if p.is_file()]
    if expect is not None and len(files) != expect:
        raise SystemExit(
            f"OMISSION_GUARD_FAIL: live find-type-f count {len(files)} != EXPECTED_FILES {expect} under {CORPUS}"
        )
    print(f"OVERRIDE_OK corpus={CORPUS} live_files={len(files)} expect={expect}", flush=True)
    md_files = [p for p in files if p.suffix.lower() == ".md"]

    # per-item aggregates
    agg = {
        it["item_id"]: {
            "item_id": it["item_id"],
            "concept": it["concept"],
            "hit_files": 0,
            "hit_pre_paper": 0,
            "hit_pre_may6": 0,
            "hit_may_2025": 0,
            "hit_no_timestamp": 0,
            "earliest_ts": None,
            "earliest_path": None,
            "earliest_title": None,
            "earliest_reasons": None,
            "latest_ts": None,
            "latest_path": None,
            "top_hits": [],  # list of dicts
            "alias_hits": defaultdict(int),
        }
        for it in ITEMS
    }

    scanned = 0
    for path in md_files:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        scanned += 1
        meta = parse_meta(text)
        # prefer created, else modified
        ts = parse_ts(meta.get("created")) or parse_ts(meta.get("modified"))
        ntext = norm(text)
        rel = str(path.relative_to(CORPUS))

        for it in ITEMS:
            ok, reasons = match_item(ntext, it)
            if not ok:
                continue
            a = agg[it["item_id"]]
            a["hit_files"] += 1
            for r in reasons:
                if r.startswith("alias:"):
                    a["alias_hits"][r[6:]] += 1
            if ts is None:
                a["hit_no_timestamp"] += 1
            else:
                if ts < PAPER_TS:
                    a["hit_pre_paper"] += 1
                if ts < MAY6_TS:
                    a["hit_pre_may6"] += 1
                if MAY_START <= ts < MAY_END:
                    a["hit_may_2025"] += 1
                if a["earliest_ts"] is None or ts < a["earliest_ts"]:
                    a["earliest_ts"] = ts
                    a["earliest_path"] = rel
                    a["earliest_title"] = meta.get("title")
                    a["earliest_reasons"] = reasons[:4]
                if a["latest_ts"] is None or ts > a["latest_ts"]:
                    a["latest_ts"] = ts
                    a["latest_path"] = rel
            if len(a["top_hits"]) < 12:
                a["top_hits"].append(
                    {
                        "path": rel,
                        "title": meta.get("title"),
                        "note_pk": meta.get("note_pk"),
                        "folder": meta.get("folder"),
                        "ts_utc": fmt_ts(ts),
                        "created": meta.get("created"),
                        "modified": meta.get("modified"),
                        "before_paper": (ts < PAPER_TS) if ts is not None else None,
                        "reasons": reasons[:5],
                        "snippet": re.sub(r"\s+", " ", text)[:220],
                    }
                )

    rows = []
    for it in ITEMS:
        a = agg[it["item_id"]]
        # sort top hits by ts
        def sk(h):
            return h["ts_utc"] or "9999"

        a["top_hits"] = sorted(a["top_hits"], key=sk)[:10]
        top_aliases = sorted(a["alias_hits"].items(), key=lambda x: -x[1])[:8]
        rows.append(
            {
                "item_id": a["item_id"],
                "concept": a["concept"],
                "hit_files": a["hit_files"],
                "hit_pre_paper": a["hit_pre_paper"],
                "hit_pre_may6": a["hit_pre_may6"],
                "hit_may_2025": a["hit_may_2025"],
                "hit_no_timestamp": a["hit_no_timestamp"],
                "earliest_ts_utc": fmt_ts(a["earliest_ts"]),
                "earliest_path": a["earliest_path"],
                "earliest_title": a["earliest_title"],
                "earliest_reasons": a["earliest_reasons"],
                "latest_ts_utc": fmt_ts(a["latest_ts"]),
                "latest_path": a["latest_path"],
                "top_aliases": [{"alias": k, "count": v} for k, v in top_aliases],
                "top_hits": a["top_hits"],
                "priority_supported_by_notes_timestamp": bool(
                    a["earliest_ts"] is not None and a["earliest_ts"] < PAPER_TS
                ),
                "gap_days_earliest_to_paper": (
                    round((PAPER_TS - a["earliest_ts"]) / 86400, 1)
                    if a["earliest_ts"] is not None
                    else None
                ),
            }
        )

    matched = sum(1 for r in rows if r["hit_files"] > 0)
    matched_pre = sum(1 for r in rows if r["priority_supported_by_notes_timestamp"])

    payload = {
        "job": "matrix12_notes_organized_expanded_synonym_token_search",
        "compiled_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "corpus": {
            "path": str(CORPUS),
            "total_files_find_type_f": len(files),
            "md_files_scanned": scanned,
        },
        "method": {
            "match_type": "alias substring/fuzzy + token-group inclusion (all tokens required)",
            "targets": "12 zero-hit export-bind item ids: 05,06,08,12,13,14,24,26,27,29,32,35",
            "timestamp_field": "created if parseable else modified from note frontmatter",
            "notes": [
                "Token groups are substring ANDs on normalized text (not full NLP).",
                "Broader aliases raise recall; false positives possible — inspect top_hits.",
                "Does not re-scan ChatGPT conversations.json; notes-organized only.",
            ],
        },
        "anchors": {
            "paper_arxiv_date_utc": "2025-12-08T00:00:00Z",
            "driftcore_claim_date_utc": "2025-05-06T00:00:00Z",
        },
        "coverage": {
            "items_searched": 12,
            "items_with_any_hit": matched,
            "items_with_pre_paper_timestamped_hit": matched_pre,
            "items_still_zero": [r["item_id"] for r in rows if r["hit_files"] == 0],
        },
        "results": rows,
        "elapsed_seconds": round(time.time() - t0, 2),
    }

    out_json = OUT_DIR / "matrix12_notes_organized_expanded_search.json"
    out_md = OUT_DIR / "matrix12_notes_organized_expanded_search.md"
    out_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False))

    L = []
    A = L.append
    A("# Matrix 12 × notes-organized — expanded synonym/token search")
    A("")
    A(f"**Compiled:** {payload['compiled_utc']}")
    A(f"**Corpus:** `{CORPUS}`")
    A(f"**Live disk files (`find -type f`):** **{len(files)}**")
    A(f"**Markdown scanned:** **{scanned}**")
    A(f"**Method:** alias fuzzy substring + token-group AND inclusion")
    A(f"**Elapsed:** {payload['elapsed_seconds']}s")
    A("")
    A("## Coverage")
    A(f"- Any hit: **{matched}/12**")
    A(f"- Pre-paper timestamped hit: **{matched_pre}/12**")
    A(f"- Still zero: {payload['coverage']['items_still_zero'] or 'none'}")
    A("")
    A("## Results")
    A("")
    A("| id | concept | hits | pre_paper | may2025 | earliest_utc | gap_d | path |")
    A("|----|---------|-----:|----------:|--------:|--------------|------:|------|")
    for r in rows:
        conc = r["concept"][:42]
        ea = r["earliest_ts_utc"] or "—"
        gap = r["gap_days_earliest_to_paper"]
        gap_s = str(gap) if gap is not None else "—"
        path = (r["earliest_path"] or "—")[:48]
        A(
            f"| {r['item_id']} | {conc} | {r['hit_files']} | {r['hit_pre_paper']} | {r['hit_may_2025']} | {ea} | {gap_s} | `{path}` |"
        )
    A("")
    A("## Per-item detail")
    for r in rows:
        A("")
        A(f"### {r['item_id']} — {r['concept']}")
        A(f"- **hits:** {r['hit_files']} · pre_paper {r['hit_pre_paper']} · pre_may6 {r['hit_pre_may6']} · may2025 {r['hit_may_2025']} · no_ts {r['hit_no_timestamp']}")
        A(f"- **earliest:** `{r['earliest_ts_utc']}` · `{r['earliest_path']}`")
        A(f"- **reasons:** {r['earliest_reasons']}")
        if r["top_aliases"]:
            A("- **top aliases:** " + ", ".join(f"{x['alias']} ({x['count']})" for x in r["top_aliases"][:6]))
        for h in r["top_hits"][:5]:
            A(f"  - `{h['ts_utc']}` · {h['title']!s} · `{h['path']}` · {h['reasons'][:3]}")
    A("")
    A("## Files")
    A(f"- `{out_json}`")
    A(f"- `{out_md}`")
    out_md.write_text("\n".join(L))

    print(json.dumps({
        "corpus_files": len(files),
        "md_scanned": scanned,
        "matched": matched,
        "matched_pre": matched_pre,
        "still_zero": payload["coverage"]["items_still_zero"],
        "out_json": str(out_json),
        "out_md": str(out_md),
        "rows": [
            {
                "id": r["item_id"],
                "hits": r["hit_files"],
                "pre_paper": r["hit_pre_paper"],
                "earliest": r["earliest_ts_utc"],
                "gap_d": r["gap_days_earliest_to_paper"],
            }
            for r in rows
        ],
        "elapsed": payload["elapsed_seconds"],
    }, indent=2))


if __name__ == "__main__":
    main()
