data = open("birds.txt").read().strip().splitlines()

def reset(data):
    birds = {}
    for n, line in enumerate(data):
        speed = complex(*(int(p) for p in line.split(",")))
        birds[n] = (speed, 0j)
    return birds

birds = reset(data)

size = 1000
frame = 250

for bird, (speed, xy) in birds.items():
    next_xy = xy + speed * 100
    birds[bird] = (speed, complex(next_xy.real % size, next_xy.imag % size))
print(sum(1 for _, xy in birds.values() if frame <= xy.real < size - frame and frame <= xy.imag < size - frame ))

birds = reset(data)
tot = 0
for hour in range(1000):
    for bird, (speed, xy) in birds.items():
        next_xy = xy + 3600 * speed
        birds[bird] = [speed, complex(next_xy.real % size, next_xy.imag % size)]
    tot += sum(1 for _, xy in birds.values() if frame <= xy.real < size - frame and frame <= xy.imag < size - frame )
print(tot)

birds = reset(data)
tot = 0
for hour in range(1000):
    for bird, (speed, xy) in birds.items():
        next_xy = xy + 31556926 * speed
        birds[bird] = [speed, complex(next_xy.real % size, next_xy.imag % size)]
    tot += sum(1 for _, xy in birds.values() if frame <= xy.real < size - frame and frame <= xy.imag < size - frame )
print(tot)
