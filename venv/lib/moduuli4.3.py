numero=input('Syötä luku: ')
lista=[]
while numero!='':
    numero = input('Syötä luku: ')
    if numero!='':
        lista.append(numero)
print('Ohjelma lopetettu.')
print('Pienin: '+ min(lista) + (' Suurin: ') + max(lista))
