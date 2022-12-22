import os
from os.path import exists
from socket import *

SERVER_HOST = '0.0.0.0'
server_port = 8081
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, server_port))
server_socket.listen(1)
print('Listening on port %s ...' % server_port)


def has_file(filename: str):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    if exists(dir_path+filename):
        return True
    return False


while True:
    connection_socket, addr = server_socket.accept()

    request = connection_socket.recv(1024).decode()
    print(request)

    filename = request.split('\r\n')[0].split(' ')[1]
    print(filename)

    if has_file(filename):
        response_first_line = 'HTTP/1.0 200 OK\n\n'
        with open(os.path.dirname(os.path.realpath(__file__)) +
                  filename, "rb") as f:
            bytes_read = f.read(4096)
            connection_socket.sendall(
                response_first_line.encode() + bytes_read)
    else:
        response_first_line = 'HTTP/1.0 404 Not Found\n\n Not Found Message'
        connection_socket.sendall(response_first_line.encode())
    connection_socket.close()
