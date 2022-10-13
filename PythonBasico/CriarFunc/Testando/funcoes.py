def funcao():
    print('Bloco de Código')

def imprime_nome(nome):
    print(f'Nome: {nome}')

def repetir(n):
    for x in range(1,n+1):
        print( f'{x}' *x)

def repete(z):
    for x in range(1,z+1):
        for y in range(1,x+1):
            print(y, end=" ")
        print('\n')

def vogais(letras):
    cont=0
    letras = letras.upper()
    for x in letras:
        if x in ['A','E','I','O','U']:
            cont+=1
    print(f'Existem {cont} vogais')

def valor_total(produto,valor,quantidade):
    mult=quantidade*valor
    return mult

def numeros(nu):
    if nu > 0:
        return 'P'
    elif nu < 0:
        return 'N'
    elif nu == 0:
        return 'Z'

def mediasAlunos (n1,n2,nome):
    alunos = []
    medias = []
    media=(n1+n2)/2
    alunos.append(nome)
    medias.append(media)
    return alunos, medias

def loopUm():
    n = 0
    while n < 5:
        print("Hello Pythonista")
        n+=1
        if n == 3:
            break
def loopDois():
    n = 0
    while n < 5:
        if n == 2:
            n+=1
            continue
        print("Hello Pythonista")
        n+=1

def loopTres():
    z = 0
    while z < 3:
        if z == 0:
            print("z é ",z)
            z+=1
        elif z == 1:
            print("z é ",z)
            z+=1
        else:
            print("z é ",z)
            z+=1

def listUm():
    minhaLista = []
    i = 0
    while len(minhaLista) < 4:
        minhaLista.append(i)
        i+=1
    print(minhaLista)

def loopQuatro():
    n = 10
    while n <=100:
        print(n, end = ";")
        n+=10

def listDois():
    minhaTuple = (23, 45, 12, 10, 25)
    i = 0

    while i < len(minhaTuple):
        print(minhaTuple[i])
        i+=1

def listTres():
    minhaLista = [23, 45, 12, 10, 25]
    i = 0
    sum = 0

    while i < len(minhaLista):
        sum += minhaLista[i]
        i+=1
    print(sum)

def listQuatro():
    listaFrutas = ["Limão","Abacate","Jambo","Laranja"]

    while listaFrutas:
        print(listaFrutas.pop())
    print(listaFrutas)

def exerUm():
    i = 0
    palavra = "O êxito é ir de frustração a frustração sem perder a animação"

    while i < len(palavra):
        if palavra[i] == "e" or palavra[i] == "o":
            i+=1
            continue
        print(palavra[i], end="")
        i+=1

def loopCinco():
    n = int(input("Digite um número: "))

    while n != 0:
        n = int(input("Digite zero para sair: "))

def loopSeis():
    p = 5
    soma = 0
    count  = 0

    while p > 0:
        count+=1
        f = int(input("Digite um número: "))
        soma += f
        p-=1

    media = soma/count
    print("Media do número recebidos ", media)

def loopSete():
    n = 1

    while n <= 5:
        quadradonum = n**2
        print(f"O quadrado de {n} é {quadradonum}")
        n+=1









