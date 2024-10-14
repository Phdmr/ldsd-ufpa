from flask import Flask, send_file

app = Flask(__name__)


@app.route("/imagem")
def enviar_imagem():
    return send_file("imagem.jpg", mimetype="image/jpeg")


@app.route("/texto")
def enviar_texto():
    return send_file("arquivo.txt", mimetype="text/plain")


@app.route("/video")
def enviar_video():
    return send_file("video.mp4", mimetype="video/mp4")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
