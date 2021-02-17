
def mergeSort(array):
  if len(array) == 1:
    return array
  
  mid_index = len(array) // 2
  leftHalf = array[0:mid_index]
  rightHalf = array[mid_index:]

  return mergeTwoArrays(mergeSort(leftHalf), mergeSort(rightHalf))


def mergeTwoArrays(leftHalf, rightHalf):
  sortedArray = [None] * (len(leftHalf) + len(rightHalf))
  k = i = j = 0

  while i < len(leftHalf) and j < len(rightHalf):
    if leftHalf[i] <= rightHalf[j]:
      sortedArray[k] = leftHalf[i]
      i += 1
    else:
      sortedArray[k] = rightHalf[j]
      j += 1
    k += 1
  
  while i < len(leftHalf):
    sortedArray[k] = leftHalf[i]
    i += 1
    k += 1
  
  while j < len(rightHalf):
    sortedArray[k] = rightHalf[j]
    j += 1
    k += 1
  return sortedArray

sortedArr = mergeSort([1, 7, 15, 3, 4])
print(sortedArr)