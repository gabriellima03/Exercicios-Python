#Tente adivinhar o número que o computador pensou (1, 10) --> só pare quando acertar --> mostre o número de tentativas
from random import randint
from time import sleep
computador = randint(0, 10)
jogador = 0
cont_palpites = 0
print('JOGO DA ADIVINHAÇÃO\n')
print('PENSANDO...')
sleep(3)
while jogador != computador:
    jogador = int(input('Tente adivinhar o número que eu pensei: '))
    cont_palpites += 1
    if jogador != computador:
        print('Errou. Tente novamente!')
    else: print(f'Parabéns, você me venceu depois de {cont_palpites} tentativa(s)! ')