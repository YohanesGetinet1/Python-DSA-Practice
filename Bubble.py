#!/usr/bin/python3
def BubbleSort(array):
    n = len(array)
    for i in range(n):
        is_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j +1]:
                array[j],array[j + 1] = array[j + 1] ,array[j]
                is_sorted = False
        if is_sorted:
            break
    return array


array = [4,8,2,1,3,10,6,15,5,7]
sorted_array =BubbleSort(array)
print(sorted_array)
