import os
import shutil
def shell():
    sp = os.getcwd()
    pwd = os.getcwd()
    while 1:
        cmd = input(pwd + ">")
        if cmd == "exit":
            return 0
        elif cmd == "ls":
            print(os.listdir())
        elif cmd[:3] == "ls ":
            print(os.listdir(cmd[3:]))
        elif cmd == "run":
            print("run [filename]")
            print("to run a python file")
        elif cmd[:4] == "run ":
            try:
                file = open(cmd[4:])
                exec(file.read())
                print("return true")
            except:
                print("return false")
        elif cmd[:6] == "touch ":
            file = open(cmd[6:])
            file.close()
        elif cmd[:4] == "cat ":
            try:
                file = open(cmd[4:])
                print(file.read())
                file.close()
                print("return true")
            except:
                print("return false")
        elif cmd[:3] == "rm ":
            try:
                os.remove(cmd[3:])
                print("return true")
            except:
                print("return false")
        elif cmd[:7] == "rm -r ":
            try:
                shutil.rmtree(cmd[7:])
                print("return true")
            except:
                print("return false")
        else:
            print("What is \"" + cmd + "\"?")