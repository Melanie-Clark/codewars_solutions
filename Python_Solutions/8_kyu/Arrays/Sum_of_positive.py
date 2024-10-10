def positive_sum(arr):
    positive_total = 0

    for a in arr:
        if a > 0:
            positive_total += a
    return positive_total