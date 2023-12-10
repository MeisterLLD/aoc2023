# This works only if your S in a 7. Modify lines 13-18 and 49 accordingly.

map = [ ]

with open('10', 'r') as f:
    for ligne in f.read().splitlines():
        map.append(ligne)

n, m = len(map), len(map[0])

def voisins(pos):
    i,j = pos
    if map[i][j] == '|': voisinspot = [ (i+1,j), (i-1, j)   ]
    if map[i][j] == '-': voisinspot = [ (i,j-1), (i, j+1)   ]
    if map[i][j] == 'L': voisinspot = [ (i-1,j), (i, j+1)   ]
    if map[i][j] == 'J': voisinspot = [ (i-1,j), (i, j-1)   ]
    if map[i][j] in ('7', 'S'): voisinspot = [ (i+1,j), (i, j-1)   ] # place your S in the appropriate line here
    if map[i][j] == 'F': voisinspot = [ (i+1,j), (i, j+1)   ]

    return [(i,j) for (i,j) in voisinspot if i >=0 and j >= 0 and i < n and j < m]


for i in range(n):
    for j in range(m):
        if map[i][j] == 'S':
            debut = (i,j)
            break


file = [debut]
dist = {debut : 0}

while len(file) > 0:
    new = file.pop(0)  # on défile (à gauche, donc)
    for s in voisins(new):  # pour tous les voisins de n (le défilé)
        if s not in dist:
            file.append(s)  #on l'enfile
            dist[s] = dist[new] + 1

print('Part 1 :', max([d for v,d in dist.items()]))


## Part 2
inside = 0

for i in range(n):
    for j in range(m):
        if (i,j) not in dist:
            counter = len(  [(i,l) for l in range(j) if (i,l) in dist and map[i][l] not in {'-','J','L'} ]   ) # if your S is a -, J or L put it here too
            inside += counter % 2


print('Part 2 :',inside)