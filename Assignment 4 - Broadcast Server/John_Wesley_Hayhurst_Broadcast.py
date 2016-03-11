import socket
import select
import threading
import Queue

def handle_client(client_sock, number):
    number_string = str(number)
    print(number)
    while 1:
        ready = select.select([client_sock],[],[], 2)
        if ready[0]:
            raw_data = client_sock.recv(1024)
            if (len(raw_data) > 0):
                sending_string = 'Client ' + number_string + ': ' + str(raw_data)
                for i in range(0,client_number):
                    if (i != number-1): #put in the list to send for all other clients
                        msg_list[i].put(sending_string)
            else:
                break
        else: #send mesages
            while not(msg_list[number-1].empty()):
                msg = msg_list[number-1].get()
                client_sock.send(msg)
    client_sock.close()


#server arguments
msg_list = []
client_number = 0
port = 8642
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', port))
server_sock.listen(1024)

while 1:
    try:
        client_sock, address = server_sock.accept()
        client_number += 1
        msg_list.append(Queue.Queue(0))
        t = threading.Thread(name=address, target=handle_client, args=(client_sock,client_number))
        t.start()
    except (KeyboardInterrupt, SystemExit):
        server_sock.close()
