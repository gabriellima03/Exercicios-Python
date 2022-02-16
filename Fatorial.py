c = 1
num = int(input('Digite um valor: '))
while num < 0:
    num = int(input('O número digitado não pode ser negativo, tente novamente: '))
while num >= 1:
    c *= num
    num -= 1
print(f'O fatorial é {c}.')
