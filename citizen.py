import sys

class Citizen:
	''' Blueprint for a Python Citizen '''
	def __init__(self, first_name, last_name):
		first_name = sys.argv[1]
		last_name = sys.argv[2]
		self.full_name = first_name + " " + last_name
	greeting = "For the glory of Python!"