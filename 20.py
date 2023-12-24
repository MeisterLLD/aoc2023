from collections import defaultdict
types = defaultdict(str)
voisins = defaultdict(list)

with open('20','r') as f:
    for ligne in f.read().splitlines():
        gauche, droite = ligne.split(' -> ')
        if gauche == 'broadcaster':
            voisins['broadcaster'] = droite.split(', ')
            types['broadcaster'] = 'broadcast'
        else:
            type = gauche[0]
            module = gauche[1:]
            voisins[module] = droite.split(', ')
            types[module] = type

def pred(module):
    L = [ ]
    for v in voisins:
        if module in voisins[v]:
            L.append(v)

    return L

flipflopstates = { module:'off' for module in types if types[module] == '%'   }

conjunctionstates = {  module: {input: 'low' for input in pred(module) }
                        for module in types if types[module] == '&' }


count = {'low': 0, 'high': 0}

def traiter(freq, origin, module, L):


    V = voisins[module]
    match types[module]:
        case 'broadcast':
            for v in V:
                L.append((freq, module, v))
                count[freq] += 1
                #print(module, ' -',freq,'-> ', v)

        case '%':
            if freq == 'low':
                newfreq = 'high' if flipflopstates[module] == 'off' else 'low'
                flipflopstates[module] = 'on' if flipflopstates[module]=='off' else 'off'
                for v in V:
                    L.append((newfreq, module, v))
                    count[newfreq] += 1
                    #print(module, ' -',newfreq,'-> ', v)


        case '&':
            conjunctionstates[module][origin] = freq
            if 'low' not in conjunctionstates[module].values():
                for v in V:
                    L.append(('low', module, v))
                    count['low'] += 1
                    #print(module, ' -','low','-> ', v)

            else:
                for v in V:
                    L.append(('high', module, v))
                    count['high'] += 1
                    #print(module, ' -','high','-> ', v)


for _ in range(1000):
    L = [  ('low', None, 'broadcaster') ]
    count['low'] += 1
    while len(L) > 0:
        freq, origin, module = L.pop(0)
        traiter(freq, origin, module, L)

print('Part 1 :', count['low']*count['high'])

## Part 2
needhigh = []

p = pred('rx')[0]
for pp in pred(p):
    flipflopstates = { module:'off' for module in types if types[module] == '%'   }

    conjunctionstates = {  module: {input: 'low' for input in pred(module) }
                        for module in types if types[module] == '&' }

    counter = 0
    fini = False
    while not fini:
        counter += 1
        L = [  ('low', None, 'broadcaster') ]
        while len(L) > 0:
            freq, origin, module = L.pop(0)
            traiter(freq, origin, module, L)
            if origin == pp and freq == 'high':
                needhigh.append(counter)
                fini = True
                break

from math import lcm
print('Part 2 :',lcm(*needhigh))
