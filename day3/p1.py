with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]


def get_if_adj(x, y, lines) -> bool:
    offsets = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for offset in offsets:
        dx, dy = offset
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0:
            continue
        if ny >= len(lines) or nx >= len(lines[0]):
            continue
        if lines[ny][nx] not in "0123456789.":
            return True
    return False


total = 0
current_int = None
is_part_num = False

for y, line in enumerate(lines):
    current_int = None
    is_part_num = False
    for x, char in enumerate(line):
        if current_int is not None:
            # currently parsing an integer
            if char in "0123456789":
                current_int = current_int + char
                is_part_num = is_part_num or get_if_adj(x, y, lines)
            else:
                # end of integer
                if is_part_num:
                    total += int(current_int)
                current_int = None
                is_part_num = False
        else:
            if char in "0123456789":
                current_int = char
                is_part_num = get_if_adj(x, y, lines)
    if current_int is not None and is_part_num:
        total += int(current_int)
if current_int is not None and is_part_num:
    total += int(current_int)
print(total)
