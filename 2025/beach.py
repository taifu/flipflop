xy = 0j
steps = steps2 = steps3 = 0
trashes = []
for trash in open("beach.txt").read().strip().splitlines():
    next_xy = complex(*(int(p) for p in trash.split(",")))
    trashes.append(next_xy)
    steps += abs(xy.real - next_xy.real) + abs(xy.imag - next_xy.imag)
    steps2 += max(abs(xy.real - next_xy.real), abs(xy.imag - next_xy.imag))
    xy = next_xy

xy = 0j
steps3 = 0
for next_xy in sorted(trashes, key=lambda x: x.real + x.imag):
    steps3 += max(abs(xy.real - next_xy.real), abs(xy.imag - next_xy.imag))
    xy = next_xy

print(int(steps))
print(int(steps2))
print(int(steps3))
