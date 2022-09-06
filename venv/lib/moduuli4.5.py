kauttajatunnus=input('Anna käyttäjätunnus: ')
salasana=input('Anna salasana: ')
oikeakt="python"
oikeass="rules"
toistot=5
yritykset=1
while (kauttajatunnus!=oikeakt or salasana!=oikeass) and (toistot>yritykset):
    kauttajatunnus = input('Anna käyttäjätunnus: ')
    salasana = input('Anna salasana: ')
    yritykset+=1

if yritykset>toistot:
    print('Pääsy evätty.')
else:
    print('Tervetuloa!')