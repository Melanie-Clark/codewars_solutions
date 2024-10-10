"""
Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0.

"""

def move_ten(st):
    new_string = ''

    for letter in st:
        if letter > 'p':
            letter = chr(ord(letter) - 16)
        else:
            letter = chr(ord(letter) + 10)
        new_string += letter

    return new_string