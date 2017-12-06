from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 12000))

while True:
	message, serverAddress = s.recvfrom(2048)
	print((message.decode())[:5])

