A = []
A.append(1)
A.append(2)
A.append(3)

def fib(A,i):
    f=A[i-1]+A[i-2]
    return f

f=0
i=3
while(f<4000000):
    f=fib(A,i)
    A.append(fib(A,i))
    i=i+1

length = len(A)
sum = 0

for j in range (0,length-1):
    if(A[j]%2==0):
        sum = sum + A[j]

print ('The sum of all even valued Fibonacci numbers under 4,000,000 is: %d' %(sum))
