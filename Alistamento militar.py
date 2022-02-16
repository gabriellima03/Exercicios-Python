from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano
print(f'Você tem {idade} anos.')
if idade > 18:
    print(f'Você está {idade - 18} anos atrasado.')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
elif idade == 18:
    print('Está na hora de se alistar.')