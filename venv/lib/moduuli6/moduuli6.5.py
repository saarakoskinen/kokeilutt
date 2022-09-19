def luvut(lista):
    tyhjalista = []
    for i in lista:
        if i %2 == 0:
            tyhjalista.append(i)
    return (tyhjalista)

lukuja = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lukuja)
print(luvut(lukuja))
