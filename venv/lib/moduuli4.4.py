from random import randint
luku=randint(1,10)
arvaus=0
while luku!=arvaus:
    arvaus=int(input('Arvaa luku: '))
    if luku<arvaus:
        print('Liian suuri luku.')
    if luku>arvaus:
        print('Liian pieni arvaus.')

print('Oikein.')
