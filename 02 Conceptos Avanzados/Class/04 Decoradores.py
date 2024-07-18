#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

from typing import Callable
def decorador(funcion: Callable) -> Callable:
    def funcionModificada() -> None:
        print("Antes de ejecutar la funcion",end="\n", file = stdout)
        funcion()
        print("Despues de ejecutar la funcion",end="\n", file = stdout)
        return None
    return funcionModificada


def saludo() -> None:
    print("Hola Daniel",end="\n", file = stdout)
    return None

saludo_modificado: Callable = decorador(funcion=saludo)
saludo_modificado()

# Manera mas facil de entender los decoradores pero no es la mas optima
