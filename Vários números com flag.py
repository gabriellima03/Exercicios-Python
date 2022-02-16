num = cont = soma = 0
while num != 999:
    num = int(input('Digite um valor [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} valores e a soma entre eles é {soma}.')


