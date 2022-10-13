nome=str(input('Digite um nome com mais de 3 caracter: '))
while len(nome)<=3:
    nome=str(input(f'O nome "{nome}" é menor ou igual a 3,digite novo nome: '))
idade=int(input('Digite uma idade entre 0 e 150 anos: '))
while idade<0 or idade>150:
    idade=int(input(f'A idade "{idade}"esta fora do parametro ,digite uma nova idade: '))
salario=float(input('Digite o salario maior que 0: '))
while salario<=0:
    salario=float(input(f'O valor "{salario}" foi abaixo de 0, digite o valor novamente: '))
sexo=str(input('Digte F para feminino ou M para masculino: '))
while sexo!='f' and sexo!='m':
    sexo=str(input(f'A letra "{sexo}" é diferente de F ou M ,digite novamente M ou F: '))
estadoC=str(input('Digite o seu estado civil com S;C;V;D: '))
while estadoC!='s' and estadoC!='c' and estadoC!='v' and estadoC!='d':
    estadoC=str(input(f'A letra "{estadoC}" é diferente dos exmplos, digite novamente: '))
