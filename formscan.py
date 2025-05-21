import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import colorama

colorama.init()
from colorama import Fore

def load_payloads(file_path='payloads.txt'):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def get_forms(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {
        "action": form.attrs.get("action"),
        "method": form.attrs.get("method", "get").lower(),
        "inputs": []
    }
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        if input_name:
            details["inputs"].append({"type": input_type, "name": input_name})
    return details

def submit_form(form_details, url, payload):
    target_url = urljoin(url, form_details["action"])
    data = {}
    for input in form_details["inputs"]:
        if input["type"] == "text":
            data[input["name"]] = payload
        else:
            data[input["name"]] = "test"
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    return requests.get(target_url, params=data)

def scan_xss(url):
    forms = get_forms(url)
    print(f"[+] Detected {len(forms)} form(s) on {url}")
    payloads = load_payloads()

    for i, form in enumerate(forms, start=1):
        form_details = get_form_details(form)
        for payload in payloads:
            response = submit_form(form_details, url, payload)
            if payload in response.text:
                print(Fore.RED + f"[!] XSS vulnerability detected!")
                print(Fore.YELLOW + f"    Form #{i} | Payload: {payload}")
                print(Fore.CYAN + f"    Action: {form_details['action']} | Method: {form_details['method']}")
                break
        else:
            print(Fore.GREEN + f"[+] Form #{i} seems secure.")
    print(Fore.RESET)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="FormScan - XSS Form Scanner")
    parser.add_argument("--url", required=True, help="Target URL to scan")
    args = parser.parse_args()

    print(Fore.BLUE + "[*] Starting FormScan on:", args.url)
    scan_xss(args.url)
