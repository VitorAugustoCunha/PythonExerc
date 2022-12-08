from datetime import datetime
a = input()
ar = a.replace('/', ' ')
aT = ar.split()
soma = 0
soma2 = 0

for i in range(len(aT)):
    atint = int(aT[i])
    soma+=atint

dia = datetime.strftime(datetime.now(), '%d %m %Y')
diaT = dia.split()

for i in range(len(diaT)):
    diaint = int(diaT[i])
    soma2+=diaint

if soma >= soma2:
    print("na validade")
elif soma < soma2:
    print("fora da validade")