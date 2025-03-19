package com.example.demo.controllers;

import com.example.demo.models.*;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "*")  // Permet au frontend d'accéder à l'API
@RestController
@RequestMapping("/api/content")
public class ContentController {

    // Contenu de la page d'accueil
    @GetMapping("/homepage")
    public HomepageContent getHomepageContent() {
        return new HomepageContent(
            "Bienvenue dans l'Espace !",
            "Explorez les mystères de l'univers.",
            "Découvrez des informations fascinantes sur les planètes, les astronautes et les technologies qui nous permettent d'explorer le cosmos."
        );
    }

    // Liste des planètes
    @GetMapping("/planets")
    public List<Planet> getPlanets() {
        return List.of(
            new Planet(1L, "Terre", "Notre planète bleue.", 12742, 3000),
            new Planet(2L, "Mars", "La planète rouge.", 6779, 4000),
            new Planet(3L, "Jupiter", "La plus grande planète du système solaire.", 139820, 5000)
        );
    }

    // Liste des astronautes
    @GetMapping("/astronauts")
    public List<Astronaut> getAstronauts() {
        return List.of(
            new Astronaut(1L, "Neil Armstrong", "Boss", "Premier homme sur la Lune."),
            new Astronaut(2L, "Youri Gagarine", "Boss", "Premier homme dans l'espace."),
            new Astronaut(3L, "Thomas Pesquet", "Boss", "Astronaute français de l'ESA.")
        );
    }

    // Liste des technologies
    @GetMapping("/technologies")
    public List<Technology> getTechnologies() {
        return List.of(
            new Technology(1L, "Propulsion Ionique", "Utilisée pour les sondes spatiales."),
            new Technology(2L, "GPS Spatial", "Navigation précise pour les satellites."),
            new Technology(3L, "Radiofréquence", "Communication avec les astronautes.")
        );
    }
}
