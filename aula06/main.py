# Importa o módulo `cliente_funcoes` do pacote `sistema_cliente`.
from sistema_cliente import cliente_funcoes


# Define a função `main`, que servirá como ponto de entrada do programa.
def main():
    # Chama a função `adicionar_cliente` do módulo `cliente_funcoes`, passando o nome e o ano de nascimento.
    cliente = cliente_funcoes.adicionar_cliente("Cesar", 1986)
    # Chama a função `exibir_cliente` do módulo `cliente_funcoes`, passando o cliente criado.
    cliente_funcoes.exibir_cliente(cliente)    

if __name__ == "__main__":
    main()