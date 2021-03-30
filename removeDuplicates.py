#the function just deletes non unique values
def removeDuplicatesByDelete(array):
    if len(array) == 0:
        return []
    first = 1
    last = 0
    while first <= len(array):
        if array[first] == array[last]:
            del array[last]
        first += 1
        last += 1
    return array

#the function returns new length or array and within that length elements will be unique.
#beyond the new length the elements can be removed
def removeDuplicatesWithTwoPointers(arr):
    last_unique = 0
    i = 1
    while i < len(arr):
        if arr[last_unique] != arr[i]:
            last_unique += 1
            arr[last_unique] = arr[i]
        i += 1
    print(arr)
    return last_unique + 1
        

print(removeDuplicatesWithTwoPointers([2, 2, 3, 3, 6, 9, 9]))
print(removeDuplicatesWithTwoPointers([0,0,1,1,1,2,2,3,3,4]))