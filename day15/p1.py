with open("input.txt") as file:
    steps = file.read().replace("\n", "").split(",")
    steps = [s for s in steps if s]


def apply_hash(s: str) -> int:
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value = value % 256
    return value


total = 0
for s in steps:
    total += apply_hash(s)
print(total)
