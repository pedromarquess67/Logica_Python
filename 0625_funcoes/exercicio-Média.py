
def calcular_media (notas):
    media= sum(notas)/len(notas)
    return media
notas=[6,6,7,7.8]
resultado=calcular_media(notas) 
print(f"Sua média é de : {resultado}")