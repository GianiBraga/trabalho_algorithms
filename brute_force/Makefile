# Nome do executável
EXEC = lrs_bf

# Nome do arquivo-fonte
SRC = lrs_brute_force.c

# Compilador
CC = gcc

# Flags de compilação
CFLAGS = -Wall -O2

# Regra padrão: compilar o código
all: $(EXEC)

$(EXEC): $(SRC)
	$(CC) $(CFLAGS) -o $(EXEC) $(SRC)

# Regra para limpar arquivos gerados (opcional)
clean:
	rm -f $(EXEC)
