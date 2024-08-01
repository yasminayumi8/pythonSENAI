print("Jogo adivinhação")
print("")
print("MENU:")
print("")
print("Seja Bem Vindo ao Jogo de adivinhação")
print("")
escolha = int(input("Escolha um numero entre 1 a 100: "))
print("")

import random
numero_secreto = random.randint(1, 100)

while escolha != 0:
    if escolha == numero_secreto:
        while True:
            try:
                print("Você acertou o numero misterioso !!!")
                print("")
                continuar = input("digite sim se vc gostaria de jogar novamente ou não se deseja sair : ")
                if continuar == "sim" or continuar == "nao":
                    break
                print("digite apenas sim ou não")
            except ValueError:
                print("digite apenas sim ou não")
        if continuar == "sim":
            escolha = int(input("Escolha um numero entre 1 a 100: "))
        elif continuar == "nao":
            break

    elif escolha > 100:
        while True:
            try:
                print("digite apenas um numero entre 1 a 100: ")
                break
            except ValueError:
                print("numero invalido")
        escolha = int(input("Escolha um numero entre 1 a 100: "))


    elif escolha > numero_secreto:
        while True:
            try:
                print("O numero escolhido é maior que o misterioso")
                if escolha >= 1 and escolha <= 100:
                    break
            except ValueError:
                print("valor invalido , digite um numero utilizado exemplo : 1")
        escolha = int(input("Escolha um numero entre 1 a 100: "))
        print("")
    elif escolha < numero_secreto:
        while True:
            try:
                print("O numero escolhido é menor que o misterioso")
                if escolha >= 1 and escolha <= 100:
                    break
            except ValueError:
                print("valor invalido , digite um numero utilizado exemplo : 1")
        escolha = int(input("Escolha um numero entre 1 a 100: "))
        print("")
    else:
        print("invalido")