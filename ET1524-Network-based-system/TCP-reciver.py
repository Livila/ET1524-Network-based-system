# TCP Client
# Anders Nelsson BTH
# Exempel från kursbok

from socket import *
# serverName = 'hostname'
serverName = '127.0.0.1'
serverPort = 12001

# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((serverName, serverPort))

# Input sentence from keyboard


while True:
    # get modified sentence back from server
    myNumber = clientSocket.recv(1024)
    print ('From Server:', myNumber.decode())

# close the TCP connection
clientSocket.close()
