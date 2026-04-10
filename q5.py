def check_divisibility(num, divisor):
    """
    Task 1
    - check if num is divisible by divisor
    - both must be numbers
    - return True or False
    """

    # cheking if inputs are numbers
    if type(num) != int and type(num) != float:
        print("num must be a number")
        return

    if type(divisor) != int and type(divisor) != float:
        print("divisor must be a number")
        return

    # cheking if divisor is zero (cant divide by zero)
    if divisor == 0:
        print("cannot divide by zero")
        return

    # doing the divisibility cheak
    if num % divisor == 0:
        return True
    else:
        return False


# Task 2: runing the function

# test case 1
result1 = check_divisibility(10, 2)
print(result1)

# test case 2
result2 = check_divisibility(7, 3)
print(result2)
