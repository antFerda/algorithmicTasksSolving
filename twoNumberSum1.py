
#time: O(n^2) 
#space: O(1)
def twoNumberSum(array, sum):
    for i in range(len(array) - 1):
        first = array[i]
        for j in range(i + 1, len(array)):
            second = array[j]
            if first + second == sum:
                return first, second


# print(twoNumberSum([1, 8, 5, -1, 10, -5], 5))

# time: O(N)
# space: O(N)
def twoNumberSumDictBased(array, sum):
    nums = dict()
    for number in array:
        potential = sum - number
        if potential in nums:
            return number, potential
        else:
            nums[number] = None
    return ()

# print(twoNumberSumDictBased([1, 8, 5, -1, 10, -5], 5))


# time: O(N * Log(N))
# space: O(1)
def twoNumberSumSorting(array, sum):
    array.sort()
    firstPointer = 0
    secondPointer = len(array) - 1

    while firstPointer < secondPointer:
        firstValue = array[firstPointer]
        secondValue = array[secondPointer]
        potentialSum = firstValue + secondValue
        
        if potentialSum == sum:
            return firstValue, secondValue
        elif potentialSum < sum:
            firstPointer += 1
        elif potentialSum > sum:
            secondPointer -= 1
    return ()

print(twoNumberSumSorting([1, 8, 5, -1, 10, -5], 19))