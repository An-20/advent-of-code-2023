from typing import List, Iterable

NUM_CYCLES = 1000000000

with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]


def transpose(l: List[Iterable]) -> List[List]:
    return list(map(list, zip(*l)))


def single_step(col: List) -> List:
    new_col = []
    for char in col:
        if char in "#.":
            new_col.append(char)
        else:
            if new_col and new_col[-1] == ".":
                new_col[-1] = "O"
                new_col.append(".")
            else:
                new_col.append("O")
    return new_col


def multi_step(cols: List[List]) -> List[List]:
    new_cols = []
    for col in cols:
        while True:
            new_col = single_step(col)
            if new_col == col:
                break
            col = new_col
        new_cols.append(new_col)
    return new_cols


def get_load(col) -> int:
    col_len = len(col)
    load = 0
    for idx, char in enumerate(col):
        if char == "O":
            load += col_len - idx
    return load


def rotate(state: List[List]) -> List[List]:
    return transpose([reversed(x) for x in state])


state = transpose(lines)  # start facing north
states = {}
idx = 0
while True:
    if idx % 4 == 0:
        tupled = tuple([tuple(x) for x in state])
        if tupled in states:
            break
        states[tupled] = idx

    next_state = multi_step(state)
    next_state = rotate(next_state)
    state = next_state
    idx += 1

entry_len = states[tupled] // 4
repeat_len = (idx - states[tupled]) // 4
rem = (NUM_CYCLES - entry_len) % repeat_len
for key, value in states.items():
    if value == (entry_len + rem) * 4:
        print(sum([get_load(x) for x in key]))
        break
