
"""
	Class variables
"""

class Employee:

	count_emps = 0
	raise_amount = 1.04
	def __init__(self, first, last, pay):

		self.first = first
		self.last = last
		self.pay = pay
		self.email = self.first + self.last + '@gmail.com'

		Employee.count_emps +=1


	def fullname(self):

		#return self.first + self.last
		return '{}-{}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = self.pay * self.raise_amount




print(Employee.count_emps)

emp_1 = Employee('Dung', 'Karl', 5000)
emp_2 = Employee('User', 'Test', 7000)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

emp_1.apply_raise()

print(emp_1.pay)
print(emp_1.__dict__)

emp_1.raise_amount = 2.0

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

print(emp_1.__dict__)

print(emp_1.count_emps)
print(emp_2.count_emps)
