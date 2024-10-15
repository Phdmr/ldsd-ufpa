import xmlrpc.client

# Solicita o IP do servidor
ip_servidor = input("Digite o IP do servidor (deixe vazio para localhost): ")
if not ip_servidor:
    ip_servidor = "localhost"
    print("Usando localhost como servidor.")

# Tenta se conectar ao servidor
try:
    # Cria o cliente que se conecta ao servidor RPC
    proxy = xmlrpc.client.ServerProxy(f"http://{ip_servidor}:8000")

    # Teste de conexão com a função ping
    resposta = proxy.ping()
    if resposta == "Pong!":
        print(f"Conexão estabelecida com o servidor {ip_servidor}!")
    else:
        raise Exception("Resposta inesperada do servidor.")
except Exception as e:
    print(f"Erro ao conectar ao servidor: {e}")
    exit(1)  # Encerra o programa se a conexão falhar


# Função para exibir o menu de operações
def menu():
    print("\nEscolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Encerrar conexão")
    return int(input("Digite o número da operação desejada: "))


# Função para coletar os dois números do usuário
def get_numbers():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    return x, y


# Loop principal do cliente
while True:
    try:
        escolha = menu()

        if escolha in [1, 2, 3, 4]:
            x, y = get_numbers()

            if escolha == 1:
                print(f"Resultado: {x} + {y} = {proxy.add(x, y)}")
            elif escolha == 2:
                print(f"Resultado: {x} - {y} = {proxy.subtract(x, y)}")
            elif escolha == 3:
                print(f"Resultado: {x} * {y} = {proxy.multiply(x, y)}")
            elif escolha == 4:
                print(f"Resultado: {x} / {y} = {proxy.divide(x, y)}")

        elif escolha == 5:
            # Encerrar a conexão com o servidor
            proxy.disconnect(ip_servidor)
            print("Conexão encerrada. Saindo do programa.")
            break

        else:
            print("Escolha inválida, tente novamente.")

    except Exception as e:
        print(f"Erro: {e}")

    continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
    if continuar != "s":
        proxy.disconnect(ip_servidor)
        print("Conexão encerrada. Saindo do programa.")
        break
