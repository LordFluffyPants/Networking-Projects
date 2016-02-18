import select
import socket
import random
import threading


def handle_client(client_sock):
    print('client connecteded')
    random_number = random.randint(0,50000)
    print(random_number)
    client_sock.send(str(random_number)+'\n') #sends out the random number

    ready = select.select([client_sock],[],[], time_out)
    if ready[0]:
        raw_data = client_sock.recv(16)
        recieved_number = int(raw_data[:-1])
        print(recieved_number)

        if recieved_number == (random_number +1):
            out = 'SEND_NAME\n'
            client_sock.send(out)
            raw_data = client_sock.recv(512)
            name = str(raw_data[:-1])
            acknowledgement = name + str(' ACK')
            print(acknowledgement)
            client_sock.send(acknowledgement)
    client_sock.close()

#arguemnts for server
port = 3333
time_out = 10
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', port))
server_sock.listen(8)

while 1:
    (client_sock, address) = server_sock.accept()
    t = threading.Thread(name=address, target=handle_client, args=(client_sock,))
    t.start()

print('closing server')
server_sock.close()
