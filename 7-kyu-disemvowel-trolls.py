def disemvowel(string_):
    vowels = ('a','A','e','E','i','I','o','O','u','U') #we create the list of vowels
    new_string = string_ #this ones a bit weird, but trust me, we will adjust new string later
    for wow in string_: #iterate, you can use debugging part to see what's happening at each step
        #print(wow) #debugging
        if wow in vowels: #check for each vowel within iterated string
            #print(wow) #debugging
            new_string = new_string.replace(wow,'') #simply replacing new string vowels that we found with nothingness ''
            #print(new_string) #debugging
    return new_string #final result


    #need to remove all vowels from the string
    #y is not considered a vowel
    #lower and cap letters - remember!
