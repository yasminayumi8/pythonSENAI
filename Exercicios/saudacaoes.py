import datetime
print("seja bem vindo ao programa de ver as horas")

def faca_escolha():
    while True:
        try:
            escolha = int(input("[1]se deseja ver a horas \n[2]se deseja sair do programa \n "))
            if escolha > 2 and escolha < 1:
                print("escolha apenas de 1 a 2")
            else:
                return escolha
        except ValueError:
            print("digite apenas numeros. Ex:[1]")
def solicite_nome():
    while True:
        try:
            nome = input("Digite o seu nome:")
            return nome
        except ValueError:
            print("digite apenas palavras. Ex:Yasmin")

if faca_escolha() == 1:
    tempo = datetime.datetime.now()
    print(f'|Hora: {tempo.hour} |Minuto: {tempo.minute} |Segundos: {tempo.second}')
    if tempo.hour >=5 and tempo.hour <12:
        print(f"Bom dia ,{solicite_nome()}")
    elif tempo.hour >=12 and tempo.hour <18:
        print(f"Boa tarde,{solicite_nome()}")
    elif tempo.hour >=18 and tempo.hour <00:
        print(f"Boa noite,{solicite_nome()}")
    elif tempo.hour >=1 and tempo.hour <4:
        print(f"Boa Madrugada,{solicite_nome()}")
    print("")
    print(faca_escolha())

else:
    print("voce saiu do programa")