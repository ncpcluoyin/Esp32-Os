import os
print("Esp32 Os Booter")
print("Boot from \"start.py\"")
try:
    file = open("start.py")
    exec(file.read())
except:
    print("system not found")
file.close()
print("system halt")