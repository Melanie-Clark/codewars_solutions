"""
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even
numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]

"""

def sort_array(source_array):
    sorted_array = sorted([s for s in source_array if s % 2 != 0])
    count = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = sorted_array[count]
            count += 1
    return source_array
