import sys
import requests
import json

try:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    content =response.json()
    s=content["data"]
    y=float(s['priceUsd'])



except requests.RequestException:
    sys.exit()


try:
    n = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
print(f"${n * y:,.4f}")

