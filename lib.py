import os
def shell():
    sp = os.getcwd()
    print("Esp32 Os shell v0.1")
    pwd = os.getcwd()
    while 1:
        cmd = input(pwd + ">")
        if cmd == "exit":
            return 0
        elif cmd[:3] == "run":
            try:
                file = open(cmd[4:])
                exec(file.read())
                print("return true")
            except:
                print("return false")
        elif cmd[:5] == "touch":
            file = open(cmd[5:])
            file.close()
        else:
            print("What is \"" + cmd + "\"?")