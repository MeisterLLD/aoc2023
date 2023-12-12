from functools import cache

@cache
def nbconf( record, groups ):
    # Cas de base
    if len(groups) == 0: # plus de # à placer
        return 1 if '#' not in record else 0

    if sum(groups) > len(record): # plus assez de place pour les #
        return 0

    if record[0] == '.': # si on démarre par un .
        return nbconf( record[1:], groups)

    nb1, nb2 = 0, 0
    if record[0] == '?': # ... par un ?
        nb1 = nbconf( record[1:], groups) # possibilités en mettant un . à la place du ?

    # possibilités avec le premier groupe de # au début
    if '.' not in record[:groups[0]] and (len(record) <= groups[0] or len(record) > groups[0] and record[groups[0]] != '#'):
            nb2 = nbconf( record[groups[0]+1:], groups[1:]   )

    return nb1 + nb2


somme = 0
with open('12', 'r') as f:
    for line in f.read().splitlines():
        record, groups = line.split(' ')
        groups = [int(x) for x in groups.split(',')]
        somme += nbconf( tuple(record) , tuple(groups) )

print('Part 1 :', somme)

## Part 2
somme = 0
with open('12', 'r') as f:
    for line in f.read().splitlines():
        record, groups = line.split(' ')
        record = (5*(record + '?'))[:-1]
        groups = 5*[int(x) for x in groups.split(',')]
        somme += nbconf( tuple(record) , tuple(groups) )

print('Part 2 :', somme)
