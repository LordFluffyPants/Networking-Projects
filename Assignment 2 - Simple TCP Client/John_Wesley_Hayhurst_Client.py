import socket
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(enigma.pcs.cnu.edu,3223)
try:
    number_rec = socket.recv()
    print number_rec
    number_send = int(number_rec) + 1
    socket.sendall(number_send)
    print socket.recv()
    if socket.recv() == "SEND_NAME":
        socket.sendall("John Wesley McDonald Hayhurst")
finally:
    socket.close()
