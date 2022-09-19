import random
def nopanheitto(silmaluku):
    return random.randint(1, silmaluku)
tahko = int(input('Anna tahkojen määrä: '))
noppa = 0
while noppa != tahko:
    noppa = nopanheitto(tahko)
    print(noppa)
