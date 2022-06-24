from struct import pack


class Conta:
    def __init__(self, CPF: str, numero: str, saldo=0.0):
        self.CPF = CPF
        self.numero = numero
        self.saldo = saldo
        self.historico = Historico()


    def inf(self):
        print(f'\nCPF: {self.CPF} \nNumero: {self.numero} \nSaldo: {self.saldo}\n')

    def movi1(self, valor: float):
        self.saldo+=valor
        self.historico.transacoes.append(f'Deposito de {valor}')


    def movi2(self, valor: float):
        if valor <= self.saldo:
            self.saldo-=valor
            self.historico.transacoes.append(f'Saque de {valor}')

        else:
            print("Saldo insuficiente")

    def transfere (self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            #banco2.saldo += valor
            self.historico.transacoes.append(f'Tranferencia de {valor}')
        else:
            print("Saldo insuficiente")

    #contax.transfere(valor, conta)
    #contas[0].transfere(100, contas[1])

class Historico:

    def __init__(self):
        self.transacoes = []

    def transacoes_bancarias(self):
        print('Transações: ')
        for i in self.transacoes:
            print("-", i)
        print('\n')


'''t=1

banco3 = Conta(CPF='145.698.854-85', numero=4758, saldo=18.0)
banco4 = Conta(CPF='145.698.854-85', numero=4758, saldo=112.0)


while t ==1:
    n = int(input(f"Área de Operação\n[0] - Exit \n[1] - Deposito \n[2] - Saque\n[3] - Extrato\n[4] - Transferência\n->"))

    if n == 1:
        Valor1 = float(input("Valor de Deposito: "))
        banco1.movi1(Valor1)
        print('\n')


    if n == 2:
        Valor2 = float(input("Valor de saque: "))
        banco1.movi2(Valor2)
        print('\n')

    if n == 3:

        banco1.inf()
        banco1.historico.transacoes_bancarias()
        #banco2.inf()

    if n== 4:
        trans = float(input("Valor da Transferencia: "))
        banco1.transfere(trans)
        print('\n')

    if n == 0:
        t=-1

'''
#Autor Endrio