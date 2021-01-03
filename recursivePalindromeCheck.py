def isPalindrome(str):
  # base case #1
  if len(str) == 0 or len(str) == 1:
    return True
  
  # base case #2
  if str[0] != str[-1]:
    return False
    
  # recursive case
  return isPalindrome(str[1:-1])
