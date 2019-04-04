import socket
import random
import datetime
import string
import json

def randomword(length):
   letters = string.ascii_lowercase


__randomfile__ = 0
__datetime__ = ''
__datetime__= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(__datetime__)

# Untuk radom data
for x in range(1):
	__randomfile__= random.randint(0,188)
	print(__randomfile__)
# Untuk read file
file 	= open("data.txt","r")
lines	= file.readlines()
# Untuk random nama negara
# splitcountry =  lines[__randomfile__].split(',')
# country = splitcountry[0]
# city 	= splitcountry[1]
# countcountry = len(country)


# for i in range(1):


# # for x in range(1):
# # 	country = random.randstr(0)
# # print(randomword(countcountry))
# # print (lines[__randomfile__])

guest ={
	'country' 		: 'country',
	'countryrand'	: 'countryrand',
	'city'			: 'countryrand',
	'score'			: 0
}

s = socket.socket()
port = 12345
host = '127.0.0.1'
rounde = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
	s.bind((host, port))
	s.listen()
	c, addr = s.accept()	
	rcvdData = c.recv(1024).decode()
	print('Welcome %s' %rcvdData)
	
	with c:
		while True:
			rcvdData = c.recv(1024).decode()
			# print(rcvdData)
			k = rcvdData.split(',')
			# print(k)
			if (k[1]== "bye"):
				break
			# Untuk radom data
			for x in range(1):
				__randomfile__= random.randint(0,187)	
			
			# negara
			splitcountry =  lines[__randomfile__].split(',')
			country = splitcountry[0]
			city 	= splitcountry[1]
			countcountry = len(country)
			# Random country name
			x = [ord(x) for x in country]
			y = random.sample(x, len(x))
			countryrandm = ''.join(map(chr, y))

			guest['country']		= country
			guest['countryrand'] 	= countryrandm
			guest['city'] 			 = city
			rounde=rounde+1
			print (countryrandm,guest['country'],guest['city'],'Rounde', rounde,  ' Score :',k[0])
			print(__datetime__)
			# print ("Socket Up and running with a connection from",addr)
			# print ("S:",rcvdData)
			b = json.dumps(guest).encode('utf-8')
			c.send(b)
			continue
	c.close()