
#1 solution
    #берем все отрицательные
    #сортируем как будто они положительные
    #возводим в квадрат
    # N + NLog(N) + N
#2 solution
    #1 iteration если начальное число по модулю больше чем последнее в конце, то двигаем его в конец, и двигаем поинтеры с двух сторон
    #2 iteration если начальное меньше чем число с конца. то двигаем ток последний поинтер
    #3 если равно два значения, то двигаем оба поинтера и перекидываем отрицат
    #4 если осталось одно число, оно будет первым
    #time: O(N), space O(N)
def square_and_sort(arr):
    left = 0
    right = len(arr) - 1
    
    squares = [0 for x in range(len(arr))]
    last = len(arr) - 1
    while last >= 0:
        left_value = arr[left]
        right_value = arr[right]
        
        diff = abs(left_value) - abs(right_value)
        if diff > 0:
            squares[last] = left_value * left_value
            left += 1
        else:
            squares[last] = right_value * right_value
            right -= 1
        last -= 1
    print(squares)
    return squares

square_and_sort([-22, -1, 0, 1, 2, 4]) # [0, 0, 0, 0, 0, 22^2]
square_and_sort([0, 1, 2, 4])