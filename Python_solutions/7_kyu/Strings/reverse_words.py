"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""

def reverse_words(text):
    reversed_text = []
    split_text = text.split(' ')
    for word in split_text:
        reversed_text.append(word[::-1])
    return " ".join(reversed_text)


# regex:
import re

def reverse_words2(text):
    reversed_text = []
    split_text = re.split("\s", text)
    for word in split_text:
        reversed_text.append(word[::-1])
    return " ".join(reversed_text)
