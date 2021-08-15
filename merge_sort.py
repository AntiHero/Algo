array = [8, 5, 2, 9, 5, 6, 3]


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
