print('GERENCIADOR DE PAGAMENTOS\n')
preco = float(input('Preço do produto: R$'))
desconto10 = preco - (preco * 10 / 100)
desconto5 = preco - (preco * 5 / 100)
com_juros = preco + (preco * 20 / 100)
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
escolha = int(input('Qual é a opção? '))
if escolha == 1:
    print(f'Você conseguiu um desconto de 10%. Logo o novo valor é: R${desconto10}')
elif escolha == 2:
    print(f'Você conseguiu um desconto de 5%. Logo o novo valor é: R${desconto5}')
elif escolha == 3:
    print(f'Você pagará R${preco} em 2x de R${preco / 2} sem juros')
elif escolha == 4:
    parcelas = int(input('Em quantas vezes você quer parcelar o produto? '))
    print(f'Você pagará {parcelas}x de R${com_juros / parcelas} com juros. O novo valor é de R${com_juros}')
else:
    print('Opção inválida.')










