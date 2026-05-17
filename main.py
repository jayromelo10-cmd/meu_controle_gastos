# criando interface main = main siguinifica principal.
from tkinter import *
from tkinter import Tk, ttk

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

# criando janela
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






janela.mainloop()