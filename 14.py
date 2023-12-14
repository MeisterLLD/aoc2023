from copy import deepcopy

def weight(rows):
    weight = 0
    rows2 = list(zip(*rows))
    rows2 = [list(reversed(row)) for row in rows2]
    for row in rows2:
        for i in range(len(row)):
            if row[i] == 'O': weight += i+1
    return weight

def prepare(direction):
    ''' Prepare the data so that your push is just like a push to the east '''
    global rows
    if direction in {0,2}: # North or South
        rows = list(zip(*rows))
        rows = [list(reversed(row)) for row in rows] if direction == 0 else [list(row) for row in rows]

    if direction == 3: # West
        rows = [list(reversed(row)) for row in rows]

def unprepare(direction):
    ''' Reciprocal of prepare '''
    global rows
    if direction in {0,2}:
        rows = [list(reversed(row)) for row in rows] if direction == 0 else [list(row) for row in rows]
        rows = list(zip(*rows))
        rows = [list(row) for row in rows]

    if direction == 3:
        rows = [list(reversed(row)) for row in rows]

def push(direction):
    global rows
    prepare(direction)

    for i in range(len(rows)):
        row = rows[i]
        n = len(row)
        separators = [j for j in range(n) if row[j] == '#'] + [n]

        for nblock in range( len(separators) - 1):
            N, M = separators[nblock], separators[nblock+1]
            counto = sum( [row[j] == 'O' for j in range(N, M )])
            rows[i][N+1:M] = ['.']* (M-N-1-counto) + ['O']*counto

        if separators[0] != 0:
            deb = separators[0]
            counto = sum( [row[j] == 'O' for j in range(0, deb)])
            rows[i][0:deb] = ['.']* (deb-counto) + ['O']*counto

        if separators == []:
            deb = n
            counto = sum( [row[j] == 'O' for j in range(0, deb)])
            rows[i][0:deb] = ['.']* (deb-counto) + ['O']*counto

    unprepare(direction)

## Part 1
with open('14','r') as f:
    rows = f.read().splitlines()
    push(0) # Push North
    print('Part 1 :', weight(rows))


## Part 2
with open('14','r') as f: # Reboot !
    rows = f.read().splitlines()

init_rows = deepcopy(rows)
dejavu = {}
i = 0
found = False

while not found: # Find a period
    dejavu[i] = tuple( [tuple(row) for row in rows]   )

    for dir in [0,3,2,1]: # New cycle
        push(dir)
    i += 1

    for k in range(len(dejavu)): # period lookup
        if dejavu[k] == tuple( [tuple(row) for row in rows]   ):
            found = True
            break

period = i-k

print('Part 2 :', weight(dejavu[k + (1000000000-k)%period]))