# Definir a classe Pessoa
class Pessoa:
    
    # Método inicializador que define atributos da classe
    def __init__(self, nome, idade, cidade):
        self.nome = nome # Declarado com público (acessível fora da classe)
        self._idade = idade # Declarado com protegido, sinalizado como protegido (acessível fora da classe). Indica que o atributo não deve ser acessado diretamente fora da classe, embora ainda seja possível. 
        self.__cidade = cidade # Declarado como privado (inacessível e imutável de fora da classe)

# Criar o objeto a partir da classe Pessoa
pessoa = Pessoa("Cesar", 18, "Curitiba")

# Chamar o atributo público
print(pessoa.nome)

# Chamar o atributo protegido
# print(pessoa._idade)

# Chamar o atributo protegido
# print(pessoa.__cidade)