import random
nopat = int(input('Kuinka monta noppaa? '))
lista = []

for i in range(nopat):
    nuppanum = random.randint(1,6)
    lista.append(nuppanum)

summa = sum(lista)
print(summa)