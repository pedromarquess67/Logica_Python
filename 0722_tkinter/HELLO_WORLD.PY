import tkinter as tk
#cria a janela principal

root= tk.Tk()

#cria um rotulo (label) com o texto "Hello, world!"

message= tk.Label (root, text= "Hello, world!")
#posiciona o rotulo na janela
message.pack()
#inicia o loop principal da interface grafica
root.mainloop()
