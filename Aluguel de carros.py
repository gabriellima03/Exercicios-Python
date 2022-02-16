km = float(input('Quantos kms você foram percorridos com o carro? '))
dias = int(input('Qual a quantidade de dias que ficou com o carro? '))
aluguel = (dias * 60) + (km * 0.15)
print(f'O aluguel do carro ficou avaliado em R${aluguel}!')