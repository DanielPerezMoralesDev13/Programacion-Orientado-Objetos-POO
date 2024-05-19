#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me 

class Persona:
    def __init__(self: 'Persona', nombre: str, edad: int, nacionalidad: str) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.nacionalidad: str = nacionalidad
        return None

    def Hablar(self: 'Persona') -> str:
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y soy {self.nacionalidad}"

class Artista:
    def __init__(self: 'Artista', habilidad: str) -> None:
        self.habilidad: str = habilidad

    def mostrarHabilidad(self: 'Artista') -> str:
        return f"Mi habilidad es {self.habilidad}"


class EmpleadoArtista(Persona, Artista):
    def __init__(
        self: 'EmpleadoArtista',
        nombre: str,
        edad: int,
        nacionalidad: str,
        habilidad: str,
        salario: float,
        empresa: str,
    ) -> None:
        # En este caso, la clase EmpleadoArtista hereda los atributos de las clases Persona y Artista.

        # pero no podemos usar super().__init__() tenemos que usar el nombre de la clase y pasar los atributos de las clases padre y pasarle el self.

        Persona.__init__(self = self, nombre = nombre, edad = edad, nacionalidad = nacionalidad)

        Artista.__init__(self = self, habilidad = habilidad)

        self.salario: float = salario
        self.empresa: str = empresa
        return None

    def presentarseSuper(self: 'EmpleadoArtista') -> str:
        return f"{super().mostrarHabilidad()}"

    # al hacer super().Hablar() estamos accediendo al metodo Hablar de la clase padre no de la clase hija.

    def presentarseSelf(self: 'EmpleadoArtista') -> str:
        return f"{self.mostrarHabilidad()}"

    # y cuando hacemos self.mostrarHabilidad() estamos accediendo al metodo mostrarHabilidad de la clase hija no de la clase padre.

    def mostrarHabilidad(self: 'EmpleadoArtista') -> str:
        return "No tengo habilidad"

    # si nosotros creamos un metodo con el mismo nombre de un metodo de una clase padre, el metodo de la clase hija va a tener prioridad.
    def presentarseOne(self: 'EmpleadoArtista') -> str:
        return f"Hola, mi nombre es {self.nombre} y mi habilidad es {self.mostrarHabilidad()} y tengo {self.edad} años y soy {self.nacionalidad} y trabajo en {self.empresa} y gano {self.salario}"

    def presentarseTwo(self: 'EmpleadoArtista') -> str:
        return f"Hola, mi nombre es {self.nombre} y {super().mostrarHabilidad()} y tengo {self.edad} años y soy {self.nacionalidad} y trabajo en {self.empresa} y gano {self.salario} dolares al mes"


Daniel = EmpleadoArtista(
    nombre="Daniel",
    edad=20,
    nacionalidad="Nicaraguense",
    habilidad="Cantar",
    salario=1000000,
    empresa="Google",
)

print(Daniel.presentarseSuper(),end = "\n")
print(Daniel.presentarseSelf(),end = "\n")
print(Daniel.presentarseTwo(),end = "\n")
