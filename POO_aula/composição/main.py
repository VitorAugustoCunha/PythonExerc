from Classes import Cliente
cliente = Cliente('Vitor', 19)
cliente.inserir_endereco('Recife', 'PE')

print(cliente.nome)
cliente.lista_enderecos()
