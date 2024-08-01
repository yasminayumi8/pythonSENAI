def faca_escolha():
    while True:
        try:
            escolha = int(input("[1]se deseja ver a temperatura em fahrenheit \n[2]se deseja ver a temperatura em Kelvins \n[3] se deseja sair do programa \n "))
            if escolha > 3 and escolha < 1:
                print("escolha apenas entre 1 a 3")
            else:
                return escolha
        except ValueError:
            print("digite apenas numeros. Ex:[1]")


def temperatura():
    while True:
        try:
            temperatura = float(input("Digite qual a temperatura em graus Celsius \n "))
            return temperatura
        except ValueError:
            print("digite apenas numeros. Ex 22.5")


print("seja bem vindo ao programa de ver temperatura em Fahrenheit e Kelvin")

while True:
    opcao = faca_escolha()

    if opcao == 2:
        kelvin = temperatura() + 273
        print("A temperatura em kelvins é de :", kelvin)
    elif opcao == 1:
        fahrenheit = temperatura() * 1.8 + 32
        print("A temperatura em fahrenheit é de :",fahrenheit)
        print("")
    else:
        print("Voce saiu do programa")
        break




