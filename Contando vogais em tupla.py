listagem = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
         'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
         'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for item in listagem:
    print(f'\nNa palavra {item} temos: ', end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

