number_of_elements=int(input('The number of elements in list\n'))

a=[]
for i in range(number_of_elements):
	a.append(int(input('enter the list elements')))
	

#Use built-in function to calculate the maximum

max_list=max(a)

print("The maximum element is ",max_list)

#Calculate the number of times the number occur

count_of_max_num=a.count(max_list)

b=a

if (count_of_max_num == 1):

	b.remove(max_list)
	second_max=max(b)
	print("The second largest number is", second_max, "The new list is" ,b)
else:
	for i in range(count_of_max_num):
		b.remove(max_list)
	print ("The second largest is" , max(b))

print("The original list is ",a)
