
# TCP Client
# Anders Nelsson BTH
# Exempel från kursbok

from socket import *
# serverName = 'hostname'
serverName = '127.0.0.1'
serverPort = 12001
# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

#timeout
#clientSocket.settimeout(1000)

while True:
    print("trying to connect to: " + serverName + ":" + str(serverPort))

    # open the TCP connection
    try: 
        clientSocket.connect((serverName, serverPort))
        break
    except:
        serverName = input('input server name: ')
print("server connection establiched")


while True:

    # get modified sentence back from server
    data = clientSocket.recv(1024)
    print ('From Server:', data[:5].decode())

print("connection closed")
# close the TCP connection
clientSocket.close()
