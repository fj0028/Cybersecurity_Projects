import requests
import argparse




#Security headers with Correct Values
sec_headers = {
    'X-Frame-Options': 'deny',
    'X-Content-Type-Options': 'nosniff',
    'Referrer-Policy': 'strict-origin-when-cross-origin',
    'Content-Security-Policy': "default-src 'none'",
    'Strict-Transport-Policy': 'max-age=31536000; includeSubDomains'
}

response = requests.get("https://api.github.com")
headers = response.headers

#Checks if security header is in HTTP response headers
for hdr in sec_headers:
    if hdr in headers:
        val = headers.get(hdr)
        sec_val = sec_headers.get(hdr)
        if val == sec_val:
            print('Accpetable Value')
        else:
            print('Not Acceptable')    
    else:
        print('Missing Header')

