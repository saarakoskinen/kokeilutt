
luvut = input('Syötä luku (tyhjästä syötöstä ohjelma lopettaa): ')
lista = []
import random
while luvut != '':
    lista.append(luvut)
    luvut = input('Syötä luku (tyhjästä syötöstä ohjelma lopettaa): ')

summa = random.sample(lista,5)
summaInt = (eval(i) for i in summa)
print(sum(summaInt))