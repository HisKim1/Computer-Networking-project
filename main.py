import struct
from socket import *
import os

BUFF_SIZE = 1024


# parameter :
# function : get python file from user's local computer / return file as struct
def getSourceCode():


# parameter :
# function :
def createConnection():
    client_socket = socket()

    # socket.connect parameter 'address' = (hostname, port) tuple로 제공해야 함
    client_socket.connect(getServerInfo())

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
# function : return server IP and address as tuple
def getServerInfo():
    dip = input('Server ip : ')
    dport = input('Server port to connect : ')
    return dip, dport


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':

    createConnection()

