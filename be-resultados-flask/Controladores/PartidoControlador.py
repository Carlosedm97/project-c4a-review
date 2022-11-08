from Repositorios.PartidoRepositorio import PartidoRepositorio
from Modelos.Partido import Partido

class PartidoControlador():
    def __init__(self): 
        self.repositorioPartido = PartidoRepositorio()

    def index(self): # Devuelve todos los documentos de la colección.
        return self.repositorioPartido.findAll()

    def create(self,infoPartido): # Crea documentos.
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self,id): # Muestra un documento.
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__
        
    def update(self,id,infoPartido): # Actualizar un documento.
         partidoActual = Partido(self.repositorioPartido.findById(id))
         partidoActual.nombre = infoPartido["nombre"]
         partidoActual.lema = infoPartido["lema"]
         return self.repositorioPartido.save(partidoActual)

    def delete(self,id): # Elimina un documento.
        return self.repositorioPartido.delete(id)