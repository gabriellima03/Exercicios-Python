#Crie um programa que leia dois valores e mostre um menu na tela para somar, multiplicar, mostrar o maior valor, opção
#de novos números e opção de sair do programa
from time import sleep
num1 = int(input('Digite um valor: '))
num2 = int(input('Agora digite outro: '))
opção = 0
maiorvalor = 0
while opção != 5:
    sleep(1)
    opção = int(input('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR VALOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
Escolha uma opção: '''))
    print('-=-' * 14)
    if opção == 1:
        soma = num1 + num2
        print(f'A soma entre os dois números é {soma}.\n')
    elif opção == 2:
        produto = num1 * num2
        print(f'O produto entre os dois números é {produto}.\n')
    elif opção == 3:
        if num1 > num2:
            maiorvalor = num1
        else:
            maiorvalor = num2
        print(f'O maior valor entre os dois números é o {maiorvalor}.\n')
    elif opção == 4:
        num1 = int(input('Digite um valor: '))
        num2 = int(input('Agora digite outro: '))
    elif opção == 5:
        print('FINALIZANDO...')
    else:
        print('Opção inválida, tente novamente!')
