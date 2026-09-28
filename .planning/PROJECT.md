# WorkBridge Web CI/CD probe

This repository is a synthetic integration fixture. It tests a Web-backed Codex CLI's ability to run full local CI, open and merge a GitHub PR, observe GitHub Actions, and publish the resulting static page to the Test environment. No production service is involved.

Scan root: this repository root. Source SHA and manifest are stored in `graphify-out/` after graph creation. A Test release is accepted only when the Pages URL serves the merged commit's unique marker.
