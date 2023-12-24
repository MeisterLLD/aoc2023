workflows = { }
location = [ ]
xx = [ ]
mm = [ ]
aa = [ ]
ss = [ ]

with open('19','r') as f:
    f1, f2 = f.read().split('\n\n')
    for ligne in f1.splitlines():
        name, tests = ligne.split('{')
        tests = tests[:-1].split(',')
        workflows[name] = tests

    for i, part in enumerate(f2.splitlines()):
        part = part[:-1]
        location.append('in')
        x, m, a, s = [int(truc.split('=')[1]) for truc in part.split(',')]
        xx.append(x)
        mm.append(m)
        aa.append(a)
        ss.append(s)

N = len(location)
for i in range(N):
    x, m, a, s = xx[i], mm[i], aa[i], ss[i]

    while location[i] not in {'A', 'R'}:
        loc = location[i]
        for workflow in workflows[loc]:
            if ':' in workflow:
                test, newloc = workflow.split(':')
                if eval(test):
                    location[i] = newloc
                    break

            else:
                location[i] = workflow


print('Part 1 :',  sum( [ xx[i]+mm[i]+aa[i]+ss[i] for i in range(N) if location[i]=='A' ]   ))

## Part 2
from copy import deepcopy
from math import prod

def numacc(ranges, starting_workflow ):
    # Cas de base
    if starting_workflow == 'A':
        return prod([max(  p[1] - p[0] + 1   ,0) for p in ranges.values() ])
    if starting_workflow == 'R':
        return 0

    # Appels récursifs
    num = 0

    for rule in workflows[starting_workflow]:
        if ':' in rule:
            test, dest = rule.split(':')
            if '<' in test:
                lhs, rhs = test.split('<')

                newbound =  min( int(rhs)-1, ranges[lhs][1] )

                yes = (ranges[lhs][0],  newbound     )
                no = ( newbound + 1   , ranges[lhs][1])
                ranges_yes = deepcopy(ranges)
                ranges_yes[lhs] = yes
                ranges[lhs] = no

                num += numacc(ranges_yes, dest)
            elif '>' in test:
                lhs, rhs = test.split('>')

                newbound = max( int(rhs)+1, ranges[lhs][0] )

                yes = (  newbound ,    ranges[lhs][1]   )
                no = (  ranges[lhs][0],     newbound - 1   )
                ranges_yes = deepcopy(ranges)
                ranges_yes[lhs] = yes
                ranges[lhs] = no

                num += numacc(ranges_yes, dest)
        else:
            num += numacc(ranges, rule)

    return num

ranges = {'x':(1,4000), 'm':(1,4000), 'a':(1,4000), 's':(1,4000)  }
print('Part 2 :', numacc(ranges,'in'))
