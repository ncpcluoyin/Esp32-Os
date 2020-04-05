import os
def shell():
    print("Esp32 shell 0.1 for Esp32 Os 0.1")
    sp = os.getcwd()
    while true:
        pwd = os.getcwd()
        print(pwd + ">>")
        input()