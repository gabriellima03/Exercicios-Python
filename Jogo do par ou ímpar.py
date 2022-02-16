from random import randint
cont = 0
print('PAR OU ÍMPAR (NÃO UTILIZE ACENTOS)\n')
while True:
    escolha = (input('Escolha [PAR/IMPAR]: ')).upper()
    while escolha != 'IMPAR' and escolha != 'PAR':
        escolha = input('Opção inválida. Escolha [PAR/IMPAR]: ').upper()
    jogador = int(input('Digite um número de 1 a 5: '))
    while jogador < 1 or jogador > 5:
        jogador = int(input('Digite um número de 1 a 5: '))
    computador = randint(1, 5)
    resultado = jogador + computador
    print(f'O computador jogou {computador} e o resultado é {resultado}.')
    if escolha == 'PAR' and resultado % 2 == 0:
        print('Você GANHOU!\n')
    elif escolha == 'IMPAR' and resultado % 2 == 1:
        print('Você GANHOU!\n')
    else:
        break
    cont += 1
print('Você PERDEU. Programa finalizado.')
print(f'Você teve {cont} vitórias.')
