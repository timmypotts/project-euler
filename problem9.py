for x in range(0,1000):
    for y in range(x+1,1000):
        for z in range(y+1,1000):
            if(x*x + y*y == z*z and x+y+z==1000):
                answer = x*y*z
                print('The product of the three Pythagorean triples that add up to 1,000 is %d' %(answer))
                exit()
