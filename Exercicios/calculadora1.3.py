def faca_escolha():
    while True:
        try:
            escolha = int(input("[1]divisão \n[2]multiplicação \n[3] subtração \n[4] adição \n[5] todos \n[6] sair do programa\n "))
            if escolha > 6 and escolha < 1:
                print("escolha apenas entre 1 a 6")
            return escolha
        except ValueError:
            print("digite apenas numeros. Ex:[1]")
def primeiro_numero():
    while True:
        try:
            numero1 = float(input("digite o valor do primeiro numero: "))
            return numero1
        except ValueError:
            print("digite apenas numeros. Ex:14")

def segundo_numero():
    while True:
        try:
            numero2 = float(input("digite o valor do segundo numero: "))
            return numero2
        except ValueError:
            print("digite apenas numeros. Ex: 22.5")


def adicao():
    conta = numero1 + numero2
    return conta
def subtracao():
    conta2 = numero1 - numero2
    return conta2
def multiplicacao():
    conta3 = numero1 * numero2
    return conta3
def divisao():
    conta4 = numero1 / numero2
    return conta4

def todos():
    conta = numero1 + numero2
    conta2 = numero1 - numero2
    conta3 = numero1 * numero2
    conta4 = numero1 / numero2
    return conta, conta2, conta3, conta4


print("seja bem vindo ao programa Calculadora Basica")
numero1 = primeiro_numero()
numero2 = segundo_numero()
opcao = faca_escolha()



if opcao == 1:
    print("O resultado da divisao é",divisao())
elif opcao == 2:
    print("O resultado da multiplicação é",multiplicacao())
elif opcao == 3:
    print("O resultado da subtração é",subtracao())
elif opcao == 4:
    print("O resultado da adição é",adicao())
elif opcao == 5:
    print("O resultado de todos é",todos())
else:
    print("sair do programa")






