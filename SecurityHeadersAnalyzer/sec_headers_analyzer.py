import requests
import argparse

#Security headers with Correct Values
sec_headers = {
    'X-Frame-Options': 'deny',
    'X-Content-Type-Options': 'nosniff',
    'Referrer-Policy': 'strict-origin-when-cross-origin',
    'Content-Security-Policy': "default-src 'none'",
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains'
}

#Checks if security header is in HTTP response headers
def check_headers(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        print(f"\n[+] Checking headers for {url}\n")

        for hdr,expected_val in sec_headers.items():
            if hdr in headers:
                actual_val = headers.get(hdr)
                if expected_val == actual_val:
                    print(f'[+] {hdr}: OK ({actual_val})')
                else:
                    print(f'[!] {hdr}: Weak or misconfigured ({actual_val})')    
            else:
                print(f'[-] {hdr}: Missing')
    
    except requests.exceptions.RequestException as e:
        print(f'[!] Error fetching {url}: {e}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check security headers for a website")
    parser.add_argument("url", help="Target URL (e.g https://example.com)")
    args = parser.parse_args()

    check_headers(args.url)
