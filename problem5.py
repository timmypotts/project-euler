def check(x):
    mod = []
    for i in range(2,21):
        m = x%i
        mod.append(m)
    if(max(mod)==0):
        return True
    else:
        return False
i = 20
while(bool !=True):
    bool = check(i)
    if(bool == True):
        print('The largest number that can be evenly divided by all numbers 1-20 is: %d' %(i))
        exit()
    i = i+20
