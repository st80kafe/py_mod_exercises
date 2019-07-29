

if __name__ == '__main__':
    pass



def silo(string_in):

        '''
        duplicates default split method of string such that
        S.split() == silo(S),
        constructing list of strings from string input that
        may contain spaces
        '''

        list_out = [] # create list of space separated inputs from string string_in
        ind = 0  # index
        last = ''

        for c in string_in: 

            if c == ' ':  
                if last == c: # consecutive blank spaces found
                    pass
                else:
                    ind += 1 # construct new item in list_out
                    last = c
            elif len(list_out) == ind: # ind==0 or multiple chars in last item found
                    if ind == 0: # first item in list_out
                        list_out.append(c) # c is non-blank first char of string_in
                        ind += 1 # len(list_out) == ind == 1
                    else:
                        list_out[ind-1] = list_out[ind-1] + c # append char to last item in list
                        last = ''
            else: # ind was incremented when blank space found in string_in
                    list_out.append(c) # first char of new item in list_out
                    last = ''

        return(list_out)



