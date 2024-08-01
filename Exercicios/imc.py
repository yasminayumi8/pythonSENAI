def peso():
    while True:
        try:
            insira = float(input("Digite o seu peso em KG: "))
            return insira
        except ValueError:
            print("digite aepnas valores inteiros")

def altura():
    while True:
        try:
            insira2 = float(input("Digite sua altura em metros: "))
            return insira2
        except ValueError:
            print("digite aepnas valores inteiros")

def imc():
    altura_ = altura()
    peso_ = peso()
    conta1 = altura_ * altura_
    conta2 = peso_ / conta1
    return conta2

calculo = imc()

classificacao = ("")


if calculo >= 17 and calculo <= 18:
  print("Seu IMC está na categoria abaixo do peso: ")
  print("seu imc é",calculo)

elif calculo >= 18.5 and calculo <= 24:
  print("Seu IMC está na categoria peso normal: ")
  print("seu imc é",calculo)

elif calculo >= 25 and calculo <= 29.9:
  print("Seu IMC está na categoria sobrepesso: ")
  print(classificacao,(int(calculo)))

elif calculo >= 30 and calculo <=40:
  print("Seu IMC está na categoria obesidade: ")
  print("seu imc é", calculo)

else:
  print("Não tem correspondência de acordo com as informações inseridas")
