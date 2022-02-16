times =('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
        'Atlético-MG', 'Atlético-PR', 'Cruzeiro', 'Botafogo',
        'Santos', 'Bahia', 'Fluminense', 'Corinthians',
        'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG',
        'Vitória', 'Paraná')

print(f'\nLista de times do Brasileirão: {times}')
print(f'\n5 primeiros colocados: {times[0:5]}')
print(f'\n4 últimos colocados: {times[-4:]}')
print(f'\nTimes em ordem alfabética: {sorted(times)}')
print(f'\nO Chapecoense está na {times.index("Chapecoense")}° posição')