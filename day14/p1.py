from typing import List, Iterable

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


def get_load(col: List) -> int:
    col_len = len(col)
    load = 0
    for idx, char in enumerate(col):
        if char == "O":
            load += col_len - idx
    return load


t = transpose(lines)
total = 0
for col in t:
    while True:
        stepped_col = single_step(col)
        if stepped_col == col:
            break
        col = stepped_col
    total += get_load(col)
print(total)
