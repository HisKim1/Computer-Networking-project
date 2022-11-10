import struct
import socket
import os

BUFF_SIZE = 1024


# parameter :
# function : get python file from user's local computer / return file as struct
def getSourceCode(client_socket):
    file_name = input('.py file name : ')
    FILE_SIZE = os.path.getsize(file_name)
    FILE_SIZE = struct.pack('L', FILE_SIZE)

    f = open(file_name, 'rb')
    l = f.read(BUFF_SIZE)

    while l:
        client_socket.send(l)
        l = f.read(BUFF_SIZE)
    f.close()


# parameter :
# function :
def setConnection():
    client_socket = socket.socket()
    print('socket created')
    client_address = getServerInfo()
    print(client_address)

    # socket.connect parameter 'address' = (hostname, port) tuple로 제공해야 함
    try:
        client_socket.connect(client_address)
    except ConnectionError :
        print(ConnectionError)


    # 일단 제외,,,
    # getSourceCode(client_socket)

    while True:

        #-------.py file로 바꿔야 할 부분--------
        message = input("any message to sent?")

        if not message:
            break
        client_socket.send(message.encode())
        #--------------------------------------

        data = client_socket.recv(1024)
        print("from server: ", data.decode())

    client_socket.close()


# parameter :
# function : return server IP and address as tuple
def getServerInfo():
    dip = input('Server ip : ')
    dport = input('Server port to connect : ')

    # Just for test -> 왜 IP로 넣으면 안되고 이름으로 넣어야 될까,,,
    dip = socket.gethostname()
    dport = 12121

    return dip, dport


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    setConnection()

