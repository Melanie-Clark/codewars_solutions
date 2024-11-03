"""
Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""

def disemvowel(string_) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join(letter for letter in string_ if letter.lower() not in vowels)