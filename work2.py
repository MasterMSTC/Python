file = open('infile.txt','r') 
#read_input=file.read()
read_input=file.readline()
file.close()

weight=float(read_input.split()[0])

height=float(read_input.split()[1])
BMI=weight/height**2

print("BMI is: {:.2f}".format(BMI))