from socket import *
import time

host = '127.0.0.1'
port = 12000
serverPort = 12001

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('', serverPort))


messageMaxLen = 100;
message = ''
for m in range(0, messageMaxLen):
	message += '0'

sequence = 10001

while True:
	s.sendto((str(sequence) + ';' + message).encode(), (host, port))
	sequence += 1
	time.sleep(1)

