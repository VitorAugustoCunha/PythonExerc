'''
class banco_dados:

    def __init__(self,numero,saldo,nome,tipo,limites,status=False):
        self.numero=numero
        self.saldo=saldo
        self.nome=nome
        self.tipo=tipo
        self.status=status
        self.limites=limites

        def depositar(self,deposito):
            if self.status== False:
                print ('conta esta desativada ')
            else:
                self.saldo+deposito
            return
        def sacar(self,saque):
            if self.status== False:
                print ('conta esta desativada ')
            else:
                if self.saldo<saque:
                    print('saldo insulficiente')
                else:
                    self.saldo-saque



    def ativarconta(self):
         self.status = True

    def desativarconta(self):

         self.status = False

    def verificarsaldo(self):
        print(self.saldo)
'''
class contabancaria:
    def __init__(self,numero,nome,tipo,saldo=0,status=False,limite=0):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.__saldo = saldo
        self.__status = status
        self.__limite = limite
    def ativarconta(self):
        if self.__status == False:
            print(f'{self.__status} Sua conta está ativada')
            self.__status = True
        else:
            self.__status == True
            print(f'{self.__status} Sua conta já está ativada')
    def depositar(self,valor):
        if self.__status == False:
            print(f'{self.__status} A conta está inativa, você não pode realizar o depositp')
        else:
            self.__saldo = self.__saldo + valor
            print(f'{self.__saldo} Deposito realizado com sucesso')
    def sacar(self,saque):
        if self.__status == False:
            print(f'Conta desativada')
        elif self.__saldo<saque:
            print(f'Saldo insuficiente')
        else:
            self.__saldo = self.__saldo - saque
            print(f'{self.__saldo} Saque efetuado com sucesso')
    def verificar_saldo(self):
        if self.__status == False:
            print(f'Conta desativada')
        elif self.__status == True and self.__limite == True:
            print(f'Seu limite é:{self.__limite} e seu saldo é:{self.__saldo}')
        else:
            print(f'{self.__saldo} Este é o seu saldo')
    def ativar_limite(self):
        if self.__status == True:
            self.__limite = 1000
            print(f'{self.__limite} Seu limite foi ativado')
        elif self.__status == False:
            print(f'{self.__status} Limite não pode ser ativado, pois a conta está desativada')
    def desativar_conta(self):
        self.__status = False
        print(f'{self.__status} Sua conta está desativada')


