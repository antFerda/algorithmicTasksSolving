def smallest_subarray_sum(s, arr):
  smallestNumber = -1
  for i in range(0, len(arr)):
    if arr[i] >= s:
      smallestNumber = 1
      break
    if i == len(arr):
      continue
    
    for j in range(i, len(arr)):
      subArray = arr[i:j+1]
      print(subArray)
      print("Values of index i: {0}, j:{1}".format(i, j))
      sumOfSubArray = sum(subArray)
      
      if sumOfSubArray == s:
        localSmallestNumber = j + 1 - i
        if localSmallestNumber < smallestNumber or smallestNumber == -1:
          smallestNumber = localSmallestNumber
          print(smallestNumber)
  
  return smallestNumber


def main():
  print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))


main()