def quicksort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
arr1 = [5,6,1,5,6,2,3,9,10,55,14,62,859]
print("first test: ", quicksort(arr1))

import random

def create_random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    
    rd_list = []
    for i in range(length):
        rd_list.append(random.randint(start, stop))
    return rd_list

arr2 = create_random_int_list(1, 1000, 100)
print("second test: ", quicksort(arr2))