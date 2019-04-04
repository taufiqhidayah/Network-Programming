import random
 
 
line = random.choice(open('data.txt').readlines())
print (line)
soal, hint = line.split(",")
print (soal)
print (hint)
x = [ord(x) for x in soal]
y = random.sample(x, len(x))
z = ''.join(map(chr, y))

print (z)