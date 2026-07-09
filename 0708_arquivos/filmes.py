def quantidade_filmes():
    print("1 - Quantidade total de filmes ")
    print("2 - Informações de um filme pelo título ")
    print("3 - Filmes de um diretor específico ")
    print("4 - Filmes de um gênero específico ")
    print("5 - Média de duração dos filmes ") 
    print("6 - Sair ")
quantidade_filmes()
while True:
    opcao=(input("Digite a opção"))
    if opcao=="1":
        print("contar_filmes")
    elif opcao=="2":
        print("info_por_titulo")
    elif opcao == "3":
        print("filmes_por_diretor")
    elif opcao== "4":
        print("filmes_por_genero")
    elif opcao=="5":
        print("media_duracao")
    elif opcao=="6":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente")
