tabuleiro = [[" " for _ in range(3)] for _ in range(3)]         #Cria uma matriz 3x3 em branco, para representar o tabuleiro só q em branco.

def mostrar_tabuleiro():                                        #Exibe o tabuleiro na tela de forma organizada, separando as colunas com | e as linhas com traços (-------
    print("\nTabuleiro:\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("-" * 9)
    print()

def verificar_vitoria(tabuleiro, jogador):                       #Função para verificar se o jogador venceu.
    # linhas
    for i in range(3):
        if (tabuleiro[i][0] == jogador and
            tabuleiro[i][1] == jogador and
            tabuleiro[i][2] == jogador):
            return True

    # colunas
    for i in range(3):
        if (tabuleiro[0][i] == jogador and
            tabuleiro[1][i] == jogador and
            tabuleiro[2][i] == jogador):
            return True

    # diagonal principal
    if (tabuleiro[0][0] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][2] == jogador):
        return True

    # diagonal secundária
    if (tabuleiro[0][2] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][0] == jogador):
        return True

    return False

def verificar_empate(tabuleiro):                            #Função para verificar se deu velha/empate
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                return False
    return True


jogador = "X"                                               #Definir o jogador X

while True:
    mostrar_tabuleiro()

    linha = int(input("Linha (0-2): "))
    coluna = int(input("Coluna (0-2): "))

    # valida posição
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:              #Verificar se a posição for invalida, como um número menor que 0 ou maior que 2.
        print("Posição inválida!")
        continue

    # verifica ocupação
    if tabuleiro[linha][coluna] != " ":                                 #Verificar se já existe um valor naquela posição.
        print("Posição ocupada!")
        continue

    # faz jogada
    tabuleiro[linha][coluna] = jogador                                  #Para executar a jogada

    # verifica vitória
    if verificar_vitoria(tabuleiro, jogador):                           # Verifica a vitória, e se vencer, exibir uma mensagem.
        mostrar_tabuleiro()
        print(f"Jogador {jogador} venceu!")
        break

    # verifica empate                                                   #Verifica se deu empate, caso dê, exibe uma mensagem.
    if verificar_empate(tabuleiro):
        mostrar_tabuleiro()
        print("Empate!")
        break

    # troca jogador                                                     # Troca de jogador, Começando com o X, e depois o O
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"