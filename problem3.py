#this code will find the largest prime factor of any number
num = 600851475143


def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

fact = prime_factors(num)
largest = max(fact)

print('The largest prime factor of %d is: %d' %(num , largest))
