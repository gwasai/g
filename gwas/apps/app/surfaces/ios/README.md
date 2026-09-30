# GWAS iOS

Native iOS target for GWAS.

Initial architecture:

1. The user's Mac runs the personal GWAS authority and local SQLite database.
2. iOS talks to the GWAS HTTP API over a private device network.
3. The iOS client never opens the Mac SQLite database directly.
4. Private records remain person-scoped; cross-person collaboration uses explicit shared events/tasks rather than database access.
5. TestFlight is the intended family beta-distribution path once the native target is signed.

The first iOS screens should mirror the remote/PWA surface: Home, namespaces, CEO picker, Providers, and Dev Bus.
