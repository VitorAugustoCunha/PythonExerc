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







