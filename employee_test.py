import unittest

from realworldproblemmodeled import Employees

class Test_realworldproblemmodeled(unittest.TestCase):
	def test_return_name(self):
		eric=Employees("eric",5662,2323)
		self.assertEqual("eric",eric.returnname(5662))

	def test_default_employee_name(self):
		name = "not_found"
		employee1 = Employee("SSDC123")
		employee_name = employee1.name

		self.assertEqual(name,employee_name)
		"""The employee should be called `not_found` if no name was passed as an argument"""

	def test_object_type(self):
		name = "agent"
		agent = Employees(name)
		self.assertTrue(type(agent) is Employees)

	def test_Employee_isinstance(self):
		agent = Employees('agent')
		self.assertIsInstance(agent, Employees, msg='The object should be an instance of the `Employees` class')




