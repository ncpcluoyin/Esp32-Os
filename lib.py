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
        else:
            print("What is \"" + cmd + "\"?")