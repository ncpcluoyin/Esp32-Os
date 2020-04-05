import os
print("Esp32 Os Booter")
print("Boot from \"start.py\")
file = open("start.py")
exec(file.read())
file.close()
print("system halt")