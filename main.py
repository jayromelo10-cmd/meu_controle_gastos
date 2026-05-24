# criando interface main = main siguinifica principal.
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

from tkinter import Button

# importando pillow
from PIL import Image, ImageTk

# importando barra de progresso do Tlinter
from tkinter.ttk import Progressbar

# importando Marplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

#importando numpy
import numpy as np

# no terminal: pip install tkcalendar -- para instalar a biblioteca de calendário
from tkcalendar import Calendar, DateEntry
from datetime import date

# Importando funções da view
from view import inserir_categoria, inserir_gastos, inserir_receita, tabela
from view import ver_categoria


# Cores da interface
cor01 = "#fc690f" # laranja
cor02 = "#4891DA" # azul cinza
cor03 = "#004c00" # verde
cor04 = "#000000" # pretp
cor05 = "#ffffff" # branco
cor06 = "#e5e5e5" # cinza claro
cor07 = "#cc0000" # vermelho
cor08 = "#fccf47" # amarelo
cor09 = "#472b23" # marron
cor10 = "#003366" # azul escuro
cor11 = "#b2c1d1" # cinza escuro
cor12 = "#6D6B6B" # cinza

# criando janela-------------------------------------------------------------------------
janela = Tk()
janela.title()
janela.geometry("900x650")
janela.configure(background=cor06)
janela.resizable(width=FALSE, height=False)

style = ttk.Style(janela)
style.theme_use("clam")

# criando frames para divisão da tela
frame_em_cima = Frame(janela, width=1043, height=50, bg=cor11, relief="flat")
frame_em_cima.grid(row=0, column=0)

frame_esquerdo = Frame(janela, width=1043, height=361, bg=cor05, pady=20, relief="raised")
frame_esquerdo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=1043, height=300, bg=cor05, relief="flat")
frame_baixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

frame_grafico = Frame(frame_esquerdo, width=580, height=250, bg=cor05)
frame_grafico.place(x=415, y=5)

# trabalhando no frame de cima------------------------------------------------------------------------

# acessando a imagem
app_img = Image.open("log.jpg")
app_img = app_img.resize((55,35))
app_img = ImageTk.PhotoImage(app_img) # praparada a imagem para ser usada

# app logo = rôtulo(frame cima, igm dentro frame, texto"Meu controle de gastos", larg=900, conp p/esquerda, padx5, stilo=raised,                                     borda=cor04, cor-letra=cor09)
App_logo = Label(frame_em_cima, image=app_img, text="Meu Controle de Gastos", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=("verdana 20 bold"), bg=cor02, fg=cor04,)
App_logo.place(x=0, y=0)

# Definindo tree como global
global tree


# função inserir gastos
def inserir_gastos_ui():

    categoria = ecategoria.get()
    data = data.get()
    quantia = quantia.get()

    if categoria == "" or data == "" or quantia == "":
        messagebox.showerror("Erro", "Preencha todos os campos")
        return

    lista = [categoria, data, quantia]
    inserir_gastos(lista)

    messagebox.showinfo("Sucesso", "Dados salvos!")


# Função inserir categoria
def inserir_categoria_2():
    nome = ecategoria.get()
    lista_inserir = [nome]
    
    for i in lista_inserir:
        if i== "":
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
        
        # passando para a função inserir gastos presente na view
        inserir_categoria(lista_inserir)
        messagebox.showinfo("Sucesso", "os dados foram adicionados com sucesso!")

        ecategoria.delete(0, "end")

        # Pegando os valores da categoria 
        categorias = ver_categoria()
        categoria = []

        for i in categorias:
            categoria.append(i[1])

        # atualizar a lista de categorias
        combo_categoria_despesas["values"] = (categoria)


# função inserir receitas
def inserir_receitas02():

    nome = "Receita"
    data = ecal_receitas.get()
    quantia = evalor_receitas.get()

    lista_inserir = [nome, data, quantia]

    for i in lista_inserir:
        if i== "":
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
        

    # chamando a função inserir receitas  presente na view
    inserir_receita(lista_inserir)
    messagebox.showinfo("Sucesso", "os dados foram adicionados com sucesso!")

    ecal_receitas.delete(0, "end")
    evalor_receitas.delete(0, "end")


    # função inserir receitas
def inserir_receitas02():
    nome = combo_categoria_despesas.get()
    data = ecal_despesas.get()
    quantia = evalor_despesas.get()

    lista_inserir = [nome, data, quantia]

    for i in lista_inserir:
        if i== "":
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
        

    # chamando a função inserir despesas  presente na view
    inserir_gastos(lista_inserir)
    messagebox.showinfo("Sucesso", "os dados foram adicionados com sucesso!")

    combo_categoria_despesas.delete(0,"end")
    ecal_despesas.delete(0, "end")
    evalor_despesas.delete(0, "end")


    # atualizando dados
    inserir_receitas02()
    inserir_gastos()
    mostrar_renda()
    porcentagem()
    grafico_barra()
    resumos()
    grafico_pizza()


# criando espaço da porcentágem-----------------------------------------------------------
def porcentagem():
    nome_01 = Label(frame_esquerdo, text="Porcentatagem da Receita de gastos", height=1, anchor=NW, font=("verdana 12"), bg=cor05, fg=cor04)
    nome_01.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("black.Horizontal.TProgressbar", background=cor08)

    bar = Progressbar(frame_esquerdo, length=180, style="black.Horizontal.TProgressbar")
    bar.place(x=10, y=35)
    bar["value"] = 50

    valor = 50
    
    porcentagem01 = Label(frame_esquerdo, text="{:,.2f}%" .format(valor), anchor=NW, font=("verdana 11"), bg=cor05, fg=cor04)
    porcentagem01.place(x=200, y=35)


# função para gráfico bars-----------------------------------------------------
def grafico_barra():
    lista_categorias = ["Renda", "Despesas", "Saldo"]
    lista_valores = [4000, 3200, 800]

    #faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    #ax.autoscale(enable=True, axis='both', tight=None)

    colors = [cor03, cor07, cor08, cor04]

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)
    #create a list to collect the plt.patches data

    c = 0
    #set individual bar lables using above list
    for i in ax.patches:
        #get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticks(range(len(lista_categorias)))
    ax.set_xticklabels(lista_categorias,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frame_esquerdo)
    canva.get_tk_widget().place(x=10, y=70)

# função de resumos totais
def resumos():
    valor = [4000, 3200, 800]

    prim_linha = Label(frame_esquerdo, text="", width=215, height=1, anchor=NW, font=("Arial 1"), bg=cor12)
    prim_linha.place(x=309, y=50)
    total_renda = Label(frame_esquerdo, text=" Total Renda Mensal            ".upper(), anchor=NW, font=("Verdana 10"), bg=cor05, fg=cor02)
    total_renda.place(x=309, y=35)
    prim_valor = Label(frame_esquerdo, text="R$ {:,.2f}".format(valor[0]), anchor=NW, font=("Arial 17"), bg=cor05, fg=cor12)
    prim_valor.place(x=309, y=70)

    seg_linha = Label(frame_esquerdo, text="", width=215, height=1, anchor=NW, font=("Arial 1"), bg=cor12)
    seg_linha.place(x=309, y=132)
    total_renda = Label(frame_esquerdo, text=" Total Despesas Mensais       ".upper(), anchor=NW, font=("Verdana 11"), bg=cor05, fg=cor02)
    total_renda.place(x=309, y=115)
    seg_valor = Label(frame_esquerdo, text="R$ {:,.2f}".format(valor[1]), anchor=NW, font=("Arial 17"), bg=cor05, fg=cor12)
    seg_valor.place(x=309, y=150)

    terc_linha = Label(frame_esquerdo, text="", width=215, height=1, anchor=NW, font=("Arial 1"), bg=cor12)
    terc_linha.place(x=309, y=207)
    total_renda = Label(frame_esquerdo, text=" Total Saldo de Caixa          ".upper(), anchor=NW, font=("Verdana 11"), bg=cor05, fg=cor02)
    total_renda.place(x=309, y=190)
    terc_valor = Label(frame_esquerdo, text="R$ {:,.2f}".format(valor[2]), anchor=NW, font=("Arial 17"), bg=cor05, fg=cor12)
    terc_valor.place(x=309, y=220)


# FUNÇÃO GRÁFICO PYTHON
def grafico_pizza():
    
# faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']
    cores = [cor03, cor07, cor08]

# only "explode" the 2nd slice (i.e. 'Hogs')
    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=cores,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_grafico)
    canva_categoria.get_tk_widget().grid(row=0, column=0)


    #plt.show()
porcentagem()
grafico_barra()
resumos()
grafico_pizza()


# CRIANDO FRAMES DENTRO DO FRAME BAIXO---------------------------------------------------------------
frame_renda = Frame(frame_baixo, width=300, height=250, bg=cor05, relief="flat")
frame_renda.grid(row=0, column=0)

frame_operacoes = Frame(frame_baixo, width=220, height=250, bg=cor05, relief="flat")
frame_operacoes.grid(row=0, column=1, padx=5)

frame_config = Frame(frame_baixo, width=300, height=250, bg=cor05, relief="flat")
frame_config.grid(row=0, column=3, padx=5)


# Tabela renda mensal----------------------------------------------------------------------
App_tabela = Label(frame_esquerdo, text="Tabela Receitas e Despesas", anchor=NW, font=("verdana 12"), bg=cor05, fg=cor04,)
App_tabela.place(x=5, y=309)

# Função ára mostrar_renda
def mostrar_renda():

    # criando cabeçalho da tabela
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = tabela()  # cada lista terá 4 valores
    
    global tree    # função para barra de rolagem

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # para posicionar a tabela
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    # para centralizar a tabela
    hd=["center","center","center", "center"]
    h=[30,100,100,100]   # são para as largulas da tabela
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # ajustar as larguras e colunas do campo de texto
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

# configurações Despesas------------------------------------------------------
informacao_01 = Label(frame_operacoes, text="Insira Novas Despesas", height=1, anchor=NW, font="Verdana 10 bold", bg=cor05, fg=cor04)
informacao_01.place(x=10, y=10)

# categoria
categorias = Label(frame_operacoes, text="Categoria", height=1, anchor=NW, font="Ivy 10", bg=cor05, fg=cor04)
categorias.place(x=10, y=40)

# pegando categorias
sub_categoria = ver_categoria()
categoria = []

for i in sub_categoria:
    categoria.append(i[1])

combo_categoria_despesas = ttk.Combobox(frame_operacoes, width=10, font="Ivy 10")
combo_categoria_despesas["values"] = (categoria)
combo_categoria_despesas.place(x=110, y=41)

# Despesas------------------------------------------------------------------------------
cal_despesas = Label(frame_operacoes, text="Data", height=1,    anchor=NW, font=("Ivy 10"), bg=cor05, fg=cor04)
cal_despesas.place(x=10, y=70)
ecal_despesas = DateEntry(frame_operacoes, width=12, background="darkblue", foreground="white", borderwidth=2, year=2022)
ecal_despesas.place(x=110, y=71)


# Valor------------------------------------------------------------------------------
valor_despesas = Label(frame_operacoes, text="Quantia Total", height=1,    anchor=NW, font=("Ivy 10"), bg=cor05, fg=cor04)
valor_despesas.place(x=10, y=100)
evalor_despesas = Entry(frame_operacoes, width=14, justify="left", relief="solid")
evalor_despesas.place(x=110, y=101)


# Botão inserir
img_add_despesas = Image.open("adicionar.png")
img_add_despesas = img_add_despesas.resize((17,17))
img_add_despesas = ImageTk.PhotoImage(img_add_despesas) # praparada a imagem para ser usada
botao_inserir_desp = Button(frame_operacoes, command=inserir_receitas02, image=img_add_despesas, text="Adicionar".upper(), width=80, compound=LEFT, anchor=NW, font=("Ivy 7 bold"), bg=cor05, fg=cor04, overrelief=RIDGE)
botao_inserir_desp.place(x=110, y=131)


# Botão Excluir
excluir_categ = Label(frame_operacoes, text="Excluir Ação", height=1, anchor=NW, font=("Ivy 10 bold"), bg=cor05, fg=cor04)
excluir_categ.place(x=10, y=190)

img_deletar_despesas = Image.open("delete.png")
img_deletar_despesas = img_deletar_despesas.resize((17,17))
img_deletar_despesas = ImageTk.PhotoImage(img_deletar_despesas) # praparada a imagem para ser usada
botao_deletar_desp = Button(frame_operacoes, image=img_deletar_despesas, text="Deletar".upper(), width=80, compound=LEFT, anchor=NW, font=("Ivy 7 bold"), bg=cor05, fg=cor04, overrelief=RIDGE)
botao_deletar_desp.place(x=110, y=190)


# configurações Receitas----------------------------------------------------------
informacao_01 = Label(frame_config, text="Insira Novas Receitas", height=1, anchor=NW, font="Verdana 10 bold", bg=cor05, fg=cor04)
informacao_01.place(x=10, y=10)

# Calendario------------------------------------------------------------------------------
cal_receitas = Label(frame_config, text="Data", height=1,    anchor=NW, font=("Ivy 10"), bg=cor05, fg=cor04)
cal_receitas.place(x=10, y=40)
ecal_receitas = DateEntry(frame_config, width=12, background="darkblue", foreground="white", borderwidth=2, year=2022)
ecal_receitas.place(x=110, y=41)


# Valor receitas------------------------------------------------------------------------------
valor_receitas = Label(frame_config, text="Quantia Total", height=1,    anchor=NW, font=("Ivy 10"), bg=cor05, fg=cor04)
valor_receitas.place(x=10, y=70)
evalor_receitas = Entry(frame_config, width=14, justify="left", relief="solid")
evalor_receitas.place(x=110, y=70)


# Botão inserir receitas----------------------------------------------------------
img_add_receitas = Image.open("adicionar.png")
img_add_receitas = img_add_receitas.resize((17,17))
img_add_receitas = ImageTk.PhotoImage(img_add_receitas) # praparada a imagem para ser usada
botao_inserir_receitas = Button(frame_config, command=inserir_receitas02, image=img_add_receitas, text="Adicionar".upper(), width=80, compound=LEFT, anchor=NW, font=("Ivy 7 bold"), bg=cor05, fg=cor04, overrelief=RIDGE)
botao_inserir_receitas.place(x=110, y=100)


# Operações nova categoria----------------------------------------------------------
informacao_01 = Label(frame_config, text="Categoria", height=1, anchor=NW, font="Ivy 10 bold", bg=cor05, fg=cor04)
informacao_01.place(x=10, y=160)

ecategoria = Entry(frame_config, width=14, justify="left", relief="solid")
ecategoria.place(x=110, y=160)


# Botão inserir categoria----------------------------------------------------------
img_add_categoria = Image.open("adicionar.png")
img_add_categoria = img_add_categoria.resize((17,17))
img_add_categoria = ImageTk.PhotoImage(img_add_categoria) # praparada a imagem para ser usada
botao_inserir_categoria = Button(frame_config, command=inserir_categoria_2, image=img_add_categoria, text="Adicionar".upper(), width=80, compound=LEFT, anchor=NW, font=("Ivy 7 bold"), bg=cor05, fg=cor04, overrelief=RIDGE)
botao_inserir_categoria.place(x=110, y=190)





mostrar_renda() 
janela.mainloop()