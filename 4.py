sum = 0

with open('4','r') as f:
    for ligne in f.read().splitlines():

        count = -1

        card = ligne.split('|')[0].split(':')[1]
        have = ligne.split('|')[1]
        numbers_card= list([int(x) for x in card.split(' ') if x!=''])
        numbers_have= list([int(x) for x in have.split(' ') if x!=''])

        for x in numbers_have:
            if x in numbers_card:
                count += 1

        if count >= 0:
            sum += 2**count

print(sum)

## Part 2
cards = [{'num':1, 'matches':0} for _ in range(202)]

i = -1
with open('4','r') as f:
    for ligne in f.read().splitlines():
        i += 1

        card = ligne.split('|')[0].split(':')[1]
        have = ligne.split('|')[1]
        numbers_card= list([int(x) for x in card.split(' ') if x!=''])
        numbers_have= list([int(x) for x in have.split(' ') if x!=''])

        for x in numbers_have:
            if x in numbers_card:
                cards[i]['matches'] += 1



for i in range(202):
    for _ in range(cards[i]['num']):
        for m in range(1,cards[i]['matches']+1):
            if i+m < 202:
                cards[i+m]['num'] += 1

sum = 0
for i in range(202):
    sum += cards[i]['num']

print(sum)