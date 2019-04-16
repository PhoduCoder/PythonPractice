class Student:
	pass


s1=Student()


s1.name='Gaurav Parashar'
s1.age=29
s1.country='India'


s2=Student()
s2.name='Destiney'
s2.age=23
s2.country='Peurto Rico'


s3=Student()
s3.name='Alex'
s3.age=24
s3.country='United States'


print('{} belongs to {}'.format(s1.name, s1.country))
print('{} belongs to {}'.format(s2.name, s2.country))
print('{} belongs to {}'.format(s3.name, s3.country))
