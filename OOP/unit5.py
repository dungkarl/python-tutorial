"""
	Special Methods
"""


class Employee:
	#count_emps = 0
	raise_amount = 1.04
	def __init__(self, first, last, pay):

		self.first = first
		self.last = last
		self.pay = pay
		self.email = self.first + self.last + '@gmail.com'

		#Employee.count_emps +=1

	def fullname(self):

		#return self.first + self.last
		return '{}-{}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = self.pay * self.raise_amount

	def __repr__(self):

		#return f"Employee ({self.first}, {self.last}, {self.pay})"
		return "Employee: ({}, {}, {})".format(self.first, self.last, self.pay)

	def __str__(self):
		return '{}-{}'.format(self.fullname(), self.email)

	def __add__(self, other):	
		return self.pay + other.pay
	
	def __len__(self):
		return len(self.fullname())


emp_1 = Employee('Dung', 'Karl', 5000)
emp_2 = Employee('User', 'Test', 7000)

print(emp_1.__repr__())
print(emp_1.__str__())


print(emp_1 + emp_2)
print(len(emp_2))
