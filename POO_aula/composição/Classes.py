class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []
    def inserir_endereco(self, cidade, estado):
        self.endereco.append(Enderecos(cidade, estado))
    def lista_enderecos(self):
        for enderecos in self.endereco:
            print(enderecos.cidade, enderecos.estado)
class Enderecos:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
