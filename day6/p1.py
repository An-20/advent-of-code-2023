with open("input.txt") as file:
    lines = file.read().split("\n")

times = [int(x) for x in lines[0].split(":")[1].split(" ") if x]
distances = [int(x) for x in lines[1].split(":")[1].split(" ") if x]


rolling = 1
for time, record_dist in zip(times, distances):
    ways = 0
    for cand_time in range(time + 1):
        glide_time = time - cand_time
        total_dist = glide_time * cand_time
        if total_dist > record_dist:
            ways += 1
    rolling *= ways

print(rolling)
