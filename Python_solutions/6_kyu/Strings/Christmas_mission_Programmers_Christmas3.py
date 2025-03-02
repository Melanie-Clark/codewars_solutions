"""
Count how many pairs of the two words "Merry" and "Christmas" appear in the given a string, and return the maximum possible number of pairs (not the numbers of single words).

Notes:

the letters are case-sensitive: M and m are different
you don't need to consider the order (the characters can be shuffled)
Examples
"MerryChristmas"                -->  1  // 1 pair
"ChristmasMerry"                -->  1  // 1 pair
"yrreMsamtsirhC"                -->  1  // 1 pair
"MerryMerry"                    -->  0  // 0 pairs
"ChristmasChristmas"            -->  0  // 0 pairs
"MMeerrrryyCChhrriissttmmaass"  -->  2  // 2 pairs
"MMmmeerrrrrryyCChhiissssttaa"  -->  2  // 2 pairs
"MMmmeerrrryyCChhiissssssttaa"  -->  1  // 1 pair
"""

# Refactored:
def merry_christmas(s):
    m_christmas = "MerryChristmas"
    return min(s.count(char)//m_christmas.count(char) for char in m_christmas)


# original code:
from collections import Counter

def merry_christmas_original(s):
    count = Counter(s)
    merry_christmas_count = Counter("MerryChristmas")

    pairs = 0
    if len(count) >= len(merry_christmas_count):
        for char, value in count.items():
            if char in merry_christmas_count:
                merry_christmas_value = merry_christmas_count.get(char)
                repeated_times = value // merry_christmas_value
                if pairs == 0 or (0 < repeated_times < pairs):
                    pairs = repeated_times
                elif repeated_times < pairs:
                    pairs = 0
                    break
    return pairs