ground = highest = 0
ground2 = highest2 = inc2 = 0
ground3 = highest3 = inc3 = 0
fib = [0, 1]
last = None
for char in list(open("roller.txt").read().strip()):
#for char in list("^^^^^"):
    ground += (inc := {'^': 1, 'v': -1}[char])
    highest = max(highest, ground)
    if last == char:
        inc2 = inc2 + 1 if inc2 > 0 else inc2 - 1
        inc3 = inc * fib[0]
        fib = [fib[1], fib[1] + fib[0]]
    else:
        inc2 = inc
        last = char
        fib = [0, 1]
        inc3 = inc
    ground2 += inc2
    highest2 = max(highest2, ground2)
    ground3 += inc3
    highest3 = max(highest3, ground3)
print(highest)
print(highest2)
print(highest3)
