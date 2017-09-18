import sys


file = open(sys.argv[1],'r')
#read_input=file.read()
read_input=file.readline()
file.close()

weight = float(read_input.split()[0])
height = float(read_input.split()[1])

BMI=0

if height != 0:
   BMI = weight / height **2


print(BMI)

file = open('outfile.txt','w')
file.write(str(BMI))
file.close()

