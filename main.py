import os
print("Esp32 Os Booter")
print("Boot from \"start.py\"")
try:
    import start
except:
    print("system not found")
print("system halt")