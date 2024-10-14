#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <math.h>

#define NUM_THREADS 5

// Estrutura para passar múltiplos argumentos para a função da thread
typedef struct {
    int id;     // ID da thread
    int start;  // Início do intervalo
    int end;    // Fim do intervalo
} ThreadData;

//Mutex para sincronizar a saida
pthread_mutex_t mutex; 

// Função para imprimir números em uma faixa
void* print_numbers(void* arg) {
    ThreadData* data = (ThreadData*) arg;
    int id = data->id;
    int start = data->start;
    int end = data->end;

    pthread_mutex_lock(&mutex); // Bloquear o mutex antes de imprimir
    printf("Thread %d imprimindo de %d a %d:\n", id, start, end);
    for (int i = start; i <= end; i++) {
        printf("%d ", i);
    }
    printf("\n");
    pthread_mutex_unlock(&mutex);  // Desbloquear o mutex após a impressão

    pthread_exit(NULL);
}

// Função para encontrar e imprimir números primos
void* find_primes(void* arg) {
    ThreadData* data = (ThreadData*) arg;
    int start = data->start;
    int end = data->end;
    
    pthread_mutex_lock(&mutex); // Bloquear o mutex antes de imprimir
    printf("\nThread 5 (primos) encontrando números primos entre %d e %d:\n", start, end);
    for (int num = start; num <= end; num++) {
        if (num > 1) {
            int is_prime = 1;
            for (int i = 2; i <= sqrt(num); i++) {
                if (num % i == 0) {
                    is_prime = 0;
                    break;
                }
            }
            if (is_prime) {
                printf("%d ", num);
            }
        }
    }
    printf("\n");
    pthread_mutex_unlock(&mutex);  // Desbloquear o mutex após a impressão

    pthread_exit(NULL);
}

int main() {
    int number;
    printf("Digite o número até onde a sequência deve ir: ");
    scanf("%d", &number);

    pthread_t threads[NUM_THREADS];
    ThreadData thread_data[NUM_THREADS];  // Para armazenar dados de cada thread

    // Inicializar o Mutex
    pthread_mutex_init(&mutex, NULL);

    // Cálculo do intervalo base e do resto
    int base_step = number / 4;
    int remainder = number % 4;

    // Definir os intervalos e distribuir o resto
    int start = 1;
    for (int i = 0; i < 4; i++) {
        int end = start + base_step - 1;
        if (i < remainder) {
            end += 1; // Distribuir o restante entre as primeiras threads
        }
        thread_data[i].id = i + 1;
        thread_data[i].start = start;
        thread_data[i].end = end;
        start = end + 1;
    }

    // Inicializar o mutex
    pthread_mutex_init(&mutex, NULL);

    // Criar 4 threads para imprimir números
    for (int i = 0; i < 4; i++) {
        pthread_create(&threads[i], NULL, print_numbers, (void*) &thread_data[i]);
    }

    // Esperar as 4 threads terminarem
    for (int i = 0; i < 4; i++) {
        pthread_join(threads[i], NULL);
    }

    // Criar a 5ª thread para encontrar números primos
    thread_data[4].id = 5;
    thread_data[4].start = 1;
    thread_data[4].end = number;
    pthread_create(&threads[4], NULL, find_primes, (void*) &thread_data[4]);

    // Esperar a 5ª thread terminar
    pthread_join(threads[4], NULL);

    //Destruir mutex
    pthread_mutex_destroy(&mutex);

    getchar(); // Consome o caracter de pular linha que está no buffer do scanf
    printf("Pressione qualquer tecla para sair...\n");
    getchar();  // Espera o usuário pressionar Enter

    return 0;
}
