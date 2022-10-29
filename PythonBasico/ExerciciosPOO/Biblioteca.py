class Pessoa:
    def __init__(self,nome,idade,peso,comendo = False,falando = False, dormindo = False):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo

    def comer(self):

        if self.dormindo == True:
            print(f"{self.nome} Está dormindo, e não pode comer dormindo")

        elif self.comendo == True:
            print(f"{self.nome} já está comendo")

        else:
            print(f"{self.nome} começou a comer.")
            self.comendo = True

    def parar_de_comer(self):
        if self.comendo == False:
            print(f"{self.nome} ainda não começou a comer.")

        else:
            print(f"{self.nome} parou de comer.")
            self.comendo = False

    def falar(self):
        if self.comendo == True:
            print(f"{self.nome} não pode falar, pois está comendo.")

        elif self.dormindo == True and self.falando == False:
            print(f"{self.nome} Está falando dormindo.")

        elif self.falando == True:
            print(f"{self.nome} Ja está falando.")
        else:
            print(f"{self.nome} começou a falar")
            self.falando = True

    def parar_de_falar(self):
        if self.falando == False:
            print(f"{self.nome} ainda não começou a falar")
        else:
            print(f"{self.nome} parou de falar.")
            self.falando = False

    def dormir(self):

        if self.dormindo == True:
            print(f"{self.nome} já está dormindo")

        elif self.comendo == True:
            print(f"{self.nome} está comendo e não pode dormir")

        elif self.falando == True:
            print(f"{self.nome} está falando e não pode dormir")

        else:
            print(f"{self.nome} foi dormir")
            self.dormindo = True

    def parar_de_dormir(self):
        if self.dormindo == False:
            print(f"{self.nome} ainda não foi dormir")
        else:

            print(f"{self.nome} parou de dormir")
            self.dormir = False

class Banco:
    def __init__(self,numero,saldo,nome,tipo,limite,status = False):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = status
        self.limite = limite

    def verificar_saldo(self):
        if self.status == True:
            print(f"seu saldo é: {self.saldo}")


    def depositar(self,deposito):
        if self.status == True:
            self.saldo += deposito
            return self.saldo
        else:
            print("Você não possui uma conta registrada no banco,"
                  "ou ela está desativada")

    def sacar(self,saque):
        if self.status == True:
            if self.saldo > 0 and saque <= self.saldo:
                print(f"você sacou: {saque}")
                self.saldo -= saque
                return self.saldo

            if self.saldo < saque:
                self.saldo -= saque
                return self.saldo

            if self.saldo < 0 and self.limite >= 0:
                self.limite += self.saldo
                print(f"Seu saldo é:{self.saldo}, porem seu limite "
                             f"foi reduzido para {self.limite}")

            else:
                print("Você não possui saldo para saque")