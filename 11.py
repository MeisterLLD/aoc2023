map = [ ] # recreating the map
with open('11', 'r') as f:
    for ligne in f.read().splitlines():
        map.append(ligne)

n, m = len(map), len(map[0])

emptyrows, emptycols = [], []

for i, ligne in enumerate(map):
    if ligne == '.'*m:
        emptyrows.append(i)

for j in range(m):
    if [map[i][j] for i in range(n)] == ['.']*n:
        emptycols.append(j)

stars = [ ]
for i in range(n):
    for j in range(m):
        if map[i][j] == '#': stars.append( (i,j) )


def dist( star1, star2 ):
    i, j = star1
    k, l = star2
    d = abs(i-k) + abs(j-l)

    for row in emptyrows:
        if min(i,k) < row < max(i,k): d += gap
    for col in emptycols:
        if min(j,l) < col < max(j,l): d += gap

    return d


gap = 1

sumdist = 0
for (i,j) in stars:
    for (k,l) in stars:
        if (i,j) < (k,l):
            d = dist( (i,j), (k,l)   )
            sumdist += d

print('Part 1 :', sumdist)

## Part 2
gap = 1000000 - 1

sumdist = 0
for (i,j) in stars:
    for (k,l) in stars:
        if (i,j) < (k,l):
            d = dist( (i,j), (k,l)   )
            sumdist += d

print('Part 2 :', sumdist)
