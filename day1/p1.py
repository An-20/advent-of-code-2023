with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]

s = 0
for line in lines:
    od = [x for x in line if x in "0123456789"]
    s += int(od[0] + od[-1])
print(s)
