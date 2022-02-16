#Leia nome, idade e sexo de 4 pessoas --> mostre a média das idades --> nome do homem mais velho -->
#qtd mulheres com menos de 20 anos.
soma_idade = 0
media_idade = 0
cont_pessoas = 0
hmaisvelho = 0
nomehmaisvelho = ''
qtdmulheressub20 = 0
for pessoa in range(1, 5):
    nome = input(f'''{pessoa}° pessoa:
Digite o seu nome: ''')
    idade = int(input('Digite a sua idade: '))
    sexo = input('Sexo [M / F]: ').upper()
    soma_idade += idade
    cont_pessoas = cont_pessoas + 1
    if sexo[0] == 'M' and idade > hmaisvelho:
        hmaisvelho = idade
        nomehmaisvelho = nome
    if sexo[0] == 'F' and idade < 20:
        qtdmulheressub20 += 1
media_idade = soma_idade / cont_pessoas
print(f'A média da idade é {media_idade}!')
print(f'O homem mais velho se chama {nomehmaisvelho}.')
print(f'A quantidade de mulheres com menos de 20 anos é {qtdmulheressub20}.')

