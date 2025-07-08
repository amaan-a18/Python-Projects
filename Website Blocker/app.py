import time
from datetime import datetime as dt
import os

# Websites to block
sites_to_block = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
    "www.gmail.com",
    "gmail.com",
]

# Path to hosts file
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect_ip = "127.0.0.1"

# Work hours (optional time check)
start_hour = 8
end_hour = 16

while True:
    current_time = dt.now()
    if start_hour <= current_time.hour < end_hour:
        print("Work hours... Blocking sites...")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for site in sites_to_block:
                if site not in content:
                    file.write(f"{redirect_ip} {site}\n")
    else:
        print("Outside work hours... Unblocking sites...")
        with open(hosts_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    file.write(line)
            file.truncate()
    time.sleep(5)
