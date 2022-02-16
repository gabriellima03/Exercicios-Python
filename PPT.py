from random import randint
from time import sleep
cont = 0
print('PEDRA, PAPEL E TESOURA\n')
itens = ('PEDRA', 'PAPEL', 'TESOURA')

while True:
    print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
    jogador = input('Digite a sua opção: ').upper()
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')

    while jogador != '0' and jogador != 'PEDRA' and jogador != '1' and jogador != 'PAPEL' and jogador != '2' and jogador != 'TESOURA':
        jogador = input('Opção inválida. Digite a sua opção: ').upper()

    if jogador == '0' or jogador == 'PEDRA':
        jogador = itens[0]
    elif jogador == '1' or jogador == 'PAPEL':
        jogador = itens[1]
    elif jogador == '2' or jogador == 'TESOURA':
        jogador = itens[2]

    computador = randint(0, 2)

    print('-=' * 13)
    print(f'Jogador jogou {jogador}')
    print(f'Computador jogou {itens[computador]}')
    print('-=' * 13)

    if jogador == 0 or jogador == 'PEDRA':
        if computador == 0:
            print('EMPATE!\n')
        elif computador == 1:
            break
        elif computador == 2:
            cont += 1
            print('JOGADOR VENCE!\n')

    elif jogador == 1 or jogador == 'PAPEL':
        if computador == 0:
            cont += 1
            print('JOGADOR VENCE!\n')
        elif computador == 1:
            print('EMPATE!\n')
        elif computador == 2:
            break

    elif jogador == 2 or jogador == 'TESOURA':
        if computador == 0:
            break
        elif computador == 1:
            cont += 1
            print('JOGADOR VENCE!\n')
        elif computador == 2:
            print('EMPATE!\n')

print('COMPUTADOR VENCE!')
print(f'PROGRAMA FINALIZADO. Você obteve {cont} vitória(s).')

