from fly import contabancaria
'''


p1=banco_dados(0o001, 0, 'keiich', 'conta corrente', 5000)



    if self.status == False:
        res = input('deseja ativar uma conta?s/n')
        if res == 's':
            self.status = True
        else:
            pass
'''
p1 = contabancaria(9196,"Alexsandro Ribeiro","Corrente")
p1.ativarconta()
p1.ativarconta()
p1.depositar(300)
p1.desativar_conta()
p1.sacar(10)
p1.verificar_saldo()
p1.ativarconta()
p1.ativar_limite()
p1.verificar_saldo()
