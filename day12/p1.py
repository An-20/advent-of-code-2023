"""
Is this a bad part 1 solution which runs in exponential time given
the number of ?s... yes.

Did I have to completely rewrite for part 2...
yes
"""

import itertools

with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]

total = 0
for line_idx, line in enumerate(lines):
    springs = list(line.split(" ")[0])
    cont = [int(x) for x in line.split(" ")[1].split(",")]
    unknown_indices = []
    for idx, char in enumerate(springs):
        if char == "?":
            unknown_indices.append(idx)
    unknown_num = len(unknown_indices)

    for unknown_springs in itertools.product(["#", "."], repeat=unknown_num):
        this_springs = springs
        for idx in range(unknown_num):
            this_springs[unknown_indices[idx]] = unknown_springs[idx]

        blocks = []
        block_len = 0
        for char in this_springs:
            if char == "#":
                block_len += 1
            elif char == "." and block_len:
                blocks.append(block_len)
                block_len = 0

        if block_len:
            blocks.append(block_len)

        if blocks == cont:
            total += 1

    print(line_idx)

print(total)
