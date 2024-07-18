#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

"""
SRP": "Single Responsability Principle" Significa en español Principio de responsabilidad unica. 

>>> Este principio dice que una clase debe tener una sola responsabilidad y no muchas responsabilidades.

>>> Este principio evita que los desarrolladores creen clases con muchas responsabilidades y que sean dificiles de mantener y de entender.
"""


class TanqueCombustible:
    def __init__(self: 'TanqueCombustible') -> None:
        self.combustible: int = 100
        return None

    def agregarCombustible(self: 'TanqueCombustible', cantidad: int) -> None:
        self.combustible += cantidad
        return None

    def obtenerCombustible(self: 'TanqueCombustible') -> int:
        return self.combustible

    def usarCombustible(self: 'TanqueCombustible', cantidad: int) -> None:
        self.combustible -= cantidad
        return None

class Auto:
    def __init__(self: 'Auto', tanque: 'TanqueCombustible') -> None:
        self.posicion: int = 0
        self.tanque: 'TanqueCombustible' = tanque
        return None

    def mover(self: 'Auto', distancia: int) -> str:
        if self.tanque.obtenerCombustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usarCombustible(cantidad = distancia // 2)
            return "Has movido el auto exitosamente"
        else:
            return "No hay suficiente combustible"

    def obtenerPosicion(self: 'Auto') -> int:
        return self.posicion


tanque: TanqueCombustible = TanqueCombustible()
mi_auto: Auto = Auto(tanque = tanque)
print(mi_auto.obtenerPosicion(),end="\n", file = stdout)

print(mi_auto.mover(distancia = 10),end="\n", file = stdout)

print(mi_auto.obtenerPosicion(),end="\n", file = stdout)

print(mi_auto.mover(distancia = 20),end="\n", file = stdout)

print(mi_auto.obtenerPosicion(),end="\n", file = stdout)

print(mi_auto.mover(distancia = 60),end="\n", file = stdout)

print(mi_auto.obtenerPosicion(),end="\n", file = stdout)

print(mi_auto.mover(distancia = 100),end="\n", file = stdout)

print(mi_auto.obtenerPosicion(),end="\n", file = stdout)

print(mi_auto.mover(distancia = 100),end="\n", file = stdout)

print(mi_auto.obtenerPosicion(),end="\n", file = stdout)
