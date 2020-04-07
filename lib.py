import os
def shell():
    sp = os.getcwd()
    pwd = os.getcwd()
    while 1:
        cmd = input(pwd + ">")
        if cmd == "exit":
            return 0
        elif cmd == "ls":
            print(os.listdir())
        elif cmd[:2] == "ls":
            print(os.listdir(cmd[3:]))
        elif cmd == "run":
            print("run [filename]")
            print("to run a python file")
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
        elif cmd[:3] == "cat":
            try:
                file = open(cmd[4:])
                print(file.read())
                file.close()
                print("return true")
            except:
                print("return false")
        elif cmd[:2] == "rm":
            try:
                os.remove(cmd[3:])
                print("return true")
            except:
                print("return false")
        else:
            print("What is \"" + cmd + "\"?")