from datetime import datetime


def menu_calculadora():

    print("Calculadora")
    print("1-soma")
    print("2-subtração")
    print("3-multiplicação")
    print("4-divisao")

ano=int(input("Digite o ano em que voce nasceu: "))
def ola_nome(nome):
    print(f"Ola {nome}")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade
def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    return idade

def return_ola_nome(nome):
    return f"Ola {nome}"
#exiba o menu da calculadora
menu_calculadora()

#exiba o print com 'ola nome'
ola_nome("yasmin")

#retorno o texto com o 'ola nome'
print(return_ola_nome("yasmin"))

print("a sua idade é", calcular_idade(ano))