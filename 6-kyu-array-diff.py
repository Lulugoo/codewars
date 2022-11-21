def array_diff(a, b):
    for no in b:
        if no in a:
            for times in range(a.count(no)):
                # print(times) #debugging
                # print(a.count(no)) #debugging
                a.remove(no)
    # print(a) #debugging
    return a

    # basically need remove all occurances of b in a list
