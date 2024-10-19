"""
n this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters (everything else), as follows.

The order is: uppercase letters, lowercase letters, numbers and special characters.

"*'&ABCDabcde12345" --> [ 4, 5, 5, 3 ]

"""

def solve(s: str) -> int:
    upper = sum(1 for i in s if i.isupper())
    lower = sum(1 for i in s if i.islower())
    numeric = sum(1 for i in s if i.isnumeric())
    special_char = sum(1 for i in s if not i.isalnum())
    return [upper, lower, numeric, special_char]