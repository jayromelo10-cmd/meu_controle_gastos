# importar SQLite
import sqlite3 as lite

# criando conexão
conec = lite.connect("dados.db")

# criando tabela de categoria
with conec:
    cur = conec.cursor()
    cur.execute("CREATE TABLE Categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")


# CRIANDO TABELA DE RECEITA
with conec:
    cur = conec.cursor()
    cur.execute("CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")


# CRIANDO TABELA DE GASTOS
with conec:
    cur = conec.cursor()
    cur.execute("CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")


conec.commit()
conec.close()
print("Tabelas criadas com sucesso!")