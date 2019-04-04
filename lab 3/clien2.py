import socket

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
 
# text = input("enter string: ")
# s = int(input("enter shift number: "))
# print("original string: ", text)
# print("after encryption: ", encrypt(text, s))

s = socket.socket()
s.connect(('127.0.0.1',12345))
print("Connection initialed...")
print("Type exit to finish sending data")
while True:
	print("Enter your message:")
	print("This is a new message")
	str = input("Enter the key number 1-26 \n ")
	# if s.str()
	
	s.send(str.encode())
	if(str == 0):
		s.send(str.encode())
		break
	# print ("N:",s.recv(1024).decode())
s.close()

