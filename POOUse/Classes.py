class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

    @property
    def nome(self):
        return self.__nome

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca
    def escrever(self):
        print(f"Caneta {self.__marca} Escrevendo")

class MaquinaDesEscrever:
    def escrever(self):
        print("Maquina Escrevendo")