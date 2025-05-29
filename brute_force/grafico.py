import matplotlib.pyplot as plt

# Dados de exemplo (você pode substituir pelos seus valores reais)
# Tamanhos das entradas (valores de TAMANHO_STRING usados no C)
tamanhos = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000]

# Tempos de execução correspondentes (em segundos)
tempos = [0.0040, 0.0128, 0.0380, 0.0728, 0.1488, 0.2366, 0.3484, 0.4874, 0.6852, 1.0792, 1.2492, 1.6146, 2.0414, 2.7604, 3.3856, 3.8530, 4.4776, 5.2648 , 11.6386 , 12.5002, 8.3808, 9.9332, 11.0734, 12.7002, 14.3946, 16.1742, 23.8126, 21.6882, 22.8996, 25.6902]  # substitua pelos seus

# Criando o gráfico de linha
plt.figure(figsize=(15, 6))
plt.plot(tamanhos, tempos, marker='o', linestyle='-', color='blue', linewidth=2)

# Títulos e rótulos
plt.title('Crescimento do Tempo de Execução x Tamanho da Entrada (LRS Força Bruta)', fontsize=14)
plt.xlabel('Tamanho da String (n)', fontsize=12)
plt.ylabel('Tempo de Execução (segundos)', fontsize=12)
plt.grid(True)
plt.xticks(tamanhos)
plt.tight_layout()

# Exibe o gráfico
plt.show()
