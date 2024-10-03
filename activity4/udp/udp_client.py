# cliente_udp.py
import socket


def get_service_address(service_name):
    # Conecta ao servidor de nomes e obtém o endereço do serviço
    name_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name_server_socket.connect(
        ("192.168.100.6", 5050)  # Mude o IP para o IP da máquina do servidor
    )
    name_server_socket.send(service_name.encode())

    address = name_server_socket.recv(1024).decode()
    name_server_socket.close()
    ip, port = address.split(":")
    return ip, int(port)


def udp_client():
    ip, port = get_service_address("udp_service")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define o tempo limite para não ficar preso esperando
    client_socket.settimeout(5)  # Timeout de 5 segundos para receber resposta

    print(f"Conectado ao servidor UDP em {ip}:{port}")

    while True:
        message = input(
            "Digite a mensagem para o servidor UDP (ou 'sair' para encerrar): "
        )
        if message.lower() == "sair":
            print("Encerrando o cliente.")
            break

        # Envia a mensagem ao servidor
        client_socket.sendto(message.encode(), (ip, port))

        try:
            # Recebe a resposta do servidor (se houver)
            response, addr = client_socket.recvfrom(1024)
            print(f"Resposta do servidor UDP: {response.decode()}")
        except socket.timeout:
            print("Nenhuma resposta recebida dentro do tempo limite.")

    client_socket.close()


if __name__ == "__main__":
    udp_client()
