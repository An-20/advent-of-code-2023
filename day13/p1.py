from typing import List, Optional

with open("input.txt") as file:
    patterns = file.read().split("\n\n")
    patterns = [[l for l in p.split("\n") if l] for p in patterns if p]


def transpose(l: List[str]):
    return list(map(list, zip(*l)))


def get_reflection_idx(p: List[str]) -> Optional[int]:
    for split_idx in range(len(p) - 1):
        matching = 0
        offset = 0
        while True:
            if not (0 <= split_idx - offset and split_idx + offset + 1 < len(p)):
                break
            if p[split_idx - offset] == p[split_idx + offset + 1]:
                matching += 1
            offset += 1
        if matching == offset:
            return split_idx + 1
    return None


def solve(p: List[str]) -> int:
    horizontal = get_reflection_idx(p)
    if horizontal is not None:
        return 100 * horizontal
    return get_reflection_idx(["".join(x) for x in transpose(p)])


total = 0
for idx, pattern in enumerate(patterns):
    total += solve(pattern)
    print(idx, total)
print(total)
