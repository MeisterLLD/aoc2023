cyphers = ['0','1','2','3','4','5','6','7','8','9']

mat = [ ]
with open('3','r') as f:
    for ligne in f.read().splitlines():
        mat.append(ligne)

n, m = len(mat), len(mat[0])

def detectword2(i,j):
    jdeb, jfin = j, j
    while jdeb >= 0 and mat[i][jdeb] in cyphers:
        jdeb -= 1
    while jfin < m and mat[i][jfin] in cyphers:
        jfin += 1
    return jdeb+1, jfin


words = set()
for i in range(n):
    for j in range(m):
        if mat[i][j] in cyphers:
            jdeb, jfin = detectword2(i, j)
            words.add( ((i,jdeb), (i, jfin)) )

def voisins( i,j  ):
    voisinspotentiels = [ (i,j-1), (i,j+1), (i-1,j-1), (i-1,j), (i-1,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)   ]
    return[ v for v in voisinspotentiels if v[0] >= 0 and v[0] < n and v[1] >= 0 and v[1] < m]

def acceptableword(  i, jdeb, jfin   ):
    for j in range(jdeb,jfin):
        for iv,jv in voisins(i,j):
            if mat[iv][jv] not in cyphers and mat[iv][jv] != '.':
                return True
    return False

sum = 0
for (i, jdeb), (i, jfin) in words:
    if acceptableword(i, jdeb, jfin):
        number = int(mat[i][jdeb:jfin]   )
        sum += number

print('Part 1 : ', sum)

## Part 2
sum = 0

for i in range(n):
    for j in range(m):
        if mat[i][j] == '*':
            entiersvoisins = set()

            for iv,jv in voisins(i,j):
                if mat[iv][jv] in cyphers:
                    jdeb, jfin = detectword2(iv,jv)
                    entiersvoisins.add(  ((iv,jdeb), (iv,jfin))  )

            if len(entiersvoisins) == 2:
                power = 1
                for ((id,jdeb), (id,jfin)) in entiersvoisins:
                    entier = int(mat[id][jdeb:jfin])
                    power = power*entier

                sum += power


print('Part 2 : ',sum)

