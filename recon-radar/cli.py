#!/usr/bin/env python3
"""CLI Entrypoint for ReconRadar"""
import argparse
from recon import core

def parse_args():
    p = argparse.ArgumentParser(description="ReconRadar — quick recon for bug bounty")
    p.add_argument("--domain", required=True, help="Target domain (example.com)")
    p.add_argument("--ports", default="80,443", help="Ports or ranges (e.g. 80,443,8000-8100)")
    p.add_argument("--out", default="report.html", help="HTML report output path")
    p.add_argument("--timeout", type=int, default=3, help="Socket timeout seconds")
    p.add_argument("--max-workers", type=int, default=200, help="Concurrency for port scan")
    return p.parse_args()

def main():
    args = parse_args()
    domain = args.domain
    ports = core.parse_ports(args.ports)
    print(f"[+] Starting ReconRadar for: {domain}")

    subs = core.enum_subdomains(domain)
    print(f"[+] Found {len(subs)} subdomains")

    scan_results = core.port_scan_many(subs, ports, timeout=args.timeout, max_workers=args.max_workers)
    core.make_report(domain, subs, scan_results, args.out)
    print(f"[+] Report written to {args.out}")

if __name__ == '__main__':
    main()
