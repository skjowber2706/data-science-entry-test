def string_reverse(s):
    """
    Task 1
    - reverse a given string
    - s must be a string
    - return the reversed string
    """

    # cheking if input is a string
    if type(s) != str:
        print("Input must be a string")
        return

    # creating empty string to store result
    reversed_str = ""

    # looping throug the string from end to start
    for i in range(len(s) - 1, -1, -1):
        reversed_str = reversed_str + s[i]  # adding each char

    return reversed_str


# Task 2: runing the function

# test case 1
result1 = string_reverse("Hello World")
print(result1)

# test case 2
result2 = string_reverse("Python")
print(result2)
