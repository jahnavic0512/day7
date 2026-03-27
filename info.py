import os
import socket
import datetime

print("=== SYSTEM INFO ===")
print("Time:", datetime.datetime.now())
print("Hostname:", socket.gethostname())
print("Current Files:", os.listdir())

# Optional (may give error in container sometimes)
try:
    print("User:", os.getlogin())
except:
    print("User: Not available")
