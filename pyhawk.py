import argparse
from core import port_scanner
from core import subdomain_finder
def main():
    parser = argparse.ArgumentParser(description="PyHawk - Pentest CLI Toolkit")
    parser.add_argument('--portscan', metavar='HOST', help='Scan ports on a host')
    parser.add_argument('--subdomains', metavar='DOMAIN', help='Find subdomains for a domain')
    args = parser.parse_args()

    if args.portscan:
        port_scanner.port_scanner(args.portscan)

if __name__ == "__main__":
    main()
if args.subdomains:
   
