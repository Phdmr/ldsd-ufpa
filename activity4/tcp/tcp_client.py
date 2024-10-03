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


def start_tcp_client():
    ip, port = get_service_address("tcp_service")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    print(f"Conectado ao servidor TCP em {ip}:{port}")

    client_socket.send(b"Oi servidor TCP!")
    response = client_socket.recv(1024)
    print(f"Resposta do servidor: {response.decode('utf-8')}")

    client_socket.close()


if __name__ == "__main__":
    start_tcp_client()
