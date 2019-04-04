import argparse

parser =argparse.ArgumentParser(description='Calculate of task')
parser.add_argument('-prime','--prime', metavar='', help='Prime number format : ')
parser.add_argument('-fact','--fact',type= int, metavar='',help='Factorial number format : number')
parser.add_argument('-fibo','--fibo',type= int,metavar='', help='Fibonaci number format : number')

args = parser.parse_args()

def fib(n):
    a, b = 0, 1
    result = [0, 1]
    while a < n:
        result.append(b)
        a, b = b, a+b
    print result


def fact(n):
	print("Factorial Number")
	times=1
	for x in range(1,n+1):
		times = times *x
	return times
	
# fact(10)

def is_prime(awal,akhir):
	# lista =[]
	print("Prime number")
	for val in range(awal, akhir + 1): 
	   if val > 1: 
	       for n in range(2, val): 
	           if (val % n) == 0: 
	               break
	       else: 
	       		print (val)
	#          lista.append(val)

	# return lista         

# is_prime(1,10)
if args.prime:
	result = args.prime.split(',')
	star  = int(result[0])
	end = int(result[1])
	is_prime(star,end)

elif args.fibo:	
	fib(args.fibo)
elif args.fact:
	print fact(args.fact)



