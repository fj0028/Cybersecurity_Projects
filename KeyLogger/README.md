# Keylogger (Ethical Cybersecurity Project)

This is a basic keylogger developed in a **controlled lab environment** for the purpose of learning about input monitoring and endpoint security as part of a cybersecurity home lab.

> ⚠️ This tool is for **educational purposes only**. Do **not** use this outside of a private environment without **explicit permission**. Unauthorized use may be illegal.

---

## Features

- System information collection (hostname, IP, OS, processor)
- Clipboard text capture
- Screenshot capture
- Microphone recording (5 seconds by default)
- Keystroke logging (30 seconds by default)
- Email delivery of all collected data
- AES-encrypted versions of collected text logs


---
## File Structure

| File/Variable         | Description                                      |
|-----------------------|--------------------------------------------------|
| `key_log.txt`         | Logs of pressed keys                             |
| `system.txt`          | System info log                                  |
| `clipboard.txt`       | Clipboard text dump                              |
| `audio.wav`           | Microphone recording                             |
| `screenshot.png`      | Screenshot of active screen                      |
| `e_*.txt`             | Encrypted versions of logs using Fernet          |

## Email Configuration

Make sure to configure the following constants in the script:

```python
FROM_EMAIL = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TO_EMAIL = "your_email@gmail.com"
KEY = b"your_fernet_key_here"
## Environment Setup
```
---
## Encryption
- Use GenerateKey.py to generate encryption key
- Use DecryptFile.py to decrypt encrypted text files

---

### Prerequisites

- Windows 10 Virtual Machine (VirtualBox or VMware recommended)
- Python 3.10+
- Admin privileges inside the VM

### Dependencies

Install with pip:

```bash
pip install -r requirements.txt
```
---

## Usage

```bash
python GenerateKey.py
python key_logger.py
python DecryptFile.py
```
---
## Cybersecurity Relevance
- Simulates post-exploitation behavior (keylogging, data collection, exfiltration).
- Demonstrates common attacker tactics like clipboard hijacking, screen/mic spying, and system recon.
- Uses email for covert data exfiltration, mimicking real-world malware communication.
- Includes file encryption and cleanup, showing anti-forensics and data protection techniques.
- Useful for red team training and malware analysis, helping defenders understand and detect malicious activity.

---

## Planned Improvements
- Convert to executable

---

## Author
Created by Francis Abreu - a cybersecurity student focused on automation and blueteaming
