import collections
from functools import cmp_to_key


with open("input.txt") as file:
    lines = file.read().split("\n")
lines = [line.split(" ") for line in lines if line]
lines = [[line[0], int(line[1])] for line in lines]


def get_type(hand):
    c = collections.Counter(hand)
    if len(c) == 1:
        # five of a kind
        return 7
    elif 4 in c.values():
        # four of a kind
        return 6
    elif 3 in c.values():
        if len(c) == 2:
            # full house
            return 5
        else:
            # three of a kind
            return 4
    elif 2 in c.values():
        if len(c) == 3:
            # two pair
            return 3
        else:
            # one pair
            return 2
    return 1  # high card


def compare(hand1, hand2):
    VALUES = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    t1 = get_type(hand1[0])
    t2 = get_type(hand2[0])
    if t1 > t2:
        return -1
    elif t2 >t1:
        return 1
    for c1, c2 in zip(hand1[0], hand2[0]):
        c1 = int(VALUES.get(c1, c1))
        c2 = int(VALUES.get(c2, c2))
        if c1 > c2:
            return -1
        elif c2 > c1:
            return 1
    return 0


lines.sort(key=cmp_to_key(compare))
lines.reverse()
total = 0
for idx, val in enumerate(lines):
    total += (idx + 1) * val[1]
print(total)
