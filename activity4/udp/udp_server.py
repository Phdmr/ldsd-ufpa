# servidor_udp.py
import socket


def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("0.0.0.0", 9091))
    print("Servidor UDP rodando na porta 9091...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Recebido de {addr}: {data.decode('utf-8')}")

        # Enviar resposta de volta para o cliente
        server_socket.sendto(b"Mensagem recebida pelo servidor UDP", addr)


if __name__ == "__main__":
    start_udp_server()
