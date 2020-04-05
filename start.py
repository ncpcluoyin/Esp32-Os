print("Starting Esp32 Os...")
print("Esp32 Os 0.1")
print("running init.py")
try:
    import init
except:
    print("error!file not found!")
    return
print("starting shell...")
try:
    import shell
except:
    print("error!file not found!")
    return