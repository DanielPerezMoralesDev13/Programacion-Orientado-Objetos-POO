#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

from typing import Callable

# Este tipo de decorador se le conoce como decorador de funcion
def decorador(funcion: Callable) -> Callable:
    def funcionModificada() -> None:
        print("Antes de ejecutar la funcion")
        funcion()
        print("Despues de ejecutar la funcion")
        return None

    return funcionModificada


@decorador
def saludo() -> None:
    print("Hola Daniel")

# Mofiicamos la funcion saludo con el decorador
saludo()

# Manera mas optima de usar los decoradores
