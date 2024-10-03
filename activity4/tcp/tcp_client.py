import socket


def get_service_address(service_name):
    name_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name_server_socket.connect(
        ("192.168.100.6", 5050)
    )  # Mude o IP para o IP da máquina do servidor
    name_server_socket.send(service_name.encode())

    address = name_server_socket.recv(1024).decode()
    name_server_socket.close()

    ip, port = address.split(":")
    return ip, int(port)


def tcp_client():
    ip, port = get_service_address("tcp_service")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, int(port)))

    print(f"Conectado ao servidor TCP em {ip}:{port}")

    while True:
        message = input(
            "Digite a mensagem para o servidor TCP (ou 'sair' para encerrar): "
        )
        if message.lower() == "sair":
            print("Encerrando o cliente.")
            break  # Encerra o loop se o usuário digitar 'sair'

        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Resposta do servidor TCP: {response}")

    client_socket.close()  # Fechar o socket ao encerrar


if __name__ == "__main__":
    tcp_client()
