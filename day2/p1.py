with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]

r = 12
g = 13
b = 14

total = 0

for line in lines:
    possible = True
    game_id = int(line.split(":")[0].split(" ")[1])
    subsets = line.split(":")[1].split(";")
    subsets = [x.strip() for x in subsets]
    for subset in subsets:
        pairs = subset.split(",")
        pairs = [x.strip() for x in pairs]
        for pair in pairs:
            num, colour = pair.split(" ")
            num = int(num)
            comp = {"red": r, "green": g, "blue": b}[colour]
            if num > comp:
                possible = False
                break
        if not possible:
            break
    if possible:
        total += game_id

print(total)
