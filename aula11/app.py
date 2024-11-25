# Importar a biblioteca csv, módulo que fornece funcionalidades para trabalhar com arquivos CSV.
import csv

try:
    # Abrir o arquivo CSV no modo "w". Abre o arquivo para escrita. Se o arquivo não existir, ele será criado. Se o arquivo já existir, ele será sobrescrito (o conteúdo anterior será apagado).
    with open("dados.csv", "w", newline="", encoding="utf-8") as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerow(["Nome", "Idade", "Cidade"])
        escrever.writerow(["Cesar", 18, "Curitiba"])

    # Abrir o arquivo CSV no modo "a". Abre o arquivo para acrescentar conteúdo no final do arquivo. Se o arquivo não existir, ele será criado.
    with open("dados.csv", "a", newline="", encoding="utf-8") as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerow(["Kelly", 19, "Cuiabá"])
        escrever.writerows([["Jessica", 20, "Manaus"],["Gabrielly", 21, "São Paulo"]])

    # Abrir o arquivo no modo "r". Abre o arquivo para leitura. O arquivo deve existir. Se o arquivo não existir, ocorrerá um erro.
    with open("dados.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)

except Exception as e:
    print(f"Ocorreu um erro insperado: {e}")

# Modo - Descrição
# 'r' - Leitura (somente leitura).
# 'w' - Escrita (sobrescreve).
# 'a' - Adição (acrescenta no final).
# 'x' - Criação exclusiva (falha se o arquivo existir).
# 'b' - Binário (não muito comum para CSV).
# 't' - Texto (padrão para CSV).
# 'r+' - Leitura e escrita (não apaga o conteúdo).
# 'w+' - Leitura e escrita (sobrescreve o conteúdo).
# 'a+' - Leitura e adição (acrescenta no final).
# 'x+' - Criação exclusiva e leitura.