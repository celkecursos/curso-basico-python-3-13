import mysql.connector
from mysql.connector import Error

def conectar():
    """Estabelece conecão com o banco de dados"""
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456A#",
            database="celke"
        )
        if conexao.is_connected():
            print("Conexão realizada com sucesso!")
            return conexao
    except Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None
    
# Cadsatra no banco de dados
def cadastrar(conexao, name, email):
    """Criar um novo registro no banco de dados."""
    try:
        cursor = conexao.cursor()
        query = "INSERT INTO users (name, email) VALUE (%s, %s)"
        valores = (name, email)
        cursor.execute(query, valores)
        conexao.commit()
        print("Usuário cadastrado com sucesso!")
        return None
    except Error as e:
        print("Usuário não cadastrado:", e)

# Listar os registro do BD
def listar(conexao):
    """Ler todos os registro do banco de dados"""
    try:
        cursor = conexao.cursor()
        query = "SELECT id, name, email FROM users"
        cursor.execute(query)
        resultados = cursor.fetchall()
        for registro in resultados:
            print(registro)
    except Error as e:
        print("Erro ao listar os usuário:", e)

# Visualizar detalhes de um registro
def visualizar(conexao, id):
    """Visualizar o registro do banco de dados."""
    try:
        cursor = conexao.cursor()
        query = "SELECT id, name, email FROM users WHERE id = %s LIMIT 1"
        valores = (int(id),)
        cursor.execute(query, valores)
        resultado = cursor.fetchone()
        if resultado:
            print("Registro encontrado:", resultado)
        else:
            print("Nenhum registro encontrado com o ID informado.")
    except Error as e:
        print("Erro ao consultar o registro:", e)

# Atualizar o registro no banco de dados
def editar(conexao, id, name, email):
    """Atualiza um usuário no banco de dados."""
    try:
        cursor = conexao.cursor()
        query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
        valores = (name, email, id)
        cursor.execute(query, valores)
        conexao.commit()
        print("Usuario editado com sucesso!")
    except Error as e:
        print("Erro ao editar o usuário:", e)

# Apagar o registro no banco de dados
def deletar(conexao, id):
    """Exclui um usuário do banco de dados."""
    try:
        cursor = conexao.cursor()
        query = "DELETE FROM users WHERE id = %s"
        valores = (int(id),)
        cursor.execute(query, valores)
        conexao.commit()
        print("Usuário excluído com sucesso!")
    except Error as e:
        print("Erro ao excluir o usuário:", e)

# Chamar a função com a conexão com banco de dados
conexao = conectar()

# Verificar se a possui a conexão com banco de dados
if conexao:
    # Cadastra um novo registro
    print("Cadastrar o registro:")
    cadastrar(conexao, "Cesar", "cesar@celke.com.br")
    cadastrar(conexao, "Kelly", "kelly@celke.com.br")
    cadastrar(conexao, "Jessica", "jessica@celke.com.br")
    cadastrar(conexao, "Gabrielly", "gabrielly@celke.com.br")
    cadastrar(conexao, "Teste", "teste@celke.com.br")
    print()

    # Ler os registros
    print("Listar os registros")
    listar(conexao)

    # Visualizar o registro
    print("Visualizar o registro")
    visualizar(conexao, 1)
    print()

    # Editar o registro
    print("Editar o registro:")
    editar(conexao, 3, "Ana", "ana@celke.com.br")
    print()

    # Apagar o registro
    print("Apagar o registro:")
    deletar(conexao, 3)
    print()
