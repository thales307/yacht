from collections import Counter

YACHT = lambda d: 50 if len(set(d)) == 1 else 0
ONES = lambda d: sum(x for x in d if x == 1)
TWOS = lambda d: sum(x for x in d if x == 2)
THREES = lambda d: sum(x for x in d if x == 3)
FOURS = lambda d: sum(x for x in d if x == 4)
FIVES = lambda d: sum(x for x in d if x == 5)
SIXES = lambda d: sum(x for x in d if x == 6)
FULL_HOUSE = (
    lambda d: sum(d)
    if len(set(d)) == 2 and len(set(sorted(d)[1:4])) == 2
    else 0
)
FOUR_OF_A_KIND = (
    lambda d: 4*sorted(d)[1]
    if len(set(d)) <= 2 and len(set(sorted(d)[1:4])) == 1
    else 0
)
LITTLE_STRAIGHT = lambda d: 30 if sorted(d) == list(range(1, 6)) else 0
BIG_STRAIGHT = lambda d: 30 if sorted(d) == list(range(2, 7)) else 0
CHOICE = lambda d: sum(d)

def score(dice, category):
    return category(dice)