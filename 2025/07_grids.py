import math

grids = {}
for n, line in enumerate(open("grids.txt").read().strip().splitlines()):
    grids[n] = tuple(int(p) for p in line.split())

tot = 0
for x, y in grids.values():
    tot += math.comb(x + y - 2, y - 1)
print(tot)

tot = 0
for x, y in grids.values():
    tot += math.factorial(2 * x + y - 3) // (math.factorial(x  - 1)**2 * math.factorial(y  - 1))
print(tot)

tot = 0
for n_dim, size in grids.values():
    total_steps = (size - 1)*n_dim
    numerator = math.factorial(total_steps)
    denominator = math.factorial(size - 1)**n_dim
    tot += numerator // denominator
print(tot)
