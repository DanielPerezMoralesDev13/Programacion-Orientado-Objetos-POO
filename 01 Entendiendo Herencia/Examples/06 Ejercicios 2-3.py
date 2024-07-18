#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

"""
Ejercicio de herencia multiple y MRO:

Imagina que estas modelando animales en un zoológico. Crear tres clases: "Animal", "Mamifero" y "Ave". La clase "Animal debe tener un metodo llamado "comer". La clase  "Mamifero" debe tener un metodo llamado "amamantar" y la clase "Ave" un metodo llamado "Volar" 

Ahora, crea un clase "Murcielago" que herede de "Mamifero" y "Ave", en ese orden, y por lo tanto debe ser capaz de "amamantar" y "volar", ademas de "comer".

Finalmente, juega con el orden de herencia y observa como cambia el comportamiento el MRO y el comportamiento de los métodos al usar super().
"""


class Animal:
    def __init__(self: 'Animal') -> None:
        return None

    def Comer(self: 'Animal') -> str:
        return "Comiendo"

class Mamifero(Animal):
    def __init__(self: 'Mamifero') -> None:
        return None

    def Amamantar(self: 'Mamifero') -> str:
        return "Amamantando"


class Ave(Animal):
    def __init__(self: 'Ave') -> None:
        return None

    def Volar(self: 'Ave') -> str:
        return "Volando"

class Murcielago(Mamifero,Ave):
    def __init__(self: 'Murcielago') -> None:
        super().__init__()
        return None

Murcielagito: Murcielago = Murcielago()

print(Murcielagito.Comer(),end="\n", file = stdout)
print(Murcielagito.Amamantar(),end="\n", file = stdout)
print(Murcielagito.Volar(),end="\n", file = stdout)