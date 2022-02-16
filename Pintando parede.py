largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print(f'A dimensão da parede é de {largura}x{altura} e a área é de {area}m²')
print('Para pintar a parede, você precisará de {} litros de tinta!'.format(area / 2))