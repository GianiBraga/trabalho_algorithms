import matplotlib.pyplot as plt
import numpy as np

# Dados
tamanhos = [
    100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
    1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000,
    2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000
]

tempos = [
    0.000074, 0.000137, 0.000174, 0.000248, 0.000301,
    0.000386, 0.000473, 0.000550, 0.000696, 0.000789,
    0.000789, 0.000881, 0.000907, 0.000951, 0.001018,
    0.001084, 0.001157, 0.001225, 0.001298, 0.001334,
    0.001407, 0.001466, 0.001498, 0.001585, 0.001647,
    0.001694, 0.001751, 0.001822, 0.001925, 0.001987
]

# Regressão linear
coef = np.polyfit(tamanhos, tempos, 1)
polinomio = np.poly1d(coef)
ajuste = polinomio(tamanhos)

plt.figure(figsize=(10, 6))
# Pontos em azul, sem linha
plt.scatter(tamanhos, tempos, color='blue', label='Tempo de Execução')

# Linha de regressão linear em verde tracejado
plt.plot(tamanhos, ajuste, color='green', linestyle='--', linewidth=2,
         label=f'Regressão Linear (y={coef[0]:.2e}x+{coef[1]:.2e})')

plt.xlabel('Tamanho da String (n)', fontsize=12)
plt.ylabel('Tempo (segundos)', fontsize=12)
plt.title('Tempo de Execução vs Tamanho da Entrada (Regressão Linear)', fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
