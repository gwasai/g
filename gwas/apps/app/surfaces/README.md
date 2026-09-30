# GWAS surfaces

One GWAS namespace can appear on multiple surfaces while sharing the same person-owned state.

- `macos/` — native authority/desktop surface
- `ios/` — native iPhone/iPad client
- `remote/` — installable web/PWA client for immediate private remote access
- `web/` — public or namespace web surface
- `chrome/`, `vscode/`, `obsidian/`, `cli/` — additional clients

The database is not a network API. Clients talk to the GWAS service. The person's Mac is the initial authority for that person's private vault.
