from itertools import cycle

dico = { }
with open('8', 'r') as f:
    instructions = list(f.readline().strip('\n'))
    f.readline()
    for ligne in f.read().splitlines():
        deb, new = ligne.split(' = ')
        new = new.strip('()')
        dico[deb] = tuple(new.split(', '))

steps  = 0
pos = 'AAA'
for direction in cycle(instructions):
    steps += 1
    pos = dico[pos][0] if direction == 'L' else dico[pos][1]
    if pos == 'ZZZ': break


print('Part 1', steps)

## Part 2
# This LCM solution is actually a leap of faith : nothing in the
# instructions guarantees that it works, e.g. if one of your ..Z node
# leads directly to another ..Z node, it would be problematic.

liststeps = [ ]
positions = [key for key in dico.keys() if key[2] == 'A']

for pos in positions:
    steps = 0
    for direction in cycle(instructions):
        steps += 1
        pos = dico[pos][0] if direction == 'L' else dico[pos][1]
        if pos[2] == 'Z': break
    liststeps.append(steps)

from math import lcm
print('Part 2', lcm(*liststeps))



