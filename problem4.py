def palindrome(num):
    return str(num) == str(num)[::-1]


pals = []
for i in range(100, 1000):
    for j in range(100, 1000):
        check = i*j
        if (str(check) == str(check)[::-1]):
            pals.append(check)

lpal = max(pals)
print('The largest palendrome made from the product of two 3-digit numbers is: %d' % (lpal))
