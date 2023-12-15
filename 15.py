def hash(s):
    value = 0
    for c in s:
        value += ord(c)
        value *= 17
        value = value%256
    return value

with open('15','r') as f:
    s = f.read().strip('\n')
    steps = s.split(',')

sumval = 0

for step in steps:
    sumval += hash(step)

print('Part 1 :',sumval)

## Part 2
from collections import defaultdict

boxes = defaultdict(list)

for step in steps:
    if '-' in step:
        label = step.split('-')[0]
        box = hash(label)
        for lab, focal in boxes[box]:
            focal = int(focal)
            if lab == label:
                boxes[box].remove([lab,focal])

    if '=' in step:
        label, focal = step.split('=')
        box = hash(label)
        for i, (lab, foc) in enumerate(boxes[box]):
            if lab == label:
                boxes[box][i] = [label,int(focal)]
                break
        else:
            boxes[box].append( [label,int(focal)] )

focusingpower = 0
for nbox in range(256):
    for nlens, (lab,focal) in enumerate(boxes[nbox]):
        focusingpower += (nbox+1)*(nlens+1)*focal

print('Part 2 :',focusingpower)
