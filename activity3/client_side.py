import requests
import os
import webbrowser


def baixar_arquivo(url, nome_arquivo):
    resposta = requests.get(url)
    with open(nome_arquivo, "wb") as f:
        f.write(resposta.content)
    print(f"{nome_arquivo} baixado com sucesso.")


def visualizar_arquivo(nome_arquivo):
    if nome_arquivo.endswith(".jpg") or nome_arquivo.endswith(".png"):
        # Abre a imagem no visualizador padrão do sistema
        os.system(
            f"xdg-open {nome_arquivo}"
            if os.name == "posix"
            else f"start {nome_arquivo}"
        )
    elif nome_arquivo.endswith(".txt"):
        # Abre o arquivo de texto no navegador ou editor de texto padrão
        webbrowser.open(nome_arquivo)
    elif nome_arquivo.endswith(".mp4"):
        # Abre o vídeo no reprodutor padrão do sistema
        os.system(
            f"xdg-open {nome_arquivo}"
            if os.name == "posix"
            else f"start {nome_arquivo}"
        )
    else:
        print("Formato de arquivo não suportado.")


def main():
    print("Escolha uma opção para visualizar:")
    print("1 - Imagem")
    print("2 - Texto")
    print("3 - Vídeo")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        url = "http://localhost:5000/imagem"
        nome_arquivo = "imagem.jpg"
    elif escolha == "2":
        url = "http://localhost:5000/texto"
        nome_arquivo = "arquivo.txt"
    elif escolha == "3":
        url = "http://localhost:5000/video"
        nome_arquivo = "video.mp4"
    else:
        print("Opção inválida!")
        return

    # Baixar e visualizar o arquivo escolhido
    baixar_arquivo(url, nome_arquivo)
    visualizar_arquivo(nome_arquivo)


if __name__ == "__main__":
    main()
