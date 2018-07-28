# Website Blocker Application

# Blocks Given Website(s) from Given Start Time until Given End Time
# Gives Users Flexibility because it Depends on User Input

# Import Modules
import argparse
import requests
from urllib.parse import urlparse
import time
from datetime import datetime as dt
import sys
import socket



# Block Given Website(s) from Given Start Time until Given End Time
# Handle Invalid User Input
def block(os, redirect_site, websites, start_time, end_time):



    # Path to "Hosts" File (Enables Website Blocking)
    # Path differs between macOS/Linux and Windows
    # User Expected to Enter Current Operating System
    hostsFilePath = "/etc/hosts"
    if os == "Windows":
        hostsFilePath = r"C:\Windows\System32\drivers\etc\hosts"
    else:
        if os != "macOS" and os != "Linux":
            print("ERROR: No Valid Value for the --os Flag was Supplied!")
            print("USAGE: python app.py --os <macOS, Linux, or Windows> --redirect_site <URL> --websites <URL-1> <Optional: URL-2> <...> --start_time <Hour: 0 - 23> <Minute: 0 - 59> --end_time <Hour: 0 - 23> <Minute: 0 - 59>")
            exit(1)



    try:



        # Check if Given Website to Redirect to when Accessing Target Website is Valid
        # Exception ConnectionError Generated if not Valid
        request = requests.get(redirect_site)

        # Convert Given Website to Redirect to when Accessing Target Website to an IP Address
        urlParser = urlparse(redirect_site)
        hostname = urlParser.netloc
        redirect_ip = socket.gethostbyname(hostname)



        # Collect Given Website(s) to Block in a List
        # Store Two Versions for Each Target Website:
        # First Version without "www."
        # Second Version with "www."
        websites_block_list = []

        for website in websites:

            request = requests.get(website)
        
            urlParser = urlparse(website)
            hostname = urlParser.netloc
            websites_block_list.append(hostname)
            if hostname.startswith("www."):
                websites_block_list.append(hostname[4:])
            else:
                websites_block_list.append("www." + hostname)



        # Infinite Loop
        while True:

            # If the Current Time is between Given Start and End Times
            if dt(dt.now().year, dt.now().month, dt.now().day, int(start_time[0]), int(start_time[1])) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, int(end_time[0]), int(end_time[1])):

                # Add Target Website and IP Address to Redirect to in "Hosts" File if not Already there
                print("Work Hours...")
                with open(hostsFilePath, "r+") as file:
                    content = file.read()
                    for website in websites_block_list:
                        if website not in content:
                            file.write(redirect_ip + " " + website + "\n")

            # The Current Time is not between Given Start and End Times
            else:

                # Remove Target Website and IP Address to Redirect to from "Hosts" File if there
                print("Fun Hours...")
                with open(hostsFilePath, "r+") as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in websites_block_list):
                            file.write(line)
                    file.truncate()

            # Sleep Application for 5 Seconds to Prevent Crashes from Infinite Loop
            time.sleep(5)

            # Flush Standard Out from Continuous print() Calls
            sys.stdout.flush()



    # Handle Invalid User Input
    except requests.exceptions.MissingSchema:
        print("ERROR: Invalid URL! No Schema Supplied!")
    except requests.exceptions.ConnectionError:
        print("ERROR: Website doesn't Exist!")
    except ValueError:
        print("ERROR: Start Time and End Time: Hours must be between 0 and 23, Minutes must be between 0 and 59!")



# main() Function
# Handle User Input
# Pass User Input to block() Function
if __name__ == "__main__":

    # Handle User Input
    argParser = argparse.ArgumentParser()
    argParser.add_argument("--os", required = True, help = "What's your Operating System: macOS, Linux, or Windows?")
    argParser.add_argument("--redirect_site", required = True, help = "Enter the URL you wish to Redirect to.")
    argParser.add_argument("--websites", nargs='+', required = True, help = "List the URLs of the Websites you wish to Block.")
    argParser.add_argument("--start_time", nargs='+', required = True, help = "Time (Hour (Format: 0 - 23) and Minute (0 - 59)) to Initiate Website Blocking.")
    argParser.add_argument("--end_time", nargs='+', required = True, help = "TIme (Hour (Format: 0 - 23) and Minute (0 - 59)) to Terminate Website Blocking.")
    args = argParser.parse_args()

    # Pass User Input to block() Function
    block(args.os, args.redirect_site, args.websites, args.start_time, args.end_time)
