"""
	Inheritance and  Creating Subclass
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


class Developer(Employee):
	raise_amount = 1.5
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		#Employee.__init__(first, last, pay)
		self.prog_lang = prog_lang




class Manager(Employee):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print("-->", emp.fullname())




	

dev_1 = Developer('Dung', 'Karl', 10000, 'Python')
dev_2 = Developer('John', 'Doe', 5000, 'Java')


# print(dev_1.email)
# print(dev_1.prog_lang)
# print(dev_2.email)

# #print(help(Developer))
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

mng_1 = Manager('Max', 'Karl', 20000)
print(mng_1.fullname())
print(mng_1.email)
mng_1.add_emp(dev_1)
mng_1.add_emp(dev_2)
mng_1.print_emps()
mng_1.remove_emp(dev_1)
print("removed")
mng_1.print_emps()
