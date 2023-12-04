with open("input.txt") as file:
    lines = file.read().split("\n")
    lines = [l for l in lines if l]

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# this one was like way harder?
# easier solutions definitely exist
# this one just scans progressively until it finds a number
# making it very inefficient
s = 0
for line in lines:
    lb = 1
    lfound = False
    while not lfound:
        cand = line[:lb]
        numerical = [x for x in cand if x in "123456789"]
        if numerical:
            left = int(numerical[0])
            lfound = True
        for idx, num in enumerate(nums):
            if num in cand:
                left = idx + 1
                lfound = True
        lb += 1

    ub = 1
    rfound = False
    while not rfound:
        cand = line[-ub:]
        numerical = [x for x in cand if x in "123456789"]
        if numerical:
            right = int(numerical[-1])
            rfound = True
        for idx, num in enumerate(nums):
            if num in cand:
                right = idx + 1
                rfound = True
        ub += 1

    s += 10 * left + right
print(s)
