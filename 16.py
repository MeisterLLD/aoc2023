with open('16','r') as f:
    carte =[row for row in f.read().splitlines()]

n, m = len(carte), len(carte[0])

incr = {'R': 1, 'L': -1, 'U':-1j, 'D':1j}

# energized = set()
dejavu = set()

def push(start, dir):

    i, j = int(start.imag), int(start.real)
    if not (0 <= i < n and 0 <= j < m): # Cas de base : arrivé dans un mur
        return None

    if (start, dir) in dejavu: # Case de base : on boucle
        return None

    # energized.add(start)
    dejavu.add( (start, dir)  )

    # Appels récursifs
    if carte[i][j] == '.':
        push(  start + incr[dir], dir)


    if carte[i][j] == '/':
        match dir:
            case 'R': push( start + incr['U'], 'U')
            case 'L': push( start + incr['D'], 'D')
            case 'U': push( start + incr['R'], 'R')
            case 'D': push( start + incr['L'], 'L')

    if carte[i][j] == '\\':
        match dir:
            case 'R': push( start + incr['D'], 'D')
            case 'L': push( start + incr['U'], 'U')
            case 'U': push( start + incr['L'], 'L')
            case 'D': push( start + incr['R'], 'R')

    if carte[i][j] == '|':
        match dir:
            case 'R' | 'L':
                push( start + incr['U'], 'U')
                push( start + incr['D'], 'D')
            case 'U' | 'D':
                push( start + incr[dir], dir)

    if carte[i][j] == '-':
        match dir:
            case 'R' | 'L':
                push( start + incr[dir], dir)
            case 'U' | 'D':
                push( start + incr['L'], 'L')
                push( start + incr['R'], 'R')


# Part 1
import sys
sys.setrecursionlimit(10000)

push( 0+0j, 'R')
print('Part 1 :', len([carte for carte, dir in dejavu]))

## Part 2
starts = [ (0,'R'), (0,'D'),  (m,'L'), (m,'D'), (0+(n-1)*1j,'U'), (0+(n-1)*1j, 'R'), ((m-1)+(n-1)*1j,'U'), ((m-1)+(n-1)*1j,'L') ]
for k in range(1,m-2):
    starts.append( (k, 'D')  )
    starts.append( (k+(n-1)*1j, 'U')  )

for k in range(1,n-2):
    starts.append( ( k*1j       , 'R')  )
    starts.append( ((m-1)+k*1j  , 'L')  )

maxen = 0
for pos, dir in starts:
    dejavu = set()
    push(pos, dir)
    num = len( [carte for carte, dir in dejavu] )
    if num > maxen:
        maxen = num 

print('Part 2 :', maxen)
