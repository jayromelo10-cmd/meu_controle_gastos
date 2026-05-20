# criando interface main = main siguinifica principal.
from tkinter import *
from tkinter import Tk, ttk

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

# criando frames para diversão da tela
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
app_img = app_img.resize((55,45))
app_img = ImageTk.PhotoImage(app_img) # praparada a imagem para ser usada

# app logo = rôtulo(frame cima, igm dentro frame, texto"Meu controle de gastos", larg=900, conp p/esquerda, padx5, stilo=raised,                                     borda=cor04, cor-letra=cor09)
App_logo = Label(frame_em_cima, image=app_img, text="Meu Controle de Gastos", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=("verdana 20 bold"), bg=cor02, fg=cor04,)
App_logo.place(x=0, y=0)


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

    lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]  # cada lista terá 4 valores
    
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
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)





mostrar_renda()
janela.mainloop()