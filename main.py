import os
print("Esp32 Os Booter")
print("Boot from \"start.py\"")
try:
    file = open("start.py")
except:
    print("system not found")
exec(file.read())
file.close()
print("system halt")