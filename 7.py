handsandbids = [ ]
with open('7', 'r') as f:
    for ligne in f.read().splitlines():
        handsandbids.append( (ligne.split(' ')[0], int(ligne.split(' ')[1])) )


def handtype(s):

    setnumbers = set()
    numpairs = 0

    for x in s:
        num = s.count(x)
        setnumbers.add( num  )
        if num==2: numpairs += 1

    if 5 in setnumbers: return 6 # five of a kind
    if 4 in setnumbers: return 5 # four of a kind
    if 3 in setnumbers and 2 in setnumbers: return 4 # full house
    if 3 in setnumbers: return 3 # three of a kind

    return numpairs//2 # other cases


L = list('AKQJT98765432')
l = list('abcdefghijklm')
def f(char):
    i = L.index(char)
    return l[i]


def greater(hb1,hb2):
    s, _ = hb1
    t, _ = hb2
    if handtype(s) < handtype(t): return -1
    if handtype(s) > handtype(t): return 1
    if [f(x) for x in s] >= [f(x) for x in t]: return -1
    else: return 0

import functools
sor = sorted(handsandbids, key = functools.cmp_to_key(greater))

sum = 0
for i in range(len(sor)):
    sum += sor[i][1]*(i+1)

print('Part 1', sum)

## Part 2
def handtype2(s):
    max = 0
    for x in L:
        if handtype(s.replace('J',x)  ) > max:
            max = handtype(s.replace('J',x)  )

    return max

L2 = list('AKQT98765432J')
l2 = list('abcdefghijklm')

def f2(char):
    i = L2.index(char)
    return l2[i]


def greater2(hb1,hb2):
    s, _ = hb1
    t, _ = hb2
    if handtype2(s) < handtype2(t): return -1
    if handtype2(s) > handtype2(t): return 1
    if [f2(x) for x in s] >= [f2(x) for x in t]: return -1
    else: return 0

sor = sorted(handsandbids, key = functools.cmp_to_key(greater2))

sum = 0
for i in range(len(sor)):
    sum += sor[i][1]*(i+1)

print('Part 2', sum)
