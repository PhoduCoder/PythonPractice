#This is a program to find the 
#maximum and the minimum of a list
#where the elements of the list
#are entered by the user

#We are using the eval 
#function to input the list

user_entered_list=eval(input("Enter the list:"))
print (user_entered_list, type(user_entered_list))

min=user_entered_list[0]
max=user_entered_list[0]

print ("before min and max", min,max)
for i in range(len(user_entered_list)):
	if user_entered_list[i]<min:
		min=user_entered_list[i]

	if user_entered_list[i]>max:
		max=user_entered_list[i]

print ("The maximum and the minimum value entered are", max, "and", min, "respectively")
