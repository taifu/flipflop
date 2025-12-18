from collections import Counter

count = Counter()
special = 0
rgb_count = [0, 0, 0]

for bush in open("sales.txt").read().strip().splitlines():
    rgb = tuple(int(p) for p in bush.split(','))
    count[rgb] += 1
    if len(set(rgb)) < 3:
        special += 1
    else:
        rgb_count[rgb.index(max(rgb))] += 1

print(",".join(str(p) for p in count.most_common()[0][0]))
print(rgb_count[1])
print(special * 10 + rgb_count[0] * 5 + rgb_count[1] * 2 + rgb_count[2] * 4)
