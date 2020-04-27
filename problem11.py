import numpy as np
from numpy import *

filename = 'p11.txt'

with open(filename, "r") as ins:
    array = []
    for line in ins:
        array.append(line)

newArray = []

for i in array:
    j = i.split(' ')
    k = [int(n) for n in j]
    newArray.append(k)

a = matrix(newArray)
print(a)

max = 0

# row products
for i in range(0, 20):
    for j in range(0, 17):
        pro = a[i, j]*a[i, j+1]*a[i, j+2]*a[i, j+3]
        if(pro >= max):
            max = pro

# collumn products
for j in range(0, 20):
    for i in range(0, 17):
        pro = a[i, j]*a[i+1, j]*a[i+2, j]*a[i+3, j]
        if(pro >= max):
            max = pro

# downward diagonal products
for i in range(0, 17):
    for j in range(0, 17):
        pro = a[i, j]*a[i+1, j+1]*a[i+2, j+2]*a[i+3, j+3]
        if(pro >= max):
            max = pro

# upward diagonal products
for i in range(3, 20):
    for j in range(0, 17):
        pro = a[i, j]*a[i-1, j+1]*a[i-2, j+2]*a[i-3, j+3]
        if(pro >= max):
            max = pro

print('The greatest product of four adjacent numbers in the above matrix is: %d' % (max))
