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

Exercicio5()