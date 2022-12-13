class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    def inserir_produto(self, *produto):
        for x in [*produto]:
            self.produtos.append(x)
    def list_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total+=produto.valor
        return total
class Produto:
    def __init__(self, nome, valor):
        self.valor = valor
        self.nome = nome
