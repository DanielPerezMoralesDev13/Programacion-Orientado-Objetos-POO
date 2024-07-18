#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

"""
El metodo especial __add__ se usa para sobrecargar el operador + y se usa para sumar dos objetos y retornar un nuevo objeto con el resultado de la suma de los dos objetos que se sumaron. 
"""

class Persona:
    def __init__(self: 'Persona', nombre: str, edad: int) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        return None

    def __str__(self: 'Persona') -> str:
        return f"""Persona(
nombre: str ='{self.nombre}',
edad: int ={self.edad}
)"""

    # al usar repr() se puede usar eval() para crear un objeto
    # debe retornar un string que sea valido para crear un objeto el formato es el siguiente.

    # Clase(parametros) si el parametro es un string se debe usar comillas simples o dobles y si es un numero no se debe usar comillas
    def __repr__(self: 'Persona') -> str:
        return f"Persona('{self.nombre}', {self.edad})"

    def __add__(self: 'Persona', otro: 'Persona') -> 'Persona':
        nuevo_valor: int = self.edad + otro.edad
        # return f"{nuevo_valor}"
        return Persona(self.nombre + otro.nombre, nuevo_valor)


daniel: Persona = Persona(nombre="Daniel", edad=18)

neymar: Persona = Persona(nombre="Neymar", edad=32)

messi: Persona = Persona(nombre="Messi", edad=35)

nueva_persona: Persona = daniel + neymar + messi

print(nueva_persona,end="\n", file = stdout)

print(nueva_persona.nombre,end="\n", file = stdout)

print(nueva_persona.edad,end="\n", file = stdout)
