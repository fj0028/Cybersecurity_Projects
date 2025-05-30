# Security Headers Analyzer

This tool checkas for missing or weak website headers such as CSP and Strict-Transport-Policy to mitigate attacks such as XSS, clickjacking, and data leaks - common things a blue teamer would look for

---

## Features

- Supports both **single URL** and **batch URL scanning** (via file input)
- Checks for industry-recommended **security headers**:
  - `X-Frame-Options`
  - `X-Content-Type-Options`
  - `Referrer-Policy`
  - `Content-Security-Policy`
  - `Strict-Transport-Security`
- Detects:
  - Missing headers
  - Present headers with **insecure values**
  - Present headers with **secure values**
- Optional **output to a text file**
- Multithreaded scanning for improved performance on bulk scans
- Built with a clean command-line interface using `argparse`

---

## Requirements

- Python 3.7+
- `requests`
- `colorama`

Install dependencies with:
```bash
pip install -r requirements.txt
```

--- 

## Usage

Single URL:
```bash
python sec_headers_analyzer.py --url https://example.com
```
File of URLs:
```bash
python sec_headers_analyzer.py --file urls.txt
```
Save Results to File:
```bash
python sec_headers_analyzer.py --file urls.txt --output results.txt
```

Example Output
```bash
[+] Checking headers for https://example.com

[+] X-Frame-Options: Acceptable (DENY)
[!] Referrer-Policy: Not Acceptable (origin-when-cross-origin)
[-] Content-Security-Policy: Missing
```
---

## Cybersecurity Relevance

These HTTP headers protect against:
- Cross-site scripting (XSS)
- Clickjacking
- MIME attacks
- Information leakage through referrers

Regularly checking them is a common blue team practice

--- 

## Planned Improvements

- Add support for more headers
- Export results to JSON or CSV
- Integration with SIEM

## Author
Created by Francis Abreu - a cybersecurity student focused on automation and blueteaming



