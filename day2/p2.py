with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]

total = 0

for line in lines:
    minimums = {"red": 0, "green": 0, "blue": 0}
    game_id = int(line.split(":")[0].split(" ")[1])
    subsets = line.split(":")[1].split(";")
    subsets = [x.strip() for x in subsets]
    for subset in subsets:
        pairs = subset.split(",")
        pairs = [x.strip() for x in pairs]
        for pair in pairs:
            num, colour = pair.split(" ")
            num = int(num)
            comp = minimums[colour]
            if num > comp:
                minimums[colour] = num
    power = minimums["red"] * minimums["green"] * minimums["blue"]
    total += power

print(total)
