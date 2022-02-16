opção = ''
media = soma = cont = 0
while opção != 'N':
    num = int(input('Digite um número: '))
    soma += num
    opção = input('Quer continuar? [S/N]: ').upper()[0]
    while opção != 'S' and opção != 'N':
        opção = input('Opção inválida. Quer continuar? [S/N]: ').upper()[0]
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print(f'Você digitou {cont} números e a média entre eles é {media:.2f}.')
print(f'O maior valor é {maior} e o menor é {menor}.')

