from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

from Controladores.PartidoControlador import PartidoControlador
miControladorPartido = PartidoControlador()

# EndPoints Partido.

@app.route("/partidos", methods=['GET']) # Metodo para listar todos los partidos.
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos", methods=['POST']) # Metodo para crear un partido.
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['GET']) # Metodo para listar un documento.
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['PUT']) # Metodo para actualizar un partido.
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['DELETE']) #Metodo para eliminar un partido.
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)


# Prueba del servicio.

@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

if __name__ == "__main__":
    app.run(debug=False, port=9000)   