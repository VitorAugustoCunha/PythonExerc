numero = int(input('digite um numero '))
VetorPrimos = []
for loop in range(1,numero+1):
    if numero % loop == 0:
        VetorPrimos.append(loop)
if len(VetorPrimos)==2:
    print(f'o numero {numero} é primo')
else:
    print(f'o numero {numero} nao é primo')