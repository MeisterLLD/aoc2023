curmap = [ ]
maps = [ ]
with open('13','r') as f:
    for s in f.read().splitlines():
        if s == '':
            maps.append(curmap)
            curmap = [ ]
        else: curmap.append(s)

maps.append(curmap)

for map in maps: # listify everything
    n = len(map)
    for i in range(n):
        map[i] = list(map[i])


verti = [0]*len(maps)
hori = [0]*len(maps)

for Nmap,map in enumerate(maps):
    n = len(map)
    m = len(map[0])

    for J in range(m-1):
        if J < m//2:
            if all( [map[i][J-k]  for i in range(n)] == [map[i][J+k+1] for i in range(n)] for k in range(J+1) ):
                verti[Nmap] = J+1
                break
        else:
            if all( [map[i][J-k]  for i in range(n)] == [map[i][J+k+1] for i in range(n)] for k in range(m-J-1) ):
                verti[Nmap] = J+1
                break


    for I in range(n-1):
        if I < n//2:
            if all( [map[I-k][j]  for j in range(m)] == [map[I+k+1][j] for j in range(m)] for k in range(I+1) ):
                hori[Nmap] = I+1
                break
        else:
            if all( [map[I-k][j]  for j in range(m)] == [map[I+k+1][j] for j in range(m)] for k in range(n-I-1) ):
                hori[Nmap] = I+1
                break


print('Part 1 : ',sum(hori)*100 + sum(verti))

## Part 2
from copy import deepcopy
verti2 = [0]*len(maps)
hori2 = [0]*len(maps)

for Nmap, map in enumerate(maps):
    n = len(map)
    m = len(map[0])

    found = False

    for i in range(n):
        for j in range(m):
            map2 = deepcopy(map)
            map2[i][j] = '.' if map[i][j]=='#' else '#'

            for J in range(m-1):
                if J < m//2:
                    if all( [map2[i][J-k]  for i in range(n)] == [map2[i][J+k+1] for i in range(n)] for k in range(J+1) ):
                        if J+1 != verti[Nmap]:
                            verti2[Nmap] = J+1
                            found = True
                            break
                else:
                    if all( [map2[i][J-k]  for i in range(n)] == [map2[i][J+k+1] for i in range(n)] for k in range(m-J-1) ):
                        if J+1 != verti[Nmap]:
                            verti2[Nmap] = J+1
                            found = True
                            break


            for I in range(n-1):
                if I < n//2:
                    if all( [map2[I-k][j]  for j in range(m)] == [map2[I+k+1][j] for j in range(m)] for k in range(I+1) ):
                        if I+1 != hori[Nmap]:
                            hori2[Nmap] = I+1
                            found = True
                            break
                else:
                    if all( [map2[I-k][j]  for j in range(m)] == [map2[I+k+1][j] for j in range(m)] for k in range(n-I-1) ):
                        if I+1 != hori[Nmap]:
                            hori2[Nmap] = I+1
                            found = True
                            break

            if found: break
        if found:break

print('Part 2 : ',sum(hori2)*100 + sum(verti2))
