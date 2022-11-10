import socket



def createSocket():

    # set host IP and port
    HOST_NAME = socket.gethostname()
    HOST_IP = socket.gethostbyname(HOST_NAME)
    HOST_PORT = 12121

    print("hostNAME :", HOST_NAME)
    print('hostIP :', HOST_IP)
    print('hostPORT : ', HOST_PORT)


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # to prevent the error caused by occupied port by other clients
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST_IP, HOST_PORT))

    # 사람 늘릴려면 바꿔줘야 함.
    server_socket.listen(1)

    client_socket, client_addr = server_socket.accept()
    print('connection established')

    while True:
        # .py 파일이면 여기도 바꿔야 됨. while로 struct 돌려가면서 받기
        # 하지만 그냥 받아도 돌아가긴 함?!! -> .py 파일이 아직 작아서 그런 듯.
        data = client_socket.recv(1024)

        # if empty file received, send error message
        if not data:
            client_socket.send('Empty file. Try again')
            continue

        # source processing part

        #show received packet
        print('from client ', client_addr, data.decode())

        # after processing, result (success | fail) message send
        result = input('student\'s result : ')
        client_socket.send(result.encode())

    client_socket.close()

if __name__ == '__main__':
    createSocket()