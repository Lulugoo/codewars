def find_short(s):
    words = s.split(' ')
    #print(words) #debugging
    words.sort(key=len) #it sorts strings from shortest to longest
    #print(words[0]) #debugging
    #print(len(words[0])) #debugging
    return len(words[0])
