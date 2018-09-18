#this code uses the sieve of Eratosthenes to opimally generate prime numebers
import numpy as np
primes = []
for i in range (0,2000000):
    primes.append(1)

primes[0]=0
primes[1]=0

for i in range(2,1415):
    if(primes[i]==1):
        j=2
        while(j*i<=1999999):
            primes[i*j]=0
            j = j+1


indices = [i for i, x in enumerate(primes) if x == 1]
answer = sum(indices)
print('The sum of all primes below two million is: %d' %(answer))
