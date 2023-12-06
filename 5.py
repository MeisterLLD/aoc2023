with open('5','r') as f:
    lignes = f.read().split('\n')

seeds = [int(x) for x in lignes[0].split(': ')[1].split(' ')]
transformations = [ (3,23), (25,53), (55,87), (89,121), (123,166), (168,202), (204,219)    ]

def seedtoloc(seed):
    old = seed
    for m,n in transformations:  # On fait chacune des 7 transformations
        for ligne in lignes[m:n]:
            debnew, debold, length = [int(x) for x in ligne.split(' ')]
            if debold <= old <= debold + length - 1:
                new = debnew + (old-debold)
                break
            new = old
        old = new
    return new

print('Part 1 : ', min([seedtoloc(seed) for seed in seeds]))

## Part 2
# Idea from Epithumia :
# find all intervals on which seed-to-loc is a translation. For that, use dichotomy
# starting from a given seed range (a,b) until seedtoloc(a)-a = seedtoloc(b)-b
# This works if (since ?) seedtoloc is one-to-one, so there cannot be two
# distinct portions of the same line in its graph, separated by another part
# (this would imply that some location has two or more corresponding seeds)


queue = [ (seeds[2*i], seeds[2*i] + seeds[2*i+1] - 1) for i in range(len(seeds) // 2)   ]
goodranges = [ ]

while queue != []:
    a,b = queue.pop()
    old_b = b
    while seedtoloc(a) - a != seedtoloc(b) - b:
        b = (a+b)//2
    goodranges.append( (a,b) )
    if old_b > b:
        queue.append( (b+1, old_b) )

print('Part 2 : ', min([seedtoloc(a) for a,_ in goodranges])  )