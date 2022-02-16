numeros = cont = soma = 0
numeros = int(input('Digite um  número [999 para parar]: '))
while numeros != 999:
    soma += numeros
    cont += 1
    numeros = int(input('Digite um  número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')

