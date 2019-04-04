#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

number_key =0
message1= "This is a new Message"
print("Connecting initiated....")
input_pertama = input("Type exit to finish sending data")
print (input_pertama)
while input_pertama != "exit":
	print ("Enter Your Message")
	print (message1)
	number_key=input("Enter the number key(1-26) ")
	while 1>=int(number_key)>=26:
		number_key=input("Enter the number key(1-26) ")
	print (number_key)
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.connect((HOST, PORT))
	    s.sendall(b'%s' % message1)
	    data = s.recv(1024)

	print('Received', repr(data))

input_pertama = input("Type exit to finish sending data")

