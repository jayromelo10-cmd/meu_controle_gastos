# importar SQLite
import sqlite3 as lite

# FUNÇÕES PARA INSERÇÕES------------------------------------------------------

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


# FUNÇÕES PARA DELETAR----------------------------------------------------------

#Deletar Receitas
def deletar_receitas(i):
    with conec:
        cur = conec.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)


#Deletar Gastos
def deletar_Gastos(i):
    with conec:
        cur = conec.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, i)


# FUNÇÕES PARA VER DADOS--------------------------------------------------------
def ver_categoria():
    lista_itens = []

    with conec:
        cur = conec.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for i in linha:
            lista_itens.append(i)
    print(ver_categoria())
    
    return lista_itens

    