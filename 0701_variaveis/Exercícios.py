tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro():
    print("\nTabuleiro:\n")
    for i in range(3):
        print(" | ".join(tabuleiro[i]))
        if i < 2:
            print("-" * 9)
    print()

def verificar_vitoria(tabuleiro, jogador):
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

def verificar_empate(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                return False
    return True


jogador = "X"

while True:
    mostrar_tabuleiro()

    linha = int(input("Linha (0-2): "))
    coluna = int(input("Coluna (0-2): "))

    # valida posição
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print("Posição inválida!")
        continue

    # verifica ocupação
    if tabuleiro[linha][coluna] != " ":
        print("Posição ocupada!")
        continue

    # faz jogada
    tabuleiro[linha][coluna] = jogador

    # verifica vitória
    if verificar_vitoria(tabuleiro, jogador):
        mostrar_tabuleiro()
        print(f"Jogador {jogador} venceu!")
        break

    # verifica empate
    if verificar_empate(tabuleiro):
        mostrar_tabuleiro()
        print("Empate!")
        break

    # troca jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"