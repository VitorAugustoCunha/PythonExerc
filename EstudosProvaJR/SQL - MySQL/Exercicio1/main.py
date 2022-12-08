from escola import Sala1
from escola import Sala2

continuar = True

while continuar == True:
    h = int(input("O que pretente fazer?\n1 - Adicionar auluno\n2- Ver Media\n3 - Sair "))
    if h == 1:
        y = int(input("Qual sala?\n1 - Sala 1\n2 - Sala 2 "))
        if y == 1:
            nome = input("Nome do aluno: ")
            nota1 = int(input("Nota 1 do aluno: "))
            nota2 = int(input("Nota 2 do aluno: "))
            nota3 = int(input("Nota 3 do aluno: "))
            aluno = Sala1(nome, nota1, nota2, nota3)
            aluno.adicionar_aluno()

        elif y == 2:
            nome = input("Nome do aluno: ")
            nota1 = int(input("Nota 1 do aluno: "))
            nota2 = int(input("Nota 2 do aluno: "))
            nota3 = int(input("Nota 3 do aluno: "))
            aluno = Sala2(nome, nota1, nota2, nota3)
            aluno.adicionar_aluno()
    elif h == 2:
        y = int(input("Qual sala?\n1 - Sala 1\n2 - Sala 2 "))
        if y == 1:
            x = int(input("Digite o ID: "))
            media = Sala1.calcular_media(x)
            print(media)

        if y == 2:
            x = int(input("Digite o ID: "))
            media = Sala2.calcular_media(x)
            print(media)
    elif h == 3:
        continuar = False