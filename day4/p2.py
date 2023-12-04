with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]

cards = {}
for idx in range(len(lines)):
    cards[idx] = 1

for idx, line in enumerate(lines):
    num = cards[idx]
    winning = line.split("|")[0].split(":")[1].strip()
    winning = [int(x) for x in winning.split(" ") if x]
    chosen = line.split("|")[1].strip()
    chosen = [int(x) for x in chosen.split(" ") if x]
    count = len([x for x in chosen if x in winning])
    for copy_idx in range(idx + 1, idx + count + 1):
        cards[copy_idx] += num

print(sum(cards.values()))
