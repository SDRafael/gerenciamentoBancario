from datetime import datetime;

class Conta:
    def __init__(self, nome, cpf, nConta, dataAbertura, tipo):
        self.nome = nome
        self.dataAbertura = dataAbertura
        self.tipo = tipo
        self.saldo = 0
        self.histMovimentacoes = []
        self.nConta = nConta
        self.cpf = cpf

    def detalhes(self):
        print(f"""
                Nome: {self.nome}
                cpf: {self.cpf}
                Numero da conta:{self.nConta}
                Data da abertura:{self.dataAbertura}
                TIpo de conta: {self.tipo}
              """)
    def depositar(self, valores):
        if valores > 0:
            self.saldo += valores
            
            self.histMovimentacoes.append(f"Deposito de R$ {valores:.2f} em {datetime.now()}")
            print(f"Valor depositado de R$ {valores}. Saldo atual de R${self.saldo}")
        else:
            print(f"Depósito inválido")
            
    def sacar(self, valores):
        if valores <= self.saldo:
            self.saldo -= valores
            self.histMovimentacoes.append(f"Saque de R$ {valores:.2f} em {datetime.now()}")
            print(f"Saque efetuado no valor de R${valores}")
        else:
            print(f"Operação negada para SAQUE {valores:.2f} por saldo insuficiente.")
            self.histMovimentacoes.append(f"Operação negada para SAQUE {valores:.2f} em {datetime.now()} por saldo insuficiente.")

    def getSaldo(self):
        return self.saldo
    def verExtrato(self):
        print(f"Extrato bancário - conta: {self.nConta}, {self.nome} - saldo: {self.saldo}")
        for mov in self.histMovimentacoes:
            print(mov)

        print(f"saldo atual de R${self.saldo}")
        
    

class Sistema:
    def __init__(self):
        #self.listaContas = []
        self.contas = {

        }    

    def cadastrar(self, nome, cpf, nConta, dataAbertura, tipo):
        cadastro = Conta(nome, cpf, nConta, dataAbertura, tipo)
        
        if nConta in self.contas:
            print(f"A conta de número {nCOnta} já existe. Operação NEGADA!")

        else:
            self.contas[nConta] = cadastro
            print(f"Cadastro efetuado para conta de número {nConta}!")

    def consultaConta(self, nConta):
        return self.contas.get(nConta, None)
        
gerente = Sistema()

gerente.cadastrar("Maria do Ibura", "000.000.000-01", "001", "2024-02-01", "corrente" )
gerente.cadastrar("Tõe de Irineu do Peixe", "100.001.000-02", "002", "2024-04-02", "poupança")
gerente.cadastrar("Jessé da Ambulância", "098.000.020-20", "003", "2024-08-06", "corrente")


consultaGerente = gerente.consultaConta("001")
"""if consultaGerente:
    consultaGerente.detalhes()

else:
    print("Conta inexistente")"""
#
# ABAIXO UM PEQUENO TESTE
#
print(consultaGerente.getSaldo())
consultaGerente.depositar(500)
print(f"pós deposito {consultaGerente.getSaldo()}")
consultaGerente.sacar(300)
consultaGerente.verExtrato()
