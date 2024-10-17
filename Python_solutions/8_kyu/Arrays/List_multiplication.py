"""
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""

def grow(arr):
    multiplied_array = 1
    for a in arr:
        multiplied_array *= a
    return multiplied_array