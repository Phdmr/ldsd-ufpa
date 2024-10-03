# cliente_udp.py
import socket


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

    while True:
        message = input("Digite a mensagem para o servidor UDP: ")
        client_socket.sendto(message.encode(), (ip, int(port)))
        response, _ = client_socket.recvfrom(1024)
        print(f"Resposta do servidor UDP: {response.decode()}")


if __name__ == "__main__":
    udp_client()
