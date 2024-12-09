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

conexao = conectar()