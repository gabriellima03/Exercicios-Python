valorcasa = float(input('Qual é o valor da casa? '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Em quantos anos você vai pagar a casa? '))
prestacao = valorcasa / (anos * 12)
porcentagem = salario * 30 / 100
print(f'O valor da prestação é de: R${prestacao:.2f}')
if prestacao > porcentagem:
    print('O empréstimo foi negado, pois a prestação excede 30% do seu salário!')
else:
    print('O empréstimo foi aprovado!')