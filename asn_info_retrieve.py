# installed DNSPython 1.16
# installed requests
# installed IPWhois

import csv
import json
import sys
import requests
from ipwhois import IPWhois

# Setup Variables
infile = "hosts.txt"
outfile = open("output.txt", 'a+')
hosts = open(infile, 'r')
lines = hosts.readline()
url = "https://www.arin.net/"
extension = ".txt"

# while loop to create URL for ARIN lookup
while lines:
    # Strip the line-feed from reading the lines in the file
    lines = lines.strip('\n')
    print("IP: " + lines)  # Print the variable above
    # Use the IPWhois to look at the line read from the file
    obj = IPWhois(lines)
    res = obj.lookup_rdap()  # Retrieve the data on the IP using RDAP
 #   print(res) # Prints a dump of the res variable
 #   print("ASN:", res['asn'])  # Print select JSON fields
    asn_info = "ASN: " + res['asn'] + '\n' + "CIDR: " + \
        res['asn_cidr'] + '\n'
    country_info = "Country: " + res['asn_country_code']
    print(asn_info + country_info)
    print('\n')
#    filewrite = json.dumps(res, indent=4)
#    outfile.write(filewrite)
    lines = hosts.readline()  # read the next line, rinse and repeat
hosts.close()
outfile.close()
