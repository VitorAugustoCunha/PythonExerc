import datetime #biblioteca calendario
from datetime import date #importa somente os dias
print('--'*15)
print('Calculo de idade ,para saber se é de maior')
print('--'*15)
dia=int(input(' Digite o dia q voce nasceu: '))
mes=int(input(' Digite o mes: '))
ano=int(input(' Digite o ano: '))
DataNascimento= datetime.date(ano,mes,dia) #colocar os dados na seguencia para o calculo
calculo=(date.today()-DataNascimento) #O ano ,mes ,dia - o dia de hoje
resuldadoF=(calculo.days/365.25) #convertendo os dias para anos
print('--'*15) #int(resuldadoF) para converte o numero decimal para interio
if resuldadoF >= 18:
    print ('Voce tem ',int(resuldadoF),' anos e é de maior.')
else :
    print ('Voce tem ',int(resuldadoF),' anos e é de menor.')
print('--'*15)