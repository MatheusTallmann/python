import math

# 1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.
def Exercicio1():
  valorA = int(input("Digite um valor para A: "))
  valorB = int(input("Digite um valor para B: "))
  valorC = int(input("Digite um valor para C: "))
  
  soma = valorB + valorA

  print(f"Soma de A com B: {soma}")
  
  if soma < valorC:
    print(f"A soma de A com B ({soma}) é menor que C ({valorC})")
  else:
    print(f"A soma de A com B ({soma}) não é menor que C ({valorC})")    


# 2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.
def Exercicio2():
  valor = float(input("Digite um valor qualquer: "))    

  if valor % 2 == 0:
    print("Este número é par!")
  else:
    print("Este número é impar!")

  if valor > 0:
    print("E ele também é positivo!")    
  else:
    print("E ele também é negativo!")  

# 3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, 
# deverá somar os dois valores, caso contrário devera multiplicar A por B. 
# Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e imprimir seu valor na tela.
def Exercicio3():
  a = int(input("Digite um valor inteiro para A: "))
  b = int(input("Digite um valor inteiro para B: "))

  if a == b:
    c = a+b
    print(f"Soma de A com B gera C({c})")
  else:
    c = a*b
    print(f"Multiplicação de A com B gera C({c})")
  
# 4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.
def Exercicio4():
  numero = int(input("Informe um número inteiro: "))

  print(f"Antecessor de {numero} é {numero-1}!")
  print(f"Sucessor de {numero} é {numero+1}!")


# 5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, 
# calcule quantos salários mínimos esse usuário ganha e imprima na tela o resultado. 
# (Base para o Salário mínimo R$ 1.518,00).
def Exercicio5():
  salario = float(input("Informe seu salário: "))
  print(f"Você recebe {int(salario / 1518)} salário(s) mínimo(s)!") 
  print(f"Equivalente a {salario / 1518:.2%} do salário mínimo!")

# 6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.
def Exercicio6():
  valor = float(input("Informe um valor a ser reajustado: "))

  valor = valor + (valor * 5 / 100)

  print(f"Valor reajustado: R${valor:.2f}")

# 7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO.
def Exercicio7():
  a = bool(int(input("Informe 1 Para True e 0 para False a: ")))
  b = bool(int(input("Informe 1 Para True e 0 para False b: ")))  

  if a and b:
    print("Ambos são true")
  elif not a and not b:
    print("Ambos são false")
  else:
    print(f"Eles possuem valores diferentes, a:{a} b:{b}")

# 8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.
def Exercicio8():
  a = int(input("Informe um valor inteiro para a: "))
  b = int(input("Informe um valor inteiro para b: "))
  c = int(input("Informe um valor inteiro para c: "))

  valores = [a,b,c]
  valores.sort(reverse=True)

  print(f"Valores em order descrescente: {valores}")

# 9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição de acordo com a tabela abaixo:
# Fórmula do IMC = peso / (altura) ²
# Tabela Condições IMC
# Abaixo de 18,5   | Abaixo do peso
# Entre 18,6 e 24,9 | Peso ideal (parabéns)
# Entre 25,0 e 29,9 | Levemente acima do peso
# Entre 30,0 e 34,9 | Obesidade grau I
# Entre 35,0 e 39,9 | Obesidade grau II (severa)
# Maior ou igual a 40 | Obesidade grau III (mórbida)

def Exercicio9():
  peso = float(input("Informe seu peso em Kg: "))
  altura = float(input("Informe sua altura em metros: "))

  imc = peso / (altura * altura)

  if imc < 18.5:
    print("Abaixo do Peso")
  elif imc >= 18.6 and imc <= 24.9:
    print("Peso ideal (parabéns)")
  elif imc >= 25 and imc <=29.9:
    print("Levemente acima do peso")
  elif imc >= 30 and imc <= 34.9:
    print("Obesidade grau I")
  elif imc >= 35 and imc <= 39.9:
    print("Obesidade grau II (severa)")
  else:
    print("Obesidade grau III (mórbida)")

# 10 - Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.
def Exercicio10():
  nota1 = float(input("Informe a nota 1: "))
  nota2 = float(input("Informe a nota 2: "))
  nota3 = float(input("Informe a nota 3: "))

  media = (nota1 + nota2 + nota3) / 3

  print(f"Média das notas: {media}")

Exercicio10()