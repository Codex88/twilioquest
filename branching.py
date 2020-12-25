import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
sum = num1 + num2

if sum <= 0:
	print("You have chosen the path of destitution.")
elif sum >= 1:
	if sum <= 100:
		print("You have chosen the path of plenty.")
	elif sum > 100:
		print("You have chosen the path of excess.")