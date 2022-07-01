def find_averages_of_subarrays(n, arr):
    winSum = 0
    winStart = 0
    result = []

    for winEnd in range(len(arr)):
        winSum += arr[winEnd]

        if (winEnd >= n - 1):
            result.append(winSum/n)
            winSum -= arr[winStart]
            winStart += 1

    return result



def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))

main()