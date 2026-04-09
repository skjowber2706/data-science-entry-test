def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
    #if x is not a number or y is not a number, then return -1
        return -1
    x, y = y, x
    print(f"x = {x}, y = {y}")
    return x, y


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

swap(9,17)
