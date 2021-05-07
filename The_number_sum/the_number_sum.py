array = [-5, 0, 1, -4, 3, 5, 4, 6, 9, 11]

# O(n^2) time | O(1) space


def twoNumberSum1(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


num1, num2 = twoNumberSum1(array, 11)
print('twoNumberSum1', num1, num2)

# O(n) time | O(n) space


def twoNumberSum2(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [targetSum - num, num]
        else:
            nums[num] = True

    return []


num1, num2 = twoNumberSum2(array, 11)
print('twoNumberSum2', num1, num2)

# O(nlog(n)) | O(1) space


def twoNumberSum3(array, targetSum):
    # O(nlogn)
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1

    return []


num1, num2 = twoNumberSum3(array, 11)
print('twoNumberSum3', num1, num2)
