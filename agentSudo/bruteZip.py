import os

cmd = "7z e cutie.png -y -p PASSWORD > /dev/null 2> /dev/null"


passwords = ""
with open("/usr/share/wordlists/rockyou.txt") as f:
    #passwords = f.readlines()
    while True:
        password = f.readline()
        print("\n\n\n" + password)
        os.system(cmd.replace("PASSWORD", password))
        with open("To_agentR.txt") as ff:
            output = ff.read()
            if len(output) > 2:
                with open("OUTPUT.txt") as fff:
                    fff.write(output)
                quit()
