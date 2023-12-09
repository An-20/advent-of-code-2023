import typing

with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]
    lines = [[int(x) for x in l.split(" ") if x] for l in lines]

def extrapolate(l: typing.List[int]) -> typing.List[int]:
    diff = []
    last = l[0]
    for val in l[1:]:
        diff.append(val - last)
        last = val

    if not all(x == 0 for x in diff):
        return l + [last + extrapolate(diff)[-1]]
    return l + [last]


print(sum([extrapolate(x)[-1] for x in lines]))
