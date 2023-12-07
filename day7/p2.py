import itertools
import collections
from functools import lru_cache, cmp_to_key


with open("input.txt") as file:
    lines = file.read().split("\n")
lines = [line.split(" ") for line in lines if line]
lines = [[line[0], int(line[1])] for line in lines]


@lru_cache(maxsize=759375)
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


@lru_cache(maxsize=1000)
def get_best_type(hand):
    CAND_VALUES = "AKQT9897654321J"
    CAND_VALUES_LEN = 15
    jokers = len([x for x in hand if x == "J"])
    if not jokers:
        return get_type(hand)

    hand = [x for x in hand if x != "J"]
    current_max = 0
    for joker_combination in itertools.product(*([CAND_VALUES] * jokers)):
        cand_hand = "".join(hand)
        for joker in range(jokers):
            cand_hand = cand_hand + joker_combination[joker]
        hand_type = get_type(cand_hand)
        if hand_type > current_max:
            current_max = hand_type
    return current_max


def compare(hand1, hand2):
    VALUES = {"A": 14, "K": 13, "Q": 12, "T": 10, "J": 1}
    t1 = get_best_type(hand1[0])
    t2 = get_best_type(hand2[0])
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

# VERY SLOW
# probably because every comparison triggers a re-evaluation of how "good" a hand is, this is partially alleviated
# with the lru_cache but stil it would be better to pre-compute "keys" to sort by.
# regardless it runs in about 2 seconds so not going to bother fixing
lines.sort(key=cmp_to_key(compare))
lines.reverse()
total = 0
for idx, val in enumerate(lines):
    total += (idx + 1) * val[1]
print(total)
