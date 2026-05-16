# importar SQLite
import sqlite3 as lite

# criando conexão
conec = lite.connect("dados.db")

#  Inserir cateoria
def inserir_categoria(i):
    with conec:
        cur = conec.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)


#  Inserir Receitas
def inserir_receita(i):
    with conec:
        cur = conec.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)


#  Inserir Gastos
def inserir_gastos(i):
    with conec:
        cur = conec.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)