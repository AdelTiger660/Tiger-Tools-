import requests
import threading

def check_subdomain(domain, subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=2)
        print(f"[+] Found: {url} - Status: {response.status_code}")
    except requests.RequestException:
        pass

def subdomain_finder(domain, wordlist_path="wordlists/common_subdomains.txt", threads=50):
    print(f"[*] Starting subdomain scan on: {domain}")
    with open(wordlist_path, 'r') as f:
        subdomains = [line.strip() for line in f.readlines()]

    thread_list = []
    for sub in subdomains:
        t = threading.Thread(target=check_subdomain, args=(domain, sub))
        t.start()
        thread_list.append(t)
        if len(thread_list) >= threads:
            for thread in thread_list:
                thread.join()
            thread_list = []
