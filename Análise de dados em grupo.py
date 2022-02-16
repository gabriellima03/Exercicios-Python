opção = ''
cont_maioridade = cont_homens = cont_msub20 = 0
print('CADASTRE AS INFORMAÇÕES')
while opção != 'N':
    sexo = input('\nDigite o seu sexo [M/F]: ').upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = input('\nOpção inválida. Digite o seu sexo [M/F]: ').upper()[0]
    if sexo == 'M':
        cont_homens += 1
    idade = int(input('Agora digite a sua idade: '))
    if idade >= 18:
        cont_maioridade += 1
    elif sexo == 'F' and idade < 20:
        cont_msub20 += 1
    opção = input('\nDeseja continuar? [S/N]: ').upper()
    while opção != 'S' and opção != 'N':
        opção = input('\nOpção inválida. Deseja continuar? [S/N]: ').upper()
print(f'{cont_maioridade} pessoas são maiores de idade.')
print(f'{cont_homens} homens foram cadastrados.')
print(f'{cont_msub20} mulheres têm menos de 20 anos.')
