"""
Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown as the number 0.

"""

def neutralise(s1, s2):
    new_string = ''
    i = 0

    while i < len(s1):
        if s1[i] == s2[i]:
            new_string += s1[i]
        else:
            new_string += '0'
        i += 1
    return new_string