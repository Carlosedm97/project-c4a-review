package main.beseguridadspringboot.Controladores;

import main.beseguridadspringboot.Modelos.Rol;
import main.beseguridadspringboot.Repositorios.RepositorioRol;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/roles")
public class ControladorRol {
    @Autowired
    private RepositorioRol miRepositorioRol;

    @GetMapping("") // Método para listar todos los roles.
    public List<Rol> index(){
        return miRepositorioRol.findAll();
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping // Método para crear un rol.
    public Rol create(@RequestBody Rol infoRol){
        return miRepositorioRol.save(infoRol);
    }

    @GetMapping("{id}") // Método para listar un rol por identificador.
    public Rol show(@PathVariable String id){
        Rol rolActual = miRepositorioRol
                .findById(id)
                .orElse(null);
        return rolActual;
    }

    @PutMapping("{id}") // Método para actualizar un rol.
    public Rol update(@PathVariable String id, @RequestBody Rol infoRol){
        Rol rolActual = miRepositorioRol
                .findById(id)
                .orElse(null);
        if (rolActual != null){
           rolActual.setNombre(infoRol.getNombre());
           rolActual.setDescripcion(infoRol.getDescripcion());
           return miRepositorioRol.save(rolActual);
        }else{
           return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}") // Método para eliminar un rol.
    public void delete(@PathVariable String id){
        Rol rolActual = miRepositorioRol
                .findById(id)
                .orElse(null);
        if (rolActual != null){
            miRepositorioRol.delete(rolActual);
        }
    }
}