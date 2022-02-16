print('CÁLCULO DE IMC\n')
peso = float(input('Digite o seu peso (KG): '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura ** 2
print(f'O seu IMC é de: {imc:.1f}! ')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('Você está no seu peso ideal.')
elif imc <= 30:
    print('Você está com sobrepeso.')
elif imc <= 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')

