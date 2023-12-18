pos = 0,0
dug = {(0,0)}

dirs = {'R':(1,0), 'L':(-1,0), 'D':(0,-1), 'U':(0,1)}

def tupladd(p,q):
    return (p[0]+q[0], p[1]+q[1])

with open('18','r') as f:
    for ligne in f.read().splitlines():
        dir, length = ligne.split( )[0], int(ligne.split( )[1])
        for _ in range(length):
            pos = tupladd(pos, dirs[dir])
            dug.add(pos)

mini_y = min( y for (_,y) in dug  )
maxi_y = max( y for (_,y) in dug  )

mini_x = min( x for (x,_) in dug  )
maxi_x = max( x for (x,_) in dug  )

rows = [ ]
for y in range(maxi_y,mini_y-1,-1):
    row = ''
    for x in range(mini_x,maxi_x+1):
        row = row + ('#' if (x,y) in dug else '.')
    rows.append(row)
print('\n'.join(rows))


import sys
sys.setrecursionlimit(1000000)

def findstart():
    for y in range(mini_y + 1, maxi_y + 1):
        for x in range(mini_x, maxi_x):
            if (x,y) in dug and (x+1,y) not in dug:
                return (x+1,y)

deb = findstart()
L = [deb]
colorie = set()


def floodfill(pos):
    if pos in colorie or pos in dug:
        return None

    colorie.add(pos)
    x, y = pos
    floodfill(  (x-1,y)  )
    floodfill(  (x+1,y)  )
    floodfill(  (x,y-1)  )
    floodfill(  (x-1,y+1)  )


floodfill(deb)

print('Part 1 :',len(colorie)+len(dug))

## Part 2
pos = 0,0
vertices = {(0,0)}
dirs = {'0':(1,0), '2':(-1,0), '1':(0,-1), '3':(0,1)}

def tupladd(p,q,n):
    return (p[0]+n*q[0], p[1]+n*q[1])


lengths = []
B = 1
with open('18','r') as f:
    for ligne in f.read().splitlines():
        instr = ligne.split('#')[1]
        length, dir = int('0x'+instr[0:5], base = 16), instr[5]
        pos = tupladd(pos, dirs[dir], length)
        vertices.add(pos)
        B += length
print('position finale', pos)


from functools import reduce
import operator
import math
center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), vertices), [len(vertices)] * 2))
vertices = sorted(vertices, key=lambda vertices: (-135 - math.degrees(math.atan2(*tuple(map(operator.sub, vertices, center))[::-1]))) % 360)


vertices.append(vertices[0])


A = 0
for i in range(len(vertices)-1):
    x, y= vertices[i]
    xx, yy = vertices[i+1]
    A += 1/2*(x*yy-xx*y)

print(abs(A)+B/2+1)