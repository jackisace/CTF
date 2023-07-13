import requests

cookies={"PHPSESSID":"6jvu07drt755cna9mta22kaq30"}
proxies={"http":"http://127.0.0.1:8080"}
target = "http://10.102.163.104/"
lists = "big.txt,catala.txt,common.txt,euskera.txt,extensions_common.txt,indexes.txt,mutations_common.txt,small.txt,spanish.txt"
extensions = ".php,.html,.txt"

for list in lists.split(","):
    with open("/usr/share/wordlists/dirb/FILE".replace("FILE", list)) as f:
        lines = f.read().split("\n")



    for line in lines:
        for extension in extensions.split(","):
            query = "http://10.102.163.104/" + line + extension

            r = requests.get(query, cookies=cookies, proxies=proxies)
            if len(r.text) != 276:
                print(len(r.text), query)
