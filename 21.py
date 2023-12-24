carte = []
with open('21','r') as f:
    for ligne in f.read().splitlines():
        carte.append(ligne)

n = len(carte)
m = len(carte[0])

for i in range(n):
    for j in range(m):
        if carte[i][j] == 'S':
            debut = i,j
            break


def voisins(pos):
    i, j = pos
    voisinspot = [ (i,j-1), (i,j+1), (i-1,j), (i+1,j)   ]
    return [(i,j) for (i,j) in voisinspot if i >=0 and j >= 0 and i < n and j < m and carte[i][j] != '#']

from collections import deque

def part1(maxsteps):
    L = deque([debut])
    dist = {debut : 0}
    maxdist = 0
    while len(L) > 0 and maxdist <= maxsteps:
        s = L.popleft()
        for v in voisins(s):
            if v not in dist:
                L.append(v)
                dist[v] = dist[s] + 1
                if dist[s] + 1 > maxdist:
                    maxdist = dist[s] + 1

    return len([x for x in dist if dist[x] <= maxsteps and dist[x] % 2 == maxsteps %2 ])

print('Part 1 :',part1(64))

## Part 2
def voisins(pos):
    i, j = pos
    voisinspot = [ (i,j-1), (i,j+1), (i-1,j), (i+1,j)   ]
    return [(i,j) for (i,j) in voisinspot if carte[i%n][j%m] != '#']

def f(n):
    return part1(65+n*131)

f0, f1, f2 = part1(65), part1(65+131), part1(65+2*131)
a0 = f0
a1 = (4*f1 - f2 - 3*a0)//2
a2 = f1 - (a0+a1)

n = 26501365//131
print('Part 2 :',a0 + a1*n + a2*n**2 )
