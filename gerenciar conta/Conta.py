import mysql.connector;
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
        self.conection = mysql.connector.connect(
            host = "localhost",
            user = "user"
            password = "password"
            database = "nome do banco"

        )
        self.cursor = self.conection.cursor()
        self.createTable()
    def createTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Contas(
                id INT AUTO_INCREMENT PRIMARY_KEY,
                Nome VARCHAR(100),
                CPF VARCHAR(15),
                Conta VARCHAR(30),
                Abertura VARCHAR(8),
                Tipo VARCHAR(1),
                Saldo FLOAT 

            )

            """)
        self.conection.commit()

    def cadastrar(self, nome, cpf, nConta, dataAbertura, tipo):
        cadastro = Conta(nome, cpf, nConta, dataAbertura, tipo)
        
        self.cursor.execute("SELECT FROM Contas WHERE nConta = %s", (nConta,))
        if self.cursor.fetchone(): #verifica se o numero da conta passado para o método cadastrar já existe
            print(f"Número de conta {nConta} já existe")
        else:
            self.cursor.execute("""
                INSERT INTO Contas (Nome, CPF, Conta, Abertura, Tipo, Saldo)
                VALUES (%s, %s, %s, %s, %s, %s)


                """, (nome, cpf,nConta, dataAbertura, tipo, cadastro.saldo))
            self.conection.commit()
            print("Cadastro efetuado com sucesso!")


        """if nConta in self.contas:
            print(f"A conta de número {nCOnta} já existe. Operação NEGADA!")

        else:
            self.contas[nConta] = cadastro
            print(f"Cadastro efetuado para conta de número {nConta}!")"""

    def consultaConta(self, nConta):
        return self.contas.get(nConta, None)
#
#Os objetos abaixo poderão enfrentar conflito pois não estão adequados à integração com Mysql
#
gerente = Sistema()

gerente.cadastrar("Maria do Ibura", "000.000.000-01", "001", "2024-02-01", "corrente" )
gerente.cadastrar("Tõe de Irineu do Peixe", "100.001.000-02", "002", "2024-04-02", "poupança")
gerente.cadastrar("Jessé da Ambulância", "098.000.020-20", "003", "2024-08-06", "corrente")


consultaGerente = gerente.consultaConta("001")
"""if consultaGerente:
    consultaGerente.detalhes()

else:
    print("Conta inexistente")"""

print(consultaGerente.getSaldo())
consultaGerente.depositar(500)
print(f"pós deposito {consultaGerente.getSaldo()}")
consultaGerente.sacar(300)
consultaGerente.verExtrato()
