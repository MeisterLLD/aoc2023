## Part 1
pos = 0,0
vertices = [ (0,0) ]
dirs = {'R':(1,0), 'L':(-1,0), 'D':(0,-1), 'U':(0,1)}

def tupladd(p,q,n):
    return (p[0]+n*q[0], p[1]+n*q[1])

B = 0
with open('18','r') as f:
    for ligne in f.read().splitlines():
        dir, length = ligne.split( )[0], int(ligne.split( )[1])
        pos = tupladd(pos, dirs[dir], length)
        vertices.append(pos)
        B += length

A = 0 # Shoelace
for i in range(len(vertices)-1):
    x, y= vertices[i]
    xx, yy = vertices[i+1]
    A -= 1/2*(y+yy)*(x-xx)

print('Part 1 :', int(A+B/2+1)) # Interior (Pick) + Boundary points

## Part 2
pos = 0,0
vertices = [ (0,0) ]
dirs = {'0':(1,0), '2':(-1,0), '1':(0,-1), '3':(0,1)}

def tupladd(p,q,n):
    return (p[0]+n*q[0], p[1]+n*q[1])

B = 0
with open('18','r') as f:
    for ligne in f.read().splitlines():
        instr = ligne.split('#')[1]
        length, dir = int('0x'+instr[0:5], base = 16), instr[5]
        pos = tupladd(pos, dirs[dir], length)
        vertices.append(pos)
        B += length

A = 0
for i in range(len(vertices)-1):
    x, y= vertices[i]
    xx, yy = vertices[i+1]
    A -= 1/2*(y+yy)*(x-xx)

print('Part 2 :', int(A+B/2+1))