import re

games = []
with open('2','r') as f:
    for ligne in f.read().splitlines():
        games.append( ligne.split(': ')[1].split('; ') )


sumid = 0

for i in range(len(games)):
    id = i+1

    idok = True

    for subset in games[i]:
        b = re.search("\d+(?=\ blue)", subset)
        r = re.search("\d+(?=\ red)", subset)
        g = re.search("\d+(?=\ green)", subset)
        nb, nr, ng = 0, 0, 0
        if b:
            nb = int(b.group())
        if r:
            nr = int(r.group())
        if g:
            ng = int(g.group())

        if nr > 12 or ng > 13 or nb > 14:
            idok = False

    if idok:
        sumid += id

print('Part 1 : ', sumid)

## Part 2
sumpower = 0

for i in range(len(games)):
    maxr, maxg, maxb = 0, 0, 0

    for subset in games[i]:
        b = re.search("\d+(?=\ blue)", subset)
        r = re.search("\d+(?=\ red)", subset)
        g = re.search("\d+(?=\ green)", subset)
        nb, nr, ng = 0, 0, 0
        if b:
            nb = int(b.group())
        if r:
            nr = int(r.group())
        if g:
            ng = int(g.group())

        if nb > maxb:
            maxb = nb
        if nr > maxr:
            maxr = nr
        if ng > maxg:
            maxg = ng

    power = maxr*maxg*maxb
    sumpower += power

print('Part 2 : ', sumpower)

