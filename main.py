print("Esp32 booter")
try:
    file = open("start.py")
    exec(file.read())
    file.close()
    print("ok!")
except:
    print("error!")
print("system halt")