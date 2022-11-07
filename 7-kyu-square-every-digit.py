def square_digits(num):
    final = ''    #
    for no in str(num):
        final += str(int(no) ** 2)
    return int(final)

    #since we get an input as int we need to transfer it to str - done
    #then we loop and square each number as a string - done
    #then we need to double that number as an int, but keeping as a str cause otherwise we cannot loop done
    #then we push the result and return it as int done


#variation 2
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
