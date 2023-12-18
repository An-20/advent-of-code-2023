from copy import deepcopy
from typing import List, Set, Tuple


def transpose(l):
    return list(map(list, zip(*l)))


with open("input.txt") as file:
    lines = file.read()
    lines = [l for l in lines.split("\n") if l]

xdim = len(lines[0])
ydim = len(lines)

# tuple of ((x, y), direction, past_coordinates)
beams: List[Tuple[Tuple[int, int], int, Set[Tuple[int, int, int]]]] = [((-1, 0), 0, set())]
energised: Set[Tuple[int, int, int]] = set()


while beams:
    new_beams = []
    new_beam_states: Set[Tuple[int, int, int]] = set()
    for beam in beams:
        (x, y), direction, past = beam
        offset = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}[direction]
        dx, dy = offset
        nx = x + dx
        ny = y + dy

        if not 0 <= nx < xdim or not 0 <= ny < ydim:
            continue
        if (nx, ny, direction) in past:
            continue
        if (nx, ny, direction) in energised:
            continue

        past.add((nx, ny, direction))
        new_beam_states.add((nx, ny, direction))
        energised.add((nx, ny, direction))
        char = lines[ny][nx]
        if char == ".":
            new_beams.append(((nx, ny), direction, past))
        elif char == "/":
            new_dir = {0: 1, 1: 0, 2: 3, 3: 2}[direction]
            new_beams.append(((nx, ny), new_dir, past))
        elif char == "\\":
            new_dir = {0: 3, 1: 2, 2: 1, 3: 0}[direction]
            new_beams.append(((nx, ny), new_dir, past))
        elif char == "|":
            if direction == 0 or direction == 2:
                new_beams.append(((nx, ny), 1, past))
                new_beams.append(((nx, ny), 3, deepcopy(past)))
            else:
                new_beams.append(((nx, ny), direction, past))
        elif char == "-":
            if direction == 1 or direction == 3:
                new_beams.append(((nx, ny), 0, past))
                new_beams.append(((nx, ny), 2, deepcopy(past)))
            else:
                new_beams.append(((nx, ny), direction, past))
        else:
            raise ValueError()

    beams = new_beams

print(len({(x[0], x[1]) for x in energised}))
