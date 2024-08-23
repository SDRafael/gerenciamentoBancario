class Conta:
    def __init__(self, nome, nConta, tipo):
        self.nome = nome
        #self.data = data
        self.tipo = tipo
        self.saldo = 0.
        self.histMovimentacoes = []
        self.__nConta = nConta

    def deposito(self, valores):
        self.saldo += valores
        
        self.histMovimentacoes.append(f"Deposito de R$ {valores:.2f}")

    def saque(self, valores):
        if valores <= self.saldo:
            self.saldo -= valores
            self.histMovimentacoes.append(f"Saque de R$ {valores:.2f}")
        else:
            print(f"Operação negada para SAQUE {valores:.2f} por saldo insuficiente.")
            self.histMovimentacoes.append(f"Operação negada para SAQUE {valores:.2f} por saldo insuficiente.")

    def extrato(self):
        extrato = []
        consulta = f"Extrato bancário - conta: {self.__nConta}, {self.nome} - saldo: {self.saldo}"
        extrato.append(consulta)
        return extrato
    

class Sistema:
    def __init__(self) -> None:
        self.listaContas = []
        self.contas = {

        }    

    def __cadastrar(self, nome, cpf):
        self.contas["nome"] = nome
        self.contas["cpf"] = cpf
        self.contas["numero"] = None
        return
    
    def cadastro(self, nome, cpf):
        if cpf in self.contas:
            return "CPF já cadastrado"
        else:
            self.__cadastrar(nome, cpf)

        
    