import sys

inputs = sys.argv
inputs.pop(0)

for entry in inputs:
	integer = int(entry)
	print_string = ""
	if integer % 3 == 0:
		print_string = print_string + "fizz"
	if integer % 5 == 0:
		print_string = print_string + "buzz"
	if print_string == "":
		print(integer)
	else:
		print(print_string)