maior = 0
menor = 0
for pessoa in range(1, 4):
    peso = float(input(f'Peso da {pessoa}° pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}.')
print(f'O menor peso lido foi {menor}.')
