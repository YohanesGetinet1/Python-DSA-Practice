#!/usr/bin/python3

def SelectionSort(Array):
    for i in range (0, len(Array)):
        min = i
        for j in range(i+1,len(Array)):
            if Array[j] < Array[min]:
                min = j
        Array[i],Array[min] = Array[min],Array[i]


Array = [7,5,9,3,8,2,6,1]
SelectionSort(Array)
print(Array)