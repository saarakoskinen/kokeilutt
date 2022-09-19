
def gal(gallo):
    return gallo*3.785
gallo = 1
while gallo > 0:
    gallo = float(input('Syötä gallonat: '))

    if gallo < 0:
      print('Ei sallittu')
      break
    print(f'{gallo} galloonaa on', f'{gal(gallo)} litraa')