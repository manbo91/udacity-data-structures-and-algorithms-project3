def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
        input_list(array), number(int): Input array to search and the target
    Returns:
        int: Index or -1
    """
    start_index = 0
    end_index = len(input_list) - 1
    return search_recursive(input_list, number, start_index, end_index)


def search_recursive(arr, number, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = arr[mid_index]
    if mid_element == number:
        return mid_index

    start_element = arr[start_index]
    if start_element == number:
        return start_index

    end_element = arr[end_index]
    if end_element == number:
        return end_index

    if start_element > end_element:
        if arr[mid_index - 1] < mid_element < arr[mid_index + 1]:
            if start_element > mid_element:
                if number > mid_element and number < end_element:
                    return search_recursive(arr, number, mid_index + 1, end_index - 1)
                else:
                    return search_recursive(arr, number, start_index + 1, mid_index - 1)
            else:
                if number < mid_element and number > start_element:
                    return search_recursive(arr, number, start_index + 1, mid_index - 1)
                else:
                    return search_recursive(arr, number, mid_index + 1, end_index - 1)
        else:
            if mid_element > arr[mid_index - 1] and mid_element > arr[mid_index + 1]:
                if number < start_element:
                    return search_recursive(arr, number, mid_index + 1, end_index - 1)
                else:
                    return search_recursive(arr, number, start_index + 1, mid_index - 1)
            else:
                if number > end_element:
                    return search_recursive(arr, number, start_index + 1, mid_index - 1)
                else:
                    return search_recursive(arr, number, mid_index + 1, end_index - 1)
    else:
        if number < mid_element:
            return search_recursive(arr, number, start_index + 1, mid_index - 1)
        else:
            return search_recursive(arr, number, mid_index + 1, end_index - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# edge case
test_function([[], 0])
test_function([[2, 4, 8, 10, 12, 14, 16, 18, 20, 1], 20])
test_function([[20, 1, 2, 4, 8, 10, 12, 14, 16, 18], 1])
test_function([[1, 2, 3, 4, 5], 4])
