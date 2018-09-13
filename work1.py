import sys


if(len(sys.argv)) != 3:
	print('Please enter your weight and height')
	sys.exit()
else:
	weight=float(sys.argv[1])
	height=float(sys.argv[2])
	BMI=weight/height**2

	print("BMI is: {:.2f}".format(BMI))
