"""
Given an array of numbers representing votes given to each of the candidates, and an integer which is equal to the number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win the election.

The winner of the election must secure strictly more votes than any other candidate. If two or more candidates receive the same (maximum) number of votes, assume there is no winner at all.

Note: big arrays will be tested.

Examples
votes = [2, 3, 5, 2]
voters = 3

result = 2
Candidate #3 may win, because he's already leading.
Candidate #2 may win, because with 3 additional votes he may become the new leader.
Candidates #1 and #4 have no chance, because in the best case scenario each of them can only tie with the candidate #3.
"""

# O(n log n):
def elections_winners(votes, k):
    sorted_votes = sorted(votes, reverse=True)
    max_votes = max(sorted_votes)

    if k == 0 and (sorted_votes[0] != sorted_votes[1]):
        return 1
    else:
        return sum(candidate + k > max_votes for candidate in sorted_votes)

# O(n):
def elections_winners2(votes, k):
    max_votes = max(votes)
    return sum(candidate + k > max_votes for candidate in votes) or votes.count(max_votes) == 1