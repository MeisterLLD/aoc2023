X, Y, Z, A, B, C = [], [], [], [], [], []
with open('24','r') as f:
    for ligne in f.read().splitlines():
        pos, vit = ligne.split(' @ ')
        x, y, z = pos.split(', ')
        a, b, c = vit.split(', ')
        X.append(int(x))
        Y.append(int(y))
        Z.append(int(z))
        A.append(int(a))
        B.append(int(b))
        C.append(int(c))

N = len(X)

m = 200000000000000
M = 400000000000000

def isvalid(x,y):
    return m<=x<=M and m<=y<=M

nbint = 0
for i in range(N):
    for j in range(i+1,N):
        det = A[i]*(-B[j]) - (-A[j])*B[i]
        if det == 0:
            continue
        t = 1/det*((-B[j])*(X[j]-X[i]) + A[j]*(Y[j]-Y[i]))
        s = 1/det*( -B[i]*(X[j]-X[i]) + A[i]*(Y[j]-Y[i]) )
        if t < 0 or s < 0:
            continue
        x, y = X[i]+t*A[i], Y[i] + t*B[i]
        if isvalid(x,y):
            nbint += 1

print('Part 1 :', nbint)

## Part 2
''' Manual elimination is pending but for now let's use z3... '''

import z3
N = len(A)
pos = z3.RealVector('pos', 3)
vel = z3.RealVector('vel', 3)
tim = z3.RealVector('tim', 3)

s = z3.Solver()

for i in range(3):
    s.add( pos[0]+tim[i]*vel[0] == X[i]+tim[i]*A[i]    )
    s.add( pos[1]+tim[i]*vel[1] == Y[i]+tim[i]*B[i]    )
    s.add( pos[2]+tim[i]*vel[2] == Z[i]+tim[i]*C[i]    )

s.check()

print('Part 2 :', s.model().eval(sum(pos)))

