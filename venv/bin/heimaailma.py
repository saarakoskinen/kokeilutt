
import math
math.pi
print("hei, maailma")
print('hei saara!')
kayttaja=input('anna nimesi ')
print("hauska tavata "+kayttaja+"!")

ympyra_str=input('anna ympyrän säde')
ympyra=float(ympyra_str)
ympyranpintaala=(ympyra*ympyra*math.pi)
print("ympyrän pinta-ala:"+str(ympyranpintaala))

suorakulmio_str=input('anna suorakulmion kanta')
suorakulmioo_str=input('ja korkeus')
suorakulmio=float(suorakulmio_str)
suora=float(suorakulmioo_str)
suorakulmionpintaala=(suorakulmio*suora)
suorakulmionpiiri=(suorakulmio*suorakulmio)+(suora*suora)
print("suorakulmion pinta-ala: "+str(suorakulmionpintaala))
print("ja piiri: "+str(suorakulmionpiiri))


luvut_str=input('syötä luku')
luvutt_str=input('toinen')
luvuttt_str=input('ja kolmas')
luvut=float(luvut_str)
luvutt=float(luvutt_str)
luvuttt=float(luvuttt_str)
summa=(luvut+luvutt+luvuttt)
tulo=(luvut*luvutt*luvuttt)
three_str=float(3)
keskiarvo=(summa/3)
print('lukujen summa on:'+str(summa))
print('lukujen tulo on: '+str(tulo))
print('ja keskiarvo: '+str(keskiarvo))


leiviskat_str=input('leiviskät')
naulat_str=input('naulat')
luoti_str=input('luodit')
leiviskat=float(leiviskat_str)
naulat=float(naulat_str)
luodit=float(luoti_str)
luoditgrammoina=float(13.3)
naulagrammoina=float(425.6)
leiviskatgrammoina=float(8512)
luoti=(13.3*luodit)
naula=(425.6*naulat)
leiviska=(8512*leiviskat)
yhteensa=(luoti+naula+leiviska)
tuhat=float(1000)
kilot=int(yhteensa/1000)
grammat=round(yhteensa%1000, 2)
print('Paino yhteensä on: '+str(kilot), 'kg ja '+str(grammat),'g')

import random
print(random.randint(0,9),random.randint(0,9),random.randint(0,9))
print(random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6))


