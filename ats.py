#!/bin/env python3

import os
import sys


# provide domain
def get_domain():
    try:
        search_domain = sys.argv[1]
    except:
        search_domain = input("Enter domain to ennumerate: ")
    
    return search_domain

# get initial details about domain
def collect_data():
    set_domain = get_domain()
    os.system(f"whois {set_domain} > whois-{set_domain}.txt")
    pass



if __name__ == "__main__":
    collect_data()