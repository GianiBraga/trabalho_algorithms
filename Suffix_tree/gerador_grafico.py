import matplotlib.pyplot as plt

# Tamanhos das entradas
tamanhos = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000] 

# Tempos de execução
tempos = [0.000322, 0.000491, 0.000812, 0.000924, 0.001251, 0.001386, 0.001523, 0.001624, 0.001843, 0.001960, 0.002078, 0.002110, 0.002191, 0.002224, 0.002352, 0.002373, 0.002401, 0.002742, 0.002783 , 0.002823 , 0.003010, 0.003160, 0.003335, 0.003543, 0.003613 , 0.003879, 0.003966, 0.004167, 0.004200, 0.004260]

# Desvios padrão correspondentes
desvios = [0.000097, 0.000212, 0.000428, 0.000360, 0.000955, 0.000959, 0.001259, 0.001649, 0.001431, 0.001730, 0.001589, 0.001678, 0.001640, 0.001949, 0.002003, 0.001956, 0.001901, 0.002543, 0.002432, 0.002997, 00.002643, 0.002821, 0.003168, 0.002943, 0.003425, 0.002919, 0.004007, 0.004284, 0.003121, 0.003536]

# Criando o gráfico
plt.figure(figsize=(30, 6))

# Linha do tempo
plt.plot(tamanhos, tempos, marker='o', linestyle='-', color='blue', linewidth=2, label='Tempo de Execução')

# Linha do desvio padrão
plt.plot(tamanhos, desvios, marker='x', linestyle='--', color='red', linewidth=2, label='Desvio Padrão')

# Títulos e rótulos
plt.title('Tempo de Execução vs Tamanho da Entrada (com Desvio Padrão)', fontsize=14)
plt.xlabel('Tamanho da String (n)', fontsize=12)
plt.ylabel('Tempo (segundos)', fontsize=12)
plt.grid(True)
plt.xticks(tamanhos)
plt.legend()
plt.tight_layout()

# Exibe o gráfico
plt.show()
