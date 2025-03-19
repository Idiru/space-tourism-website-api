package com.example.demo.models;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class Astronaut {
    private Long id;
    private String name;
    private String job;
    private String bio;
}
