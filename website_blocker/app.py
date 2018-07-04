from urllib.parse import urlparse
import argparse
import requests

def block(os, websites):

    hostsFilePath = "/etc/hosts"
    if os == "Windows":
        hostsFilePath = r"C:\Windows\System32\drivers\etc\hosts"
    else:
        if os != "macOS" and os != "Linux":
            print("ERROR: No Valid Value for the --os Flag was Supplied!")
            print("USAGE: python app.py --os <macOS, Linux, or Windows>")
            exit(1)

    try:

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

    except requests.exceptions.MissingSchema:
        print("ERROR: Invalid URL! No Schema Supplied!")
    except requests.exceptions.ConnectionError:
        print("ERROR: Website doesn't Exist!")

    redirect_ip = "127.0.0.1"

if __name__ == "__main__":

    argParser = argparse.ArgumentParser()
    argParser.add_argument("--os", required = True, help = "What's your Operating System: macOS, Linux, or Windows?")
    argParser.add_argument("--websites", nargs='+', required = True, help = "List the URLs of the Websites you wish to Block.")
    args = argParser.parse_args()

    block(args.os, args.websites)
