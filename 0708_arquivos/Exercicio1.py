nomes=[]
for i in range(4):
    nome=input("Digite algum nome: ")
    nomes.append(nome)
with open ("nomes.txt", "w", encoding="utf-8") as f:
    for nome in nomes:
        f.write(nome+"\n")
