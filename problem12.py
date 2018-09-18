#this block simply generates triangular numbers
tri = []
tri.append(1)
tri.append(3)
for i in range(3,1000000):
    x = tri[i-2]+i
    tri.append(x)

def numfact(x):
    count = 0
    for i in range(1,x+1):
        if(x%i==0):
            count+=1
    return count

for i in tri:
    fact = numfact(i)
    if(fact == 500):
        print fact
