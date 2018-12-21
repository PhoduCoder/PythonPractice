#print("Enter the number of elements in the list")

#num_of_elements = input('Enter the number of elemnts you would like in the list')

given_list = [2,3,4,54,32,1,4,5]

min=given_list[0]
max=given_list[0]
for i in range(len(given_list)):
	if (given_list[i]<min):
		min = given_list[i]

	if (given_list[i]>max):
		max=given_list[i]

print ("The minimum number is ", min, "\n")

print ("The maximum number is", max, "\n")
