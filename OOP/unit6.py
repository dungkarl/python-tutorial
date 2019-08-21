"""
	Property Decorators - Getters, Setters, and Deleters
"""

class Employee:
	
	def __init__(self, first, last):

		self.first = first
		self.last = last
		#self.email = self.first + self.last + '@gmail.com'

		#Employee.count_emps +=1
	@property
	def fullname(self):

		#return self.first + self.last
		return '{} {}'.format(self.first, self.last)
	@property
	def email(self):
		return '{}{}@gmail.com'.format(self.first, self.last)


	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):

		print('deleted')
		self.first = None
		self.last = None
		


emp_1 = Employee('Dung', 'Karl')


#emp_1.fullname = 'Dung Dinh'

emp_1.fullname = 'John Doe'	


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


del emp_1.fullname