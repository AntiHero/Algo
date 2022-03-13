array = [-5, 0, 1, -4, 3, 5, 4, 6, 9, 11]


# O(n^2) time | O(1) space
def two_number_sum1(arr, target_sum):
    for i in range(len(arr) - 1):
        first_num = arr[i]
        for j in range(i + 1, len(arr)):
            second_num = arr[j]
            if first_num + second_num == target_sum:
                return [first_num, second_num]
    return []


num1, num2 = two_number_sum1(array, 11)
print('two_number_sum1', num1, num2)


# O(n) time | O(n) space
def two_number_sum2(arr, target_sum):
    nums = {}
    for num in arr:
        potential_match = target_sum - num
        if potential_match in nums:
            return [target_sum - num, num]
        else:
            nums[num] = True

    return []


num1, num2 = two_number_sum2(array, 11)
print('two_number_sum2', num1, num2)


# O(nlog(n)) | O(1) space
def two_number_sum3(arr, target_sum):
    # O(nlogn)
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [arr[left], arr[right]]
        elif current_sum < target_sum:
            left += 1
        elif current_sum > target_sum:
            right -= 1

    return []


num1, num2 = two_number_sum3(array, 11)
print('two_number_sum3', num1, num2)
