"""
	Python Object Oriented Programing
	Class and Instances

"""

class Employee:
	def __init__(self, first, last, pay):

		self.first = first
		self.last = last
		self.pay = pay
		self.email = self.first + self.last + '@gmail.com'


	def fullname(self):

		#return self.first + self.last
		return '{}-{}'.format(self.first, self.last)



emp_1 = Employee('Dung', 'Karl', 5000)
emp_2 = Employee('User', 'Test', 7000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())

#emp_1.fullname()
print(Employee.fullname(emp_2))
