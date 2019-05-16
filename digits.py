def digits(t):
    '''prints digits of integer t to length 9 digits
    accuracy of last digit printed is sometimes -1'''
    for e in range(1,10):
        if abs(t)/10**e < 1:
            if abs(t)/10**e > .1:
                d = (abs(t)/10**e)
                for ee in range(e,0,-1):
                    print(int(d*10))
                    d = (abs(d*10.0) - int(d*10))
                        
                                

