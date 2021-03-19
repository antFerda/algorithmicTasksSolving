
def findThreeLargest(alist):
    temp_largest = [None, None, None]
    for num in a:
        checkLargerAndReplace(temp_largest, num)
    return temp_largest

def checkLargerAndReplace(temp_largest, num):
    for i in range(2, -1, -1):
        if temp_largest[i] == None or temp_largest[i] < num:
            return shiftAndAppend(num, i, temp_largest)

def shiftAndAppend(num, idx, temp_largest):
    if idx == 0:
        temp_largest[0] = num
    if idx == 1:
        temp_largest[0] = temp_largest[1]
        temp_largest[1] = num
    if idx == 2:
        temp_largest[0] = temp_largest[1]
        temp_largest[1] = temp_largest[2]
        temp_largest[2] = num
    return temp_largest


a = [1, 3, -1, -5, 99, 22, -12]
print(findThreeLargest(a))