#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

"""
Los getters y setters son métodos que nos permiten acceder y modificar atributos privados de una clase.
"""


class Persona:
    def __init__(self: 'Persona', nombre: str, edad: int) -> None:
        self.__nombre: str = nombre
        self.__edad: int = edad
        return None

    # Getters para obtener los valores de los atributos privados
    def getNombre(self: 'Persona') -> str:
        return self.__nombre

    def getEdad(self: 'Persona') -> int:
        return self.__edad

    # Setters para modificar los valores de los atributos privados
    def setNombre(self: 'Persona', nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre
        return None
    
    def setEdad(self: 'Persona', nueva_edad: int) -> None:
        self.__edad = nueva_edad
        return None


Daniel: Persona = Persona(nombre="Daniel", edad=20)

# Getters para obtener los valores de los atributos privados
print(Daniel.getNombre(),end="\n", file = stdout)

# Setters para modificar los valores de los atributos privados

# Forma correcta para modificar los atributos privados
Daniel.setNombre(nuevo_nombre="Benjamin")

Daniel.__nombre = "Benjamin" # No se puede modificar el atributo privado de esta forma
print(Daniel.getNombre(),end="\n", file = stdout)
