import typing


def transpose(l: typing.List[typing.List[str]]):
    return list(map(list, zip(*l)))


with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [list(l) for l in lines if l]


expanded_rows = []
row_count = 0
for row_idx, row in enumerate(lines):
    if all(x == "." for x in row):
        row_count += 1000000
    else:
        row_count += 1
    expanded_rows.append(row_count)

expanded_cols = []
col_count = 0
for col_idx in range(len(lines[0])):
    if all(lines[x][col_idx] == "." for x in range(len(lines))):
        col_count += 1000000
    else:
        col_count += 1
    expanded_cols.append(col_count)


# expanded_rows = []
# expanded_cols = []
# row_count = 0
# for row_idx, row in enumerate(lines):
#     if all(x == "." for x in row):
#         expanded_rows.append(row_idx)
#
# for col_idx in range(len(lines[0])):
#     if all(lines[x][col_idx] == "." for x in range(len(lines))):
#         expanded_cols.append(col_idx)


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
        dx = abs(expanded_cols[g1x] - expanded_cols[g2x])
        dy = abs(expanded_rows[g1y] - expanded_rows[g2y])
        total += dx + dy

print(total)
