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
        return [l[0] - extrapolate(diff)[0]] + l
    return [last] + l


print(sum([extrapolate(x)[0] for x in lines]))
