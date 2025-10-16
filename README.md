# ReconRadar

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Build](https://img.shields.io/github/actions/workflow/status/<your-username>/recon-radar/ci.yml?branch=master)](https://github.com/<your-username>/recon-radar/actions)
[![Docker Pulls](https://img.shields.io/docker/pulls/<your-username>/recon-radar)](https://hub.docker.com/)
[![Stars](https://img.shields.io/github/stars/<your-username>/recon-radar?style=social)](https://github.com/<your-username>/recon-radar/stargazers)

> **ReconRadar — Automated Reconnaissance & Reporting**  
> Fast, modular reconnaissance toolkit built for Bug Bounty hunters, red teams, and OSINT workflows.

---

## What is ReconRadar?

ReconRadar automates the annoying, repetitive parts of reconnaissance: subdomain enumeration, concurrent port scanning, and clear HTML reporting.  
Designed to be **lightweight**, **extensible**, and **CI-friendly**, ReconRadar gives you a reproducible starting point to build more advanced tooling and integrations (Burp, dashboards, or pipelines).

---

## Key Features

- Subdomain enumeration using `crt.sh` (public certificates)
- Concurrent asynchronous port scanning (custom ranges)
- HTML report export with summaries and severity highlights
- One-line Docker run (Dockerfile included)
- CI template for automated runs (GitHub Actions)
- Plugin-friendly architecture — add modules for Burp, scanners, or exporters

---

## 🛠️ Why this project belongs in your GitHub

- Demonstrates **OSINT + scanning** fundamentals for Bug Bounty programs  
- Clean, testable structure that recruiters and collaborators can quickly inspect  
- Easy to fork and extend (plugins, dashboards, integrations)

---

## Quickstart

```bash
# clone your fork
git clone https://github.com/<your-username>/recon-radar.git
cd recon-radar

# create & activate a virtualenv
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# basic run (ports can be single, comma-separated, or ranges)
python cli.py --domain example.com --ports 80,443,8000-8100 --out report.html
```

---

## Example CLI

```
$ python cli.py --domain example.com --ports 80,443,8000-8100 --out report.html --timeout 3 --concurrency 200
[+] Enumerating subdomains via crt.sh...
[+] Found 128 subdomains
[+] Starting concurrent port scan (200 workers)
[✓] 37 hosts with open ports
[+] Generating colorized HTML report -> report.html
```

---

## Docker

Run quickly in Docker (no Python env setup required):

```bash
# build
docker build -t recon-radar:latest .

# run
docker run --rm -v $(pwd):/work recon-radar:latest --domain example.com --ports 80,443 --out /work/report.html
```

---

## CI / GitHub Actions

A lightweight workflow is provided in `.github/workflows/ci.yml` to run tests and produce artifacts. Example job steps:

- checkout
- set up Python 3.10
- install deps
- run linting & tests
- (optional) run a minimal, non-network reconnaissance against a canned input and upload `report.html` as an artifact

> **Important:** CI should **never** run aggressive scans against third-party domains. Use mocked responses or an allowlist.

---

## Security & Safe-Use Notice

ReconRadar can actively scan networks — only run it against domains you own or have written permission to test. Misuse may violate laws and program terms. Always:

- Obtain explicit permission
- Follow responsible disclosure
- Rate-limit scans to avoid service disruption

---

## Extending ReconRadar

- Add new discovery modules (Shodan, AlienVault, passive DNS)
- Implement HTTP service fingerprinting & banner grabbing
- Integrate with Burp or an internal dashboard
- Add JSON/CSV exporters and a REST API for orchestration

---

## Contributing

Contributions welcome! Follow these guidelines:

1. Fork the repo and create a feature branch: `git checkout -b feat/my-feature`
2. Commit with clear messages: `feat: add xyz`, `fix: correct abc`, `chore: update deps`
3. Run linters and tests before PR
4. Open a PR describing the change and the security impact

See `CONTRIBUTING.md` for more details.

---

## Suggested commit messages (examples)

```text
feat: add crt.sh subdomain enumerator
fix: handle timeouts during concurrent port scanning
docs: update README with Docker usage
chore: bump aiohttp to 3.x
```

---

## Sample report (what to expect)

- Summary table of subdomains and open ports
- Individual host sections with HTTP probes and quick notes
- Filters for severity and export button
- Timestamped run metadata and CLI options used

(See `samples/report.html` for a preview in the repo.)

---

## License

MIT License — see `LICENSE` for full text.

---

## Credits & Contacts

- Author: **Your Name** / `@your-handle`
- Maintainers: Open for collaborators — open issues or PRs
- Found a bug? File it under: `https://github.com/<your-username>/recon-radar/issues`

---

## Final Notes (Hacker + Professional blend)

ReconRadar is designed to *look sharp in a CV* and *perform reliably in a pipeline*. Keep scans ethical, commit clearly, and make your README the first strong impression on reviewers.

---
