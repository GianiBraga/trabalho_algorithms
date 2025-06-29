import matplotlib.pyplot as plt

# Defina use_log_x = True para escala logarítmica no eixo X, False para escala normal
use_log_x = False

# Tamanhos das entradas (valores de TAMANHO_STRING usados no C)
tamanhos = [
    100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
    1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
    2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000
]

# Tempos de execução correspondentes (em segundos)
tempos = [
    0.0008, 0.0054, 0.0172, 0.0395, 0.0757,
    0.1290, 0.2078, 0.3006, 0.4292, 0.5820,
    0.7756, 1.0786, 1.3811, 1.6662, 2.3295,
    2.6001, 3.3389, 3.6474, 4.5854, 5.4063,
    6.1034, 6.5761, 7.2961, 8.3127, 9.0586,
    10.4286, 12.8581, 14.5126, 17.5305,18.3522
]



# Desvios padrão correspondentes
desvios = [
    0.0001, 0.0002, 0.0003, 0.0005, 0.0003,
    0.0005, 0.0013, 0.0006, 0.0054, 0.0006,
    0.0051, 0.0014, 0.0108, 0.0158, 0.0018,
    0.0017, 0.0053, 0.0022, 0.0513, 0.0354,
    0.0192, 0.0463, 0.0749, 0.0443, 0.0352,
    0.0409, 0.0042, 0.0622, 0.0105, 0.0075
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
