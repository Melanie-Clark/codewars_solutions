"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""


def high(x):
    longest_sum = 0
    longest_word = ""
    for word in x.split():
        total = sum(ord(char) - 96 for char in word)

        if total > longest_sum:
            longest_word = word
            longest_sum = total
    return longest_word

# total refactpred from:
# sum = 0
# for char in word:
#     sum += ord(char) - 96