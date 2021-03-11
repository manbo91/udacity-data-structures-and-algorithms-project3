def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
        ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return (None, None)

    minimum = float('inf')
    maximum = float('-inf')

    for num in ints:
        if num < minimum:
            minimum = num

        if num > maximum:
            maximum = num

    return (minimum, maximum)


import random

l = [i for i in range(0, 10)]
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((None, None) == get_min_max([])) else "Fail")
print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print("Pass" if ((2, 2) == get_min_max([2,2,2,2,2,2])) else "Fail")
print("Pass" if ((0, 2) == get_min_max([0,2,1,1,0,2])) else "Fail")
