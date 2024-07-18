#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me 

# la herencia en Programacion orientado a objetos, es cuando una clase hereda los atributos y metodos de otra clase, esto nos permite reutilizar codigo, y no tener que escribir el mismo codigo una y otra vez.

# la clase super clase o super padre, es la clase que hereda sus atributos y metodos a las subclases o clases hijas. tambien se le conoce como clase padre o clase base.

"""
Existen 3 tipos de herencia: 

>>> Herencia Simple: Cuando Una Clase Hereda Los Atributos Y Metodos De Una Sola Clase.

Ejemplo grafico con caracteres ASCII:

    -----------------
    |    Persona    |
    -----------------
           |
           |
           |
    -----------------
    |    Empleado   |
    -----------------


>>> Herencia Jerarquica: Es Cuando Varias Clases Heredan Los Atributos Y Metodos De Una Sola Clase.

Ejemplo grafico con caracteres ASCII:
                        -----------------
                        |    Persona    |
                        -----------------
                                |
                                |
            ------------------------------------
            |                  |               |
            |                  |               |
    -----------------  -----------------  ----------- 
    |    Emplado    |  |   Estudiante  |  |   Jefe  |
    -----------------  -----------------  -----------
    
    
>>> Herencia Multiple: Es Cuando Una Clase Hereda Los Atributos Y Metodos De Varias Clases.
"""


from sys import stdout


class Persona:
    def __init__(self: 'Persona', nombre: str, edad: int, nacionalidad: str) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.nacionalidad: str = nacionalidad
        return None


    def hablar(self: 'Persona') -> str: return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y soy {self.nacionalidad}"


class Empleado(Persona):
    # para heredar los atributos de la clase padre, solo se debe pasar la clase padre como parametro en la clase hija.

    # en este caso, la clase Empleado hereda los atributos de la clase Persona.

    # tambien se pueden agregar nuevos atributos a la clase hija.

    """
    Los atributos de la clase padre son: nombre, edad y nacionalidad.
    y los de la clase hija son: trabajo y salario.
    """

    def __init__(
        self: 'Empleado',
        nombre: str,
        edad: int,
        nacionalidad: str,
        trabajo: str,
        salario: float,
    ) -> None:
        # para heredar los atributos de la clase padre, se debe usar la funcion super() y pasar los atributos de la clase padre no es necesario pasar el self.

        super().__init__(nombre = nombre, edad = edad, nacionalidad = nacionalidad)
        self.trabajo: str = trabajo
        self.salario: float = salario
        return None

    # se pueden sobre escribir metodos de la clase padre, en la clase hija.

    def hablar(self: 'Persona') -> str: return f"No quiero hablar con nadie"

    # aqui se sobre escribio el metodo hablar de la clase padre, en la clase hija.

    # tambien se pueden sobre escribir los atributos de la clase padre, en la clase hija.

    # el ejemplo de este fichero es herencia simple, ya que la clase Empleado hereda los atributos de la clase Persona.


daniel: Empleado = Empleado(
    nombre = "Daniel",
    edad = 18,
    nacionalidad = "Nicaraguense",
    trabajo = "Programador",
    salario = 1000.00,
)

print(daniel.nacionalidad,end = "\n", file = stdout)
print(daniel.hablar(),end = "\n", file = stdout)
