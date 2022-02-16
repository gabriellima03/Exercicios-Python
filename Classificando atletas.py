from datetime import date
nasc = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'A sua idade é {idade} anos!')
if idade <=9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25 :
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')