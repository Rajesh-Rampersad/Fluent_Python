# Importamos la biblioteca math para usar math.hypot
import math

# Definimos la clase Vector
class Vector:
    # Constructor de la clase Vector
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Método especial __repr__ para representar la instancia como una cadena
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    # Método especial __abs__ para calcular el valor absoluto del vector
    def __abs__(self):
        return math.hypot(self.x, self.y)

    # Método especial __bool__ para determinar si el vector es verdadero o falso
    def __bool__(self):
        return bool(abs(self))

# Ejemplo de uso de la clase Vector
if __name__ == "__main__":
    # Crear instancias de Vector
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)

    # Realizar una operación de adición
    resultado_suma = v1 + v2
    print(resultado_suma)  # Imprime: Vector(4, 5)

    # Calcular el valor absoluto de un vector
    v = Vector(3, 4)
    valor_absoluto = abs(v)
    print(valor_absoluto)  # Imprime: 5.0

    # Realizar una multiplicación escalar
    resultado_multiplicacion = v * 3
    print(resultado_multiplicacion)  # Imprime: Vector(9, 12)

    # Calcular el valor absoluto del resultado de la multiplicación
    valor_absoluto_multiplicacion = abs(v * 3)
    print(valor_absoluto_multiplicacion)  # Imprime: 15.0
