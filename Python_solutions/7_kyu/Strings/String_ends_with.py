"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true

"""

def solution(text, ending):
    return text[-len(ending):] == ending

# Alternative solution:
def solution2(string, ending):
    return string.endswith(ending)