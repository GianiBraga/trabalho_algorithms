import matplotlib.pyplot as plt

# Defina use_log_x = True para escala logarítmica no eixo X, False para escala normal
use_log_x = False

# Tamanhos das entradas
tamanhos = [
    100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
    1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
    2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000
]

# Tempos de execução
tempos = [
    0.000074, 0.000137, 0.000174, 0.000248, 0.000301,
    0.000386, 0.000473, 0.000550, 0.000696, 0.000789,
    0.000789, 0.000881, 0.000907, 0.000951, 0.001018,
    0.001084, 0.001157, 0.001225, 0.001298, 0.001334,
    0.001407, 0.001466, 0.001498, 0.001585, 0.001647,
    0.001694, 0.001751, 0.001822, 0.001925, 0.001987
]

# Desvios padrão
desvios = [
    0.000023, 0.000030, 0.000040, 0.000058, 0.000058,
    0.000102, 0.000096, 0.000121, 0.000122, 0.000156,
    0.000128, 0.000161, 0.000177, 0.000188, 0.000165,
    0.000178, 0.000163, 0.000202, 0.000230, 0.000114,
    0.000166, 0.000173, 0.000219, 0.000230, 0.000174,
    0.000189, 0.000236, 0.000266, 0.000212, 0.000264
]

# Cria o gráfico com linha azul e barras de erro vermelhas
plt.figure(figsize=(10, 6))
plt.errorbar(
    x=tamanhos,
    y=tempos,
    yerr=desvios,
    fmt='o-',
    color='blue',     # linha e marcadores em azul
    ecolor='red',     # barras de erro em vermelho
    elinewidth=1.5,
    capsize=3,
    label='Tempo de Execução'
)

# Escolha entre escala normal ou logarítmica no eixo X
if use_log_x:
    plt.xscale('log')
    escala = 'Logarítmica'
else:
    plt.xscale('linear')
    escala = 'Linear'

# Títulos e rótulos
plt.title(f'Tempo de Execução vs Tamanho da Entrada (Escala X: {escala})', fontsize=14)
plt.xlabel('Tamanho da String (n)', fontsize=12)
plt.ylabel('Tempo (segundos)', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()

# Exibe o gráfico
plt.show()
