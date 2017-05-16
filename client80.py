# Echo client program
import socket, thread

HOST = "192.168.0.123"    # The remote host
PORT = 80              # The same port as used by the server
message="""GET / http/1.1
host: 192.168.0.123"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def posielaj(s):
    while 1:
        s.sendall(message)

thread.start_new_thread(posielaj, (s,))
    
while 1:
    data = s.recv(1024)
    print data

s.close()
