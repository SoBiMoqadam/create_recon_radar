"""Simple TCP port scanner (blocking sockets)"""
import socket

def port_scan_host(host: str, port: int, timeout: int = 2) -> bool:
    try:
        # prefer numeric IP lookups
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        sock.close()
        return True
    except Exception:
        return False
