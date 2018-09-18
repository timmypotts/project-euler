def collatz(x, seq=[]):
    if(x==1):
        seq.append(x)
        print seq
        return seq
    elif(x%2==0):
        x=x/2
        seq.append(x)
        print seq
        collatz(x)
    else:
        x=3*x+1
        seq.append(x)
        print seq
        collatz(x)

sequence = []
sequence.append(500)
collatz(500, sequence)
