#!/bin/env bash

whois -h whois.arin.net $1 > whois-$1.txt
