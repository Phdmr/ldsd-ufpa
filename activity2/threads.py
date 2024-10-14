import threading


# Função que imprime uma faixa de números
def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i, end=" ")
    print()


# Função que encontra e imprime números primos
def find_primes(start, end):
    print(f"\nNúmeros primos entre {start} e {end}: ", end="")
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")
    print()


# Função principal
def main():
    # Entrada do usuário
    number = int(input("Digite o número até onde a sequência deve ir: "))

    # Cálculo do intervalo base e do resto
    base_step = number // 4
    remainder = number % 4

    # Definir os intervalos para as threads
    ranges = []
    start = 1
    for i in range(4):
        end = start + base_step - 1
        if i < remainder:  # Distribuir o restante entre as primeiras threads
            end += 1
        ranges.append((start, end))
        start = end + 1

    # Criar e iniciar as 4 threads para imprimir números
    threads = []
    for start, end in ranges:
        t = threading.Thread(target=print_numbers, args=(start, end))
        threads.append(t)
        t.start()

    # Esperar todas as threads terminarem
    for t in threads:
        t.join()

    # Criar e iniciar a 5ª thread para encontrar números primos
    prime_thread = threading.Thread(target=find_primes, args=(1, number))
    prime_thread.start()
    prime_thread.join()


if __name__ == "__main__":
    main()
