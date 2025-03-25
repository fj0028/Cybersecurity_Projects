import pyfiglet
import sys
import socket
import concurrent.futures
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

#User specifies target IP
target = input(str("Target IP: "))

#Banner
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

port_services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP Proxy"
}

#Banner grabbing
def grab_banner(s):
    try:
        s.settimeout(1)
        banner = s.recv(1024).decode().strip()
        return banner
    except: 
        return None



def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex((target, port))
    
    if result == 0:
        service = port_services.get(port, "Unkown Service")
        print(f"[*] Port {port} is open ({service})")
        
        if port in {21, 22, 25, 80, 110, 143, 443, 3306, 5432}:  # Services that might return banners
                banner = grab_banner(s)
                if banner:
                    print(f"    Banner: {banner}")
    s.close()

#Creates threads to scan through most common ports
def main():
     with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
          results = executor.map(scan_port, range(1,1025)) 



if __name__ == "__main__":
    try:
        main()
    
    except KeyboardInterrupt:
        print("\n Exiting")
        sys.exit()

#Errors connecting to host address
    except socket.error:
        print("\nHost not responding")
        sys.exit()
