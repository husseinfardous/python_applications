import argparse

import requests
from urllib.parse import urlparse

import time
from datetime import datetime as dt

import sys

import socket

def block(os, redirect_site, websites, start_time, end_time):

    hostsFilePath = "/etc/hosts"
    if os == "Windows":
        hostsFilePath = r"C:\Windows\System32\drivers\etc\hosts"
    else:
        if os != "macOS" and os != "Linux":
            print("ERROR: No Valid Value for the --os Flag was Supplied!")
            print("USAGE: python app.py --os <macOS, Linux, or Windows> --redirect_site <URL> --websites <URL-1> <Optional: URL-2> <...> --start_time <Hour: 0 - 23> <Minute: 0 - 59> --end_time <Hour: 0 - 23> <Minute: 0 - 59>")
            exit(1)

    try:

        request = requests.get(redirect_site)

        urlParser = urlparse(redirect_site)
        hostname = urlParser.netloc
        redirect_ip = socket.gethostbyname(hostname)

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

        while True:

            if dt(dt.now().year, dt.now().month, dt.now().day, int(start_time[0]), int(start_time[1])) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, int(end_time[0]), int(end_time[1])):

                print("Work Hours...")
                with open(hostsFilePath, "r+") as file:
                    content = file.read()
                    for website in websites_block_list:
                        if website not in content:
                            file.write(redirect_ip + " " + website + "\n")

            else:

                print("Fun Hours...")
                with open(hostsFilePath, "r+") as file:
                    content = file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in websites_block_list):
                            file.write(line)
                    file.truncate()

            time.sleep(5)
            sys.stdout.flush()

    except requests.exceptions.MissingSchema:
        print("ERROR: Invalid URL! No Schema Supplied!")
    except requests.exceptions.ConnectionError:
        print("ERROR: Website doesn't Exist!")
    except ValueError:
        print("ERROR: Start Time and End Time: Hours must be between 0 and 23, Minutes must be between 0 and 59!")

if __name__ == "__main__":

    argParser = argparse.ArgumentParser()
    argParser.add_argument("--os", required = True, help = "What's your Operating System: macOS, Linux, or Windows?")
    argParser.add_argument("--redirect_site", required = True, help = "Enter the URL you wish to Redirect to.")
    argParser.add_argument("--websites", nargs='+', required = True, help = "List the URLs of the Websites you wish to Block.")
    argParser.add_argument("--start_time", nargs='+', required = True, help = "Time (Hour (Format: 0 - 23) and Minute (0 - 59)) to Initiate Website Blocking.")
    argParser.add_argument("--end_time", nargs='+', required = True, help = "TIme (Hour (Format: 0 - 23) and Minute (0 - 59)) to Terminate Website Blocking.")
    args = argParser.parse_args()

    block(args.os, args.redirect_site, args.websites, args.start_time, args.end_time)
