import argparse

def block(os):

    hostsFilePath = "/etc/hosts"
    if os == "Windows":
        hostsFilePath = r"C:\Windows\System32\drivers\etc\hosts"
    else:
        if os != "macOS" and os != "Linux":
            print("ERROR: No Valid Value for the --os Flag was Supplied")
            print("USAGE: python app.py --os <macOS, Linux, or Windows>")
            exit(1)

    redirect_ip = "127.0.0.1"
    websites_block_list = ["www.facebook.com", "facebook.com"]

if __name__ == "__main__":

    argParser = argparse.ArgumentParser()
    argParser.add_argument("--os", required = True, help = "What's your Operating System: macOS, Linux, or Windows?")
    args = argParser.parse_args()

    block(args.os)
