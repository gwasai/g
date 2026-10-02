# GitHub Issues → GWAS Hub

This surface turns GitHub issues into a visible GWAS Hub work feed.

## Why

ChatGPT can create or update GitHub issues through the connected GitHub account. GWAS can then read those same issues through either:

1. the GitHub REST API (portable/read-only public view), or
2. the authenticated `gh` CLI / GitHub API on the person's Mac (preferred for the local authority).

That creates a simple bridge:

```
ChatGPT
  -> GitHub issue / PR
  -> GWAS Hub sync
  -> local work_item / source_ref
  -> GWAS UI
```

GitHub is an external coordination source, not the private source of truth for genomic, medical, financial, secrets, or permission data.

## Current page

`index.html` fetches public issues for `gwasai/g` and provides a lightweight filterable work view. It can be served statically or embedded as a GWAS web surface.

## Local sync

Use `tools/sync_github_issues.py` on the Mac to pull issue metadata through authenticated `gh` when available. The output is suitable for later ingestion into the GWAS Work ledger.

GitHub issue numbers should remain stable external references such as:

```
github://gwasai/g/issues/3
github://gwasai/g/issues/4
```

GWAS Work items get their own local IDs and may link to zero or more external issues/PRs.
