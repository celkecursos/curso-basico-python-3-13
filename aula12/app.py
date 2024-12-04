# Definir a classe Pessoa
class Pessoa:

    # Método inicializador que define atributo da classe
    def __init__(self, nome, idade):
        self.nome = nome    # Atributo nome
        self.idade = idade  # Atributo idade

    # Método para apresentar os dados da pessoa
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criar o objeto a partir da classe Pessoa
pessoa = Pessoa("Cesar", 18)

# Chamar o método "apresentar" do objeto pessoa
pessoa.apresentar()