#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h> 

#define TAMANHO_STRING 190
#define NUM_EXECUCOES 5

int main()
{
    const char *letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    double tempos[NUM_EXECUCOES];
    int n = TAMANHO_STRING;

    // Inicializa o gerador de números aleatórios
    srand((unsigned int)time(NULL));

    // Gera a string aleatória apenas uma vez
    char S_original[TAMANHO_STRING + 1];
    for (int i = 0; i < n; i++)
    {
        S_original[i] = letras[rand() % 26];
    }
    S_original[n] = '\0'; // Finaliza com caractere nulo

    printf("String utilizada: %s\n\n", S_original);

    // Executa o algoritmo NUM_EXECUCOES vezes com a mesma string
    for (int execucao = 1; execucao <= NUM_EXECUCOES; execucao++)
    {
        char S[TAMANHO_STRING + 1];
        strcpy(S, S_original); // Copia a string original para uso nesta execução

        char longest[TAMANHO_STRING + 1] = "";

        clock_t inicio = clock(); // Início da medição de tempo

        // Algoritmo força bruta para encontrar o LRS
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j <= n; j++)
            {
                int len_sub = j - i;
                char substring[TAMANHO_STRING + 1];
                strncpy(substring, S + i, len_sub);
                substring[len_sub] = '\0';

                int count = 0;
                for (int k = 0; k <= n - len_sub; k++)
                {
                    if (strncmp(S + k, substring, len_sub) == 0)
                    {
                        count++;
                    }
                }

                if (count > 1 && len_sub > strlen(longest))
                {
                    strcpy(longest, substring);
                }
            }
        }

        clock_t fim = clock(); // Fim da medição de tempo
        double tempo_execucao = (double)(fim - inicio) / CLOCKS_PER_SEC;
        tempos[execucao - 1] = tempo_execucao;

        printf("[%d] Tempo: %.4f segundos | Substring mais longa: %s\n",
               execucao, tempo_execucao, longest);
    }

    // Cálculo da média
    double soma = 0.0;
    for (int i = 0; i < NUM_EXECUCOES; i++)
    {
        soma += tempos[i];
    }
    double media = soma / NUM_EXECUCOES;

    // Cálculo do desvio padrão
    double soma_quadrados = 0.0;
    for (int i = 0; i < NUM_EXECUCOES; i++)
    {
        soma_quadrados += (tempos[i] - media) * (tempos[i] - media);
    }
    double desvio_padrao = sqrt(soma_quadrados / (NUM_EXECUCOES - 1));

    // Exibição dos resultados
    printf("\nTempo médio de execução (%d execuções): %.4f segundos\n",
           NUM_EXECUCOES, media);
    printf("Desvio padrão: %.4f segundos\n", desvio_padrao);

    return 0;
}
