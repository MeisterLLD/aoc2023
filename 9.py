sumhistory = 0

with open('9', 'r') as f:
    for ligne in f.read().splitlines():
        row = list(map(int, ligne.split(' ')))

        matrix = [row]

        while not all(x==0 for x in row):
            row2 = [row[i+1] - row[i] for i in range(len(row) - 1)]
            row = row2
            matrix.append(row2)

        matrix[-1].append(0)

        for i in range(len(matrix)-2, -1, -1):
            matrix[i].append( matrix[i][-1] + matrix[i+1][-1]   )

        sumhistory += matrix[0][-1]

print('Part 1 :',sumhistory)

## Part 2
sumhistory = 0

with open('9', 'r') as f:
    for ligne in f.read().splitlines():
        row = list(map(int, ligne.split(' ')))
        row.reverse()

        matrix = [row]

        while not all(x==0 for x in row):
            row2 = [row[i+1] - row[i] for i in range(len(row) - 1)]
            row = row2
            matrix.append(row2)

        matrix[-1].append(0)

        for i in range(len(matrix)-2, -1, -1):
            matrix[i].append( matrix[i][-1] + matrix[i+1][-1]   )

        sumhistory += matrix[0][-1]

print('Part 2 :',sumhistory)