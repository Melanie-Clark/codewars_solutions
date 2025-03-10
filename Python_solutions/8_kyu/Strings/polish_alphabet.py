"""
There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.

Your task is to change the letters with diacritics:

ą -> a,
ć -> c,
ę -> e,
ł -> l,
ń -> n,
ó -> o,
ś -> s,
ź -> z,
ż -> z
"""

def correct_polish_letters(st):
    return st.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))