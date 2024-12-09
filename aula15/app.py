# Classe base Pessoa (classe pai)
class Pessoa:
    def __init__(self, nome, cidade):
        self.nome = nome # Atributo público
        self.cidade = cidade # Atributo público

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} moro em {self.cidade}.")

# Classe derivada Funcionario, herda de Pessoa (classe filha)
class Funcionario(Pessoa):
    def __init__(self, nome, cidade, cargo, salario):
        super().__init__(nome, cidade)
        self.cargo = cargo
        self.salario = salario

    def apresentar_funcionario(self):
        self.apresentar()
        print(f"Eu trabalho com {self.cargo} e meu salário é de R$ {self.salario:.2f}.")

# Classe derivada Cliente, herda de Pessoa (classe filha)
class Cliente(Pessoa):
    def __init__(self, nome, cidade, saldo):
        super().__init__(nome, cidade)
        self.saldo = saldo

    def apresentar_cliente(self):
        self.apresentar()
        print(f"Saldo do cliente {self.saldo:.2f}.")

# Criar o objeto da classe Funcionário
funcionario = Funcionario("Cesar", "Curitiba", "Desenvolvedor", 50.00)
# Chamar o método de apresentação do funcionário
funcionario.apresentar_funcionario()

# Criar o objeto da classe Cliente
cliente = Cliente("Kelly", "Manaus", 252.00)
# Chamar o método de apresentação do Cliente
cliente.apresentar_cliente()

