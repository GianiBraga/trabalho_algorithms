import matplotlib.pyplot as plt

# Tamanhos das entradas
tamanhos = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000] 

# Tempos de execução
tempos = [0.000322, 0.000491, 0.000812, 0.000924, 0.001251, 0.001386, 0.001523, 0.001624, 0.001843, 0.001960, 0.002078, 0.002110, 0.002191, 0.002224, 0.002352, 0.002373, 0.002501, 0.002642, 0.002783 , 0.002853 , 0.002910, 0.003160, 0.003235, 0.003443, 0.003513 , 0.003679, 0.003766, 0.003967, 0.004000, 0.004160]

# Desvios padrão correspondentes
desvios = [0.000097, 0.000212, 0.000328, 0.000560, 0.000655, 0.000759, 0.000859, 0.000949, 0.001031, 0.001130, 0.001289, 0.001378, 0.001440, 0.001549, 0.001603, 0.001756, 0.001801, 0.001943, 0.002032, 0.002197, 00.002243, 0.002321, 0.002468, 0.002543, 0.002625, 0.002719, 0.002807, 0.002984, 0.003021, 0.003136]

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
