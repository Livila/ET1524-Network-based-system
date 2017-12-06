from socket import *

host = 'ingonline.nu'
port = 80
socket = socket(AF_INET, SOCK_STREAM)
socket.connect((host, port))

socket.sendall("GET http://ingonline.nu/tictactoe/index.php?board=xoxoeoexx HTTP/1.1\n\n".encode())

response = socket.recv(1024)

print (response.decode())

socket.close()
