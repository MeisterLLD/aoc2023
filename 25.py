from collections import defaultdict
from copy import deepcopy
from collections import deque
from random import choice

G = defaultdict(list)
with open('25','r') as f:
    for ligne in f.read().splitlines():
        module, voisins = ligne.split(': ')
        voisins = voisins.split(' ')
        for v in voisins:
            G[module].append(v)
            G[v].append(module)

def removeedge(G,s1,s2):
    G[s1].remove(s2)
    G[s2].remove(s1)

def ncc(G):
    nn = []
    vus = set()

    while len(vus) < len(G):
        n = 1
        deb = [p for p in list(G.keys()) if p not in vus][0]
        vus.add(deb)
        pile = [deb]
        while len(pile) > 0:
            x = pile.pop()
            for v in G[x]:
                if v not in vus:
                    vus.add(v)
                    n += 1
                    pile.append(v)

        nn.append(n)
    return nn

def shortestpath(G, s1, s2):
    file = deque([s1])
    vus = {s1}
    pred = {s1 : None}
    while s2 not in pred:
        x = file.popleft()
        for v in G[x]:
            if v not in vus:
                vus.add(v)
                file.append(v)
                pred[v] = x

    cur = s2
    chemin = [ ]
    while cur != s1:
        chemin.append(cur)
        cur = pred[cur]

    return chemin+[s1]

freq = defaultdict(int)
for _ in range(1000):
    s1, s2 = choice(list(G.keys())), choice(list(G.keys()))
    path = shortestpath(G, s1, s2)
    for i in range(len(path)-1):
        ar = (path[i], path[i+1])
        ar = tuple(sorted(ar))
        freq[ar] += 1

torem = []
for _ in range(3):
    ar = max(freq, key = lambda v: freq[v] )
    freq[ar] = 0
    torem.append(ar)

for s1, s2 in torem:
    removeedge(G,s1,s2)

print('Part 1 :', ncc(G)[0]*ncc(G)[1] )