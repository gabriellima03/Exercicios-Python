num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',' dezenove','vinte')
opção = int(input('Digite um número entre 0 e 20: '))
while opção < 0 or opção > 20:
    opção = int(input('Opção inválida. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {num[opção]}.')

