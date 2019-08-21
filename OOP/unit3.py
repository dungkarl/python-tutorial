"""
	classmethods and staticmethods
"""

import datetime

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

	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True
		


print(Employee.count_emps)

emp_1 = Employee('Dung', 'Karl', 5000)
emp_2 = Employee('User', 'Test', 7000)


#Employee.set_raise_amount(2.0)
# emp_1.set_raise_amount(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-60000'
emp_str_2 = 'Karl-Max-70000'
emp_str_3 = 'Le-Nin-80000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)
print(new_emp_2.pay)


my_date = datetime.date(2019, 8, 16)
print(my_date)
print(my_date.weekday())
print(Employee.is_workday(my_date))