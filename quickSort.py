def partition(alist, first, last):
    print("Sorting subarray %s" % alist[first: last])
    
    pivotValue = alist[first]
    print("Sorting with pivot value %s" % pivotValue)

    sorted = False
    leftCursor = first + 1
    rightCursor = last
    while not sorted:
        #move leftCursor
        while alist[leftCursor] <= pivotValue and leftCursor <= rightCursor:
            leftCursor = leftCursor + 1
        
        #move rightCursor
        while alist[rightCursor] >= pivotValue and rightCursor >= leftCursor:
            rightCursor = rightCursor - 1
        
        #done if crossed
        if rightCursor < leftCursor:
            sorted = True
        else: #swap when not crossed
            alist[leftCursor], alist[rightCursor] = alist[rightCursor], alist[leftCursor]
    
    #swap values with pivot if found split
    alist[rightCursor], alist[first] = pivotValue, alist[rightCursor]

    print("Sorted subarray %s" % alist[first: last])

    return rightCursor

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)



alist = [54,26,93,17,77,31,44,55,20]
print('Before ' + str(alist))
quickSort(alist)
print('After ' + str(alist))