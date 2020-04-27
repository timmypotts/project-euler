# QUESTION:
# ===================================================
# What is the sum of the digits of the number 2^1000?

# For this one I just put every digit of 2^1000 into an array and used the python sum method to add up all the elements in the array. Simple stuff


bigNum = 2**1000
digits = [int(d) for d in str(bigNum)]
answer = sum(digits)
print(answer)
