def primeiro_lado():
    while True:
        try:
            lado1 = float(input("digite o valor do primeiro lado : "))
            return lado1
        except ValueError:
            print("digite apenas numeros. Ex:14")
def segundo_lado():
    while True:
        try:
            lado2 = float(input("digite o valor do segundo lado : "))
            return lado2
        except ValueError:
            print("digite apenas numeros. Ex:14")
def terceiro_lado():
    while True:
        try:
            lado3 = float(input("digite o valor do terceiro lado : "))
            return lado3
        except ValueError:
            print("digite apenas numeros. Ex:14")

lado1 = primeiro_lado()
lado2 = segundo_lado()
lado3 = terceiro_lado()


if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    triangulo = "O triângulo apresentado é equilátero"
    exiba=(triangulo)

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
  triangulo = "O triângulo apresentado é isóceles"
  exiba=(triangulo)

elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
  triangulo = "O triângulo apresentado é escaleno"
  exiba=(triangulo)

else:
  exiba=("As informações inseridas estão incorretas")

print("O triangulo é : ",exiba)