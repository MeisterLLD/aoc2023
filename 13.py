with open('13','r') as f:
    maps = [map.splitlines() for map in f.read().split('\n\n')]

transmaps = [ list(zip(*map)) for map in maps] # bonne astuce pour transposer


def score(nbdiff):

    sum1, sum2 = 0, 0

    for map, transmap in zip(maps, transmaps):
        found = False
        for mirror in range(1, len(map)):
            up, down = reversed(map[:mirror]), map[mirror:]
            if sum( x != y for ligne1,ligne2 in zip(up, down) for x,y in zip(ligne1,ligne2) ) == nbdiff: # on compte les différences
                sum1 += 100*mirror
                found = True
                break

        if not found:
            for mirror in range(1, len(transmap)):
                up, down = reversed(transmap[:mirror]), transmap[mirror:]
                if sum( x != y for ligne1,ligne2 in zip(up, down) for x,y in zip(ligne1,ligne2) ) == nbdiff:
                    sum2 += mirror
                    break

    return sum1 + sum2


print(f'Part 1 : {score(0)}')
print(f'Part 2 : {score(1)}')