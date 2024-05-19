#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

"""
El encapsulamiento es un mecanismo que permite restringir el acceso a métodos y variables de un objeto, evitando que se puedan manipular por fuera de la clase.

El guion bajo es una convención utilizada para indicar que un atributo o método es privado en Python. Sin embargo, es importante tener en cuenta que esta convención no impide el acceso a estos elementos desde fuera de la clase. El encapsulamiento en Python se basa en la convención y en la responsabilidad del programador de no acceder directamente a los atributos o métodos privados desde fuera de la clase.

Existe 3 tipos de encapsulamiento:

>>> - Publico: Cualquier atributo o método puede ser llamado desde cualquier parte, ya sea dentro de la clase o fuera de ella. Este es el comportamiento por defecto en Python

>>> - Protegido: Los atributos o métodos solo pueden ser llamados dentro de la clase o de sus subclases. Para definir un atributo o método como protegido se debe escribir el nombre del atributo o método iniciando con un guion bajo.

>>> - Privado: Los atributos o métodos solo pueden ser llamados dentro de la clase. Para definir un atributo o método como privado se debe escribir el nombre del atributo o método iniciando con dos guiones bajos.

Las ventajas del encapsulamiento son: 

>>> - Evitar que los atributos o métodos sean llamados desde cualquier parte del programa, lo cual puede llevar a comportamientos inesperados.

>>> - Dar un control más estricto sobre cómo se manipulan los datos de una clase.

>>> - Facilitar la modificación de la implementación interna de una clase sin afectar 
el resto del programa.

>>> - Ayudar a proteger la integridad de los datos de una clase.

>>> - Ocultar la complejidad al usuario de una clase, mostrando solo los métodos que son necesarios para interactuar con dicha clase.
"""

# Para poder ejecutar metodo privado desde fuera de la clase se debe crear un metodo publico o protegido que llame al metodo privado


class MiClase:
    def __init__(self: 'MiClase') -> None:
        self.atributo_publico: str = "Soy un atributo publico"
        self._atributo_protegido: str = "Soy un atributo protegido"
        self.__atributo_privado: str = "Soy un atributo inalcanzable desde fuera de la clase"
        return None

    def metodoPublico(self: 'MiClase') -> str:
        return "Soy un metodo publico"

    def _metodoProtegido(self: 'MiClase') -> str:
        return "Soy un metodo protegido"

    def __metodoPrivado(self: 'MiClase') -> str:
        return "Soy un metodo inalcanzable desde fuera de la clase"

    def getFuncionMetodoPrivado(self: 'MiClase') -> str:
        return self.__metodoPrivado()


objeto: MiClase = MiClase()
print(objeto.getFuncionMetodoPrivado(),end="\n") # se puede acceder a un metodo privado mediante un metodo publico
print(objeto.atributo_publico,end="\n")  # se puede acceder a un atributo publico
print(objeto._atributo_protegido,end="\n")  # se puede acceder a un atributo protegido
# print(objeto.__atributo_privado) # no se puede acceder a un atributo privado

print(objeto.metodoPublico(),end="\n")  # se puede acceder a un metodo publico
print(objeto._metodoProtegido(),end="\n")  # se puede acceder a un metodo protegido
# print(objeto.__metodoprivado(),end="\n") # no se puede acceder a un metodo privado
