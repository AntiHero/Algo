arr = [[1, 2, 3, 4, 5, 6],
       [7, 8, 9, 10, 11, 12],
       [13, 14, 15, 16, 17, 18],
       [19, 20, 21, 22, 23, 24]]


# O(n) Time | O(n) space
def spiral_traverse(array):
    result = []
    s_col, s_row = 0, 0
    e_col, e_row = len(array[0]) - 1, len(array) - 1

    while s_row <= e_row and s_col <= e_col:
        for col in range(s_col, e_col + 1):
            result.append(array[s_row][col])

        for row in range(s_row + 1, e_row + 1):
            result.append(array[row][e_col])

        for col in reversed(range(s_col, e_col)):
            result.append(array[e_row][col])

        for row in reversed(range(s_row + 1, e_row)):
            result.append(array[row][s_col])

        s_row += 1
        e_row -= 1
        s_col += 1
        e_col -= 1

    return result


print("spiral traverse:", spiral_traverse(arr))


def recursive_spiral_traverse(array):
    result = []
    spiral_fill(array, result, 0, 0, len(array) - 1, len(array[0]) - 1)

    return result


def spiral_fill(array, result, s_row, s_col, e_row, e_col):
    if s_row <= e_row and s_col <= e_col:
        for col in range(s_col, e_col + 1):
            result.append(array[s_row][col])

        for row in range(s_row + 1, e_row + 1):
            result.append(array[row][e_col])

        for col in reversed(range(s_col, e_col)):
            result.append(array[e_row][col])

        for row in reversed(range(s_row + 1, e_row)):
            result.append(array[row][s_col])
    else:
        return

    spiral_fill(array, result, s_row + 1, s_col + 1, e_row - 1, e_col - 1)


print("spiral traverse:", recursive_spiral_traverse(arr))
