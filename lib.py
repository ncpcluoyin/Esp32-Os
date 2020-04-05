import os
def shell():
    sp = os.getcwd()
    print("Esp32 Os shell v0.1")
    pwd = os.getcwd()
    while 1:
        cmd = input(pwd + ">")