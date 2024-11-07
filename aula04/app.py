# Estruturas de Decisão (if, elif, else)

nota = 60

if nota >= 90:
    print("Nota: A")
elif nota >= 80:
    print("Nota: B")
elif nota >= 70:
    print("Nota: C")
else:
    print("Nota: D")

# Estruturas de Repetição
# Exemplo de for Loop

frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

# Exemplo de while Loop

contador = 1

while contador <= 5:
    print("Convidado:", contador)
    contador += 1

# Comandos de Controle de Fluxo

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exemplo de break
for numero in numeros:
    if numero == 7:
        print("Número 7 encontrado! Interrompendo o loop")
        break
    print(numero)

# Exemplo de continue
for numero in range(1, 10):
    if numero % 2 == 0: 
        continue # Pula a interação para números pares
    print("Número ímpar:", numero)

# Exemplo de pass
for numero in range(1, 5):
    if numero == 3:
        pass
    else:
        print("Número:", numero)
