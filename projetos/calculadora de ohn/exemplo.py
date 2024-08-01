print("bem vindo ao calculadora de ohn")
print("")
print("[0] sair do programa")
print("[1]resistencia")
print("[2]tensao")
print("[3] corrente")
print("[4] resistencia necessaria")
print("")
opcao = int(input("digite a opcao: "))

while opcao != 0:

    if opcao == 1:
        print("resistencia")
        print("")
        while True:
            try:
                tensao = float(input("digite a tensao: "))
                if tensao > 0:
                    break
            except ValueError:
                print("valor invalido , digite um numero utilizado exem : 1.0")

        while True:
            try:
                corrente = float(input("digite a corrente em ampares "))
                if corrente > 0:
                    break
            except ValueError:
                print("valor invalido , digite um numero utilizado exem : 1.0")

        resistencia = tensao / corrente

        print("a resistencia em ampares ", resistencia)

    elif opcao == 2:
        print("tensao")
        print("")
        while True:
            try:
                resistencia= float(input("digite a resistencia : "))
                if corrente > 0:
                    break
            except ValueError:
                print("valor invalido , digite um numero utilizado exem : 1.0")

        while True:
            try:
                corrente = float(input("digite a corrente em ampares "))
                if corrente > 0:
                    break
            except ValueError:
                print("valor invalido , digite um numero utilizado exem : 1.0")

        tensao = resistencia * corrente

        print("a tensão é de ", tensao)

    elif opcao == 3:
        print("corrente")
        print("")
        while True:
            try:
                tensao = float(input("digite a tensao em volts: "))
                if corrente > 0:
                    break
            except ValueError:
                print("valor invalido , digite um numero utilizado exem : 1.0")

        while True:
            try:
                resistencia = float(input("digite a corrente em ohms: "))
                if corrente > 0:
                    break

            except ValueError:
                print("valor invalido , digite um numero utilizado exem : 1.0")

        corrente = resistencia / tensao
        print("a corrente é de ", corrente)

    elif opcao == 4:
        print("resistencia resitor")
        print("")
        while True:
            try:
                tensao = float(input("digite a tensao da fonte em volts: "))
                if corrente > 0:
                    break
            except ValueError:
                print("valor invalido , digite um numero utilizado exem : 1.0")

        while True:
            try:
                dispositivo = float(input("digite a tensao do dispositivo em volts: "))
                if corrente > 0:
                    break
            except ValueError:
                print("valor invalido , digite um numero utilizado exem : 1.0")

        while True:
            try:
                corrente = float(input("digite a corrente em ampares : "))
                if corrente > 0:
                    break
            except ValueError:
                print("valor invalido , digite um numero utilizado exem : 1.0")

        resistencia_resistor = tensao - dispositivo / corrente

        print("a adequada para a resistencia do resistor em ampares é ", resistencia_resistor)

    else:
        print("opcao invalida")

    print("")
    print("escolha outra opção")
    print("[0] sair do programa")
    print("[1]resistencia")
    print("[2]tensao")
    print("[3] corrente")
    print("[4] resistencia necessaria")
    print("")

    opcao = int(input("digite a opcao: "))