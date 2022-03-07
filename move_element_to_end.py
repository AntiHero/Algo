from shutil import move


# O(n) time | O(1) space
def move_element_to_end(array, element):
    i = 0
    j = len(array) - 1

    while i < j:
        while i < j and array[j] == element:
            j -= 1

        if array[i] == element:
            array[j], array[i] = array[i], array[j]

        i += 1

    return array


arr = [1, 2, 3, 2, 2, 2, 4, 2, 2]

print(move_element_to_end(arr, 2))
