def update_dictionary(dct, key, value):
    """
    Task 1
    - update dictionary with key-value pair
    - if key alredy exist, print old value then update
    - return updated dictionary
    """

    # cheking if input is a dictonary
    if type(dct) != dict:
        print("Input must be a dictionary")
        return

    # cheking if key alredy exist in dictonary
    if key in dct:
        print("Original value:", dct[key])  # print old val

    # updaiting or adding new key-value
    dct[key] = value

    return dct


# Task 2: runing the function

# test case 1
result1 = update_dictionary({}, "name", "Alice")
print(result1)

# test case 2
result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)
