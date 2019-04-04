import socket
import datetime

def encrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  
  return cipher

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
c, addr = s.accept()
print ("Socket Up and running with a connection from",addr)
print(datetime.datetime.now())
while True:
	date = datetime.datetime.now()
	rcvdData = c.recv(1024).decode()
	print ("S:",rcvdData)
	text = ("This is a new message")
	# enc = encrypt(text, int(rcvdData))
	print("coded message: %s" % encrypt(text, int(rcvdData)))
	print("encode message: %s " % text)
	print(date)
	# sendData = input("N: ")
	conv= str(rcvdData)
	f= open("hasil.txt","a+")
	f.write(str(rcvdData)+','+str(date) + ','+encrypt(text, int(rcvdData))+'\n')
	# c.send(sendData.encode())
	if(int(rcvdData)==0):
		break
c.close()