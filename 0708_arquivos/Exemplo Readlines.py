with open("c:/Users/Aluno/Desktop/Logica_Python/0708_arquivos/exemplo.txt", "r") as f:
    linhas= f.readlines()
    for linha in linhas:
        print(linha.strip())