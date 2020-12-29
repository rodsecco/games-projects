import adivinhacao
import forca

def escolher_jogo():
    print("************************************")
    print("***Vamos jogar: Escolha seu jogo!***")
    print("************************************")

    print("(1) Acerte o número (2) Forca")

    choosen_game = int(input("Qual jogo? R:"))

    if(choosen_game == 1):
        print("Jogando - Acerte o número")
        adivinhacao.jogar()
    elif(choosen_game == 2):
        print("Jogando - Forca")
        forca.jogar()
    else:
        print("Escolha um jogo existente!")

if(__name__ == "__main__"):
    escolher_jogo()