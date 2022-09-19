import math
pi = math.pi
def pizza(halkaisija, hinta):
    return hinta / (pi * math.pow((halkaisija / 2),2) / 10000)

pizza1 = float(input('Anna pizzan 1 halkaisija: '))
pizza1e = float(input('Anna pizzan 1 hinta: '))
pizza2 = float(input('Anna pizzan 2 halkaisija: '))
pizza2e = float(input('Anna pizzan 2 hinta: '))

pizza1s = pizza(pizza1,pizza1e)
pizza2s = pizza(pizza2, pizza2e)

print('Pizza 1: ',pizza1s, '€ / m2')
print('Pizza 2: ',pizza2s, '€ / m2')

if pizza1s == pizza2s:
    print('Pizzat ovat saman hintaisia.')
elif pizza1s < pizza2s:
    print('pizza 1 on halvempi.')
else:
    print('Pizza 2 on halvempi.')