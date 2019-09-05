import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Dung", "Karl", 50000)
        self.emp_2 = Employee("John", "Doe", 40000)
    
    def tearDown(self):
        print("tearDown")