log=str(input('Digite o nome do usuario:'))
senha=str(input('digite uma senha ,diferente do nome: '))
while log==senha:
    senha=str(input('Senha é igual ao nome, digite uma nova senha: '))
print('Sua senha foi salvo.')