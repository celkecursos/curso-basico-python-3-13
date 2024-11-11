# Estrutura Básica de uma Função em Python
def saudacao():
    print("Olá, bem-vindo ao tutorial de Python!\n")
saudacao()

# Parâmetros e Argumentos
def saudacao(nome):
    print(f"Olá, {nome}\n")
saudacao("Cesar")

# Retorno de Valores
def soma(a, b):
    return a + b
resultado = soma(5, 3)
print("Resultado:", resultado)
print()

# Funções com Parâmetros Padrão
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")
saudacao()
saudacao("Cesar")
print()

# Argumentos e Parâmetros Variáveis (*args e **kwargs)
def soma(*numeros):
    return sum(numeros)
print(soma(1, 2, 3, 4))

def exibir_informacoes(**info):
    print(info)
    for chave, valor in info.items():
        print(f"{chave}: {valor}")
exibir_informacoes(nome="Cesar", idade=18)
print()

# Escopo de Variáveis
def numero():
    x = 10 # Variável local
    print("Variável local:", x)
numero()

x = 5 # Variável global
print("Variável global:", x)
print()

# Funções Lambda (Funções Anônimas)
dobro = lambda x: x * 2
print(dobro(2))

# Este lambda é equivalente 
def dobro(x):
    return x * 2
print(dobro(2))