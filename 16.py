with open('16','r') as f:
    carte =[row for row in f.read().splitlines()]

n, m = len(carte), len(carte[0])


incr = {'R':(0,1), 'L': (0,-1), 'U':(-1,0), 'D':(1,0)}

energized = set()
dejavu = set()

def push(start, dir):
    i, j = start

    if not (0 <= i < n and 0 <= j < m): # Cas de base : arrivé dans un mur
        return None

    if (start, dir) in dejavu: # Case de base : on boucle
        return None

    energized.add((i,j))
    dejavu.add( ((i,j), dir)  )

    # Appels récursifs
    if carte[i][j] == '.':
        push(  tuple(sum(x) for x in zip(start, incr[dir])), dir)


    if carte[i][j] == '/':
        match dir:
            case 'R': push(tuple(sum(x) for x in zip(start, incr['U'])), 'U')
            case 'L': push(tuple(sum(x) for x in zip(start, incr['D'])), 'D')
            case 'U': push(tuple(sum(x) for x in zip(start, incr['R'])), 'R')
            case 'D': push(tuple(sum(x) for x in zip(start, incr['L'])), 'L')

    if carte[i][j] == '\\':
        match dir:
            case 'R': push(tuple(sum(x) for x in zip(start, incr['D'])), 'D')
            case 'L': push(tuple(sum(x) for x in zip(start, incr['U'])), 'U')
            case 'U': push(tuple(sum(x) for x in zip(start, incr['L'])), 'L')
            case 'D': push(tuple(sum(x) for x in zip(start, incr['R'])), 'R')

    if carte[i][j] == '|':
        match dir:
            case 'R' | 'L':
                push(tuple(sum(x) for x in zip(start, incr['U'])), 'U')
                push(tuple(sum(x) for x in zip(start, incr['D'])), 'D')
            case 'U' | 'D':
                push(tuple(sum(x) for x in zip(start, incr[dir])), dir)

    if carte[i][j] == '-':
        match dir:
            case 'R' | 'L':
                push(tuple(sum(x) for x in zip(start, incr[dir])), dir)
            case 'U' | 'D':
                push(tuple(sum(x) for x in zip(start, incr['L'])), 'L')
                push(tuple(sum(x) for x in zip(start, incr['R'])), 'R')


## Part 1
import sys
sys.setrecursionlimit(10000)

push( (0,0), 'R')
print('Part 1 :',len(energized))

## Part 2
starts = [ ((0,0),'R'), ((0,0),'D'),  ((0,m),'L'), ((0,m),'D'), ((n-1,0),'U'), ((n-1,0), 'R'), ((n-1,m-1),'U'), ((n-1,m-1),'L') ]
for j in range(1,m-2):
    starts.append( ((0  ,j), 'D')  )
    starts.append( ((n-1,j), 'U')  )

for i in range(1,n-2):
    starts.append( ((i,0), 'R' )  )
    starts.append( ((i,m-1), 'L')   )

maxen = 0
for pos, dir in starts:
    energized = set()
    dejavu = set()
    push(pos, dir)
    if len(energized) > maxen:
        maxen = len(energized)

print('Part 2 :', maxen)