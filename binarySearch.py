# Returns either the index of the location in the array,
#  or -1 if the array did not contain the targetValue
def doSearch(array, targetValue, min = 0, max = 0):
  if max == 0:
    max = len(array) - 1
  print(array)
  print('Looking for target %d with min %d and max %d' % (targetValue, min, max))

  if max < min:
    return -1

  guess = int(round((max - min)/2, 0)) + min
  print('Our guess index %d and value at guess %d' % (guess, array[guess]))

  if targetValue == array[guess]:
    return guess
  elif targetValue > array[guess]:
    return doSearch(array, targetValue, min = guess + 1, max=max)
  else:
    return doSearch(array, targetValue, min=min, max = guess - 1)
  
  return -1;
