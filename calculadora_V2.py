"""
Nome do programa: funcoes2.py
Descricao: Calculadora
Autor: Evando Chaves
Criado em: 28/07/2024
"""

saida = ''

def adicao(num1, num2):
    return num1+num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return 'Nao foi possivel realizar a divisao por 0'
    else:
        return num2 / num1

def calculadora(numero1, numero2, operacao):
    resultado = None
    
    if operacao == '+':
        resultado = adicao(numero1, numero2)
    elif operacao == '-':
        resultado = subtracao(numero1, numero2)
    elif operacao == '*':
        resultado = multiplicacao(numero1, numero2)
    elif operacao == '/':
        resultado = divisao(numero1, numero2)
    else:
        resultado = 'Operacao invalida'
    return resultado

while saida.lower() != 'n':

    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))

    operacao = input('Digite a operação (+, -, *, / ):')
    
    resultado = calculadora(numero1, numero2, operacao)
    
    print('Resultado da operacao:', resultado)

    
    saida = input("Deseja continuar? Digite 'S' para sim ou 'N' para nao: ")




