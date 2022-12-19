from socket import *

server_name = 'localhost'
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)

msg = input('Input lowercase sentence:')
client_socket.sendto(msg.encode(),
                     (server_name, server_port))

modified_msg, server_address = client_socket.recvfrom(2048)
print(modified_msg.decode())
client_socket.close()
