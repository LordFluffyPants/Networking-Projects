import socket
import sys
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('enigma.pcs.cnu.edu',3223))
try:
    number_rec = socket.recv(16)
    number_send = str(int(number_rec) + 1)+"\n"
    socket.send(number_send)
    socket.send("John Wesley McDonald Hayhurst\n")
finally:
    socket.close()
