import random
from datetime import  datetime
from random import randint
class pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.ano_atual = self.ano_atual

    def comer(self, alimento):
        if self.comendo == True:
            print(f'{self.nome} já está comendo {alimento}, não pode comer')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_Comer(self):
        if self.comendo == True:
            print(f'{self.nome} parou de comer')
            self.comendo = False
            return
        print(f'{self.nome} não está comendo')

    def falar(self, assunto):
        if self.comendo == True:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando == True:
            print(f'{self.nome} já está falando, não pode falar')
            return
        print(f'{self.nome} está falando {assunto}')
        self.falando = True

    def parar_Falar(self):
        if self.comendo == True:
            print(f'{self.nome} não pode para de falar, pois está comendo')
            return
        if self.falando == True:
            print(f'{self.nome} parou de falar')
            self.falando = False
            return
        print(f'{self.nome} não está falando')
    def ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gerar_id():
        rand = random.randint(0,2000)
        return rand
