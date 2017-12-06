from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', 12000))

prevPacket = 10000

while True:
	message, serverAddress = s.recvfrom(2048)

	if prevPacket + 1 != int((message.decode())[:5]):
		print(prevPacket + 1)

	prevPacket = int((message.decode())[:5])

