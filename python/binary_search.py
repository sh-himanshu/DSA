"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    value_index = 0
    arr_len = len(input_array)

    while arr_len > 0:
        center_index = int(
            (arr_len / 2) - 1
            if arr_len % 2 == 0
            else (arr_len - 1) / 2
        )

        # found
        if value == input_array[center_index]:
            value_index += center_index
            break

        # not found
        if arr_len == 1:
            value_index = -1
            break

        if value < input_array[center_index]:
            # value is less than the center element
            input_array = input_array[0 : center_index + 1]
        else:
            # value is more than the center element
            input_array = input_array[center_index + 1 : arr_len]
            value_index += center_index + 1

        # update array length
        arr_len = len(input_array)

    return value_index


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
