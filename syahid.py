import argparse
from math import sqrt

##Factorial##
num = int(input("enter a number: "))

fac = 1

for jkt in range(1, num + 1):
    fac = fac * jkt

print("factorial of ", num, " is ", fac)

##Count Prime Number##

print('PRIME NUMBER')
lower = int(input("Give lower limit: "))
upper = int(input("Give upper limit: "))
print()
primes = []
for jkt in range(lower, upper+1):
    if jkt == 1:
        print("1 is not a valid start number")
    else:
        primeFlag = True
        for syah in range(2, jkt):
            if jkt % syah == 0:
                primeFlag = False
        if(primeFlag):
            primes.append
            print(jkt," number prime")
        else:
            print(jkt," not number prime")

print((upper-lower+1), " numbers were examined, ", len(primes), " were prime numbers")
print("The last found prime number is: ", primes[-1:])