# ChatGPT ↔ GitHub ↔ GWAS Work Bridge

## Role of each system

### ChatGPT
Useful for planning, research, drafting, code generation, and creating/updating external coordination records.

### GitHub
A durable, public/open-source coordination ledger for GWAS software work: issues, pull requests, commits, releases, and code review.

### GWAS
The person's local authority. It owns private state, permissions, personal data, work projections, provider credentials, and the complete local accountability graph.

## Mapping

A GitHub issue is not itself the GWAS Work item.

Example:

```json
{
  "work_item_id": "work:gwas:work-ledger",
  "title": "Add GWAS Work ledger / todos / accountability UI",
  "external_refs": [
    "github://gwasai/g/issues/3"
  ]
}
```

This allows one Work item to later link to:

- a GitHub issue
- one or more PRs
- a ChatGPT conversation
- installer/build artifacts
- screenshots
- tests
- Dev Bus traces

## Sync rules

- GitHub title/state/labels/comments are external observations.
- GWAS imports them as events and updates a projection.
- Private GWAS fields are never automatically pushed to a public issue.
- The local person can explicitly publish a summary back to GitHub.
- GitHub issue closure does not silently equal human approval inside GWAS.

## Screenshots

Screenshot files under a person's media namespace should be indexable as local artifacts, e.g.

```
media.crhaueter.com/screenshots/originals/<file>
```

A work item may link screenshots without copying the image into GitHub.
