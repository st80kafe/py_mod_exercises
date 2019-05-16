def digits(t):
    '''prints digits of positive integer t to length 9 digits'''


    for c in range(1,10):   # find number of digits

        if t/10**c < 1:

            if t/10**c >= .1:  # number of digits = c

                for e in range(c-1,-1,-1):
                # value of exponent e before division of int t by 10**e
                
                    print(t//10**e) # print first digit of t

                    # subtract value of first digit multiplied by power of 10
                    t = t - ( (t//10**e)*10**e )
                        
                                

