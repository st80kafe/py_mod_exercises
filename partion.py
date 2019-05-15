def partion():

    'implements ion2e function exercise 3.42'

    S = input('Enter string: ')

    X = "ion"


    if X not in S:

        quit

    else:

        L = list(S)

        if L[-1] == 'n' and L[-2] == 'o' and L[-3] == 'i' :

            for w in range(1,4):

                L.pop()
                
            L.append('e')

         else:

             quit

        Sb = str()

        for c in range(0,len(L)):

            Sb = Sb + L[c]

        print(Sb)
            

        

        
