"""Core orchestration for ReconRadar"""
from .subdomains import enum_subdomains_crtsh
from .portscan import port_scan_host
from .report import render_html_report
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict

def parse_ports(ports_str: str) -> List[int]:
    ports = set()
    for part in ports_str.split(','):
        if '-' in part:
            a, b = part.split('-', 1)
            ports.update(range(int(a), int(b) + 1))
        else:
            ports.add(int(part))
    return sorted(ports)

def enum_subdomains(domain: str) -> List[str]:
    return enum_subdomains_crtsh(domain)

def port_scan_many(hosts: List[str], ports: List[int], timeout: int = 2, max_workers: int = 200):
    results = {}
    tasks = []
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        for host in hosts:
            tasks.append(ex.submit(_scan_host_task, host, ports, timeout))
        for fut in as_completed(tasks):
            host, open_ports = fut.result()
            results[host] = open_ports
    return results

def _scan_host_task(host: str, ports: List[int], timeout: int):
    open_ports = []
    for p in ports:
        if port_scan_host(host, p, timeout=timeout):
            open_ports.append(p)
    return host, open_ports

def make_report(domain: str, subdomains: List[str], scan_results: Dict[str, List[int]], out_path: str):
    render_html_report(domain, subdomains, scan_results, out_path)
