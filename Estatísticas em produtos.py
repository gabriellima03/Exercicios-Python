opção = mais_barato = ''
total = cont_mil = valor_mais_barato = cont = 0
print('ESTATÍSTICAS EM PRODUTOS')
while opção != 'N':
    produto = input('\nNome do produto: ')
    preço = float(input('Preço: R$'))
    cont += 1
    if cont == 1:
        valor_mais_barato = preço
        mais_barato = produto
    if preço < valor_mais_barato:
        valor_mais_barato = preço
        mais_barato = produto
    total += preço
    if preço > 1000:
        cont_mil += 1
    opção = input('Quer continuar? [S/N]: ').upper()
    while opção != 'S' and opção != 'N':
        opção = input('Opção inválida. Quer continuar? [S/N]: ').upper()
print(f'O total da compra foi de R${total:.2f}.')
print(f'{cont_mil} produtos tem um valor acima de R$1000,00.')
print(f'O produto mais barato foi o(a) {mais_barato}, custando R${valor_mais_barato:.2f}.')
