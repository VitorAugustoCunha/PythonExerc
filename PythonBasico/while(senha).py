i=0
senha=input('digite uma nova senha: ')
while True:
    if len(senha)==0:
        senha=input('possui um vazio ,digite uma nova senha ')
    else:
        print('senha confirmada')
        break

senha2=input('digite a sua senha: ')
while senha2!=senha:
    i+=1
    if i<4:
        print(f'vc ainda tem mais {4-i} tentativas. ',end='')
        senha2=input('digite a senha novamente: ')
    else:
        break
if senha==senha2:
    print('senha correta')
else:
    print('conta bloqueada')