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
            file = open(cmd[6:],"w")
            file.close()
        elif cmd[:4] == "cat ":
            try:
                file = open(cmd[4:])
                print(file.read())
                file.close()
                print("return true")
            except:
                print("return false")
        elif cmd[:6] == "rm -r ":
            try:
                shutil.rmtree(cmd[6:])
                print("return true")
            except:
                print("return false")
        elif cmd[:3] == "rm " and cmd[:6] != "rm -r ":
            try:
                os.remove(cmd[3:])
                print("return true")
            except:
                print("return false")
        elif cmd[:6] == "mkdir ":
            os.mkdir(cmd[6:])
        elif cmd == "":
            continue
        elif cmd[:6] == "mkdir ":
            os.mkdir(cmd[6:])
        elif cmd[:5] == "edit ":
            print("press \"quit\" to exit")
            lines = 1
            line = ""
            text = ""
            while 1:
                line = input(str(lines) + "#")
                if line == "quit":
                    break
                if lines == 1:
                    text = line
                    lines = lines + 1
                    continue
                text = text + "\n" + line
                lines = lines + 1
            filename = cmd[5:]
            file = open(filename,"w")
            file.write(text)
            file.close()
        elif cmd[:3] == "cd ":
            try:
                os.chdir(cmd[3:])
                print("return true")
            except:
                print("return false")
        else:
            print("What is \"" + cmd + "\"?")