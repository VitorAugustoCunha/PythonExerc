nota = []
notat = 0
soma: float=0
media = float
for loop in range(5):
    nota.append(float(input('digite a nota dos anunos')))
    soma=soma+nota[loop]
media = soma /5
print(media)
for laap in range(5):
    if nota[laap] >= media:
        print(nota[laap])
