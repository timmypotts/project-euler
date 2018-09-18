#this code can calculate the 10,001st prime in approxomately 31.31 seconds
primes = []
primes.append(2)
primes.append(3)


def checkPrime(x): #by only checking if a number is divisible by previous primes, this greatly reduces the number of comparisons needed to check if a number is prime
    primecheck = []
    for i in range(0,len(primes)/2): #by only checking primes up to half the size of the current number being checked, this took the time from 40.42 seconds to 31.31 seconds
        check = x%primes[i]
        primecheck.append(check)
    if (0 not in primecheck):
        primes.append(x)
i = 4
while(len(primes)<10002):
    checkPrime(i)
    i = i+1


pri = (primes[10000])
print('The 10,001st prime number is: %d' %(pri))
