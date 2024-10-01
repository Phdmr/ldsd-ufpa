# Servidor de nomes simples

import socket

# Dicionário para armazenar nomes e endereços de serviços
SERVICES = {"tcp_service": ("localhost", 8080), "udp_service": ("localhost", 8081)}


def name_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9090))
    server_socket.listen(5)
    print("Servidor de Nomes rodando na porta 9090...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Solicitação recebida de: {addr}")

        service_name = client_socket.recv(1024).decode()
        if service_name in SERVICES:
            service_address = f"{SERVICES[service_name][0]}:{SERVICES[service_name][1]}"
            client_socket.send(service_address.encode())
        else:
            client_socket.send(b"Servico nao encontrado.")
        client_socket.close()


if __name__ == "__main__":
    name_server()
