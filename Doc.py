"""
Documentação Simples - Conceitos Básicos de Python

Este arquivo contém exemplos e explicações sobre:
- Blocos Condicionais
- Laços de Repetição
- Variáveis
- Funções
- Métodos Principais (Impressão e Leitura)
"""

# -------------------------
# Variáveis
# -------------------------
# As variáveis armazenam valores e podem ser de diferentes tipos

# Exemplo de variáveis
nome = "Matheus"  # String
idade = 30      # Inteiro
altura = 1.75   # Float
ativo = True    # Booleano

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Ativo: {ativo}")

# -------------------------
# Blocos Condicionais
# -------------------------
# Estruturas condicionais permitem a execução de código baseado em condições

# Exemplo de if-elif-else
if idade < 18:
    print("Menor de idade")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")

# -------------------------
# Laços de Repetição
# -------------------------
# Os loops permitem a execução repetida de um bloco de código

# Exemplo de loop for
for i in range(5):
    print(f"Iteração {i}")

# Exemplo de loop while
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

# -------------------------
# Funções
# -------------------------
# As funções encapsulam código reutilizável

def saudacao(nome):
    """Função que recebe um nome e exibe uma saudação."""
    return f"Olá, {nome}!"

# Chamando a função
mensagem = saudacao("Maria")
print(mensagem)

# Exemplo de função com múltiplos parâmetros e retorno
def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

resultado = soma(10, 5)
print(f"Soma: {resultado}")

# -------------------------
# Métodos Principais - Impressão e Leitura
# -------------------------

# Impressão de dados
print("Este é um exemplo de impressão")

# Leitura de dados do usuário
entrada = input("Digite algo: ")
print(f"Você digitou: {entrada}")

# Leitura de números inteiros
numero = int(input("Digite um número inteiro: "))
print(f"Número digitado: {numero}")

# Leitura de números decimais
numero_decimal = float(input("Digite um número decimal: "))
print(f"Número decimal digitado: {numero_decimal}")