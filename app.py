from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "mensagem": "API de chamados em funcionamento"
    })