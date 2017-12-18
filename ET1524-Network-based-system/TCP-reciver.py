# TCP reciver

from socket import *
# serverName = 'hostname'
serverName = '127.0.0.1'
serverPort = 12001

# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((serverName, serverPort))

# Input sentence from keyboard

prevPacket = 10000

while True:
    # get modified sentence back from server
    myNumber = clientSocket.recv(100)
   
    if prevPacket + 1 != int((myNumber.decode())[:5]):
        test = (myNumber.decode())[:5]
        if test == "00000" :
            print(myNumber.decode())
        else :
            print(test)

    prevPacket = int((myNumber.decode())[:5]);
    #print ('From Server:', myNumber.decode())

# close the TCP connection
clientSocket.close()
