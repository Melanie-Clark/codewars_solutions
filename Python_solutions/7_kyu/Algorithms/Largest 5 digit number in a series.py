"""
In the following 6 digit number:

283910
91 is the greatest sequence of 2 consecutive digits.

In the following 10 digit number:

1234567890
67890 is the greatest sequence of 5 consecutive digits.

"""

def solution(digits):
    start_point = 0
    end_point = 5
    max_number = 0
    while end_point < len(digits) + 1:
        five_digit_number = int(digits[start_point:end_point])
        print(five_digit_number)
        if max_number < five_digit_number:
            max_number = five_digit_number
        start_point += 1
        end_point += 1
    return max_number

# for loop is more efficient:
def solution(digits):
    max_number = 0
    for i in range(0, len(digits)-4):
        five_digit_number = int(digits[i:i+5])
        if five_digit_number > max_number:
            max_number = five_digit_number
    return max_number