with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]

moves = lines[0]
edges = lines[1:]
nedges = {}
for edge in edges:
    a = edge[:3]
    b = edge[7:10]
    c = edge[12:15]
    nedges[a] = (b, c)

count = 0
current = "AAA"
while True:
    move = moves[count % len(moves)]
    if move == "L":
        current = nedges[current][0]
    else:
        current = nedges[current][1]
    count += 1
    if current == "ZZZ":
        break
print(count)
