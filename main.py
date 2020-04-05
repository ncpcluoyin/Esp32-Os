import os
print("Esp32 Os Booter")
print("Boot from \"start.py\"")
try:
    file = open("start.py")
    exec(file.read())
    file.close()
except:
    exit()
print("system halt")