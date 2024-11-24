try:
    numero = int(input("Digite um número: "))
    print(f"Você digitou o número: {numero}")
    resultado = 10 / numero
    print("Resultado da divisão:", resultado)
# except Exception as e:
#     print(f"Ocorreu erro: {e}")
except ValueError:
    print("Você não digitou um número válido.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except:
    print("Digite um número válido.")
finally:
    print("Sempre será executado, independente de sucesso ou erro.")