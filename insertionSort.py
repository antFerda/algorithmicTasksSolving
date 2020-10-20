def insert(array, rightIndex, value):
  # Write this method
  print('Adding value %d' % value)

  rightLimit = rightIndex + 1
  sorted_arr = array[0:rightLimit]
  unsorted_arr = array[rightLimit:]

  for i, obj in enumerate(sorted_arr[:]):
    if value <= obj:
      before = sorted_arr[0:i]
      before.append(value)
      sorted_arr = before + sorted_arr[i:]
      break
  if value not in sorted_arr:
    sorted_arr.append(value)
  
  unsorted_arr.remove(value)
  sorted_arr.extend(unsorted_arr)
  print('Returning', sorted_arr)

  array = sorted_arr
  return
