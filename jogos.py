
import learningPython.adivinhacao as adivinhacao
import learningPython.forca as forca

print("*************************")
print("Escolha o Jogo")
print("*************************")

print("(1)Adivinhação (2)Forca")

jogo = int(input("Escolha o Jogo: "))

if(jogo == 1):
    print("Jogando Adivinhação")
    adivinhacao.jogar()
elif(jogo == 2):
    print("Jogando Forca")
    forca.jogar()