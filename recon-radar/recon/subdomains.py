"""Subdomain enumeration helpers
- Uses crt.sh JSON output as a simple, legal OSINT source
"""
import requests
from typing import List

def enum_subdomains_crtsh(domain: str) -> List[str]:
    """Query crt.sh for certificates and extract common names.

    Note: crt.sh is a public OSINT service. Respect rate limits and caching.
    """
    q = f"%.{domain}"
    url = f"https://crt.sh/?q={q}&output=json"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            return [domain]
        data = resp.json()
    except Exception:
        # fallback: return the root domain
        return [domain]

    subs = set()
    for entry in data:
        name = entry.get('name_value') or entry.get('common_name')
        if not name:
            continue
        for n in name.split('\n'):
            n = n.strip().lower()
            if n.endswith(domain):
                subs.add(n)
    # ensure root domain included
    subs.add(domain)
    return sorted(subs)
