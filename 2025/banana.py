tot = [0] * 3
for line in open("banana.txt").read().splitlines():
    tot[0] += (count := len(line) // 2)
    if (len(line) // 2) % 2 == 0:
        tot[1] += count
    if 'e' not in line:
        tot[2] += count
for tot in tot:
    print(tot)
