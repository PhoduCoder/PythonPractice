#sec_vec=[[1,2,3],[2,3], 4]
sec_vec=[[1,2,3],5,[2,3], 4]

flat_list=[]

for i in sec_vec:
	if(type(i)) is list:
		for num in i:
			flat_list.append(num)
	else:
		flat_list.append(i)

print (flat_list)
