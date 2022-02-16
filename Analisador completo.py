#Leia nome, idade e sexo de 4 pessoas --> mostre a média das idades --> nome do homem mais velho -->
#qtd mulheres com menos de 20 anos.
soma_idade = 0
media_idade = 0
cont_pessoas = 0
idadehmaisvelho = 0
nomehmaisvelho = ''
qtdmulheressub20 = 0
for pessoa in range(1, 5):
    nome = input(f'''{pessoa}° pessoa:
Digite um nome: ''')
    idade = int(input('Digite uma idade: '))
    sexo = input('Sexo [M / F]: ').upper()
    cont_pessoas += 1
    soma_idade += idade
    media_idade = soma_idade / cont_pessoas
    if sexo[0] == 'M' and idade > idadehmaisvelho:
        idadehmaisvelho = idade
        nomehmaisvelho = nome
    if sexo[0] == 'F' and idade < 20:
        qtdmulheressub20 += 1
print(f'A média de todas as idades é de {media_idade}.')
print(f'O homem mais velho tem {idadehmaisvelho} anos e se chama {nomehmaisvelho}.')
print(f'Existe(m) {qtdmulheressub20} mulher(es) com menos de 20 anos.')


