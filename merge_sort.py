array = [8, 5, 2, 9, 5, 6, 3]


# O(n*log(n)) time | O(n*log(n)) space
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle_idx = len(arr) // 2
    left_half = arr[:middle_idx]
    right_half = arr[middle_idx:]
    return merge_sorted_arrays(merge_sort(left_half), merge_sort(right_half))


def merge_sorted_arrays(left_half, right_half):
    sorted_array = [None for i in range(len(left_half) + len(right_half))]

    """
    k - current index in a sorted array
    i - current index in a left half
    j - current index in a right half
    """
    k = i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_array[k] = left_half[i]
            i += 1
        else:
            sorted_array[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        sorted_array[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        sorted_array[k] = right_half[j]
        j += 1
        k += 1

    return sorted_array


print('merge sort', merge_sort(array))


# O(n*log(n)) time | O(n) space
def merge_sort_in_place(arr):
    if len(arr) <= 1:
        return arr

    auxiliary_arr = arr[:]
    merge_sort_helper(arr, auxiliary_arr, 0, len(arr) - 1)
    return arr


def merge_sort_helper(main_arr, auxiliary_arr, start_idx, end_idx):
    if start_idx == end_idx:
        return

    middle_idx = (start_idx + end_idx) // 2
    merge_sort_helper(auxiliary_arr, main_arr, start_idx, middle_idx)
    merge_sort_helper(auxiliary_arr, main_arr, middle_idx + 1, end_idx)
    do_merge(main_arr, auxiliary_arr, start_idx, middle_idx, end_idx)


def do_merge(main_arr, auxiliary_arr, start_idx, middle_idx, end_idx):
    k = start_idx
    i = start_idx
    j = middle_idx + 1

    while i <= middle_idx and j <= end_idx:
        if auxiliary_arr[i] <= auxiliary_arr[j]:
            main_arr[k] = auxiliary_arr[i]
            i += 1
        else:
            main_arr[k] = auxiliary_arr[j]
            j += 1

        k += 1

    while i <= middle_idx:
        main_arr[k] = auxiliary_arr[i]
        i += 1
        k += 1

    while j <= end_idx:
        main_arr[k] = auxiliary_arr[j]
        j += 1
        k += 1



print('original array', array)
print('merge sort in place', merge_sort_in_place(array))
