import random
nome1 = str(input('Primeiro nome: '))
nome2 = str(input('Segundo nome: '))
nome3 = str(input('Terceiro nome: '))
nome4 = str(input('Quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)