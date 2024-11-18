# Função map()
# map(função, iterável)

# Lista de valores iniciais
valores = [1000, 1500, 2000, 2500, 3000]
print("Valores iniciais:", valores)

# Função para calcular o juro de 2%
calcular_juro = lambda valor: valor * 1.02

# Usar map() para aplicar a função a cadp item da lista
valores_com_juro = list(map(calcular_juro, valores))

# Exibir os valors com juro de 2%
print("Valores com juro de 2% aplicados:", valores_com_juro)

# Função map() com lambda
valores_iniciais = [5000, 5500, 6000, 6500, 7000]
print("Valores iniciais:", valores_iniciais)
valores_com_juro = list(map(lambda valor: valor * 1.02, valores_iniciais))
print("Valores com juro de 2% aplicados:", valores_com_juro)
print()

# Função filter
# filter(função, iterável)

# Criar a função para verificar se um número é par
def verificar_numero_par(x):
    return x % 2 == 0

# Lista de números
numeros = [1, 2, 3, 4, 5, 6]

# Usar filter() para filtrar números pares
pares = filter(verificar_numero_par, numeros)

# Converter o resultado para uma lista e imprimir
print(list(pares))

# Função filter() com lambda
numeros = [10, 11, 12, 13, 14, 15, 16]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)
print()

# Função reduce()
# reduce(função, iterável, valor_inicial)

# Nota: Em Python 3, reduce() está disponível no módulo functools.
from functools import reduce

def soma(a, b):
    return a + b

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usar reduce() para somar todos os elementos da lista
total = reduce(soma, numeros)
print(total)

# Função reduce() com lambda
numeros = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numeros, 50)
print(total)