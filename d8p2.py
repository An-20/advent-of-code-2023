import math

with open("2023d8i.txt") as file:
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


starting = []
for node in nedges:
    if node[2] == "A":
        starting.append(node)


cycles = []
for node in starting:
    count = 0
    while True:
        move = moves[count % len(moves)]
        if move == "L":
            node = nedges[node][0]
        else:
            node = nedges[node][1]
        count += 1
        if node[2] == "Z":
            break
    cycles.append(count)

# how does this work?
# well it just happens that every cycle never meets a different end point before the "true" end point
print(math.lcm(*cycles))
