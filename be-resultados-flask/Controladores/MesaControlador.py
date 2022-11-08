from Repositorios.MesaRepositorio import MesaRepositorio
from Modelos.Mesa import Mesa

class MesaControlador():

    def __init__(self):
        self.repositorioMesa = MesaRepositorio()

    def index(self):
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        nuevaMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesa):
         mesaActual = Mesa(self.repositorioMesa.findById(id))
         mesaActual.nro_mesa = infoMesa["nro_mesa"]
         mesaActual.nro_cedulas = infoMesa["nro_cedulas"]
         return self.repositorioMesa.save(mesaActual)

    def delete(self, id):
        return self.repositorioMesa.delete(id)