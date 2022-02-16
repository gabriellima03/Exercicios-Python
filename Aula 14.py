#Leia o sexo de uma pessoa, mas só aceite 'M' e 'F', caso contrário, peça para digitar novamente.
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Sexo [M/F]: ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida. Digite novamente.')
    else:
        print('Fim.')
