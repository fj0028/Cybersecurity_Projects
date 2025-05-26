import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
import colorama 
from colorama import Fore
colorama.init(autoreset=True)

#Security headers with Correct Values
sec_headers = {
    'X-Frame-Options': ['deny', 'sameorigin'],
    'X-Content-Type-Options': ['nosniff'],
    'Referrer-Policy': ['no-referrer', 'strict-origin-when-cross-origin', 'same-origin'],
    'Content-Security-Policy': ["default-src 'none'"], #Very strict, can expand later
    'Strict-Transport-Security': ['max-age=31536000; includeSubDomains']
}

#Checks if security header is in HTTP response headers
def check_headers(url, output=None):
    try:
        if not url.startswith("http"):
            url = "https://" + url
        
        response = requests.get(url, timeout=5, allow_redirects=True)
        headers = response.headers

        print(f"\n[+] Checking headers for {url}\n")
        report = [f"Results for {url}:\n"]

        for hdr,expected_vals in sec_headers.items():
            if hdr in headers:
                actual_val = headers.get(hdr)
                # List comprehension to check if actual value is in list of expected values
                if any(expected.lower() in actual_val.lower() for expected in expected_vals): 
                    print(f'{Fore.GREEN}[+]{Fore.RESET} {hdr}: Acceptable ({actual_val})')
                    report.append(f'[+] {hdr}: Acceptable ({actual_val})')
                else:
                    print(f'{Fore.YELLOW}[!]{Fore.RESET} {hdr}: Not Acceptable ({actual_val})')    
                    report.append(f'[!] {hdr}: Not Acceptable ({actual_val})')    
            else:
                print(f'{Fore.RED}[-]{Fore.RESET} {hdr}: Missing')
                report.append(f'[-] {hdr}: Missing')
        
        report.append("\n")
        
        if output:
            with open(output, 'a') as f:
                for line in report:
                    f.write(line + '\n')
    
    except requests.exceptions.RequestException as e:
        print(f'[!] Error fetching {url}: {e}')
        if output:
            with open(output, 'a') as f:
                f.write(f'Error fetching {url}: {e}\n\n')

def main(urls, output=None):
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(lambda url: check_headers(url, output), urls)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check security headers for a website")
    parser.add_argument("--url", help="Target URL (e.g https://example.com)")
    parser.add_argument("--file", help="File with list of target URLs")
    parser.add_argument("--output", help="Save resutls to a text file")
    args = parser.parse_args()

    if not args.url and not args.file:
        parser.error("You must provide either --url or --file")
    
    if args.url:
        check_headers(args.url, args.output)
    
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
                main(urls, args.output)
       
        except FileExistsError:
            print(f"[!] Could not open file {args.file}")
