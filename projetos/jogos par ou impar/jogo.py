print("Jogo PAR OU IMPAR")
print("")
print("MENU:")
print("")
print("Seja Bem Vindo ao jogo de  Par ou Impar")
print("")
while True:
    try:
        escolha = input("Voce deseja ser par ou impar? : ")
        if escolha == "par" or escolha == "impar":
            break
        print("digite apenas impar ou par")
    except ValueError:
        print("erro, digite apenas par ou impar")
print("")
while True:
    try:
        numero = int(input("Escolha um numero de 1 a 5: "))
        if numero >0 and numero <= 5:
            break
    except ValueError:
        print("digite um numero entre 1 e 5 exemp:3")
import random
numero_secreto = random.randint(1, 5)
resultado = numero_secreto

conta = numero_secreto + numero
par_impar = conta % 2

print("o numero escolhido pelo computador foi :", resultado)
print("")
print("a soma dos dois numeros escolhidos :",conta)

while True:

    if par_impar == 0:
        while True:
            if escolha == "par":
                print("voce ganhou")
            else:
                print("voce perdeu")

            break

    elif par_impar != 0:
         while True:
            if escolha != "impar":
                print("Voce ganhou ")
            else:
                print("Voce perdeu")
            break

    print("")
    while True:
        try:
            continuar = input("Deseja continuar? [sim/não] :")
            if continuar == "sim" or continuar == "nao":
                break
            print("digite apenas sim ou não")
        except ValueError:
            print("digite apenas sim ou não")
    if continuar == "sim":
        numero_secreto = random.randint(1, 5)
        print("")
    elif continuar == "nao":
            break


    while True:
        try:
            escolha = input("Voce deseja ser par ou impar? : ")
            if escolha == "par" or escolha == "impar":
                break
            print("digite apenas impar ou par")
        except ValueError:
            print("digite apenas par ou impar")
    while True:
        try:
            numero = int(input("Escolha um numero de 1 a 5: "))
            if numero >0 and numero <= 5:
                break
        except ValueError:
            print("digite um numero entre 1 e 5 exemp:3")
    print("o numero escolhido pelo computador foi :", resultado)
    print("")
    print("a soma dos dois numeros escolhidos :", conta)




