"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
"""

def high_and_low(numbers: str) -> str:
    num_list = [int(n) for n in numbers.split(" ")]
    return f"{max(num_list)} {min(num_list)}"