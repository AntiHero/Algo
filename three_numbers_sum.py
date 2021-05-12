array = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0


# O(n^2) time | O(n) space
def three_numbers_sum(arr, target_sum):
    # O(nlog(n))
    arr.sort()

    r_pointer = len(arr) - 1
    l_pointer = 1
    c_pointer = 0

    triplets = []

    while c_pointer < len(arr) - 2:
        nums_sum = arr[r_pointer] + arr[l_pointer] + arr[c_pointer]
        if nums_sum == target_sum:
            triplets.append([arr[l_pointer], arr[c_pointer], arr[r_pointer]])
            l_pointer += 1
            r_pointer -= 1

        elif nums_sum > target_sum:
            r_pointer -= 1

        else:
            l_pointer += 1

        if l_pointer >= r_pointer:
            r_pointer = len(arr) - 1
            c_pointer += 1
            l_pointer = c_pointer + 1

    return triplets


print('three numbers sum', three_numbers_sum(array, target))


def three_numbers_sum2(arr, target_sum):
    arr.sort()
    triplets = []

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target_sum:
                triplets.append([arr[left], arr[i], arr[right]])
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return triplets


print('three numbers sum2', three_numbers_sum2(array, target))
