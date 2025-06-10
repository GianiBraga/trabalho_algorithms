import matplotlib.pyplot as plt

# Dados de exemplo (você pode substituir pelos seus valores reais)
# Tamanhos das entradas (valores de TAMANHO_STRING usados no C)
tamanhos = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000]

# Tempos de execução correspondentes (em segundos)
tempos = [0.0040, 0.0128, 0.0380, 0.0728, 0.1488, 0.2366, 0.3484, 0.4874, 0.6852, 1.0792, 1.2492, 1.6146, 2.0414, 2.7604, 3.3856, 3.8530, 4.4776, 5.2648 , 6.6386  , 7.5002, 8.3808, 9.9332, 11.0734, 12.7002, 14.3946, 16.1742, 19.8126, 21.6882, 22.8996, 25.6902]  # substitua pelos seus

# Desvios padrão correspondentes
desvios = [0.0007, 0.0040, 0.0130, 0.0198, 0.0372, 0.0402,  0.0415, 0.0333, 0.0467, 0.0426, 0.0608, 0.0311, 0.0546, 0.1385, 0.1315, 0.0860, 0.0999, 0.1723, 0.1469, 0.1488, 0.1567, 0.0508, 0.1881, 0.1582, 0.4935, 0.4347, 1.0975, 1.1245, 0.8569, 1.3152]

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
