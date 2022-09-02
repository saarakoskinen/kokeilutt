minpituus=37
kuha=int(input('Anna kuhan pituus: '))
puuttuva_pituus=minpituus-kuha
if kuha>=37:
    print('Kuha ei ole alimittainen.')
if kuha<=36:
    print('Kuha on alimittainen, heitä takaisin. '+str(puuttuva_pituus)+ 'cm')

print('hyttiluokat: LUX, A, B, C')
hyttiluokat=['LUX', 'A', 'B', 'C']
hytti=input('Syötä hyttiluokka: ')
if hytti==hyttiluokat[0]:
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif hytti==hyttiluokat[1]:
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif hytti==hyttiluokat[2]:
    print('C on ikkunaton hytti autokannen alapuolella.')
elif hytti==hyttiluokat[3]:
    print('LUX on parvekkeellinen hytti yläkannella.')
else:
    print('Virheellinen hyttiluokka')

print('nainen vai mies')
sukupuoli=(input('Syötä biologinen sukupuolesi pienin kirjaimin: '))
hemoglobiini=float(input('Syötä hemoglobiiniarvosi (g/l): '))
sukupuolet=['nainen', 'mies']
if sukupuoli==sukupuolet[0]:
    if hemoglobiini<=116:
        print('Hemoglobiini liian matala.')
    if hemoglobiini>=176:
        print('Hemoglobiini liian korkea.')
    if hemoglobiini>=117 and hemoglobiini<=175:
        print('Hemoglobiini normaali.')

if sukupuoli==sukupuolet[1]:
    if hemoglobiini<=133:
        print('Hemoglobiini liian matala.')
    if hemoglobiini>=196:
        print('Hemoglobiini liian korkea.')
    if hemoglobiini<=195 and hemoglobiini>=134:
        print('Hemoglobiini normaali.')


vuosi=float(input('Anna vuosiluku: '))
if vuosi%4==0 and (vuosi%100!=0 or vuosi%400==0):
    print('Kyseinen vuosi on karkausvuosi.')
else:
    print('Kyseinen vuosi ei ole karkausvuosi.')