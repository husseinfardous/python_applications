# Website Blocker Application

# Blocks Websites from 8:00 AM until 4:00 PM
# Can be Scheduled by Windows to Run Automatically on Boot Up

# Import Modules
import time
from datetime import datetime as dt
import sys



# Path to "Hosts" File (Enables Website Blocking)
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# IP Address to Redirect User to when Accessing Target Website
redirect = "127.0.0.1"

# Target Website(s) to Block
website_list = ["www.chess.com", "chess.com"]



# Infinite Loop
while True:

    # If the Current Time is between 8:00 AM and 4:00 PM
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):

        # Add Target Website and IP Address to Redirect to in "Hosts" File if not Already there
        print("Work Hours...")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(redirect + " " + website + "\n")

    # The Current Time is not between 8:00 AM and 4:00 PM
    else:

        # Remove Target Website and IP Address to Redirect to from "Hosts" File if there
        print("Fun Hours...")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    # Sleep Application for 5 Seconds to Prevent Crashes from Infinite Loop
    time.sleep(5)

    # Flush Standard Out from Continuous print() Calls 
    sys.stdout.flush()
