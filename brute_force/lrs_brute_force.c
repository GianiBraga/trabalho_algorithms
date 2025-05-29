#include <stdio.h>     // Biblioteca padrão de entrada e saída
#include <stdlib.h>    // Para alocação dinâmica (malloc, calloc, free) e rand()
#include <string.h>    // Para funções de manipulação de strings (strlen, strcpy, strncpy, strstr)
#include <time.h>      // Para medir tempo de execução com clock()

#define TAMANHO_STRING 100    // Define o tamanho da string gerada aleatoriamente
#define NUM_EXECUCOES 5       // Define o número de execuções do teste para calcular tempo médio

// Função que gera uma string aleatória com letras maiúsculas
void gerar_string(char *str, int tamanho) {
    const char *letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";  // Alfabeto usado
    for (int i = 0; i < tamanho; i++) {
        str[i] = letras[rand() % 26];  // Seleciona um caractere aleatório de A-Z
    }
    str[tamanho] = '\0';  // Finaliza a string com caractere nulo
}

// Função que conta quantas vezes uma substring aparece dentro de uma string
int contar_ocorrencias(const char *str, const char *substr) {
    int count = 0;
    const char *p = str;

    // Enquanto encontrar a substring dentro da string principal
    while ((p = strstr(p, substr)) != NULL) {
        count++;     // Incrementa o contador
        p += 1;      // Avança um caractere (permite sobreposição de substrings)
    }
    return count;
}

int main() {
    srand((unsigned int)time(NULL));  // Inicializa o gerador de números aleatórios
    double tempos[NUM_EXECUCOES];     // Array para armazenar o tempo de cada execução
    char string_original[TAMANHO_STRING + 1];  // String que será analisada

    gerar_string(string_original, TAMANHO_STRING);  // Gera uma string aleatória
    int n = strlen(string_original);                // Armazena o tamanho da string

    // Repetição do algoritmo para múltiplas execuções (média de tempo)
    for (int execucao = 1; execucao <= NUM_EXECUCOES; execucao++) {
        // Inicializa a variável que irá armazenar a substring mais longa
        char *longest = calloc(n + 1, sizeof(char));  // Inicialmente vazia

        clock_t inicio = clock();  // Marca o tempo de início

        // Algoritmo de força bruta: percorre todas as substrings possíveis
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                int len = j - i;  // Comprimento da substring atual

                // Aloca memória e copia a substring de string_original[i:j]
                char *substring = (char *)malloc((len + 1) * sizeof(char));
                strncpy(substring, string_original + i, len);
                substring[len] = '\0';  // Finaliza a substring com '\0'

                // Conta quantas vezes essa substring aparece na string
                int count = contar_ocorrencias(string_original, substring);

                // Atualiza a "longest" se essa for maior e aparecer mais de uma vez
                if (count > 1 && len > strlen(longest)) {
                    strcpy(longest, substring);
                }

                free(substring);  // Libera a memória da substring temporária
            }
        }

        clock_t fim = clock();  // Marca o tempo de fim
        double tempo_execucao = ((double)(fim - inicio)) / CLOCKS_PER_SEC;  // Tempo em segundos
        tempos[execucao - 1] = tempo_execucao;  // Armazena o tempo da execução atual

        // Exibe o tempo e a maior substring repetida encontrada
        printf("[%d] Tempo: %.4f segundos | Substring mais longa: %s\n",
               execucao, tempo_execucao, longest);

        free(longest);  // Libera a memória da maior substring
    }

    // Calcula a média dos tempos de execução
    double soma = 0.0;
    for (int i = 0; i < NUM_EXECUCOES; i++) {
        soma += tempos[i];
    }
    double media = soma / NUM_EXECUCOES;

    // Exibe o tempo médio
    printf("\nTempo médio de execução (%d execuções): %.4f segundos\n", NUM_EXECUCOES, media);

    return 0;
}
