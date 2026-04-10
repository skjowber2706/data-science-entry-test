def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Search for all occurrences of find_val in lst
    - Replace them with replace_val
    - Return the modified list
    """

    # check if input is a list
    if type(lst) != list:
        print("Input must be a list")
        return

    # loop through the list
    for i in range(len(lst)):
        # check if current item matches find_val
        if lst[i] == find_val:
            lst[i] = replace_val  # replace it

    return lst


# Task 2: testing the function

# Test case 1
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(result1)

# Test case 2
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print(result2)
