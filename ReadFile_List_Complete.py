import sys

for line in open(sys.argv[1], 'r'):
   print(line)


list_Auto =[]
for line in open(sys.argv[1], 'r'):
   list_Auto.append(line.split(','))

list_Auto =[]
for line in open(sys.argv[1], 'r'):
   list_Auto.append([float(line.split(',')[0]), float(line.split(',')[1]), line.split(',')[8]])

file = open(sys.argv[1],'r')
list_Auto = list([float(line.split(',')[0]), float(line.split(',')[1]), line.rstrip('\n').split(',')[8]] for line in file)
file.close()

print(list_Auto[0:5])

print(list_Auto[-1])

# CHANGE elements in a list

## Changes in one "copied" list affect the other:
## ONLY the reference to the list is copied!!!

list_Auto2=list_Auto

list_Auto2[0][0]=10

# list_Auto is changed !!!
print(list_Auto[0])

## SEE FUNCTIONS and METHODS


mpg = [item[0] for item in list_Auto]
cilinders = [item[1] for item in list_Auto]

### NUMPY
## unsupported operand type(s) for /: 'list' and 'list'

mpg/cilinders

### SEE test_packages

import numpy as np

npa_mpg=np.array(mpg)
npa_cilinders=np.array(cilinders)

mpg_cilinders=npa_mpg/npa_cilinders

type(mpg_cilinders)

mpg_cilinders.shape


### RE- READING from list_Auto

npa_Auto=np.array(list_Auto)

### npa_Auto is a

v_mpg=npa_Auto[:,0]
v_cilinders=npa_Auto[:,1]

## Doesn't work, WHY???
mpg_cilinders_2=v_mpg/v_cilinders

# list_Auto DIFFERENT TYPES .... numpy arrays only ONE!


### SOLUTION : convert to float

v_mpg=npa_Auto[:,0].astype(np.float32)
v_cilinders=npa_Auto[:,1].astype(np.float32)

mpg_cilinders_2=v_mpg/v_cilinders

### working with arrays

mpg_cil_2d=np.vstack([v_mpg, v_cilinders])

mpg_cil_2d[:,0:5]

## RESHAPE

tmp=mpg_cil_2d.reshape[-1]
tmp.shape

tmp=mpg_cil_2d.reshape(397,2)

## study the result...

# practice with simple examples

### Some analysis using MATPLOTLIB

import matplotlib.pyplot as plt

# HOW TO PLOT??
plt.plot(v_mpg, v_cilinders)
plt.show()

# Scatter Plot
plt.figure(2)
plt.scatter(v_mpg, v_cilinders)

plt.show()

# ... improve...

plt.figure(3)
plt.scatter(v_mpg, v_cilinders)
plt.xlabel('Miles per galon')
plt.ylabel('Number of cylinders')
plt.title('Scatter MPG vs no. Cylinders')
plt.yticks([3, 4, 5, 6, 8],
           ['3Cyl','4Cyl','5Cyl','6Cyl','8Cyl'])
plt.show()




# Histogram
random_var=np.random.normal(0,1,10000)

# Build histogram with 5 bins
plt.figure(4)
plt.hist(random_var,5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 100 bins
plt.hist(random_var,100)

## Plotting Auto Data

plt.figure(5)
plt.subplot(2,1,1)
plt.hist(v_mpg,20)

plt.subplot(2,1,2)
plt.hist(v_cilinders,20)


## Exclude num cyl > = 5

v_mpg1=v_mpg[v_cilinders<=4]
v_cilinders1=v_cilinders[v_cilinders<=4]

v_mpg1.shape

plt.figure(6)
plt.subplot(2,1,1)
plt.hist(v_mpg1,20)

plt.subplot(2,1,2)
plt.hist(v_cilinders1,20)

## Exclude num cyl < 7

v_mpg2=v_mpg[v_cilinders>=7]
v_cilinders2=v_cilinders[v_cilinders>=7]

v_mpg2.shape

plt.figure(7)
plt.subplot(2,1,1)
plt.hist(v_mpg2,20)

plt.subplot(2,1,2)
plt.hist(v_cilinders2,20)