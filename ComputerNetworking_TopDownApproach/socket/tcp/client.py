from socket import *

server_name = 'localhost'
server_port = 12001
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

msg = input('Input lowercase sentence:')
client_socket.send(msg.encode())

modified_msg = client_socket.recv(1024)
print('From server: ', modified_msg.decode())
client_socket.close()
