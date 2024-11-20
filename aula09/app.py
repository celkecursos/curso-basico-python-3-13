# A função input() é usada para capturar dados fornecidos pelo usuário.
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# A função print() exibe mensagens ou dados no console.
print(f"Olá, {nome}! Você tem {idade} anos.")
print()

# Capturar os dados do usuário
nome = input("Qual é o seu nome? ")
altura = float(input("Qual é a sua altura em metros (Ex: 1.81)? "))
peso = float(input("Qual é o seu peso e kg? "))

# Calcular o IMC
imc = peso / (altura ** 2)

# Mostrar resultado
print(f"Olá, {nome}. Seu IMC é {imc:.2f}.")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Você está com peso normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")