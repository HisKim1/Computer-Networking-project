import struct
import socket
import os

BUFF_SIZE = 1024


# parameter : client_socket = socket already created. use this socket to send .py
# function : get python file from user's local computer
def sendSourceCode(client_socket):
    file_name = input('.py file path : ')

    # if there does not exist such file
    while not os.path.exists(os.path.abspath(file_name)):
        file_name = input('there is no file. type again.')

    # getsize() return certain file size of byte
    FILE_SIZE = os.path.getsize(file_name)

    FILE_SIZE = struct.pack('L', FILE_SIZE)

    # file을 읽어서 BUFF_SIZE만큼씩만 보낸다... struct는 어디서 쓰인 것일까...
    f = open(file_name, 'rb')
    l = f.read(BUFF_SIZE)

    # just for counting # of packets
    i = 1

    while l:
        print(f'{i}번째 packet')
        client_socket.send(l)
        l = f.read(BUFF_SIZE)
        i += 1
    f.close()


# parameter :
# function :
def setConnection():
    client_socket = socket.socket()
    print('socket created')

    client_address = getServerInfo()
    print(client_address)

    try:
        print('start to connect')
        os.system("pause")

        # error type of connect() : TimeoutError, InterruptedError
        client_socket.connect(client_address)
    except Exception as ex:
        print(f'exception occured : {ex}')

    while True:
        sendSourceCode(client_socket)

        #-------sample : message 주고 받기--------
        # message = input("any message to sent?")
        #
        # if not message:
        #     break
        # client_socket.send(message.encode())
        #--------------------------------------

        data = client_socket.recv(1024)
        print("from server : ", data.decode())

        retry = input('Try again? (Y/N) : ')
        if retry == 'Y' or retry == 'Y'.lower():
            continue
        else:
            break

    client_socket.close()


# parameter :
# function : return server IP in string and port in int as tuple
def getServerInfo():
    dip = input('Server ip : ')
    dport = input('Server port to connect : ')

    # socket의 address에는 (hostname=str, port=int), (IPv4 address=str, port=int) 둘 다 가능함.

    # gethostbyaddr(ip) returns (hostname, alias name, IP address)
    # dip = socket.gethostbyaddr(dip)

    return dip, int(dport)


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    setConnection()

