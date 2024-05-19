#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me
"""
Duck Typing es un concepto en Python que se refiere a la idea de que no importa el tipo de objeto con el que estás trabajando, sino qué operaciones o comportamientos puedes hacer con él. Si un objeto se comporta como un pato (es decir, tiene los mismos métodos y propiedades), entonces puedes tratarlo como un pato.
"""


class Pato:
    def __init__(self: 'Pato') -> None:
        return None

    def hablar(self: 'Pato') -> str:
        return "¡Cuac!"


class Perro:
    def __init__(self: 'Perro') -> None:
        return None

    def hablar(self: 'Perro') -> str:
        return "¡Guau!"


def hacerHablar(Animal: Pato | Perro):
    # No importa el tipo de 'Animal' mientras tenga un método 'hablar'
    print(Animal.hablar(),end="\n")


pato: Pato = Pato()
perro: Perro = Perro()

# Aunque 'pato' y 'perro' son de diferentes tipos,
# ambos tienen un método 'hablar', por lo que podemos usarlos
# de manera intercambiable en la función 'hacerHablar'

hacerHablar(Animal = pato)  # Imprime: ¡Cuac!
hacerHablar(Animal = perro)  # Imprime: ¡Guau!

# En este ejemplo, la función hacerHablar puede tomar cualquier objeto que tenga un método hablar. No importa si el objeto es un Pato o un Perro, siempre que tenga un método hablar, se puede usar en hacerHablar. Esto es Duck Typing.
