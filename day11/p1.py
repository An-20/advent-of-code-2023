import typing


with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [list(l) for l in lines if l]


def expand(l: typing.List[typing.List[str]]):
    rows = []
    for line in l:
        if all(x == "." for x in line):
            rows.append(["."] * len(line))
        rows.append(line)
    return rows


def transpose(l: typing.List[typing.List[str]]):
    return list(map(list, zip(*l)))


lines = expand(lines)
t = transpose(lines)
lines = transpose(expand(t))

galaxies = []
for row_idx, row in enumerate(lines):
    for col_idx, char in enumerate(row):
        if char == "#":
            galaxies.append((col_idx, row_idx))


total = 0
for galaxy_1 in range(len(galaxies)):
    for galaxy_2 in range(galaxy_1 + 1, len(galaxies)):
        g1x, g1y = galaxies[galaxy_1]
        g2x, g2y = galaxies[galaxy_2]
        dx = abs(g1x - g2x)
        dy = abs(g1y - g2y)
        total += dx + dy

print(total)
