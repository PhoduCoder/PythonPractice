class Student:
	
	def __init__(self, name, age, country):
		self.name=name
		self.age=age
		self.country=country


	def display(self, name, country):
		print('{} belongs to {} .format(self.name, self.country)')



s1=Student('Gaurav Parashar', 29, 'India')
s2=Student('Destiney ', 23, 'Puerto Rico')
s3=Student('Alex', 25, 'United States')

print(s1.__dict__)

print("=============")

print(Student.__dict__)

s1.display('Gaurav Parashar', 'India')
