#!/bin/env python3

import requests

r = requests.get("http://whois.arin.net/rest/")

if __name__ == "__main__":
    print("You tried")