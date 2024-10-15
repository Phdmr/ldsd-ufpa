from xmlrpc.server import SimpleXMLRPCServer

# Funções remotas
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida"
    return x / y

# Função para se desconectar do cliente
def disconnect(client_ip):
    print(f"Cliente {client_ip} se desconectou.")
    return True

# Função para testar a conexão
def ping():
    return "Pong!"

# Criação do servidor na porta 8000
ip_servidor = input("Digite o ip desta máquina (se vazio, será usado localhost): ")
if not ip_servidor:
    ip_servidor = "localhost"
    print("Usando localhost")
server = SimpleXMLRPCServer((f"{ip_servidor}", 8000))
print("Servidor RPC disponível na porta 8000...")

# Registra funções
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")
server.register_function(disconnect, "disconnect")
server.register_function(ping, "ping")  # Adiciona função de teste de conexão

# Inicia o servidor
server.serve_forever()
