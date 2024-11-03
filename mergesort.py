import math

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    middle = math.floor(len(arr) / 2)
    
    left, right = arr[:middle], arr[middle:]
    
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    while left and right:
        elem = left.pop(0) if left[0] <= right[0] else right.pop(0)
        result.append(elem)
        
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
        
    return result

arr1 = [5,6,1,5,6,2,3,9,10,55,14,62,859]
print("first test: ", merge_sort(arr1))

import random

def create_random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    
    rd_list = []
    for i in range(length):
        rd_list.append(random.randint(start, stop))
    return rd_list

arr2 = create_random_int_list(1, 1000, 100)
print("second test: ", merge_sort(arr2))