def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in single traversal.

    Args:
        input_list(list): List to be sorted
    """

    n = len(input_list)
    next_0_pos = 0
    next_2_pos = n - 1

    for i in range(len(input_list)):
        if input_list[i] == 2 and i >= next_2_pos:
            break

        if next_2_pos > 0 and input_list[i] == 2:
            while input_list[next_2_pos] == 2:
                next_2_pos -= 1
                if next_2_pos <= i:
                    return input_list

            input_list[i] = input_list[next_2_pos]
            input_list[next_2_pos] = 2
            next_2_pos -= 1

        if next_0_pos < n and input_list[i] == 0:
            input_list[i] = input_list[next_0_pos]
            input_list[next_0_pos] = 0
            next_0_pos += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([
    2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0,
    1
])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


test_function([])
test_function([2, 1, 0])
test_function([2, 2, 0, 0, 1, 1, 2, 2, 0, 0, 1, 1])
