first_string="Testing"


def getAllSubstring(given_string):
        length=len(given_string)
        substring_list=[]
        for i in range(length):
                substring_list.append(given_string[0:i+1])

        return substring_list

#second_string="Not"

all_substring=getAllSubstring(first_string)

print(all_substring)

#for i in range(length_of_string):
#	print(given_string[0:i+1])
#	substring_list.append(given_string[0:i+1])
#
#print (substring_list)
	
