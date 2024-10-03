import socket
import threading


def handle_client(client_socket, addr):
    print(f"Cliente conectado: {addr}")
    client_socket.send(b"Bem-vindo ao servidor TCP!")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Recebido de {addr}: {data.decode('utf-8')}")
        client_socket.send(b"Recebido")

    client_socket.close()


def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 9090))
    server_socket.listen(5)
    print("Servidor TCP rodando na porta 9090...")

    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, addr)
        )
        client_thread.start()


if __name__ == "__main__":
    start_tcp_server()
