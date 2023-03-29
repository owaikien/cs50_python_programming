import re
import sys

def main():
    print(validate(input("IPv4 Address:")))

def validate(ip):
    if re.match(r"^\d+\.\d+\.\d+\.\d+$", ip):
        octets = ip.split(".")
        for octet in octets:
            if int(octet) > 255:
                return False
        return True
    
main()