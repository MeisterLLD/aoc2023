times = [51, 69, 98, 78]
records = [377, 1171, 1224, 1505]

mulnumbers = 1

for i in range(4):
    time = times[i]
    record = records[i]

    x = 0
    while (time - x)*x <= record:
        x += 1

    numbers = 0
    while (time - x)*x > record:
        numbers += 1
        x += 1

    mulnumbers *= numbers

print('Part 1 : ', mulnumbers)

## Part 2
time = 51699878
record = 377117112241505

from math import sqrt, floor, ceil

def numbers(time, record):
    Delta = time**2 - 4*record
    return  ceil( (time + sqrt(Delta))/2 - 1  ) - floor( (time - sqrt(Delta))/2  + 1 ) + 1

print('Part 2 : ', numbers(time,record))

