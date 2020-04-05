print("Esp32 Os v0.1")
try:
    import lib
    lib.shell()
except:
    print("system quit")
    exit()