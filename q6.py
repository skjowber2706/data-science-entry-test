def find_first_negative(lst):
    """
    Task 1
    - find the first negative number in list
    - use while loop
    - return number or "No negatives"
    """

    # cheking if input is a list
    if type(lst) != list:
        print("Input must be a list")
        return

    i = 0  # starting index

    # looping throug the list using while
    while i < len(lst):
        # cheking if number is negative
        if lst[i] < 0:
            return lst[i]  # return first negative

        i = i + 1  # move to next index

    # if no negative found
    return "No negatives"


# Task 2: runing the function

# test case 1
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print(result1)

# test case 2
result2 = find_first_negative([2, 10, 7, 0])
print(result2)
