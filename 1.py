with open('1','r') as f:
    sommecal = 0
    for ligne in f.readlines():
        listenombres = []
        for x in ligne:
            if x in ['0','1','2','3','4','5','6','7','8','9']:
                listenombres.append(int(x))

        calib = 10*listenombres[0] + listenombres[-1]
        sommecal += calib


print('Part 1 : ',sommecal)

## Part 2
words = ['one','two','three','four','five','six','seven','eight','nine','0','1','2','3','4','5','6','7','8','9']
def firstword(s, words):
    for i in range(len(s)):
        for w in words:
            if s[i:i+len(w)] == w:
                return w

def lastword(s, words):
    revwords = [w[::-1] for w in words]
    revs = s[::-1]
    return firstword(revs, revwords)[::-1]


def wordtonum(s):
    match s:
        case 'one':
            return 1
        case 'two':
            return 2
        case 'three':
            return 3
        case 'four':
            return 4
        case 'five':
            return 5
        case 'six':
            return 6
        case 'seven':
            return 7
        case 'eight':
            return 8
        case 'nine':
            return 9
        case _:
            return int(s)



with open('1','r') as f:
    sommecal = 0
    for ligne in f.readlines():
        first, last = wordtonum(firstword(ligne, words)), wordtonum(lastword(ligne, words))
        sommecal += 10*first + last

print('Part 2 : ', sommecal)