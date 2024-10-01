# cliente_tcp.py
import socket


def get_service_address(service_name):
    name_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name_server_socket.connect(("localhost", 9090))
    name_server_socket.send(service_name.encode())

    address = name_server_socket.recv(1024).decode()
    name_server_socket.close()
    return address


def tcp_client():
    service_address = get_service_address("tcp_service")
    ip, port = service_address.split(":")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, int(port)))

    while True:
        message = input("Digite a mensagem para o servidor TCP: ")
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Resposta do servidor TCP: {response}")


if __name__ == "__main__":
    tcp_client()
