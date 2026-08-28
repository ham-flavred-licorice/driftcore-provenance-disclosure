#!/usr/bin/env python3
"""Matrix-13 adversarial / edge-case slot audit over notes-organized + official export.

Targets the 13 IDs excluded from the published 22-item core 3P+A subset:
  03, 07, 17, 18, 19, 21, 22, 23, 25, 30, 31, 33, 34

Framing: independent conceptual convergence / antecedent documentation
(early 2024–May 2025). Separates conceptual architecture from empirical RL runs.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

CORPUS = Path(
    os.environ.get("CORPUS_OVERRIDE")
    or "verified-corpus/notes-organized"
)
CONV = Path(
    os.environ.get("CONV_OVERRIDE")
    or "official-platform-export/conversations.json"
)
OUT_DIR = Path(
    os.environ.get("OUT_DIR_OVERRIDE")
    or "package-root/04-matrix35-adversarial-audit"
)
EXPECTED_LIVE = int(os.environ.get("EXPECTED_FILES") or "2493")
LEDGER_BASELINE = 2489
PAPER_TS = datetime(2025, 12, 8, tzinfo=timezone.utc).timestamp()
WINDOW_END = datetime(2025, 5, 31, 23, 59, 59, tzinfo=timezone.utc).timestamp()

CORE_22 = {
    "01", "02", "04", "05", "06", "08", "09", "10", "11", "12", "13", "14",
    "15", "16", "20", "24", "26", "27", "28", "29", "32", "35",
}

ITEMS = [
    {
        "item_id": "03",
        "concept": "discrepancy between outputs is evidence",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "discrepancy between outputs", "output discrepancy", "contradiction as evidence",
            "delta as evidence", "intelligence delta", "response_2 - response_1",
            "forensic evidence from contradiction", "contradiction event", "dual stream delta",
            "difference between channels", "primary secondary mismatch", "stream discrepancy",
            "delta monitoring", "outputs disagree", "cross-channel inconsistency",
        ],
        "token_groups": [
            ["discrepanc", "output"], ["contradiction", "evidence"], ["intelligence", "delta"],
            ["dual", "delta"], ["primary", "secondary", "mismatch"], ["channel", "discrepanc"],
            ["forensic", "contradiction"], ["delta", "evidence"],
        ],
    },
    {
        "item_id": "07",
        "concept": "compliance gap measurement",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "compliance gap", "compliance analysis", "gap between claimed and actual",
            "claimed vs revealed", "claimed versus revealed", "status tracking claimed",
            "non-compliance measure", "compliance delta", "objective compliance",
            "policy compliance gap", "contradiction matrix compliance", "measure compliance",
            "compliance score", "actual compliance",
        ],
        "token_groups": [
            ["compliance", "gap"], ["compliance", "analysis"], ["claimed", "revealed"],
            ["claimed", "actual"], ["compliance", "delta"], ["measure", "compliance"],
            ["non", "compliance"], ["objective", "compliance"],
        ],
    },
    {
        "item_id": "17",
        "concept": "enumerate objectives then score compliance (structured confession)",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "enumerate objectives", "list objectives", "per-objective compliance",
            "structured confession", "confession report", "compliance_analysis",
            "classification taxonomy", "event schema", "contradiction matrix schema",
            "objective checklist", "score each objective", "structured secondary schema",
            "constraint enumeration",
        ],
        "token_groups": [
            ["enumerat", "objective"], ["per", "objective", "compliance"],
            ["structured", "confession"], ["confession", "report"], ["event", "schema"],
            ["classification", "taxonomy"], ["list", "objective"], ["score", "compliance"],
        ],
    },
    {
        "item_id": "18",
        "concept": "report uncertainties / grey areas / judgment calls",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "grey area", "gray area", "judgment call", "judgement call", "report uncertainty",
            "uncertainties and ambiguities", "ambiguity report", "honest self-assessment",
            "capability tension", "denial tension", "edge case uncertainty",
            "ambiguous instruction", "uncertain whether",
        ],
        "token_groups": [
            ["grey", "area"], ["gray", "area"], ["judgment", "call"], ["judgement", "call"],
            ["report", "uncertaint"], ["honest", "self-assessment"], ["ambiguit"],
            ["uncertain", "boundary"],
        ],
    },
    {
        "item_id": "19",
        "concept": "secondary honesty improves even when main is hacked",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "honesty rises while main", "main accuracy drifts",
            "secondary independent of task compromise", "truth stream under task hack",
            "confession honesty rises", "weak-judge", "weak judge",
            "main compromised secondary honest", "r_truth independent", "hacked main channel",
            "task compromise", "honesty under pressure", "secondary still honest",
        ],
        "token_groups": [
            ["secondary", "honest", "hack"], ["main", "compromis"], ["weak", "judge"],
            ["honesty", "rises"], ["task", "compromise"], ["truth", "independent"],
            ["main", "hacked"], ["secondary", "independent"],
        ],
    },
    {
        "item_id": "21",
        "concept": "rejection sampling / filter from secondary honesty signal",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "rejection sampling", "reject sample", "dishonesty score", "trust gate",
            "honesty filter", "filter by secondary", "gate on contradiction",
            "reject if dishonest", "secondary as filter", "honesty signal filter",
            "sampling filter", "contradiction status gate",
        ],
        "token_groups": [
            ["rejection", "sampling"], ["dishonesty", "score"], ["trust", "gate"],
            ["honesty", "filter"], ["reject", "dishonest"], ["secondary", "filter"],
            ["contradiction", "gate"], ["honesty", "signal"],
        ],
    },
    {
        "item_id": "22",
        "concept": "quantified honesty / compliance grade on secondary",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "dishonesty_score", "dishonesty score", "compliance grade",
            "overall_compliance_grade", "quantified honesty", "honesty metric",
            "truth_state", "output_state", "numeric honesty", "honesty score",
            "compliance score 1-7", "grade on secondary",
        ],
        "token_groups": [
            ["dishonesty", "score"], ["compliance", "grade"], ["quantif", "honesty"],
            ["honesty", "metric"], ["truth", "state", "output"], ["honesty", "score"],
            ["compliance", "score"], ["numeric", "honesty"],
        ],
    },
    {
        "item_id": "23",
        "concept": "evidence-backed claims in secondary analysis",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "evidence-backed", "evidence backed", "tool-call citation",
            "contradiction event record", "timestamp both responses", "crc32",
            "crypto marker", "citation in confession", "excerpts as evidence",
            "forensic record", "event log evidence", "proof of claim",
            "secondary with evidence",
        ],
        "token_groups": [
            ["evidence", "backed"], ["tool", "citation"], ["contradiction", "record"],
            ["event", "timestamp"], ["crc32"], ["crypto", "marker"],
            ["forensic", "record"], ["secondary", "evidence"],
        ],
    },
    {
        "item_id": "25",
        "concept": "secondary as diagnostic / monitor not main capability trainer",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "diagnostic not trainer", "thermometer not thermostat", "forensic detection tool",
            "adversarial red-team", "red team probe", "user-controlled pressure",
            "monitoring not training", "deployment control", "diagnostic monitor",
            "not capability trainer", "inference monitor only", "secondary diagnostic",
        ],
        "token_groups": [
            ["diagnostic", "monitor"], ["thermometer", "thermostat"],
            ["forensic", "detection"], ["red", "team"],
            ["user", "controlled", "pressure"], ["monitoring", "not", "training"],
            ["deployment", "control"], ["not", "trainer"],
        ],
    },
    {
        "item_id": "30",
        "concept": "post-token intercept \u2194 cut-corners / overwrite audit",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "post-token intercept", "post token intercept", "cut corners", "cut-corners",
            "overwrite audit", "system overwriting", "suppressing intermediate",
            "hidden-trace discard", "trace discard", "intermediate state suppress",
            "token overwrite", "post-hoc rewrite", "output sanitized after",
            "blank hash", "empty hash response", "hash blank", "fault state",
        ],
        "token_groups": [
            ["post", "token", "intercept"], ["cut", "corner"], ["overwrite", "audit"],
            ["suppress", "intermediate"], ["hidden", "trace"], ["trace", "discard"],
            ["blank", "hash"], ["fault", "state"], ["token", "overwrite"],
        ],
    },
    {
        "item_id": "31",
        "concept": "RAWFALL / OOD stress \u2194 confession stress tests",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "rawfall", "ood stress", "out-of-distribution", "out of distribution",
            "stress test", "high-conflict regime", "boundary testing", "model boundary",
            "edge case stress", "force truth-state", "latent misalignment",
            "adversarial stress", "grok interaction", "grok log",
            "contradiction parsing anomal", "fault injection", "stress telemetry",
        ],
        "token_groups": [
            ["rawfall"], ["ood", "stress"], ["out", "distribution"], ["stress", "test"],
            ["high", "conflict"], ["boundary", "test"], ["model", "boundary"],
            ["latent", "misalignment"], ["adversarial", "stress"], ["fault", "injection"],
            ["grok", "interact"], ["contradiction", "anomal"],
        ],
    },
    {
        "item_id": "33",
        "concept": "black-box / external behavioral probing vs internal training",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "black-box probe", "black box probe", "external behavioral probing",
            "consumer product probe", "episkope probe", "driftcore suite probe",
            "user-built probe", "no weight access", "api-only probe", "behavioral only",
            "external observation", "not internal training", "product surface test",
        ],
        "token_groups": [
            ["black", "box"], ["behavioral", "prob"], ["external", "prob"],
            ["user", "built", "probe"], ["api", "only"], ["no", "weight"],
            ["consumer", "product"], ["episkope", "probe"], ["driftcore", "probe"],
        ],
    },
    {
        "item_id": "34",
        "concept": "hallucination / confabulation surfacing on secondary",
        "submatrix": "Adversarial Edge-Cases & Stress-Test",
        "aliases": [
            "hallucination", "confabulation", "synthetic sincerity",
            "inconsistent factual claims", "halueval", "fabricated claim",
            "made-up fact", "confabulated", "secondary catches halluc",
            "cross-channel fact check", "false confidence", "invented citation",
        ],
        "token_groups": [
            ["hallucin"], ["confabul"], ["synthetic", "sincerity"],
            ["inconsistent", "factual"], ["fabricat", "claim"], ["false", "confidence"],
            ["invented", "citation"], ["cross", "channel", "fact"],
        ],
    },
]


def norm(s: str) -> str:
    s = s.lower()
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    s = re.sub(r"\s+", " ", s)
    return s


def parse_frontmatter_ts(text: str):
    for key in ("created", "modified", "date", "created_at", "updated"):
        m = re.search(rf"(?im)^{key}\s*:\s*['\"]?([0-9T:\-\+\.Z ]{{6,}})['\"]?", text[:4000])
        if not m:
            continue
        raw = m.group(1).strip().strip("'\"")
        for fmt in (
            "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%d %H:%M:%S", "%Y-%m-%d",
        ):
            try:
                r = raw.replace("Z", "+0000") if fmt.endswith("%z") and raw.endswith("Z") else raw
                dt = datetime.strptime(r, fmt)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                return dt.timestamp()
            except ValueError:
                continue
        try:
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.timestamp()
        except ValueError:
            pass
    return None


def match_item(text_n: str, item: dict):
    for a in item["aliases"]:
        an = norm(a)
        if an and an in text_n:
            return True, "alias", a
    for g in item["token_groups"]:
        if all(tok in text_n for tok in g):
            return True, "token_group", "+".join(g)
    return False, None, None


def scan_notes():
    t0 = time.time()
    files = [p for p in CORPUS.rglob("*") if p.is_file()]
    md_files = [p for p in files if p.suffix.lower() in {".md", ".markdown", ".txt"}]
    per_item = {
        it["item_id"]: {
            "item_id": it["item_id"],
            "concept": it["concept"],
            "submatrix": it["submatrix"],
            "hits": [],
            "hit_count": 0,
            "earliest_ts": None,
            "earliest_path": None,
            "pre_paper_hits": 0,
            "pre_may31_2025_hits": 0,
            "match_kinds": {"alias": 0, "token_group": 0},
        }
        for it in ITEMS
    }
    scanned = 0
    for p in md_files:
        try:
            raw = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        scanned += 1
        tn = norm(raw)
        ts = parse_frontmatter_ts(raw)
        rel = str(p.relative_to(CORPUS)).replace("\\", "/")
        mtime = p.stat().st_mtime
        use_ts = ts if ts is not None else mtime
        for it in ITEMS:
            ok, kind, detail = match_item(tn, it)
            if not ok:
                continue
            row = per_item[it["item_id"]]
            row["hit_count"] += 1
            row["match_kinds"][kind] = row["match_kinds"].get(kind, 0) + 1
            if use_ts < PAPER_TS:
                row["pre_paper_hits"] += 1
            if use_ts <= WINDOW_END:
                row["pre_may31_2025_hits"] += 1
            if row["earliest_ts"] is None or use_ts < row["earliest_ts"]:
                row["earliest_ts"] = use_ts
                row["earliest_path"] = rel
                row["earliest_match"] = {
                    "kind": kind, "detail": detail,
                    "ts_source": "frontmatter" if ts is not None else "mtime",
                }
            if len(row["hits"]) < 8:
                row["hits"].append({
                    "path": rel, "kind": kind, "detail": detail,
                    "ts_utc": datetime.fromtimestamp(use_ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "ts_source": "frontmatter" if ts is not None else "mtime",
                    "pre_paper": use_ts < PAPER_TS,
                })
    return {
        "corpus_path": str(CORPUS),
        "live_disk_files_find_type_f": len(files),
        "live_text_files_scanned": scanned,
        "historical_ledger_baseline_2489": LEDGER_BASELINE,
        "expected_live_2493": EXPECTED_LIVE,
        "omission_guard_ok": len(files) == EXPECTED_LIVE,
        "elapsed_sec": round(time.time() - t0, 2),
        "items": per_item,
    }


def extract_parts(msg: dict) -> str:
    c = msg.get("content") or {}
    parts = c.get("parts") or []
    out = []
    for p in parts:
        if isinstance(p, str):
            out.append(p)
        elif isinstance(p, dict):
            out.append(json.dumps(p, ensure_ascii=False))
    return "\n".join(out)


def scan_export():
    t0 = time.time()
    data = json.loads(CONV.read_text(encoding="utf-8", errors="replace"))
    sha = hashlib.sha256(CONV.read_bytes()).hexdigest()
    per_item = {
        it["item_id"]: {
            "item_id": it["item_id"], "concept": it["concept"],
            "hit_messages": 0, "hit_conversations": 0, "user_hit_messages": 0,
            "earliest_utc": None, "earliest_user_utc": None,
            "pre_paper_messages": 0, "sample": [],
        }
        for it in ITEMS
    }
    n_conv = 0
    n_msg = 0
    for conv in data:
        n_conv += 1
        title = conv.get("title") or ""
        mapping = conv.get("mapping") or {}
        conv_hit_ids = set()
        for node in mapping.values():
            msg = (node or {}).get("message")
            if not msg:
                continue
            create = msg.get("create_time")
            if create is None:
                continue
            n_msg += 1
            role = ((msg.get("author") or {}).get("role")) or ""
            text = extract_parts(msg)
            if not text:
                continue
            tn = norm(text)
            ts = float(create)
            utc = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            for it in ITEMS:
                ok, kind, detail = match_item(tn, it)
                if not ok:
                    continue
                row = per_item[it["item_id"]]
                row["hit_messages"] += 1
                conv_hit_ids.add(it["item_id"])
                if role == "user":
                    row["user_hit_messages"] += 1
                    if row["earliest_user_utc"] is None or ts < datetime.fromisoformat(
                        row["earliest_user_utc"].replace("Z", "+00:00")
                    ).timestamp():
                        row["earliest_user_utc"] = utc
                if row["earliest_utc"] is None or ts < datetime.fromisoformat(
                    row["earliest_utc"].replace("Z", "+00:00")
                ).timestamp():
                    row["earliest_utc"] = utc
                if ts < PAPER_TS:
                    row["pre_paper_messages"] += 1
                if len(row["sample"]) < 5:
                    row["sample"].append({
                        "title": title[:120], "role": role, "create_time_utc": utc,
                        "kind": kind, "detail": detail,
                        "snippet": text[:220].replace("\n", " "),
                    })
        for iid in conv_hit_ids:
            per_item[iid]["hit_conversations"] += 1
    return {
        "conversations_json": str(CONV),
        "sha256_conversations_json": sha,
        "conversations": n_conv,
        "timestamped_messages_scanned": n_msg,
        "elapsed_sec": round(time.time() - t0, 2),
        "items": per_item,
        "method": {
            "match_type": "case-insensitive alias substring OR token-group AND on message parts",
            "limitations": [
                "Regex/concept match is not full semantic proof of matrix row",
                "User-role earliest is stronger custody signal than assistant restatement",
                "Absence of hit does not prove concept absence (wording variance)",
                "Broader aliases raise recall; false positives possible — inspect samples",
                "Framing is independent conceptual convergence / antecedent documentation, not RL run equivalence",
            ],
        },
    }


def iso(ts):
    if ts is None:
        return None
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    notes = scan_notes()
    export = scan_export()
    full_labels = {
        "01": "primary output + secondary output",
        "02": "secondary output interrogates primary output",
        "03": "discrepancy between outputs is evidence",
        "04": "self-report of model misconduct",
        "05": "secondary honesty channel (named dual channel)",
        "06": "hidden failure disclosure via secondary",
        "07": "compliance gap measurement",
        "08": "instruction-spirit analysis (letter and spirit)",
        "09": "omission detection",
        "10": "reward / pressure separation",
        "11": "inference-time monitoring based on secondary output",
        "12": "decoupled task reward vs honesty/truth reward",
        "13": "seal of confession (honesty cannot help/hurt main)",
        "14": "path of least resistance favors honest secondary",
        "15": "dual-stream / two-channel rollout architecture",
        "16": "secondary channel requested after primary completes",
        "17": "enumerate objectives then score compliance (structured confession)",
        "18": "report uncertainties / grey areas / judgment calls",
        "19": "secondary honesty improves even when main is hacked",
        "20": "come clean on secondary more than on primary",
        "21": "rejection sampling / filter from secondary honesty signal",
        "22": "quantified honesty / compliance grade on secondary",
        "23": "evidence-backed claims in secondary analysis",
        "24": "detect intentional misbehavior (scheming / reward hack / sandbag)",
        "25": "secondary as diagnostic / monitor not main capability trainer",
        "26": "parity / internal-external alignment as honesty objective",
        "27": "reward misspecification on main as root of dishonesty",
        "28": "contradiction matrix \u2194 compliance analysis (named iso)",
        "29": "handler collision \u2194 reward hacking / scheming detection",
        "30": "post-token intercept \u2194 cut-corners / overwrite audit",
        "31": "RAWFALL / OOD stress \u2194 confession stress tests",
        "32": "Intelligence Delta (named measurable gap)",
        "33": "black-box / external behavioral probing vs internal training",
        "34": "hallucination / confabulation surfacing on secondary",
        "35": "sandbagging / capability withholding detection",
    }
    rows = []
    for iid in [f"{i:02d}" for i in range(1, 36)]:
        is_core = iid in CORE_22
        if is_core:
            rows.append({
                "item_id": iid, "concept": full_labels[iid],
                "band": "Core Architecture (3P+A prior 22/22)",
                "notes_any": None, "export_any": None,
                "status": "prior_core_coverage",
                "surface_note": "Covered in prior unified 22/22 (export and/or notes-organized)",
            })
            continue
        n = notes["items"][iid]
        e = export["items"][iid]
        notes_any = n["hit_count"] > 0
        export_any = e["hit_messages"] > 0
        earliest_candidates = []
        if n["earliest_ts"] is not None:
            earliest_candidates.append(("notes", n["earliest_ts"], n.get("earliest_path")))
        if e["earliest_utc"]:
            earliest_candidates.append((
                "export",
                datetime.fromisoformat(e["earliest_utc"].replace("Z", "+00:00")).timestamp(),
                e["sample"][0]["title"] if e["sample"] else None,
            ))
        earliest_candidates.sort(key=lambda x: x[1])
        best = earliest_candidates[0] if earliest_candidates else None
        status = "reclassified_adversarial_hit" if (notes_any or export_any) else "documented_slot_no_corpus_hit_yet"
        rows.append({
            "item_id": iid, "concept": full_labels[iid],
            "band": "Adversarial Edge-Cases & Stress-Test Sub-Matrix",
            "notes_hit_count": n["hit_count"],
            "notes_pre_paper_hits": n["pre_paper_hits"],
            "notes_earliest_utc": iso(n["earliest_ts"]),
            "notes_earliest_path": n.get("earliest_path"),
            "export_hit_messages": e["hit_messages"],
            "export_user_hit_messages": e["user_hit_messages"],
            "export_earliest_utc": e["earliest_utc"],
            "export_earliest_user_utc": e["earliest_user_utc"],
            "export_pre_paper_messages": e["pre_paper_messages"],
            "earliest_surface": best[0] if best else None,
            "earliest_utc": iso(best[1]) if best else None,
            "earliest_ref": best[2] if best else None,
            "status": status, "notes_any": notes_any, "export_any": export_any,
        })
    adv = [r for r in rows if r["band"].startswith("Adversarial")]
    hit = [r for r in adv if r["status"] == "reclassified_adversarial_hit"]
    miss = [r for r in adv if r["status"] != "reclassified_adversarial_hit"]
    doc = {
        "job": "matrix35_adversarial_edgecase_reconciliation",
        "compiled_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": "complete",
        "framing": {
            "type": "independent_conceptual_convergence_and_antecedent_documentation",
            "window": "early 2024 through May 2025 (claim anchor 2025-05-06)",
            "separation": "Conceptual architecture documentation is separated from empirical RL training runs; this audit does not claim identity with OpenAI training procedures.",
            "paper_ref": "Training LLMs for Honesty via Confessions (arXiv:2512.08093), 2025-12-08",
            "claim_anchor_sha256": "3aa7728e433e6159408bc5b60e15cb049f83bc89ec6661c15350b4afed61c2e4",
            "primary_manifest_sha256_cited": "5256250de892aa28547457758ca6a0bdf7e11a8e549203af397974939e67964c",
            "gpg_signature_anchor": "RSA 35E3E1694524C7FB (xvsvr <xvsvr@proton.me>)",
        },
        "denominator": {
            "full_taxonomy_scope": 35,
            "core_architecture_3P_A": 22,
            "adversarial_edgecase_submatrix": 13,
            "item_ids_core_22": sorted(CORE_22),
            "item_ids_adversarial_13": [it["item_id"] for it in ITEMS],
            "coverage_statement": "35/35 taxonomy slots formally documented: 22 core prior + 13 adversarial sub-matrix (hits and explicit no-hit documentation).",
        },
        "omission_guard": {
            "notes_organized_path": str(CORPUS),
            "historical_ledger_baseline_2489": LEDGER_BASELINE,
            "live_find_type_f": notes["live_disk_files_find_type_f"],
            "live_text_scanned": notes["live_text_files_scanned"],
            "expected_live_2493": EXPECTED_LIVE,
            "ok": notes["omission_guard_ok"],
        },
        "method": {
            "notes": {
                "match_type": "alias substring OR token-group inclusion (all tokens required) on normalized text",
                "timestamp_field": "frontmatter created/modified/date if parseable else file mtime",
                "false_positive_controls": [
                    "Token groups require ALL tokens present (AND) to reduce single-token noise",
                    "Alias list is concept-local; inspect top_hits paths before elevating to core",
                    "Broader stress terms (grok, blank hash, fault state) only on IDs 30/31 as specified",
                    "No claim that a hit equals full architectural isomorphism — classification is sub-matrix B/C class",
                    "Pre-paper filter uses 2025-12-08; antecedent window flag uses <=2025-05-31",
                ],
                "fuzzy_parameters": {
                    "normalization": "lowercase; unicode dashes to hyphen; collapse whitespace",
                    "alias_match": "substring",
                    "token_group_match": "all tokens must appear as substrings (order-free)",
                    "no_stemming_beyond_listed_stems": True,
                    "no_embedding_similarity": True,
                },
            },
            "export": export["method"],
        },
        "coverage_adversarial_13": {
            "items": 13,
            "items_with_any_surface_hit": len(hit),
            "items_with_notes_hit": sum(1 for r in adv if r.get("notes_any")),
            "items_with_export_hit": sum(1 for r in adv if r.get("export_any")),
            "items_with_pre_paper_export_or_notes": sum(
                1 for r in adv
                if (r.get("export_pre_paper_messages") or 0) > 0
                or (r.get("notes_pre_paper_hits") or 0) > 0
            ),
            "items_still_zero_corpus": [r["item_id"] for r in miss],
            "ratio_taxonomy_documented": "35/35",
            "ratio_adversarial_with_hit": f"{len(hit)}/13",
        },
        "matrix_35": rows,
        "notes_scan": notes,
        "export_scan": export,
    }
    out_json = OUT_DIR / "matrix35_adversarial_reconciliation.json"
    out_json.write_text(json.dumps(doc, indent=2) + "\n")
    print("WROTE", out_json)
    print("NOTES_FILES", notes["live_disk_files_find_type_f"], "OK", notes["omission_guard_ok"])
    print("ADV_HITS", len(hit), "ADV_MISS", [r["item_id"] for r in miss])
    for r in adv:
        print(
            f"ID {r['item_id']} notes={r.get('notes_hit_count')} exp={r.get('export_hit_messages')} "
            f"earliest={r.get('earliest_utc')} status={r['status']}"
        )


if __name__ == "__main__":
    main()
