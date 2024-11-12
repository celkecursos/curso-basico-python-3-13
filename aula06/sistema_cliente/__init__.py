# O arquivo __init__.py é usado para transformar uma pasta em um pacote Python.
# Se precisa apenas que o Python reconheça o diretório como um pacote, um arquivo __init__.py vazio é suficiente. 

# Ele permite que importe módulos individuais do pacote.
# Se precisa que certos módulos ou funções estejam disponíveis diretamente ao importar o pacote, pode importá-los no __init__.py.
# Exemplo: from .cliente_funcoes import adicionar_cliente
from .cliente_funcoes import adicionar_cliente