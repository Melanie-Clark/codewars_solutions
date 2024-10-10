"""
Simple, given a string of words, return the length of the shortest word(s).
"""

def find_short(s):
    list = s.split(' ')
    return min(len(l) for l in list)