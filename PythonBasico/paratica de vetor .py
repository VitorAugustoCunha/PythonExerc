lista_compras=['1','2','3']
for lopp in range (2):
    lista_compras.append(str(input('fala merda:')))'''.append serve para colocar no ultimo lugar da lista'''


for i in lista_compras:
    print (i)
lista_compras.insert(int(input('digite o local p digitra: ')),input('nome'))'''.inset serve para inserir o dado no local que deseja'''

print(lista_compras)
print('+++'*14)
a=int(input('digite o local pra apagar: '))
del lista_compras[a]     '''deletar o local que deseja'''
for i in lista_compras:
    print(i)
item=lista_compras.pop(+2)

print('---'*14)
print(lista_compras)
