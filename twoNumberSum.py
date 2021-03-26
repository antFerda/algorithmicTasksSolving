
#создадим hashtable со всеми значениями из листа
#будем проходит по значениям и высчитывать значение которое нужно для суммы (y = sum - x)
#затем проверяем по константному времени, содержится ли в хэштейбл число y
#если значение найдено, но мы нашли пару
def findPairs(l, sum):
    st = dict()
    result = []

    for x in l:
        st[x] = None
    for x in st:
        y = sum - x
        if y in st:
            result.append((x, y))
    
    print(result)
    return result


a = [-1, 4, 5, 8, 0, 2, 6, 9]

#find all pairs that sums up to 10
findPairs(a, 10)

#find all pairs that sums up to 8
findPairs(a, 8)