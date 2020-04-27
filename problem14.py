# QUESTION:
# ===================================================================================================
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?


# This question focuses on optimizing the algorithm used to solve it. We could simply go though each number and calculate the sequence from 1 to 1,000,000 and find the longest sequence
# However, since it is not asking for the sequence itself, I apprached this by simply counting how many steps my algorithm had to take for each number instead of having to use memory to store cumbersome sequences

def collatz(x, i):
    if(x == 1):
        return i

    elif(x % 2 == 0):
        x = x/2
        i += 1
        return collatz(x, i)
    else:
        x = 3*x+1
        i += 1
        return collatz(x, i)


def findLongest():
    maxLen = 0
    answer = 0
    for i in range(1, 1000000):
        len = collatz(i, 1)
        if maxLen < len:
            maxLen = len
            answer = i

    print("The integer with the longest Collatz sequence is %d with a length of %d" % (
        answer, maxLen))


findLongest()
