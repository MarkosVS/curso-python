class Conta:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.__saldo = 0.0

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, novo):
        self.__saldo = novo

    def sacar(self, quantia):
        if(self.__saldo >= quantia):
            self.__saldo -= quantia

    def depositar(self, quantia):
        self.__saldo += quantia


class ContaCorrente(Conta):
    def __init__(self, nome, cpf):
        super.__init(nome, cpf)


class ContaPoupanca(Conta):
    def __init__(self, nome, cpf):
        super.__init(nome, cpf)
        self.rendimento = 0.01

    def render(self):
        novo = self.saldo + (self.saldo * self.rendimento)
        self.set_saldo(novo)


class ContaConjunta(Conta):
    def __init__(self, nome, cpf):
        super.__init(nome, cpf)


c = ContaConjunta(('José', 'Maria'), ('02932', '139714'))
print(c)
