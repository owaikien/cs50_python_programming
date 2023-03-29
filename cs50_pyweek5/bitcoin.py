import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try: 
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    price = o["bpi"]["USD"]["rate_float"]
    total = price * float(sys.argv[1])
    print (f"{total:,.4f}")
except requests.RequestException:
    sys.exit()
except ValueError:
    sys.exit("Command-line is not a number")