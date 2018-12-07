class Conta:
    def __init(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0.0

    def depositar(self, quantia):
        self.saldo += quantia

    def sacar(self, quantia):
        if(quantia <= self.saldo):
            self.saldo -= quantia
