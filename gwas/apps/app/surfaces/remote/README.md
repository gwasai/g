# GWAS Remote

Installable browser/PWA surface for iPhone before the native iOS client is distributed.

## Intended deployment

Do **not** expose the private GWAS database to the public internet.

The Mac runs GWAS on localhost and a private network proxy exposes the GWAS HTTP service only to the person's authorized devices. The remote page then uses the same API as the native macOS shell.

The current prototype reads:

- `/_gwas/api/status`
- `/_gwas/api/namespaces`
- `/_gwas/api/ceo`
- `/_gwas/api/devbus`

When served by the Mac itself it is same-origin and requires no separate public backend.

## Data rule

SQLite stays behind the authority. iPhone/web/native clients talk to APIs/events; they do not open or synchronize the raw SQLite file.

## Family rule

Each person owns a separate private GWAS authority. Sharing uses explicit, scoped messages/events/tasks. A synthetic `g` agent derived from another person's work must not be represented as that person's actual approval or decision.
