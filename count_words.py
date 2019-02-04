##############################################################################
#########		Words_Count.py				#############
########	Author: Gaurav Parashar				#############
########	Description: Program to find unique and non	#############
########			unique words in a file		#############
##############################################################################


#We need to use the Counter Class
from collections import Counter


#Reading from a file
with open('test.txt', 'r') as f:
	string_words=f.read()
#After f.read() is an object of string type


#Converting the string to a list based on spaces
list_from_string=string_words.split()

#create a counter object
#Note that Counter takes either an iterable or 
#a mapping object as the argument
counter_word_count=Counter(list_from_string)


#Lists created to store unique and 
#common word counts
uniq_word_list=[]
common_word_list=[]

#Using a for loop to
#get which keys have corresponding
#value equal to 1
for word in counter_word_count.keys():
	if (counter_word_count[word]==1):
		uniq_word_list.append(word)

	else:
		common_word_list.append(word)

print(uniq_word_list)

print ("=====================")

print (common_word_list)

print ("also printing =================================")



#This is one more way using the counter class 
#elements method
#one more way of taking all words in a list
new_list=[]
for word in (counter_word_count.elements()):
	new_list.append(word)

#To print the sorted words list
print (sorted(new_list))	
