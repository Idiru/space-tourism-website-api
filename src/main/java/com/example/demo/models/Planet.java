package com.example.demo.models;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class Planet {
    private Long id;
    private String name;
    private String description;
    private double range;  // en km
    private double travelTime;  // en jours
}
