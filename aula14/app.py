# Definir a classe Pessoa
class Pessoa:
    
    # Método inicializador que define atributos da classe
    def __init__(self, nome):
        self.nome = nome # Declarado com público (acessível fora da classe)
        self._idade = 18 # Declarado com protegido, sinalizado como protegido (acessível fora da classe). Indica que o atributo não deve ser acessado diretamente fora da classe, embora ainda seja possível. 
        self.__cidade = "Cuiabá" # Declarado como privado (inacessível e imutável de fora da classe)

    # Getter par ao atributo _idade (protegido)
    def get_idade(self):
        return self._idade
    
    # Setter para o atributo _idade (protegido)
    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            print("Idade inválida. Deve ser um número positiva")

    # Getter para o atributo __cidade (privado)
    def get_cidade(self):
        return self.__cidade

    # Setter para o atributo __cidade (privado)
    def set_cidade(self, nova_cidade):
        self.__cidade = nova_cidade

# Criar o objeto a partir da classe Pessoa
pessoa = Pessoa("Cesar")

# Chamar o atributo público
print("Nome", pessoa.nome)

# Chamar o atributo protegido
# print(pessoa._idade)
# Acessar e modificar o atributo protegido usando getter e setter
print("Idade atual:", pessoa.get_idade())
pessoa.set_idade(19)
print("Nova idade:", pessoa.get_idade())

# Chamar o atributo protegido
# print(pessoa.__cidade)
# Acessar e modificar o atributo privado usando getter e setter
print("Cidade atual:", pessoa.get_cidade())
pessoa.set_cidade("Curitiba")
print("Nova cidade:", pessoa.get_cidade())