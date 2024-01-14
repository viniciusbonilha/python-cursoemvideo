times = ('Botafogo', 'Palmeiras', 'Bragantino', 'Grêmio', 'Atlético-MG', 'Flamengo',
        'Athletico-PR', 'Fluminense', 'Fortaleza', 'São Paulo', 'Internacional',
        'Cuiabá', 'Corinthians', 'Santos', 'Bahia', 'Vasco da Gama', 'Cruzeiro',
        'Goiás', 'Coritiba', 'América-MG')
print('-' * 120)
print(f'Classificação do Brasileirão 2023: {times}')
print('-' * 120)
print(f'Os cinco primeiros colocados do Campeonato Brasileiro são: {times[0:5]} ')
print('-' * 120)
print(f'Os quatro últimos colocados do Campeonato Brasileiro são: {times[-4:]}')
print('-' * 120)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-' * 120)
print(f"O São Paulo está em {times.index('São Paulo')+1}º colocado.")
print('-' * 120)
