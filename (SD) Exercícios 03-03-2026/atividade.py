#Exercicio cleber
import math
import random

# Descrição: Crie um programa que demonstra o uso de variáveis básicas (inteiros, floats,
# strings e booleanos). Após entender como funciona, modifique o programa para incluir mais
# dois tipos de variáveis: uma lista e um dicionário.
print(" Variáveis Simples")

inteiro = 10
decimal = 5.5
texto = "ola mundo"
booleano = True

lista = [1, 2, 3, 4]
dicionario = {"nome": "lucas", "idade": 19}

print(inteiro)
print(decimal)
print(texto)
print(booleano)
print(lista)
print(dicionario)


# • Descrição: O programa irá solicitar que o usuário insira um nome e um número. Verificar se o
# número digitado é par ou ímpar, validar se o nome contém mais de 3 caracteres. Se não, peça
# para o usuário digitar novamente.
print(" Entrada de Dados")

nome = input("Digite seu nome: ")

while len(nome) <= 3:
    nome = input("Nome muito curto, digite novamente: ")

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print("Numero par")
else:
    print("Numero impar")


# • Descrição: Um programa que realiza operações matemáticas básicas (soma, subtração,
# multiplicação, divisão, raiz quadrada e logaritmo) entre dois números fornecidos pelo usuário.
print(" Operações Matemáticas Básicas:")

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

print("Soma:", n1 + n2)
print("Subtracao:", n1 - n2)
print("Multiplicacao:", n1 * n2)

if n2 != 0:
    print("Divisao:", n1 / n2)

print("Raiz quadrada do primeiro:", math.sqrt(n1))

if n1 > 0:
    print("Logaritmo do primeiro:", math.log(n1))


# Descrição: Uma loja virtual apresenta ao usuário a possibilidade de escolher entre diferentes
# produtos (mínimo de 3) e suas quantidades, calcular o valor total de um pedido e incluir
# descontos baseados na quantidade de itens (5) comprados e adicione a opção de calcular o
# frete baseado em correio, transportadora e motoboy.
print(" Loja Virtual:")

print("1 - Camisa 50")
print("2 - Tenis 200")
print("3 - Bone 30")

op = int(input("Escolha produto: "))
qtd = int(input("Quantidade: "))

total = 0

if op == 1:
    total = 50 * qtd
elif op == 2:
    total = 200 * qtd
elif op == 3:
    total = 30 * qtd

# desconto se comprar 5 ou mais
if qtd >= 5:
    total = total * 0.9  # 10 porcento desconto

print("Escolha frete:")
print("1 - Correio 20")
print("2 - Transportadora 40")
print("3 - Motoboy 15")

frete = int(input("Opcao: "))

if frete == 1:
    total += 20
elif frete == 2:
    total += 40
elif frete == 3:
    total += 15

print("Total da compra:", total)


# • Descrição: Um programa que permite ao usuário adivinhar um número e recebe feedback se
# o palpite foi maior ou menor que o número correto.
# Expanda o programa para incluir diferentes níveis de dificuldade (fácil, médio, difícil), onde o
# intervalo de números varia.
print("Adivinhação:")

print("Nivel:")
print("1 - facil (1 a 10)")
print("2 - medio (1 a 50)")
print("3 - dificil (1 a 100)")

nivel = int(input("Escolha: "))

if nivel == 1:
    numero_secreto = random.randint(1, 10)
elif nivel == 2:
    numero_secreto = random.randint(1, 50)
else:
    numero_secreto = random.randint(1, 100)

palpite = int(input("Tente adivinhar: "))

while palpite != numero_secreto:
    if palpite > numero_secreto:
        print("Muito alto")
    else:
        print("Muito baixo")
    palpite = int(input("Tente de novo: "))

print("Acertou!")


# • Descrição: Um programa que calcula as somas das notas de provas e trabalhos e determina
# se o aluno foi aprovado, está em recuperação, ou foi reprovado. Adicione a funcionalidade de
# calcular médias trimestrais e uma média anual ao final.
print(" Notas Finais:")

nota1 = float(input("Nota prova 1: "))
nota2 = float(input("Nota prova 2: "))
trab1 = float(input("Nota trabalho 1: "))
trab2 = float(input("Nota trabalho 2: "))

media = (nota1 + nota2 + trab1 + trab2) / 4

print("Media final:", media)

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperacao")
else:
    print("Reprovado")


# • Descrição: Um programa que calcula o peso ideal baseado na altura e sexo do usuário,
# também calcular o IMC (Índice de Massa Corporal) e fazer recomendações baseadas no
# resultado.
print("Peso Ideal:")

sexo = input("Digite sexo (M/F): ")
altura = float(input("Altura em cm: "))
peso = float(input("Peso em kg: "))

if sexo == "M":
    peso_ideal = (altura - 100) - (altura - 150) / 4
else:
    peso_ideal = (altura - 100) - (altura - 150) / 2

print("Peso ideal:", peso_ideal)

imc = peso / ((altura / 100) ** 2)

print("IMC:", imc)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")


# • Descrição: Crie um sistema de loja onde o usuário pode escolher produtos, calcular o total, e
# optar por pagamento à vista ou parcelado. Adicione taxas de juros para pagamentos
# parcelados
print("Sistema de Loja com Pagamento:")

print("Produto A 100")
print("Produto B 200")

escolha = int(input("Escolha produto: "))
quant = int(input("Quantidade: "))

if escolha == 1:
    total2 = 100 * quant
else:
    total2 = 200 * quant

print("1 - A vista")
print("2 - Parcelado")

pag = int(input("Forma pagamento: "))

if pag == 1:
    total2 = total2 * 0.95  # 5 desconto
else:
    total2 = total2 * 1.1   # 10 juros

print("Total a pagar:", total2)
