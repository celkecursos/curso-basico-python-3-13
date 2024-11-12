# Importar a classe `datetime` do módulo `datetime`, que fornece funções para manipular datas e horas.
from datetime import datetime

# Define a função `adicionar_cliente`, que recebe o `nome` e o `ano_nascimento` como parâmetros.
def adicionar_cliente(nome, ano_nascimento):
    """Adicionar um cliente ao sistema""" # Essa é uma docstring explicando a função

    # Obter o ano atual com `datetime.now().year`
    ano_atual = datetime.now().year

    # Calcular a idade do cliente subtraindo o ano de nascimento do ano atual.
    idade = ano_atual - ano_nascimento

    # Usa uma `f-string` para formatar e imprimir o nome e a idade do cliente.
    print(f"Nome: {nome} \nIdade: {idade}")

