# GWAS personal-authority architecture

## Authority

Each person owns a separate GWAS authority. The initial authority is that person's Mac running GWAS and its local SQLite state.

- `c` is the current person.
- `g` is the dataset, representation, and agentic work derived from/for that person.
- `z` is future-facing ZWAS work.

The database is an implementation detail behind the GWAS service. iPhone, web, Chrome, VS Code, Obsidian, CLI, and other surfaces call the service; they do not open the raw SQLite database.

## Private remote access

The first remote transport is a private device network. GWAS stays bound to localhost and Tailscale Serve proxies it to authorized devices in the user's tailnet.

Do not use a public tunnel for medical, genomic, financial, secrets, or permission data by default.

## Family installations

A sibling's GWAS installation is a separate authority and private vault. Family members do not share one database.

Cross-person collaboration exchanges explicit, scoped events/tasks such as:

- capability advertisement
- task request
- task acceptance/decline
- bounded context grant
- result/evidence
- human approval

Private source data stays local unless its owner explicitly grants a scoped disclosure.

## Person-derived g agents

A `g` agent may be derived from public work, provided examples, or explicitly shared work associated with a real person. It must remain distinguishable from the real person.

A generated action may be:

- inspired by a person
- assigned to that person's synthetic g agent
- evaluated against that person's historical work

It is not that person's decision, endorsement, or approval unless the person actually approves it.

## Assignment and provenance

Every consequential task should record:

- requesting c person
- assigned g agent
- real-person inspiration/provenance, if any
- permissions/context granted
- model/provider/run
- result/evidence
- whether a real human approved the result

## Hosting boundaries

GitHub stores source code and public artifacts.

Public hosts such as Vercel can serve public/static GWAS sites, documentation, and intentionally public APIs. They are not the default storage location for a person's private GWAS vault.

## Provider provisioning

Each namespace can lazily own provider boundaries such as:

- OpenAI project: `gwas-ceo`
- Anthropic workspace: `gwas-ceo`
- local runtime: `gwas-ceo`

Inference credentials and organization-admin provisioning credentials are separate. Admin credentials, when enabled, live only in the person's secure local credential store and are never sent to client-side iOS/web code.
