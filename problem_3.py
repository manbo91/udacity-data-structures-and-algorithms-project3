def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
        input_list(list): Input List
    Returns:
        (int),(int): Two maximum sums
    """
    n = len(input_list)

    if n < 2:
        return []

    for i in range(n, -1, -1):
        heapify(input_list, n, i)

    maximum_sums_list = [[], []]

    for i in range(n - 1, -1, -1):
        largest_element = input_list[0]
        input_list[i], input_list[0] = input_list[0], input_list[i]
        heapify(input_list, i, 0)

        if len(maximum_sums_list[0]) == len(maximum_sums_list[1]):
            maximum_sums_list[0].append(str(largest_element))
        else:
            maximum_sums_list[1].append(str(largest_element))

    return [int("".join(arr)) for arr in maximum_sums_list]


def heapify(arr, n, i):
    largest_index = i
    left_node = i * 2 + 1
    right_node = i * 2 + 2

    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]
        heapify(arr, n, largest_index)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case = [[0, 0, 0], [0, 0]]
test_function(test_case)

test_case = [[], []]
test_function(test_case)

test_case = [[1], []]
test_function(test_case)
