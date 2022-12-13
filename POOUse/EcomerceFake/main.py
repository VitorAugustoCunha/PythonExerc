from Classes import Produto, CarrinhoDeCompras

carinho = CarrinhoDeCompras()

iphone = Produto('Iphote', 10000)
camisa = Produto('Camisa', 30)

carinho.inserir_produto(iphone, camisa)

print(carinho.list_produto())
print(carinho.soma_total())
