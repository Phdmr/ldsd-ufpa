# servidor_udp.py
import socket
import threading


def handle_udp_client(data, addr, server_socket):
    """Função para tratar cada mensagem de cliente UDP em uma thread separada"""
    print(f"Recebido de {addr}: {data.decode()}")
    server_socket.sendto(b"Mensagem recebida.", addr)


def udp_server():
    """Função principal do servidor UDP que aceita múltiplos clientes"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 8081))
    print("Servidor UDP rodando na porta 8081...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        # Inicia uma thread para tratar a mensagem recebida de um cliente
        client_thread = threading.Thread(
            target=handle_udp_client, args=(data, addr, server_socket)
        )
        client_thread.start()


if __name__ == "__main__":
    udp_server()
