# This works only if your S in a 7. Modify lines 13-18 and 49 accordingly.

map = [ ] # recreating the map
with open('10', 'r') as f:
    for ligne in f.read().splitlines():
        map.append(ligne)

n, m = len(map), len(map[0])

def voisins(pos): # neighbour function
    i,j = pos
    c = map[i][j]
    match c:
        case '|': voisinspot = [ (i+1,j), (i-1, j)   ]
        case '-': voisinspot = [ (i,j-1), (i, j+1)   ]
        case 'L': voisinspot = [ (i-1,j), (i, j+1)   ]
        case 'J': voisinspot = [ (i-1,j), (i, j-1)   ]
        case '7' | 'S': voisinspot = [ (i+1,j), (i, j-1)   ] # place your S in the appropriate line here
        case 'F': voisinspot = [ (i+1,j), (i, j+1)   ]
    return [(i,j) for (i,j) in voisinspot if i >=0 and j >= 0 and i < n and j < m]

for i in range(n): # find starting position
    for j in range(m):
        if map[i][j] == 'S':
            debut = (i,j)
            break

# BFS
file = [debut]
dist = {debut : 0}
while len(file) > 0:
    new = file.pop(0)
    for s in voisins(new):
        if s not in dist:
            file.append(s)
            dist[s] = dist[new] + 1

print('Part 1 :', max([d for v,d in dist.items()]))

## Part 2
''' For each point not in the loop, count intersections to the left of it with the loop, except if they're - or J or L
Crossing the loop makes you alternate between in/out the regions enclosed by the loop.
Omitting J and L is a visual trick, just think of it as offsetting everything a tiny bit : don't start from the center of
your starting pixel but just a little bit below : then passing └ or ─ or ┘ is ok since you don't hit them !
In that sense, what you are counting is the number of pixels whose point just a bit below their center, are enclosed in the loop.
But since they're pixels, that is equivalent to them being fully in it !
It also works with excluding -, 7, F instead of -, L, J, and imagining the tiny offset in the other direction '''

inside = 0
for i in range(n):
    for j in range(m):
        if (i,j) not in dist:
            counter = len(  [(i,l) for l in range(j) if (i,l) in dist and map[i][l] not in {'-', 'J', 'L'} ]   ) # if your S is a -, J or L put it here too
            inside += counter % 2


print('Part 2 :',inside)

