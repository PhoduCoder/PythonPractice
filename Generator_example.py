
def square_generator_function(list_of_num):
	for i in list_of_num:
		yield (i**2, i**3)

caller_gen=square_function([1,2,3,4,5])

#print (caller_gen, type(caller_gen))

print ("-------------------------")

for i,j in caller_gen:
	print ("The square of the list is {} and the cube of the list is {}".format(i,j))
