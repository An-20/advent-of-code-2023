with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]

total = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != "*":
            continue

        part_numbers = []
        # store part numbers as a tuple of ((start_x, start_y), value)
        # so then we can distinguish between identical part numbers
        # yes this is really dodgy

        offsets = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        for offset in offsets:
            dx, dy = offset
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0:
                continue
            if ny >= len(lines) or nx >= len(lines[0]):
                continue
            if lines[ny][nx] in "0123456789":
                # parse the part number
                # find the leftmost digit
                left = nx
                while True:
                    nleft = left - 1
                    if nleft >= 0 and lines[ny][nleft] in "0123456789":
                        left = nleft
                    else:
                        break
                # find the rightmost digit
                right = nx
                while True:
                    nright = right + 1
                    if nright < len(line) and lines[ny][nright] in "0123456789":
                        right = nright
                    else:
                        break
                part_numbers.append(((left, ny), int(lines[ny][left:right + 1])))
        # forgive me
        part_numbers = list(set(part_numbers))
        if len(part_numbers) == 2:
            print(part_numbers)
            total += part_numbers[0][1] * part_numbers[1][1]

print(total)
