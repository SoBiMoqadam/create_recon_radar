# ReconRadar

Automated Recon & Reporting tool for Bug Bounty hunters.

**Built with:** Python 3.10+, aiohttp/requests, simple port scanner.

## Features
- Subdomain enumeration using crt.sh
- Basic port scanning (concurrent)
- HTML report export
- Dockerfile for one-line run
- CI template (GitHub Actions)

## Quickstart

```bash
# clone your fork
git clone https://github.com/<your-username>/recon-radar.git
cd recon-radar
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run recon
python cli.py --domain example.com --ports 80,443,8000-8100 --out report.html
```

## Why this project in your GitHub?
- Shows practical bug-bounty skills (OSINT + scanning)
- Clean structure and tests-friendly layout
- Easy to extend with plugins, Burp integration or dashboard

## Contribution
- Follow `CONTRIBUTING.md` style if you add features
- Keep network access explicit and safe

## License
MIT
