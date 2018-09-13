file = open('infile_table.txt','r')

for line in file:

	weight=float(line.split()[0])
	height=float(line.split()[1])
	BMI=weight/height**2

	print("Weight {:.2f} Weight {:.2f} gives BMI: {:.2f}".format(weight,height,BMI))



file.close()

