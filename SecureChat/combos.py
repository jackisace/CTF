import itertools


a = "apaloma"
b = "APALOMA"
c = "4p4l0m4"


combos = []

for combo in map(''.join, itertools.product(*zip(a, b))):
    combos.append(combo)
for combo in map(''.join, itertools.product(*zip(b, c))):
    combos.append(combo)
for combo in map(''.join, itertools.product(*zip(c, a))):
    combos.append(combo)

setCombos = set(combos)

for combo in setCombos:
    print(combo)

