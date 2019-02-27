

def twoStrings(str1,str2):
	return set(str1.split())

def splitUsingSets(str1):
	list_of_strings=str1.split('\t')
	print(set(list_of_strings))

if __name__ =='__main__':
	
	#q=int(input())

	#for q_itr in range(q):
	#	s1=input()
	#	s2=input()

	#	result=twoStrings(s1,s2)
	#	print(result)
	s3=input()
	splitUsingSets(s3)

