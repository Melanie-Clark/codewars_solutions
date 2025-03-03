"""
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
"Hi!" --> "H!!"
"!Hi! Hi!" --> "!H!! H!!"
"aeiou" --> "!!!!!"
"ABCDE" --> "!BCD!"
"""

def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)