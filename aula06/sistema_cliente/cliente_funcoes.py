# Importa a classe `datetime` do módulo `datetime`, que fornece funções para manipulação de datas e horas.
from datetime import datetime

# Define a função `adicionar_cliente`, que recebe o `nome` e o `ano_nascimento` como parâmetros.
def adicionar_cliente(nome, ano_nascimento):
    """Adicionar um cliente ao sistema""" # Essa é uma docstring explicando a função

    # Calcula a idade do cliente chamando a função `calcular_idade`, passando o ano de nascimento.
    idade = calcular_idade(ano_nascimento)

    # Retorna um dicionário contendo o `nome` e a `idade` do cliente.
    return {"nome": nome, "idade": idade}

# Calcula a idade atual com base no ano de nascimento fornecido.
def calcular_idade(ano_nascimento):
    """Calcula a idade do cliente com base no ano de nascimento""" # Essa é uma docstring explicando a função

    # Obtém o ano atual chamando `datetime.now().year`, que retorna o ano da data e hora atuais.
    ano_atual = datetime.now().year

    # Retorna a idade, subtraindo o ano de nascimento do ano atual.
    return ano_atual - ano_nascimento

# Define a função `exibir_cliente`, que recebe um dicionário `cliente` como parâmetro.
def exibir_cliente(cliente):
    """Exibe as informações do cliente""" # Essa é uma docstring explicando a função
    # Usa uma `f-string` para formatar e imprimir o nome e a idade do cliente.
    print(f"Nome: {cliente['nome']} \nIdade: {cliente['idade']}")

