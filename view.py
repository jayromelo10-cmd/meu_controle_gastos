# importar SQLite
import sqlite3 as lite
import sqlite3

# FUNÇÕES PARA INSERÇÕES------------------------------------------------------

# criando conexão
conec = lite.connect("dados.db")
conec = sqlite3.connect('dados.db')
cur = conec.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS Receitas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT,
        data TEXT,
        valor REAL
    )
''')
conec.commit()

# função para dados de tabela
def tabela():
    gastos = ver_gastos()
    receitas = ver_receitas()

    tabela_lista = []

    for i in gastos:
        tabela_lista.append(i)

    return tabela_lista


# função para dados do gráfico de barra
def barra_valores():

    lista_itens = []

    with conec:
        cur = conec.cursor()
        cur.execute("SELECT * FROM barra_valores")

        linha = cur.fetchall()

        for i in linha:
            lista_itens.append(i)

    return lista_itens



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

# ver categoria
def ver_categoria():
    lista_itens = []

    with conec:
        cur = conec.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for i in linha:
            lista_itens.append(i)

    return lista_itens


# ver receitas
def ver_receitas():
    lista_itens = []

    with conec:
        cur = conec.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for i in linha:
            lista_itens.append(i)
    
    return lista_itens


# ver gastos
def ver_gastos():
    lista_itens = []

    with conec:
        cur = conec.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for i in linha:
            lista_itens.append(i)
    
    return lista_itens

    