import socket
import sys
import threading
import time

print("-" * 50)
print("Python port scanner by AUM THUMMAR")
print("-" * 50)

trgt = input("Enter Target : ")
start_port = int(input("Enter Starting port :"))
end_port = int(input("Enter Ending port :"))

start_time = time.time()

if trgt is None:
    sys.exit()

try:
    target = socket.gethostbyname(trgt)
except socket.gaierror:
    print("Warning/Error : Name resolution error")
    sys.exit()

print("Scanning target", target)


def scan_port(port):
    # print("Scanning port : ", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    conn = s.connect_ex((target, port))
    if conn == 0:
        print("Port {} is OPEN".format(port))
    s.close()


for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()

end_time = time.time()
print("Time elapsed : ", end_time - start_time, "s")
