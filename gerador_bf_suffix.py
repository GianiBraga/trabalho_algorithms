import matplotlib.pyplot as plt

# Defina use_log_x = True para escala logarítmica no eixo X, False para escala normal
use_log_x = False

# Tamanhos das entradas (valores de TAMANHO_STRING usados no C)
tamanhos = [
    100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
    1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
    2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000
]

# Dados do algoritmo de Ukkonen (Árvore de Sufixos)
tempos_st = [
    0.000074, 0.000137, 0.000174, 0.000248, 0.000301,
    0.000386, 0.000473, 0.000550, 0.000696, 0.000789,
    0.000789, 0.000881, 0.000907, 0.000951, 0.001018,
    0.001084, 0.001157, 0.001225, 0.001298, 0.001334,
    0.001407, 0.001466, 0.001498, 0.001585, 0.001647,
    0.001694, 0.001751, 0.001822, 0.001925, 0.001987
]
desvios_st = [
    0.000023, 0.000030, 0.000040, 0.000058, 0.000058,
    0.000102, 0.000096, 0.000121, 0.000122, 0.000156,
    0.000128, 0.000161, 0.000177, 0.000188, 0.000165,
    0.000178, 0.000163, 0.000202, 0.000230, 0.000114,
    0.000166, 0.000173, 0.000219, 0.000230, 0.000174,
    0.000189, 0.000236, 0.000266, 0.000212, 0.000264
]

# Dados do método de Força Bruta
tempos_fb = [
    0.0008, 0.0054, 0.0172, 0.0395, 0.0757,
    0.1290, 0.2078, 0.3006, 0.4292, 0.5820,
    0.7756, 1.0786, 1.3811, 1.6662, 2.3295,
    2.6001, 3.3389, 3.6474, 4.5854, 5.4063,
    6.1034, 6.5761, 7.2961, 8.3127, 9.0586,
    10.4286, 12.8581, 14.5126, 17.5305, 18.3522
]
desvios_fb = [
    0.0001, 0.0002, 0.0003, 0.0005, 0.0003,
    0.0005, 0.0013, 0.0006, 0.0054, 0.0006,
    0.0051, 0.0014, 0.0108, 0.0158, 0.0018,
    0.0017, 0.0053, 0.0022, 0.0513, 0.0354,
    0.0192, 0.0463, 0.0749, 0.0443, 0.0352,
    0.0409, 0.0042, 0.0622, 0.0105, 0.0075
]

# Inicia figura
plt.figure(figsize=(10, 6))

# Traça Ukkonen
plt.errorbar(
    tamanhos, tempos_st, yerr=desvios_st,
    fmt='o-', capsize=3, elinewidth=1.5,
    label='Árvore de Sufixos (Ukkonen)',
    color='blue', ecolor='blue'
)

# Traça Força Bruta
plt.errorbar(
    tamanhos, tempos_fb, yerr=desvios_fb,
    fmt='s--', capsize=3, elinewidth=1.5,
    label='Força Bruta',
    color='orange', ecolor='orange'
)

# Ajusta escala do eixo X
if use_log_x:
    plt.xscale('log')

# Títulos e rótulos
plt.title('Comparação de Tempo de Execução\nUkkonen vs Força Bruta', fontsize=14)
plt.xlabel('Tamanho da String (n)', fontsize=12)
plt.ylabel('Tempo de Execução (s)', fontsize=12)

plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()

# Exibe o gráfico
plt.show()
