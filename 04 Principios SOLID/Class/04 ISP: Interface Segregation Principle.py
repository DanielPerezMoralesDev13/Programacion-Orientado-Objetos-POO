#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

"""
"ISP": "Interface Segregation Principle" Significa en español Principio de segregacion de interfaces. 

Este principio dice que una clase no debe depender de metodos que no usa. Es decir que una clase no debe depender de metodos que no usa para que sea facil de mantener y de cambiar.

Este principio se puede aplicar en lenguajes de programacion que no tienen interfaces como Python. En Python se puede aplicar este principio con clases abstractas.

Este principio nos permite que los usuario no dependan de metodos que no usan. Es decir que los usuario no dependan de metodos que no usan para que sea facil de mantener y de cambiar.
"""

"""
from abc import ABC, abstractmethod


class Trabajador(ABC):
    @abstractmethod
    def __init__(self: 'Trabajador') -> None:
        return None

    @abstractmethod
    def comer(self: 'Trabajador') -> None:
        return None

    @abstractmethod
    def trabajar(self: 'Trabajador') -> None:
        return None

    @abstractmethod
    def dormir(self: 'Trabajador') -> None:
        return None


class Humano(Trabajador):
    def __init__(self: 'Humano') -> None:
        return None

    def comer(self: 'Humano') -> str:
        return "Estoy comiendo"

    def trabajar(self: 'Humano') -> str:
        return "Estoy trabajando"

    def dormir(self: 'Humano') -> str:
        return "Estoy durmiendo"


class Robot(Trabajador):
    def __init__(self: object) -> None:
        return None

    def comer(self: object) -> None:
        return None

    def trabajar(self: object) -> str:
        return "El robot esta trabajando"

    def dormir(self: object) -> None:
        return None


robot: Trabajador = Robot()

"""

"""
Este codigo no se puede ejecutar porque la clase Robot no tiene el metodo comer y dormir.
Esto viola el principio de segregacion de interfaces porque la clase Robot depende de metodos que no usa.
Para solucionar este problema se puede crear una clase abstracta que tenga los metodos comer y dormir y que las clases Humano y Robot hereden de la clase abstracta.
"""

from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def __init__(self: 'Trabajador') -> None:
        return None

    @abstractmethod
    def trabajar(self: 'Trabajador') -> str | None:
        return None

class Comedor(ABC):
    @abstractmethod
    def __init__(self: 'Comedor') -> None:
        return None

    @abstractmethod
    def comer(self: 'Comedor') -> str | None:
        return None


class Dormidor(ABC):
    @abstractmethod
    def __init__(self: 'Dormidor') -> None:
        return None

    @abstractmethod
    def dormir(self: 'Dormidor') -> str | None:
        return None

class Humano(Trabajador, Comedor, Dormidor):
    def __init__(self: 'Humano') -> None:
        Trabajador.__init__(self = self)
        Comedor.__init__(self = self)
        Dormidor.__init__(self = self)
        return None

    def comer(self: 'Humano') -> str | None:
        return "El humano comiendo"

    def trabajar(self: object) -> str | None:
        return "El humano esta trabajando"

    def dormir(self: object) -> str | None:
        return "El humano durmiendo"

class Robot(Trabajador):
    def __init__(self: 'Robot') -> None:
        return None

    def trabajar(self: 'Robot') -> str | None:
        return "El robot esta trabajando"


humano: Humano = Humano()
print(humano.trabajar(),end="\n")
print(humano.comer(),end="\n")
print(humano.dormir(),end="\n")

robot: Trabajador = Robot()
print(robot.trabajar(),end="\n")
try: print(robot.comer(),end="\n")  # !Da error porque la clase Robot no tiene el metodo comer
except AttributeError as e:
    print(e,end="\n")


"""
Este la manera correcta de aplicar el principio de segregacion de interfaces.
Ya que la clase Robot no depende de metodos que no usa.
Se creo una clase abstracta para los metodos comer y dormir.
Esto para que la clase Robot no dependa de metodos que no usa.
"""
