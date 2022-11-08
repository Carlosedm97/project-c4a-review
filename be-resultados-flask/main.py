from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

from Controladores.PartidoControlador import PartidoControlador
miControladorPartido = PartidoControlador()

from Controladores.CandidatoControlador import CandidatoControlador
miControladorCandidato = CandidatoControlador()

# EndPoints Partido.

@app.route("/partidos", methods=['POST']) # Metodo para crear un partido.
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos", methods=['GET']) # Metodo para listar todos los partidos.
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['GET']) # Metodo para listar un documento.
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['PUT']) # Metodo para actualizar un partido.
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id,data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['DELETE']) #Metodo para eliminar un partido.
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

# EndPoints Candidato.

@app.route("/candidatos", methods=['POST']) # Metodo para crear un candidato.
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidatos", methods=['GET']) # Metodo para listar todos los candidatos.
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['GET']) # Metodo para listar un documento.
def getCandidato(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['PUT']) # Metodo para actualizar un candidato.
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id,data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['DELETE']) # Metodo para eliminar un candidato.
def eliminarCandidato(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>/partido/<string:id_partido>", methods=['PUT']) # Metodo para agregar un candidato a un partido.
def asignarPartidoACandidato(id,id_partido):
    json = miControladorCandidato.asignarPartido(id,id_partido)
    return jsonify(json)

# Prueba del servicio.

@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

if __name__ == "__main__":
    app.run(debug=False, port=9000)   