def swap(array, firstIndex, secondIndex):
  temp = array[firstIndex]
  array[firstIndex] = array[secondIndex]
  array[secondIndex] = temp

  
def indexOfMinimum(array, startIndex):
  minValue = array[startIndex]
  minIndex = startIndex

  for i in range(minIndex + 1,len(array)):
    if array[i] < minValue:
      minIndex = i
      minValue = array[i]
  return minIndex


def selectionSort(array):
  # Write this method
  for i in range(len(array)):
    swap(array, i, indexOfMinimum(array, i))
  return array


print(selectionSort([1, 5, 6, 4]))