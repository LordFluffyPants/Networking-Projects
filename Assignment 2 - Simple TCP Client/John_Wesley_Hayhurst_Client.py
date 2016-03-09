import socket
import time
import sys
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('127.0.0.1',4444))
try:
    number_rec = socket.recv(16)
    number_send = str(int(number_rec) + 1)+"\n"
    socket.send(number_send)
    dummy = socket.recv(16)
    socket.send("John Wesley McDonald Hayhurst\n")
finally:
    time.sleep(10)
    socket.close()
