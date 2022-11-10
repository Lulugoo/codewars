import collections

def find_it(seq):
    if len( seq ) == 0: # edge case defined in advance
        return None
    b = collections.Counter(seq) #great module to track stuff inside the sequence with Counter imported from Collections
    #print (b) #debugging
    for c in b:
        #print (c) #debugging
        if b[c] % 2 == 1: #finding the odd number
            #print(b[c]) #debugging - number of times appears c
            #print (c) #debugging - final result c
            return c
            
    #need to count how many times int in the given list appears
    #if odd times - return
    #there is always only one int that appears odd number of times
