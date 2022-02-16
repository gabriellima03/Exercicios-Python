from datetime import date
totmaior = 0
totmenor = 0
for i in range(1, 8):
    ano = int(input(f'Em que ano a {i}° pessoa nasceu? '))
    atual = date.today().year
    idade = atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Temos {totmaior} pessoas maior de idade e {totmenor} pessoas menor de idade.')




