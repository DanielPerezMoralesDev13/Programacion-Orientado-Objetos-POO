#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

from typing import Callable
def decoradorOne(funcion: Callable) -> Callable:
    def funcionInterna() -> None:
        print("Decorador 1 antes de la ejecución de la función")
        funcion()
        print("Decorador 1 después de la ejecución de la función")
        return None
    return funcionInterna


def decoradorTwo(funcion: Callable) -> Callable:
    def funcionInterna() -> None:
        print("Decorador 2 antes de la ejecución de la función")
        funcion()
        print("Decorador 2 después de la ejecución de la función")
        return None

    return funcionInterna


@decoradorOne
@decoradorTwo
def saludo() -> None:
    print("¡Hola!")
    return None

saludo()

"""
saludo está decorado con @decoradorOne y @decoradorTwo, la salida completa será:

>>> Decorador 1 antes de la ejecución de la función
>>> Decorador 2 antes de la ejecución de la función
>>> ¡Hola!
>>> Decorador 2 después de la ejecución de la función
>>> Decorador 1 después de la ejecución de la función

La salida que ves es el resultado de aplicar dos decoradores, decoradorOne y decoradorTwo, a la función saludo. Los decoradores en Python se aplican de abajo hacia arriba. Por lo tanto, primero se aplica decoradorTwo, luego decoradorOne.

Cuando llamas a la función saludo(), esto es lo que sucede:

Debido al decorador decoradorOne, se imprime "Decorador 1 antes de la ejecución de la función".

Luego, se llama a la función saludo. Pero saludo ha sido decorada con decoradorTwo, por lo que en lugar de ejecutar saludo directamente, se ejecuta el código del decorador decoradorTwo.

Dentro de decoradorTwo, se imprime "Decorador 2 antes de la ejecución de la función", luego se ejecuta la función original saludo (que imprime "¡Hola!"), y finalmente se imprime "Decorador 2 después de la ejecución de la función".

Después de que se completa la ejecución de decoradorTwo y saludo, se vuelve al decorador decoradorOne, donde se imprime "Decorador 1 después de la ejecución de la función".


Se puedes aplicar tantos decoradores como desees a una función en Python.
"""
