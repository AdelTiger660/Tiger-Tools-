import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((target, port))
            print(f"[+] Port {port} is open")
    except:
        pass

def port_scanner(target, ports=range(1, 1025), threads=100):
    print(f"[*] Scanning {target}...")
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in ports:
            executor.submit(scan_port, target, port)
