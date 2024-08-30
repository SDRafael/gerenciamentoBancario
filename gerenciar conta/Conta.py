import mysql.connector;
from datetime import datetime, date;

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
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "user",
            password = "***",
            database = "db_name"

        )
        self.cursor = self.connection.cursor()
        self.createTable()
    def createTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Contas(
                id INT AUTO_INCREMENT PRIMARY KEY,
                Nome VARCHAR(100),
                CPF VARCHAR(20),
                Conta VARCHAR(30),
                Abertura DATE,
                Tipo VARCHAR(10),
                Saldo FLOAT)
            """)
        self.connection.commit()

    def cadastrar(self, nome, cpf, nConta, dataAbertura, tipo):
        cadastro = Conta(nome, cpf, nConta, dataAbertura, tipo)
        
        self.cursor.execute("SELECT * FROM Contas WHERE Conta = %s", (nConta,))
        if self.cursor.fetchone(): #verifica se o numero da conta passado para o método cadastrar já existe
            print(f"Número de conta {nConta} já existe")
        else:
            self.cursor.execute("""
                INSERT INTO Contas (Nome, CPF, Conta, Abertura, Tipo, Saldo)
                VALUES (%s, %s, %s, %s, %s, %s)


                """, (nome, cpf,nConta, dataAbertura, tipo, cadastro.saldo))
            self.connection.commit()
            print("Cadastro efetuado com sucesso!")


        

    def consultaConta(self, nConta):
        self.cursor.execute("SELECT * FROM Contas WHERE Conta = %s", (nConta,))

        contaCOnsulta = self.cursor.fetchone()
        if contaCOnsulta:
            nome, cpf, nConta, dataAbertura, tipo, saldo = contaCOnsulta[1:]
            conta = Conta(nome, cpf, nConta, dataAbertura, tipo)
            conta.saldo = saldo
            return conta
        else: 
            print("A conta não existe")
            return None
        
    def closeConnection(self):
        self.cursor.close()
        self.connection.close()
        
        
gerente = Sistema()

gerente.cadastrar("Maria do Ibura", "000.000.000-01", "001", date(2024, 2, 1), "corrente" )
gerente.cadastrar("Tõe de Irineu do Peixe", "100.001.000-02", "002", date(2024, 4, 2), "poupança")
gerente.cadastrar("Jessé da Ambulância", "098.000.020-20", "003", date(2024, 8, 6), "corrente")


consultaGerente = gerente.consultaConta("001")
if consultaGerente:
    consultaGerente.detalhes()
    print(consultaGerente.getSaldo())
    consultaGerente.depositar(500)
    print(f"pós deposito {consultaGerente.getSaldo()}")
    consultaGerente.sacar(300)
    consultaGerente.verExtrato()

gerente.closeConnection()
