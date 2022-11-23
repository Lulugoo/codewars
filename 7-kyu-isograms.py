def is_isogram(string):
    list = [*string.lower()]
    #print(list) #debugging
    setOfElements = set()
    for e in list:
        if e in setOfElements:
            return False
        else:
            setOfElements.add(e)
    return True
    
    #return bolean
    #some edge cases
    #same characters may not be adjacent
    #same characters may not be same case
    #an empty array = isogram
