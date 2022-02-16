num = 1
while num > 0:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num}x{i} = {num * i}')
print('PROGRAMA TABUADA ENCERRADO.')


