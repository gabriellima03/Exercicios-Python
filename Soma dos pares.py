soma = 0
cont = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}° valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números pares e a soma deles é: {soma}')