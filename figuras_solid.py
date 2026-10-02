import math

class Circulo:
    def __init__(self, radio: float):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor a cero.")
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * self.radio ** 2

class Rectangulo:
    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("Las dimensiones deben ser mayores a cero.")
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

if __name__ == "__main__":
    c = Circulo(5)
    r = Rectangulo(4, 6)
    print(f"Área Círculo (SOLID): {c.calcular_area():.2f}")
    print(f"Área Rectángulo (SOLID): {r.calcular_area():.2f}")