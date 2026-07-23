def main():
    while True:
        menu()
        opcao = input("Digite a opção: ")

        if opcao == "1":
            contar_filmes()

        elif opcao == "2":
            info_por_titulo()

        elif opcao == "3":
            filmes_por_diretor()

        elif opcao == "4":
            filmes_por_genero()

        elif opcao == "5":
            media_duracao()

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente")



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


def info_por_titulo():
    titulo_busca=input("Título: ").strip().lower()
    encontrado= False
    try:
        with open("filmes.txt", encoding="utf=8") as f:
            for linha in f:
                if linha.strip().startswith("Título:"):
                    titulo=linha.split(":", 1)[1]. strip()
                    if titulo.lower() == titulo_busca:
                        print(f"Título: {titulo}")
                        try:
                            ano=next(f).strip()
                            diretor = next(f).strip()
                            genero= next(f). strip()
                            duracao= next(f).strip()
                        except StopIteration:
                            print("Registro incompleto para esse título.")
                            return
                        print(ano)
                        print(diretor)
                        print(genero)
                        print(duracao)
                        encontrado=True
                        break
    except FileNotFoundError:
        print("Arquivo 'filmes.txt' não encontrado")
        return
    if not encontrado:
        print("Filme não encontrado")

(menu)

def filmes_por_diretor():
    diretor_busca=input("Diretor: ").strip().lower()
    contador=0
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            ultimo_titulo = ""
            for linha in f:
                s= linha.strip()
                if s.startswith("Título:"):
                    ultimo_titulo= s.split(":", 1)[1].strip()
                elif s.startswith("Diretor:"):
                    diretor= s.split(":", 1) [1].strip()
                    if diretor.lower()==diretor_busca:
                        contador+=1
                        print(f"- {ultimo_titulo}")
    except FileNotFoundError:
        print("Arquivo 'filmes.txt' não encontrado.")
        return
    print(f"Total de filmes do diretor '{diretor_busca}': {contador}")
    return contador

def filmes_por_genero():
    genero_busca=input("Gênero: ").strip().lower()
    contador=0
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            ultimo_titulo = ""
            for linha in f:
                s= linha.strip()
                if s.startswith("Título:"):
                    ultimo_titulo= s.split(":", 1)[1].strip()
                elif s.startswith("Gênero:"):
                    genero= s.split(":", 1) [1].strip()
                    if genero_busca in genero.lower():
                        contador+=1
                        print(f"- {ultimo_titulo} ({genero})")
    except FileNotFoundError:
        print("Arquivo 'filmes.txt' não encontrado.")
        return
    print(f"Total de filmes do gênero '{genero_busca}': {contador}")
    return contador

def media_duracao():
    soma= 0
    cont= 0
    try:
        with open ("filmes.txt", encoding="utf-8") as f:
            for linha in f:
                s= linha.strip()
                if s.startswith("Duração:"):
                    try:
                        minutos= int(s.split(":", 1) [1]. strip().split()[0])
                    except (ValueError, IndexError):
                        continue
                    soma +=minutos
                    cont +=1
    except FileNotFoundError:
        print("Arquivo 'filmes.txt' não encontrado.")
        return
    if cont==0:
        print("Nenhuma duração valida encontrada.")
    else:
        media = soma/cont
        print(f"Média de duração: {media:.2f} minutos")
        return media


if __name__ == "__main__":
    main()