with open("input.txt") as file:
    sections = file.read().split("\n\n")

# parse
sections = [s.split(":")[1] for s in sections]
seeds = sections[0]
seeds = [int(x) for x in seeds.split(" ") if x]
seeds = list(zip(seeds[::2], seeds[1::2]))
sections = [[[int(y) for y in x.split(" ") if y] for x in section.split("\n") if x] for section in sections[1:]]
sections = [sorted(s, key=lambda x: x[1]) for s in sections]
sections = list(reversed(sections))

# sections = [s.replace("\n", " ") for s in sections][1:]
# sections = [[int(x) for x in section.split("")] for section in sections]


def get_mapping_result(mapping, value) -> int:
    for sub_mapping in mapping:
        dest, src, range_len = sub_mapping
        if dest <= value < dest + range_len:
            return src + value - dest
    return value


def check_if_in_seed_range(seed, pairs) -> bool:
    for pair in pairs:
        range_start, range_len = pair
        if range_start <= seed < range_start + range_len:
            return True
    return False


location = 0
while True:
    last = location
    for mapping in sections:
        last = get_mapping_result(mapping, last)
    if check_if_in_seed_range(last, seeds):
        print(location)
        break
    location += 1
