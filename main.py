import socket
from socket import *

BUFF_SIZE = 1024

# parameter :
# function : get python file from user's local computer
def getSourceCode():
    file_address = input('location of .py file : ')


# parameter :
# function :
def createConnection():
    client_socket = socket()

    # socket.connect parameter 'address' = (hostname, port) tuple로 제공해야 함
    client_socket.connect(getServerInfo())


# parameter :
# function : return server IP and address as tuple
def getServerInfo():
    dip = input('Server ip : ')
    dport = input('Server port to connect : ')
    return dip, dport


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':

    createConnection()

