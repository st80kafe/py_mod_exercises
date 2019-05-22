def even(i):
    'outputs range of positive integers divisible by 2 or 3'

    e = ", "  # append formatting argument e to print()

    for t in range(2,i+1):

        if t >= i - i%2:   # when printing i or i-1

            if t == i or i%3 > 0:
                e = '\n'   # modify value of e

                    
        if t%2 == 0 or t%3 == 0:
            print(t, end=e)

