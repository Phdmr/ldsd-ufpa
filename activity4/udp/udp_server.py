# servidor_udp.py
import socket


def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 8081))
    print("Servidor UDP rodando na porta 8081...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Recebido de {addr}: {data.decode()}")
        server_socket.sendto(b"Mensagem recebida.", addr)


if __name__ == "__main__":
    udp_server()
