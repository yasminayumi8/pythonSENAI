print("Menu principal:")
print("")
print("Bem vindo ao programa de calculadora de ohn")
print("")
calculo = int(input("Digite qual medida deseja calcular: \n [1] Resistência Elétrica \n [2] Tensão Elétrica"
                    " \n [3] Corrente elétrica \n [4] Resistência necessária para um resistor "))
print("")
while calculo != 0:
    if calculo >= 1 and calculo <= 4:
        if calculo == 1:
            while True:
                try:
                    v = float(input("Digite o valor da Tensão em volts: "))
                    if v > 0:
                        break
                except ValueError:
                    print("valor invalido , digite um numero utilizado exem : 1.0")

            while True:
                try:
                    R = float(input("Digite o valor do resitor em ohms: "))
                    if R > 0:
                        break
                except ValueError:
                    print("valor invalido , digite um numero utilizado exem : 1.0")

            calculo1 = v / R
            print("o valor da Corrente eletrica é", calculo1)

        elif calculo == 2:
            while True:
                try:
                    I = float(input("Qual o valor da corrente eletrica em amperes?:"))
                    if I > 0:
                        break
                except ValueError:
                    print("valor invalido , digite um numero utilizado exem : 1.0")

            while True:
                try:
                    R = float(input("Digite o valor do resistor em ohms: "))
                    if R > 0:
                        break
                except ValueError:
                    print("valor invalido , digite um numero utilizado exem : 1.0")

            calculo2 = R * I
            print("o valor da Tensão Elétrica é : ", calculo2)

        elif calculo == 3:
            while True:
                try:
                    v = float(input("Qual o valor da tensão volts ?:"))
                    if v > 0:
                        break
                except ValueError:
                    print("valor invalido , digite um numero utilizado exem : 1.0")

            while True:
                try:
                    R = float(input("Digite o valor do resistor em ohms: "))
                    if R > 0:
                        break
                except ValueError:
                    print("valor invalido , digite um numero utilizado exem : 1.0")

            calculo3 = R / v
            print("o valor da Corrente elétrica é: ", calculo3)

        elif calculo == 4:
            while True:
                try:
                    fonte = float(input("Qual o fonte do resistor em ohms ?: "))
                    if fonte > 0:
                        break
                except ValueError:
                    print("valor invalido , digite um numero utilizado exem : 1.0")

            while True:
                try:
                    led = float(input("Digite o valor da tensão do LED: "))
                    if led > 0:
                        break
                except ValueError:
                    print("valor invalido , digite um numero utilizado exem : 1.0")

            while True:
                try:
                    corrente = float(input("Digite o valor do corrente eltrica em amperes: "))
                    if corrente > 0:
                        break
                except ValueError:
                    print("valor invalido , digite um numero utilizado exem : 1.0")

            calculo4 = fonte - led
            calculo5 = corrente / calculo4
            print("o valor da Resistência necessária para um resistor é : ", calculo5)

        while True:
            try:
                calculo = int(
                    input("Digite qual medida deseja calcular: \n [1] Resistência Elétrica \n [2] Tensão Elétrica"
                          " \n [3] Corrente elétrica \n [4] Resistência necessária para um resistor ")
                )
                if calculo > 0:
                    break
            except ValueError:
                print("valor invalido , digite um numero utilizado exem : 1.0")

    else:
        print("invalido")

print("OBJETIVO FINALIZADO")
