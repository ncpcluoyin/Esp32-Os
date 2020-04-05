print("Esp32 Os v0.1")
try:
    import lib
    lib.shell()
except:
    print("lib.py not found!")
    exit()