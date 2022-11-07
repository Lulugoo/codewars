def modify_multiply(st, loc, num):
    newList = st.split()
    findString = newList[loc]
    multiplyString = (findString + '-') * num
    return multiplyString[:-1] # return the whole string except the last character '-'


#string will be given done
#first we need to split the str into list, so that we could locate based on given first int done
#need to find a word locations based on given int - done
#when you locate the word you multiply that word by the last int - done
#plus add hyphen between each word - done
#edge case if string index is out of range - done
