print("Starting Esp32 Os...")
print("Esp32 Os 0.1")
print("running init.py")
try:
    file = open("init.py")
    exec(file.read())
    print("OK")
except:
    print("error!file not found!")
    return
print("starting shell...")
try:
    file = open("shell.py")
    exec(file.read())
except:
    print("error!file not found!")
    return