def power(x, n):
  # base case
  if n == 0:
    return 1
  
  # recursive case: n is negative 
  if n < 0:
    return 1/power(x, (-1)*n)

  # recursive case: n is odd
  if n % 2 != 0:
    return power(x, n - 1) * x

  # recursive case: n is even
  y = power(x, n/2)
  return y * y
