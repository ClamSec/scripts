#!/usr/bin/env python3

import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)

req = requests.get("https://" + sys.argv[1])
print("\n" + str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])
print("\nThe IP address of " + sys.argv[1] + " is " + gethostby_ +"\n")

# ipinfo.io API
req_ipinfo = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
resp_ipinfo = json.loads(req_ipinfo.text)

print("Location: " + resp_ipinfo["loc"])
print("Region: " + resp_ipinfo["region"])
print("City: " + resp_ipinfo["city"])
print("Country: " + resp_ipinfo["country"])
