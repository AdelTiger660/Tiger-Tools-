import argparse
from core import port_scanner

def main():
    parser = argparse.ArgumentParser(description="PyHawk - Pentest CLI Toolkit")
    parser.add_argument('--portscan', metavar='HOST', help='Scan ports on a host')

    args = parser.parse_args()

    if args.portscan:
        port_scanner.port_scanner(args.portscan)

if __name__ == "__main__":
    main()
