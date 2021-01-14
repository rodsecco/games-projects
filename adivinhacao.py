from random import randint

def jogar():
    print("**************************************")
    print("***Vamos jogar: Adivinhe o número!!***")
    print("**************************************")

    min_number = 1
    max_number = 100
    points = 1000

    random_number = randint(min_number, max_number)

    print("Escolha seu nível de dificuldade:")
    print("(1) Fácil (2) Médio (3) Difícil")

    dificulty = int(input("Escolha do nível: "))

    if(dificulty == 1):
        tries = 15
        print("Você terá {} tentativas".format(tries))
    elif(dificulty == 2):
        tries = 10
        print("Você terá {} tentativas".format(tries))
    elif(dificulty == 3):
        tries = 5
        print("Você terá {} tentativas".format(tries))
    else:
        print("Número não válido - nível 'Super Difícil' escolhido!")
        tries = 3
        print("Você terá {} tentativas".format(tries))

    for round in range(1, tries + 1):

        guess = input("Digite um número entre {} e {}: ".format(min_number, max_number))
        int_guess = int(guess)

        print("Você digitou o número:", int_guess)

        if(int_guess < min_number or int_guess > max_number):
            print("Você pode apenas digitar números entre {} e {}".format(min_number, max_number))
            print("Você tem mais {} tentativas!".format(remaining_tries), sep=" ")
            continue

        acertou = int_guess == random_number
        maior = int_guess > random_number
        menor = int_guess < random_number

        if (acertou):
            print("Parabéns, você acertou!", "-> Número secreto: {}".format(random_number), end="\n")
            print("Fim de jogo! Pontuação final: {} pts".format(points), end="\n")
            break
        else:
            if(menor):
                print("Resposta errada, o número digitado é menor que o número secreto!")
            elif(maior):
                print("Resposta errada, o número digitado é maior que o número secreto!")
            lost_points = abs(random_number - int_guess)
            points = points - lost_points

            remaining_tries = tries - round
            print("Você tem mais {} tentativas!".format(remaining_tries), sep=" ")
    else:
        print("Você perdeu, o número era: {}!".format(random_number))
        print("Fim de jogo! Pontuação final: {} pts".format(points), end="\n")

if(__name__ == "__main__"):
    jogar()