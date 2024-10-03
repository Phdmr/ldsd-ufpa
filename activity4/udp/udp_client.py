# cliente_udp.py
"""import socket


def get_service_address(service_name):
    name_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name_server_socket.connect(
        ("192.168.100.6", 5050)
    )  # Mude o IP para o IP da maquina do servidor
    name_server_socket.send(service_name.encode())

    address = name_server_socket.recv(1024).decode()
    name_server_socket.close()
    ip, port = address.split(":")
    return ip, int(port)


def udp_client():
    ip, port = get_service_address("udp_service")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"Conectado ao servidor UDP em {ip}:{port}")

    while True:
        message = input("Digite a mensagem para o servidor UDP: ")
        client_socket.sendto(message.encode(), (ip, port))
        response = client_socket.recvfrom(1024)
        print(f"Resposta do servidor UDP: {response.decode()}")


if __name__ == "__main__":
    udp_client()
"""
import socket


def get_service_address(service_name):
    name_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name_server_socket.connect(
        ("192.168.100.6", 5050)
    )  # IP e porta do servidor de nomes
    name_server_socket.send(service_name.encode("utf-8"))

    response = name_server_socket.recv(1024).decode("utf-8")
    name_server_socket.close()

    ip, port = response.split(":")
    return ip, int(port)


def start_udp_client():
    ip, port = get_service_address("udp_service")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Configura um timeout de 5 segundos para o socket UDP
    client_socket.settimeout(5.0)

    print(f"Conectado ao servidor UDP em {ip}:{port}")

    try:
        # Enviar mensagem para o servidor UDP
        client_socket.sendto(b"Oi, servidor UDP!", (ip, port))

        # Tentar receber a resposta do servidor
        response, addr = client_socket.recvfrom(1024)
        print(f"Resposta do servidor: {response.decode('utf-8')}")

    except socket.timeout:
        print("Timeout: O servidor UDP não respondeu.")

    finally:
        # Fechar o socket após a operação
        client_socket.close()


if __name__ == "__main__":
    start_udp_client()
