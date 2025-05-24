# Port Scanner

A multithreaded TCP port scanner that can scan a range of ports on a specified IP

---

## Features
- Uses Pythons's `socket` and `threading` modules
- Supports multithreading for faster scanning
- Identifies open ports and common services

---

## Requirements
- Python 3.x

```bash
python portscanner.py
```

---

## Architecture Overview

### Main Components:
- socket: Used to create TCP connections and test if a port is open
- threading: Each port scan runs in a separate thread for speed
- main(): Gathers input and controls the scanning loop and thread spawning

### Execution Flow:
1. User inputs a target IP
2. The main thread loops through a range of ports
3. A new thread is started for each port using the `scan_port()` function
4. Each thread attempts a TCP connection
5. If the port is open, it prints a message

![PortScannerUse](https://github.com/user-attachments/assets/3cf4b51a-faa1-4245-a0d8-4d318df2ab1b)

>[!NOTE]
>This tool is inteded for educational purposes only. Only scan networsk you own or have explicit permission to test

---

## Cybersecurity Relevance
Port scanning is a foundational skill in network reconnaissance, the first phase of most penetration tests
and read team operations. This project helps demonstrate:

- Enumaration: Identifying open TCP ports to discover services running on a host
- Threat Modeling: Recognizing which services are publicly accessible and could be entry points for exploitation
- Real-World Tools Comaprison: Mimics the behavior of tools like nmap giving insight into how they work
- Automation: Highlights how multithreading increases scan performance

