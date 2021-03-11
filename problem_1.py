def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
        number(int): Number to find the floored squared root
    Returns:
        int: Floored Square Root
    """
    if number == 0:
        return 0
    if number == 1:
        return 1
    return sprt_recursive(number, 0, number)


def sprt_recursive(number, start_number, end_number):
    if end_number - start_number <= 1:
        return start_number

    mid_number = (start_number + end_number) // 2
    mid_number_pow = mid_number * mid_number

    if number == mid_number_pow:
        return mid_number
    elif number < mid_number_pow:
        return sprt_recursive(number, start_number, mid_number)
    else:
        return sprt_recursive(number, mid_number, end_number)


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (12 == sqrt(144)) else "Fail")
print("Pass" if (22 == sqrt(484)) else "Fail")
print("Pass" if (32 == sqrt(1024)) else "Fail")
print("Pass" if (1024 == sqrt(1048876)) else "Fail")
