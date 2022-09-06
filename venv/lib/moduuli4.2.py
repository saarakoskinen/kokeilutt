tuumat =float(input('Anna tuumat: '))
while tuumat>0:
    cm_arvo = 2.54*tuumat
    vastaus = print(str(tuumat) + '"' + '=' + str(cm_arvo) + 'cm')
    tuumat = int(input('Anna tuumat: '))
if tuumat<0:
    print('Ohjelma lopetettu.')