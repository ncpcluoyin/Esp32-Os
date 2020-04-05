print("Esp32 booter")
try:
    file = open("start.py")
    exec(file.read())
    file.close()
except:
    print("start.py not found!")
    exit()
print("system halt")