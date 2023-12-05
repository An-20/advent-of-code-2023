import math

with open("input.txt") as file:
    sections = file.read().split("\n\n")

# parse
sections = [s.split(":")[1] for s in sections]
seeds = sections[0]
seeds = [int(x) for x in seeds.split(" ") if x]
sections = [[[int(y) for y in x.split(" ") if y] for x in section.split("\n") if x] for section in sections[1:]]
sections = [sorted(s, key=lambda x: x[1]) for s in sections]

# sections = [s.replace("\n", " ") for s in sections][1:]
# sections = [[int(x) for x in section.split("")] for section in sections]


def get_mapping_result(mapping, value) -> int:
    for sub_mapping in mapping:
        dest, src, range_len = sub_mapping
        if src <= value < src + range_len:
            return dest + value - src
    return value


lowest = math.inf
for seed in seeds:
    last = seed
    for mapping in sections:
        last = get_mapping_result(mapping, last)
    if last < lowest:
        lowest = last
print(lowest)
