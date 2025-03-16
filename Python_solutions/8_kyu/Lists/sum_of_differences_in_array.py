"""
Your task is to sum the differences between consecutive pairs in the array in descending order.

Example
[2, 1, 10]  -->  9
In descending order: [10, 2, 1]

Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9
"""

def sum_of_differences(arr):
    sorted_arr = sorted(arr, reverse=True)
    return sum([sorted_arr[i] - (sorted_arr[i + 1]) for i in range(len(sorted_arr)-1)])