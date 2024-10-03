import socket


def start_name_server():
    # Mapeamento de nome de serviço para IP e porta
    services = {
        "tcp_service": ("192.168.100.6", 9090),
        "udp_service": ("192.168.100.6", 9091),
    }

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 5050))  # Porta do servidor de nomes
    server_socket.listen(5)
    print("Servidor de Nomes rodando na porta 5050...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão recebida de {addr}")

        # Receber o nome do serviço
        service_name = client_socket.recv(1024).decode("utf-8")

        if service_name in services:
            ip, port = services[service_name]
            client_socket.send(f"{ip}:{port}".encode("utf-8"))
        else:
            client_socket.send(b"Servico nao encontrado.")

        client_socket.close()


if __name__ == "__main__":
    start_name_server()
