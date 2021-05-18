arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]


# O(n) time | O(1) space
def sub_array_sort(array):
    min_out_of_order = float("inf")
    max_out_of_order = float("-inf")

    for i in range(len(array)):
        num = array[i]
        if is_out_of_order(i, num, array):
            min_out_of_order = min(min_out_of_order, num)
            max_out_of_order = max(max_out_of_order, num)

    if min_out_of_order == float("inf"):
        return [-1, -1]

    sub_arr_left_idx = 0
    while min_out_of_order >= array[sub_arr_left_idx]:
        sub_arr_left_idx += 1

    sub_arr_right_idx = len(array) - 1
    while max_out_of_order <= array[sub_arr_right_idx]:
        sub_arr_right_idx -= 1

    return [sub_arr_left_idx, sub_arr_right_idx]


def is_out_of_order(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]


print("sub_array_sort", sub_array_sort(arr))
