def likes(names):
    returnedText = ''

    if (len(names) == 0):
        returnedText = 'no one likes this'
    elif (len(names) == 1):
        returnedText = str(names[0]) + ' likes this'
    elif (len(names) > 1 and len(names) < 4):
        for name in range(0, len(names) - 1):
            returnedText = returnedText + names[name] + ', '
        returnedText = returnedText[:-2]
        returnedText = returnedText + ' and ' + str(names[len(names) - 1]) + ' like this'
    else:
        for name in range(0, 2):
            returnedText = returnedText + names[name] + ', '
        returnedText = returnedText[:-2]
        returnedText = returnedText + ' and ' + str(len(names) - 2) + ' others like this'
    return returnedText

# need to prep like system
# none for empty, name when 1, names when 2, names when 3, and 2 names plus number when 4 or more
# given string in the list, return string with names and numbers.
