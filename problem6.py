sum = 0
for i in range(1,101):
    ii = i*i
    sum = sum + ii

summ = 0
for i in range(1,101):
    summ = summ + i

answer = (summ*summ) - sum
print('The difference between the sum of the squares of the first 100 natural numbers and the the sum squared is: %d' %(answer))
