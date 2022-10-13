n1=float(input('digite um numero de 0 ate 10: '))
while (n1<0) or (n1>10):
    if n1<0:
        n1=float(input('O valor foi abaixa de 0 ,digite novamente: '))
    elif n1>10:
        n1=float(input('O valor foi acima de 10 ,digite o valor novamente: '))
print(f'o valor {n1} esta dentro do paramentro')