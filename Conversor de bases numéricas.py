num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
 [ 1 ] Converter para BINÁRIO
 [ 2 ] Converter para OCTAL
 [ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'O BINÁRIO é {bin(num)}')
elif opcao == 2:
    print(f'O OCTAL é {oct(num)}')
elif opcao == 3:
    print(f'O HEXADECIMAL é {hex(num)}')
