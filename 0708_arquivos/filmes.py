def menu():
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")


def contar_filmes():
    contador = 0

    with open("filmes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.strip().startswith("Título"):
                contador += 1

    print(f"Quantidade de filmes: {contador}")


def info_titulo():
    titulo_procurado = input("Digite o título do filme: ")

    with open("filmes.txt", "r", encoding="utf-8") as arq:
        while True:
            linha_titulo = arq.readline()

            if linha_titulo == "":
                break

            ano = arq.readline()
            diretor = arq.readline()
            genero = arq.readline()
            duracao = arq.readline()

            titulo_arquivo = linha_titulo.split(":")[1].strip()

            if titulo_arquivo == titulo_procurado:
                filme = {
                    "Título": titulo_arquivo,
                    "Ano": ano.split(":")[1].strip(),
                    "Diretor": diretor.split(":")[1].strip(),
                    "Gênero": genero.split(":")[1].strip(),
                    "Duração": duracao.split(":")[1].strip()
                }

                for chave, valor in filme.items():
                    print(f"{chave}: {valor}")

                break

        else:
            print("Filme não encontrado.")


def por_diretor():
    diretor_procurado = input("Digite o diretor do filme: ")

    encontrou = False

    with open("filmes.txt", "r", encoding="utf-8") as arq:
        while True:
            linha_titulo = arq.readline()

            if linha_titulo == "":
                break

            if linha_titulo.strip() == "":
                continue

            ano = arq.readline()
            linha_diretor = arq.readline()
            genero = arq.readline()
            duracao = arq.readline()

            titulo = linha_titulo.split(":")[1].strip()
            diretor = linha_diretor.split(":")[1].strip()

            if diretor == diretor_procurado:
                encontrou = True

                filme = {
                    "Título": titulo,
                    "Ano": ano.split(":")[1].strip(),
                    "Diretor": diretor,
                    "Gênero": genero.split(":")[1].strip(),
                    "Duração": duracao.split(":")[1].strip()
                }

                for chave, valor in filme.items():
                    print(f"{chave}: {valor}")

                print()

    if encontrou == False:
        print("Diretor não encontrado.")

menu()

while True:
    opcao = input("Digite a opção: ")

    if opcao == "1":
        contar_filmes()

    elif opcao == "2":
        info_titulo()

    elif opcao == "3":
        por_diretor()

    elif opcao == "4":
        print("filmes_por_genero")

    elif opcao == "5":
        print("media_duracao")

    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente")