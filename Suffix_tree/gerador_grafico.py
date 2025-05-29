import matplotlib.pyplot as plt

# Dados de exemplo (você pode substituir pelos seus valores reais)
# Tamanhos das entradas (valores de TAMANHO_STRING usados no C)
tamanhos = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000] 

# Tempos de execução correspondentes (em segundos)
tempos = [0.001200, 0.001200, 0.001600, 0.003400, 0.005600, 0.001800, 0.003600, 0.003000, 0.005400, 0.007600, 0.003800, 0.012200, 0.022200, 0.011000, 0.014200 , 0.005000 ,0.013400 , 0.020800 , 0.018400 , 0.027200 ,0.022000 ,0.008000 , 0.017600 , 0.019800 , 0.016400 , 0.022600 , 0.019000  ,0.032800  , 0.020200 , 0.021600 , 0.025600 , 0.020800 , 0.030400 , 0.040400 , 0.035800 , 0.028000 , 0.017600 , 0.031800 , 0.021200]  # substitua pelos seus

# Criando o gráfico de linha
plt.figure(figsize=(30, 6))
plt.plot(tamanhos, tempos, marker='o', linestyle='-', color='blue', linewidth=2)

# Títulos e rótulos
plt.title('Crescimento do Tempo de Execução x Tamanho da Entrada (LRS Suffix tree)', fontsize=14)
plt.xlabel('Tamanho da String (n)', fontsize=12)
plt.ylabel('Tempo de Execução (segundos)', fontsize=12)
# plt.ylim(0, 1) 
plt.grid(True)
plt.xticks(tamanhos)
plt.tight_layout()

# Exibe o gráfico
plt.show()
