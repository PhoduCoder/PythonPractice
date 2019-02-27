
number_of_numbers=10

result=[]

def fib(number_of_numbers):
	for i in range(number_of_numbers):
		result.append(i+(i+1))
	print (result)

fib(number_of_numbers)
