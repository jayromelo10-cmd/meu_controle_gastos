# importar SQLite
import sqlite3 as lite

# criando conexão
conec = lite.connect("dados.db")

# criando tabela de categoria
with conec:
    cur = conec.cursor()
    cur.execute("""
CREATE TABLE IF NOT EXISTS Categoria(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
)
""")


# CRIANDO TABELA DE RECEITA
with conec:
    cur = conec.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")


# CRIANDO TABELA DE GASTOS
with conec:
    cur = conec.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")


# criando tabela barra_valores
with conec:
    cur = conec.cursor()

    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(cur.fetchall())



conec.commit()
conec.close()
print("Tabelas criadas com sucesso!")