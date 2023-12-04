with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]

total = 0
for line in lines:
    winning = line.split("|")[0].split(":")[1].strip()
    winning = [int(x) for x in winning.split(" ") if x]
    chosen = line.split("|")[1].strip()
    chosen = [int(x) for x in chosen.split(" ") if x]
    count = len([x for x in chosen if x in winning])
    if count >= 1:
        total += 2 ** (count - 1)

print(total)
