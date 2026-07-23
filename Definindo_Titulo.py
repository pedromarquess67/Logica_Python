#Definindo o título

import tkinter as tk
root= tk.Tk()
root.title("SENAI- Desenvolvimento de Sistemas")

#ler o titulo da janela
title=root.title()

#Cria um rótulo (label) com o título da janela
message= tk.Label (root, text=title)

#Posiciona o rótulo na anela
message.pack()

#Define o tamanho da janela( largua x altura + posição x + posição y)
root.geometry("400x200+50+250")

root.mainloop()