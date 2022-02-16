num = (int(input('Digite um número: '))), \
(int(input('Digite outro número: '))), \
(int(input('Digite mais um número: '))), \
(int(input('Digite o último número: ')))
print(f'Você digitous os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vez(es).')
print(f'O valor 3 apareceu na {num.index(3) + 1}° posição.')
