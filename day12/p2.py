from typing import Tuple
from functools import lru_cache

with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]
    data = [
        (
            ((line.split(" ")[0] + "?") * 5)[:-1],
            tuple([int(x) for x in line.split(" ")[1].split(",")] * 5)
        )
        for line in lines
    ]


@lru_cache(maxsize=None)
def count(rem_springs: str, rem_blocks: Tuple[int]) -> int:
    num_unknown = rem_springs.count("?")
    num_damaged = rem_springs.count("#")
    num_damaged_rem = sum(rem_blocks)

    if num_damaged_rem > num_unknown + num_damaged:
        return 0  # base case: sum of blocks is not achievable with remaining springs

    if not num_damaged_rem:
        if num_damaged == 0:
            return 1  # base case: no more blocks, no more damaged springs left
        else:
            return 0  # base case: no more blocks, but damaged springs remain (impossible)

    char = rem_springs[0]
    total = 0
    if char in ".?":
        total += count(rem_springs[1:], rem_blocks)

    if char in "#?":
        # start of a new block
        block_len = rem_blocks[0]
        if all(x in "#?" for x in rem_springs[:block_len]):
            is_valid_last_block = len(rem_springs) == block_len and len(rem_blocks) == 1
            is_valid_next_char = len(rem_springs) > block_len and rem_springs[block_len] in ".?"
            if is_valid_last_block or is_valid_next_char:
                total += count(rem_springs[block_len + 1:], rem_blocks[1:])

    return total


total = 0
for springs, blocks in data:
    print(springs, blocks, count(springs, blocks))
    total += count(springs, blocks)
print(total)
