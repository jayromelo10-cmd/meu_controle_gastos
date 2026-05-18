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
cor11 = "#b2c1d1" # azul claro

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

frame_esquerdo = Frame(janela, width=1043, height=361, bg=cor06, pady=20, relief="raised")
frame_esquerdo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_direito = Frame(janela, width=1043, height=300, bg=cor06, relief="flat")
frame_direito.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)


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
    nome_01 = Label(frame_esquerdo, text="Porcentatagem da Receita de gastos", height=1, anchor=NW, font=("verdana 12"), bg=cor06, fg=cor04)
    nome_01.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("black.Horizontal.TProgressbar", background=cor08)

    bar = Progressbar(frame_esquerdo, length=180, style="black.Horizontal.TProgressbar")
    bar.place(x=10, y=35)
    bar["value"] = 50

    valor = 50
    
    porcentagem01 = Label(frame_esquerdo, text="{:,.2f}%" .format(valor), anchor=NW, font=("verdana 12"), bg=cor06, fg=cor04)
    porcentagem01.place(x=200, y=35)


# função para gráfico bars-----------------------------------------------------
def grafico_barra():
    lista_categorias = ["Renda", "Despesas", "Saldo"]
    lista_valores = [4000, 3200, 800]

    #faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    #ax.autoscale(enable=True, axis='both', tight=None)

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




porcentagem()
grafico_barra()

janela.mainloop()