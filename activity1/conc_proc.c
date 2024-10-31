#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>

#define NUM_CHILDREN 5
#define RANGE 100

void write_to_file_and_screen(int start, int end, FILE *file, int process_num) {
    // Indica o número do processo e o intervalo no arquivo
    fprintf(file, "Processo %d (PID: %d) imprimindo range %d-%d: ", process_num, getpid(), start, end);
    printf("Processo %d (PID: %d) imprimindo range %d-%d: ", process_num, getpid(), start, end);

    for (int i = start; i <= end; i++) {
        fprintf(file, "%d ", i);  // Escreve no arquivo
        printf("%d ", i);         // Escreve na tela
    }
    fprintf(file, "\n");  // Nova linha no arquivo
    printf("\n");         // Nova linha na tela
}

int main() {
    pid_t pid;
    int start, end;
    FILE *file;

    // Abre o arquivo para escrita
    file = fopen("output.txt", "w");
    if (file == NULL) {
        perror("Erro ao abrir o arquivo");
        exit(EXIT_FAILURE);
    }

    printf("Iniciando criação de processos...\n");

    for (int i = 0; i < NUM_CHILDREN; i++) {
        start = i * RANGE + 1;
        end = (i + 1) * RANGE;

        pid = fork();  // Cria um processo filho

        if (pid < 0) {
            perror("Erro ao criar o processo filho");
            exit(EXIT_FAILURE);
        } else if (pid == 0) {
            // Código do processo filho
            printf("Processo filho %d iniciado, PID: %d\n", i + 1, getpid());
            write_to_file_and_screen(start, end, file, i + 1);
            printf("Processo filho %d finalizado, PID: %d\n", i + 1, getpid());
            fclose(file);
            exit(0);
        } else {
            // Código do processo pai
            printf("Processo pai aguardando o término do processo filho %d (PID: %d)\n", i + 1, pid);
            wait(NULL);  // Aguarda o processo filho terminar
            printf("Processo filho %d terminou.\n", i + 1);
        }
    }

    printf("Todos os processos filhos foram finalizados.\n");
    fclose(file);
    printf("Pressione qualquer tecla para sair...\n");
    getchar();  // Espera o usuário pressionar Enter
    return 0;
}
