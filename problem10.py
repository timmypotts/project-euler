# QUESTION:
# ===================================================================================================
# Find the sum of all the primes below two million.

# This question could be solved with a brute-force method, but would take an impractically long time.
# Instead, I used a seive. I created an array of two million elements and set every value to 1.
# Since 0 and 1 are not prime, we can immediately remove them from consideration and set the values at their corresponding indices to 0


import numpy as np
primes = []
for i in range(0, 2000000):
    primes.append(1)

primes[0] = 0
primes[1] = 0

# I used a seive so instead of having to find all the prime numbers below 2,000,000 - I could find all the numbers that are NOT prime and set their index's value to 0
# The algorithm would find 2 to be the first index of the array with a 1 occupying it. The algorithm would then mark every even number under 2,000,000 -- except 2 -- as non-prime.
# This will continue for all integers up to 1415, since 1415^2 = 2,002,225. All integers higher than 1415, the first square root above 2-million, will have already been marked as not-prime by the seive in previous iterations.


for i in range(2, 1416):
    if(primes[i] == 1):
        j = 2
        while(j*i <= 1999999):
            primes[i*j] = 0
            j = j+1

# From here we have all prime numbers marked as 1 in our array. We then just add together the indices at the 1 values to get our answer


indices = [i for i, x in enumerate(primes) if x == 1]
answer = sum(indices)
print('The sum of all primes below two million is: %d' % (answer))

# This produces an answer of 1,429,13,828,922
