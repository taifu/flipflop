tunnels = list(open("tunnel.txt").read().strip())

stations = {}
order = []
for p, stat in enumerate(tunnels):
    try:
        first_p = stations[stat]
        stations[stat] = [stat, first_p, p, abs(first_p - p)]
    except KeyError:
        stations[stat] = p
        order.append(stat)

visited = set()
steps = steps2 = 0
curr_p = 0

while True:
    try:
        station = stations[tunnels[curr_p]]
    except IndexError:
        break
    steps += station[3]
    steps2 += station[3] if station[0].islower() else -station[3]
    visited.add(station[0])
    curr_p = set(station[1:3]).difference(set((curr_p,))).pop() + 1

print(steps)
print("".join(t for t in order if t not in visited))
print(steps2)
