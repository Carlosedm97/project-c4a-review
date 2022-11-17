package main.beseguridadspringboot.Repositorios;

import main.beseguridadspringboot.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioRol extends MongoRepository<Rol, String> {
}