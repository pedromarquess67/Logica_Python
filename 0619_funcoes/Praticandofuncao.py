comprimento=int(input("Digite o comprimento que você quer utilizar: "))
altura=int(input("Digite a altura que você quer utilizar: "))
def desenharretangulo (altura, comprimento):
    for i in range(altura):
        if i==0 or i==altura -1:
            print("+" + (comprimento-2)*"-" + "+")
        else:
            print("|" + (comprimento-2)* " "+ "|")
desenharretangulo(altura,comprimento)
desenharretangulo(6,7)