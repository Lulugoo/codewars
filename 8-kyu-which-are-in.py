def in_array(array1, array2):
    arr = []  # step 1. we push results to a new array which is first empty
    for a2 in array2:  # step 2. we loop through the array 2
        for a1 in array1:  # step 3. we nested loop array 1 within array 2
            if a1 in a2 and a1 not in arr:  # step 4. we compare results
                arr.append(a1)  # step 5. if conditions are met we push a1 result to a new array

    return sorted(arr)  # step 6. we return an array.
