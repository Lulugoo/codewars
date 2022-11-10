def solution(number):
    result = []  # empty list after sum method will return 0 by default

    for num in range(1,
                     number):  #loop all numbers starting from given ending to 1. Range() method helps to create that range of numbers
        if num % 3 == 0 or num % 5 == 0:  # the main condition logic that filters either or
            result.append(num)  # simply append the result
    return sum(result)  # simply sum up all results that is being pushed all together

    # we have a number
    # from 0 to the given number, which numbers are multiples of 3 or 5
    # see the total sum of all multiples
    # need to loop and find all multiples of 3
    # need to loop and find all multiples of 5
    # need to put results in one list and return sum
    # edge case if a number multiple of both 3 and 5 - count once
    # if the number < 0 return 0
