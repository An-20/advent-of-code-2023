"""
quick maths:
let t be total time
let r be record distance
let c be candidate time such that 0 <= c < t
let g be glide time so g = t - c

cg > r
c(t - c) > r
ct - c^2 > r
-c^2 + tc - r > 0

A = -1
B = t
C = -r
"""
import math

with open("input.txt") as file:
    lines = file.read().split("\n")

time = int(lines[0].split(":")[1].replace(" ", ""))
distance = int(lines[1].split(":")[1].replace(" ", ""))


def solve_quadratic(a, b, c) -> list[float]:
    disc = b**2 - 4 * a * c
    if disc < 0:
        return []
    sol1 = (-b + math.sqrt(disc)) / (2*a)
    sol2 = (-b - math.sqrt(disc)) / (2 * a)
    return [sol1, sol2]


sol1, sol2 = sorted(solve_quadratic(-1, time, -distance))
sol1 = math.ceil(sol1)
sol2 = math.floor(sol2)
number_solutions = sol2 - sol1 + 1
print(number_solutions)
