import socket
import json
s = socket.socket()

player={
	"name" 	: 'Default',
	'score' : 10
}
rounde1 = 0
score = 0
str2 =''
str3 =''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
	s.connect(('127.0.0.1',12345))
	print('Connection Initialed')
	print('Connected to Game Server Throught 127.0.0.1 port 12345')
	print('Welcome to word Puzle Game')
	str1= input("Please inser your Name : ")
	s.send(str1.encode());
	str3 = 'next,1'
	s.send(str3.encode()); 
	while True:
		if(str2 == "Bye" or str2 == "bye"):
			s.send(str2.encode());
			break	
		rcvdData = s.recv(1024)
		y= json.loads(rcvdData.decode('utf-8'))
				
		rounde1 = rounde1+1
		print("Round " , rounde1)
		print("your score is : " ,score)
		print("Guest this country ", y['countryrand'])
		str2 = input("your answer is : ")

		casscore = str(score)
		a = casscore +','+ str2
		# k = a.split(',')

		s.send(a.encode());
		if(str2 == "Bye" or str2 == "bye"):
			s.send(str2.encode());
			break
		elif (str2 == y['country']):
			score= score +10
			continue
			# s.send(str.encode());
		elif(str2 == "help"):
			print('Hint... this city capital is %s' %y['city'])
			print('Guest this country %s' %y['countryrand'])
			str2 = input("Your answer is : ")
			if (str2 == y['country']):
				score= score +5
				continue
				# s.send(str.encode());
			else:
				score= score +0
				# s.send(str.encode());
				continue

		# else:
		# s.send(str.encode());
		print ("N:",y['country'] , y['city'], y['countryrand'])
