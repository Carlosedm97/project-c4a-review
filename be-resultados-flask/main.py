from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

# Variables globales.

from Controladores.PartidoControlador import PartidoControlador
miControladorPartido = PartidoControlador()

from Controladores.CandidatoControlador import CandidatoControlador
miControladorCandidato = CandidatoControlador()

from Controladores.MesaControlador import MesaControlador
miControladorMesa = MesaControlador()

from Controladores.ResultadoControlador import ResultadoControlador
miControladorResultado = ResultadoControlador()


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

# EndPoints Mesa.

@app.route("/mesas", methods=['POST']) # Metodo para crear una mesa.
def crearMesa():
    data = request.get_json()
    json = miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesas", methods=['GET']) # Metodo para listar todas las mesas.
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['GET']) # Metodo para listar una mesa.
def getMesa(id):
    json = miControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['PUT']) # Metodo para actualizar una mesa.
def modificarMesa(id):
    data = request.get_json()
    json = miControladorMesa.update(id, data)
    return jsonify(json)

@app.route("/mesas/<string:id>", methods=['DELETE']) # Metodo para eliminar una mesa.
def eliminarMesa(id):
    json = miControladorMesa.delete(id)
    return jsonify(json)

# EndPoints Resultados.

@app.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=['POST']) # Metodo para crear un resultado.
def crearResultado(id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.create(data, id_mesa, id_candidato)
    return jsonify(json)

@app.route("/resultados", methods=['GET']) # Metodo para listar todos los resultados.
def getResultados():
    json = miControladorResultado.index()
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['GET']) # Metodo para listar un resultado.
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)

@app.route("/resultados/<string:id>/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=['PUT']) # Metodo para actualizar un resultado.
def modificarResultado(id, id_mesa, id_candidato):
    data = {}
    json = miControladorResultado.update(id, data, id_mesa, id_candidato)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['DELETE']) #Metodo para eliminar un resultado.
def eliminarResultado(id):
    json = miControladorResultado.delete(id)
    return jsonify(json)

@app.route("/resultados/candidato/<string:id_candidato>",methods=['GET'])
def resultadosDeCandidatos(id_candidato):
    json=miControladorResultado.listarResultadoDeCandidato(id_candidato)
    return jsonify(json)

@app.route("/resultados/mesa/<string:id_mesa>", methods=["GET"]) # Metodo para buscar los candidatos votados en una mesa.
def inscritosMesa(id_mesa):
    json = miControladorResultado.getListarCandidatosMesa(id_mesa)
    return jsonify(json)

@app.route("/resultados/mesas/<string:id_candidato>", methods=["GET"]) # Metodo para buscar el candidato en las mesas.
def inscritoEnMesas(id_candidato):
    json = miControladorResultado.getListarMesasDeInscritoCandidato(id_candidato)
    return jsonify(json)

@app.route("/resultados/maxdocument", methods=["GET"]) # Método para buscar el total de votos en una mesa.
def getMaxDocument():
    json = miControladorResultado.getMayorCedula()
    return jsonify(json)


# Prueba del servicio.

@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

if __name__ == "__main__":
    app.run(debug=False, port=9000)   