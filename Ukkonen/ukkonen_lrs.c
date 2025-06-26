/*
 * Implementação em C do Algoritmo de Ukkonen para construção de Árvore de Sufixos
 * Inclui terminador '$' para distinguir sufixos e função de impressão hierárquica.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CHAR 256

// Estrutura de nó na árvore de sufixo
typedef struct SuffixNode {
    struct SuffixNode *children[MAX_CHAR];
    struct SuffixNode *suffixLink;
    int start;
    int *end; // ponteiro para fim da aresta
} SuffixNode;

// Globais
char *text;
SuffixNode *root = NULL;
SuffixNode *lastNewNode = NULL;
SuffixNode *activeNode = NULL;
int activeEdge = -1;
int activeLength = 0;
int remainingSuffixCount = 0;
int leafEnd = -1;
int *rootEnd = NULL;

// Protótipos
SuffixNode *newNode(int start, int *end);
int edgeLength(SuffixNode *n);
int walkDown(SuffixNode *curr);
void extendSuffixTree(int pos);
void buildSuffixTree();
void printTree(SuffixNode *n, int depth);
void freeTree(SuffixNode *n);

// Cria novo nó
SuffixNode *newNode(int start, int *end) {
    SuffixNode *node = malloc(sizeof(SuffixNode));
    for (int i = 0; i < MAX_CHAR; i++) node->children[i] = NULL;
    node->suffixLink = root;
    node->start = start;
    node->end = end;
    return node;
}

// Comprimento da aresta
int edgeLength(SuffixNode *n) {
    return *(n->end) - n->start + 1;
}

// Caminha pelo active point
int walkDown(SuffixNode *curr) {
    if (activeLength >= edgeLength(curr)) {
        activeEdge += edgeLength(curr);
        activeLength -= edgeLength(curr);
        activeNode = curr;
        return 1;
    }
    return 0;
}

// Estende a árvore
void extendSuffixTree(int pos) {
    leafEnd = pos;
    remainingSuffixCount++;
    lastNewNode = NULL;

    while (remainingSuffixCount > 0) {
        if (activeLength == 0)
            activeEdge = pos;
        int idx = (unsigned char)text[activeEdge];
        if (!activeNode->children[idx]) {
            activeNode->children[idx] = newNode(pos, &leafEnd);
            if (lastNewNode) { lastNewNode->suffixLink = activeNode; lastNewNode = NULL; }
        } else {
            SuffixNode *next = activeNode->children[idx];
            if (walkDown(next)) continue;
            if (text[next->start + activeLength] == text[pos]) {
                if (lastNewNode && activeNode != root) { lastNewNode->suffixLink = activeNode; lastNewNode = NULL; }
                activeLength++;
                break;
            }
            int *splitEnd = malloc(sizeof(int));
            *splitEnd = next->start + activeLength - 1;
            SuffixNode *split = newNode(next->start, splitEnd);
            activeNode->children[idx] = split;
            split->children[(unsigned char)text[pos]] = newNode(pos, &leafEnd);
            next->start += activeLength;
            split->children[(unsigned char)text[next->start]] = next;
            if (lastNewNode) lastNewNode->suffixLink = split;
            lastNewNode = split;
        }
        remainingSuffixCount--;
        if (activeNode == root && activeLength > 0) {
            activeLength--;
            activeEdge = pos - remainingSuffixCount + 1;
        } else if (activeNode != root) {
            activeNode = activeNode->suffixLink;
        }
    }
}

// Constrói a árvore (inclui '$')
void buildSuffixTree() {
    int n = strlen(text);
    rootEnd = malloc(sizeof(int)); *rootEnd = -1;
    root = newNode(-1, rootEnd);
    activeNode = root;
    for (int i = 0; i < n; i++) extendSuffixTree(i);
}

// Imprime a árvore hierarquicamente
void printTree(SuffixNode *n, int depth) {
    if (!n) return;
    if (n->start != -1) {
        int len = edgeLength(n);
        printf("%*s", depth*2, ""); // indent
        printf("|-- %.*s\n", len, text + n->start);
    }
    for (int i = 0; i < MAX_CHAR; i++) {
        if (n->children[i]) printTree(n->children[i], depth + 1);
    }
}

// Libera memória
void freeTree(SuffixNode *n) {
    if (!n) return;
    for (int i = 0; i < MAX_CHAR; i++) if (n->children[i]) freeTree(n->children[i]);
    if (n->start == -1) free(n->end);
    else if (n->end != &leafEnd) free(n->end);
    free(n);
}

int main() {
    // Inclui terminador único
    char input[] = "banana";
    int len = strlen(input);
    text = malloc(len + 2);
    strcpy(text, input);
    text[len] = '$';
    text[len+1] = '\0';

    printf("Construindo árvore de sufixo para: %s\n", text);
    buildSuffixTree();
    printf("\nÁrvore de sufixo (arestas):\n");
    printTree(root, 0);
    freeTree(root);
    free(text);
    return 0;
}
