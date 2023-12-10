with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]


start = (0, 0)
for idx, line in enumerate(lines):
    if "S" in line:
        start = (line.index("S"), idx)


ADJ_RULES = {
    "S": [(0, 1), (0, -1), (1, 0), (-1, 0)],
    "|": [(0, 1), (0, -1)],
    "-": [(1, 0), (-1, 0)],
    "L": [(0, 1), (-1, 0)],
    "J": [(0, 1), (1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, -1), (-1, 0)],
    ".": []
}


to_search = [start]
dists = {start: 0}
while to_search:
    to_search = sorted(to_search, key=lambda x: dists[x], reverse=True)
    current = to_search.pop()
    current_dist = dists[current]
    x, y = current
    char = lines[y][x]
    offsets = ADJ_RULES[char]
    offsets = [(-x, -y) for x, y in offsets]
    used_offsets = []
    for offset in offsets:
        dx, dy = offset
        nx = x + dx
        ny = y + dy
        if not 0 <= nx < len(lines[0]):
            continue
        if not 0 <= ny < len(lines):
            continue
        nchar = lines[ny][nx]
        if (nx, ny) not in dists and nchar in ADJ_RULES and offset in ADJ_RULES[nchar]:
            to_search.append((nx, ny))
            dists[(nx, ny)] = current_dist + 1
            if current == start:
                used_offsets.append(offset)

    # small bugfix: we need to identify exactly what sort of pipe S is before doing area calculations
    if current == start:
        used_offsets = [(-x, -y) for x, y in used_offsets]
        for char, offsets in ADJ_RULES.items():
            print(used_offsets, offsets)
            if used_offsets == offsets:
                old_line = list(lines[y])
                old_line[x] = char
                lines[y] = "".join(old_line)
                break


vis = lines.copy()
vis = [list(x) for x in vis]
count = 0
xdim = len(lines[0])
ydim = len(lines)
for y in range(ydim):
    for x in range(xdim):
        if (x, y) in dists:
            continue
        char = lines[y][x]
        rx = x
        ry = y
        intersection_count = 0
        while rx < xdim:
            rx += 1
            if (rx, ry) in dists and lines[ry][rx] in "S|7F":
                intersection_count += 1
        if intersection_count % 2 == 1:
            vis[y][x] = "I"
            count += 1
        else:
            vis[y][x] = "O"

for line in vis:
    print("".join(line))
print(count)
