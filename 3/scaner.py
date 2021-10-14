import socket
import threading

ports = []
for i in range (0, 10000):
    ports.append(0)
def open (port):
    sock = socket.socket()
    try:
        sock.connect(('127.0.0.1', port))
    except:
        print(port, 'dose not opened')
        sock.close()
    else:
        ports[port] = 1
        print (port, 'opened')
        sock.close()


t = [threading.Thread(target=open, args=[i]) for i in range(2999, 3002)]
[t1.start() for t1 in t]
[t1.join() for t1 in t]
for i in range (0, 10000):
    if ports[i] != 0:
        print ("Port ", i, "opened")