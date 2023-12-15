with open("input.txt") as file:
    steps = file.read().replace("\n", "").split(",")
    steps = [s for s in steps if s]


def apply_hash(s: str) -> int:
    value = 0
    for char in s:
        value += ord(char)
        value *= 17
        value = value % 256
    return value


state = [[] for _ in range(256)]
for step in steps:
    label = step[:-1] if "-" in step else step.split("=")[0]
    box_idx = apply_hash(label)

    if "-" in step:
        state[box_idx] = [x for x in state[box_idx] if x[0] != label]
    else:
        focal_length = int(step.split("=")[1])
        if label in [x[0] for x in state[box_idx]]:
            state[box_idx] = [x if x[0] != label else (label, focal_length) for x in state[box_idx]]
        else:
            state[box_idx].append((label, focal_length))

total = 0
for box_idx, box in enumerate(state):
    for slot_idx, lens in enumerate(box):
        total += (box_idx + 1) * (slot_idx + 1) * lens[1]
print(total)
