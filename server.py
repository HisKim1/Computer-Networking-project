import socket



def createSocket():
    HOST_NAME = socket.gethostname()
    HOST_IP = socket.gethostbyname(HOST_NAME)
    HOST_PORT = 12121

    print('hostIP :', HOST_IP)
    print('hostPORT : ', HOST_PORT)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST_IP, HOST_PORT))

    server_socket.listen(1)

    client_socket, client_addr = server_socket.accept()
    print('connection established')

    while True:
        data = client_socket.recv(1024)

        print('from client ', client_addr, data.decode())

        result = input('Well done! any message?')
        client_socket.send(result.encode())

    client_socket.close()

if __name__ == '__main__':
    createSocket()