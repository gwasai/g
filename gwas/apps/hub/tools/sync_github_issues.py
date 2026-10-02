#!/usr/bin/env python3
"""
Export GitHub issues for GWAS Hub.

Preferred path: authenticated GitHub CLI.
Fallback path: public GitHub REST API for public repositories.

This exporter does not write private data to GitHub. It only retrieves issue
metadata and emits normalized JSON for local GWAS ingestion.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone


def via_gh(repo: str, limit: int) -> list[dict]:
    fields = "number,title,state,url,labels,assignees,createdAt,updatedAt,closedAt,body"
    cmd = [
        "gh", "issue", "list",
        "--repo", repo,
        "--state", "all",
        "--limit", str(limit),
        "--json", fields,
    ]
    p = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return json.loads(p.stdout)


def via_rest(repo: str, limit: int) -> list[dict]:
    url = f"https://api.github.com/repos/{repo}/issues?state=all&per_page={min(limit,100)}&sort=updated&direction=desc"
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "GWAS-Hub"},
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        rows = json.load(r)
    out = []
    for x in rows:
        if "pull_request" in x:
            continue
        out.append({
            "number": x.get("number"),
            "title": x.get("title"),
            "state": x.get("state"),
            "url": x.get("html_url"),
            "labels": [{"name": v.get("name")} for v in x.get("labels", [])],
            "assignees": [{"login": v.get("login")} for v in x.get("assignees", [])],
            "createdAt": x.get("created_at"),
            "updatedAt": x.get("updated_at"),
            "closedAt": x.get("closed_at"),
            "body": x.get("body"),
        })
    return out


def normalize(repo: str, rows: list[dict], source: str) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    items = []
    for x in rows:
        n = x.get("number")
        items.append({
            "external_ref": f"github://{repo}/issues/{n}",
            "source": "github",
            "repository": repo,
            "number": n,
            "title": x.get("title"),
            "state": str(x.get("state", "")).lower(),
            "url": x.get("url"),
            "labels": [v.get("name") for v in x.get("labels", []) if v.get("name")],
            "assignees": [v.get("login") for v in x.get("assignees", []) if v.get("login")],
            "body": x.get("body"),
            "created_at": x.get("createdAt"),
            "updated_at": x.get("updatedAt"),
            "closed_at": x.get("closedAt"),
        })
    return {
        "schema": "gwas.github-issues-export/1",
        "repository": repo,
        "retrieved_via": source,
        "retrieved_at": now,
        "items": items,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="gwasai/g")
    ap.add_argument("--limit", type=int, default=100)
    ap.add_argument("--out", help="write JSON to this path; default stdout")
    args = ap.parse_args()

    source = "rest"
    rows = None
    if shutil.which("gh"):
        try:
            rows = via_gh(args.repo, args.limit)
            source = "gh"
        except Exception as exc:
            print(f"gh failed; falling back to REST: {exc}", file=sys.stderr)
    if rows is None:
        rows = via_rest(args.repo, args.limit)

    payload = normalize(args.repo, rows, source)
    text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
