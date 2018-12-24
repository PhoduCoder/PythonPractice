#Author: Gaurav Parashar
# This is going to be 
# a sample python script that
# creates a list based on user input

test_list = []

size_of_list = int(input("What's the size of the list you want:"))


for i in range(size_of_list):
	num1= int(input('enter the number'))
	test_list.append(num1)
#test_list = []


#Note that the list.append() method doesn't return any thing
#Hence the below line would return a none type
#test_list=test_list.append(num1)
#test_list.append(num1)


print (test_list, type(test_list))

