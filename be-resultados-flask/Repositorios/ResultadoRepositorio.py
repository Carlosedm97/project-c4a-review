from Repositorios.InterfazRepositorio import IntefazRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId

class ResultadoRepositorio(IntefazRepositorio(Resultado)):
    def getListadoCandidatosInscritosMesa(self, id_mesa): # Me da las votaciones por mesa.
        theQuery = {"mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

    def getListadoMesasCandidatoInscrito(self, id_candidato): # Votaciones por candidato.
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)
    
    def getNumeroCedulaMayorCandidato(self):
        query = {
            "$group":{
                "_id": "$candidato",
                "max": {
                    "$max": "$cedula"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }

        pipeline = [query]
        return self.queryAggregation(pipeline)